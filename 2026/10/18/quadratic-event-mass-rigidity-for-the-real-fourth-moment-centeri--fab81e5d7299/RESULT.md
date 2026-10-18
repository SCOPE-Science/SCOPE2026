# Quadratic event-mass rigidity for the real fourth-moment centering norm

## Finding

Let \((\Omega,\mathcal F,\mathbb P)\) be **any** probability space and let \(C f=f-\mathbb E f\) act on the real Banach space \(L^4(\mathbb P)\). Put
\[
K=1+\frac{2}{\sqrt3},\qquad
h=\sqrt{3+2\sqrt3},\qquad
\alpha=\frac{3-h}{6},
\]
\[
a=\frac{\sqrt3}{2}(h-1),\qquad
b=-\frac{\sqrt3}{2}(h+1),\qquad
d=a-b,\quad A=\frac{2}{\sqrt3},\quad M=\max\{|a|,|b|\}.
\]
Define the attainable-event-mass distance
\[
\delta(\mathbb P)=\inf_{B\in\mathcal F}|\mathbb P(B)-\alpha|\in[0,\alpha].
\]
Then the gap from the sharp unrestricted fourth-power centering constant obeys **dimension-free two-sided estimates**
\[
\boxed{\quad c\,\delta(\mathbb P)^2\ \le\ K-\|C\|_{L^4\to L^4}^{4}\ \le\ C_*\,\delta(\mathbb P)^2\quad}
\]
with explicit positive universal coefficients
\[
c=A\min\left\{\frac{d^4}{64M^4},\frac{1}{16\alpha^2}\right\},
\qquad C_*=A d^4(1+\alpha)^2.
\]
Numerically, \(\alpha\approx0.07625670719\), \(c\approx0.07659599\), and \(C_*\approx502.99072\). These coefficients are valid, not asserted optimal. The quadratic exponent is optimal uniformly over probability spaces. Moreover, \(\|C\|^4=K\) if and only if \(\delta(\mathbb P)=0\), while a nonzero \(L^4\) function attains the sharp unrestricted ratio \(K\) if and only if an event has exactly probability \(\alpha\).

## Assumptions and scope

The field is real, the exponent is exactly four, and the expectation is the constant (trivial-sub-σ-algebra) expectation on a probability space. There are no assumptions of finite support, uniform atom weights, non-atomicity, or extremizer existence. The zero-dimensional/trivial probability-space case is included. The assertion is about the actual norm of the particular operator \(I-\mathbb E\), not the minimal projection constant of an arbitrary hyperplane.

## Proof

**1. Exact quartic remainder.** Direct polynomial expansion using \(h^2=3+2\sqrt3\), \(a-b=\sqrt3h\), and \(\alpha=(a-1)/(a-b)\) gives, for real \(z,\mu\),
\[
Kz^4-(z-\mu)^4-A(z-a\mu)^2(z-b\mu)^2
=(10+6\sqrt3)\mu^3(z-\mu).
\]
With \(\mu=\mathbb Ef\), integration eliminates the right-hand side. Therefore for every real \(f\in L^4\),
\[
\boxed{K\,\mathbb E|f|^4-\mathbb E|f-\mu|^4
=A\,\mathbb E[(f-a\mu)^2(f-b\mu)^2].}\tag{1}
\]
In particular the right side is nonnegative, so \(\|C\|^4\le K\). A nonzero equality function must have \(\mu\ne0\), because \(\mu=0\) makes the remainder \(A\mathbb E|f|^4>0\). Thus equality in (1) means \(f\in\{a\mu,b\mu\}\) almost surely. Writing \(B=\{f=b\mu\}\) and taking expectations forces \(\mathbb P(B)=(a-1)/(a-b)=\alpha\). Conversely such an event yields an equality function.

**2. A uniform lower gap.** Normalize \(\mathbb E|f|^4=1\) and denote its deficit in (1) by \(D=K-\mathbb E|f-\mu|^4\). For each sample value choose the nearer of \(a\mu\) and \(b\mu\); call this chosen root \(r\), its error \(e=f-r\), and let \(B\) be the measurable set on which \(b\mu\) is chosen. The farther root has distance at least both \(|e|\) and \(d|\mu|/2\) from \(f\). Consequently
\[
\mathbb E|e|^4\le D/A,\qquad
\mathbb E|e|^2\le\frac{4D}{A d^2\mu^2}\quad(\mu\ne0).
\]
Writing \(t=\mathbb P(B)\), the mean identity gives
\[
\mathbb E e=\mu(1-a+dt)=d\mu(t-\alpha).
\]
Cauchy--Schwarz then yields
\[
D\ge\frac{A d^4\mu^4}{4}|t-\alpha|^2
\ge\frac{A d^4\mu^4}{4}\delta(\mathbb P)^2.\tag{2}
\]
Also \(1=\|f\|_4\le\|r\|_4+\|e\|_4\le M|\mu|+(D/A)^{1/4}\). If \(D<A/16\), then \(|\mu|>1/(2M)\), and (2) gives \(D\ge A d^4\delta^2/(64M^4)\). If \(D\ge A/16\), use \(\delta\le\alpha\) to get \(D\ge A\delta^2/(16\alpha^2)\). Taking the infimum over normalized \(f\) gives the stated lower inequality, including the \(\mu=0\) case (then \(D=A\)).

