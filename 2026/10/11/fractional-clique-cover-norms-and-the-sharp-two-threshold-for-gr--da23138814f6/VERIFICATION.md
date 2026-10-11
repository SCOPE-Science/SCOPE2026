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
# Verification record

The proof has been checked symbolically on arbitrary finite supports, rather than inferred from sampling. The finite primal maximizing total coordinate weight subject to clique-weight constraints has dual minimizing fractional clique-cover weight; singleton feasibility gives strong duality. Complementation turns those cliques into independent sets, producing the fractional chromatic number exactly.

The boundary calculation uses the dual feasible weights \(1/m\) on each vertex of an odd cycle of length \(2m+1\). Every independent set meets the cycle in at most \(m\) vertices, yielding a strictly greater-than-\(2\) lower bound. In the construction, sampling one element of each ground set produces a clique star that captures exactly \(k/n_k\) of each coordinate in expectation. Uniform coefficients attain the inverse ratio by the cited Erdős–Ko–Rado theorem. The finite identity holds blockwise and extends to the completion because the constants are uniform. The Lovász–Kneser theorem supplies the unbounded chromatic number of the complement, not a finite computation.

Reproduction from the definitions: choose a real \(c>2\), set \(n_k=\lfloor ck\rfloor\), repeat the graph on all \(k\)-subsets of \([n_k]\) at each \(k\) across \(\omega_1\) indexed copies, join distinct copies, and use within-copy intersection adjacency. One can check the finite \(k=2,n_k=5\) illustration through the identities \(\binom52=10\) and \(\binom41=4\). It is not used as an infinite proof.

There are no computational certificates, external verification jobs, numerical tolerances, or hidden dependencies. Published graph theorems are dependencies and were checked against the statements in DOI:10.1007/s00373-024-02782-9. Neither exhaustive prior-art coverage nor independent audit is asserted.
