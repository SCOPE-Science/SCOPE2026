# Sharp obtuse-angle amplification law for nodal finite-element clipping

## Finding

For every nondegenerate Euclidean triangle \(T\), every constant real symmetric positive-definite \(2\times2\) diffusion matrix \(D\), and every nondegenerate clipping interval \([a,b]\) with \(a<b\), the sharp amplification of the piecewise-affine Dirichlet energy by **clipping the three vertex values and then reinterpolating** is
\[
\sup_{E_{T,D}(x)>0}\frac{E_{T,D}(P_{[a,b]}x)}{E_{T,D}(x)}
=\begin{cases}
1,&\Theta\le\pi/2,\\
\csc^2\Theta,&\pi/2<\Theta<\pi,
\end{cases}
\]
where \(\Theta\) is the largest interior angle of the transformed triangle \(D^{-1/2}T\), and \(P_{[a,b]}(t)=\max(a,\min(t,b))\). The same exact sharp constant holds for either one-sided clip \(\max(t,a)\) or \(\min(t,b)\). Every nondecreasing scalar 1-Lipschitz map obeys the same upper bound, without a general assertion of sharpness for that map.

The amplification constant is exactly one in the nonobtuse metric geometry and is strictly larger than one precisely when that metric triangle is obtuse. It tends to infinity as its largest angle approaches \(\pi\). For the exact \(120^\circ\) example below, the maximal ratio is \(4/3\).

## Assumptions and scope

Let \(T\subset\mathbb R^2\) have distinct noncollinear vertices \(z_1,z_2,z_3\), with barycentric basis \(\lambda_i\). For a real nodal vector \(x=(x_1,x_2,x_3)\), define the \(P_1\) interpolant and its constant-coefficient diffusion energy by
\[
u_x(z)=\sum_{i=1}^{3}x_i\lambda_i(z),\qquad
E_{T,D}(x)=\int_T (\nabla u_x)^{\mathsf T}D\nabla u_x\,dz.
\]
Here \(D=D^{\mathsf T}\succ0\) is fixed on \(T\); no mesh regularity or acute-angle assumption is imposed. Both the numerator and denominator are invariant under shifting \(x\) by a constant before a pure linear energy evaluation, but the clipping operator itself is applied to the original specified values. The ratio is taken over all \(x\) with nonzero original energy; fixed finite clipping bounds \(a<b\) do not restrict \(x\).

The metric angle \(\Theta\) is the largest ordinary interior angle in the triangle with vertices \(D^{-1/2}z_i\). Equivalently the dot products of transformed gradients use the \(D\)-inner product.

## Proof

**Reduction to two ordered slopes.** Take any nonconstant nodal vector, relabeling the three vertices so \(x_i\le x_j\le x_k\). Set \(r=x_j-x_i\ge0\), \(s=x_k-x_j\ge0\). Since \(\nabla\lambda_i+\nabla\lambda_j+\nabla\lambda_k=0\),
\[
\nabla u_x=-r\nabla\lambda_i+s\nabla\lambda_k=:v+w.
\]
For any nondecreasing 1-Lipschitz scalar map \(g\), the transformed gaps are \(r'=g(x_j)-g(x_i)\in[0,r]\) and \(s'=g(x_k)-g(x_j)\in[0,s]\). Consequently, \(\nabla u_{g(x)}=\alpha v+\beta w\) for some \(\alpha,\beta\in[0,1]\), interpreting a zero gap as a zero vector. Pointwise in the ordered-gap pair, convexity of squared norm on the unit square gives
\[
\|\alpha v+\beta w\|_D^2\le
\max\{0,\|v\|_D^2,\|w\|_D^2,\|v+w\|_D^2\},
\qquad \|q\|_D^2=q^{\mathsf T}Dq.
\]
The angle between the nonzero vectors \(-\nabla\lambda_i\) and \(\nabla\lambda_k\) in the \(D\)-inner product is exactly the interior angle \(\theta_j\) at the middle-valued vertex of \(D^{-1/2}T\). This can be checked by mapping the triangle through \(z\mapsto D^{-1/2}z\) and using the fact that a barycentric gradient is orthogonal to its opposite edge.

**Angle bound.** If \(\theta_j\le\pi/2\), then \(v^{\mathsf T}Dw\ge0\), so both single-slope energies are at most \(\|v+w\|_D^2\). If \(\pi/2<\theta_j<\pi\), write \(V=\|v\|_D\), \(W=\|w\|_D\). Direct expansion gives the exact identities
\[
\|v+w\|_D^2-V^2\sin^2\theta_j
=(W+V\cos\theta_j)^2\ge0,
\]
\[
\|v+w\|_D^2-W^2\sin^2\theta_j
=(V+W\cos\theta_j)^2\ge0.
\]
Hence the energy ratio is bounded by \(\max\{1,\csc^2\theta_j\}\). A nondegenerate triangle has at most one obtuse angle, yielding the asserted bound with largest angle \(\Theta\). The area multiplier \(|T|\) in each energy cancels.

