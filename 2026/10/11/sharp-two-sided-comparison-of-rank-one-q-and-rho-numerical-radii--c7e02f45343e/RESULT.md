# Sharp two-sided comparison of rank-one \(q\)- and \(\rho\)-numerical radii

## Finding

**Theorem (complete sharp comparison).** Let \(\mathcal H\) be a complex Hilbert space with \(\dim\mathcal H\ge 2\). Fix \(0\le q\le1\) and \(\rho>0\), and put
\[
 s=\sqrt{1-q^2},\qquad \eta=|\rho-1|,\qquad t=\frac{q}{1+s}.
\]
For every nonzero rank-one operator \(T\in\mathcal B(\mathcal H)\), the best possible constants in the simultaneous inequalities
\[
 m_{\rho,q}\,\omega_q(T)\le\omega_\rho(T)\le M_{\rho,q}\,\omega_q(T)
\]
are
\[
 \boxed{m_{\rho,q}=\begin{cases}
 \dfrac{1-\eta^2}{\rho(1-q\eta)},&0\le\eta<t,\\[5pt]
 \dfrac{2}{\rho(1+s)},&\eta\ge t,
 \end{cases}}
 \qquad
 \boxed{M_{\rho,q}=\max\!\left\{\dfrac{2}{\rho(1+s)},\dfrac{2(1+\eta)}{\rho(1+q)}\right\}.}
\]
The denominator \(1-q\eta\) in the first branch is strictly positive because that branch requires \(\eta<t\le1\).

For unit vectors \(a,b\), write \(c=|\langle a,b\rangle|\), and take \(T(x)=\langle x,a\rangle b\). If \(0\le q<1\), the **minimizing overlap is unique**: it equals \(c=0\) when \(\eta\ge t\), while for \(\eta<t\) it is
\[
 \boxed{c_* =\frac{q(1+\eta^2)-2\eta}{1+\eta^2-2q\eta}\in(0,1).}
\]
For \(0\le q<1\), a maximizing overlap is always \(c=0\) or \(c=1\), with the larger of the two displayed endpoint constants deciding which one. Both endpoints maximize in case of equality between those constants, and no interior overlap maximizes. Equivalently, if \(q>s\), the maximum switches from the orthogonal case to the parallel case at \(\eta=(q-s)/(1+s)\); when \(q\le s\), the parallel case always maximizes, apart from the equality case \(q=s,\eta=0\).

When \(q=1\), the ratio is monotone in \(c\): its minimum is at \(c=1\) if \(\eta<1\), at \(c=0\) if \(\eta>1\), and every overlap is simultaneously minimizing and maximizing if \(\eta=1\) (equivalently, \(\rho=2\)). The maximizing overlap is the opposite endpoint when \(\eta\ne1\). Every ratio between the displayed sharp constants occurs in every complex Hilbert space of dimension at least two.

## Assumptions and scope

Here \(\omega_q(T)\) denotes the \(q\)-numerical radius
\[
 \sup\{|\langle Tx,y\rangle|:\|x\|=\|y\|=1,\ \langle x,y\rangle=q\},\qquad 0\le q\le1.
\]
The \(\rho\)-numerical radius \(\omega_\rho(T)\) is the Minkowski functional of operators admitting a unitary \(\rho\)-dilation: \(T/\omega_\rho(T)\) lies at the boundary of the class for which \(T^k=\rho P_{\mathcal H}U^k|_{\mathcal H}\) for all positive integers \(k\) (the functional is defined by an infimum of such scalings). These are two distinct standard numerical-radius generalizations; neither parameter is an exponent. A rank-one \(T\) has representation \(T(x)=\langle x,a\rangle b\) with nonzero \(a,b\). Its normalized overlap \(c=|\langle a,b\rangle|/(\|a\|\|b\|)\) belongs to \([0,1]\) and is independent of the representation.

Both existing rank-one identities from the cited literature are used with their original parameter domains and normalizations. The new assertion is the optimal two-sided comparison across **all** rank-one operators at fixed \((\rho,q)\), including every equality and phase-boundary case; it does not assert these two source identities as new.

## Proof

**Reduction to one scalar.** Denčić, Stanković, Krstić and Damnjanović [1, Theorem 2.1] prove
\[
 \omega_q(T)=\frac{\|a\|\|b\|}{2}\left(1+qc+s\sqrt{1-c^2}\right).
\]
Stanković [2, Theorem 2.2] proves
\[
 \omega_\rho(T)=\frac{\|a\|\|b\|}{\rho}(1+\eta c).
\]
Thus the ratio of positive quantities is exactly
\[
 F(c)=\frac{\omega_\rho(T)}{\omega_q(T)}
 =\frac{2(1+\eta c)}{\rho(1+qc+s\sqrt{1-c^2})},\quad 0\le c\le1.
\]
Every such \(c\) is realized, with orthonormal \(e_1,e_2\), by the rank-one map \(T_c(x)=\langle x,e_1\rangle(c e_1+\sqrt{1-c^2}\,e_2)\). This proves that minimizing and maximizing \(F\) gives globally sharp operator constants and that every intermediate value is realized by continuity.

