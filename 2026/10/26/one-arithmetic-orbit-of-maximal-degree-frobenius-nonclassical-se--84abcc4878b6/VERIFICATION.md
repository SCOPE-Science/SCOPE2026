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

Work in \(\mathbf F_4=\mathbf F_2[\alpha]/(\alpha^2+\alpha+1)\). The normal-form theorem is cited in `RESULT.md`; the package verifies the new finite classification.

Build and run from this directory: `g++ -O3 -std=c++17 verify_cpp.cpp -o verify_cpp && ./verify_cpp`; separately run `python verify_python.py` (requires NumPy). Both programs contain the full finite-field arithmetic and need no external data. Confirm their displayed outputs against `REFERENCE_OUTPUT.txt`.

The C++ program evaluates all \(4^{10}\) normalized coefficient vectors, enumerates all \(4^9\) matrices, discards singular ones, and computes the exact orbit of a known smooth example, confirming exhaustive counts. The Python program independently evaluates the coefficient vectors using vector filtering and constructs a 960-member orbit under four projective generators. The differential calculation in `RESULT.md` proves why these finite checks certify geometric smoothness over the algebraic closure.

The cited normal-form theorem was examined in its proof and example sections. This package does not reproduce or independently reproves its full Koszul-complex argument. The results have not received an external independent audit, and originality remains subject to unindexed literature.
