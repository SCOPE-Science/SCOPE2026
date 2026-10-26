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

Install Python 3 and the dependency listed in `requirements.txt`, then run `python verify.py` from the package directory. The program reconstructs the Fourier formulas, checks four symbolic identities against the complete six-degree rational numerators, and tests the first row of the update against exact four-by-four inverses at 60 rational combinations. Every matrix row sum is also checked exactly. Successful output is:

`SYMBOLIC_OK 4 Fourier-to-polynomial rational identities`

`VERIFY_OK 4 symbolic identities; 240 exact direct-matrix entries; 60 stochastic row checks`

These finite matrices and symbolic polynomial identities support the all-parameter analytical reasoning; finite sampling alone does not prove unconditional nonnegativity, unique positive zeros, or novelty. The latter follow from explicit coefficient signs and Descartes' rule in RESULT.md. The full historical literature remains open to independent audit.
