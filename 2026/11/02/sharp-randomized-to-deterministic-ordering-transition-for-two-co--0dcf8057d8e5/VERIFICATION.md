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

# Reproduction and boundaries

Run `python verify.py` in this directory, after installing `requirements.txt`. The checker performs symbolic algebra of the two exact affine maps and their invariant moments, verifies strict curvature-phase algebra and asymptotic constants, and exhaustively checks rational order histories of lengths \(1\) through \(9\) under six rational parameter choices. Its run completed successfully with 122 reported exact checks (some checks combine several symbolic identities). It also verifies a rational example with both order probabilities.

The proof in `RESULT.md` covers every \(a,b>0\), \(\delta\ne0\), and \(0<h<1/\max\{a,b\}\) analytically. Finite enumeration does not establish an infinite-parameter theorem; it tests the formulas in a bounded set. There is no numerical Monte Carlo inference, optimizer oracle or external certificate. Independence of validation has not been established. Specialized prior publications may affect priority of the exact theorem.
