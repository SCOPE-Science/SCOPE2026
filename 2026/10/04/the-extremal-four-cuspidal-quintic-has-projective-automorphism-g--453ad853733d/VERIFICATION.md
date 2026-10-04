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

Run `python3 artifacts/verify_target.py` from the package root. The checker uses only the Python standard library and exact arithmetic in \(\mathbb Q(\omega)\), with \(\omega^2+\omega+1=0\).

It checks three critical finite algebraic steps: all monomials of the implicit quintic have the same character \(\omega^2\) under \((x,y,z)\mapsto(\omega x,\omega^2y,z)\); the normalization coordinates have characters \(\omega,\omega^2,1\) under \(s\mapsto\omega s\); and the six permutations of the three equal-type cusp preimages split into exactly three cross-ratio-preserving even permutations and three odd permutations changing \(-\omega\) to \(-\omega^2\).

The checker does not establish the literature classification or the published local analytic cusp types; those are premises taken from Koras--Palka. It also does not turn the literature search into a proof of novelty. The mathematical proof of the automorphism upper bound is the normalization-lift plus cross-ratio argument stated in RESULT.md.
