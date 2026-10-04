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

The proof was checked at the two places where Jin's published \(2p\)-moment enters.

For fixed \(t\), define
\[
Y_n(t)=n^{-p/2}\left|\sum_{j=1}^{\lfloor nt\rfloor}\xi_j\right|^p.
\]
Scalar \(p\)-moment convergence gives \(Y_n(t)\Rightarrow t^{p/2}\sigma^p|N(0,1)|^p\) and convergence of expectations, hence uniform integrability. If \(Y_{n,1},\ldots,Y_{n,d(n)}\) are iid copies, then for every fixed truncation level \(K\), the truncated empirical mean has variance at most \(K^2/d(n)\), while the expected tail is uniformly small as \(K\to\infty\). This proves the required triangular weak law without assuming \(\mathbb E Y_n(t)^2<\infty\).

For the uniform-in-time part, the martingale term satisfies
\[
\mathbb E|Q_n^{(d)}|^2
=p^2d\,\mathbb E|X_{1,1}^{(d)}|^2\sum_{j=1}^n
\mathbb E|S_{j-1,1}^{(d)}|^{2p-2}.
\]
The scaling powers are
\[
d\cdot d^{-2/p}\cdot d^{-(2p-2)/p}=d^{-1}.
\]
Under a finite \((2p-2)\)-moment when \(p>2\), or finite variance when \(1<p\le2\),
\[
\mathbb E|S_{j-1,1}^{(d)}|^{2p-2}\le C_p d^{-(2p-2)/p}j^{p-1},
\]
so
\[
\mathbb E|Q_n^{(d)}|^2\le C_p n^p/d.
\]
Doob's inequality therefore makes the normalized martingale negligible for every \(d(n)\to\infty\). The remaining monotonicity and finite-grid argument is the same deterministic/probabilistic reduction as in the published uniform metric proof.

Limits: the argument proves sufficiency, not necessity, of the moment order \(\max\{2,2p-2\}\). It materially uses independence across coordinates. The \(p=2\) finite-variance specialization is prior work and is not part of the originality claim.
