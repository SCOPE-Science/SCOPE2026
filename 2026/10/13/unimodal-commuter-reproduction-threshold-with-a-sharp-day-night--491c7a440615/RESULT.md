# Unimodal commuter reproduction threshold with a sharp day–night transition

## Finding

For the unvaccinated, **autonomous** two-city metropolitan SIR model of Moschen and Aronna [1], a one-way commuter fraction can reduce the disease-invasion reproduction number, but the reduction has an exact structural limit: the reproduction number is strictly decreasing up to at most one interior optimum and is strictly increasing thereafter. A precisely characterized symmetric-population/half-transmission benchmark has an interior optimum **if and only if** the resident-time weight is smaller than \(2/3\). In a second exact benchmark, intermediate commuting suppresses invasion although both no commuting and nearly complete commuting allow invasion.

More precisely, let \(\beta_1>\beta_2>0\) be the transmission rates, \(n_1,n_2>0\) the residence populations, \(\gamma,\mu>0\) the common recovery and demographic rates, \(\alpha\in[0,1)\) a **constant** nighttime/resident-exposure weight, and \(p\in[0,1)\) the fraction of city-2 residents commuting to city 1. City-1 residents remain in city 1. At the disease-free equilibrium, denote the associated autonomous basic reproduction number by \(\mathcal R_0(p)\).

**General theorem.** For these parameters, \(\mathcal R_0(p)\) either strictly decreases throughout \([0,1)\), or has a unique point \(p_*\in(0,1)\) such that it strictly decreases for \(p<p_*\) and strictly increases for \(p>p_*\). In the first case the infimum is a limiting value as \(p\uparrow1\), not necessarily an admissible optimum.

**Sharp benchmark phase boundary.** If \(n_1=n_2\) and \(\beta_2=\beta_1/2\), an interior optimal fraction exists exactly for \(0\le\alpha<2/3\); for \(2/3\le\alpha<1\), the threshold strictly decreases on the entire original domain. When \(\alpha=0\), its unique minimizer and minimum normalized Perron eigenvalue are
\[
p_*=\sqrt3-\sqrt2,\qquad
\min_{0\le p<1}\frac{(\gamma+\mu)\mathcal R_0(p)}{\beta_1}
=\frac{\sqrt6+\sqrt3-\sqrt2-1}{2}.
\]
For this same benchmark with \(\beta_1/(\gamma+\mu)=11/10\) and \(\alpha=0\), the two and only two invasion thresholds are
\[
p_{\pm}=\frac{79\pm\sqrt{2281}}{220},\qquad
0<p_-<p_+<1.
\]
The disease-free equilibrium is linearly invasion-stable when \(p_-<p<p_+\) and linearly invasion-unstable for \(0\le p<p_-\) and \(p_+<p<1\). At \(p=p_{\pm}\), the infected linearization has a zero eigenvalue; no nonlinear threshold claim is made there.

## Assumptions and scope

The residence-to-work mobility matrix is
\[
P=\begin{pmatrix}1&0\\p&1-p\end{pmatrix},
\]
and daily average exposures are described by the constant parameter \(\alpha\), not by a periodic on/off switching schedule. No vaccination is applied. All parameters satisfy the strict positivity assumptions above; the conclusion permits \(\alpha=0\) and \(p=0\), but requires \(p<1\), as the daytime population of city 2 vanishes when \(p=1\) and the source's effective-prevalence formula would divide by zero. Matrix expressions at \(p=1\) below always mean their well-defined continuous limits from below. Only this limiting *matrix*, not the original nonlinear model, is evaluated there.

Let
\[
a=\alpha,\quad q=1-a,\quad b=\frac{\beta_2}{\beta_1}\in(0,1),\quad r=\frac{n_2}{n_1}>0.
\]
The source's next-generation formula at the disease-free state [1, Appendix A.1] is
\[
\mathcal R_0(p)=\frac{\rho(F(p))}{\gamma+\mu},\qquad
F(p)=a\operatorname{diag}(\beta_1,\beta_2)+qP\operatorname{diag}(\beta_1,\beta_2)E^{-1}P^{\mathsf T}N,
\]
where \(N=\operatorname{diag}(n_1,n_2)\) and \(E=\operatorname{diag}(n_1+pn_2,(1-p)n_2)\). All inverses exist on the stated domain. The standard linear invasion classification uses the sign of the leading eigenvalue of \(F(p)-(\gamma+\mu)I\); it does not address periodic Floquet multipliers or final epidemic size.

