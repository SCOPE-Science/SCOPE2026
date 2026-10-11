# Sharp boundedness and conditioning of simultaneous Williamson forms for aligned multiplier pairs

## Finding

Let \((\Omega,\mu)\) be a nonzero \(\sigma\)-finite measure space. On \(H=L^2(\Omega;\mathbb R)\), let \(p,q\) be finite, strictly positive measurable functions and let \(a,b\) be finite, nonnegative measurable functions. Assume \(c=a+b>0\) almost everywhere and that all four functions \(ap,aq,bp,bq\) belong to \(L^\infty(\Omega)\). Set
\[
J=\begin{pmatrix}0&I\\-I&0\end{pmatrix},\qquad
A=\begin{pmatrix}M_{ap}&0\\0&M_{aq}\end{pmatrix},\qquad
B=\begin{pmatrix}M_{bp}&0\\0&M_{bq}\end{pmatrix}
\]
on \(H\oplus H\). Here \(M_f\) means multiplication by \(f\). These bounded nonnegative operators satisfy \(AJB=BJA\), hence their Hamiltonians commute.

Consider **all** bounded invertible real-linear symplectic operators \(S\) satisfying \(S^*JS=J\) for which there exist bounded nonnegative selfadjoint operators \(D_A,D_B\) on \(H\) such that
\[
A=S^*(D_A\oplus D_A)S,\qquad B=S^*(D_B\oplus D_B)S.
\]
In particular, the target operators need **not** be multiplication operators and the normalizer may mix spectral fibers. Put
\[
R=\operatorname*{ess\,sup}_{\omega\in\Omega}
\max\left\{\frac{p(\omega)}{q(\omega)},\frac{q(\omega)}{p(\omega)}\right\}\in[1,\infty].
\]
The set of these simultaneous Williamson normalizers is nonempty precisely when \(R<\infty\), and its sharp distortion is
\[
\boxed{\min_S\|S\|\,\|S^{-1}\|=\sqrt R.}
\]
When \(R=\infty\), no bounded invertible simultaneous normalizer exists, despite the boundedness and injectivity of \(A+B\). The sharp quantity depends only on relative stiffness \(p/q\), not on the partition of energy between \(a\) and \(b\).

## Assumptions and scope

All equalities and inequalities between measurable functions hold almost everywhere. The space can have atoms or a continuous measure component. Neither \(A\), \(B\), nor their sum is required to have a bounded inverse. The multiplication symbols are finite almost everywhere and the four products assumed above are essentially bounded. Positivity means positive semidefinite. Since \(c,p,q>0\) almost everywhere, \(C=A+B\) is injective but need not be bounded below. We optimize the ordinary Hilbert-space operator-norm condition number among **all** bounded symplectic normalizers of the indicated form, not among only diagonal ones.

## Proof

**1. Simultaneous algebra and an attaining construction.** Because scalar multipliers commute, directly multiplying the block matrices gives
\[
AJB=BJA=\begin{pmatrix}0&M_{abpq}\\-M_{abpq}&0\end{pmatrix}.
\]
If \(R<\infty\), the functions \(s=(p/q)^{1/4}\) and \(s^{-1}=(q/p)^{1/4}\) belong to \(L^\infty\). Define \(S=M_s\oplus M_{s^{-1}}\); it is boundedly invertible and \(S^*JS=J\). Let \(D_A=M_{a\sqrt{pq}}\), \(D_B=M_{b\sqrt{pq}}\). These are bounded because \(a\sqrt{pq}=\sqrt{(ap)(aq)}\) and likewise for \(b\). Direct multiplication yields
\[
S^*(D_A\oplus D_A)S=A,\qquad
S^*(D_B\oplus D_B)S=B.
\]
The two operator norms of \(S\) and \(S^{-1}\) both equal \(R^{1/4}\), so \(\|S\|\|S^{-1}\|=\sqrt R\).

**2. A bound applying to every normalizer.** Suppose an arbitrary bounded symplectic \(S\) has the stated congruence representations. Write \(D=D_A+D_B\ge0\), \(\mathcal D=D\oplus D\), \(C=A+B=S^*\mathcal D S\), and \(T=JC\). From \(S^*JS=J\) and \(J^{-1}=-J\), one has \(JS^*=S^{-1}J\). Thus
\[
T=S^{-1}J\mathcal D S,\qquad
-T^2=S^{-1}\mathcal D^2 S.
\]
For each \(\varepsilon>0\), the functional calculus (equivalently, polynomial approximation of the continuous function \(u\mapsto(u+\varepsilon)^{-1/2}\) on the bounded positive spectrum) gives
\[
K_\varepsilon:=T(-T^2+\varepsilon I)^{-1/2}
=S^{-1}\bigl(J\mathcal D(\mathcal D^2+\varepsilon I)^{-1/2}\bigr)S.
\]
Since \(J\) is an isometry and commutes with \(\mathcal D\), the middle factor is a contraction. Consequently
\[
\|K_\varepsilon\|\le\|S^{-1}\|\,\|S\|\qquad(\varepsilon>0).
\]
Importantly, this argument permits repeated symplectic spectral values and mixing of spectral fibers: no spectral simplicity or finite-dimensional truncation is assumed.

