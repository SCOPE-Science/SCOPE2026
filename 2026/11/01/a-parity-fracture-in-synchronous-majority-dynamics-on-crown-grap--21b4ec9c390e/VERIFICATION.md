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

# Verification record

Run `python verify_majority_crown.py` with a standard Python 3 interpreter. The program imports only `math` and `collections` from the standard library. It independently implements the exact formulas and a four-original-pair-type lifting iteration. For each integer size from one through fifty, every nonnegative composition of the size into four initial pair types is followed through the finite dynamics, retaining original category labels. It checks the number of fixed labelled states, primitive two-cycle *states*, total two-cycle attraction basin, and sharp maximum transient against the formulas in `RESULT.md`.

Separately, for each size one through seven, a vertex-level simulator explicitly enumerates neighbors of each of the two shores, independently updates all bits, and checks all labelled configurations. It verifies that every least period is one or two and that all four counts coincide with the analytic formulas. The text file `verification_output.txt` is the recorded output of the finished checker, ending with `CROWN_MAJORITY_PARITY_VERIFY_OK`.

There is no inference that finite tests cover arbitrary size. The infinite-family proof is the explicit two- and four-branch neighbor rule together with the six-case reduction, exact combinatorial counting, and Stirling analysis in `RESULT.md`. No independent external audit has been performed.
