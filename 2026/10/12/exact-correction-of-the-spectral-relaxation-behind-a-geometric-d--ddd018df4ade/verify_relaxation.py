from fractions import Fraction as F

def eq12(N):
    lam = [F(1), N/F(6), N/F(6), N/F(6), -N/F(4), -N/F(4)]
    xi = [F(1), F(0), F(0), F(0), F(0), F(0)]
    assert lam[0] >= lam[1] >= lam[2] >= lam[3] >= 0 >= lam[4] >= lam[5]
    assert xi == sorted(xi, reverse=True) and all(t >= 0 for t in xi)
    assert abs(lam[4]) + abs(lam[5]) == N/F(2)
    assert sum(lam[:4]) == F(1) + N/F(2)
    assert sum(xi) == F(1)
    assert sum(t*t for t in xi) <= sum(lam[i]*xi[i] for i in range(6))
    return sum(lam[i]*lam[i] - lam[i]*xi[i] for i in range(6)) - N*N/F(2)

def claimed(N):
    return N*(F(2)-F(5)*N)/F(16)

for N in [F(1,100), F(1,5), F(2,5), F(1,2), F(1)]:
    R = eq12(N)
    assert R == -F(7,24)*N*N
    assert R - claimed(N) == N*(N-F(6))/F(48)
    assert R < claimed(N)

# Exact algebraic check of the auxiliary minimum formula at rational samples.
def G(n,a,b):
    if b <= 2*a:
        return (4*a*a-4*a*b-(n-1)*b*b)/(4*n)
    return a*(a-b)

def witness_value(n,a,b):
    if b <= 2*a:
        M=(2*a+(n-1)*b)/(2*n)
        rest=(2*a-b)/(2*n)
        x=[M]+[rest]*(n-1); y=[b]+[F(0)]*(n-1)
    else:
        x=[a]+[F(0)]*(n-1); y=[b]+[F(0)]*(n-1)
    assert sum(x)==a and sum(y)==b and min(x)>=0 and min(y)>=0
    return sum(x[i]*x[i]-x[i]*y[i] for i in range(n))

for n,a,b in [(2,F(3,2),F(1,3)),(4,F(7,5),F(1)),(5,F(2),F(4)),(3,F(2,3),F(2))]:
    assert witness_value(n,a,b) == G(n,a,b)

print('VERIFY_OK')
