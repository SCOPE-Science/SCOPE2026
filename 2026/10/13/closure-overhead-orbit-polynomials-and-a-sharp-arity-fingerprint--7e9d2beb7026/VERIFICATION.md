---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification of the meet-tree orbit-polynomial theorem

Run the embedded standard-library Python program `verify.py` with `python3 verify.py`.

## Exact replay result

```
Direct canonical enumeration: 421 shapes on <=11 vertices
GF and direct n,w,k census: VERIFIED for k<=6, n<=6
k=1 totals=[1, 1, 1, 1, 1, 1]
k=2 totals=[1, 2, 5, 15, 48, 166]
k=3 totals=[1, 2, 6, 20, 72, 282]
k=infinity totals=[1, 2, 6, 21, 78, 313]
unrestricted n=1: [1]
unrestricted n=2: [1, 1]
unrestricted n=3: [2, 3, 1]
unrestricted n=4: [4, 9, 6, 2]
unrestricted n=5: [9, 25, 27, 14, 3]
unrestricted n=6: [20, 72, 103, 80, 32, 6]
VERIFY_OK 740 exact coefficient and combinatorial assertions; 421 independent rooted shapes; 6 arities
```

The cycle-index engine expands the bivariate ordinary generating-function equation by exact rational arithmetic and total degree. The separate direct engine recursively enumerates unordered rooted trees with black and white vertices, rejects white unary vertices, checks canonical uniqueness, and computes each tree's multiset of pairwise meets of black vertices using explicit pathwise lowest common ancestors. For all six tested degree caps, it compares individual bivariate coefficients with the independent generating-series engine. Further assertions verify the first arity-discrepancy polynomial, the full range of overheads, unrestricted OEIS A052300 totals and the ordinary rooted-tree/full-binary-tree endpoint counts.

The enumeration is exhaustive over the finite domain of at most six selected vertices, corresponding to at most eleven generated vertices, and degree caps one through six. It is not an exhaustive verification for larger subsets or infinitely many arities. The structural proof, not this program, establishes the unrestricted theorem. The program has no external dependencies and does not access a network.
