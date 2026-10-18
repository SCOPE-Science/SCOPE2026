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

# Reproducibility and scope

Execute `python3 verify.py` with Python 3.10 or later; no external modules or datasets are used. The program builds the six pairwise Gram equations and their Jacobian over an explicit split quadratic form of each ambient dimension \(M=5,6,7,8\). It constructs all \(6+4+12+3=25\) indexed representative configurations, checks their equations, column ranks and differential ranks, and checks two smooth comparison configurations for each dimension. It also exhausts all symmetric hollow four-by-four matrices over \(\mathbb F_3\) having rank exactly two and checks their bipartite support property. The successful result is `VERIFY_OK witness_cases=108 hollow_rank_two_mod3=116`.

The defining proof step that every rank-two hollow symmetric matrix in characteristic zero is a cross-term of two disjointly supported vectors is proved directly in `RESULT.md` by factoring the matrix through a two-dimensional quadratic space. The finite program is a regression test, not an infinite certificate. The general results about irreducible isotropic Grassmannians, closed incidence images, primeness and dimension are mathematical arguments in `RESULT.md`; the program neither enumerates arbitrary points nor computes scheme-theoretic singular multiplicities.
