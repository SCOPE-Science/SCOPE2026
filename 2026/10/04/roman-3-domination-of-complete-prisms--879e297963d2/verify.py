from itertools import product
from math import comb

def complete_prism(n):
    # A = 0..n-1, B = n..2n-1; each layer is K_n; matching i--n+i
    N = 2*n
    adj = [set() for _ in range(N)]
    for base in (0, n):
        for i in range(n):
            for j in range(i+1, n):
                adj[base+i].add(base+j)
                adj[base+j].add(base+i)
    for i in range(n):
        adj[i].add(n+i)
        adj[n+i].add(i)
    return adj

def is_r3(adj, lab):
    for v, x in enumerate(lab):
        s = sum(lab[u] for u in adj[v])
        if x == 0 and s < 3:
            return False
        if x == 1 and s < 2:
            return False
    return True

def classify_minimum(n, lab):
    A = sum(lab[:n])
    B = sum(lab[n:])
    if n == 4:
        if (A,B) == (2,3):
            a=lab[:n]; b=lab[n:]
            return (a.count(2)==1 and a.count(0)==n-1 and
                    b.count(1)==n-1 and b.count(0)==1 and
                    next(i for i,x in enumerate(a) if x==2) ==
                    next(i for i,x in enumerate(b) if x==0))
        if (A,B) == (3,2):
            a=lab[:n]; b=lab[n:]
            return (b.count(2)==1 and b.count(0)==n-1 and
                    a.count(1)==n-1 and a.count(0)==1 and
                    next(i for i,x in enumerate(b) if x==2) ==
                    next(i for i,x in enumerate(a) if x==0))
        return False
    if n == 5:
        if (A,B)==(3,3):
            return True
        if (A,B)==(2,4):
            a=lab[:n]; b=lab[n:]
            return (a.count(2)==1 and a.count(0)==n-1 and
                    b.count(1)==n-1 and b.count(0)==1 and
                    next(i for i,x in enumerate(a) if x==2) ==
                    next(i for i,x in enumerate(b) if x==0))
        if (A,B)==(4,2):
            a=lab[:n]; b=lab[n:]
            return (b.count(2)==1 and b.count(0)==n-1 and
                    a.count(1)==n-1 and a.count(0)==1 and
                    next(i for i,x in enumerate(b) if x==2) ==
                    next(i for i,x in enumerate(a) if x==0))
        return False
    return A == 3 and B == 3

def formula(n):
    if n == 4:
        return 5, 8
    if n == 5:
        return 6, comb(7,3)**2 + 10
    return 6, comb(n+2,3)**2

# Full direct brute force for n=4 and n=5.
direct_labelings = 0
direct_minima = 0
for n in (4,5):
    adj = complete_prism(n)
    best = 10**9
    mins = []
    for lab in product(range(4), repeat=2*n):
        direct_labelings += 1
        w = sum(lab)
        if w > best:
            continue
        if is_r3(adj, lab):
            if w < best:
                best = w
                mins = []
            mins.append(lab)
    fb, fc = formula(n)
    assert best == fb, (n,best,fb)
    assert len(mins) == fc, (n,len(mins),fc)
    assert all(classify_minimum(n,lab) for lab in mins)
    direct_minima += len(mins)

# Independent aggregate DP: for fixed layer sums A,B, local feasibility is exact.
def allowed(a,b,A,B):
    return not ((a <= 1 and A+b < 3) or (b <= 1 and B+a < 3))

def aggregate_count(n,A,B):
    states=[(a,b) for a in range(4) for b in range(4) if allowed(a,b,A,B)]
    dp={(0,0):1}
    for _ in range(n):
        nd={}
        for (x,y),cnt in dp.items():
            for a,b in states:
                if x+a <= A and y+b <= B:
                    nd[(x+a,y+b)] = nd.get((x+a,y+b),0) + cnt
        dp=nd
    return dp.get((A,B),0)

dp_values = 0
for n in range(4,61):
    expected_value, expected_count = formula(n)
    found_value = None
    found_count = 0
    for W in range(0, expected_value+1):
        c=0
        for A in range(W+1):
            c += aggregate_count(n,A,W-A)
        if c:
            found_value = W
            found_count = c
            break
    assert found_value == expected_value, (n,found_value,expected_value)
    assert found_count == expected_count, (n,found_count,expected_count)
    dp_values += 1

print("VERIFY_OK")
print("full_bruteforce_n = 4,5")
print("direct_labelings_checked =", direct_labelings)
print("direct_minimum_functions_checked =", direct_minima)
print("aggregate_exact_DP_n = 4..60")
print("aggregate_parameter_values_checked =", dp_values)
print("all Roman-{3} domination numbers matched")
print("all minimum-function counts matched")
print("all n=4 and n=5 minimum functions matched the structural classification")
