# Exact shortest-arm law for continuous linear spline projection on metric stars

## Finding
Let \(m\ge3\), let \(\Gamma\) be a compact metric star with arms of lengths \(\ell_1,\ldots,\ell_m>0\), and put \(S=\sum_{j=1}^m\ell_j\), \(h=\min_j\ell_j\). Let \(V\) be the space of continuous functions on \(\Gamma\) that are affine on every whole arm, with no prescribed boundary values. Write \(P:L^2(\Gamma)\to V\) for the \(L^2\)-orthogonal projector with respect to arc length. Its extension to bounded measurable inputs satisfies the exact sharp endpoint law
\[
\boxed{\|P\|_{L^\infty(\Gamma)\to L^\infty(\Gamma)}=\frac{7S+3h}{3(S+h)}.}
\]
Every maximizing evaluation vertex is a leaf on an arm of minimum length, and no other point of the star is maximizing. For every such leaf, a measurable input of modulus one attains the operator norm there.

For fixed \(m\ge3\) and fixed total length \(S>0\), the complete range of attainable projector norms, varying over all strictly positive arm lengths, is
\[
\boxed{\left[\frac{7m+3}{3(m+1)},\ \frac73\right).}
\]
The minimum is attained exactly by the equilateral star. The supremum \(7/3\) is not attained but is approached as the shortest arm shrinks to zero at fixed total length. The norm exceeds \(2\) exactly when \(h<S/3\); thus every star with at least four arms has norm strictly greater than \(2\), whereas the equilateral three-arm star has norm \(2\). The sharp negative excursion of the projection of data satisfying \(0\le f\le1\) is \(-\tfrac12(\|P\|_{\infty\to\infty}-1)\), attained at a shortest-arm leaf.

## Assumptions and scope
The metric star is the union of \(m\) intervals \([0,\ell_j]\) with their zero endpoints identified into a common center. Each arm is otherwise disjoint; its outer endpoint is a leaf. Arc length is the measure; there is exactly one affine element per arm. The projector has the standard full continuous nodal hat basis, one central hat and one hat at each leaf. No Dirichlet constraints, mass lumping, vertex atoms, derivative matching, or additional interior knots are imposed. The input and output spaces may be real or complex. Supremum norms are essential suprema on functions, identified with true suprema on the continuous projected outputs.

The statement concerns a sharp stability constant for a globally continuous graph-spline \(L^2\) projection, not a local projector on each independent arm and not the energy/Ritz projection. In particular, joining arms changes the projector because the central coefficient is shared.

## Proof
Let \(\phi_0\) be the central nodal hat, and \(\phi_j\) the leaf hat on arm \(j\). With arm coordinate \(u\in[0,1]\), \(\phi_0=1-u\), \(\phi_j=u\), and all other leaf hats vanish. Their Gram matrix is
\[
M_{00}=S/3,\qquad M_{0j}=M_{j0}=\ell_j/6,\qquad M_{ij}=\delta_{ij}\ell_i/3\quad(i,j\ge1).
\]
It is positive definite because the hats are linearly independent. The Schur complement of the diagonal leaf block is \(S/4\). Consequently its exact inverse \(B=M^{-1}\) has entries
\[
B_{00}=4/S,\qquad B_{0j}=B_{j0}=-2/S,\qquad B_{ij}=3\delta_{ij}/\ell_i+1/S\quad(i,j\ge1).
\]
The projection has reproducing kernel
\[
K(x,y)=\sum_{a,b=0}^m\phi_a(x)B_{ab}\phi_b(y),\qquad (Pf)(x)=\int_\Gamma K(x,y)f(y)\,dy.
\]
For every fixed \(x\), the sharp norm of evaluation at \(x\) is \(\int_\Gamma|K(x,y)|\,dy\), realized by \(f(y)=\operatorname{sgn}\!\big(K(x,y)\big)\) (and by the complex phase analogue, with the value at zeros irrelevant).

The function \(x\mapsto K(x,\cdot)\) is affine in the coordinate of each arm, so \(x\mapsto\int|K(x,y)|\,dy\) is convex on each arm. Thus some vertex maximizes globally. Moreover, it is strictly below the larger endpoint value at any interior point: the center and leaf kernels have opposite signs on a positive-length initial segment of every arm, so the triangle inequality is strict in their nontrivial convex combinations.

At the center, \(K(0,y)=(4-6u)/S\) on every arm. Therefore
\[
\int_\Gamma|K(0,y)|\,dy=\int_0^1|4-6u|\,du=5/3.
\]
Fix leaf \(i\). On its own arm, its kernel is linear from \(-2/S\) at the center to \(3/\ell_i+1/S\) at the leaf. On every other arm it is linear from \(-2/S\) to \(1/S\). The absolute integral of the affine function between real endpoint values \(a<0<b\) is \((a^2+b^2)/(2(b-a))\). Hence the contribution of the own arm is
\[
\frac{9S^2+6S\ell_i+5\ell_i^2}{6S(S+\ell_i)},
\]
while all remaining arms together contribute \(5(S-\ell_i)/(6S)\). Adding gives the exact leaf row norm
\[
\mathcal L_i=\int_\Gamma|K(\mathrm{leaf}_i,y)|\,dy=\frac{7S+3\ell_i}{3(S+\ell_i)}.
\]
Its derivative with respect to \(\ell_i\) at fixed \(S\) is \(-4S/[3(S+\ell_i)^2]<0\), so precisely the shortest-arm leaves maximize among leaves. Since \(\ell_i<S\) for \(m\ge3\), \(\mathcal L_i-5/3=2(S-\ell_i)/[3(S+\ell_i)]>0\); thus no center or interior point attains the global norm. The sign input above attains the bound at the chosen shortest leaf.

