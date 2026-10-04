from fractions import Fraction as Q

# Bell correlations in the order Phi+, Phi-, Psi+, Psi-.
VERTICES = ((1,-1,1),(-1,1,1),(1,1,-1),(-1,-1,-1))

def corr(ns, den):
    return tuple(sum(Q(ns[k],den)*VERTICES[k][j] for k in range(4)) for j in range(3))

def bounds(q):
    lo=(q-1)**2/Q(6)
    dl=(5*q*q-6*q+5)/Q(48)
    du=2*q*q/Q(27)
    hi=dl if q <= Q(15,13) else du
    return lo,hi

def discord_and_q(c):
    s=sorted((abs(v) for v in c), reverse=True)
    q=sum(s)
    d=(s[1]*s[1]+s[2]*s[2])/Q(3)
    return d,q

count=0
den=30
for a in range(den+1):
  for b in range(den-a+1):
    for c0 in range(den-a-b+1):
      d0=den-a-b-c0
      c=corr((a,b,c0,d0),den)
      dg,q=discord_and_q(c)
      if q < 1:
        continue
      lo,hi=bounds(q)
      assert lo <= dg <= hi, (a,b,c0,d0,dg,q,lo,hi)
      count += 1

# Exact extremal-family checks on q = 1 + 2k/120, k=0,...,120.
for k in range(121):
    q=Q(1)+Q(2*k,120)
    lo,hi=bounds(q)
    low=(Q(1),(q-1)/2,(q-1)/2)
    dl=((q+1)/4,(q+1)/4,(q-1)/2)
    du=(q/3,q/3,q/3)
    dlow=(low[1]**2+low[2]**2)/3
    ddl=(dl[1]**2+dl[2]**2)/3
    ddu=(du[1]**2+du[2]**2)/3
    assert dlow == lo
    assert max(ddl,ddu) == hi

qstar=Q(15,13)
fstar=(Q(1)+qstar/Q(3))/Q(2)
assert fstar == Q(9,13)
dl=(5*qstar*qstar-6*qstar+5)/48
du=2*qstar*qstar/27
assert dl == du
print(f"VERIFY_OK bell_grid={count} extremal_q_grid=121 crossover=9/13")
