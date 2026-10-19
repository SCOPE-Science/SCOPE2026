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

# Reproducibility and verification

The theorem's infinite-domain upper bound is analytical: pair the two sides of the affine coefficient, integrate the Abel kernel, differentiate, eliminate two square roots into a degree-at-most-three polynomial, and apply Rolle's theorem separately to the two open outer radial intervals. No finite enumeration is used as the proof of the upper bound.

Execute `python verify.py` in a Python environment providing `sympy` and `mpmath`. The executable checks the exact derivative, the cubic eliminant degree, radial reduction across positive and negative jump locations, nine independent high-precision quadratures, and six nonoverlapping sign-changing brackets. The sign brackets are checked by interval enclosures, using exact rational and \(\pi\)-dependent coefficients, with the inverse cosine evaluated as \(\operatorname{atan2}(\sqrt{1-z^2},z)\) on \(0<z<1\). All checks passed in the delivered execution.

The six bracket pairs are \((19/10,21/10)\), \((9/2,24/5)\), \((14,16)\), \((46,48)\), \((100,102)\), and \((149,151)\); switching radii are one and five. The analytical derivative bound forces all six sign-changing roots to be simple. As an independent literature cross-check, Chen–Jin–Li–Lu, arXiv:2610.11916v1, Theorem 1.1 and its proof, establish six simple first-order zeros for two positive jumps.

The package does not provide exact algebraic expressions for the roots, a certificate for all finite-perturbation cycles, or an independent audit of literature priority. The interval calculations support the explicit example; they are not substituted for the universal Rolle argument.
