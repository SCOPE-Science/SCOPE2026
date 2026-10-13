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

The verification script `artifacts/verify.py` uses only the three source generator matrices and the ring coordinate model described in the proof. For each matrix it enumerates all \(4^2=16\) coefficient pairs, computes Hamming weight directly from the resulting ring-coordinate word, and compares the exact distribution with the claimed polynomial. It then independently recomputes the distribution from the three nonzero binary residue weights and the union support of the two residue generators.

The replay prints, in source-table order, the distributions
\[
\{0:1,4:9,6:6\},\qquad
\{0:1,4:3,6:6,8:6\},\qquad
\{0:1,4:6,8:9\},
\]
and terminates with `VERIFY_OK`.

The finite replay verifies only these three fixed printed generators. The general ring identities used to justify the binary-pair model were checked against the primary source; the script is not evidence for unrelated free codes or for completeness of the source classification itself.
