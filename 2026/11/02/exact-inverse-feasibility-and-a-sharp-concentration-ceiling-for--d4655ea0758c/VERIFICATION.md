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

# Reproduction and scope of checks

Run `python verify.py` under Python 3. The only imports are from the Python standard library. The checker uses exact rational numbers throughout, including in its independently implemented Gaussian elimination and augmenting-path maximum flow.

The executable test suite carries out 1,528 assertions-at-the-case-level: 400 generated feasible networks with exact forward-resolvent weights, 400 perturbed target cases comparing all neighborhood-cut inequalities against exact bipartite max-flow feasibility, and 728 complete-graph cap/equality checks. Graphs span two through eight vertices, and the sparse random tests include heterogeneous rational retention probabilities. It additionally verifies that each constructed reverse-flow matrix reproduces the proposed weights exactly.

The fixed random seed ensures reproducibility. This verification suite supports the identities and guards against algebraic and orientation mistakes. It is not a proof of every possible finite trust network or the continuum of retention values; the general proof is in `RESULT.md`.

No independent external validation or audit has been performed.
