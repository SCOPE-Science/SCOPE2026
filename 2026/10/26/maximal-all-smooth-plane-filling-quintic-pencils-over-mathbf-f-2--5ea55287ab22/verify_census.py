"""Exact classification of all-smooth binary plane-filling quintic pencils.

Requires Python 3 and SymPy. All field operations in enumeration are over F_2.
No sampling or extension-field cutoff is used for geometric smoothness.
"""
import collections
import itertools
import json
import sympy as sp

MON = [(a,b,5-a-b) for a in range(5,-1,-1) for b in range(5-a,-1,-1)]
PTS = [p for p in itertools.product((0,1),repeat=3) if any(p)]
X,Y,Z = sp.symbols('X Y Z')
VAR = (X,Y,Z)
MON_EXPR = [X**a*Y**b*Z**c for a,b,c in MON]


def value(e,p):
    return int(all(t == 0 or v == 1 for t,v in zip(e,p)))


def jet_rows():
    rows=[]
    for p in PTS:
        rows.append(sum(value(e,p)<<i for i,e in enumerate(MON)))
    for p in PTS:
        radial=p.index(1)
        for j in range(3):
            if j == radial:
                continue
            r=0
            for i,e in enumerate(MON):
                if e[j] & 1:
                    de=tuple(e[k]-int(k==j) for k in range(3))
                    r ^= value(de,p)<<i
            rows.append(r)
    return rows


def inverse_columns(rows):
    assert len(rows)==21
    left=rows[:]
    right=[1<<i for i in range(21)]
    for i in range(21):
        j=next((j for j in range(i,21) if (left[j]>>i)&1),None)
        assert j is not None, 'first-jet matrix must have full rank'
        left[i],left[j]=left[j],left[i]
        right[i],right[j]=right[j],right[i]
        for k in range(21):
            if k!=i and (left[k]>>i)&1:
                left[k]^=left[i]
                right[k]^=right[i]
    assert left==[1<<i for i in range(21)]
    return [sum(((right[i]>>j)&1)<<i for i in range(21)) for j in range(21)]


def form(jet,cols):
    ans=0
    for j in range(21):
        if (jet>>j)&1:
            ans^=cols[j]
    return ans


def all_local_forms(cols):
    for digits in itertools.product((1,2,3),repeat=7):
        jet=sum(d<<(7+2*i) for i,d in enumerate(digits))
        yield form(jet,cols)


def multiply(a,b):
    c={}
    for u in a:
        for v in b:
            e=tuple(u[i]+v[i] for i in range(3))
            if e in c:
                del c[e]
            else:
                c[e]=1
    return c


def projective_matrices():
    for rows in itertools.product(range(1,8),repeat=3):
        a,b,c=rows
        if len({a,b,c})==3 and a^b!=c:
            yield rows


def substituted_monomials(rows):
    powers=[]
    for t in rows:
        v={tuple(int(j==i) for j in range(3)):1 for i in range(3) if (t>>(2-i))&1}
        p=[{(0,0,0):1}]
        for _ in range(5):
            p.append(multiply(p[-1],v))
        powers.append(p)
    idx={e:i for i,e in enumerate(MON)}
    return [sum(1<<idx[e] for e in multiply(multiply(powers[0][a],powers[1][b]),powers[2][c]))
            for a,b,c in MON]


def transform(w,table):
    z=0
    while w:
        low=w&-w
        z^=table[low.bit_length()-1]
        w^=low
    return z


def expr(w):
    return sum(MON_EXPR[i] for i in range(21) if (w>>i)&1)


def geometric_smooth(w):
    f=expr(w)
    gradients=[sp.diff(f,v) for v in VAR]
    for c in range(3):
        affine=[v for j,v in enumerate(VAR) if j!=c]
        polynomials=[g.subs({VAR[c]:1}) for g in gradients]
        if list(sp.groebner(polynomials,*affine,order='lex',modulus=2))!=[1]:
            return False
    return True


def base_reduced(a,b):
    f,g=expr(a),expr(b)
    for c in range(3):
        affine=[v for j,v in enumerate(VAR) if j!=c]
        u,v=affine
        ff=f.subs({VAR[c]:1})
        gg=g.subs({VAR[c]:1})
        jac=sp.diff(ff,u)*sp.diff(gg,v)-sp.diff(ff,v)*sp.diff(gg,u)
        if list(sp.groebner([ff,gg,jac],u,v,order='lex',modulus=2))!=[1]:
            return False
    return True


def compute():
    rows=jet_rows()
    cols=inverse_columns(rows)
    local=set(all_local_forms(cols))
    assert len(local)==2187
    matrices=[substituted_monomials(a) for a in projective_matrices()]
    assert len(matrices)==168 and len({tuple(a) for a in matrices})==168
    unvisited=set(local)
    form_orbits=[]
    while unvisited:
        f=min(unvisited)
        orbit={transform(f,t) for t in matrices}
        assert orbit<=unvisited
        form_orbits.append((f,len(orbit),orbit))
        unvisited-=orbit
    assert len(form_orbits)==18
    smooth=set().union(*(orbit for f,n,orbit in form_orbits if geometric_smooth(f)))
    assert len(smooth)==1512
    pairs=[]
    members=sorted(smooth)
    for i,f in enumerate(members):
        for g in members[i+1:]:
            if (f^g) in smooth:
                pairs.append((f,g))
    assert len(pairs)==50400
    pencils={tuple(sorted((f,g,f^g))) for f,g in pairs}
    assert len(pencils)==16800
    missing=set(pencils)
    orbit_data=[]
    while missing:
        pencil=min(missing)
        orbit={tuple(sorted(transform(f,t) for f in pencil)) for t in matrices}
        assert orbit<=missing
        orbit_data.append({'member_masks':list(pencil),'orbit_size':len(orbit),
                           'reduced_base':base_reduced(pencil[0],pencil[1])})
        missing-=orbit
    assert len(orbit_data)==108
    spectrum=collections.Counter((o['orbit_size'],o['reduced_base']) for o in orbit_data)
    assert spectrum=={(168,True):93,(168,False):3,(56,True):9,(56,False):3}
    assert sum(o['orbit_size'] for o in orbit_data)==16800
    return {'monomial_order':MON,'point_order':PTS,'jet_matrix_rank':21,
            'locally_smooth_forms':len(local),'locally_smooth_orbits':len(form_orbits),
            'geometrically_smooth_forms':len(smooth),'smooth_form_orbits':sum(geometric_smooth(f) for f,_,_ in form_orbits),
            'smooth_pairs':len(pairs),'all_smooth_pencils':len(pencils),
            'pencil_orbits':len(orbit_data),'orbit_size_spectrum':dict(collections.Counter(o['orbit_size'] for o in orbit_data)),
            'reduced_base_pencils':sum(o['orbit_size'] for o in orbit_data if o['reduced_base']),
            'nonreduced_base_pencils':sum(o['orbit_size'] for o in orbit_data if not o['reduced_base']),
            'reduced_base_orbits':sum(o['reduced_base'] for o in orbit_data),
            'nonreduced_base_orbits':sum(not o['reduced_base'] for o in orbit_data),
            'orbit_representatives':orbit_data}


if __name__=='__main__':
    print(json.dumps(compute(),sort_keys=True,separators=(',',':')))
