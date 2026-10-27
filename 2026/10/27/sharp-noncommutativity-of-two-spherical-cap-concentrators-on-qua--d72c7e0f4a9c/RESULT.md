# Sharp noncommutativity of two spherical-cap concentrators on quadratic harmonics

## Finding

Let \(S^2\) carry normalized area measure \(d\sigma\), and let \(\mathcal H_2\) be the five-dimensional complex space of spherical harmonics of exactly degree \(2\), equipped with its \(L^2(S^2,d\sigma)\) inner product. For a unit axis \(u\in S^2\) and a cap threshold \(-1<c<1\), put
\[
C(u,c)=\{\xi\in S^2:\xi\cdot u\ge c\},\qquad
A_{u,c}=P_2\,M_{\mathbf 1_{C(u,c)}}\big|_{\mathcal H_2},
\]
where \(P_2\) is orthogonal projection onto \(\mathcal H_2\).

**Theorem.** For any two axes \(u,v\in S^2\) and any thresholds \(c,d\in(-1,1)\),
\[
\boxed{\|[A_{u,c},A_{v,d}]\|_{\mathrm{op}}\le \frac9{250}.}
\]
Equality holds **if and only if**
\[
\boxed{c^2=d^2=\frac15,\qquad (u\cdot v)^2=\frac12.}
\]
In particular, the sharp bound is attained by two caps with the same threshold \(1/\sqrt5\) and axes at \(45^\circ\). The commutator always has eigenvalues \(0,\pm iL,\pm iR\), for explicit nonnegative \(L,R\) below. The sharp value comes exclusively from the two-dimensional angular block; the competing three-dimensional block is **strictly** below \(9/250\) for every cap pair.

## Assumptions and scope

All functions may be complex-valued. The caps may overlap, be disjoint, or have thresholds of either sign. The operator norm is for the five-dimensional Hilbert space \(\mathcal H_2\), not the full low-pass space through degree \(2\). Boundary circles have measure zero. The result applies to arbitrary axis directions; their only relevant parameter is \(t=(u\cdot v)^2\in[0,1]\). All exact inequalities are over real parameters, not approximations from grids.

## Proof

**1. Cap eigenvalues.** Fix the polar axis. The \(|m|=0,1,2\) eigenspaces of a polar cap have multiplicities \(1,2,2\), and their respective normalized polar densities, with \(r=\cos\theta\), are
\[
\rho_0(r)=\tfrac58(3r^2-1)^2,\quad
\rho_1(r)=\tfrac{15}4r^2(1-r^2),\quad
\rho_2(r)=\tfrac{15}{16}(1-r^2)^2.
\]
Each integrates to \(1\) over \([-1,1]\); the cap eigenvalues are \(\lambda_j(c)=\int_c^1\rho_j(r)\,dr\). Elementary integration gives
\[
 a(c):=\lambda_0(c)-\lambda_2(c)=\frac{5c(1-c^2)(3c^2+1)}{16},
\quad b(c):=\lambda_1(c)-\lambda_2(c)=\frac{15c(1-c^2)^2}{16}.
\]
The scalar term \(\lambda_2(c)I\) drops from commutators. Also \(a(-c)=-a(c)\) and \(b(-c)=-b(c)\), so signs of the thresholds can be absorbed when maximizing the norm.

