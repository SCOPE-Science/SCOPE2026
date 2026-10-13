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

The final claim was checked against the explicit formulas in arXiv:2610.01941v1. The source fixes \(0<p<1/2\), defines the rotated binary pure-state channel and \(C=h(p)\), gives the channel-aware exponent in Eq. (9), and derives its phase-uniform converse through the binomial block decomposition in Eq. (11) and the \(D(t\|p)\) comparison in Eq. (12). The proof's threshold is the entropy boundary \(h(t_R)=R\).

For correctness, set \(A=p(1-p)\), \(L=\log((1-p)/p)\), \(u=p-t_R\), and \(\delta=C-R\). Taylor's theorem gives
\[
\delta=Lu+\frac{u^2}{2A}+\frac{1-2p}{6A^2}u^3+O(u^4),
\]
\[
D(p-u\|p)=\frac{u^2}{2A}+\frac{1-2p}{6A^2}u^3+O(u^4).
\]
Since \(L>0\), local series inversion is valid and yields the universal-side cubic coefficient in the finding. On the aware side, the objective has first three derivatives at \(s=0\) equal to \(\delta\), \(-AL^2\), and \(A(1-2p)L^3\) after subtracting \(sR\). Strict local concavity gives an interior maximizer \(s_*=\delta/(AL^2)+O(\delta^2)\), yielding the aware-side cubic coefficient. Their difference is exactly \(1/(2A^2L^4)\).

The proof is analytic. No finite numerical calculation, search result, or log is used as a substitute for the asymptotic argument. The checked scope is fixed \(p\in(0,1/2)\) and \(R\uparrow h(p)\); endpoint-uniformity and low-rate behavior are unproved here.
