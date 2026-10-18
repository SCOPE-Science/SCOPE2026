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

Run `python3 verify.py` using Python 3.10 or later. No nonstandard packages, network access, or external datasets are needed. The program independently constructs the unordered cubical cells and matrices from the labeled complete graph; it does not trust precomputed matrices. It tests the signed boundary identity, all exact determinant witnesses, the mod-two rank, the cohomology lattice basis, the fifteen elementary cup products' spanning property, and an explicit integral order-two cup representative.

The determinant tests are finite, exact Bareiss elimination. The characteristic-two ranks are exact bitwise Gaussian elimination. In particular, a nonzero square determinant over the rationals, a mod-two rank loss, and a primitive smaller minor are used together to prove the full Smith invariants: this is not an inference from floating-point ranks. The four listed minors and cochain-support sets are encoded visibly in the verifier and are also explained in `RESULT.md`.

The successful local invocation of this packaged script returned `VERIFY_OK cells=(15,60,45) ranks=(14,36) H2=Z^9+Z/2 cup_surjective=True torsion_order=2`.

The verification addresses the finite mathematical theorem and does not establish priority against all possible literature or independent scientific validation. No unpublished or remote computation is required.