Because \(h\le S/m\), the strictly decreasing function \((7S+3h)/(3(S+h))\) is minimized exactly at \(h=S/m\), which forces every arm length to equal \(S/m\). This gives the stated minimum. Letting \(h\downarrow0\) while keeping the other arms positive makes the norm tend strictly upward to \(7/3\), which cannot be attained since \(h>0\). All intermediate values occur by a continuous one-parameter family with one arm of length \(h\in(0,S/m]\) and the other \(m-1\) arms sharing the remaining length equally. Solving \((7S+3h)/(3(S+h))>2\) yields \(h<S/3\); at degree \(m\ge4\), this is automatic.

Lastly, \(P1=1\), so \(\int K(x,y)\,dy=1\). For \(0\le f\le1\), the smallest possible value of \((Pf)(x)\) is the integral of the negative part of \(K(x,\cdot)\), which equals \((1-\int|K(x,y)|dy)/2\). Maximizing the negative mass over \(x\) gives the positivity-defect assertion, and the indicator of the negative kernel set attains it.

## Verification
The included `verify.py` independently assembles the Gram matrix from arm lengths, inverts it by exact rational Gaussian elimination (not using the displayed block inverse), and evaluates all absolute kernel-row integrals exactly from their endpoint values. A fixed-seed collection of 1,980 positive rational length vectors, ranging from two to twelve arms, checks the mass-matrix inverse, center and leaf row integrals, monotonic extremality and closed formulas, together with two limiting/symmetric sanity checks. It reports 1,982 exact checks when run with Python 3. These computations exercise finite instances, not the universally quantified proof. They may be rerun with `python3 verify.py`.

## Relationship to prior work
Uniform \(L^\infty\) stability of \(L^2\)-orthogonal spline projection is classical. Oswald's 2006 preprint (later published in 2007/2008) recounts the bound \(3\) for piecewise-linear splines on intervals and constructs a divergent family for triangulations of Euclidean domains of dimension at least two. The theorem here is not a direct consequence of either result: it concerns one-dimensional *branched* networks, and establishes an exact geometry-dependent norm strictly below \(7/3\), not merely an upper bound. Passenbrunner and Shadrin's 2013 paper proves almost-everywhere convergence and inverse-Gram decay for interval spline projection, not a branched graph formula. A closely related 2013 Oswald survey studies triangular meshes and one-dimensional sharp bounds; its bibliographic description was examined, but full-text access was unavailable and is a remaining priority risk.

A published sharp affine-projector result on a simplex (identifier `99c2b9dd9b34`) concerns the *local* polynomial projector on an individual simplex, explicitly without global continuity constraints between elements. It does not imply the present globally coupled star projection or its shortest-arm law. Similarities between matrix formulas alone are not implications: the simplex Gram matrix is a rank-one deformation of a scalar identity, while the star mass matrix has one shared vertex and edge-length-weighted leaves. The stated star formula was also compared against accessible earlier results on splines, least-squares finite elements, graph projection norms, and their aliases in mathematical-record searches. No checked claim implied the exact norm-and-range statement; this is limited search evidence, not proof of universal priority.

## Limitations
Only one continuous piecewise-affine finite element per arm is treated. Adding knots, imposing node constraints, weighting measure nonuniformly within an arm, or changing projection norms can alter the formula. The claim does not cover arbitrary trees, all finite element discretizations, or multivariate simplicial complexes. The checker supports the elementary block-matrix computation but cannot certify uniqueness in the literature. Related older work may express an equivalent identity as a graph-spline Lebesgue constant or finite-element reproducing-kernel norm; particularly, the complete text of Oswald's 2013 chapter was unavailable via the attempted authorized access route. Independent mathematical and bibliographic review has not been performed.

## References
1. Peter Oswald, *A counterexample concerning the \(L_2\)-projector onto linear spline spaces*, arXiv:math/0611573, first publicly posted 2006-11-19; subsequently Mathematics of Computation, DOI 10.1090/S0025-5718-07-02059-5.
2. Markus Passenbrunner and Alexei Shadrin, *On almost everywhere convergence of orthogonal spline projections with arbitrary knots*, arXiv:1308.4824, first publicly posted 2013-08-22; Journal of Approximation Theory 180 (2014), 77–89, DOI 10.1016/j.jat.2013.12.004.
3. Peter Oswald, *\(L^\infty\)-Bounds for the \(L^2\)-Projection onto Linear Spline Spaces*, in *Recent Advances in Harmonic Analysis and Applications* (2013), 303–316, DOI 10.1007/978-1-4614-4565-4_24; abstract/bibliographic material checked, full text inaccessible.
4. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34 (accessed 2026-10-17).
