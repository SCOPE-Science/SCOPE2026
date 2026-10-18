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

The accompanying standalone `verify.py` uses only Python's standard library and exact `fractions.Fraction` arithmetic. It evaluates the original independent-occupancy group sum separately for each ordered pair and site, enumerating subsets of all other possible occupants and applying the exact group-size factor `1/(k-1)`; it then independently evaluates the proposed polynomial in graph adjacency and common-neighbor counts.

Execute `python verify.py` in the same directory as the extracted program. Its expected final marker is `EXACT_REPLAY_OK matrix_entries= 1044`. The six finite graphs checked are cycles of lengths five and six, complete bipartite graphs of degrees three and four, the three-dimensional cube, and the triangular prism. Four rational positive home-fidelity settings are checked per graph, together with the exact stochastic row sums. For the triangular prism at fidelity two, the checker obtains `A=244/1875`, `B=109/3750`, `S=272/625`, `triangle_edge=199/1250`, `other_edge=244/1875`, and `temperature=353/625`.

The proof of the infinitely many degree and graph cases does not rely on this finite test. Independently inspect the binomial integrating identity, the conditional occupant distribution at each type of meeting site, the derivative of the self-weight, the sign of the scalar root equation, and the Bernoulli strict bound. The limit is obtained from uniform convergence of the scalar root equations on a compact interval, not from finite degree sampling. Verification applies to the stated model only; actual fixation probabilities or evolutionary outcomes were neither computed nor asserted. Independent external validation has not been conducted.
