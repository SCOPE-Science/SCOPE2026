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

# Reproducibility and boundaries

Run `python3 check_pappus_rips.py` from this package with Python 3 (standard library only). The program constructs the graph from its standard LCF edge prescription, computes shortest paths, enumerates every clique at scales one to three, and executes the deterministic vertex-toggle Morse matching at scale two. It verifies the entire signed-gradient Hasse graph is acyclic rather than trusting a claimed count of critical cells.

It independently enumerates all 216 graph automorphisms by exhaustive distance-preserving backtracking; checks signed fixed-simplex Lefschetz sums at each nontrivial scale; computes the full character distributions; and separately checks the six-block tensor formula for every group element. The exact output ends with `PAPPUS_RIPS_HOMOTOPY_216_CHARACTERS_EXACT_OK`.

The proof for the scale-three join and for the terminal scale is structural and does not depend on extrapolating from experiments. The computation is exhaustive for this one 18-vertex graph, not for any family. The quotient conclusion uses rational coefficients; no claim is made about torsion of quotient spaces or integral homology representations at scale two. Independent audit is not performed.
