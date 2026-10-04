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

The proof was replayed directly from the two metric definitions and the quantitative Schur definitions.

1. For \(M_q^{(A)}\), every nonzero distance is \(1\) or \(q\). The only nontrivial triangle restriction is \(q\le2\).
2. The evaluation sequence \(\delta(1),\delta(-1),\delta(2),\delta(-2),\ldots\) has norm-tail diameter \(q\). A unit Lipschitz function can have value gap greater than \(1\) on at most one antipodal pair, so its scalar tail oscillation is at most \(1\); the positive-versus-nonpositive indicator attains \(1\). Thus the witness has exactly \(\operatorname{ca}=q\) and \(\delta=1\).
3. For \(M_q^{(B)}\), the distances are \(1,2,q\). An antipodal side is bounded by the path length \(2+1=3\), and a same-sign side of length \(2\) has a \(1+1\) path, so the metric is valid for \(2\le q\le3\).
4. For \(y_n=\delta(n)-\delta(-n)\), one has \(\|y_n\|=q\). For every unit Lipschitz function, all but at most two antipodal differences lie in \([-1,1]\), so every weak-star cluster point of \((y_n)\) has norm at most \(1\). The equivalence in Proposition 5.1 of arXiv:2505.12893v1 therefore excludes every Schur constant below \(q\).
5. Proposition 8.2 of arXiv:2505.12893v1 gives the matching \(q\)-Schur upper bound in both families because the minimum nonzero distance is \(1\) and the diameter is \(q\).
6. The universal lower bound \(1\) follows from the alternating sequence \(u,-u,u,-u,\ldots\) in any nonzero Banach space. The universal upper bound \(3\) for uniformly discrete Lipschitz-free spaces is Theorem 1.1 of arXiv:2604.01875v1.

Endpoint replay: at \(q=2\), the first family is the distance pattern of Example 8.3 in arXiv:2505.12893v1; at \(q=3\), the second family is the distance pattern of Example 8.5. No finite experiment is used as a substitute for the interval proofs. No independent audit has been performed.
