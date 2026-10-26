# The four-to-five-state defect transition and stable pentagon rigidity

## Finding

Let \(\mu\) be a probability law on exactly \(m\) distinct points of \(\mathbb R^2\), all of positive mass, satisfying
\[
\mathbb E\xi=0,\qquad \mathbb E\xi\xi^{\mathsf T}=I_2,\qquad \mathbb E\xi^{\otimes3}=0.
\]
For a real symmetric trace-zero \(2\times2\) matrix \(A\), define the quadratic orthogonal-representation defect
\[
\Gamma_\mu(A)=\frac14\mathbb E(\xi^{\mathsf T}A\xi)^2,\qquad
\Lambda(\mu)=\sup_{\operatorname{tr} A=0,\,\|A\|_F=1}\Gamma_\mu(A).
\]
The following support-constrained conclusions hold.

**Exact support frontier.** There is no such law with \(m\le3\). Every four-point law is, after an orthogonal change of coordinates and relabeling, exactly
\[
\Pr\{\xi=\pm p^{-1/2}e_1\}=p/2\ \text{at each sign},\qquad
\Pr\{\xi=\pm(1-p)^{-1/2}e_2\}=(1-p)/2\ \text{at each sign},
\quad 0<p<1.
\]
For this family \(\Lambda(\mu)=1/[8p(1-p)]\). Therefore the sharp minimum over laws on exactly \(m\) atoms is
\[
\inf\Lambda(\mu)=
\begin{cases}
1/2,&m=4,\\
1/4,&m\ge5.
\end{cases}
\]
At \(m=4\) equality occurs only for \(p=1/2\). At \(m=5\), equality occurs only for the uniform regular pentagon of radius \(\sqrt2\), up to orthogonal transformations; all regular \(m\)-gons of radius \(\sqrt2\), with uniform weights, attain \(1/4\) when \(m\ge5\).

**Quantitative five-state rigidity.** If \(m=5\) and
\[
0\le\Lambda(\mu)-1/4\le\varepsilon\le10^{-8},
\]
then there are a rotation angle \(\theta\) and a relabeling \(j=0,\dots,4\) of the atoms and weights such that, writing \(u(\phi)=(\cos\phi,\sin\phi)\),
\[
\left|\Pr\{\xi=x_j\}-\frac15\right|\le6\sqrt\varepsilon,
\qquad
\bigl\|x_j-\sqrt2\,u(\theta+2\pi j/5)\bigr\|_2\le440\sqrt\varepsilon
\]
for each \(j\). The displayed constants are explicit safe bounds, not claims of optimality.

## Assumptions and scope

The support count \(m\) refers to *distinct* atoms, with strictly positive weights; zero weights do not count. The laws are bounded because their support is finite. The Frobenius norm and matrix trace use the standard Euclidean normalization. The defect is the trace-free quadratic Galtchouk–Kunita–Watanabe residual for centered, isotropic, third-moment-free increments; no assertion is made about the full BSDE error or its optimal discretization. The near-extremizer theorem concerns exactly five atoms and does not claim the same coordinatewise stability for arbitrary larger supports.

## Proof

**1. Three or fewer states cannot match the moments.** In \(L^2(\mu)\), the three functions \(1,\xi_1,\xi_2\) are orthonormal by centering and covariance normalization. Thus \(m\ge3\). If \(m=3\), these already form a basis. Third-moment cancellation makes every centered quadratic \(\xi_i\xi_j-\delta_{ij}\) perpendicular to that basis. It must therefore vanish at each support point, implying \(\xi\xi^{\mathsf T}=I_2\) there. This contradicts the rank-one property of an outer product of a vector in \(\mathbb R^2\). Hence \(m\ge4\).

**2. Classification of all four-state rules.** With \(m=4\), the orthogonal complement of \(\operatorname{span}\{1,\xi_1,\xi_2\}\) in \(L^2(\mu)\) has dimension one. Choose a nonconstant real function \(h\) spanning it. Every centered quadratic lies in that complement, so for one fixed real symmetric matrix \(B\), pointwise on the four atoms,
\[
\xi\xi^{\mathsf T}=I_2+hB.
\]
The matrix \(B\) cannot vanish because \(\xi\xi^{\mathsf T}\) has rank at most one, while \(I_2\) has rank two. Since every support value of \(h\) is a zero of the nonzero polynomial \(t\mapsto\det(I_2+tB)\), there are at most two distinct values of \(h\). There cannot be only one since \(h\) is nonconstant. The two associated matrices are nonzero rank-one positive semidefinite matrices: if one were zero, the other alone could not average to covariance \(I_2\).

Thus the four positions lie on exactly two distinct lines through the origin. Their weighted means along these independent lines must both vanish. Each line must consequently carry at least two points; since there are four total, each carries exactly one antipodal pair, with equal within-pair masses. Write the total pair masses as \(p\) and \(q=1-p\) and the nonzero vectors as \(u,v\). Isotropy gives \(puu^{\mathsf T}+qvv^{\mathsf T}=I_2\); the square matrix with columns \(\sqrt p\,u,\sqrt q\,v\) is orthogonal, proving the displayed family. Conversely it clearly satisfies all required moments.