**Sharpness of the upper and bounded clip.** If \(\Theta\le\pi/2\), select any nonconstant \(x\) with every component strictly inside \((a,b)\); its ratio equals one. If \(\Theta>\pi/2\), let \(j\) be the obtuse vertex and choose the other indices \(i,k\). Let \(G_i=\|\nabla\lambda_i\|_D\), \(G_k=\|\nabla\lambda_k\|_D\). For sufficiently small \(\delta>0\), take
\[
x_i=b-\delta,\qquad x_j=b,\qquad
x_k=b+\eta,\qquad
\eta=-\delta\frac{G_i}{G_k}\cos\Theta>0.
\]
The bounded or upper-only clip changes \((x_i,x_j,x_k)\) into \((b-\delta,b,b)\), annihilating \(w\) and preserving \(v\). Since \(W=-V\cos\Theta\), the first exact identity above is equality, and the quotient is \(\csc^2\Theta\). For the lower-only clip, pick sufficiently small \(\eta>0\), take \(x_i=a-\delta,x_j=a,x_k=a+\eta\) with \(\delta=-\eta G_k\cos\Theta/G_i>0\). This annihilates \(v\) and preserves \(w\), attaining the same quotient by the second identity. The finite clipping interval can be respected in either construction by making the preserved gap sufficiently small. Thus all three claimed suprema are attained as maxima.

**Exact counterexample.** For \(D=I\), vertices \((0,0)\), \((1,0)\), \((-1/2,\sqrt3/2)\) have a \(120^\circ\) angle at the first vertex. With \(x=(1,0,3/2)\) and clipping to \([0,1]\), \(y=(1,0,1)\). The local stiffness matrix, after dividing out a common positive geometric factor, is
\[
K=\begin{pmatrix}4&-2&-2\\-2&4/3&2/3\\-2&2/3&4/3\end{pmatrix}.
\]
Then \(x^{\mathsf T}Kx=1\), while \(y^{\mathsf T}Ky=4/3\), exactly the sharp factor \(\csc^2(2\pi/3)=4/3\).

**Mesh consequence.** On any conforming planar \(P_1\) triangulation with a constant SPD tensor on each triangle, the sum of the local inequalities gives a global energy bound with coefficient \(\max_T C_{T,D_T}\). This coefficient is a valid bound, not asserted to be globally attained under vertex-sharing constraints. Pointwise spatial clipping of the *continuous* affine function is a distinct operation and is energy nonincreasing by the Sobolev chain rule; it need not remain affine on the original triangle. The strict gain above concerns clipping **nodal data and reinterpolating**.

## Verification

The standalone program `verify.py` (Python 3 with NumPy as specified in `requirements.txt`) validates the stiffness construction against an exact rational \(120^\circ\) witness, tests 210,000 randomly chosen local isotropic/anisotropic energy inequalities for bounded/one-sided nonlinearities, and checks 46 sharpness constructions. Run `python verify.py` from the extracted file directory. It prints `VERIFY_OK: exact_example=4/3, random_energy_comparisons=210000, sharp_upper_lower_examples=46`. These computational tests corroborate, but do not replace, the proof for every triangle and all real nodal values.

## Relationship to prior work

Li, Yang and Zhou [1] introduced nodal cut-off in high-order parabolic finite-element/exponential integration. Yang, Yuan and Zhou [2], Appendix B and Lemma 4.1 of their accessible preprint, establish \(H^1\)-seminorm contraction for nodal cut-off on **one-dimensional piecewise-linear** elements, where the interval energy is a sum of nonnegative squared nodal differences. Neither result states this sharp local two-dimensional triangle-angle amplification law.

Kreuzer [3] proves a posteriori cutoff energy improvement using the **pointwise** truncated finite-element function, which is different from nodally truncating and then taking the \(P_1\) interpolant; his inequality remains valid and does not rule out the counterexample here. Huang [4] relates anisotropic nonobtuse/Delaunay mesh geometry to discrete maximum principles, using the diffusion metric; it does not give the sharp two-dimensional quantitative clipping amplification. A Delaunay cancellation in a globally assembled stiffness matrix must not be confused with elementwise nonobtuseness. No published equivalent with the same operator, energy quotient and anisotropic sharp constant was identified in the comparisons undertaken; specialized results may remain uncatalogued.

## Limitations

The result is local to planar affine \(P_1\) elements and piecewise-constant SPD diffusion. It is not a statement about \(L^2\) projection, higher-order finite elements, three-dimensional simplices, anisotropic meshes with spatially varying diffusion within an element, or algorithmic convergence rates. The mesh coefficient is sufficient rather than necessarily globally sharp. This is a mathematical sharpness theorem for the specified energy transformation, not an assertion that nodal cut-off always increases energy on obtuse meshes. Independent publication-priority and mathematical review have not been performed.

## References

1. B. Li, J. Yang and Z. Zhou, *Arbitrarily high-order exponential cut-off methods for preserving maximum principle of parabolic equations*, arXiv:2010.08789v1, publicly submitted 2020-10-17, https://arxiv.org/abs/2010.08789 .
2. J. Yang, Z. Yuan and Z. Zhou, *Arbitrarily High-order Maximum Bound Preserving Schemes with Cut-off Postprocessing for Allen-Cahn Equations*, arXiv:2102.13271v1, publicly submitted 2021-02-26, https://arxiv.org/abs/2102.13271 .
3. C. Kreuzer, *A Note on Why Enforcing Discrete Maximum Principles by a Simple a Posteriori Cutoff is a Good Idea*, arXiv:1208.3958v1, https://arxiv.org/abs/1208.3958 .
4. W. Huang, *Discrete maximum principle and a Delaunay-type mesh condition for linear finite element approximations of two-dimensional anisotropic diffusion problems*, arXiv:1008.0562v1, https://arxiv.org/abs/1008.0562 .
