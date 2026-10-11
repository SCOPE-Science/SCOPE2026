"""Direct reproducibility checks for reflection Lefschetz formulas of grid matching complexes.
Run: python verify_grid_reflection.py (Python 3 + SymPy).
"""
import sympy as sp
from itertools import combinations

def edges(n):
    ans=[]
    for r in range(3):
        for c in range(n):
            if r<2: ans.append((r*n+c,(r+1)*n+c))
            if c<n-1: ans.append((r*n+c,r*n+c+1))
    return [tuple(sorted(e)) for e in ans]

def signed_invariant_matchings(n,kind):
    E=edges(n); index={e:i for i,e in enumerate(E)}
    def mapvertex(v):
        r,c=divmod(v,n)
        if kind=='row':r=2-r
        if kind=='col':c=n-1-c
        return r*n+c
    p=[index[tuple(sorted(map(mapvertex,e)))] for e in E]
    total=0; fixed=0
    def walk(i,occupied,selected):
        nonlocal total,fixed
        if i==len(E):
            st=set(selected)
            if {p[j] for j in st}!=st: return
            fixed+=1;seen=set();orbits=0
            for j in st:
                if j not in seen:
                    orbits+=1;h=j
                    while h not in seen:
                        seen.add(h);h=p[h]
            total+=(-1)**orbits
            return
        walk(i+1,occupied,selected)
        u,v=E[i];block=(1<<u)|(1<<v)
        if occupied&block==0:walk(i+1,occupied|block,selected+(i,))
    walk(0,0,())
    return total,fixed

def transfer():
    return sp.Matrix(8,8,lambda a,b:
        (-1)**int(b).bit_count()*(1-sum(((int(a)|int(b))&mask)==0 for mask in (3,6)))
        if int(a)&int(b)==0 else 0)

def verify():
    T=transfer();z=sp.Symbol('z');I=sp.eye(8)
    resolvent=(I-z*T).inv()
    den=z**6-2*z**5+4*z**4+2*z**3+2*z+1
    f=(1+z)**2*(z**2-z+1)/den
    q=-z**2*(z**4-z**3+2*z**2+z+1)/den
    assert sp.cancel(resolvent[0,0]-f)==0
    assert sp.cancel(z*(resolvent[0,7]-resolvent[0,1]-resolvent[0,4])-q)==0
    a=[1,1]
    for n in range(2,8): a.append(a[-1]-a[-2])
    row=sp.zeros(1,8);row[0]=1;F=[1];Q=[0]
    for m in range(1,8):
        Q.append(int(-row[1]-row[4]+row[7]))
        row=row*T;F.append(int(row[0]))
    # Exhaustive enumeration is independent of the 8-state transfer construction.
    for n in range(2,8):
        Sr,nr=signed_invariant_matchings(n,'row')
        Sc,nc=signed_invariant_matchings(n,'col')
        assert Sr==a[n]**2,(n,'row',Sr,a[n]**2)
        assert Sc==(Q[n//2] if n%2==0 else -F[n//2]),(n,'col',Sc)
        print('n=',n,'invariant counts=',nr,nc,'Lefschetz=',-Sr,-Sc)
    print('VERIFY_OK: exact rational generating functions and all invariant matchings for n=2,...,7')

if __name__=='__main__': verify()
