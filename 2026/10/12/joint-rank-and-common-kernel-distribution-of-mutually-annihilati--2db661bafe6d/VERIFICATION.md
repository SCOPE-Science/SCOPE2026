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

The proof is self-contained: a fixed joint kernel \(K\) induces a pair of maps from \(V/K\) into \(K\), and the requirement of trivial common kernel is handled by Möbius inversion in the subspace lattice. The separate injective-map count verifies the summed marginal for arbitrary prime powers.

Reproduce with `python3 artifacts/verify.py` in a standard Python 3 installation. The script enumerates square-zero matrices and multiplies them directly for \((n,q)=(1,2),(2,2),(2,3),(3,2)\); it verifies every rank/common-kernel stratum. It additionally tests the exact rank-sum identity for dimensions through eight and the field orders \(2,3,4,5\), using integer arithmetic rather than matrix enumeration for nonprime orders. Successful output ends with `VERIFY_OK_ANNIHILATING_RANK_STRATA`.

These finite checks are neither exhaustive over all dimensions nor a substitute for the proof; independent mathematical audit has not been performed.
