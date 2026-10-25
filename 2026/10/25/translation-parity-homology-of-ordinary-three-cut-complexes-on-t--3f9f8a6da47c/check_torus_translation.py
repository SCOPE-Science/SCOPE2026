"""Exact finite rational-model checks for translation-twisted graph cut homology.

Run: python check_torus_translation.py
Only finite checks are made; the accompanying proof covers all m,n>=5.
"""
from itertools import combinations
from fractions import Fraction

def parity(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

def rank(columns):
    # Sparse exact rational Gaussian elimination, not a finite-field calculation.
    piv={}
    for v in columns:
        w={r:Fraction(x) for r,x in v.items() if x}
        while w:
            k=max(w)
            if k not in piv:
                z=w[k]
                piv[k]={r:x/z for r,x in w.items()}
                break
            a=w[k]
            for r,x in piv[k].items():
                y=w.get(r,0)-a*x
                if y: w[r]=y
                elif r in w: del w[r]
    return len(piv)

def complex_faces(m,n):
    N=m*n
    v=lambda x,y: (x%m)*n+(y%n)
    edge=lambda a,b: (min(a,b),max(a,b))
    E=set();T=set();Q=set()
    for x in range(m):
      for y in range(n):
        a=v(x,y);nbr=[v(x+1,y),v(x-1,y),v(x,y+1),v(x,y-1)]
        for b in nbr:E.add(edge(a,b))
        for b,c in combinations(nbr,2):T.add(tuple(sorted((a,b,c))))
        Q.add(tuple(sorted([v(x,y),v(x+1,y),v(x,y+1),v(x+1,y+1)])))
    assert len(E)==2*N and len(T)==6*N and len(Q)==N
    return [ [(i,) for i in range(N)], list(combinations(range(N),2)),sorted(T),sorted(Q) ]

def trans(m,n,a,b,face):
    img=tuple(((x+a)%m)*n+(y+b)%n for x,y in (divmod(t,n) for t in face))
    return tuple(sorted(img)), parity(img)

def all_trans(m,n):return list((a,b) for a in range(m) for b in range(n))

def globalsign(m,n,a,b):
    perm=[((x+a)%m)*n+(y+b)%n for x in range(m) for y in range(n)]
    return parity(perm)

def invariant_complex(m,n,twisted=False):
    fs=complex_faces(m,n); ts=all_trans(m,n); N=m*n
    glob={(a,b):globalsign(m,n,a,b) if twisted else 1 for a,b in ts}
    # For each degree, form exactly one orbit-sum generator per admissible face orbit.
    cells=[];coeff_maps=[]; sizes=[]
    for p,faces in enumerate(fs):
        visited=set();basis=[];cm={}
        for face in faces:
            if face in visited:continue
            orbits={}
            for a,b in ts:
                im,os=trans(m,n,a,b,face)
                factor=os*glob[a,b]
                if im in orbits and orbits[im]!=factor:
                    orbits[im]=None
                elif im not in orbits:
                    orbits[im]=factor
            visited.update(orbits)
            if None in orbits.values():continue
            j=len(basis);basis.append(face)
            for im,fac in orbits.items():cm[im]=(j,fac)
        cells.append(basis);coeff_maps.append(cm);sizes.append(len(basis))
    ranks=[]; maps=[]
    for p in (1,2,3):
        lower_rep_index={face:i for i,face in enumerate(cells[p-1])}
        columns=[]
        for face in cells[p]:
            # The coefficient of target orbit representative in the boundary
            # of the invariant sum is determined by all images of this simplex.
            orbit={}
            for a,b in ts:
                im,os=trans(m,n,a,b,face)
                fac=os*glob[a,b]
                if im in orbit and orbit[im]!=fac:raise AssertionError('stabilizer mismatch')
                orbit[im]=fac
            col={}
            for im,fac in orbit.items():
                for i in range(p+1):
                    boundary=im[:i]+im[i+1:]
                    if boundary not in lower_rep_index:continue
                    row=lower_rep_index[boundary]
                    val=fac*((-1)**i)
                    col[row]=col.get(row,0)+val
            columns.append(col)
        maps.append(columns)
        ranks.append(rank(columns))
    for p in (1,2):
        left=maps[p-1]
        for c in maps[p]:
            comp={}
            for row,a in c.items():
                for k,b in left[row].items():
                    comp[k]=comp.get(k,0)+a*b
            assert all(z==0 for z in comp.values()), (m,n,twisted,p,c,comp)
    b0=sizes[0]-ranks[0]
    b1=sizes[1]-ranks[0]-ranks[1]
    b2=sizes[2]-ranks[1]-ranks[2]
    b3=sizes[3]-ranks[2]
    return {'m':m,'n':n,'twisted':twisted,'chain_dimensions':sizes,'ranks':ranks,'betti':[b0,b1,b2,b3]}

def expected(m,n,twisted):
    N=m*n
    bothodd=(m%2==1 and n%2==1)
    botheven=(m%2==0 and n%2==0)
    if bothodd:return [(N-9)//2,1]
    if botheven:return [(N-12)//2,1]
    if twisted:
        return [(N-13-(-1)**(N//2))//2,0]
    return [(N-10)//2,1]

if __name__=='__main__':
    for m,n in [(5,5),(5,6),(5,8),(6,6),(6,7)]:
        for twisted in (False,True):
            out=invariant_complex(m,n,twisted)
            want1,want2=expected(m,n,twisted)
            assert out['betti']==[0 if (twisted and (m%2 != n%2)) else 1,want1,want2,0], (out,want1,want2)
            print(out)
    print('TOROIDAL_CUT_TRANSLATION_INVARIANTS_OK')
