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

# Reproducibility and verification

The file `verify_paired_book.py` is a self-contained Python 3 standard-library program. Execute it using `python verify_paired_book.py` from the same directory as this file. The expected complete output is embedded as `verification_output.txt`.

The verifier builds \(B_r\) from its stated edges, enumerates all \(2^{2r+2}\) vertex subsets for each \(r=2,3,4,5,6,7,8\), and checks paired domination by direct closed-neighborhood coverage and recursive perfect-matching search of the induced graph. It separately constructs every claimed feasible family, compares exact vertex subsets with the direct test, checks each coefficient of the stated polynomial, and extracts inclusion-minimal sets by comparing every proper feasible subset. The tests cover 349,504 candidate subsets; 6,215 of these were paired dominating and 84 inclusion-minimal across the seven graph sizes.

All tests passed in the recorded execution. The proof in `RESULT.md` establishes the statement for every \(r\ge2\); the finite test is not an exhaustive verification of infinitely many graphs. No independent mathematical or bibliographic validation was conducted.
