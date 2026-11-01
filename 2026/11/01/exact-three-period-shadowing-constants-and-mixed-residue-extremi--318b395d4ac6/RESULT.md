# Exact three-period shadowing constants and mixed-residue extremizers for bilateral weighted shifts

## Finding
Let \(H=\ell^2(\mathbb Z)\) be complex and let \(T e_j=w_j e_{j+1}\), with strictly positive weights of period \(p\ge1\) and product \(c=\prod_{j=0}^{p-1}w_j\ne1\). For a two-sided approximate orbit \((y_n)_{n\in\mathbb Z}\) satisfying \(\sup_n\|y_{n+1}-Ty_n\|\le\delta\), let \(S(T)\) be the least real \(K\) such that some exact two-sided orbit \((x_n)\) has \(\sup_n\|x_n-y_n\|\le K\delta\), uniformly over all \(\delta>0\) and all approximate orbits. Then \(S(T)\) is given **exactly** by the following finite simplex maximizations, indices read modulo \(p\):

If \(0<c<1\), put \(a_{i,0}=1\) and \(a_{i,r}=\prod_{s=1}^r w_{i-s}\) for \(1\le r<p\). Then
\[
S(T)=\frac{1}{1-c}\max_{x\in\Delta_{p-1}}\sum_{r=0}^{p-1}\sqrt{\sum_{i=0}^{p-1}a_{i,r}^2 x_i}.
\]
If \(c>1\), put \(b_{i,r}=\prod_{s=0}^{r-1}w_{i+s}^{-1}\), for \(1\le r\le p\). Then
\[
S(T)=\frac{1}{1-c^{-1}}\max_{x\in\Delta_{p-1}}\sum_{r=1}^{p}\sqrt{\sum_{i=0}^{p-1}b_{i,r}^2 x_i}.
\]
Here \(\Delta_{p-1}=\{x_i\ge0:\sum_i x_i=1\}\). In the unstable formula the final summand is the constant \(c^{-1}\).

**Three-period closed solution.** For \(p=3\), define \((A_i,B_i)=(w_{i-1}^2,(w_{i-1}w_{i-2})^2)\) in the stable case and \((A_i,B_i)=(w_i^{-2},(w_iw_{i+1})^{-2})\) in the unstable case. Let \(L=1\) if \(c<1\), and \(L=c^{-1}\) if \(c>1\). The optimal constant is
\[
S(T)=\frac{L+M}{1-\min\{c,c^{-1}\}},\quad M=\max_{0\le i<j\le2}E_{ij},
\]
where \(E_{ij}\) is the maximum of \(\sqrt{A_i}+\sqrt{B_i}\), \(\sqrt{A_j}+\sqrt{B_j}\), and, only when the edge has opposing coordinate slopes and its critical point is internal, the following radical. Orient the endpoints so \(a=A_i-A_j>0\) and \(b=B_j-B_i>0\), and set
\[
t_* =\frac{a^2 B_j-b^2 A_j}{ab(a+b)}.
\]
When \(0<t_*<1\), the additional candidate is
\[
\sqrt{\frac{(a+b)(a B_j+b A_j)}{ab}}.
\]
No interior critical point is used when the edge coordinates are monotone in the same direction. In particular, there exists an optimal dual vector with nonzero mass in at most two congruence classes; this need not reduce to one class.

For the exact stable three-period weights \((10,1,1/20)\), the unique optimal residue masses are \(x_0=0\), \(x_1=1724711/3489255\) and \(x_2=1-x_1\). The sharp constant is
\[
S(T)=2+\frac{\sqrt{15507412305}}{4389}=30.3729234347\ldots.
\]
Every vector supported in a single residue class yields at most \(24\). Thus optimizing only over coordinate classes underestimates the actual sharp uniform error-amplification factor by more than one quarter.

## Assumptions and scope
All Hilbert spaces, shift coefficients and pseudo-orbits above are complex. The weights are strictly positive, periodic in the space index, and the product \(c\) differs from one. Errors are bounded uniformly over **all** positive and negative time indices, in the Hilbert norm. The constant concerns existence of an exact orbit uniformly tracking **every** such approximate orbit. It is not the \(\ell^2\)-in-time resolvent norm, a finite-horizon stability constant, or the best coordinate-vector bound. Neither the critical product \(c=1\) nor arbitrary nonperiodic weights are claimed.

## Proof
**1. Exact bounded correction.** Write \(e_n=y_{n+1}-Ty_n\) and \(d_n=y_n-x_n\). Then \(d_{n+1}=Td_n+e_n\). The identity \(T^p=c U^p\), with \(U\) the unit bilateral shift, shows \(\|T^n\|\to0\) geometrically when \(c<1\). The unique bounded solution of the correction recurrence is then
\[
d_n=\sum_{j=0}^{\infty} T^j e_{n-1-j}.
\]
When \(c>1\), \(\|T^{-n}\|\to0\) geometrically and the unique bounded correction is
\[
d_n=-\sum_{j=0}^{\infty}T^{-j-1}e_{n+j}.
\]
The series converge uniformly for bounded errors. Uniqueness follows by iterating any bounded homogeneous solution in the exponentially contracting forward or backward direction. Since every bounded error sequence is realized by the pseudo-orbit obtained by taking \(y=d\) and the exact orbit \(x=0\), this correction operator norm equals the claimed optimal shadowing modulus, with no loss from restricting to pseudo-orbits.

