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

# Reproducible verification

Run `python3 checks/verify.py` with Python 3. The script has no nonstandard dependencies. It performs exact integer-coordinate checks in the quadratic ring for each greedily constructed base-phi word, exact Fibonacci recurrence arithmetic, exhaustive enumeration of eight even Lucas intervals, and finite transition-inequality checks. The greedy sign selection uses 110-digit decimal arithmetic; every final representation is separately checked as an exact integer-coordinate identity, and the theorem does not rely on any floating-point inference.

The verified outputs include the eight maxima `2,5,13,34,89,233,610,1597`, their witnesses `4,10,26,68,178,466,1220,3194`, the unique minimum index at the left Lucas endpoint in each interval, 2,213 tested integers, and 9,506 matrix-state inequalities. The proof in `RESULT.md` supplies the quantifiers and the infinite inequality induction. These tests do not constitute independent mathematical validation or certify bibliographic priority.
