from fractions import Fraction as F

def d_from_probs(p):
    p1,p2,p3,p4=p
    c1=p1-p2+p3-p4
    c2=-p1+p2+p3-p4
    c3=p1+p2-p3-p4
    s=sorted([c1*c1,c2*c2,c3*c3])
    return (s[0]+s[1])/4

def conc(p):
    return max(F(0), 2*max(p)-1)

def lo(C):
    return F(0) if C==0 else C*C/2

def face(C): return (1+2*C+5*C*C)/16
def iso(C): return (1+2*C)*(1+2*C)/18
def hi(C): return face(C) if C <= F(1,13) else iso(C)

# Exact formula checks for rational C values including the crossover.
Cs=[F(0),F(1,100),F(1,13),F(1,10),F(1,2),F(9,10),F(1)]
for C in Cs:
    pface=( (1+C)/2,(1-C)/4,(1-C)/4,F(0) )
    piso=( (1+C)/2,(1-C)/6,(1-C)/6,(1-C)/6 )
    assert conc(pface)==C and conc(piso)==C
    assert d_from_probs(pface)==face(C)
    assert d_from_probs(piso)==iso(C)
    if C>0:
        pedge=((1+C)/2,(1-C)/2,F(0),F(0))
        assert conc(pedge)==C and d_from_probs(pedge)==lo(C)
assert iso(F(1,13))==face(F(1,13))
for C in Cs:
    assert iso(C)-face(C)==(1-C)*(13*C-1)/F(144)

# Exact finite grid sanity check over the probability simplex.
# This is deliberately supplementary: the analytic proof covers the continuum.
checked=0
for N in (12,18,24,30):
    vals={}
    for a in range(N+1):
      for b in range(N+1-a):
       for c in range(N+1-a-b):
        d=N-a-b-c
        p=tuple(F(x,N) for x in (a,b,c,d))
        C=conc(p); D=d_from_probs(p)
        assert lo(C) <= D <= hi(C)
        checked += 1
print(f"VERIFY_OK rational_states={checked} crossover=1/13")