**3. Exact four-state defect.** The trace-free Frobenius-orthonormal basis
\[
A_1=2^{-1/2}\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
A_2=2^{-1/2}\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]
puts the defect matrix into the diagonal form
\[
\bigl[\Gamma_\mu(A_i,A_j)\bigr]_{i,j=1}^2
=\begin{pmatrix}1/[8p(1-p)]&0\\0&0\end{pmatrix},
\]
where \(\Gamma_\mu(A,B)=\frac14\mathbb E[(\xi^{\mathsf T}A\xi)(\xi^{\mathsf T}B\xi)]\). Its largest eigenvalue is \(1/[8p(1-p)]\ge1/2\), with equality precisely at \(p=1/2\).

**4. Universal bound, attainability, and exact five-state equality.** For any supported law meeting the assumptions, the displayed basis gives the pointwise identity
\[
\sum_{i=1}^2(\xi^{\mathsf T}A_i\xi)^2=\frac12|\xi|^4.
\]
Hence the trace of the defect matrix is \(\mathbb E|\xi|^4/8\ge1/2\) by \(\mathbb E|\xi|^2=2\) and Jensen, and its largest eigenvalue is at least \(1/4\). For the uniform regular \(m\)-gon \(\xi_j=\sqrt2\,u(2\pi j/m)\) with \(m\ge5\), angular Fourier moments of orders one through four vanish. This proves the moment conditions and the defect matrix equals \(I_2/4\).

If a five-atom law has defect \(1/4\), the preceding inequalities force \(|\xi|^2=2\) on all atoms and force its two-dimensional defect matrix to equal \(I_2/4\). Writing \(z_j=(\xi_{j,1}+i\xi_{j,2})/\sqrt2\) on the unit circle, the initial moment assumptions say \(\sum_jw_jz_j^k=0\) for \(k=1,2,3\); the equality of the two defect eigenvalues and vanishing cross term give the same identity for \(k=4\). Form the square matrix \(V_{kj}=\sqrt{w_j}z_j^k\), \(0\le k,j\le4\). The four Fourier equations and total mass one imply \(VV^*=I_5\); hence also \(V^*V=I_5\). Its diagonal says \(w_j=1/5\). Its off-diagonal says \(\sum_{k=0}^4(z_j/z_i)^k=0\) for \(i\ne j\), so the five ratios are precisely the nontrivial fifth roots of unity. The nodes are therefore a regular pentagon, up to rotation and reflection.

**5. Quantitative five-state rigidity.** Fix \(m=5\) and \(0\le\Lambda-1/4\le\varepsilon\le10^{-8}\). Define \(s=|\xi|^2/2\). The trace identity and the upper bound on both defect eigenvalues give
\[
\mathbb E(s-1)^2=\mathbb E s^2-1\le4\varepsilon.
\]
Let \(K\) be the defect matrix in the preceding basis. Its trace is at least \(1/2\), while its largest eigenvalue is at most \(1/4+\varepsilon\). Thus its smallest eigenvalue is at least \(1/4-\varepsilon\) and
\[
\|K-I_2/4\|_{\mathrm{op}}\le\varepsilon.
\]
At each atom choose a unit complex number \(z\) in the direction of \(\xi\), arbitrary if the atom is zero, and set \(t=\sqrt s\). Write \(m_k=\mathbb Ez^k\). The exact moment conditions are \(\mathbb Et^kz^k=0\) for \(k=1,2,3\). Cauchy–Schwarz and \(\mathbb E(s-1)^2\le4\varepsilon\) yield
\[
|m_1|,|m_2|\le2\sqrt\varepsilon,\qquad |m_3|\le6\sqrt\varepsilon.
\]
For the cubic bound, use \(|s^{3/2}-1|\le\frac32|s-1|(1+\sqrt s)\) and \(\mathbb E(1+\sqrt s)^2\le4\). The identity
\[
\mathbb E(\xi_1+i\xi_2)^4=8(K_{11}-K_{22})+16iK_{12}
\]
gives \(|\mathbb Es^2z^4|\le8\varepsilon\); moreover
\[
\mathbb E|s^2-1|\le
\bigl(\mathbb E(s-1)^2\mathbb E(s+1)^2\bigr)^{1/2}
\le5\sqrt\varepsilon.
\]
Thus \(|m_4|\le8\varepsilon+5\sqrt\varepsilon\le6\sqrt\varepsilon\). In particular \(|m_k|\le7\sqrt\varepsilon\) for \(1\le k\le4\).

