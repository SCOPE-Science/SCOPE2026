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
Run `python3 verify_kneser.py` and `python3 verify_family.py` with Python 3.10 or later (standard library only). Compare to `checks.txt`. The first program independently evaluates face membership by induced degrees and forbidden triples on all 32,768 subsets of \(\mathrm{KG}(6,2)\), then exhaustively validates the directed discrete-Morse Hasse graph, independently computes finite-field boundary ranks, and evaluates signed Lefschetz traces for all 720 symbol permutations. The second program independently enumerates the structural family and checks the matching for each \(4\le n\le9\). Both terminate with success markers only if all assertions pass. The files contain entire finite checks, not truncated examples.

The **infinite** classification follows from the step-by-step gluing and Hurewicz argument in `RESULT.md`, not by extrapolating the finite computations. No independent audit was performed, no higher-parameter result is claimed, and no equivariant homotopy equivalence is asserted.
