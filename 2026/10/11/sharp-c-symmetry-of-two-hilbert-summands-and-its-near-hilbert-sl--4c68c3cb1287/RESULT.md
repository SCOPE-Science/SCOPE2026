# Sharp \(C\)-symmetry of two Hilbert summands and its near-Hilbert slope
## Finding
Let \(H\) and \(K\) be arbitrary nonzero **real** Hilbert spaces and let \(1<p<\infty\). Set
\[
Z_p=H\oplus_p K,
\qquad
\|(u,v)\|=\bigl(\|u\|_H^p+\|v\|_K^p\bigr)^{1/p}.
\]
The optimal global Chmieliński \(C\)-approximate symmetry parameter is
\[
\boxed{\displaystyle
\sigma_C(Z_p)
=\sigma_C(\ell_p^2)
=\max_{z\ge0}
\frac{\sinh(|p-2|z)}{\cosh(z)^{1/p}\cosh((p-1)z)^{(p-1)/p}}
}.
\tag{1}
\]
The formula is valid in arbitrary Hilbert dimensions, including infinite dimensions. If \(p=2\), the value is \(0\). If \(p\ne2\), the maximum is strictly positive, strictly below \(1\), and attained; every maximizing pair is blockwise collinear, with the two nonzero block pairings carrying opposite signs. In addition, the value is invariant under conjugate exponents:
\[
\sigma_C(Z_p)=\sigma_C(Z_{p/(p-1)}),
\tag{2}
\]
with arbitrary nonzero Hilbert fibers on either side.

There is a **sharp linear near-Hilbert law**. Let \(z_0>0\) solve
\[
z_0\tanh z_0=1,
\]
uniquely. Then, as \(p\to2\) through \(1<p<\infty\),
\[
\boxed{\displaystyle
\sigma_C(Z_p)
=\frac{z_0}{\cosh z_0}|p-2|+o(|p-2|)}.
\tag{3}
\]
Numerically \(z_0=1.1996786402577338\ldots\) and the sharp coefficient is \(0.66274341934918158\ldots\). For each \(p\ne2\), any maximizing positive hyperbolic parameter tends to \(z_0\) as \(p\to2\).

## Assumptions and scope
The scalar field is \(\mathbb R\); no dimension or separability restriction is imposed beyond \(\dim H,\dim K\ge1\). A unit Birkhoff–James pair satisfies \(x\perp_B y\) precisely when \(J(x)(y)=0\), because \(Z_p\) is smooth. With \(J(x)\) the unique norm-one support functional at \(x\in S_{Z_p}\), define
\[
\sigma_C(Z_p)=\sup\bigl\{|J(y)(x)|:x,y\in S_{Z_p},\ J(x)(y)=0\bigr\}.
\tag{4}
\]
Chmieliński's characterization says \(y\perp_B^\varepsilon x\) if and only if \(|J(y)(x)|\le\varepsilon\). Thus (4) is the sharp global reverse parameter. For \(p\ne2\), the proof below shows \(\sigma_C(Z_p)<1\), so the optimum lies in the customary range \([0,1)\).

## Proof
Write \(x=(u,v)\) and \(y=(\xi,\zeta)\), both norm one, and put
\[
a=\|u\|,\ b=\|v\|,\ c=\|\xi\|,\ d=\|\zeta\|.
\]
The normalized support functional in the Hilbert sum is
\[
J(x)(y)=a^{p-2}\langle u,\xi\rangle_H+b^{p-2}\langle v,\zeta\rangle_K,
\tag{5}
\]
where a contribution from a zero component is defined to be zero (including when \(1<p<2\)). The analogous formula holds with \(x,y\) interchanged.

