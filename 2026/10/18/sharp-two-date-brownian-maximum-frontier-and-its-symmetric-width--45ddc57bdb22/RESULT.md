# Sharp two-date Brownian maximum frontier and its symmetric width

## Finding

Let \(B\) be standard Brownian motion, \(M_t=\sup_{0\le s\le t}B_s\), and fix \(0<a<b<\infty\). For \(0\le q\le1\), consider **all** stopping times \(\tau\) in the natural Brownian filtration with \(\mathbb P(\tau=a)=q\) and \(\mathbb P(\tau=b)=1-q\). Their expected running maxima fill exactly a closed interval \([L(q),U(q)]\), with explicit endpoints and no external randomization.

Put \(h=b-a\), \(C_t=\sqrt{2t/\pi}\), and for \(z\ge0\) let
\[
H(z)=C_b\,\operatorname{erf}\!\left(z\sqrt{\frac{b}{2ah}}\right)
+C_a\exp\!\left(-\frac{z^2}{2a}\right)
\operatorname{erfc}\!\left(\frac z{\sqrt{2h}}\right).
\]
For \(0<q<1\), define \(u_q=\sqrt{2a}\,\operatorname{erfc}^{-1}(q)\) and \(v_q=\sqrt{2a}\,\operatorname{erf}^{-1}(q)\). Then
\[
\boxed{U(q)=H(u_q),\qquad L(q)=C_a+C_b-H(v_q).}
\]
At the boundary set \(L(0)=U(0)=C_b\) and \(L(1)=U(1)=C_a\), consistently with the endpoint limits. For \(0<q<1\), the unique (up to null sets) maximizing rule continues from \(a\) to \(b\) iff \(M_a-B_a\le u_q\); the unique minimizing rule continues iff \(M_a-B_a\ge v_q\).

The upper frontier \(U\) is strictly concave, the lower frontier \(L\) is strictly convex, and the interval width is symmetric and strictly concave:
\[
W(q)=U(q)-L(q)=U(q)+U(1-q)-C_a-C_b.
\]
Therefore **the unique widest attainable interval is at \(q=1/2\)**, for every \(0<a<b\), with width
\[
\boxed{W_{\max}=2H\!\left(\sqrt{2a}\,\operatorname{erf}^{-1}(1/2)\right)-C_a-C_b>0.}
\]

## Assumptions and scope

The filtration is the usual augmentation of the natural filtration of a one-dimensional standard Brownian motion started at zero. The only stopping dates allowed are the two deterministic dates \(a\) and \(b\), with their probabilities prescribed. A stopping rule can condition on the entire trajectory up to \(a\); it cannot use information after \(a\) to decide at \(a\). No independent randomization is included or needed. All displayed statements hold for every real \(0<a<b<\infty\) and every \(q\in[0,1]\). No statement is made for an atomless or a three-or-more-atom target law.

## Proof

