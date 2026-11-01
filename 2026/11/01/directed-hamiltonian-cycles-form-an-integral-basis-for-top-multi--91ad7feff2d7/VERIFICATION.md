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

# Direct verification and limits

The standalone program `verify_hamiltonian_top.py` requires Python 3 and only standard-library modules. Run `python3 verify_hamiltonian_top.py`; its expected full stdout is embedded as `verification_output.txt`. It rebuilds all Hamiltonian-path facets and ridges for each input digraph, signs each formal Hamiltonian-cycle boundary integrally, tests exact cancellation in codimension one, and computes the entire top boundary rank modulo two independently of the asserted rank formula. It checks exhaustive three- and four-vertex digraph families, additional reproducible deterministic cases and explicit dihedral wheel orbits.

The exhaustive verification covers 64 digraphs of order three and 4,096 of order four; it does **not** exhaust all directed graphs of larger order or prove homotopy equivalences. The all-graph theorem follows from the ridge-completion and direct-sum boundary proof in `RESULT.md`. It is a top-degree homology result, not a classification of lower groups. Integrality follows from one primitive simplex-boundary generator in each disjoint top-boundary block, not from modular experiments. The induced integral group-module assertion follows from exact signed simplicial actions. No external independent audit has been performed.
