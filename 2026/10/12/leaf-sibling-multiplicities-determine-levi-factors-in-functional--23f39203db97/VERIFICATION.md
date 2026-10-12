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
# Verification

The proof is symbolic and valid in arbitrary finite dimension under the stated characteristic-zero, acyclic functional-square, and no-isolated-vertex hypotheses. The critical identities are the square relation \(D(e_{\sigma(v)})=2d_{vv}e_{\sigma(v)}\) and the mixed-product relation \(c_vd_{vu}e_{\sigma(v)}+c_ud_{uv}e_{\sigma(u)}=0\).

`verify.py` reconstructs these linear equations independently. It enumerates every labeled acyclic partial functional graph on \(2\) through \(5\) vertices with no isolated vertices, assigns deterministic nonzero edge weights, computes the derivation-space nullity modulo two large primes, and compares it with
\[
|S|(1+|L|)+\sum_p\binom{\lambda_p}{2}.
\]
There are \(892\) tested forests. The expected replay output is `VERIFY_OK cases=892 primes=2`.

The finite computation is not an infinite-dimensional or characteristic-zero proof; it is a regression check for the closed formula and indexing conventions. Positive characteristic and isolated vertices are outside the claim.
