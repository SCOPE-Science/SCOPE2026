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

The exact recurrence and Gaussian coefficient norm are reconstructed in RESULT.md. For balanced orders, the critical factorial-energy ratio satisfies \(1-n/(2\ell)+O(\ell^{-2})\); its product is comparable to \(\ell^{-n/2}\), and the additional projected angular norm is comparable to \(\ell^{n/2-1}\). These comparisons verify both convergence cutoffs and the divergence of the full symbol-weighted norm. The proof is valid for all stated integer orders and arbitrary complex phases of nonzero coefficients.

Run `python CHECK.py` in the same directory for reproducible exact-rational checks of factorial identities at sample parameters and diagnostic asymptotic checks. Finite checks cannot certify the infinite statements; those are established in the proof. This package has no separate independent mathematical audit.
