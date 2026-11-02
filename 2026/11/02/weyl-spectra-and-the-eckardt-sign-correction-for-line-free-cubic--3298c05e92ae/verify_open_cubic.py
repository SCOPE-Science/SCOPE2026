#!/usr/bin/env python3
"""Exact verification of Frobenius and Eckardt corrections for cubic-surface open loci.

Only Python 3 standard-library modules are required. No finite-field packages.
"""
from collections import Counter, deque, defaultdict
from itertools import combinations
from math import lcm
import csv, sys

N = 6
E = [(0,) + tuple(int(i == j) for j in range(N)) for i in range(N)]
L = [(1,) + tuple(-int(k in (i,j)) for k in range(N)) for i,j in combinations(range(N),2)]
Q = [(2,) + tuple(-int(k != i) for k in range(N)) for i in range(N)]
V = E + L + Q
assert len(V) == len(set(V)) == 27
index = {v:i for i,v in enumerate(V)}

def dot(a,b): return a[0]*b[0]-sum(a[i]*b[i] for i in range(1,7))
def refl(v, r):
    t = dot(v,r)
    return tuple(v[i]+t*r[i] for i in range(7))
roots = [tuple(0 if j == 0 else (1 if j == i else (-1 if j == i+1 else 0)) for j in range(7)) for i in range(1,6)]
roots.append((1,-1,-1,-1,0,0,0))
generators = [tuple(index[refl(v,r)] for v in V) for r in roots]
assert all(dot(r,r)==-2 for r in roots)
assert all(all(g[g[i]]==i for i in range(27)) for g in generators)
identity=tuple(range(27))
def mul(a,b): return tuple(a[b[i]] for i in range(len(a)))

def group():
    seen={identity:0}; elements=[identity]; todo=deque([identity])
    while todo:
        a=todo.popleft()
        for s in generators:
            b=mul(s,a)
            if b not in seen:
                seen[b]=len(elements); elements.append(b); todo.append(b)
    assert len(elements)==51840
    return elements,seen

edges=[(i,j) for i,j in combinations(range(27),2) if dot(V[i],V[j])==1]
assert len(edges)==135
assert Counter(i for e in edges for i in e)==Counter({i:10 for i in range(27)})
edge_index={e:i for i,e in enumerate(edges)}
flags=[(i,k) for k,(i,j) in enumerate(edges) for i in (i,j)]
flag_index={f:i for i,f in enumerate(flags)}
assert len(flags)==270

def induced(g):
    eg=tuple(edge_index[tuple(sorted((g[i],g[j])))] for i,j in edges)
    fg=tuple(flag_index[(g[i],eg[k])] for i,k in flags)
    return eg,fg

def orbit_lengths(g):
    vis=set(); a=[]
    for i in range(len(g)):
        if i not in vis:
            j=i;d=0
            while j not in vis:vis.add(j);j=g[j];d+=1
            a.append(d)
    return sorted(a,reverse=True)

def orbits_str(g):
    c=Counter(orbit_lengths(g))
    return ','.join(str(d)+':'+str(c[d]) for d in sorted(c))

def pic_matrix(g):
    # H=L_{01}+E_0+E_1; ordered basis is (H,E_0,...,E_5).
    H=tuple(V[g[6]][i]+V[g[0]][i]+V[g[1]][i] for i in range(7))
    cols=[H]+[V[g[i]] for i in range(6)]
    return [[cols[j][i] for j in range(7)] for i in range(7)]

