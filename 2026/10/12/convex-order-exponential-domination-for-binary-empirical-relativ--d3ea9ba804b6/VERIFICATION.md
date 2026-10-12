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

For \(P=(p,q)\) with \(p\le q\), set \(d=\log(q/p)\). The proof uses the exact centered-information law
\[
X=
\begin{cases}
qd,&\text{with probability }p,\\
-pd,&\text{with probability }q,
\end{cases}
\]
and the centered unit exponential \(Y=E-1\).

The critical all-parameter checks are analytic:

1. \(pd\le p\log(1/p)\le1/e<1\), so the lower atom of \(X\) lies above the lower endpoint \(-1\) of \(Y\).
2. The stop-loss transform of \(Y\) is \(-a\) for \(a\le-1\) and \(e^{-(1+a)}\) for \(a>-1\).
3. On the only nontrivial interval \(-pd\le a<qd\), the ratio that must be at most one is
\[
R(a)=p(qd-a)e^{1+a}.
\]
If \(d\ge1\), its maximum is \(p^p q^q\le1\). If \(d<1\), its maximum is \(pd\,e^{1-pd}\le1\).
4. Equal means plus all-threshold stop-loss domination gives \(X\preceq_{\mathrm{cx}}Y\).

The standalone verifier `verify_binary_information_convex_order.py` is a deterministic floating-point regression check. It samples probabilities over many orders of magnitude, thresholds covering both supports, and representative MGF parameters. The numerical replay does not establish the universal quantifiers; those are supplied by the proof above.
