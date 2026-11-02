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

# Reproducibility and mathematical limits

Execute `python verify.py` with Python 3. The program enumerates ordered vertex pairs and their complete distance-extension supports for \(H(d,q)\), for dimensions one through three and alphabet sizes two, three and four, independently checks the closed coordinate-type support formula and invariance for all pairs at a common distance, and checks cycles of lengths five through eight. Captured output is in `verification_output.txt` and ends `ALL_CHECKS_PASS`.

The general equivalence theorem is a mathematical argument based on the three-pebble back-and-forth and explicit three-variable distance formulas, not a computation. No code is claimed to verify all distance-regular graphs or independent priority. Independent mathematical audit was not performed.
