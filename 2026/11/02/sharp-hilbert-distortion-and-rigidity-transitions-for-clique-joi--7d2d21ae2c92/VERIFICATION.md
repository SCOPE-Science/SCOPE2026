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

# Verification performed

The universal lower bound is derived from the Hilbert quadrilateral identity, rectangle incidence counts, two exact centroid variance identities, and the graph-distance constraints. The exact upper bound is attained by three explicitly given orthogonal regular simplices. Rigidity and nonrigidity are proved through equality analysis and a separate translation construction. These are mathematical arguments, not computer inferences.

The bundled `CHECKER.py` uses only standard-library `fractions.Fraction`. A completed exact-arithmetic run checked 224 triples with \(2\le n\le m\le8\) and \(1\le h\le8\), and 20 alternative balanced strict-phase embeddings. All 154006 enumerated pair-distance inequalities passed, together with the threshold and simplex-radius identities. The checker should be run from the unpacked package using `python CHECKER.py`.

No finite enumeration establishes the universal parameter ranges or the optimal-classification statement; the analytical proof does. No independent mathematical audit, formal theorem prover, or external certificate was used. Earlier matching claims under different graph or semidefinite terminology remain a source-priority risk.
