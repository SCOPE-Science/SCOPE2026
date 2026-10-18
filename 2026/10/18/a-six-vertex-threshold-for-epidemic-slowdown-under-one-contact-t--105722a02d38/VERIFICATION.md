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

# Exact reproducibility

Run `python3 contact_outbreak_check.py` with any standard Python 3 environment. The program uses only `fractions.Fraction` and `functools.lru_cache` from the Python standard library. It enumerates every labelled undirected simple edge mask on \(n\in\{2,3,4,5\}\) vertices, retaining every connected graph and examining every nonedge as an added link. Each pair is evaluated twice: a direct finite Bellman subset recursion and an independent exhaustive weighted sum over terminal self-avoiding paths. Exact rational equality is asserted for each original and augmented graph; no decrease occurs for any of the 3227 eligible edge additions.

Observed checks: n=2: 1 connected graph, 0 comparisons; n=3: 4, 3; n=4: 38, 84; n=5: 728, 3140. The resulting run reports zero decreases and verifies the analytic family formulas for every integer \(1\le m\le16\) by both independent algorithms, including six-vertex decrease 1/150 and seven-vertex decrease 1/63. The family theorem for all integers \(m\ge1\) is proved algebraically in RESULT.md, not inferred from its finite regression tests.

The calculation treats each contact with any previously infected vertex as terminal and counts the seed as one infected vertex. The mean is over one index case uniformly sampled from all vertices. Model parameters not explicitly fixed here and the probability of clinical infection failure are outside scope. No independent external review or certification is asserted.
