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

# Verification of the signed-cosine quadratic taper

The scalar \(SO(3)\) character coefficient is \((A_\ell+bB_\ell)/(\pi(2\ell+1))\), with \(A_\ell,B_\ell\) defined and derived in RESULT.md. Exact symbolic computation reproduces the closed rational formula for \(A_\ell/B_\ell\), the factorization proving the global minimum at \(\ell=2\), the two lowest-degree endpoint values, and the Euclidean Fourier witness \(-361/3726\) at radial frequency \(3\). These checks complement, rather than replace, the derivation in the proof.

Run `python check_rotation_taper.py` with Python 3, `sympy`, and `mpmath` installed. In the recorded run it passed the algebraic checks and 18 direct normalized-Haar character-integral comparisons (working precision 30 decimal places; maximum absolute residual approximately \(4.93\times10^{-32}\)). The finite checks do not constitute an infinite-degree enumeration. The proof covers every integer \(\ell\ge0\), every real parameter \(b\), and distinct finite rotation sets through the central Bochner criterion and a Peter--Weyl uniqueness argument.

No independent audit or independent validation has been performed. Novelty comparisons were bounded; equivalent work outside the inspected literature remains possible.