**Step 1: Reduction to one choice event.** Each admissible stopping time is determined by an event \(A=\{\tau=b\}\in\mathcal F_a\) of probability \(1-q\). For \(D=M_a-B_a\), independent increments imply
\[
M_b-M_a=(S_h-D)_+,
\]
where \(S_h=\sup_{0\le r\le h}(B_{a+r}-B_a)\) is independent of \(\mathcal F_a\). The reflection principle gives \(D\overset d=|N(0,a)|\) and \(S_h\overset d=|N(0,h)|\). Consequently, writing \(G_h(d)=\mathbb E(S_h-d)_+\),
\[
\mathbb EM_\tau=C_a+\mathbb E\big[\mathbf1_A G_h(D)\big],
\quad
G_h(d)=\sqrt{\frac{2h}{\pi}}e^{-d^2/(2h)}-d\operatorname{erfc}\!\left(\frac d{\sqrt{2h}}\right).
\]
Indeed \(G_h'(d)=-\operatorname{erfc}(d/\sqrt{2h})<0\) for every finite \(d\ge0\). The half-normal density is
\[
f_a(d)=\sqrt{\frac2{\pi a}}e^{-d^2/(2a)},\quad d\ge0,
\]
with strictly increasing distribution function \(F_a(d)=\operatorname{erf}(d/\sqrt{2a})\).

**Step 2: Sharp selectors and uniqueness.** Among all \(A\in\mathcal F_a\) with probability \(1-q\), rearrangement against the strictly decreasing function \(G_h(D)\) gives the maximum at \(A=\{D\le u_q\}\), and the minimum at \(A=\{D\ge v_q\}\). For instance, if \(A_* =\{D\le u_q\}\), then the integrand \((\mathbf1_{A_*}-\mathbf1_A)(G_h(D)-G_h(u_q))\) is everywhere nonnegative; its expectation is \(\mathbb E[(\mathbf1_{A_*}-\mathbf1_A)G_h(D)]\) because \(A\) and \(A_*\) have equal probabilities. Equality requires \(A=A_*\) almost surely, since \(D\) is atomless and \(G_h\) strictly decreases. The minimizing argument reverses the order. In particular there can be no improvement by using aspects of the observed path beyond its drawdown.

**Step 3: Evaluation.** For \(z\ge0\) set
\[
\widetilde H(z)=C_a+\int_0^z f_a(d)G_h(d)\,\mathrm dd.
\]
Direct differentiation of the explicit \(H\) in the finding gives
\(H'(z)=f_a(z)G_h(z)\); also \(H(0)=C_a\). Hence \(\widetilde H=H\). Moreover \(H(\infty)=C_b\), alternatively following from \(\mathbb EM_b=C_b\). Thus selection of the smallest drawdowns yields \(U(q)=H(u_q)\), and selection of the largest yields \(L(q)=C_a+H(\infty)-H(v_q)=C_a+C_b-H(v_q)\).

**Step 4: The whole interval is attained.** The probability transform \(V=F_a(D)\) is uniform on \([0,1]\) and belongs to \(\mathcal F_a\). For each \(s\in[0,q]\), the event \(A_s=\{s\le V\le s+1-q\}\) has probability \(1-q\). The corresponding expectation
\[
C_a+\int_s^{s+1-q}G_h(F_a^{-1}(w))\,\mathrm dw
\]
is continuous in \(s\); it takes \(U(q)\) at \(s=0\) and \(L(q)\) at \(s=q\). By the intermediate value theorem it fills the interval. Conversely Steps 1–2 bound every admissible rule between these endpoints.

**Step 5: Curvature and the unique widest law.** In the interior, differentiating the inverse quantiles (\(u_q'=-1/f_a(u_q)\) and \(v_q'=1/f_a(v_q)\)) gives
\[
U'(q)=-G_h(u_q),\qquad
U''(q)=-\frac{\operatorname{erfc}(u_q/\sqrt{2h})}{f_a(u_q)}<0,
\]
\[
L'(q)=-G_h(v_q),\qquad
L''(q)=\frac{\operatorname{erfc}(v_q/\sqrt{2h})}{f_a(v_q)}>0.
\]
Since \(u_{1-q}=v_q\), we have \(L(q)=C_a+C_b-U(1-q)\). The width \(W(q)=U(q)+U(1-q)-C_a-C_b\) is strictly concave and symmetric around \(q=1/2\), so its unique maximum occurs there. For any interior \(q\), the half-normal density and strictly monotone gain ensure \(U(q)>L(q)\); hence the maximum width is strictly positive.

## Verification

A standalone verifier `verify.py` independently computes the selection integrals by high-precision quadrature, differentiates the closed form, checks the half-normal normalization, verifies the interior inequalities, and compares a benchmark. Executing `python verify.py` with `mpmath` available passed 291 high-precision identity checks and strict inequalities at 42 parameter pairs; these tests supplement, not replace, the analytic proof. For \(a=1\), \(b=2\), \(q=1/2\), the values are \(U\approx1.0623396438887272\), \(L\approx0.8639240840096507\), and \(W\approx0.1984155598790764\). The entire proof uses only the Brownian reflection principle, independent increments, one-dimensional rearrangement, explicit differentiation, and elementary calculus.

## Relationship to prior work

Beiglböck, Eder, Elgert, and Schmock (2018) establish general geometric optimality and a drawdown-barrier representation for *maximizing* expected Brownian running maximum under a specified stopping-time law (Corollary 1.2), with a different structural warning for the minimization problem (Remark 7.1). The drawdown monotonicity and barrier principle used here are therefore **established background**, not asserted to be new. Deng and Zhang (2026, arXiv:2610.01585v1), the motivating literature, consider an atomless target law and construct a variational-inequality characterization of its optimal drawdown boundary. Bayraktar and Miller (arXiv:1604.03042) develop distribution-constrained stopping for finite atomic laws using dynamic programming for terminal-payoff functionals. The distinct evaluated result here is the complete elementary **two-date, two-sided numerical value frontier**, including the inverse-error-function formula, its nonrandomized attainability, and the universal half-half maximizer of the uncertainty width. General implicit barrier theorems cannot be characterized as absent; the narrower issue is whether they or other sources already supply these explicit evaluated formulas.

## Limitations

The theorem concerns a single Brownian path with exactly two possible deterministic stopping dates and the expected running maximum, not a general utility, drifted diffusion, more dates, or an atomless stopping law. The unique-rule statements refer to rules modulo null sets. The existing general optimal stopping literature subsumes the broad selection geometry, and unlocated binary-law evaluations remain a publication-priority risk. Independent scientific verification has not been performed. The numerical checks do not establish novelty or infinite mathematical claims.

## References

1. S. Deng and X. Zhang, *Distribution-constrained maximum stopping of maximum type*, arXiv:2610.01585v1, first posted 2026-10-01, https://arxiv.org/html/2610.01585v1 .
2. M. Beiglböck, M. Eder, C. Elgert, and U. Schmock, *Geometry of distribution-constrained optimal stopping problems*, Probability Theory and Related Fields 172 (2018), 71–101, https://doi.org/10.1007/s00440-017-0805-x .
3. E. Bayraktar and C. W. Miller, *Distribution-constrained optimal stopping*, arXiv:1604.03042, https://arxiv.org/abs/1604.03042 .
