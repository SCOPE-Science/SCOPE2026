from fractions import Fraction as Q

def f(z):
    x,y=z
    m=max(Q(0),2*x)
    return (y+m,Q(1)-m)

def section(r):
    return (Q(1)+2*r,Q(1)-2*r)

cycle=[(Q(1),Q(1))]
for _ in range(6):cycle.append(f(cycle[-1]))
assert len(set(cycle))==7 and f(cycle[-1])==cycle[0]

# Exact midpoint tests in each partition: no floating-point tolerances.
for r,t in [(Q(1,32),7),(Q(3,32),None),(Q(1,4),6), (Q(7,8),6), (Q(1,17),7), (Q(1,9),None)]:
    z=section(r)
    if t is not None:
        assert z not in cycle
        for j in range(1,t):
            z=f(z)
            assert z not in cycle,(r,j,z)
        assert f(z)==cycle[0],(r,t,f(z))
    else:
        for j in range(7):z=f(z)
        assert z==section(16*r-1),(r,z)

# Every L=16^{-k} survivor interval comes from exactly k inverse branches.
for k in range(7):
    a,b=Q(0),Q(1)
    for j in range(k):
        a=(a+1)/16
        b=(b+1)/16
    assert b-a==Q(1,16**k)
    assert (b-a)*Q(14,16)==Q(14,16**(k+1))
    assert (b-a)*Q(1,16)==Q(1,16**(k+1))

# The seven-clock tail partition: exact formulas at representative times.
for n in range(0,50):
    remaining=Q(1)
    for k in range(n//7+2):
        if 7*k+6<=n:remaining-=Q(14,16**(k+1))
        if 7*k+7<=n:remaining-=Q(1,16**(k+1))
    q,m=divmod(n,7)
    expected=Q(1,16**q) if m<=5 else Q(2,16**(q+1))
    assert remaining==expected,(n,remaining,expected)

print('CAPTURE_CLOCK_VERIFIED')
