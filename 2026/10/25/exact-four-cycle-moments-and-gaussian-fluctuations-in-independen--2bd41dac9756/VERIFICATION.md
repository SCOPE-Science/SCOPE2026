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

# Verification

## Analytic checks

For two \(d\)-regular graphs on \(m\) vertices, the edge-overlap mean is \(md^2/[2(m-1)]\). Its variance follows from an exhaustive combinatorial partition into identical, endpoint-sharing, and disjoint ordered edge pairs. Substitution and symbolic simplification give \(md^2(m-d-1)^2/[2(m-3)(m-1)^2]\) for \(m\ge4\). For the dimension-two boundary there is a single square, with no fluctuation.

The entire recursive variance uses the conditional-mean-zero property of the matching overlap at each node, not an unjustified unconditional independence of increments. A Gaussian central limit law follows by approximating the large graph by independent blocks at a fixed lower depth and then sending the depth to infinity: the omitted variance divided by the number of vertices is bounded by \(\sum_{k>L}b_k/2^k\to0\). The constants are convergent because \(a_k,b_k=O(k^2)\). The limiting variance is strictly positive because \(b_3=8/9\).

## Reproducible finite checks

Run `python verify_four_cycles.py` with Python 3 (standard library only). The program exhaustively checks 24 level-three matchings; then, for four combinations of level-three child types, exhaustively evaluates all 40,320 level-four top matchings, yielding 161,280 evaluations. It separately tests 140 randomly generated larger recursive constructions by directly counting simple four-cycles using common-neighbor pairs. The exact-rational assertions return \(a_3=8/3\), \(b_3=8/9\), \(a_4=36/7\), and \(b_4=576/245\). This finite exhaustive checking applies only at the stated levels, not to unbounded dimensions or all possible models.

## Scope and integrity

The independent-copy model and independence across recursive matching nodes are hypotheses, not consequences. Neither the finite program nor the recurrence alone establishes the central limit theorem without the separate analytic Gaussian approximation. No independent audit, external certificate or broad novelty certification has been performed.
