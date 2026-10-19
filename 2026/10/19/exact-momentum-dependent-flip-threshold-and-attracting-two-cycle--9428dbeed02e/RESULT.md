# Exact momentum-dependent flip threshold and attracting two-cycle for smoothed scalar Muesterov

## Finding

For the scalar smooth-sign Muesterov iteration defined below, every momentum \(0\le\beta<1\) has an **exact** local stability threshold
\[
 a_c(\beta)=\frac{2(1+\beta)}{1+2\beta}.
\]
The zero-error fixed point is locally exponentially stable precisely for \(0<a<a_c(\beta)\), and unstable for \(a>a_c(\beta)\). At the threshold one characteristic root is \(-1\); no exponential stability is asserted there.

If \(a>a_c(\beta)\), there exists exactly one nonconstant period-two orbit up to cyclic shift. It is the symmetric sign-alternating orbit \(z_k=(-1)^k h\), with
\[
 h=\left(\frac{a^2}{4(1+\beta)^2}-\frac1{(1+2\beta)^2}\right)^{1/2}>0.
\]
This orbit is **locally exponentially attracting for every** \(a>a_c(\beta)\), however large the fixed step. Its amplitude emerges continuously with the precise square-root law
\[
 h\sim\sqrt{\frac{a_c(\beta)}{2(1+\beta)^2}}\sqrt{a-a_c(\beta)}
 \quad(a\downarrow a_c(\beta)).
\]
Thus positive Nesterov momentum lowers the precise two-cycle onset from \(a_c(0)=2\) toward \(4/3\) as \(\beta\uparrow1\); these are not merely sufficient bounds.

In the zero-momentum case \(\beta=0\), there is a complete **global** dichotomy. Every starting point converges to zero when \(0<a\le2\). At \(a=2\), every nonzero orbit not hitting zero finitely satisfies \(|z_k|\sim(2k)^{-1/2}\). When \(a>2\), every orbit not eventually equal to zero converges in alternating sign to the unique two-cycle of amplitude \(\sqrt{a^2/4-1}\).

## Assumptions and scope

Fix \(\lambda,\varepsilon,\alpha>0\), \(0\le\beta<1\) and \(f(x)=\lambda x^2/2\). Consider the *analytic smooth-sign* scalar specialization of the Nesterov-type nonlinear preconditioned gradient step:
\[
 y_k=x_k+\beta(x_k-x_{k-1}),\qquad
 x_{k+1}=y_k-\alpha\frac{\lambda y_k}{\sqrt{\varepsilon^2+(\lambda y_k)^2}}.
\]
Set \(z_k=\lambda x_k/\varepsilon\), \(a=\alpha\lambda/\varepsilon\) and
\[
 F_a(t)=t-\frac{at}{\sqrt{1+t^2}}.
\]
Then, for arbitrary real initial pair \((z_{-1},z_0)\),
\[
 z_{k+1}=F_a((1+\beta)z_k-\beta z_{k-1}).
\]
The quadratic objective is centered at zero; gradients are exact. The model is **not** the unregularized sign map, a stochastic solver, or a finite polynomial matrix-polar algorithm. “Locally exponentially attracting” refers to the two-dimensional state \((z_k,z_{k-1})\) and linear convergence to the corresponding periodic orbit near it. Global attraction above onset is asserted only when \(\beta=0\).

## Proof

