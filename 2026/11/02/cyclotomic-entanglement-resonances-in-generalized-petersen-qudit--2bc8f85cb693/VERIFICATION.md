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

# Reproduction and scientific limits

Run `python verify.py --spectra` in a Python 3.10+ environment with NumPy as specified in `requirements.txt`.

The script reconstructs the cubic generalized Petersen graph from its three edge families, then independently forms the balanced cut matrix and performs finite-field Gaussian elimination. Its separate polynomial-arithmetic implementation evaluates the claimed gcd and rank formula without building the proof's circulant block. Exact checks cover four primes, \(2\le m\le30\), and every allowed skip, giving 1,740 graph-rank comparisons. The two explicit five-step formulas are also tested for \(6\le m<300\). Five direct phase-coefficient singular-value checks compare the predicted complete nonzero spectra, not just the ranks. These were executed successfully.

The infinite-parameter theorem is established by the exact character-sum, block-kernel and polynomial-module proofs in `RESULT.md`; finite tests are supplementary. The code does not assess arbitrary cuts, composite local dimensions or physical noise.
