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

The proof uses a projector identity derived from automorphism transitivity, an exact Rayleigh budget certificate and an explicit corona spectral decomposition. The included standalone `VERIFY.py` was executed using installed NumPy, NetworkX and SymPy and returned `PASS 4209 finite assertions across vertex-and-edge-transitive families`. It constructs actual weighted Laplacian matrices on cycles, cliques, hypercubes, balanced bicliques and the Petersen graph, tests Fiedler leverage, candidate optimal gaps and budgets, random noninvariant assignments, local budget-preserving variations, and exact rational price/eigenvalue identities. These tests are supporting checks, not a certificate for all graphs and continuous prices. The exact all-parameter proof is given in RESULT.md. Independent audit has not been performed.
