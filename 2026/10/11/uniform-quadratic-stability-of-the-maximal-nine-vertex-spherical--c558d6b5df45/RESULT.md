# Uniform quadratic stability of the maximal nine-vertex spherical polyhedron

## Finding

Let \(p=(p_0,\ldots,p_8)\in(S^2)^9\) be the explicit triaugmented triangular-prism configuration given below, and write \(\mathcal V(q)=\operatorname{vol}_3\operatorname{conv}\{q_0,\ldots,q_8\}\) for \(q\in(S^2)^9\). The constrained Riemannian Hessian \(\mathcal H=D^2_{(S^2)^9}\mathcal V(p)\), acting on the \(18\)-dimensional tangent space with its product round metric, has **exactly three** zero eigenvalues, corresponding to infinitesimal common rotations. On their orthogonal complement it obeys the fully certified inequality

\[
-\langle\mathcal H\xi,\xi\rangle>\frac{39}{100}\|\xi\|^2\quad\text{for every nonzero }\xi\perp T_p(SO(3)\cdot p).
\]

In particular, **there exists** \(\delta>0\) such that every labeled \(q\in(S^2)^9\) with \(\min_{R\in SO(3)}(\sum_{i=0}^8\|q_i-Rp_i\|^2)^{1/2}<\delta\) satisfies the explicit local stability estimate

\[
3\sqrt{2\sqrt3-3}-\mathcal V(q)\ge\frac1{10}\min_{R\in SO(3)}\sum_{i=0}^8\|q_i-Rp_i\|^2.
\]

## Assumptions and scope

The configuration belongs to the unit sphere in Euclidean three-space. Put \(r=\sqrt3-1\) and \(h=\sqrt{2\sqrt3-3}\). In the displayed labeling take

\[
\begin{aligned}
a_0&=(1,0,0),&a_1&=(-1/2,\sqrt3/2,0),&a_2&=(-1/2,-\sqrt3/2,0),\\
u_0&=(1/2,\sqrt3/2,0),&u_1&=(-1,0,0),&u_2&=(1/2,-\sqrt3/2,0),\\
x_i&=(r(u_i)_1,r(u_i)_2,h),&y_i&=(r(u_i)_1,r(u_i)_2,-h)\qquad(0\le i\le2),
\end{aligned}
\]

and \(p=(a_0,a_1,a_2,x_0,x_1,x_2,y_0,y_1,y_2)\). Here \(r^2+h^2=1\), and every point has unit norm. The word *local* means close to the rotation orbit of this **labeled** configuration. No global quantitative stability constant is claimed.

## Proof

**1. Smooth volume chamber.** The convex hull at \(p\) has the following outward-oriented triangular facets, with indices starting at zero:

```
(7,2,4), (5,4,2), (3,0,6), (3,4,5), (3,5,0),
(8,6,0), (8,7,6), (8,2,7), (8,0,5), (8,5,2),
(1,6,7), (1,7,4), (1,3,6), (1,4,3).
```

For each triple \((i,j,k)\), the outward half-space test \(\det(p_j-p_i,p_k-p_i,p_l)<0\) holds strictly for every \(l\notin\{i,j,k\}\); the smallest opposite-side determinant has absolute value exceeding \(0.5476\), certified without floating-point comparisons. The facets use all nine vertices, have exactly twenty-one edges (each incident to two facets), and exhaust a convex simplicial sphere by Euler's relation. Thus there is a neighborhood in which the same facet list is valid and the volume is the cubic polynomial

\[
F(z)=\frac16\sum_{(i,j,k)\text{ facet}}\det(z_i,z_j,z_k).
\]

The exact value \(F(p)=3h\) follows by direct determinant expansion, agreeing with the published global maximization theorem.

**2. Exact constrained Hessian.** Choose two orthonormal tangent vectors at each vertex. At the equatorial vertices use \((-p_{iy},p_{ix},0)\) and \((0,0,1)\). At \(x_i\) or \(y_i\), let \(\epsilon=+1\) or \(-1\) respectively, and use

\[
\bigl(-(u_i)_2,(u_i)_1,0\bigr),\qquad
\bigl(-\epsilon h(u_i)_1,-\epsilon h(u_i)_2,r\bigr).
\]

Denote the resulting eighteen tangent basis vectors by \(e_{i\alpha}\). The ambient derivative of the facet polynomial satisfies

\[
\nabla_{z_i}F(p)=\frac16\sum_{(i,j,k)\text{ cyclically oriented facet}}p_j\times p_k,
\quad
\lambda_i=p_i\cdot\nabla_{z_i}F(p).
\]

Since the published global theorem makes \(p\) a maximizer, the first tangent derivatives vanish. They can also be checked by direct substitution into the displayed formula. The constrained Hessian is therefore

\[
\mathcal H_{i\alpha,j\beta}
=\begin{cases}
D^2 F(p)[e_{i\alpha},e_{j\beta}],&i\ne j,\\
-\lambda_i\delta_{\alpha\beta},&i=j,
\end{cases}
\]

