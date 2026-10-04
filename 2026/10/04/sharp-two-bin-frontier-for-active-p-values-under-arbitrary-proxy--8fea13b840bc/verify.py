from fractions import Fraction as F

def envelope(s,h1,h2,b1,b2):
    t1=min(F(1),s/b1)
    t2=min(F(1),s/b2)
    return h1*t1+(h2-h1)*t2

def coeff(h1,h2,b1,b2):
    return h1/b1+(h2-h1)/b2

# Exact boundary example.
h1,h2,b1,b2=F(1,5),F(4,5),F(1,2),F(1)
assert coeff(h1,h2,b1,b2)==1
# Split-tail decomposition is impossible: beta >= 1-h1 and beta <= 1-h1/b1.
assert 1-h1==F(4,5)
assert 1-h1/b1==F(3,5)
assert (1-h1)>(1-h1/b1)
for k in range(0,101):
    s=F(k,100)
    assert envelope(s,h1,h2,b1,b2)<=s if s<1 else envelope(s,h1,h2,b1,b2)<=1

# Corroborate the theorem's envelope implication on a finite rational family.
vals=[F(0),F(1,5),F(2,5),F(3,5),F(4,5),F(1)]
bs=[F(1,5),F(2,5),F(3,5),F(4,5),F(1)]
for lo in vals:
  for hi in vals:
    if lo>hi: continue
    for x in bs:
      for y in bs:
        if x>y: continue
        C=coeff(lo,hi,x,y)
        if C<=1:
          for k in range(0,101):
            s=F(k,100)
            if s<1:
              assert envelope(s,lo,hi,x,y)<=s
# A coefficient violation has the explicit small-level adversarial witness probability C*s>s.
lo,hi,x,y=F(1,4),F(3,4),F(1,3),F(1)
C=coeff(lo,hi,x,y)
assert C>1
s=F(1,10)
assert s<=x and C*s>s
print('VERIFY_OK')