## Proof

**1. Symmetric two-by-two reduction.** Conjugating \(F(p)/\beta_1\) by the positive diagonal population scaling gives a symmetric matrix with the same eigenvalues,
\[
H(p)=\begin{pmatrix}
 a+\dfrac{q}{1+rp}&\dfrac{q\sqrt r\,p}{1+rp}\\[4pt]
 \dfrac{q\sqrt r\,p}{1+rp}&b(1-qp)+\dfrac{qrp^2}{1+rp}
\end{pmatrix}.
\]
Set \(L(p)=\lambda_{\max}(H(p))\). The entries are real-analytic on a neighborhood of \([0,1]\); the upper eigenvalue is simple at \(p=0\), because \(H(0)=\operatorname{diag}(1,b)\), and at \(p>0\), because the off-diagonal entries are strictly positive. Therefore \(L\) is real-analytic on \([0,1]\). Also \(L(p)\ge H_{11}(p)>a\) and \(\mathcal R_0(p)=\beta_1L(p)/(\gamma+\mu)\).

**2. An exact implicit quadratic.** Direct evaluation of the determinant gives
\[
Q(z,p):=(1+rp)\det(zI-H(p))
=(z-1)(z-b)
+p\{r(z-a)(z-b)+bq(z-1)\}
-rq(1-b)(z-a)p^2.
\]
At \(z=L(p)\), the identity \(Q(L(p),p)=0\) holds. Since the two eigenvalues are distinct,
\[
Q_z(L(p),p)=(1+rp)\{L(p)-\lambda_{\min}(H(p))\}>0.
\]
Implicit differentiation yields \(L'=-Q_p/Q_z\). At \(p=0\), \(L(0)=1\), and consequently
\[
L'(0)=-r(1-a)<0.
\]
At any interior point where \(L'=0\), differentiating twice gives
\[
L''(p)=-\frac{Q_{pp}(L(p),p)}{Q_z(L(p),p)}
=\frac{2rq(1-b)(L(p)-a)}{Q_z(L(p),p)}>0.
\]
Thus every stationary point is a strict local minimum. Two such points would force a distinct interior stationary local maximum between them, impossible by the strictly positive second derivative at every stationary point. This proves the general theorem, including strict monotonicity on either side of the unique possible minimum. The same curvature identity is valid at the limiting endpoint whenever \(L'(1)=0\), showing that a zero derivative at that endpoint cannot follow an earlier interior minimum.

**3. Exact day–night phase transition.** Put \(r=1\) and \(b=1/2\). The larger eigenvalue of the continuous limiting matrix at \(p=1\) is
\[
L(1)=\frac{2+a+\sqrt{5a^2-8a+4}}4.
\]
Substitution in the implicit derivative gives the exact identity
\[
Q_p(L(1),1)=\frac{(1-a)(3a-2)}4.
\]
Because \(Q_z>0\) and \(L'(0)<0\), if \(a<2/3\) then \(L'(1)>0\) and there is exactly one interior critical point, necessarily the global minimum. If \(a>2/3\), then \(L'(1)<0\), so no stationary point occurs and \(L\) is strictly decreasing. At \(a=2/3\), the limiting derivative vanishes but the endpoint curvature formula gives \(L''(1)>0\). Hence \(L'<0\) immediately to the left of 1; again the no-maxima argument excludes interior stationary points. This proves the sharp iff statement on the entire parameter interval.

**4. Exact optimal fraction and two invasion crossings.** At \(a=0\), eliminating \(z\) from \(Q(z,p)=0\) and \(Q_p(z,p)=0\) in the benchmark gives
\[
p^4-10p^2+1=0.
\]
Its sole root in \((0,1)\) is \(p_*=\sqrt3-\sqrt2\); direct substitution in the upper-eigenvalue branch yields the stated minimum. If \(\beta_1/(\gamma+\mu)=11/10\), the condition \(\mathcal R_0=1\) becomes \(L=10/11\). Substitution in \(Q(10/11,p)\) gives the two roots \(p_{\pm}\) stated above. They both belong to \((0,1)\). For this benchmark, \(H(p)\) is a rank-one nonnegative update of \(\operatorname{diag}(0,(1-p)/2)\), so its smaller eigenvalue is at most \(1/2<10/11\): both determinant roots are crossings of the **top** eigenvalue, not artifacts of the smaller root. Since \(L(0)=\lim_{p\uparrow1}L(p)=1\) and \(L\) has exactly one minimum, \(\mathcal R_0<1\) exactly between these crossings, with the inequalities reversing outside. The infected Jacobian is \(F-(\gamma+\mu)I\), so these inequalities give precisely the stated linear invasion classification.

## Verification

A standalone script, `verify_commuter.py`, symbolically checks the characteristic identity, its partial derivatives, the exact limiting derivative factor, the stationary-point elimination polynomial, the radical minimizer, the exact threshold roots, and the rational commuting witness. It runs finite spectral samples as a non-proof sanity check. Run `python verify_commuter.py` with Python 3, SymPy, and NumPy. The replayed output is `VERIFY_OK`. The analytic all-parameter unimodality proof is above and does not rely on sampled numerical data.

For a direct rational witness, at \(a=0\) and \(p=1/3\),
\[
L(1/3)=\frac{7+\sqrt{13}}{12},\qquad
\mathcal R_0(1/3)=\frac{11(7+\sqrt{13})}{120}<1,
\]
whereas the no-commuting value and the near-full-commuting limit are both \(11/10>1\).

## Relationship to prior work

Moschen and Aronna [1] derive the next-generation matrix, establish general and metropolitan bounds in Theorems 2.1–2.2, and examine the effects of mobility parameters through simulations in Appendix C.1. Those results do not themselves specify the exact one-way commuting minimizer, show global unimodality, locate the sharp \(2/3\) transition, or yield the pair of exact invasion crossings. The theorem here specializes and analyzes **their** commuting matrix, not a replacement model.

Rapaport and Mimouni [2] already analyze and minimize the epidemic threshold in another two-patch commuter SIR system and explicitly show that commuting toward the higher-transmission patch can reduce the threshold. Therefore neither that counterintuitive possibility nor the broad idea of commuter optimization is asserted to be novel here. Their analysis distinguishes permanent residents and explicit switching-rate commuter groups in a larger state system; it does not imply the stated characteristic identity and sharp day–night transition for the residence-to-work averaging model of [1]. A 2023 precursor dissertation by Moschen [3] predates [1] but its complete text could not be inspected; this is an unresolved comparison risk.

## Limitations

The result is for an autonomous, time-averaged day–night weight and no vaccination; the original source also considers piecewise periodic switching and vaccination controls, to which this theorem is not extended. It establishes **linear disease-free invasion thresholds**, not global extinction, nonlinear bifurcation type at \(\mathcal R_0=1\), or an optimum of the paper's economic vaccination-control objective. At \(p=1\), city 2 has zero daytime population and the original effective-prevalence division is undefined; only the continuous limiting eigenvalue matrix is used. The benchmark \(n_1=n_2\) is a mathematical symmetry case, not a claim about measured metropolitan populations. The possibility of a previously unindexed equivalent derivation in [3] or other literature remains open despite the comparisons below.

## References

[1] M. Soledad Aronna and Lucas Machado Moschen, *Optimal vaccination strategies on networks and in metropolitan areas*, arXiv:2402.00207, version 1 first public 2024-01-31; *Infectious Disease Modelling* **9** (2024), 1198–1222. https://arxiv.org/html/2402.00207v2 ; https://doi.org/10.1016/j.idm.2024.06.007 . Primary MSC 92D30.

[2] Alain Rapaport and Ismail Mimouni, *The role of permanently resident populations in the two-patches SIR model with commuters*, arXiv:2211.16137 (2022). https://arxiv.org/html/2211.16137v1 .

[3] Lucas Machado Moschen, *Optimal Vaccination Strategies for Epidemics in Metropolitan Areas*, Master's dissertation, Fundação Getulio Vargas (2023). https://repositorio.fgv.br/items/f1a36cab-6196-498f-b679-84763dd5d0ce . Complete text not accessible in this review; only bibliographic and synopsis material was available.