If any of \(a,b,c,d\) vanishes and \(J(x)(y)=0\), then \(J(y)(x)=0\) by (5). We may therefore assume all four numbers are positive. From \(J(x)(y)=0\), write
\[
h=|a^{p-2}\langle u,\xi\rangle_H|
=|b^{p-2}\langle v,\zeta\rangle_K|,
\qquad
0\le h\le\min\{a^{p-1}c,b^{p-1}d\}.
\tag{6}
\]
The inequality follows from Hilbert Cauchy–Schwarz. Since the two pairings have opposite signs,
\[
|J(y)(x)|
=h\left|\left(\frac ca\right)^{p-2}-\left(\frac db\right)^{p-2}\right|.
\tag{7}
\]
Set \(\omega=a^p\in(0,1)\),
\[
\tau=\frac{c/a}{d/b}>0,\qquad
\rho=\frac db>0.
\]
The unit-sphere conditions imply \(a^p+b^p=1\) and
\[
1=\omega\tau^p\rho^p+(1-\omega)\rho^p,
\qquad
\rho=\bigl(1+\omega(\tau^p-1)\bigr)^{-1/p}.
\tag{8}
\]
Combining (6)–(8) yields the exact upper envelope
\[
|J(y)(x)|\le
|\tau^{p-2}-1|
\frac{\min\{\omega\tau,1-\omega\}}{
\bigl(1+\omega(\tau^p-1)\bigr)^{(p-1)/p}}.
\tag{9}
\]
For fixed \(\tau>0\), write \(A=\tau^p-1>-1\) and \(q=(p-1)/p\). On
\[
0<\omega\le\omega_*:=\frac{1}{1+\tau},
\]
the derivative of the variable factor in (9) is
\[
\frac{d}{d\omega}\frac{\omega\tau}{(1+\omega A)^q}
=\frac{\tau(1+\omega A/p)}{(1+\omega A)^{q+1}}>0.
\tag{10}
\]
For \(\omega_*\le\omega<1\), its derivative is
\[
\frac{d}{d\omega}\frac{1-\omega}{(1+\omega A)^q}
=-\frac{1+A(p-1+\omega)/p}{(1+\omega A)^{q+1}}<0.
\tag{11}
\]
Indeed, \(A>-1\) and \(0<(p-1+\omega)/p<1\), making the displayed numerators positive. Hence \(\omega_*\) is the **unique** maximizing block mass for every fixed \(\tau\). Substitution in (9) gives
\[
D_p(\tau)=
\frac{\tau^{1/p}|\tau^{p-2}-1|}
{(1+\tau)^{1/p}(1+\tau^{p-1})^{(p-1)/p}}.
\tag{12}
\]

This is a sharp upper bound, not merely a relaxation: for any \(\tau>0\), choose unit \(h_H\in H\) and \(h_K\in K\), put
\[
\omega=\frac1{1+\tau},\quad a=\omega^{1/p},\quad b=(1-\omega)^{1/p},\quad
\rho=(1+\omega(\tau^p-1))^{-1/p},
\]
\[
c=a\tau\rho,\qquad d=b\rho,\qquad
x=(a h_H,b h_K),\quad y=(c h_H,-d h_K).
\tag{13}
\]
The two vectors have unit norm, and
\[
J(x)(y)=\rho(\omega\tau-(1-\omega))=0.
\]
Both Cauchy–Schwarz inequalities in (6) are equalities, giving \(|J(y)(x)|=D_p(\tau)\). Therefore
\[
\sigma_C(Z_p)=\sup_{\tau>0}D_p(\tau)=\sigma_C(\ell_p^2).
\tag{14}
\]
If \(p\ne2\), \(D_p\) is positive for \(\tau\ne1\), vanishes at \(\tau=1\) and tends to zero at \(\tau\downarrow0\) and \(\tau\to\infty\). It therefore attains a positive maximum at finite \(\tau\ne1\). By strictness in (10)–(11), a maximizing pair must have \(\omega=\omega_*\); equality in (6) then forces both Hilbert Cauchy–Schwarz inequalities to be equalities. Hence the two block pairings are collinear, with opposite signs. Conversely, (13) attains equality at every maximizing \(\tau\). Strict convexity of \(Z_p\) implies that \(|J(y)(x)|=1\) can occur only when \(x=\pm y\), which is impossible for a Birkhoff pair; hence the attained maximum is strictly less than one.

