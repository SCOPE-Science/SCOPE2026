from math import gcd

def sq(x,y):
    return 4*x*x + 10*x*y + 2*y*y

def p_of(x,y): return 3*x + 8*y
def q_of(x,y): return 37*x + 8*y
def invol(x,y): return (-x, 5*x+y)

assert sq(2,-1) == -2 and sq(-2,9) == -2
assert p_of(2,-1) == -2 and q_of(-2,9) == -2

def from_pq(p,q):
    if (q-p) % 34: return None
    if (37*p-3*q) % 272: return None
    x=(q-p)//34
    y=(37*p-3*q)//272
    return x,y

expected={
    2:{(0,1)},
    4:{(1,0),(-1,5)},
    8:{(3,-1),(-3,14)},
    16:{(1,1),(-1,6)},
}
found={}
for p in range(1,528):
    for q in range(1,528):
        if p*q > 527: continue
        xy=from_pq(p,q)
        if xy is None: continue
        x,y=xy
        s=sq(x,y)
        if not (0 < s <= 16): continue
        assert 2176*s == p*p + 66*p*q + q*q
        assert p_of(x,y)==p and q_of(x,y)==q
        if gcd(abs(x),abs(y)) != 1: continue
        found.setdefault(s,set()).add((x,y))

assert found == expected, (found, expected)
for gap in (6,10,12,14): assert gap not in found
assert invol(0,1)==(0,1)
assert invol(1,0)==(-1,5)
assert invol(3,-1)==(-3,14)
assert invol(1,1)==(-1,6)
print('VERIFY_OK')
print({k:sorted(v) for k,v in sorted(found.items())})
