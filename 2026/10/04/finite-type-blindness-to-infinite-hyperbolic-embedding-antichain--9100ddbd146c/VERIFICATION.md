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

The verification is a source-level implication check.

Belletti--Detcherry Corollary 6.2(2) states that if a compact oriented \(3\)-manifold \(M\) embeds in a rational homology sphere, then for any \(k\) and \(n\) there is an infinite sequence \((M_i)\) of compact oriented hyperbolic \(3\)-manifolds, all \((Y_k,T_n)\)-equivalent to \(M\), such that \(M_i\) does not embed in \(M_j\) whenever \(i\ne j\).

Set
\[
k=d+1.
\]
By Belletti--Detcherry Definition 3.4, \((Y_{d+1},T_n)\)-equivalence uses gluing maps in an intersection containing the \(Y_{d+1}\) condition, so it implies \(Y_{d+1}\)-equivalence.

Massuyeau Proposition 3.32 states that if two manifolds in a fixed \(Y_1\)-equivalence class are \(Y_{d+1}\)-equivalent, then every finite-type invariant \(F\) of degree at most \(d\) has equal values on them. Since \(Y_{d+1}\)-equivalence implies \(Y_1\)-equivalence, all \(M_i\) and \(M\) lie in the same required class. Hence
\[
F(M_i)=F(M)
\]
for every \(i\), and therefore all \(M_i\) have the same degree-at-most-\(d\) finite-type profile.

No finite experiment is used. No converse to Proposition 3.32 is used. No claim is made about invariants of unbounded degree or about finite-type theories defined using different surgery filtrations.
