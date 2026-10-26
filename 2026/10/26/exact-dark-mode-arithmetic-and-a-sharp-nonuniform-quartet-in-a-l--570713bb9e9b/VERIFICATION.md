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
The analytic proof is contained in RESULT.md and uses no external executable for the infinite-chain conclusion. The included executable files can be run from the same directory with `python verify.py` (SymPy) and `python check_numeric.py` (NumPy).

`verify.py` performs exact cyclotomic reductions for every admissible pair of indices and every \(N\in\{2,\ldots,13\}\), verifies the absence of any nonunit repeated hopping ratio in this entire finite range, and confirms the first nonunit resonance at \(N=14\), \(s=3\), \(k=5,11\). It also proves the two algebraic energies from the four-site characteristic polynomial. Its integer-polynomial remainder calculations are exact.

`check_numeric.py` separately verifies clean-chain dark energies, end-site overlaps and sample lossy spectra at three values of the family parameter. Finite floating-point checks corroborate but do not establish the infinite family, which follows from the displayed sine formulas and exact sums.

The source paper supplies the model and general secular equation. No unpublished external certification, independent audit or formal proof-assistant verification is claimed.
