---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

At fixed k a product of edge indicators has expectation α_j=(k)_j/(n)_j for j distinct endpoints. A pair of distinct edges occupies three vertices in W=Σ binom(d,2) ways and four vertices otherwise. For triples with a middle edge, the endpoint-choice statistic K counts each three-edge path once and each triangle three times, so P=K−3T. Counting a distinguished wedge in a triple gives W(m−2)=3T+3S+2P+U, where S is the star count and U the five-vertex type; the six-vertex count is the remainder. These identities give the two degree-matched third-moment coefficients by inclusion-exclusion on the absent vertices. An independent direct recovery check is E[binom(Y_3,3)]=T/binom(n,3) and E[binom(Y_4,3)]=((n−3)T+S+P)/binom(n,4); the first two moments convert raw cubic moments to these factorial moments. In the prism, the two pure triples contribute two triangles and the mixed triples yield 12 two-edge and six one-edge sets. In K_{3,3} the two pure triples are edgeless and the 18 mixed triples have two edges. For k≥4 the complementary sample relation is Y_k=m−d(6−k)+Y_(6−k), so only k=3 differs. Binomial mixing gives the exact polynomial and summing its coefficients gives all three signs. Connected regular graphs of order below six are unique per realizable degree (only the trivial graph, edge, cycles and complete graphs occur); unequal degrees could not have identical edge means. The cubic graphs at order six follow by complementing the two possible 2-regular types.

## originality

PASS

The same-date habitat-tree result contains the tree specialization of the independent-survival cubic contrast, with the same edge-triple census method and a related PGF divisibility argument. The earlier graphical-zonotope result uses the same cubic witness to extract triangles from a different statistic. Neither supplies the two-size inverse problem with independent triangle and degree-mixing directions for general degree-matched graphs, or the exact whole-survivor edge-count risk reversal for the connected regular witness. The bounded pass concerns those conclusions, not priority for vertex-sampled motif calculus, the tree specialization, or discovery of the cubic pair.

## value

PASS

There are two distinct structural directions: the cubic witness changes T at fixed K; two trees with degree sequence (3,2,2,1,1,1), arranging the degree-two vertices on different arms or the same arm, change K from 4 to 3 at fixed T=0. The result says when these genuinely different features can be recovered from a compressed survivor observable. The smallest connected regular witness gives a concrete ranking reversal between specified thresholds, not merely numerical disagreement in a third moment. This is a natural identifiability and counterexample claim without an empirical or statistical guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