Write \(\tau=e^{2z}\). Elementary exponential cancellation transforms (12) to
\[
D_p(e^{2z})=
\frac{|\sinh((p-2)z)|}{
\cosh(z)^{1/p}\cosh((p-1)z)^{(p-1)/p}}.
\tag{15}
\]
Replacing \(z\) by \(-z\) does not change the right-hand side, proving (1). If \(p'=p/(p-1)\), substitute \(z'=(p-1)z\) in (15) for \(p'\). Then
\[
|(p'-2)z'|=|(p-2)z|,
\]
and the two factors in the denominator exchange places, proving (2).

Finally, put \(\delta=|p-2|\). Uniformly for \(z\) in compact subsets of \([0,\infty)\),
\[
\frac{D_p(e^{2z})}{\delta}\longrightarrow \frac{z}{\cosh z}
\quad\text{as }p\to2.
\tag{16}
\]
The maximum does not escape to infinity. For \(7/4\le p\le9/4\), use \(\cosh t\ge e^t/2\) for \(t\ge0\) and \(\sinh(\delta z)/\delta\le z e^{\delta z}\) to obtain
\[
0\le\frac{D_p(e^{2z})}{\delta}
\le 2z\exp\!\left[-\left(\frac{1+(p-1)^2}{p}-\delta\right)z\right]
\le 2z e^{-9z/14}.
\tag{17}
\]
Thus (16) is uniform over \([0,\infty)\). The derivative of \(z/\cosh z\) has the sign of \(1-z\tanh z\), a strictly decreasing function from \(1\) through zero exactly once on \((0,\infty)\). Hence it has the unique maximizer \(z_0\), with \(z_0\tanh z_0=1\). Uniform convergence and the uniform tail bound prove both (3) and convergence of **every choice** of positive maximizing parameters to \(z_0\).

## Verification
The standalone `verify.py` reproduces the scalar maximization for several exponents, the exact sharp witness construction, the derivative signs and the Hölder-conjugacy transformation. It stress-tests noncollinear Hilbert-block directions in finite dimensions against the sharp scalar bound and checks convergence of the normalized defect to the analytic near-Hilbert coefficient. The checker uses only Python's standard library. It is supplementary: the proof above is a continuum argument covering all real Hilbert dimensions.

## Relationship to prior work
Bose's 2023 public preprint *Geometry of \(\ell_p\)-direct sums of normed linear spaces* (arXiv:2309.14252v1, primary MSC 46B20) gives the exact support-functional and Birkhoff–James orthogonality descriptions for such sums (Theorems 9 and 19), followed by a qualitative classification of left- and right-symmetric points (Theorem 25). Its full preprint was inspected through the proof and references; it does not state (1), the rigidity of all extremizers, or the sharp linear expansion (3). Its later 2025 journal publication is not the first-public date.

Chmieliński, Khurana and Sain's 2021 publicly released study *Approximate smoothness in normed linear spaces* (arXiv:2109.11884v1) provides the support-functional product formula for \(\ell_p\)-sums (Proposition 5.1 in its 2023 published version) and characterizes approximate smoothness; it does not calculate the optimal global reverse Birkhoff symmetry defect. Their 2020 publicly released paper *Local Approximate Symmetry of Birkhoff–James Orthogonality in Normed Linear Spaces* introduces the global and local approximate-symmetry framework and studies general qualitative properties, including the polyhedral case.

Chmieliński and Wójcik's 2018 article *Approximate symmetry of Birkhoff orthogonality* introduces a related global geometric constant. Only its abstract and bibliographic information were accessible during this comparison. An unrecognized equivalent formula in that full text remains an explicit residual originality risk.

The exact Dragomir symmetry calculation for the cubic and Hölder-dual planes concerns a different approximate-orthogonality definition, and the earlier \(C\)-approximate cubic-plane value is only a single specialization of (1) and cannot imply the Hilbert-fiber rigidity or near-Hilbert slope. Searches also compared variants phrased in support-functional residuals, hyperbolic ratios, dual exponents and Hilbert-valued direct sums; absence of search results is not proof of absolute novelty.

## Limitations
The theorem is for two nonzero real Hilbert summands with a common exponent \(1<p<\infty\). It does not treat arbitrary Banach summands, three or more blocks, complex scalars, or the nonsmooth exponents \(p=1,\infty\). No full-text comparison with the 2018 global-approximate-symmetry paper was possible. The statement that all maximizing pairs are blockwise collinear applies only when \(p\ne2\); at \(p=2\), all Birkhoff pairs have the zero defect. The numerical tests do not certify infinite-dimensional cases, which follow from the dimension-free analytic proof.

## References
1. B. Bose, *Geometry of \(\ell_p\)-direct sums of normed linear spaces*, arXiv:2309.14252v1, first public 25 September 2023, primary MSC 46B20; later published in *Ann. Univ. Paedagog. Crac. Stud. Math.* 25 (2025), 31–51.
2. J. Chmieliński, D. Khurana, D. Sain, *Approximate smoothness in normed linear spaces*, arXiv:2109.11884v1, first public 24 September 2021; *Banach J. Math. Anal.* 17 (2023), article 41; doi:10.1007/s43037-023-00263-4.
3. J. Chmieliński, D. Khurana, D. Sain, *Local Approximate Symmetry of Birkhoff–James Orthogonality in Normed Linear Spaces*, arXiv:2012.08162v1, first public 15 December 2020; *Results Math.* 76 (2021), article 136; doi:10.1007/s00025-021-01437-y.
4. J. Chmieliński, P. Wójcik, *Approximate symmetry of Birkhoff orthogonality*, *J. Math. Anal. Appl.* 461 (2018), 625–640; doi:10.1016/j.jmaa.2018.01.031.
5. J. Chmieliński, T. Stypuła, P. Wójcik, *Approximate orthogonality in normed spaces and its applications*, *Linear Algebra Appl.* 531 (2017), 305–317; doi:10.1016/j.laa.2017.06.001.
