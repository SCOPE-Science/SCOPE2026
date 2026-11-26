---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduce the length-seven certificate

Run `node verify_length7.js` in this directory. The bounded checker enumerates all 64 normalized length-seven images. It verifies that `01` violates strict preservation for every candidate and that `001` violates weak preservation for every candidate except the two normalized survivors. It then checks least periods, the first and last bits, the proper long overlaps, and all 22 nonempty admissible inputs of length at most four for the two survivors. The final global preservation step uses Theorem 4 of Shallit, Shur and Zorcic, as cited in `RESULT.md`.
