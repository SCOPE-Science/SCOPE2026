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

The packaged `verify.py` was read from its actual path before execution.

For each tested triple \(p,n,k\), it forms
\[
R=\mathbb Z/(p^n),
\qquad
I=(p^k),
\]
and creates the ideal-based graph directly from the condition \(xy\in I\). It then identifies the predicted \(m\) universal socle lifts, checks the valuation-one neighborhood when \(k\ge3\), exhaustively enumerates all total dominating subsets, and compares their cardinality counts with the coefficients of
\[
(1+x)^N-(1+x)^{N-m}-mx.
\]
It also enumerates all paired dominating two-sets and checks the formula
\[
m(N-m)+\binom m2.
\]

Exact output:

```text
p=2 n=2 k=2 vertices=1 universal=1 total_coeffs=[0, 0] paired_min_pairs=0
p=2 n=3 k=2 vertices=2 universal=2 total_coeffs=[0, 0, 1] paired_min_pairs=1
p=3 n=2 k=2 vertices=2 universal=2 total_coeffs=[0, 0, 1] paired_min_pairs=1
p=2 n=3 k=3 vertices=3 universal=1 total_coeffs=[0, 0, 2, 1] paired_min_pairs=2
p=3 n=3 k=3 vertices=8 universal=2 total_coeffs=[0, 0, 13, 36, 55, 50, 27, 8, 1] paired_min_pairs=13
p=2 n=4 k=3 vertices=6 universal=2 total_coeffs=[0, 0, 9, 16, 14, 6, 1] paired_min_pairs=9
p=2 n=5 k=4 vertices=14 universal=2 total_coeffs=[0, 0, 25, 144, 506, 1210, 2079, 2640, 2508, 1782, 935, 352, 90, 14, 1] paired_min_pairs=25
VERIFY_OK
```

The finite replay is corroborative. The arbitrary finite-chain-quotient result follows from the filtration count, equations (2)–(5), and direct subset enumeration in the proof.
