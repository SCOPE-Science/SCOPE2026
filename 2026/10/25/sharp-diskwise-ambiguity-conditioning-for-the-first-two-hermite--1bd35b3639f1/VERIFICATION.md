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

The exact Hermite ambiguity identity fixes the normalization \(s=\pi(x^2+\omega^2)\). A direct differentiation of \(F_w(s)=e^{-s}[1+w s(s-2)]\) gives all candidate minima, with no unsearched critical branches. The monotone-intersection argument proves global uniqueness for every \(R>2\), while the strict endpoint argument proves uniqueness below \(2\) and the optimizer interval at the threshold. The implicit root is certified unique by its derivative sign, not by numerical root finding.

The supplied self-contained Python 3 program `check.py` ran successfully and printed `PASS: 1698 numerical assertions`. It checks exact critical-point minimization against sampled radii and weights, active-minimum coincidence, monotone allocations, the short- and long-radius regimes, and direct formula evaluations. It requires only Python's standard library. Numerical tests neither prove novelty nor replace the continuum analytical proof.

The lower singular value is sharp for arbitrary \(\Phi\in L^2(D_R)\), since small positive-area annuli approach all radial minimizers. The proof makes no sharpness claim after restricting to physically realizable ambiguity functions of signals. No external or independent validation has been performed.
