"""Finite checks for power-complete maps of strong semilattices of nilpotent groups."""
from itertools import permutations
from math import gcd, lcm

class Group:
    def __init__(self, elems, ident, mult, name):
        self.elems = tuple(elems)
        self.ident = ident
        self.mult = mult
        self.name = name
    def power(self, x, n):
        y=self.ident
        for _ in range(n):
            y=self.mult(y,x)
        return y
    def exponent(self):
        ans=1
        for x in self.elems:
            y=self.ident
            for j in range(1,len(self.elems)+1):
                y=self.mult(y,x)
                if y==self.ident:
                    ans=lcm(ans,j)
                    break
            else:
                raise AssertionError('not finite group')
        return ans

def cyclic(n):
    return Group(tuple(range(n)),0,lambda x,y:(x+y)%n,f'C{n}')

def elementary_four():
    return Group(tuple(range(4)),0,lambda x,y:x^y,'V4')

def dihedral_eight():
    els=tuple((a,b) for a in range(4) for b in range(2))
    return Group(els,(0,0),lambda x,y:((x[0]+(-1 if x[1] else 1)*y[0])%4,(x[1]+y[1])%2),'D8')

def heisenberg_27():
    els=tuple((a,b,c) for a in range(3) for b in range(3) for c in range(3))
    return Group(els,(0,0,0),lambda x,y:((x[0]+y[0])%3,(x[1]+y[1])%3,(x[2]+y[2]+x[0]*y[1])%3),'H3')

def direct(A,B):
    return Group(tuple((x,y) for x in A.elems for y in B.elems),(A.ident,B.ident),lambda x,y:(A.mult(x[0],y[0]),B.mult(x[1],y[1])),A.name+'x'+B.name)

def valid(g,alpha,k):
    return set(alpha)==set(g.elems) and len(alpha)==len(g.elems) and len({g.mult(x,g.power(alpha[i],k)) for i,x in enumerate(g.elems)})==len(g.elems)

def find_complete(g):
    for alpha in permutations(g.elems):
        if valid(g,alpha,1):
            return dict(zip(g.elems,alpha))
    raise AssertionError(f'no ordinary complete map on {g.name}')

def power_complete_for_odd_k(P,Q,k):
    assert k%2==1
    if len(P.elems)>1:
        beta=find_complete(P)
        e=P.exponent()
        ell=pow(k,-1,e)
        alphaP={x:P.power(beta[x],ell) for x in P.elems}
    else:
        alphaP={P.ident:P.ident}
    m=Q.exponent()
    a=next(j for j in range(1,2*m+2) if gcd(j,m)==gcd(1+k*j,m)==1)
    G=direct(P,Q)
    alpha=tuple((alphaP[p],Q.power(q,a)) for p,q in G.elems)
    assert valid(G,alpha,k)
    return a,len(G.elems)

def clifford_two_fibers(top,bottom):
    # Strong semilattice with two idempotents: the connecting map top -> bottom is trivial.
    elems=(tuple(('B',x) for x in bottom.elems)+tuple(('T',x) for x in top.elems))
    def product(x,y):
        if x[0]=='B' and y[0]=='B': return ('B',bottom.mult(x[1],y[1]))
        if x[0]=='T' and y[0]=='T': return ('T',top.mult(x[1],y[1]))
        return x if x[0]=='B' else y
    def power(x,k):
        v=('B',bottom.ident) if x[0]=='B' else ('T',top.ident)
        for _ in range(k): v=product(v,x)
        return v
    return elems,product,power

def exhaust_clifford(top,bottom,k):
    elems,product,power=clifford_two_fibers(top,bottom)
    accepted=0
    for alpha in permutations(elems):
        t={product(x,power(y,k)) for x,y in zip(elems,alpha)}
        if len(t)==len(elems):
            accepted+=1
            assert all(x[0]==y[0] for x,y in zip(elems,alpha)), 'grade localization failed'
    return accepted

def main():
    positive=0
    for P in (cyclic(1),elementary_four(),dihedral_eight()):
        for Q in (cyclic(1),cyclic(3),cyclic(9),cyclic(15),heisenberg_27()):
            for k in (3,5,7):
                a,n=power_complete_for_odd_k(P,Q,k)
                positive+=1
    assert positive==45
    negative=0
    for n in (2,4,6):
        g=cyclic(n)
        for k in (3,5,7):
            if n==6 and k==7: continue
            assert not any(valid(g,p,k) for p in permutations(g.elems))
            negative+=1
    # The two Clifford examples have nontrivial semilattice multiplication.
    assert exhaust_clifford(elementary_four(),cyclic(3),3)>0
    assert exhaust_clifford(elementary_four(),cyclic(3),5)>0
    assert exhaust_clifford(cyclic(2),cyclic(3),3)==0
    assert exhaust_clifford(cyclic(2),cyclic(3),5)==0
    arithmetic=0
    for m in range(1,102,2):
        for k in range(3,32,2):
            assert any(gcd(a,m)==gcd(1+k*a,m)==1 for a in range(1,2*m+2))
            arithmetic+=1
    print(f'PRODUCT_WITNESSES={positive} CYCLIC_OBSTRUCTIONS={negative} CLIFFORD_EXHAUSTIVE=4 CRT_CASES={arithmetic} VERIFY_OK')

if __name__=='__main__':
    main()