**2. Dual norm and residues.** For bounded \((e_j)\), Hilbert-space duality gives exactly
\[
\sup_{\sup_j\|e_j\|\le1}\big\|\sum_{j\ge0}T^j e_j\big\|
=\sup_{\|v\|=1}\sum_{j\ge0}\|(T^*)^j v\|.
\]
The equality holds by independently selecting each error vector aligned with \((T^*)^jv\); truncation and absolute convergence justify interchanging limits. Replace \(T^j\) by \(T^{-j-1}\) for the unstable case. Because \((T^*)^{p}=cU^{-p}\) and \(((T^{-1})^*)^{p}=c^{-1}U^p\), group each series into residues \(r\) modulo \(p\) to obtain the factors \((1-c)^{-1}\) and \((1-c^{-1})^{-1}\), respectively. For \(v\), write \(x_i=\sum_{k\in\mathbb Z}|\langle v,e_{pk+i}\rangle|^2\). Then \(x\in\Delta_{p-1}\) and the squared norms of all truncated adjoint powers have precisely the listed weighted averages. Conversely every simplex point is realized by a unit vector supported on any choice of one coordinate in each residue class. Therefore the finite maximizations are exact, not estimates.

**3. Geometry of three-period optimization.** Once the constant term is removed, the objective is \(F(x)=\sqrt{\sum_iA_ix_i}+\sqrt{\sum_iB_ix_i}\). Its image depends only on \((A,B)\in\operatorname{conv}\{(A_i,B_i):0\le i\le2\}\). The function \(\sqrt A+\sqrt B\) is strictly increasing in both coordinates. Any interior point of a two-dimensional triangle admits a small perturbation increasing both, so cannot maximize. A degenerate triangle is already a segment. Thus a maximum lies on one of its three edges, establishing two-class support. Along an edge, the two square roots are concave. If the coordinate slopes have the same sign the larger endpoint wins. With opposite signs, differentiating gives the single stationary candidate \(t_*\) above; its value simplifies algebraically to the displayed radical. Strict concavity when both slopes are nonzero gives uniqueness on an edge whenever the stationary point is internal.

**4. Exact three-period witness.** For \((w_0,w_1,w_2)=(10,1,1/20)\), the three points \((A_i,B_i)\) equal \((1/400,1/400)\), \((100,1/4)\), \((1,100)\). The first is strictly coordinate-dominated by the third, so its mass must vanish at every maximum. Put \(t=x_1\). The remaining expression is
\[
F(t)=\sqrt{1+99t}+\sqrt{100-(399/4)t},\qquad 0\le t\le1.
\]
Its derivative vanishes uniquely at \(t=1724711/3489255\), and its endpoint derivative signs show this is an internal maximum. Exact rational simplification gives \(F(t_*)=\sqrt{15507412305}/8778\); multiply by \((1-1/2)^{-1}=2\), and include the constant summand \(1\). The largest one-class value is \(2(1+1+10)=24\), completing the strict-mixing demonstration.

## Verification
The included standalone `check_shadowing.py` independently evaluates the exact rational witness, checks the edge closed formula against dense grid maximization for positive sample weights in both stable and unstable regimes, and checks the convergent finite-truncation Green sums against the simplex formula. Run it using `python check_shadowing.py` with Python 3, SymPy and NumPy; the mathematical result itself is proved above, not inferred from a finite grid or experiment.

## Relationship to prior work
Pinto, *Shadowing for weighted composition operators on spaces of continuous functions* (arXiv:2607.28361v1, publicly submitted July 30, 2026) establishes qualitative shadowing classifications for weighted shifts and related composition operators. Yuan, *A Quantitative Shadowing Lemma for Hyperbolic Operators* (preprints.org/202610.2146v1, posted October 22, 2026), already uses an exact dual Green-operator norm and reports an explicitly computable bilateral-weighted-shift example. Bernardes and Peris (2024) develop broader qualitative linear shadowing theory. Accordingly the dual-Green principle and qualitative existence are **not** presented as new. The mathematical claim here is the uniform, explicit all-positive-weight period-three algebraic optimization, its two-residue sufficiency, and the sharply mixed-residue witness, including the exact value and failure of single-residue testing.

## Limitations
This classification is exact for strictly positive periodic weights with product unequal to one; it makes no critical-product or nonperiodic assertion. The 2026 Yuan paper's available abstract is particularly close because it announces exact dual Green norms and weighted-shift constants; its full text was inaccessible during this comparison. Hence the complete absence of a prior equivalent three-period radical formula cannot be guaranteed and independent publication-priority checking remains warranted. The 2026 Pinto preprint's full text was likewise inaccessible; only its abstract and bibliographic metadata were available. Those access restrictions are not used to claim that the papers do not contain a statement. No independent mathematical audit was performed.

## References
1. João V. A. Pinto, *Shadowing for weighted composition operators on spaces of continuous functions*, arXiv:2607.28361v1 (July 30, 2026), https://arxiv.org/abs/2607.28361.
2. Zisong Yuan, *A Quantitative Shadowing Lemma for Hyperbolic Operators*, Preprints.org 202610.2146v1 (posted October 22, 2026), https://www.preprints.org/manuscript/202610.2146.
3. Nilson C. Bernardes Jr. and Alfred Peris, *On shadowing and chain recurrence in linear dynamics*, Advances in Mathematics 441 (2024), 109539, https://doi.org/10.1016/j.aim.2024.109539.
