---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Condition on the one-dimensional maximizing-index sets \(I_X\) and \(I_Y\) having cardinalities \(K_X=k\) and \(K_Y=\ell\). Exchangeability makes each index set uniform over subsets of its cardinality, and product independence makes the two subsets independent. A two-dimensional leader exists exactly when they intersect. Thus the conditional probability is \(1-\binom{n-k}{\ell}/\binom{n}{\ell}\), with value one when \(\ell>n-k\), and averaging gives the stated exact formula. The union bound on intersection size gives the upper bound \(\min(1,k\ell/n)\). The exact disjointness product is at most \((1-k/n)^\ell\le e^{-k\ell/n}\), giving the lower bound \(1-e^{-k\ell/n}\). Independent rational checks for all \(n\le50\) verified both inequalities for every \((k,\ell)\), but the arbitrary-\(n\) proof is algebraic. Since both bounding functions are bounded and vanish only at zero, \(a_n\to0\) exactly when \(K_XK_Y/n\to0\) in probability. The liminf leader criterion follows by a fixed positive tail lower bound in one direction and, conversely, from \(a_n\le E\min(1,R_n)\) with a deterministic truncation threshold.

## originality

PASS

The 2022 primary paper defines the leader probabilities, treats discrete and absolutely continuous cases, and explicitly identifies finding a computable leader criterion as its main open problem. It also asks whether a product law with both coordinate supports infinite can ever have the leader property. The 2022 quasi-unidimensional follow-up studies the different representation \(Z=f(X)\) and again leaves computable criteria open. Neither source states the product-coordinate maximum-tie reduction, the exact hypergeometric intersection formula, or the equivalence in terms of \(K_XK_Y/n\). Fresh Resultary and exact web searches found no earlier record with this criterion.

## value

PASS

The source literature explicitly asks for computable leader criteria and leaves broad product-law behavior open. Reducing every two-dimensional product law to the joint scale of its two one-dimensional maximum tie multiplicities is a clean structural criterion that handles atoms and continuous parts uniformly and converts a multivariate order event into one-dimensional statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
