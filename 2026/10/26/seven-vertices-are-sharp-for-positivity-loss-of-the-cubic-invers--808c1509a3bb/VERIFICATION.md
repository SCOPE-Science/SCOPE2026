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

Run `python verify.py` from this package with Python 3.10+ and SymPy 1.12+. The script uses exhaustive permutation-orbit enumeration of all labeled simple graphs through six vertices, integer-polynomial determinants and cofactors, and exact rational inverse identities at four specified timesteps on the seven-vertex path. It neither trusts floating-point eigensolvers nor imports an external graph database.

The run produced 142 connected unlabeled graphs, 1,933 unordered off-diagonal cofactor checks, 1,932 immediately coefficientwise nonnegative cofactors, and one additional cofactor certified after multiplication by \((1+h)^{32}\). Because \(\det A_G(h)>0\) for positive timesteps, these certificates prove strict positivity over the **entire continuum** \(h>0\) for each enumerated graph. A separate exact rational witness proves negativity at the seven-vertex threshold. See `verification_output.txt` for the actual output.

The proof is finite-exhaustive for graph order at most six; it does not imply a universal result for larger, weighted or directed graphs. The four rational checks do not determine the full seven-vertex positivity interval. Independent external validation has not been performed.
