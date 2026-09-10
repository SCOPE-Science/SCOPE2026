"""LGV certificate: Fischer Sec-4 determinant for (m,n,k)-Magog trapezoids (P=Q=1),
summed over weakly-increasing bottom rows. Validated vs brute force at
(0,3,2),(0,4,2),(0,4,3),(0,5,2),(0,5,3). Evaluates the (0,6,3) LGV anchor leg.
"""
from math import factorial
from itertools import combinations_with_replacement
from lgv2 import det_int

def binom(n, k):
    if k < 0: return 0
    num = 1
    for i in range(k): num *= n - i
    return num // factorial(k)

def lgv_total(m, n, k, P=1, Q=1):
    total = 0; nb = 0
    per_row = {}
    for btpl in combinations_with_replacement(range(1, m+n+1), k):
        b = list(btpl)
        M = []
        for i in range(1, n+1):
            row = []
            for j in range(1, n+1):
                if i <= n-k:
                    e = (binom(j+k+m-3, 2*j+m-i-3) + (P+Q)*binom(j+k+m-3, 2*j+m-i-2)
                         + P*Q*binom(j+k+m-3, 2*j+m-i-1))
                else:
                    bi = b[i-(n-k+1)]
                    e = (binom(j+m+n-bi-i-1, 2*j+m-bi-i-1)
                         + P*binom(j+m+n-bi-i-1, 2*j+m-bi-i))
                row.append(e)
            M.append(row)
        d = det_int(M)
        per_row[btpl] = d
        total += d; nb += 1
    return total, nb, per_row

if __name__ == "__main__":
    import json
    for (n, k) in [(6, 3)]:
        tot, nb, per = lgv_total(0, n, k)
        print(f"(0,{n},{k}): LGV-sum={tot} (bottom rows: {nb})", flush=True)
        with open(f"lgv063.json", "w") as f:
            json.dump({"total": tot, "nbottom": nb,
                       "per_row": {str(k): v for k, v in per.items()}}, f)
