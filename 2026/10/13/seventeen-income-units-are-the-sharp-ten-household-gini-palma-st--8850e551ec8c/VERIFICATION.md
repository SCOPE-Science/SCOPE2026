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
For a sorted ten-household profile \(x\) of total \(S\),
\[
G(x)=\frac{D(x)}{10S},\qquad D(x)=\sum_{i<j}(x_j-x_i),
\]
and
\[
P(x)=\frac{x_{10}}{x_1+x_2+x_3+x_4}.
\]

The embedded `verify_gini_palma_boundary.py` enumerates every positive integer partition into ten parts for \(10\le S\le17\), verifies profile counts \(1,1,2,3,5,7,11,15\), and finds zero strict reversals through total \(16\) and exactly two at total \(17\).

Run `python3 verify_gini_palma_boundary.py`. The first output line must be `VERIFY_OK`.

All classification comparisons use integers or exact rational arithmetic.
