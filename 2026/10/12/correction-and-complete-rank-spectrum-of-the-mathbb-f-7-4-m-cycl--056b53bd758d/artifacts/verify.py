from collections import Counter
from itertools import product

p = 7
zero, one, w = (0,)*4, (1,0,0,0), (0,1,0,0)

def add(*terms):
    return tuple(sum(col) % p for col in zip(*terms))

def scale(n, u):
    return tuple((n*v) % p for v in u)

def mul(u, v):
    h = [0]*7
    for i,a in enumerate(u):
        for j,b in enumerate(v):
            h[i+j] += a*b
    for i in range(6,3,-1):
        h[i-2] += h[i]
        h[i-4] += h[i]
    return tuple(c%p for c in h[:4])

def power(u, n):
    x = one
    for _ in range(n):
        x = mul(x, u)
    return x

def evaluate(c, x):
    u = zero
    for coefficient in reversed(c):
        u = add(mul(u,x),coefficient)
    return u

def rank(c):
    echelon = {}
    for u in c:
        for j in range(4):
            if not u[j]:
                continue
            if j not in echelon:
                echelon[j] = scale(pow(u[j], -1, p), u)
                break
            u = add(u, scale(-u[j], echelon[j]))
    return len(echelon)

assert add(power(w,4),scale(-1,power(w,2)),scale(-1,one)) == zero
assert power(w,8) == (2,0,3,0)
assert power(w,16) == scale(-1,one) and power(w,32) == one
assert [d for d in range(1,5) if pow(7,d,32)==1] == [4]
alpha = add(scale(4,mul(w,w)),scale(-2,one))
assert mul(alpha,alpha) == scale(-1,one)
g = (alpha,scale(-1,add(one,alpha)),one,zero)
xg = (zero,*g[:-1])

messages = ((t,one) for t in product(range(p),repeat=4))
counts = Counter()
for a,b in [*messages,(one,zero)]:
    c = tuple(add(mul(a,f),mul(b,h)) for f,h in zip(g,xg))
    assert evaluate(c,one)==zero and evaluate(c,alpha)==zero
    counts[rank(c)] += 1
assert counts == {1:1,2:49,3:2352}
assert [counts[k]*(p**4-1) for k in range(1,4)] == [2400,117600,5644800]
print('Verified 2402 cyclic-code projective points:', sorted(counts.items()))
