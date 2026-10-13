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

# Reproducibility and limitations
The theorem is analytic. Reconstruct the normalized Laplacian from the cycle and alternating prices, verify the explicit proposed conductances satisfy the weighted budget, construct the complex polygon vector in the proof, and check the edge-chord bound and two-vertex Bloch spectrum. Equality of the Rayleigh quotient with the spectral gap is a global upper-bound certificate; uniqueness uses noncollinearity of successive circle chords at every vertex.

Run `python3 verify.py` with Python 3 and NumPy installed. This constructs the Laplacian from edge data for sampled rings, checks its numerical eigenvalues, verifies the polygon dual certificates, tests nonsymmetric feasible allocations, and checks the exact six-cycle rational example. The numerical tests provide consistency checks only. They do not establish the quantified all-size theorem, prove historical originality, or constitute an independent audit.
