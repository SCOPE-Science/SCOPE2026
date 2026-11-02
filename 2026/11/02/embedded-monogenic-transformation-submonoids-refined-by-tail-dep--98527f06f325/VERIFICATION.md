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
# Reproduction

Run `python verify.py` and `python counts.py` from a directory containing these two supplied files. Both use only the Python standard library.

`verify.py` exhaustively enumerates all labeled self-maps in degrees one to six, constructs their actual embedded generated submonoid by iterating powers, and partitions identical submonoids into equality classes. For every nonzero \((h,p)\) class it checks the formal-series coefficient predicted by the theorem and verifies that the number of generating transformations per class is \(\varphi(p)\) when \(h\le1\), otherwise one. It also tests zero classes for smaller periods. Results: the six exact monoid totals are \(1,4,26,237,2842,42488\); output terminates in `VERIFY_OK`.

`counts.py` independently generates integer partitions of each cyclic-set size, evaluates the number and order of permutations of that cycle type, and sums the finite total formula exactly with rational arithmetic. Values for degrees one to twelve are printed; the first six are cross-checked against exhaustive values. Output terminates in `FORMULA_OK`.

The exhaustive checks do not prove the statement for arbitrary degree; the complete proof is in `RESULT.md`. The exponential estimate relies on the formal-series coefficient bound evaluated at \(z=1/2\) and Stirling's formula, not on extrapolation from the tables.
