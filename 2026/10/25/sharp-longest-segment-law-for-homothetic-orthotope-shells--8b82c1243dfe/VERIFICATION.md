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
The proof in `RESULT.md` establishes the global real-parameter theorem. The bundled rational checker evaluates finite examples and tests all candidate closed segments joining grid points in dimensions two, three and four at three rational thicknesses; it uses exact interval intersection to decide whether any interior point meets the open inner orthotope. It also checks sharp constructions at unequal side lengths. The checker outputs `ORTHOTOPE_SHELL_OK cases= 17658` on success.

To reproduce, run `python3 checker.py` in the extracted directory. Python standard library is the only dependency. Finite tests do not imply the all-dimensional result; the two-coordinate lemma, interval-Helly reduction and equality proof are the essential analytic evidence. No external or independent scientific audit has been performed.
