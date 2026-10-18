---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Every unweighted real finite-DAG isotonic metric fit exists uniquely for p>1. On each equality-connected block B the fit is the scalar p-mean, and the complete projection is a continuous finite selection among direct sums of these maps. Each block derivative has norm |B|^(1/p)||alpha||_q where alpha_i=|r_i|^(p-2)/sum|r_j|^(p-2); for 1<p<2 the probability-vector bound gives |B|^(1/p), for p>2 residual signed balance and concavity bound each alpha_i<=1/2 and give (|B|/2)^(1/p), for p=2 Hilbert nonexpansiveness, and size<=2 has exact 1. The finite-selection local-to-global lemma is valid along segments. For every weakly connected graph, strictly positive KKT edge multipliers put all zero fits in a stable full-pooling cell. As multipliers concentrate on one edge (p>2), weights approach (1/2,1/2,0,...); selecting noncut vertex j, concentrating on an edge of G-j and scaling incident-to-j multipliers ε² (p<2) makes weight at j dominate. This supplies genuine graph-specific local derivative lower bounds, not merely an unconstrained scalar analogy. Disconnected norm is max over blocks. No extrapolation from source numerical diagnostics is needed.

## originality

PASS

Best-of-knowledge PASS for extension from known chain-only and scalar-line exact moduli to every finite partial order, with a nontrivial graph-uniform sharpness proof. Prior published Resultary chain formula and constant-line scalar mean formula are explicitly credited and not treated as independent innovations. Algorithms for arbitrary DAG isotonic regression and qualitative Lipschitz regularity do not entail sharp constants or graph-adapted full-pooling witnesses. Material full 1998 Finzel--Li source remained inaccessible; its public abstract only proves qualitative existence, leaving a bounded named risk rather than automatic rejection.

## value

PASS

Exact perturbation moduli for arbitrary finite partial orders are intrinsically motivated robustness measures for isotonic best fits. The theorem makes a nontrivial structural statement: all connected branching/chain posets of a given size share the same sharp constant, despite graph-dependent active constraints, and exhibits witnesses via strictly positive edge multipliers. Known chain/constant-line special cases leave this quantified graph-uniform classification open. No general theorem beyond the exact natural finite-order invariant is demanded.

The dated certificate retains the supplied scientific assessment, sources and limitations.
