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

Execute `python3 artifacts/check_cubezero.py` with Python 3 and no third-party libraries. The script constructs explicit ring arithmetic, exhaustively enumerates all `2 x 2` matrices in the 14 configurations, calculates cubes through matrix multiplication, and checks each exact valuation layer separately. Compare the resulting output with `artifacts/verification_output.txt`. The final line must read `CUBE_ZERO_CHAIN_RING_CENSUS_OK 14`.

The tests include equal-characteristic quotient rings and mixed-characteristic integer quotient rings, plus genuine extension-field arithmetic in `F_4[t]/(t^2)`. Cases are finite and cannot establish the all-length theorem. The proof in `RESULT.md` supplies its quantifiers, nonstandard primitive-matrix counting lemma, and valuation lifting arguments; no independent scientific audit has occurred.
