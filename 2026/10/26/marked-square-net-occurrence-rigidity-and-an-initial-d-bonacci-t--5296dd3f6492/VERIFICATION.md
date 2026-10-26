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

# Reproducibility

From the directory containing these files, run `python3 verify_net_occurrences.py` using a standard Python 3 environment. Expected exact stdout is in `verification_output.txt`; the checker uses only Python's standard library.

The first family of tests exhaustively enumerates admissible binary and ternary interiors in the stated finite ranges and checks the entire set of net occurrences, including their starting positions and lengths. The second family independently applies the substitution and compares observed net counts and, at the transition iterate, observed positions with the closed form, for dimensions two through eight. There were 173 marked-word tests and 49 finite substitution iterates.

The only verification of the all-length and all-dimension theorem is its symbolic argument: the program does not purport to exhaust infinitely many inputs. Additional assumptions, boundaries, and the exception for already known binary Fibonacci words are detailed in `RESULT.md`.
