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
Run `python3 verify.py`.

The checker reconstructs finite witnesses for the theorem's tail on the grid
\[
2\le b\le10,
\qquad
1\le n\le50.
\]
For each pair it computes
\[
g=\gcd(n,b-1),
\qquad
T=\max_{1\le j\le(b-1)/g}s_b(jn),
\]
and tests several consecutive admissible target values beginning at \(T\). It uses the distinct-power construction behind the progression theorem to build an actual multiple of \(n\) with each requested digit sum, then independently checks divisibility and digit sum.

The checker also verifies sampled additive-closure identities by concatenating disjoint base-\(b\) blocks.

This finite replay is regression evidence only. The infinite theorem is proved symbolically in `RESULT.md`.
