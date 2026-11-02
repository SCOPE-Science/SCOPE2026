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

Run `python3 verify_aronhold.py` with Python 3.8 or later. All arithmetic is exact integers; no external library is required. The program reconstructs all 28 odd quadratic refinements over the binary 6-space, generates the 288 Aronhold heptads via the parity test, verifies 72/16 design frequencies, extracts the specified 28 incidence columns, and computes their 28-by-28 integer determinant by fraction-free Bareiss elimination. It returns `VERIFY_OK` only if the absolute determinant is seven. No read/write of external files or web access is required.

Limits: This computational certificate proves the displayed finite determinant and heptad enumeration only. The inference to the infinite formal integer lattice follows from the proof in RESULT.md. The program does not independently settle historical priority or any arithmetic variation in characteristic two.
