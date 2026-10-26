# Sharp negative-type exponent for the icosahedral rotation-angle metric

## Finding

Let \(I\le SO(3)\) be the group of \(60\) orientation-preserving symmetries of a regular icosahedron, and write \(\vartheta(g)\in[0,\pi]\) for the principal rotation angle of \(g\). Define \(d(g,h)=\vartheta(g^{-1}h)\). For every exponent \(s>0\), set \(D_s=[d(g,h)^s]_{g,h\in I}\) and, for every \(t>0\), set \(K_{s,t}=[\exp(-t\,d(g,h)^s)]_{g,h\in I}\).

Put
\[
s_* = \frac{\log(4/3)}{\log(3/2)}=0.7095112913514545\ldots.
\]
The following assertions are equivalent:

1. \(0<s\le s_*\).
2. \(D_s\) is conditionally negative semidefinite on the subspace \(\{c\in\mathbb C^{60}:\sum_{g\in I}c_g=0\}\).
3. \(K_{s,t}\) is positive semidefinite for **every** \(t>0\).

In fact, whenever they hold, \(K_{s,t}\) is **strictly positive definite** for every \(t>0\). For \(s>s_*\), there exists \(t_0(s)>0\) for which \(K_{s,t}\) is not positive semidefinite for any \(0<t<t_0(s)\). At \(s=s_*\), the centered matrix \(-\tfrac12 H D_s H\), where \(H=I_{60}-\mathbf1\mathbf1^{\mathsf T}/60\), has rank **\(34\)** and a \(25\)-dimensional kernel within \(\mathbf1^\perp\); for \(0<s<s_*\) its rank is \(59\). Thus \((I,d^{s_*/2})\) has an injective Euclidean realization of minimal dimension \(34\), whereas the subcritical powered metrics require dimension \(59\).

## Assumptions and scope

The metric is the **intrinsic rotation-angle distance restricted to the finite group** \(I\), not the chordal Frobenius distance and not the full manifold \(SO(3)\). Angles are in radians; uniform rescaling has no effect on the cutoff. Positive semidefinite kernels mean nonnegative quadratic forms for all complex coefficients on the full \(60\)-point set. Conditional negative semidefiniteness means \(\sum_{g,h}\overline{c_g}c_h d(g,h)^s\le0\) whenever \(\sum_g c_g=0\). Strict positive definiteness of \(K\) refers to positivity for every nonzero vector in \(\mathbb C^{60}\).

## Proof

**1. Rotation classes and Fourier decomposition.** The group \(I\cong A_5\) has conjugacy classes of sizes \(1,15,20,12,12\), at angles \(0,\pi,2\pi/3,2\pi/5,4\pi/5\). Its irreducible complex representations have dimensions \(1,3,3,4,5\). The following character values are ordered by the four nonidentity angle classes:

