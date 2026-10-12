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

# Verification record

`python3 CHECK.py` independently enumerated all parent-choice sequences for sizes \(2\le n\le9\), calculated exact rational covariance coefficient vectors, and matched those against the finite product formula. It also checked the parity identity and the generating-polynomial derivative at \(z=1\); 58 exact coefficient/identity cases passed. Fourier reconstruction for sizes \(2\le n\le9\), moduli \(2\le q\le9\), and all residue classes passed 352 comparisons with numerical tolerance \(10^{-9}\).

The proof of the infinite assertions is analytic: the conditioning recurrence, its solved product, fixed-root Gamma asymptotics, and phase-subsequence argument are explicitly supplied in RESULT.md. Finite checker passes are not infinite proofs, and no independent review is claimed.
