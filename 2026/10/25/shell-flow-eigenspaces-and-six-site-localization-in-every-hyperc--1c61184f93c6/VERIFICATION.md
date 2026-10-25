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

Run `python3 check_cycle.py` with Python 3.8 or later; only standard-library packages are used. The script tests dimensions \(3\) through \(9\), all interior shell pairs and both eigenphase signs. It reports 546 successful deterministic finite checks of the constructed vectors, Grover updates, normalization, cycle-rank graph connectivity, and summed dimension formula. In an additional, independently written dense-array calculation, matrix unitarity and eigenvalue inclusion/multiplicity lower bounds were checked for \(d=3,4,5\).

The proof for all dimensions is the exact edgewise identity, the rank of the incidence matrix of a connected bipartite graph, and the closed binomial sum in `RESULT.md`. No finite test is claimed to certify those infinite-family steps. In particular, the result establishes only an explicit subspace at each eigenvalue; it does not claim the entire corresponding eigenspace has that dimension.

Scientific comparison used the originating full text, prior two-tessellable walk cycle-space results and relevant hypercube localization and magnetic Grover-walk studies. Independent assessment of priority and mathematical validity has not been performed.