| Dimension | \(\pi\) | \(2\pi/3\) | \(2\pi/5\) | \(4\pi/5\) |
| --- | ---: | ---: | ---: | ---: |
| \(3\) | \(-1\) | \(0\) | \(\varphi\) | \(\varphi'\) |
| \(3\) | \(-1\) | \(0\) | \(\varphi'\) | \(\varphi\) |
| \(4\) | \(0\) | \(1\) | \(-1\) | \(-1\) |
| \(5\) | \(1\) | \(-1\) | \(0\) | \(0\) |

Here \(\varphi=(1+\sqrt5)/2\) and \(\varphi'=(1-\sqrt5)/2=1-\varphi\). For clarity, these entries can be derived without assuming a character table: the geometric three-dimensional representation has trace \(1+2\cos\vartheta\); Galois conjugation gives the second three-dimensional row. Subtracting the trivial character from the permutation character on five letters gives the four-dimensional row. Subtracting the trivial character from the symmetric square of the geometric representation gives the five-dimensional row, via \(\chi_{\mathrm{Sym}^2 V}(g)=(\chi_V(g)^2+\chi_V(g^2))/2\). Orthogonality and \(1^2+3^2+3^2+4^2+5^2=60\) show that this list is complete.

For a central function \(f\) on \(I\), left convolution has eigenvalue \(d_\rho^{-1}\sum_{g\in I}f(g)\chi_\rho(g)\) on the \(\rho\)-isotypic block, with multiplicity \(d_\rho^2\). Since the only excluded block under \(\sum_g c_g=0\) is the trivial representation, the claimed conditional negativity is equivalent to four scalar nonpositivity inequalities.

**2. Exact scalar inequalities.** Write \(x=(4/5)^s\), \(y=(2/5)^s\), \(z=(2/3)^s\), and factor out the positive common multiplier \(\pi^s\). The numerators of the four nontrivial convolution eigenvalues are
\[
\begin{aligned}
S_3&=-15+12\varphi y+12\varphi'x,\\
S_{3'}&=-15+12\varphi'y+12\varphi x,\\
S_4&=20z-12(x+y),\\
S_5&=15-20z.
\end{aligned}
\]
The actual eigenvalues are \(\pi^s S_\rho/d_\rho\). Because \(z=(2/3)^s\) is strictly decreasing, \(S_5\le0\) is equivalent to \(s\le s_*\), with equality exactly at \(s=s_*\). For \(s>s_*\), this single five-dimensional Fourier type obstructs conditional negativity.

It remains to verify the other three signs for all \(0<s\le s_*\). First, elementary fourth powers give \((3/2)^{3/4}>4/3\), hence \(s_*<3/4\). As \(y\le x\), \(\varphi>0\), and \(\varphi+\varphi'=1\),
\[
S_3\le-15+12(\varphi+\varphi')x<-3.
\]
For the conjugate three-dimensional character, use \((4/5)^5<2/5\) to obtain \(x^5<y\). The arithmetic-geometric mean inequality gives \(x<y^{1/5}\le(4+y)/5\). Moreover \(s<3/4\) implies \(y>(2/5)^{3/4}>1/2\), since \((2/5)^3>1/16\). Since \(1-4\varphi/5<0\),
\[
\varphi x+\varphi'y<\frac{4\varphi}{5}+\left(1-\frac{4\varphi}{5}\right)y
<\frac12+\frac{2\varphi}{5}<\frac54.
\]
The last inequality follows from \(\varphi<15/8\). Thus \(S_{3'}<0\).

Finally, for \(0<s<3/4\),
\[
\frac{x+y}{z}=\left(\frac35\right)^s+\left(\frac65\right)^s
>\frac23+1=\frac53,
\]
because \((3/5)^{3/4}>2/3\), equivalently \((3/5)^3>(2/3)^4\), and \((6/5)^s>1\). It follows that \(S_4<0\). Consequently all three other Fourier types remain **strictly negative** at the sharp boundary.

**3. Dimensions and exponential kernels.** The centered distance-power matrix eliminates the trivial Fourier block. Below \(s_*\), its remaining \(9+9+16+25=59\) eigenvalues are strictly negative. At equality, exactly the five-dimensional representation block disappears, with multiplicity \(5^2=25\); the three remaining nontrivial blocks contribute rank \(9+9+16=34\). Double-centering therefore produces a positive semidefinite Euclidean squared-distance Gram matrix of precisely the stated rank, and all points remain distinct because \(d(g,h)^s>0\) for \(g\ne h\).

The classical finite-metric Schoenberg equivalence states that \(D_s\) is conditionally negative semidefinite if and only if \(e^{-tD_s}\) is positive semidefinite for every \(t>0\). To see strictness in our finite setting, the centered Gram factorization realizes \(d(g,h)^s=\|u_g-u_h\|^2\) with distinct vectors \(u_g\). The ordinary Euclidean Gaussian \(e^{-t\|u-v\|^2}\) is strictly positive definite on distinct finite points (for example, by its everywhere-positive Fourier density). Conversely, if \(s>s_*\), the positive \(S_5\) eigenvalue gives a nonzero zero-sum vector \(c\) with \(c^*D_sc>0\); then \(c^*e^{-tD_s}c=-t\,c^*D_sc+O(t^2)<0\) for every sufficiently small \(t>0\). This proves every assertion.

## Verification

The included standalone `check_icosahedral.py` enumerates all \(60\) even permutations of five symbols, constructs the two order-five conjugacy classes by explicit conjugation, and forms all \(60\times60\) angle-power matrices independently of the character-eigenvalue formulas. For six exponents, including the sharp boundary and nearby values, it compares the **entire** numerical spectrum (all multiplicities) against the four character expressions and the trivial eigenvalue. The maximum observed spectral discrepancy is less than \(3.1\times10^{-13}\); Gaussian Gram matrices are also checked at three damping strengths. These computations are reproducibility checks, not replacements for the inequalities above, which establish the result for every real exponent in the stated ranges.

Run `python check_icosahedral.py` in an environment with Python 3 and NumPy. No external data are required.

## Relationship to prior work

Meckes's *Positive definite metric spaces* (first public preprint 2010-12-29), Section 3, develops the stable-positive-definiteness / negative-type equivalence for general finite metrics, but does not calculate the icosahedral rotation-angle exponent or representation-block collapse. Gneiting's *Strictly and non-strictly positive definite functions on spheres* (first public preprint 2011-11-30), including its powered-exponential discussion, concerns geodesic distance on round spheres; its one-parameter Schoenberg classifications do not characterize the restricted bi-invariant metric on the finite subgroup \(I\subset SO(3)\). Feragen--Lauze--Hauberg's *Geodesic Exponential Kernels: When Curvature and Linearity Conflict* (first public preprint 2014-11-02) supplies the general curved-space motivation and the conditional-negativity criterion, but its global-geodesic-space conclusions do not determine this finite-group exact spectral threshold. The new assertion is the exact character-theoretic cutoff and its \(25\)-dimensional boundary degeneration, not those general equivalences.

## Limitations

The theorem addresses exactly the \(60\) rotations in the regular icosahedral group and the *all-damping* property of the powered angular kernels. It does **not** classify the full set of individual damping strengths \(t\) for any exponent above the cutoff; large damping always makes a finite-point Gaussian Gram matrix close to the identity. It does not assert that the unrestricted group \(SO(3)\) has the same negative-type exponent. Character-table and finite-group Fourier facts are classical; novelty is asserted only for the explicit cutoff and boundary rank, subject to the limited literature comparison recorded separately.

## References

1. Mark W. Meckes, *Positive definite metric spaces*, arXiv:1012.5863, first version 2010-12-29, https://arxiv.org/abs/1012.5863 (especially Theorem 3.3 and Section 3).
2. Tilmann Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077, first version 2011-11-30, https://arxiv.org/abs/1111.7077 (especially powered-exponential and Schoenberg sections).
3. Aasa Feragen, François Lauze, Søren Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296, first version 2014-11-02, https://arxiv.org/abs/1411.0296 (especially Theorem 4 and Section 4).
