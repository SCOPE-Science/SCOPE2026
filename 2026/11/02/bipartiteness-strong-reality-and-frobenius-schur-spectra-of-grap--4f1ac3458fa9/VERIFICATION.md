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

# Computational verification

Run `python3 check_graphical_fs.py` with the standard Python library. The checker independently enumerates all labeled simple graphs with one through four vertices over GF(2) (75 graphs), and three selected graphs over GF(4). It computes matrix ranks, exact quadratic Gauss sums, FS indicator integrality and values, the bipartiteness equivalence, and the Frobenius--Schur involution count identity. The observed marker is `GRAPHICAL_FS_INDICATORS_OK 75 3 nonbipartite 24 negative 1`. The general result is proved mathematically and not deduced from this finite test. The checker does not compute all irreducible character tables or settle publication priority.
