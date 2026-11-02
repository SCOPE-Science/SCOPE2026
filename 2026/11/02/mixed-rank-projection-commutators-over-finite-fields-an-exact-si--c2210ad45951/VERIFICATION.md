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

# Verification and scope

The theorem's unrestricted proof is the block calculation and finite-field dot-pair enumeration in `RESULT.md`. All characteristic-two cases are included in the proof: the companion polynomial need not be separable.

Run `python verify.py` with Python 3. It independently enumerates normalized rank-one idempotents and their product-trace and commutator-rank cells for eleven parameter triples over fields of order \(2,3,4,5\). For the four \(n=4\) cases, explicit matrix multiplication independently checks idempotence, ranks, the cubic commutator identity, and the nilpotent-index distinction. The remaining cases check the dot-pair laws directly. It checks the total against \(q^{n-1}(q^n-1)/(q-1)\) and complement symmetry where supported by the implementation.

Actual execution passed all cases, with the final line: `VERIFY_OK all mixed-rank projection counts and cubic laws`.

The tests are finite and do not establish the infinite quantification. The source-literature comparison is subject to the residual publication-coverage limitation recorded separately in `REVIEW.md`. No external or independent mathematical validation is represented as having occurred.
