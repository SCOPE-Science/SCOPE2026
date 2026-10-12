from fractions import Fraction
from itertools import product

# Diagonal quadratic forms for C1,C2,C3.
Q1=(Fraction(1),Fraction(1),Fraction(-1))
Q2=(Fraction(1,3),Fraction(1),Fraction(-1))
Q3=(Fraction(1),Fraction(1,3),Fraction(-1))

# Relative spectra Q1^{-1}Q2 and Q1^{-1}Q3.
A2=(Fraction(1,3),Fraction(1),Fraction(1))
A3=(Fraction(1),Fraction(1,3),Fraction(1))
assert sorted(A2)==sorted([Fraction(1,3),1,1])
assert sorted(A3)==sorted([Fraction(1,3),1,1])
# No nontrivial scalar c can preserve the spectrum with multiplicities.
cs=set()
for a in A2:
    for b in A2:
        if a:
            c=b/a
            if sorted([c*x for x in A2])==sorted(A2):
                cs.add(c)
assert cs=={Fraction(1)}

# Lines as coefficient rows, normalized projectively.
lines={
    'L1':(-1,1,-2),
    'L2':(1,1,2),
    'L3':(-1,1,2),
    'L4':(1,1,-2),
}
def canon(v):
    v=list(v)
    for a in v:
        if a:
            if a<0: v=[-x for x in v]
            return tuple(v)
    raise ValueError
canon_to_name={canon(v):k for k,v in lines.items()}

# The full conic-triple stabilizer consists of 8 sign/swap maps.
# Representatives: diag(sx,sy,1), optionally followed by X<->Y.
elems=[]
for sx,sy in product((1,-1),repeat=2):
    for swap in (False,True):
        def act_line(v,sx=sx,sy=sy,swap=swap):
            a,b,c=v
            # row coefficient action by inverse; signs are self-inverse.
            a,b=a*sx,b*sy
            if swap:
                a,b=b,a
            return canon((a,b,c))
        perm={name:canon_to_name[act_line(v)] for name,v in lines.items()}
        elems.append(((sx,sy,swap),perm))
assert len(elems)==8

stab_B1=[e for e,p in elems if {p['L1'],p['L2']}=={'L1','L2'}]
stab_B2=[e for e,p in elems if {p['L1'],p['L3']}=={'L1','L3'}]
assert set(stab_B1)=={(1,1,False),(1,-1,False)}
assert set(stab_B2)=={(1,1,False),(1,1,True),(-1,-1,False),(-1,-1,True)}

print('VERIFY_OK')
print('conic_triple_stabilizer_order',len(elems))
print('B1_stabilizer',stab_B1)
print('B2_stabilizer',stab_B2)
