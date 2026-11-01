"""Standalone exact checks of a closed two-cycle count for finite open ladders.
Standard-library only. Run with Python 3.10+.
"""
from itertools import product

B = (
 (0,0,1,0,0,0),
 (0,0,0,7,2,6),
 (1,4,4,0,0,0),
 (0,1,2,0,0,0),
 (0,0,0,4,1,4),
 (0,0,0,12,4,9),
)
L=(0,0,2,8,2,8)
R=(0,2,1,0,1,4)
P=tuple(product((0,1), repeat=2))


def transfer(n):
    assert n >= 2
    v=list(R)
    for _ in range(n-2):
        v=[sum(B[i][j]*v[j] for j in range(6)) for i in range(6)]
    assert sum(L[i]*v[i] for i in range(6))%2==0
    return sum(L[i]*v[i] for i in range(6))//2


def direct_phase_sum(n):
    """Independently enumerates all 2^(2*n) binary firing-phase assignments."""
    assert n >= 2
    edges=[(2*i,2*i+1) for i in range(n)]
    for i in range(n-1):
        edges.extend(((2*i,2*(i+1)),(2*i+1,2*(i+1)+1)))
    nei=[set() for _ in range(2*n)]
    for v,w in edges:
        nei[v].add(w);nei[w].add(v)
    summ=0
    for colors in product((0,1),repeat=2*n):
        term=1
        for v in range(2*n):
            term*=sum(colors[v] != colors[w] for w in nei[v])
            if not term:break
        summ+=term
    assert summ%2==0
    return summ//2


def direct_states(n):
    """Enumerates bounded chip states; checks F^2(x)=x and F(x)!=x."""
    assert 2 <= n <= 4
    edge=[(2*i,2*i+1) for i in range(n)]
    for i in range(n-1):
        edge.extend(((2*i,2*i+2),(2*i+1,2*i+3)))
    nei=[[] for _ in range(2*n)]
    for a,b in edge:nei[a].append(b);nei[b].append(a)
    deg=[len(x) for x in nei]
    ranges=[range(2*d) for d in deg]
    def update(chips):
        firing=[int(chips[i]>=deg[i]) for i in range(2*n)]
        return tuple(chips[i]-deg[i]*firing[i]+sum(firing[j] for j in nei[i]) for i in range(2*n))
    states=0;period2=0
    for x in product(*ranges):
        states+=1
        y=update(x)
        if y!=x and update(y)==x:period2+=1
    assert period2%2==0
    return states,period2//2


def check_quotient():
    """Construct the six symmetry orbit classes directly from rung bit-pairs."""
    states=tuple(product(P,repeat=2))
    def image(pair,flip,swap):
        a,b=pair
        if flip:
            a=tuple(1-x for x in a)
            b=tuple(1-x for x in b)
        if swap:
            a=a[::-1]
            b=b[::-1]
        return a,b
    orbit=[];seen=set()
    for ab in states:
        if ab in seen:continue
        o=sorted({image(ab,f,s) for f in range(2) for s in range(2)})
        orbit.append(o);seen.update(o)
    assert len(orbit)==6
    def local(a,b,c):
        return ((a[0]!=b[0])+(b[0]!=c[0])+(b[0]!=b[1])) * \
               ((a[1]!=b[1])+(b[1]!=c[1])+(b[0]!=b[1]))
    def edge(a,b):
        return ((a[0]!=b[0])+(a[0]!=a[1])) * \
               ((a[1]!=b[1])+(a[0]!=a[1]))
    for i,o in enumerate(orbit):
        assert L[i]==sum(edge(a,b) for a,b in o)
        a,b=o[0]
        assert R[i]==edge(b,a)
        for j,target in enumerate(orbit):
            val=sum(local(a,b,c) for bb,c in target if bb==b)
            assert B[i][j]==val,(i,j,B[i][j],val)
    return len(orbit)

def exact_GF():
    # Scalar transfer and analytic recurrence at n=2; numerator matches
    # (18-11z-10z^2+z^3) / ((1-z^2)(1-12z+z^2)).
    seq=[transfer(n) for n in range(2,27)]
    assert seq[:7]==[18,205,2450,29185,347778,4144141,49381922]
    assert all(seq[k]==12*seq[k-1]-12*seq[k-3]+seq[k-4]
               for k in range(4,len(seq)))
    # Matrix characteristic polynomial:
    # det(xI-B)=(x-1)^3 (x+1)(x^2-12x+1).
    # Check the linear recurrence induced by the characteristic polynomial
    # at every component of six basis vectors, without symbolic software.
    def matmul(A,C):
        return [[sum(A[i][k]*C[k][j] for k in range(6))
                 for j in range(6)] for i in range(6)]
    ident=[[int(i==j) for j in range(6)] for i in range(6)]
    powers=[ident]
    for _ in range(6):powers.append(matmul(powers[-1],B))
    # Evaluate the monic polynomial product using integer arithmetic.
    def pmul(A,C):
        y=[0]*(len(A)+len(C)-1)
        for i,a in enumerate(A):
            for j,b in enumerate(C):y[i+j]+=a*b
        return y
    polynomial=pmul(pmul(pmul([-1,1],[-1,1]),[-1,1]),pmul([1,1],[1,-12,1]))
    assert len(polynomial)==7
    assert all(sum(polynomial[k]*powers[k][i][j] for k in range(7))==0
               for i in range(6) for j in range(6))
    # Exhaustively certify scalar order-four annihilator using six initial
    # residuals and Cayley-Hamilton on a 6x6 transfer matrix.
    p4=[-1,12,0,-12,1]
    # Avoid relying on powers higher than six: evolve the observable
    # scalar sequence and validate the six necessary initial residuals.
    vals=[2*transfer(i) for i in range(2,16)]
    assert all(sum(p4[j]*vals[t+j] for j in range(5))==0 for t in range(6))
    # Since each residual is a linear functional of B^t, the characteristic
    # identity above propagates these six zeros to all t.
    return len(seq)


def main():
    assert check_quotient()==6
    print('SIX_CLASS_TRANSFER_RECONSTRUCTED_OK')
    count=exact_GF()
    print('CERTIFIED_TRANSFER_RECURRENCE: 6x6 characteristic identity and six residual seeds; %d numerical terms'%count)
    phase_total=0
    for n in range(2,9):
        a,b=transfer(n),direct_phase_sum(n)
        assert a==b,(n,a,b)
        phase_total+=2**(2*n)
        print('PHASE n=%d primitive_orbits=%d'%(n,a))
    total=0
    for n in range(2,5):
        states,orbits=direct_states(n)
        assert orbits==transfer(n)
        total+=states
        print('DIRECT_STATES n=%d checked=%d primitive_orbits=%d'%(n,states,orbits))
    print('PHASE_ASSIGNMENTS_EXAMINED=%d'%phase_total)
    print('BOUNDED_STATES_EXAMINED=%d'%total)
    print('LADDER_CHIPFIRE_EXACT_VERIFY_OK')
if __name__=='__main__':main()