For the five distinct atoms write \(w_j>0\) and define \(V_{kj}=\sqrt{w_j}z_j^k\), \(0\le k,j\le4\). The off-diagonal entries of \(VV^*-I_5\) are angular moments \(m_{|k-\ell|}\), so its operator norm is at most \(28\sqrt\varepsilon\). This is below one, so \(V\) is invertible. Since \(VV^*\) and \(V^*V\) have the same eigenvalues, also
\[
\|V^*V-I_5\|_{\mathrm{op}}\le28\sqrt\varepsilon.
\]
The diagonal entries give \(|5w_j-1|\le28\sqrt\varepsilon\) and \(w_j\ge0.19\). Off-diagonal entries give, for \(i\ne j\),
\[
\left|\sum_{k=0}^4(z_j/z_i)^k\right|\le150\sqrt\varepsilon,
\quad\text{hence}\quad |(z_j/z_i)^5-1|\le300\sqrt\varepsilon.
\]
Every unit-circle ratio is therefore within \(300\sqrt\varepsilon\) of one of the fifth roots of unity. To see this, choose the nearest fifth root, write its angular separation as at most \(\pi/5\), and use \(\sin(5x)\ge\sin x\) for \(0\le x\le\pi/10\). Relative to the first node, two distinct nodes cannot be assigned the same fifth root: otherwise their ratio is within \(600\sqrt\varepsilon\) of one, implying by \(|\sum_{k=0}^4w^k-5|\le10|w-1|\) that its five-term geometric sum has magnitude at least \(4.4\), contradicting the bound \(150\sqrt\varepsilon\le0.015\). Thus the assignments use all five fifth roots.

Finally, for each \(j\), the nonnegative weighted sum \(\sum_j w_j(s_j-1)^2\le4\varepsilon\) and \(w_j\ge0.19\) give \(|s_j-1|\le5\sqrt\varepsilon\). Since \(|\sqrt{s_j}-1|\le|s_j-1|\), the angular bound yields
\[
\|\xi_j-\sqrt2\,u(\theta+2\pi j/5)\|_2
\le\sqrt2(5+300)\sqrt\varepsilon<440\sqrt\varepsilon,
\]
while the diagonal bound gives \(|w_j-1/5|\le(28/5)\sqrt\varepsilon<6\sqrt\varepsilon\). This proves the quantitative assertion.

## Verification

The standalone standard-library program `verify.py` checks 49 exact rational four-point laws (all moments through degree three, the defect eigenvalue and its lower bound), 25 regular polygon designs (harmonics through degree four and the two-by-two defect matrix), and 200 reproducible near-pentagon Vandermonde perturbations. It produces `PASS 3762 finite exact/numerical assertions` in the present run. These finite tests do not certify the all-laws classification, support optimum, or perturbation theorem; those are established by the proofs above.

## Relationship to prior work

Tanaka, *Third-moment cancellation and predictable representation in finite-state BSDE approximation* (arXiv:2610.20880v1, 14 October 2026), defines the quadratic GKW defect, proves the support-unrestricted operator bound \(1/4\) in dimension two, and characterizes equality by weighted spherical 4-designs. Section 10 specifically asks about the support-size versus defect tradeoff. The same paper mentions the four-point equal-weight coordinate-axis rule and the six-point symmetric simplex, but does not determine the exact four-to-five-state frontier or a coordinatewise quantitative near-optimality estimate. The universal bound and extremal-design criterion are credited to it, not claimed anew.

Classical cubature theory already supplies general lower bounds and symmetry of minimal degree-three rules. In particular, Cools's 1997 survey, Section 8.3, reports Möller's theorem that a rule attaining the symmetric degree-three lower bound is centrally symmetric. Therefore the antipodal aspect of the four-point classification should not be regarded as independently novel. Here it is used to evaluate and compare the precise defect, while the explicit five-point \(\sqrt\varepsilon\)-stability assertion controls *both* nodes and unequal weights from the excess martingale defect. General stability theorems for minimal positive quadratures, if available, might subsume that assertion after a nontrivial specialization.

## Limitations

The quantitative constants \(10^{-8},6,440\) are sufficient but not optimized, and no sharpness claim is made for the square-root exponent. The stability result concerns exactly five positive atoms; no separation-free atomwise control is asserted for larger support. The claims concern only planar trace-free quadratic residuals, not arbitrary Hessian sectors, full higher-dimensional schemes, or convergence rates. Novelty beyond the classical design/cubature theory requires independent priority assessment; the paper's unpublished companion manuscript was not accessible for full-text comparison. Numerical checks cannot establish universal quantifiers.

## References

1. A. Tanaka, *Third-moment cancellation and predictable representation in finite-state BSDE approximation*, arXiv:2610.20880v1, first posted 14 October 2026, Sections 2, 6 and 10. https://arxiv.org/html/2610.20880v1
2. R. Cools, *Constructing cubature formulae: the science behind the art*, Acta Numerica **6** (1997), 1–54, especially Sections 7–8. https://doi.org/10.1017/S0962492900002701
3. H. M. Möller, bounds for minimal centrally symmetric odd-degree cubature formulae (1973), as cited and discussed in Cools, Section 8.3.
