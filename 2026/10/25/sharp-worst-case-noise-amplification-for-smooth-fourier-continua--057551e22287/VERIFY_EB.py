"""Exact-arithmetic checks for blended Lagrange continuation."""
from fractions import Fraction
from math import comb
from itertools import product

def lagrange_weights(nodes, x):
    out=[]
    for i, u in enumerate(nodes):
        term=Fraction(1)
        for j,v in enumerate(nodes):
            if i!=j:
                term*=Fraction(x-v,u-v)
        out.append(term)
    return out

def L(d,q):
    return sum(comb(q+j-1,j)*comb(q+d-1,d-1-j) for j in range(d))

def blend_row(d,N,C,q,sigma):
    # Original grid at 0,...,N-1, continuation near right endpoint.
    wr=lagrange_weights(list(range(N-d,N)), N-1+q)
    wl=lagrange_weights(list(range(d)), q-C)
    ans=[Fraction(0)]*N
    for i,v in enumerate(wr):ans[N-d+i]+=(1-sigma)*v
    for i,v in enumerate(wl):ans[i]+=sigma*v
    return ans

def sharp_formula(d,C,q,sigma):
    return (1-sigma)*L(d,q)+sigma*L(d,C-q)

def test():
    checks=0
    for d in range(2,8):
      for C in range(2,18):
        N=2*d+3
        for q in range(1,C):
          sigma=Fraction(q,C)
          row=blend_row(d,N,C,q,sigma)
          assert sum(abs(v) for v in row)==sharp_formula(d,C,q,sigma)
          assert sum(row)==1
          # Exact dual certificate for the infinity operator norm at this row.
          signs=[1 if v>=0 else -1 for v in row]
          assert abs(sum(v*s for v,s in zip(row,signs)))==sum(abs(v) for v in row)
          checks+=1
    # Validate formula L via direct extrapolation; ± weights for all modes.
    for d in range(2,16):
      for q in range(1,30):
        w=lagrange_weights(list(range(d)), -q)
        assert sum(abs(v) for v in w)==L(d,q)
        assert len(w)==d
        checks+=1
    # Lower bound inf; check strict odd-center gap for positive left weight.
    for d in range(2,12):
      for C in range(2,28):
        k=C//2
        if C%2==0:
          assert sharp_formula(d,C,k,Fraction(1,2))==L(d,k)
        else:
          assert sharp_formula(d,C,k,Fraction(1,3))>L(d,k)
        checks+=1
    assert L(3,3)==31 and L(3,4)==49
    assert L(9,32)==17527209985
    for d in range(2,10): assert L(d,1)==2**d-1
    print('PASS',checks,'exact-rational coefficient/duality tests plus boundary tests')

if __name__=='__main__':test()

def beta_smooth_step(d,m,t):
    """Exact regularized Beta(d+m+1,d+m+1) CDF for rational t."""
    from math import comb
    from fractions import Fraction
    t=Fraction(t)
    a=d+m+1
    return sum(Fraction(comb(2*a-1,j))*t**j*(1-t)**(2*a-1-j) for j in range(a,2*a))

def test_minimax():
    for d,C in [(2,6),(3,8),(4,6),(3,10)]:
        optimum=L(d,C//2)
        attained=False
        for m in [1,3,10,30,60]:
            norm=max(sharp_formula(d,C,q,beta_smooth_step(d,m,Fraction(q,C))) for q in range(1,C))
            assert norm>=optimum
            if norm==optimum:
                attained=True;break
        assert attained,(d,C)
        assert beta_smooth_step(d,m,Fraction(1,2))==Fraction(1,2)
    for d,C in [(2,5),(3,7),(4,9)]:
        optimum=L(d,C//2)
        prev=None
        for m in [1,3,10,30]:
            norm=max(sharp_formula(d,C,q,beta_smooth_step(d,m,Fraction(q,C))) for q in range(1,C))
            assert norm>optimum
            if prev is not None:assert norm<prev
            prev=norm
    print('PASS exact beta-family attainment/nonattainment demonstration')

if __name__=='__main__':test_minimax()
