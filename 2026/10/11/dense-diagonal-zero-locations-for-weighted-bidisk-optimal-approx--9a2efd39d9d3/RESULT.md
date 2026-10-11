# Dense diagonal zero locations for weighted bidisk optimal approximants

## Finding

For each real \(\alpha>0\), let \(\mathcal D_\alpha(\mathbb D^2)\) have coefficient norm
\[
\|F\|_\alpha^2=\sum_{j,k\ge0}|F_{jk}|^2(j+1)^\alpha(k+1)^\alpha,
\qquad F(z,w)=\sum_{j,k\ge0}F_{jk}z^jw^k.
\]
The inner product is linear in its first argument. For a nonzero polynomial \(f\), the *linear optimal polynomial approximant* is the unique affine polynomial \(p\) minimizing \(\|1-pf\|_\alpha\).

**Theorem.** Given any \(\alpha>0\), \(\zeta\in\mathbb D\), and \(\varepsilon>0\), there is a symmetric polynomial \(f\) satisfying \(f(0,0)=1\) and \(f(z,w)\ne0\) whenever \(|z|\le1\), \(|w|\le1\), whose linear optimal polynomial approximant has a zero \((t,t)\in\mathbb D^2\) with \(|t-\zeta|<\varepsilon\). In particular, the possible diagonal zero coordinates are dense in the whole open disk, even with both symmetry and closed-bidisk zero-freeness imposed on \(f\).

## Assumptions and scope

The approximation space consists of all polynomials in \(z,w\) of total degree at most one; no coefficient bound or prescribed degree for \(f\) is asserted. The theorem concerns positive Dirichlet parameter \(\alpha>0\), not the bidisk Hardy case \(\alpha=0\). The parameter \(\zeta\) is a target coordinate, not a zero of the original polynomial. We give an explicit two-limit construction for every nonzero target; approximation to the origin follows by approaching it through nonzero targets.

## Proof

**1. The exact diagonal-zero formula.** Put \(M=z+w\). If \(f\) is symmetric, uniqueness of orthogonal projection implies that its linear approximant is \(p=A+BM\). Assume \(f(0,0)=1\). With \(G_0=\|f\|_\alpha^2\), \(G_1=\langle f,Mf\rangle_\alpha\), and \(G_2=\|Mf\|_\alpha^2\), orthogonality of \(1-pf\) to \(f\) and \(Mf\) gives
\[
A G_0+B\overline{G_1}=1,\qquad A G_1+B G_2=0,
\]
because \(\langle1,f\rangle_\alpha=1\) and \(\langle1,Mf\rangle_\alpha=0\). The Gram determinant \(\Delta=G_0G_2-|G_1|^2\) is strictly positive: \(f\) has constant coefficient one but \(Mf\) has constant coefficient zero, so they are linearly independent. Therefore
\[
A=G_2/\Delta\ne0,\qquad B=-G_1/\Delta.
\]
Whenever \(G_1\ne0\), the diagonal zero coordinate is exactly
\[
t(f)=\frac{G_2}{2G_1}=\frac{\|Mf\|_\alpha^2}{2\langle f,Mf\rangle_\alpha}.
\]

**2. A two-point concentrating block.** Fix \(0<|\zeta|<1\). Select distinct unimodular numbers \(a,b\) with \(a+b=2\zeta\). One choice is
\[
a=e^{i(\arg\zeta+\arccos|\zeta|)},\qquad
b=e^{i(\arg\zeta-\arccos|\zeta|)}.
\]
For integers \(m\ge1\) set
\[
K_{m,a}(z)=\sum_{j=0}^m\overline a^{\,j}z^j,\quad
U_m(z,w)=K_{m,a}(z)K_{m,b}(w),\quad
h_m(z,w)=U_m(z,w)+U_m(w,z).
\]
The polynomial \(h_m\) is symmetric and obeys \(\|h_m\|_{L^\infty(\overline{\mathbb D}^2)}\le 2(m+1)^2\).

Write \(L=m+1\), \(s=a+b=2\zeta\). A direct comparison of monomial coefficients in the Hardy inner product gives
\[
\langle U_m,MU_m\rangle_0=mL\overline{s},\qquad
\|MU_m\|_0^2=2L^2+2m^2\operatorname{Re}(a\overline b)
=L^2|s|^2+O(L).
\]
The same identities hold with the two variables interchanged. Every cross term between \(U_m\) and \(U_m(w,z)\), with either argument multiplied by \(M\), is bounded independently of \(m\): coefficients factor into products of geometric sums of powers of \(a\overline b\), and \(a\ne b\) makes each such sum uniformly bounded. Thus
\[
\langle h_m,Mh_m\rangle_0=2mL\overline{s}+O(1),\qquad
\|Mh_m\|_0^2=2L^2|s|^2+O(L).
\]
Since \(s\ne0\), the first expression does not vanish for all sufficiently large \(m\), and
\[
r_m:=\frac{\|Mh_m\|_0^2}{2\langle h_m,Mh_m\rangle_0}\longrightarrow
\frac{|s|^2}{2\overline s}=\frac{s}{2}=\zeta.
\]
The implicit constants in these elementary finite-sum estimates may depend on the fixed pair \(a,b\), which is harmless because the target is fixed before taking \(m\to\infty\).

