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

# Verification of exact finite identities

Run `python3 verify_fixed_layers.py` with Python 3. The script needs only standard-library modules and no external files. Its last successful execution reported:

`VERIFY_OK brute_vs_dp=114 exact_polynomial_checks=64 Pisano_convolutions=4 two_top_coefficients=9 rational_arithmetic=PASS`

The 114 comparisons independently enumerate all legal fixed-weight index subsets for \(2\le s\le7\) and length \(0\le L\le18\), and compare each with a residue-aware transfer dynamic program. The 64 exact polynomial checks cover four weights and the first 16 positive Pisano blocks. Four independent period-convolution calculations check all leading and next-order coefficients and limiting fractions displayed in the statement. In addition, nine higher-index examples (weights 2 through 10) independently recover the top two coefficients by finite differences of the exact transfer counts, agreeing with the general convolution formulas.

## Mathematical proof dependency
The infinite parts are the periodic-transfer rational generating function, the precise degree bound for its pole at one, the one-adjacent-pair correction with an error from multiple constrained coincidences, and the small-eigenvalue vanishing argument for four low weights. These steps are fully stated in `RESULT.md`. The finite checks independently corroborate the arithmetic, but cannot prove eventual polynomiality or exclude a hidden infinite counterexample by themselves.

## Limits
The program is not a proof assistant and offers no independent audit. There is no claim of optimality of the Pisano quasi-polynomial period or of uniformity when the fixed weight increases.