**2. Rotating the degree-two space.** Identify \(\mathcal H_2\) with complex trace-free symmetric \(3\times3\) matrices by restricting the quadratic form \(\xi\mapsto\xi^TQ\xi\) to the sphere. Use the real orthonormal traceless-matrix basis
\[
\begin{split}
E_0&=\mathrm{diag}(-1,-1,2)/\sqrt6,\\
E_{1x}&=(e_xe_z^T+e_ze_x^T)/\sqrt2,\quad E_{1y}=(e_ye_z^T+e_ze_y^T)/\sqrt2,\\
E_{2c}&=\mathrm{diag}(1,-1,0)/\sqrt2,\quad E_{2s}=(e_xe_y^T+e_ye_x^T)/\sqrt2.
\end{split}
\]
The degree-two harmonic inner product is a common positive multiple of the Frobenius inner product, so this is an orthogonal coordinate model for the concentration operators. With \(x=\cos\theta\), \(z=\sin\theta\), an axis rotation through \(\theta\) in the \(xz\)-plane has real orthogonal matrix
\[
D(x,z)=\begin{pmatrix}
(3x^2-1)/2 &-\sqrt3xz&0&\sqrt3z^2/2&0\\
\sqrt3xz&x^2-z^2&0&-xz&0\\
0&0&x&0&-z\\
\sqrt3z^2/2&xz&0&(1+x^2)/2&0\\
0&0&z&0&x
\end{pmatrix}.
\]
Writing \(a=a(c)\), \(b=b(c)\), \(a'=a(d)\), \(b'=b(d)\), the commutator is unitarily similar to the commutator of
\[
\mathrm{diag}(a,b,b,0,0)\quad\text{and}\quad
D\,\mathrm{diag}(a',b',b',0,0)D^T.
\]
It separates into a real skew \(3\times3\) block on indices \(0,1,3\) and a real skew \(2\times2\) block on indices \(2,4\).

**3. Exact two-block norm.** Set \(t=x^2\in[0,1]\), and define
\[
\begin{split}
U&=3t(1-t)(a-b)^2\left(\frac{a'(3t-1)}2-b'(2t-1)\right)^2,\\
V&=3(1-t)^2a^2\left(\frac{a'(3t-1)}4-b't\right)^2,\\
W&=t(1-t)b^2\left(\frac{3a'(1-t)}2+b'(2t-1)\right)^2.
\end{split}
\]
Direct matrix multiplication gives
\[
L^2=U+V+W,\qquad R^2=b^2(b')^2t(1-t),
\quad \|[A_{u,c},A_{v,d}]\|=\max\{L,R\}.
\]
The two skew blocks yield \(\{0,\pm iL,\pm iR\}\), with the usual convention that some eigenvalues can coincide at zero.

**4. Sharp two-dimensional block.** For \(0\le r\le1\),
\[
\frac{d}{dr}b(r)=\frac{15}{16}(1-r^2)(1-5r^2).
\]
Consequently \(0\le b(r)\le 3/(5\sqrt5)\), with equality only at \(r=1/\sqrt5\). Together with \(t(1-t)\le1/4\), this gives
\[
R\le \frac12\left(\frac3{5\sqrt5}\right)^2=\frac9{250},
\]
with equality precisely for the stated squared thresholds and squared axis overlap.

**5. Strict global control of the other block.** Here an exact, finite, rational Bernstein-positivity certificate avoids numerical maximization. For \(c,d,t\in[0,1]\), let
\[
F(c,d,t)=\left(\frac9{250}\right)^2-(U+V+W).
\]
This polynomial has separate degrees \((10,10,4)\) in \((c,d,t)\). Convert it exactly to the tensor-product Bernstein basis on the unit cube, and recursively bisect at \(1/2\), splitting coordinate \(c\), then \(d\), then \(t\), cyclically. Accept a box only when **every** Bernstein coefficient is strictly positive. Exact rational arithmetic certifies a partition with nine accepted leaves and seventeen visited nodes, with depth at most four. The smallest coefficient on every accepted leaf exceeds \(1/40000\). Since a Bernstein basis is nonnegative and sums to one throughout its box, this is a proof that
\[
F(c,d,t)>\frac1{40000}>0
\]
for the entire unit cube. The supplied program `verify_two_caps.py` derives \(F\), checks the spherical integrals and rotation-block identities symbolically, performs all rational basis conversions and subdivisions, and asserts the strict coefficient margin. It needs no floating-point decisions for certification. In particular, \(L<9/250\) for all cap parameters. Combining this with step 4 proves the theorem and all equality cases.

## Verification

Run `python verify_two_caps.py` with Python 3 and SymPy. The checker verifies all three normalized cap densities, the rotation matrix identity modulo \(x^2+z^2=1\), the complete squared-entry formulas for both skew blocks, a strict nine-leaf exact Bernstein certificate with coefficient floor \(1/40000\), and the exact optimizing derivative and equality constant. Exact-rational positivity on finitely many Bernstein cells establishes an inequality on the **whole continuum** of cap parameters; it is not finite sample interpolation. The verification script supplies its own source expressions and performs symbolic checks at execution.

## Relationship to prior work

Spherical Slepian localization and cap concentration matrices are established in Simons–Dahlen–Wieczorek (2004/2006) and Michel–Plattner–Seibert (2021). The latter develops a general polar-cap commuting **differential operator** and spin-weighted variants; that single-region commuting relation is different from the commutator of concentration operators for **two different cap axes**. Jaming–Speckbacher (2020) establishes large-sieve concentration bounds for harmonic expansions on two-point-homogeneous spaces, not a sharp joint operator commutator. The present finite-dimensional calculation exploits the established harmonic framework but optimizes a new two-cap interaction over both openings and relative orientation. The exact one-cap angular spectra, considered separately, do not alone identify the sharp two-cap constant.

## Limitations

Only exact degree \(2\) on \(S^2\) is covered. The number \(9/250\) is not asserted for the low-pass space, vector or tensor Slepian spaces, or higher harmonic degrees; nor does it imply a noise-robust reconstruction theorem.

## References

1. V. Michel, A. Plattner, K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650 (first publicly posted 2021-03-26), especially Sections 3.1–3.3.
2. P. Jaming and M. Speckbacher, *Concentration Estimates for Finite Expansions of Spherical Harmonics on Two-Point Homogeneous Spaces via the Large Sieve Principle*, arXiv:2004.02474 (first posted 2020-04-06), especially Section 4.
3. F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral Concentration on a Sphere*, arXiv:math/0408424 (2004), foundational spherical Slepian concentration setting.
