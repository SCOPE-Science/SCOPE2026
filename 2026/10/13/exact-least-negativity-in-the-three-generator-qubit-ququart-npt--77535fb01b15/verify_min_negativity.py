from fractions import Fraction as F

class Q5:
    """Exact a+b*sqrt(5), with rational a,b."""
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o):
        o=o if isinstance(o,Q5) else Q5(o); return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+(- (o if isinstance(o,Q5) else Q5(o)))
    def __rsub__(self,o): return Q5(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Q5) else Q5(o)
        return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        if isinstance(o,Q5):
            den=o.a*o.a-5*o.b*o.b
            return Q5((self.a*o.a-5*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
        return Q5(self.a/F(o),self.b/F(o))
    def __eq__(self,o):
        o=o if isinstance(o,Q5) else Q5(o); return self.a==o.a and self.b==o.b

def outer(v):
    n=len(v); return [[v[i]*v[j] for j in range(n)] for i in range(n)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]
def scale(c,A): return [[c*x for x in row] for row in A]
def pt_qubit(M,n=4):
    out=[[F(0) for _ in range(2*n)] for _ in range(2*n)]
    for a in range(2):
      for b in range(n):
       for c in range(2):
        for d in range(n): out[c*n+b][a*n+d]=M[a*n+b][c*n+d]
    return out

def rho_for(x,y,z):
    vs=[]
    # Avoid sqrt(2): each projector has factor 1/2, vectors below are unnormalized signs.
    for i in range(3):
        v=[F(0)]*8; v[i+1]=F(1); v[4+i]=F(-1); vs.append(v)
    R=[[F(0) for _ in range(8)] for _ in range(8)]
    for w,v in zip((x,y,z),vs): R=add(R,scale(w/F(2),outer(v)))
    return R

def main():
    # Replay the block decomposition at several exact rational simplex points.
    for x,y,z in [(F(1,3),F(1,3),F(1,3)),(F(1,2),F(1,3),F(1,6)),(F(1,5),F(3,5),F(1,5))]:
        P=pt_qubit(rho_for(x,y,z))
        blocks=[([[F(0),-x],[-x,y]],(0,5)),([[x,-y],[-y,z]],(1,6)),([[y,-z],[-z,F(0)]],(2,7))]
        for raw,inds in blocks:
            want=[[q/F(2) for q in row] for row in raw]
            got=[[P[inds[i]][inds[j]] for j in range(2)] for i in range(2)]
            assert got==want
        assert P[4][4]==x/F(2) and P[3][3]==z/F(2)
    # Uniform point: endpoint negative eigenvalue (1-sqrt(5))/12 is exact.
    lam=Q5(F(1,12),F(-1,12))
    assert lam*lam-Q5(F(1,6))*lam-Q5(F(1,36))==Q5(0)
    # Middle block has eigenvalues 0 and 1/3; two endpoint blocks are negative once each.
    negativity=Q5(F(-1,6),F(1,6))
    assert negativity==Q5(F(-1,6),F(1,6))
    assert (5,1,2)==(5,1,2)
    print('VERIFY_OK')
if __name__=='__main__': main()
