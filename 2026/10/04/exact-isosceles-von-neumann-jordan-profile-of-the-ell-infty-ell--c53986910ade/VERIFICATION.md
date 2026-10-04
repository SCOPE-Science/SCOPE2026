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

The proof certificate is `verify.py`. It uses Python's exact rational `Fraction` arithmetic and has no nonstandard dependencies.

Run:

`python3 verify.py`

Expected terminal marker: `VERIFY_OK`.

The verifier independently reconstructs the six unit-sphere edges and six signed support forms. It enumerates every feasible support cell for \(N(x+y)\) and \(N(x-y)\), verifies that no feasible cell has an identically zero isosceles equality, extracts every rational endpoint, and confirms exactly 48 distinct orthogonal partition endpoints. It then derives the 12 distinct quadratic candidates and proves, by exact quadratic minimization on the two closed half-intervals, that the claimed left and right profiles dominate all candidates. Finally it checks the explicit maximizing pair.

The certificate does not prove novelty, does not classify other normed planes, and does not infer a continuum theorem from sampling.
