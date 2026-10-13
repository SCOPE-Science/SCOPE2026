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

The principal analytic estimate applies to **every** two-coordinate independent product with both marginal upper endpoints unattained as positive-mass atoms. Define
\[
g_Y(n)=\Pr\{Y_1=\max(Y_1,\ldots,Y_n)\}
=\mathbb E[F_Y(Y_1)^{n-1}].
\]
The absence of a top atom ensures \(F_Y(Y_1)<1\) almost surely, so dominated convergence yields \(g_Y(n)\to0\). For any \(q=\Pr(X>t)>0\), the leader event obeys
\[
a_n\le(1-q)^n+nq\,g_Y(n).
\]
Picking successively smaller positive tails \(q_k\) and \(n_k=\lceil k/q_k\rceil\) as in the proof forces \(a_{n_k}\to0\). The finite verifier does **not** certify that argument: it tests its exact finite implication at representative rational discrete laws.

Run `python3 verify.py` using only the Python standard library. The script exhaustively enumerates all \(n\)-row samples for \(1\le n\le4\) of a fixed rational product law and checks the top-atom hit lower bound, maximizing-index lower bound, and threshold upper bound exactly. It also verifies the binomial identity
\[
a_n=p+(1-p)^n
\]
for an atomless first coordinate and Bernoulli second coordinate, at \(p=2/7\) and \(1\le n\le19\), and verifies a three-coordinate top-vector witness. Expected terminal line:

`VERIFY_OK exact_finite_rows=4 sharp_bernoulli_limit=2/7 all_top_product=3/40`

These are exact rational finite examples; the infinite theorem and sharpness argument are in `RESULT.md`. No enumeration is claimed to be exhaustive over distributions.
