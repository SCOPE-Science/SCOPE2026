"""Exact finite checks for the balanced-biclique indicator variation theorem.
Run: python3 verify_biclique.py. Uses Python's standard library only.
Finite checks are independent corroboration, not a proof for all graph orders.
"""
from fractions import Fraction as F


def claimed_constant(r):
    assert isinstance(r, int) and r >= 2
    return max(F(r, r + 1), F(4*r*r - 11*r + 8, (r+1)*(3*r-4)))


def analytic_ratio(r, a, b):
    """Compute the ratio from the four vertex-value classes, not the theorem."""
    assert 0 <= a <= r and 0 <= b <= r
    if (a, b) in ((0, 0), (r, r)):
        return None
    s = a+b
    def A(t):
        return max(F(t), F(t+b,r+1), F(a + int(b>0),r+1), F(s,2*r))
    def B(t):
        return max(F(t), F(t+a,r+1), F(b + int(a>0),r+1), F(s,2*r))
    A0, A1, B0, B1 = A(0),A(1),B(0),B(1)
    numerator = (a*b*abs(A1-B1) + a*(r-b)*abs(A1-B0)
                 + (r-a)*b*abs(A0-B1) + (r-a)*(r-b)*abs(A0-B0))
    denominator = a*(r-b)+b*(r-a)
    assert denominator > 0
    return numerator / denominator


def direct_graph_ball_ratio(r, a, b):
    """Enumerate every center and every distinct-radius ball in the actual graph."""
    n=2*r
    inp=[1]*a+[0]*(r-a)+[1]*b+[0]*(r-b)
    if min(inp)==max(inp): return None
    balls=[]
    for c in range(n):
        balls.append({c})
        balls.append({c} | (set(range(r,n)) if c <r else set(range(r))))
        balls.append(set(range(n)))
    M=[]
    for i in range(n):
        M.append(max(F(sum(inp[j] for j in ball),len(ball))
                     for ball in balls if i in ball))
    num=sum(abs(M[i]-M[j]) for i in range(r) for j in range(r,n))
    den=sum(abs(inp[i]-inp[j]) for i in range(r) for j in range(r,n))
    return num/den


def polynomial_identities(r,a,b):
    """The two elementary comparison certificates from the analytic proof."""
    P=lambda a,b:(r-b)*(r-2*a)*(b+1)-r*(r-a)*b
    D=lambda a,b:r*(a+b)-2*a*b
    assert P(a,b)*D(1,b)-P(1,b)*D(a,b) == -r*r*(a-1)*(r-b)
    assert (P(1,b)*D(1,2)-P(1,2)*D(1,b)
            == -(b-2)*(b*(3*r-4)*(r-2)+r*(r*r-2)))
    assert P(1,2)==r*r-10*r+12


def main():
    graph_checks=0
    count_checks=0
    certificate_checks=0
    for r in range(2,9):
        for a in range(r+1):
            for b in range(r+1):
                expected=analytic_ratio(r,a,b)
                direct=direct_graph_ball_ratio(r,a,b)
                assert direct==expected,(r,a,b,direct,expected)
                graph_checks+=1
    for r in range(2,46):
        maxima=[]
        for a in range(r+1):
            for b in range(r+1):
                v=analytic_ratio(r,a,b)
                if v is not None:
                    assert v<=claimed_constant(r),(r,a,b,v,claimed_constant(r))
                    maxima.append(v)
                    count_checks+=1
        assert max(maxima)==claimed_constant(r),r
        if r>=6:
            assert analytic_ratio(r,1,2)==claimed_constant(r)
        else:
            assert analytic_ratio(r,0,1)==claimed_constant(r)
    for r in range(2,42):
        for b in range(2,r+1):
            for a in range(1,b):
                polynomial_identities(r,a,b)
                certificate_checks+=1
    for r in range(2,40):
        assert (claimed_constant(r)>1)==(r>=9)
        assert claimed_constant(r)<F(4,3)
        assert claimed_constant(r+1)>claimed_constant(r)
    print('PASS: {} exact direct-ball comparisons; {} orbit-count comparisons; {} polynomial certificate substitutions.'.format(graph_checks,count_checks,certificate_checks))
    for r in (2,5,6,8,9,10,20,45):
        print('r={} sharp cut constant={}'.format(r,claimed_constant(r)))

if __name__=='__main__':
    main()
