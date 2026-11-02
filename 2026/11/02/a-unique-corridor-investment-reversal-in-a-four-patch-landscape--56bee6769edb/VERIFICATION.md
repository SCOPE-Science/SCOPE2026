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

# Reproducibility checks

The standalone `verify.py` uses Python 3.10+, SymPy and NumPy. Command: `python verify.py` in the directory containing the script. It passed 2,577 symbolic, exact-rational and numeric checks, including the two general characteristic-polynomial identities; rational determinant expansions independently computed from 24-term permutation sums; sampled positive-weight sign comparisons; exact evaluation of the radical threshold; and non-crossing parameter cases.

The general proof relies on a full determinant identity, Cauchy interlacing, positivity of Perron eigenvectors and monotonicity of the Perron root. Finite comparisons cannot establish the all-real-parameter theorem on their own. The original metapopulation-capacity publication was accessible as abstract and bibliographic information, not full technical text; historical priority is not certified. Independent scientific audit has not been performed.