**3. Zero-free lift into positive Dirichlet weight.** For fixed \(m\), choose
\[
\lambda_m=\frac1{4(m+1)^2},\qquad
f_{m,N}(z,w)=1+\lambda_m(zw)^Nh_m(z,w),\qquad N\ge2.
\]
On the entire closed bidisk,
\[
|f_{m,N}-1|\le\lambda_m\,2(m+1)^2=\frac12,
\]
so these are zero-free symmetric polynomials with constant coefficient one.

Let \(q_{m,N}=(zw)^Nh_m\). Their monomial supports are disjoint from those of \(1\) and \(M\). Hence the coefficient orthogonality is exact:
\[
\langle f_{m,N},Mf_{m,N}\rangle_\alpha
=\lambda_m^2\langle q_{m,N},Mq_{m,N}\rangle_\alpha,
\]
\[
\|Mf_{m,N}\|_\alpha^2
=2^{\alpha+1}+\lambda_m^2\|Mq_{m,N}\|_\alpha^2.
\]
For any fixed polynomial \(h\) and its shift \(q_N=(zw)^Nh\), each coefficient weight, divided by \(N^{2\alpha}\), tends to one. Because the relevant sums are finite,
\[
N^{-2\alpha}\langle q_N,Mq_N\rangle_\alpha\to\langle h,Mh\rangle_0,
\qquad N^{-2\alpha}\|Mq_N\|_\alpha^2\to\|Mh\|_0^2.
\]
The constant term \(2^{\alpha+1}\) vanishes after division by \(N^{2\alpha}\), precisely because \(\alpha>0\). The exact zero formula in Step 1 therefore gives, for each sufficiently large fixed \(m\),
\[
\lim_{N\to\infty}t(f_{m,N})=r_m.
\]
Combining the two limits, set \(\delta=\min\{\varepsilon/3,(1-|\zeta|)/3\}>0\). First choose \(m\) so that \(|r_m-\zeta|<\delta\), then choose \(N\) so that \(|t(f_{m,N})-r_m|<\delta\). Consequently \(|t(f_{m,N})-\zeta|<2\delta<\varepsilon\) and \(|t(f_{m,N})|\le |\zeta|+2\delta<1\). This proves the assertion for \(\zeta\ne0\). For \(\zeta=0\), take any nonzero target in \(\mathbb D\) of modulus smaller than \(\varepsilon/3\), and apply the already proved case with tolerance smaller than \(\varepsilon/3\).

## Verification

All key steps are exact finite coefficient identities and finite geometric-sum bounds. The accompanying standalone `check_moments.py` computes the coefficient moments of \(h_m\) and of the weighted high-degree lifts directly for several nonreal targets and positive weights, directly testing the norm, inner-product and OPA-zero formula. The script is corroborative only: the all-parameter limit and the density statement follow from the proof above, not from a finite experiment. Run `python check_moments.py` using Python's standard library.

## Relationship to prior work

Navío and Seco (arXiv:2609.37180v1, first posted 2026-09-29) prove existence, for each positive Dirichlet parameter, of a zero-free symmetric polynomial whose linear optimal approximant has an interior zero. Their explicit shifted block yields diagonal zeros approaching one fixed point, \((-11/12,-11/12)\); they separately discuss a Hardy-space question about zeros arbitrarily close to the origin, which the present positive-weight result does not resolve. Their high-degree transfer principle and exact projection formulas are used here as background, but their existence theorem and fixed-block construction do not imply arbitrary diagonal zero location. The present two-point Fejér concentration family varies its Hardy block with the target to establish density.

Bénéteau, Khavinson and Seco (arXiv:2405.16943v1) give the earlier Hardy bidisk counterexample; Geronimo and Woerdeman (arXiv:2508.15938v1) optimize a restricted Hardy family. The stated density theorem is for \(\alpha>0\) only, and makes no claim concerning optimal localization in the Hardy case.

## Limitations

The polynomial degree can grow very rapidly as the accuracy and target vary; no uniform effective degree bound is claimed. Density does not assert exact attainment of every target. The original Hardy-space question at \(\alpha=0\), including localization near the origin, is not addressed. The claim is about diagonal zeros of degree-one approximants only, not the full zero set of approximants of every degree. A related result could exist outside the primary works inspected.

## References

1. O. Navío and D. Seco, *Polynomial Counterexamples to Shanks' Conjecture in Dirichlet-Type Spaces over the Bidisc*, arXiv:2609.37180v1 (initial release 2026-09-29), especially Sections 1–3.
2. C. Bénéteau, D. Khavinson and D. Seco, *A Counterexample to the Weak Shanks Conjecture*, arXiv:2405.16943v1 (2024-05-27); later in *Constructive Approximation* 62 (2025).
3. J. S. Geronimo and H. J. Woerdeman, *A Fourier Analysis Approach to Disprove the Weak Shanks Conjecture*, arXiv:2508.15938v1 (2025-08-21); later *Proceedings of the American Mathematical Society*.