**3. Computing the invariant and taking the noncoercive limit.** Independently of any putative normalizer, multiplication algebra gives
\[
T=\begin{pmatrix}0&M_{cq}\\-M_{cp}&0\end{pmatrix},\qquad
-T^2=\begin{pmatrix}M_{c^2pq}&0\\0&M_{c^2pq}\end{pmatrix}.
\]
Therefore
\[
K_\varepsilon=
\begin{pmatrix}
0&M_{cq/\sqrt{c^2pq+\varepsilon}}\\
-M_{cp/\sqrt{c^2pq+\varepsilon}}&0
\end{pmatrix}
\]
and the Hilbert-space multiplier norm is exactly
\[
\|K_\varepsilon\|=
\operatorname*{ess\,sup}_{\omega}
\frac{\max\{c(\omega)p(\omega),c(\omega)q(\omega)\}}
{\sqrt{c(\omega)^2p(\omega)q(\omega)+\varepsilon}}.
\]
As \(\varepsilon\downarrow0\), the nonnegative integrand increases pointwise to \(\max\{\sqrt{p/q},\sqrt{q/p}\}\); here positivity of \(c,p,q\) prevents any vanishing-denominator ambiguity in the limit. Monotone convergence of essential suprema (via the positive-measure level sets of the limiting function) now yields
\[
\lim_{\varepsilon\downarrow0}\|K_\varepsilon\|=\sqrt R,
\]
including the value \(+\infty\). The preceding contraction estimate forces \(\|S\|\|S^{-1}\|\ge\sqrt R\) for **every** bounded normalizer. Together with Step 1, this proves both necessity and sharp attainment.

**4. Explicit noncoercive boundary.** Take \(\Omega=(0,1)\) with Lebesgue measure, \(p(t)=1\), \(q(t)=t^2\), \(a(t)=t\), and \(b(t)=1-t\). Then \(A,B\) are bounded positive injective operators, \(AJB=BJA\), and \(C=M_1\oplus M_{t^2}\) is injective but not bounded below. Since \(R=\operatorname*{ess\,sup}_{0<t<1}t^{-2}=\infty\), Step 3 prohibits every bounded simultaneous Williamson normalizer, including ones that globally mix the continuous spectral fibers. The explicit formal squeeze uses \(s(t)=t^{-1/2}\), which indeed fails to be a bounded operator on \(L^2(0,1)\).

## Verification

The algebraic identities can be checked in each two-dimensional symplectic fiber. The accompanying standard-library script checks the symplectic identity, both congruence identities, and exact norm formulas for a finite, nonuniform example with one vanished \(a\)-coefficient. This is a finite sanity check only: the infinite-dimensional statement follows from the analytical lower bound and monotone essential-supremum argument above, **not** from computations.

## Relationship to prior work

Kamat and Tonny, arXiv:2610.04583v1 (2026), Theorems 2.3 and 3.1, produce a simultaneous Williamson representation for bounded positive symplectically commuting operators with a generally unbounded transformation. Their operator may act on a dense domain; the paper does not give a necessary-and-sufficient criterion for a bounded symplectic normalizer or its globally optimal operator-norm condition number in this multiplier class. This result computes both for *aligned multiplier pairs* and quantifies a genuinely noncoercive obstruction.

Bhat and John, arXiv:1804.03921v3 (2019), Theorem 4.3 and Corollary 4.4, establish a bounded symplectic normal form for **strictly positive invertible** infinite-dimensional operators. That hypothesis excludes the noncoercive examples here. Babu and Mishra's open-access 2024 article concerns stability and orthosymplectic ambiguity of *finite-dimensional positive-definite* Williamson diagonalizers. It does not address the infinite-dimensional existence boundary or the multiplier-field essential supremum. The finite-dimensional diagonal-scaling observation is classical in spirit; the contribution asserted here is the sharp all-normalizer infinite-dimensional criterion, including noncoercive continuous spectra.

## Limitations

The result is confined to the aligned multiplication-operator class; it does **not** characterize bounded simultaneous Williamson representations of arbitrary symplectically commuting positive operators. It assumes strict positivity almost everywhere of \(p,q,a+b\); if there is a joint kernel of positive measure the ratio must instead be restricted to the active component. No estimates of numerical perturbations, implementability on Fock spaces, Schatten properties, or unbounded-domain extensions are claimed. Novelty comparisons are based on inspected sources, not on a proof that no equivalent older result exists; a general hidden bounded-symplectic-similarity criterion remains a literature risk. Independent validation has not occurred.

## References

1. R. Kamat and A. Tonny, *Simultaneous Williamson's normal form for positive operators*, arXiv:2610.04583v1, first publicly posted 2026-10-03, Theorems 2.3 and 3.1, Sections 4 and 6.
2. B. V. R. Bhat and T. C. John, *Real Normal Operators and Williamson's Normal Form*, arXiv:1804.03921v3, 2019, Theorem 4.3 and Corollary 4.4.
3. G. Babu and H. K. Mishra, *Block perturbation of symplectic matrices in Williamson's theorem*, Canadian Mathematical Bulletin 67 (2024), 201--214, doi:10.4153/S0008439523000620; open-access full text.
4. M. Idel, S. Soto Gaona and M. M. Wolf, *Perturbation bounds for Williamson's symplectic normal form*, Linear Algebra and its Applications 525 (2017), 45--58, doi:10.1016/j.laa.2017.03.013 (background perturbation literature; abstract-level comparison only).