**3. A uniform upper gap.** Fix any event \(B\), write \(t=\mathbb P(B)\), \(\eta=t-\alpha\), and define the two-valued test function
\[
g=(a+d\eta)\mathbf1_{\Omega\setminus B}
+(b+d\eta)\mathbf1_B.
\]
Its mean is exactly \(a-dt+d(t-\alpha)=1\), so Jensen's inequality gives \(\mathbb E|g|^4\ge1\). Substituting in (1),
\[
D(g)= A d^4\eta^2\big[(1-t)(1+\eta)^2+t(1-\eta)^2\big]
\le A d^4(1+|\eta|)^2\eta^2.
\]
For each \(\varepsilon>0\), choose an event with \(|\eta|\le\delta(\mathbb P)+\varepsilon\); such events exist by the definition of the infimum, and the empty event shows \(\delta\le\alpha\). Hence the norm estimate \(K-\|C\|^4\le D(g)/\mathbb E|g|^4\) and letting \(\varepsilon\downarrow0\) give \(K-\|C\|^4\le C_*\delta^2\).

**4. Equality, sharp order and arithmetic consequence.** Both inequalities together imply that the norm equals \(K^{1/4}\) precisely when \(\delta=0\). The equality-function criterion follows from the first step. For two-atom laws with probabilities \(t,1-t\) approaching \(\alpha\), the attainable-mass distance equals \(|t-\alpha|\), so the two estimates force a deficit of exactly quadratic **order** in that distance. Thus neither a strictly larger exponent for a universal upper estimate nor a strictly smaller exponent for a universal lower estimate is possible.

For uniform \(n\)-atom measures the distance is \(\operatorname{dist}(n\alpha,\mathbb Z)/n\). The number \(\alpha\) obeys
\[
54\alpha^4-108\alpha^3+72\alpha^2-18\alpha+1=0
\]
and is irrational: a reduced rational root \(u/v\) would require \(3\mid v\) by reducing the cleared polynomial modulo three; then \(3\nmid u\), and its first term has exact three-adic valuation three while the other four terms have valuation at least four, impossible. Thus every finite uniform measure has a strictly positive deficit, with its size controlled by the stated squared subset-mass distance.

## Verification

The included standard-library script `verify.py` checks the algebraic coefficient identity in the exact number field \(\mathbb Q(\sqrt3,\sqrt{3+2\sqrt3})\), verifies the algebraic relation for \(\alpha\), tests 200 weighted finite instances of the integrated sum-of-squares identity, 200 constructive finite-weight witnesses, and 1000 two-atom comparisons against the exact two-point norm formula. Execute `python3 verify.py`. The exhaustive symbolic coefficient calculation checks one crucial lemma; the finite numerical tests are illustrations, not a proof for arbitrary probability spaces.

## Relationship to prior work

Franchetti determined the unrestricted sharp centered \(L^p\) constants, and Móri independently provided the reduction to two-point laws. In particular the benchmark \(K=1+2/\sqrt3\) is **previously known** and is not claimed new. Aksoy and Lewicki treated minimality of projections through group averaging; those general projection statements do not supply the event-mass deficit. Lewicki and Skrzypek gave precise equal-weight finite-dimensional hyperplane projection results (including certain sufficiently large dimensions), so the finite-uniform consequence here is not presented as an independent exact finite-dimensional norm formula. Shargorodsky and Sharia give general bounds for centered and conditionally centered moments but do not state the universal two-sided quadratic dependence on the range of event masses in their inspected discussion. The claimed contribution is the **all-probability-space quantitative equivalence**, exact quartic remainder mechanism, and equality classification, not a new universal benchmark constant.

## Limitations

The positive constants are far from optimal. The result does not give the exact operator norm when \(\delta>0\), nor does it extend to complex random variables, exponents other than four, or arbitrary conditional expectations. The 1990 source and complete 2016 article could not be materially compared in full, leaving a risk that an older general theorem contains an equivalent weighted-atom stability statement. No exhaustive historical priority or independent validation is claimed.

## References

1. A. G. Aksoy and G. Lewicki, *Minimal projections with respect to various norms*, arXiv:1007.2214v1 (first submitted 2010-07-13), https://arxiv.org/abs/1007.2214.
2. C. Franchetti, *The norm of the minimal projection onto hyperplanes in* \(L^p[0,1]\) *and the radial constant*, Boll. Unione Mat. Ital. B 4 (1990), 803–821.
3. T. F. Móri, *Sharp inequalities between centered moments*, J. Inequal. Pure Appl. Math. 10 (2009), article 99, https://eudml.org/doc/225301.
4. G. Lewicki and L. Skrzypek, *Minimal projections onto hyperplanes in* \(\ell_p^n\), J. Approx. Theory 202 (2016), 42–63, https://doi.org/10.1016/j.jat.2015.11.005.
5. E. Shargorodsky and T. Sharia, *Sharp estimates for conditionally centered moments and for compact operators on* \(L^p\) *spaces*, Math. Nachr. 296 (2023), 368–381, https://doi.org/10.1002/mana.202100217.
