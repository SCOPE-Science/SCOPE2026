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

Run `python verify.py` using `requirements.txt`. An exact SymPy replay confirms the symbolic pair-orbit differences and polynomial remainder, then computes rational inverses of every grounded follower Laplacian for six rational conductance parameters at each of the orders \(3,4,5,6,7\). It compares the resulting \(1470\) pairwise traces to the analytical spectral formulas, checks all optimal orbit classes, and checks the rational example \(n=3\), \(t=2/5\): resistance advantage \(1/108\) for a same-part pair but coherence advantage \(5/342\) for a matched pair.

The reproducibility check requires a standard Python environment with SymPy. Symbolic identities and the provided proof establish the infinite-family result; checking finitely many graphs is not a substitute. Independent mathematical or editorial examination has not occurred.