def matmul(a,b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def mattrace(a):return sum(a[i][i] for i in range(len(a)))

def charpoly(a):
    # Faddeev-LeVerrier/Newton identities, exact integer divisions.
    m=len(a); b=a; traces=[]
    for j in range(m):
        traces.append(mattrace(b)); b=matmul(b,a)
    coeff=[1]
    for k in range(1,m+1):
        z=-sum(coeff[k-i]*traces[i-1] for i in range(1,k+1))
        assert z%k==0
        coeff.append(z//k)
    return coeff

def pictrace(g):return mattrace(pic_matrix(g))

def fixed_data(g):
    fixed={i for i in range(27) if g[i]==i}
    ff=sum(i in fixed and j in fixed for i,j in edges)
    sw=sum(g[i]==j and g[j]==i for i,j in edges)
    eg,fg=induced(g)
    assert sum(eg[i]==i for i in range(135)) == ff+sw
    assert sum(fg[i]==i for i in range(270)) == 2*ff
    return pictrace(g),len(fixed),ff,sw

def classes(elements,lookup):
    remaining=set(range(51840)); out=[]
    while remaining:
        start=next(iter(remaining)); subset={start};queue=[start]
        while queue:
            a=elements[queue.pop()]
            for s in generators:
                b=lookup[mul(s,mul(a,s))]
                if b not in subset:subset.add(b);queue.append(b)
        remaining-=subset
        out.append((start,len(subset)))
    out.sort(key=lambda z:(orbit_lengths(elements[z[0]]),fixed_data(elements[z[0]])),reverse=False)
    assert len(out)==25 and sum(z[1] for z in out)==51840
    return out

# Independent comparison with the published 25-class Weyl-table columns:
# (conjugacy-class size, element order, trace on the Picard group).
published=[(4320,12,0),(720,6,2),(80,3,-2),(5760,9,1),
(1440,6,-1),(4320,12,2),(6480,8,1),(1440,6,2),(540,4,-1),
(540,4,3),(45,2,-1),(5184,10,0),(1440,6,-1),(2160,6,0),
(4320,6,1),(5184,5,2),(3240,4,1),(480,3,1),(1620,4,3),
(1440,6,2),(540,2,1),(240,3,4),(270,2,3),(36,2,5),(1,1,7)]

def row_table():
    elements,lookup=group()
    cl=classes(elements,lookup)
    rows=[]; observed=[]; zeta_signatures=[]
    for num,(start,size) in enumerate(cl,1):
        g=elements[start];c=orbit_lengths(g); order=lcm(*c)
        trace,fl,ff,sw=fixed_data(g)
        eg,fg=induced(g)
        coeff=charpoly(pic_matrix(g))
        assert coeff[1]==-trace
        a=trace-fl;b=1-fl+ff-sw
        row={'class':num,'class_size':size,'element_order':order,
             'lines_cycle_type':str(tuple(c)),'pic_trace':trace,
             'fixed_lines':fl,'fixed_edges_both_fixed':ff,
             'fixed_edges_swapped':sw,'open_q_coefficient':a,
             'open_constant':b,'line_orbits':orbits_str(g),
             'edge_orbits':orbits_str(eg),'branch_orbits':orbits_str(fg),
             'pic_det_coeffs':str(tuple(coeff))}
        rows.append(row);observed.append((size,order,trace))
        # Two independent methods: raw Frobenius powers and orbit-length formula.
        signature=[]
        for n in range(1,25):
            h=identity
            for _ in range(n):h=mul(h,g)
            tr,fln,ffn,swn=fixed_data(h)
            direct=(tr-fln,1-fln+ffn-swn)
            from_orbits=lambda x:sum(d for d in orbit_lengths(x) if n%d==0)
            ecount=from_orbits(eg);fcount=from_orbits(fg);lcount=from_orbits(g)
            M=pic_matrix(g);power=[[int(i==j) for j in range(7)] for i in range(7)]
            for _ in range(n):power=matmul(power,M)
            independent=(mattrace(power)-lcount,1-lcount+fcount-ecount)
            assert direct==independent,(num,n,direct,independent)
            signature.append(direct)
        zeta_signatures.append(tuple(signature))
    assert Counter(observed)==Counter(published)
    assert len(set((r['open_q_coefficient'],r['open_constant']) for r in rows))==15
    assert len(set(zeta_signatures))==25
    # At q>=8 each of the 25 formal zetas remains distinct. Small q may collide.
    for q,expected in [(2,25),(3,23),(4,25),(5,23),(6,23),(7,22),(8,25),(9,25),(17,25)]:
        assert len({tuple(q*a+b for a,b in s) for s in zeta_signatures})==expected
    return rows

# Two independent split blow-up examples in characteristic 17.
def plane(p):
    return [(x,y,1) for x in range(p) for y in range(p)]+[(x,1,0) for x in range(p)]+[(1,0,0)]
def det3(vs,p):
    (a,b,c),(d,e,f),(g,h,i)=vs
    return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%p

def kernel1(mat,p):
    a=[[v%p for v in row] for row in mat]
    rank=0;piv=[]
    for j in range(len(a[0])):
        t=next((i for i in range(rank,len(a)) if a[i][j]),None)
        if t is None:continue
        a[rank],a[t]=a[t],a[rank]
        k=pow(a[rank][j],-1,p)
        a[rank]=[(k*v)%p for v in a[rank]]
        for i in range(len(a)):
            if i==rank:continue
            k=a[i][j];a[i]=[(v-k*w)%p for v,w in zip(a[i],a[rank])]
        piv.append(j);rank+=1
        if rank==len(a):break
    free=[i for i in range(len(a[0])) if i not in piv]
    if not free:return []
    v=[0]*len(a[0]);v[free[0]]=1
    for i,j in enumerate(piv):v[j]=(-a[i][free[0]])%p
    return v

def cmon(x):
    a,b,c=x;return (a*a,b*b,c*c,a*b,a*c,b*c)

def secant(x,y,p):
    a,b,c=x;d,e,f=y
    return ((b*f-c*e)%p,(c*d-a*f)%p,(a*e-b*d)%p)

def projectivize(v,p):
    for x in v:
        if x%p:
            k=pow(x,-1,p);return tuple((w*k)%p for w in v)
    raise ValueError('zero vector')

def split_example(six,p=17):
    assert len(six)==6 and len(set(six))==6
    assert all(det3([six[i],six[j],six[k]],p)!=0 for i,j,k in combinations(range(6),3))
    assert not kernel1([cmon(t) for t in six],p)
    lines=[secant(six[i],six[j],p) for i,j in combinations(range(6),2)]
    conics=[kernel1([cmon(six[j]) for j in range(6) if j!=i],p) for i in range(6)]
    assert len(set(map(lambda t:projectivize(t,p),lines)))==15
    assert len(set(map(lambda t:projectivize(t,p),conics)))==6
    eq=[lambda z,l=l:sum(a*b for a,b in zip(l,z))%p for l in lines]
    eq +=[lambda z,c=c:sum(a*b for a,b in zip(c,cmon(z)))%p for c in conics]
    off=0;eck_plane=0
    for z in plane(p):
        r=sum(f(z)==0 for f in eq)
        if r==0:off+=1
        if z not in six:
            assert r<=3
            if r==3:eck_plane+=1
    # The other possible triple concurrences lie on one of the six exceptional curves.
    eck_exceptional=0
    for z in six:
        tangent=[]
        for l in lines:
            if sum(a*b for a,b in zip(l,z))%p==0:tangent.append(projectivize(l,p))
        for a,b,c,d,e,f in conics:
            if (a*z[0]**2+b*z[1]**2+c*z[2]**2+d*z[0]*z[1]+e*z[0]*z[2]+f*z[1]*z[2])%p==0:
                grad=(2*a*z[0]+d*z[1]+e*z[2],2*b*z[1]+d*z[0]+f*z[2],2*c*z[2]+e*z[0]+f*z[1])
                tangent.append(projectivize(grad,p))
        assert len(tangent)==10
        multiplicity=Counter(tangent)
        assert max(multiplicity.values())<=2
        eck_exceptional+=sum(v==2 for v in multiplicity.values())
    assert off == p*p-20*p+109-eck_plane-eck_exceptional
    return off,eck_plane,eck_exceptional


def run(table_path=None):
    rows=row_table()
    if table_path:
        with open(table_path,'w',encoding='utf-8',newline='') as h:
            writer=csv.DictWriter(h,fieldnames=list(rows[0]),lineterminator='\n');writer.writeheader();writer.writerows(rows)
    common=[(1,0,0),(0,1,0),(0,0,1),(1,1,1),(2,3,1)]
    a=split_example(common+[(6,4,1)])
    b=split_example(common+[(3,7,1)])
    assert a==(57,0,1),(a,b)
    assert b==(55,1,2),(a,b)
    print('W(E6): 51840 elements; 25 conjugacy classes; 15 first-field polynomials; 25 formal zeta signatures')
    print('Two independent split F17 six-point blow-ups:',a,b)
    print('Split baseline at q=17: 58; Eckardt corrections: -1, -3')
    print('VERIFY_OK')

if __name__=='__main__':
    run(sys.argv[2] if len(sys.argv)==3 and sys.argv[1]=='--write-table' else None)
