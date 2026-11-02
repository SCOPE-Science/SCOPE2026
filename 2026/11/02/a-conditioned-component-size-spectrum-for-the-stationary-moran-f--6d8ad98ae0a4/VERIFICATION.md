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

Run `python3 verify.py` with Python 3's standard library. The program reconstructs every admissible independent parent-choice vector on \(2\le n\le6\), accumulates the resulting component-size histogram and root count, and compares its rational expectations after several exponential tilts with a separately implemented exact triangular recurrence. It also compares the integral formula with finite-size recurrences at six tilt values. The verified run returned `PASS: 170 independent exact-enumeration, recurrence, and numerical assertions`.

The proof's non-finite inputs are the explicitly stated independent-Bernoulli local central limit estimate, the Euler approximation of a finite triangular system and McDiarmid's bounded-difference inequality. The program is not an infinite-sample proof and does not independently establish literature priority. The complete mathematical justification and hypotheses are in `RESULT.md`.
