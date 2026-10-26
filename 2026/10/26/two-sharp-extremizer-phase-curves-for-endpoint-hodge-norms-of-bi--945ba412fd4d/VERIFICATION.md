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
# Verification of the displayed theorem

Run `python verify_prism.py` with SymPy. The program checks three layers of evidence: (1) rational algebra for the source currents and competing edge-orbit norms; (2) global polynomial coefficient certificates, including 31 finite parameter pairs in the intermediate regime; and (3) direct exact-rational incidence-pseudoinverse computations on ten small graphs, totaling 362 edge columns. Success is indicated by its printed `PASS` line.

The proof is the spectral decomposition and all-parameter coefficientwise inequalities in `RESULT.md`. Finite graph computations only provide corroboration. The script does not certify an independent review or rule out unpublished equivalent work. The method is restricted to simple unit-resistance graph edges and canonical orthogonal cut/cycle projections.
