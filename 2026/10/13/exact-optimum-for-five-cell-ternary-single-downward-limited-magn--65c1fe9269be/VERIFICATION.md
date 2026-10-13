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
# Reproducible verification

The listed code is stored in `data/codewords.txt`. Execute `python tools/verify_code.py` from the package root. This standard-library program asserts 45 distinct ternary words and checks disjointness of their possible received sets. Observed output: `CODE_OK size=45 distinct_received=185`.

Run `python tools/solve_packing.py` and `python tools/solve_pairs.py` with `scipy` and `numpy` installed and a working HiGHS mixed-integer solver. Observed outputs: `PACKING_OPTIMAL 45 upper=45 lower=45 received_constraints=243` and `GRAPH_OPTIMAL 45 upper=45 lower=45 vertices=243 edges=1890`. Neither script accepts a feasible incumbent in lieu of globally optimal solver status, and each checks the reported dual bound and relative mixed-integer gap.

The receiver-based packing model and pairwise confusability model are built separately from elementary channel definitions. They independently support the finite upper bound, but both rely on the computational correctness of the mixed-integer solver; this is not a solver-independent formal proof certificate. No claim is made for other word lengths, alphabets, or multiple errors.