**(1) Linear fixed-point frontier.** Since \(F_a(0)=0\) and \(F_a'(0)=1-a\), the state Jacobian at zero has trace and determinant
\[
 T=(1+\beta)(1-a),\qquad D=\beta(1-a).
\]
The exact second-order real Schur–Jury inequalities are \(1-T+D>0\), \(1+T+D>0\) and \(1-D>0\). They reduce to
\[
 a>0,\qquad 2(1+\beta)-(1+2\beta)a>0,\qquad 1-\beta+\beta a>0.
\]
The third holds automatically. Hence the origin is locally exponentially stable exactly for \(0<a<a_c(\beta)\). When \(a>a_c(\beta)\), the second Jury expression is negative, forcing a multiplier outside the closed unit disk. At equality the characteristic roots are \(-1\) and \(\beta/(1+2\beta)\).

**(2) All primitive two-cycles.** Let \(u\ne v\) be successive entries of any period-two orbit, with \(v=F_a((1+\beta)u-\beta v)\) and \(u=F_a((1+\beta)v-\beta u)\). Write \(S(t)=t/\sqrt{1+t^2}\), an odd, strictly increasing bijection from \(\mathbb R\) to \((-1,1)\). The two equations give
\[
 aS((1+\beta)u-\beta v)=(1+\beta)(u-v),
\]
\[
 aS((1+\beta)v-\beta u)=-(1+\beta)(u-v).
\]
Injectivity and oddness of \(S\) show that the two arguments are negatives of one another. Their sum is \(u+v\), so \(v=-u\). Setting \(u=h>0\) then yields
\[
 F_a((1+2\beta)h)=-h
 \iff \frac{a}{\sqrt{1+(1+2\beta)^2h^2}}=a_c(\beta).
\]
It has a positive solution precisely if \(a>a_c(\beta)\), and solving gives the displayed unique amplitude. Expansion of its square proves the square-root onset law.

**(3) Local stability of the entire cycle branch.** At either point of this orbit, the argument of \(F_a\) has magnitude \((1+2\beta)h\). The common derivative equals
\[
 q=F_a'((1+2\beta)h)=1-\frac{a_c(\beta)^3}{a^2}.
\]
Since \(a>a_c(\beta)\),
\[
 -\frac1{1+2\beta}=1-a_c(\beta)<q<1.
\]
The one-step state derivative is the same matrix at both orbit points,
\[
 J=\begin{pmatrix}(1+\beta)q&-\beta q\\1&0\end{pmatrix}.
\]
Its Jury quantities are \(1-q\), \(1+(1+2\beta)q\) and \(1-\beta q\), each strictly positive. Thus both eigenvalues of \(J\) lie inside the unit disk. The two-step return derivative is \(J^2\), whose eigenvalues also have modulus below one. The period-two orbit is locally exponentially attracting for every \(a>a_c(\beta)\).

**(4) Complete zero-momentum global dynamics.** Put \(r_k=|z_k|\) and \(\beta=0\). If \(0<a\le2\), then for every \(r>0\), \(0<a/\sqrt{1+r^2}<2\); hence \(r_{k+1}=r_k|1-a/\sqrt{1+r_k^2}|<r_k\). Its only possible limit is zero. At \(a=2\), near zero,
\[
 r_{k+1}=r_k-r_k^3+O(r_k^5),\qquad
 r_{k+1}^{-2}-r_k^{-2}=2+o(1),
\]
so summation gives \(r_k\sim(2k)^{-1/2}\), provided zero is never reached finitely.

Suppose \(a>2\), and define \(c=\sqrt{a^2-1}\), \(h=\sqrt{a^2/4-1}\). For \(r>c\), the scalar map is positive with \(0<F_a(r)<r\), and an orbit not hitting zero must eventually enter \((0,c)\); otherwise its decreasing magnitudes would converge to \(\ell\ge c\), inconsistent with the multiplier being strictly less than one at \(\ell\). In \((0,c)\), the sign flips and the positive magnitude map is
\[
 g(r)=\frac{ar}{\sqrt{1+r^2}}-r.
\]
It maps \((0,c)\) strictly into itself. Indeed its maximum occurs at \(r=\sqrt{a^{2/3}-1}\), where
\[
 \max g=(a^{2/3}-1)^{3/2}<\sqrt{a^2-1}=c.
\]
The unique positive fixed point is \(h\). Since \(g(r)+r=ar/\sqrt{1+r^2}\) strictly increases and equals \(2h\) at \(r=h\), and \(g(r)>r\) below \(h\) whereas \(g(r)<r\) above \(h\), we obtain
\[
 |g(r)-h|<|r-h|\quad (r\in(0,c),\ r\ne h).
\]
An orbit above \(2h\) decreases until it enters \((0,2h)\) (there is no fixed point outside \(h\)). Thereafter its distance from \(h\) is strictly below \(h\), bounding the orbit away from zero. Compactness and strict contraction of distance off \(h\) force \(r_k\to h\). The sign flips at every subsequent step. This completes the global dichotomy without claiming its extension to positive momentum.

## Verification

`artifacts/verify_scalar_soft_muesterov.py` (Python standard library) reproduces the exact zero-Jacobian Schur inequalities, analytic two-cycle identities, derivative simplification and cycle Schur stability across parameter grids, checks the scalar zero-momentum magnitude contraction, verifies critical inverse-square convergence, and checks Jacobian derivatives by finite differences. It returned `PASS: 9140 deterministic identities, stability checks, interval contractions and critical limits` when executed from the packaged file. Finite sampled checks are **not** proofs of any all-parameter or global claim; those follow from the algebra above.

## Relationship to prior work

The September 2026 Muesterov paper [1] defines the Nesterov-type spectral-preconditioned iteration, establishes sufficiently small-step convergence, and reports observed oscillation behavior. Its full text and appendix were examined: they do not state this *exact* scalar momentum-dependent onset, period-two uniqueness, or all-step local attraction of the branch. The present theorem is a scalar analytic-preconditioner model, not a guarantee for the complete matrix method.

The earlier quadratic Muon study [2] discusses exact-sign oscillations; the nonsmooth sign map has different dynamics. An independently published sharp flip theorem [3], based on the \(\kappa=4\) scalar Polar-Express smooth surrogate **without momentum**, exhibits a related flip mechanism but uses a different preconditioner and does not imply the new \(\beta\)-dependent threshold. No assertion of novelty is made for the general flip-bifurcation phenomenon.

## Limitations

The threshold describes local exponential stability of the zero state, not a global criterion for \(\beta>0\). Above it the period-two orbit is proved locally, not globally, attracting. At exact equality \(a=a_c(\beta)\) the state is nonhyperbolic; the theorem does not classify its nonlinear decay for positive \(\beta\). No higher-period orbit census, finite-precision guarantee, stochastic-noise statement, or matrix-valued extension is claimed. External literature indexing is incomplete, so equivalent statements in older or unindexed nonlinear-dynamics research remain possible.

## References

1. *Convergence guarantees for Muon: New parameter regimes and generalizations*, arXiv:2609.30546v1, publicly posted 2026-09-24, https://arxiv.org/abs/2609.30546 (Muesterov model and small-step convergence).
2. *Insights on Muon from Simple Quadratics*, arXiv:2602.11948, publicly posted 2026-02-12, https://arxiv.org/abs/2602.11948 (exact-sign quadratic dynamics).
3. *A sharp flip frontier for the Polar-Express surrogate on scalar quadratics*, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-sharp-flip-frontier-for-the-polar-express-surrogate-on-scalar--5f6e926df82f (different smooth surrogate, zero momentum).