where each off-diagonal term is the sum of signed trilinear terms \(\det(e_{i\alpha},e_{j\beta},p_k)/6\) over the incident oriented facets. The diagonal correction is the sphere's second fundamental form. There is no additional same-vertex second derivative, because \(F\) is separately affine in each vertex.

**3. Quantified transverse negativity.** For the three coordinate rotations put \(W_{i\alpha,j}=e_{i\alpha}\cdot(E_j\times p_i)\), where \(E_j\) is the \(j\)-th Cartesian basis vector. Symmetry and \(r^2+h^2=1\) give the **exact** Gram identity

\[
W^{\mathsf T}W=\operatorname{diag}(g,g,k),\qquad
 g=\frac{15}{2}-3r^2,\quad k=3+6r^2.
\]

The orthogonal projector onto the infinitesimal-rotation space is \(P=W\operatorname{diag}(1/g,1/g,1/k)W^{\mathsf T}\). Because the volume is rotationally invariant and \(p\) is stationary, \(\mathcal HW=0\). The attached checker proves that the symmetric real \(18\times18\) matrix

\[
C=-\mathcal H+P-\frac{39}{100}I_{18}
\]

is **positive definite**: it constructs rigorous enclosing rational intervals for all its entries and performs an outward-rounded \(LDL^{\mathsf T}\) decomposition. All eighteen certified pivots are positive; the smallest lower endpoint exceeds \(0.05575\). Arithmetic uses only exact integers, with all divisions and products rounded outward. On the orthogonal complement of \(\operatorname{im}(W)\) one has \(P=0\), proving the strict \(39/100\) gap. On \(\operatorname{im}(W)\), \(\mathcal H=0\), proving that these are exactly the Hessian's three null directions.

**4. Quadratic stability.** In a sufficiently small neighborhood of the compact orbit \(SO(3)\cdot p\), nearest-orbit normal coordinates exist. The first variation vanishes and the Hessian is uniformly negative with the stated gap on all normal slices by rotation invariance. Taylor expansion, with uniform remainder \(o(\|\xi\|^2)\), gives a deficit of at least \(0.19\|\xi\|^2\) when the neighborhood is small enough. The squared chordal distance of the nine points to the orbit equals \(\|\xi\|^2+o(\|\xi\|^2)\). Shrinking the neighborhood if necessary yields the stated conservative coefficient \(1/10\). No finite numerical experiment substitutes for the analytic Taylor argument.

## Verification

Run `python3 certify_nine_vertex.py` with Python 3 and no third-party packages. The program checks all eighty-four strict facet half-space inequalities (fourteen facets, six opposite vertices each), computes the Hessian from explicit determinants, bounds the real constants by integer-square-root intervals at denominator \(10^{18}\), and checks all eighteen positive \(LDL^{\mathsf T}\) pivots. It prints `VERIFY_OK` on success. It also checks high-precision first-derivative and rotational Gram residuals as **consistency tests only**; their exact vanishing follows from the analytic symmetry and stationary-maximizer argument above. The finite matrix certificate proves the spectral bound for all real tangent perturbations, not just sampled perturbations.

## Relationship to prior work

Hoehner and Ledford proved the optimal nine-vertex spherical polyhedron and its equality class in Theorem 1.1 of arXiv:2608.04392v1, first publicly posted August 5, 2026. That global result supplies the distinguished configuration and its criticality. The present claim adds the full transverse Hessian sign and explicit certified spectral gap in all fifteen nonrotational tangent directions, plus the quadratic local volume-deficit estimate. A unique global maximizer need not have nondegenerate Hessian; the new conclusion does not follow formally from uniqueness. Their uses of Hessians for auxiliary concavity estimates concern different functions, not this constrained full-configuration second variation. Earlier inscribed-polytope optimization work treats global maxima and stationarity, not the quantitative Hessian conclusion for these nine points.

## Limitations

The coefficient \(39/100\) is a certified lower bound for the positive transverse spectral gap, not asserted optimal; numerical evidence suggests a gap near \(0.39549\). The local radius \(\delta\) is existential, not numerically optimized. Stability is proved near one labeled rotational orbit, not globally over all configurations modulo vertex permutations. The global uniqueness theorem and its geometric coordinates are used from the cited published source. The argument is confined to a fixed nine-point configuration and uses the published global maximum theorem as an input.

## References

1. S. Hoehner and J. Ledford, *The maximum volume polytope with nine vertices inscribed in the sphere*, arXiv:2608.04392v1, initially public 2026-08-05; particularly Theorem 1.1 and Section 4.
2. J. D. Berman and K. Hanes, *Volumes of Polyhedra Inscribed in the Unit Sphere in E³*, Mathematische Annalen **188** (1970), 78–84, DOI 10.1007/BF01435416 (historical maximal-volume and stationarity background).
