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

The proof is contained in `RESULT.md`, and the executable exact-check program is `verify_rsd_coupon.py`. Run `python verify_rsd_coupon.py` with an ordinary Python 3 interpreter. It uses only the standard library, performs exact rational calculations, and produces `VERIFY_OK n=1..12 coupon_exact=joint_probability_exact direct_ranks_n=1..4 count=13863` on success.

The verifier exhaustively conditions on a fixed final RSD assignment for \(n\le4\), computes the coupon-singleton law by a distinct finite-state Markov recursion for \(n\le12\), and compares with the generating polynomial derived from the RSD position-indexed formula. Conditional symmetry makes conditioning on the fixed final assignment legitimate. Enumerations are finite corroboration, not a general proof; the independent uniform rank/coupon coupling and finite-product identity establish the theorem for all finite \(n\).

The coupon integral formula and asymptotic exponential law are previously established results, not newly independently certified external discoveries. No external independent audit has been performed.
