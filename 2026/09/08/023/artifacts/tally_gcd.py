"""Method A: gcd-based enumeration of integers coprime to 30030."""
import math, csv, collections
P = 2*3*5*7*11*13
assert P == 30030
cop = [n for n in range(1, P+1) if math.gcd(n, P) == 1]
assert len(cop) == 5760, len(cop)
gaps = [cop[i+1]-cop[i] for i in range(len(cop)-1)]
gaps.append((P + cop[0]) - cop[-1])
c = collections.Counter(gaps)
with open("histogram_a.csv","w",newline="") as f:
    w = csv.writer(f); w.writerow(["gap","count"])
    for d in sorted(c): w.writerow([d, c[d]])
print(dict(sorted(c.items())))
print("sumN", sum(c.values()), "mom", sum(k*v for k,v in c.items()))
