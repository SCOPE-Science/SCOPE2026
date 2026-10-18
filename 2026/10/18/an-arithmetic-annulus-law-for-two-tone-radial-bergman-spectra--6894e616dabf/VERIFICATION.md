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

# Verification details

Use Python 3 with the mpmath package and execute `python verify.py` from this package directory. The program checks direct quadrature against the independently expressed gamma ratio in five parameter cases, five beta/gamma normalization identities, nine large-degree approximations, 123 annulus-radius constructions, and 93 exact rational-periodicity comparisons (up to floating-point precision). The observed output is `VERIFY_OK`.

Analytic verification rests on the exact beta moment identity, the fixed-parameter gamma quotient, the logarithmic mesh lemma, Kronecker's torus density theorem, planar circle-addition geometry, and the diagonal Fredholm characterization. Numerical verification cannot certify arbitrary parameters, infinitely many monomials, or historical originality. The 2001 comparison was available at abstract level only.
