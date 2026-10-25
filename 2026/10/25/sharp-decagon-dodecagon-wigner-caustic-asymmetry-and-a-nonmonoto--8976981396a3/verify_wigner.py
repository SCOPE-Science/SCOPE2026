"""Exact algebraic audit of the decagonal and dodecagonal Wigner-area bounds.

Run: python verify_wigner.py. Requires SymPy. No sampled geometry is used.
"""
import itertools
import sympy as S


def simp(x):
    return S.simplify(S.trigsimp(x))


def eq(a,b):
    return all(simp(x-y)==0 for x,y in zip(a,b))


def shift(v):
    return (-v[-1],)+tuple(v[:-1])


def orbit(rep,n):
    out=[];v=tuple(rep)
    for _ in range(2*n):
        if not any(eq(v,w) for w in out):out.append(v)
        v=shift(v)
    assert eq(v,rep)
    return out


def exact_vertices(n):
    alpha=S.pi/n
    a=S.Matrix([[S.cos(j*alpha) for j in range(n)],
                [S.sin(j*alpha) for j in range(n)]])
    verts=[]; candidates=0
    for free in itertools.combinations(range(n),2):
        fixed=[j for j in range(n) if j not in free]
        M=a[:,list(free)]
        if simp(M.det())==0:continue
        for signs in itertools.product((S.Integer(-1),S.Integer(1)),repeat=n-2):
            candidates+=1
            d=[None]*n
            for j,v in zip(fixed,signs):d[j]=v
            sol=M.inv()*(-a[:,fixed]*S.Matrix(signs))
            for j,v in zip(free,sol):d[j]=simp(v)
            admissible=True
            for v in d:
                # This comparison is performed on exact algebraic numbers by SymPy.
                lo=S.simplify(v+1>=0)
                hi=S.simplify(1-v>=0)
                assert lo in (S.true,S.false) and hi in (S.true,S.false), (n,v,lo,hi)
                if not (lo and hi):admissible=False;break
            if admissible and not any(eq(d,w) for w in verts):verts.append(tuple(d))
    assert candidates==(n*(n-1)//2)*2**(n-2)
    return verts


def wigner_area(n,d):
    z=-S.Rational(1,2)*sum(d[i]*d[j]*S.sin(S.pi*(j-i)/n)
           for i in range(n) for j in range(i+1,n))
    return simp(z)


def prove(n,representatives,expected_counts,expected_W):
    vertices=exact_vertices(n)
    orbits=[orbit(t,n) for t in representatives]
    assert [len(o) for o in orbits]==expected_counts
    assert sum(map(len,orbits))==len(vertices)
    for v in vertices:
        assert sum(any(eq(v,x) for x in o) for o in orbits)==1
    for o,target in zip(orbits,expected_W):
        assert all(simp(wigner_area(n,d)-target)==0 for d in o)
    return len(vertices)



def independent_shoelace_check(n, d):
    """Reconstruct both polygons from their actual edge vectors."""
    a=S.pi/n
    u=[S.Matrix([S.cos(j*a),S.sin(j*a)]) for j in range(n)]
    edges=[(1+d[j])*u[j] for j in range(n)] + [-(1-d[j])*u[j] for j in range(n)]
    x=[S.Matrix([S.Integer(0),S.Integer(0)])]
    for e in edges:x.append(x[-1]+e)
    assert all(simp(z)==0 for z in x[-1])
    def cross(v,w):return v[0]*w[1]-v[1]*w[0]
    polygon_area=simp(sum(cross(x[j],x[j+1]) for j in range(2*n))/2)
    mid=[(x[j]+x[j+n])/2 for j in range(n)]
    signed=simp(sum(cross(mid[j],mid[(j+1)%n]) for j in range(n))/2)
    assert simp(signed+wigner_area(n,d))==0
    central=n*S.cot(S.pi/(2*n))/2
    assert simp(polygon_area+2*wigner_area(n,d)-central)==0


def main():
    r=S.sqrt(5);t=r-2
    w5=(5-2*r)*S.cot(S.pi/10)/4
    count5=prove(5,[(1,-1,1,-1,1),(-t,1,-t,-1,1)], [2,10],[w5,w5])
    r=S.sqrt(3)
    count6=prove(6,[(1,1,-1,-1,1,1),
                   (1,0,-1,1,1-r,1),
                   (1,3-2*r,3-2*r,1,-1,1)],
                 [4,12,12],[r/2,(r-1)/2,(5*r-8)/2])
    c5=5*S.cot(S.pi/10)/2
    c6=3*S.cot(S.pi/12)
    assert simp((w5/(c5-2*w5))-(S.sqrt(5)-2)/4)==0
    assert simp((r/2/(c6-r))-(r-1)/8)==0
    independent_shoelace_check(5, tuple(S.Rational(1,2)*x for x in (1,-1,1,-1,1)))
    independent_shoelace_check(6, tuple(S.Rational(1,3)*x for x in (1,1,-1,-1,1,1)))
    assert bool(S.simplify((r-1)/8>(S.sqrt(5)-2)/4))
    assert bool(S.simplify((S.sqrt(5)-2)/4>0))
    print('EXACT_WIGNER_DECAGON_DODECAGON_OK',count5,count6)

if __name__=='__main__':main()
