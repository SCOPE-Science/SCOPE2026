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

The theorem is verified by exact finite counting; no numerical approximation is needed.

For \(k=n-2d\), fixing residual sets \(D\subseteq[n+1]\) and \(R\subseteq[n]\) of sizes \(2d+1\) and \(2d\) leaves two complements of size \(k\). An admissible restriction with those residual sets is exactly a bijection between the complements, so there are \(k!\) such restrictions. The count is independent of \((D,R)\). This proves that \((D^\rho,R^\rho)\) is product-uniform.

On the event \(S\cap(D^\rho\times R^\rho)=\varnothing\), every leaf label lies outside the valid residual rectangle. Thus the conditional error over designs is exactly \(1\) on that event. Counting the event gives
\[
\frac{B_{2d+1,2d}(\overline S)}{\binom{n+1}{2d+1}\binom n{2d}}.
\]

For each fixed label, membership in the random residual rectangle has probability
\[
\frac{2d+1}{n+1}\frac{2d}{n}.
\]
The union bound therefore gives the support-size inequality. A \(p\)-ary height-\(e\) tree has at most \(p^e\) leaves, hence at most \(p^e\) distinct labels. If the error is zero, every residual rectangle meets \(S\), so the complement is \(K_{2d+1,2d}\)-free by definition.

Limits checked: the argument concerns actual reduced-tree error, not the path-sensitive \(\chi(P,\rho)\) probability in the source's final sufficient condition. It provides no new lower bound for \(\mathrm{AC}^0[p]\)-Frege and no sufficiency statement for realizing a given hitting set as a correct search tree.
