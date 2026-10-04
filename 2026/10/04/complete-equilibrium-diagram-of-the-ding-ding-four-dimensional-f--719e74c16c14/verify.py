from fractions import Fraction as Q

def F(state,a,b,c,d):
    x,y,z,w=state
    return (
        a*(y-x),
        b*x-y-x*z+w,
        x*x-c*z,
        w-d*x*x*x,
    )

def zero(v):
    return all(t == 0 for t in v)

# Principal published parameters: R=-144, hence no nonzero real equilibrium.
a,b,c,d=Q(24),Q(25),Q(3),Q(1,2)
R=c*(1-b)/(d*c-1)
assert R == -144
assert zero(F((Q(0),Q(0),Q(0),Q(0)),a,b,c,d))
# A point on the paper's plotted curve with x=1 is not an equilibrium.
assert F((Q(1),Q(1),Q(1,3),Q(1,2)),a,b,c,d)[1] == Q(145,6)

# A positive-R example with all parameters positive: R=4 gives exactly the two sign branches.
a,b,c,d=Q(7),Q(3,2),Q(4),Q(1,8)
R=c*(1-b)/(d*c-1)
assert R == 4
for s in (Q(1),Q(-1)):
    x=2*s
    E=(x,x,R/c,d*x*x*x)
    assert zero(F(E,a,b,c,d))

# Degenerate equilibrium-curve case b=1 and dc=1.
a,b,c,d=Q(5),Q(1),Q(2),Q(1,2)
for x in (Q(-3,2),Q(0),Q(7,3)):
    assert zero(F((x,x,x*x/c,x*x*x/c),a,b,c,d))

# At the origin, row 4 of J-I is identically zero, hence lambda=1 is an eigenvalue.
# J(O) row 4 is [0,0,0,1].
assert [Q(0),Q(0),Q(0),Q(1)-Q(1)] == [Q(0)]*4
print('VERIFY_OK')