**Strictly unimodal interior problem.** Suppose \(0\le q<1\), so \(s>0\). For \(0<c<1\), direct differentiation shows that the sign of \(F'(c)\) is the sign of
\[
 G(c)=\eta-q+s\frac{\eta+c}{\sqrt{1-c^2}},\qquad
 G'(c)=\frac{s(1+\eta c)}{(1-c^2)^{3/2}}>0.
\]
At the left endpoint, \(G(0)=\eta(1+s)-q\). Hence \(G\) has no zero if \(\eta\ge t\), and then \(F\) increases strictly on \((0,1)\) (possibly with zero right derivative at the left endpoint), giving the unique minimum at \(c=0\). If \(\eta<t\), then \(G(0)<0\), while \(G(c)\to+\infty\) as \(c\to1^-\); consequently \(F\) has exactly one critical point, its global strict minimum. Solving \(G(c)=0\), choosing the positive square-root branch, gives
\[
 c_*=\frac{q(1+\eta^2)-2\eta}{1+\eta^2-2q\eta},\qquad
 \sqrt{1-c_*^2}=\frac{s(1-\eta^2)}{1+\eta^2-2q\eta}.
\]
Both identities follow by expanding squares using \(q^2+s^2=1\); the denominators are positive because \(\eta<t<1\). Substitution gives
\[
 F(c_*)=\frac{1-\eta^2}{\rho(1-q\eta)}.
\]
The endpoint value is \(F(0)=2/[\rho(1+s)]\). Since there is no interior local maximum, the sharp maximum is \(\max\{F(0),F(1)\}\), where \(F(1)=2(1+\eta)/[\rho(1+q)]\). The strict derivative-sign pattern shows that both endpoints are the only maximizing overlaps when their values coincide. Their equality reduces to \(q-s=\eta(1+s)\), which produces the second stated switch; for \(q=s,\eta=0\) it is the boundary equality case.

**The case \(q=1\).** Here \(s=0\), and
\[
 F(c)=\frac{2(1+\eta c)}{\rho(1+c)},\qquad
 F'(c)=\frac{2(\eta-1)}{\rho(1+c)^2}.
\]
It decreases when \(\eta<1\), increases when \(\eta>1\), and is constant when \(\eta=1\). The formulas and all equality statements follow by evaluating at \(c=0,1\), including \(\rho=2,q=1\), when the two numerical radii coincide. This completes every endpoint and parameter case.

## Verification

The accompanying standalone `verify_ratio.py` uses only the Python standard library. Running `python3 verify_ratio.py` checks exact rational witnesses, both threshold regimes, and rational instances of the derived formula, including the degenerate equality \(q=1,\rho=2\). In particular, for \(q=3/5\), \(\rho=6/5\), one has \(s=4/5\), \(\eta=1/5\), \(c_*=7/25\), and
\[
 F(0)=\frac{25}{27},\qquad F(7/25)=\frac{10}{11},\qquad F(1)=\frac54.
\]
The infinite-dimensional and continuous-parameter conclusions come from the preceding exact calculus argument and the cited rank-one identities, **not** from finite tests.

## Relationship to prior work

[1] determines \(\omega_q(T)\) for fixed rank-one \(T\), including a study of dependence on \(q\) with the operator fixed. [2] independently determines \(\omega_\rho(T)\) for rank-one \(T\) and studies parametrized Buzano-type bounds. The two source formulas are used as established input. Neither inspected manuscript states the sharp cross-gauge ratio over all rank-one operators, its interior minimizing overlap, or both transition boundaries. Other operator-radius comparisons, including [3], concern different weighted radii or wider classes without this full rank-one extremizer classification. In particular, comparing the two formulas **pointwise at a specified operator** does not give their optimum over operator geometry at fixed parameters; the sign and stationary-point analysis above supplies that optimization.

## Limitations

The result is specific to nonzero rank-one operators on complex Hilbert spaces of dimension at least two. It does not assert identical constants for arbitrary-rank operators or a novel formula for either radius individually. The two formulas used as premises are previously published mathematical results, and the remaining argument is elementary calculus. No independence or external certification is claimed. Although relevant full texts and indexed research records were checked, an equivalent unindexed characterization could exist.

## References

[1] D. Denčić, H. Stanković, M. Krstić, I. Damnjanović, *\(q\)-numerical radius of rank-one operators and the generalized Buzano inequality*, arXiv:2503.05036v1 (first posted 2025-03-06), Theorem 2.1 and Section 3; https://arxiv.org/html/2503.05036v1.

[2] H. Stanković, *On the \(\rho\)-numerical radius of rank-one operators and parametrized Buzano-type inequalities*, arXiv:2609.00037v1 (first posted 2026-08-29), Theorem 2.2 and Sections 1–2; https://arxiv.org/html/2609.00037v1.

[3] M. Khosravi and A. Sheikhhosseini, *A Comparison of some Weighted Numerical Radii of Hilbert Space Operators*, arXiv:2608.09178v1 (2026-08-10), Sections 2–5; https://arxiv.org/abs/2608.09178.
