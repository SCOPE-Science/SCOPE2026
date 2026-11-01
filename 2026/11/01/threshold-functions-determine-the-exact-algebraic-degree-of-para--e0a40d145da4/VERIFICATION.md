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

# Reproducibility and limits

Run `python3 verify.py` from the extracted package; the script needs only Python standard-library modules. The completed run returned:

`CUBE_DEGREE_CHECK_OK: 72172 exact finite checks; witness counts 2,12,102,1880; signed 2D clipping verified`

The program tests the subset-sum coefficient signature for every one of the \(2^{2^d}\) Boolean vertex labelings for each \(1\le d\le4\); verifies the published low-dimensional threshold counts are realized using bounded integer-weight witnesses; and cross-checks signed truncated-power volumes of two-dimensional cube cuts against exact rational polygon clipping. The bounded witness enumeration is **not** a complete classification by itself; independently published counts from OEIS A000609 supply those examples. Finite rational computations corroborate the symbolic mechanism, but universal sharpness follows from the all-dimensional proof in RESULT.md. No independent mathematical audit or formal proof certificate has been performed.
