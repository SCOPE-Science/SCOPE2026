# Exact Hilbert distortion of a four-point ultrametric with an equilateral cluster

## Finding

For every \(0<t\le1\), let \(M_t=\{o,a_1,a_2,a_3\}\) have pairwise distances \(d(o,a_i)=1\) and \(d(a_i,a_j)=t\) for distinct indices. Over the real scalars, its Lipschitz-free space has exact Euclidean Banach--Mazur distance

\[\boxed{d_{\mathrm{BM}}\!\left(\mathcal F(M_t),\ell_2^3\right)^2=\frac{7-2t-t^2}{3-t^2}.}\]

For example, at \(t=1/2\), the squared distance is \(23/11\). It decreases strictly with \(t\), has limit \(7/3\) as \(t\) tends to zero through positive values, and equals \(2\) at the equilateral endpoint \(t=1\). The infimum is taken over every invertible real linear transformation.

## Assumptions and scope

The free space \(\mathcal F(M_t)\) is the real Banach space whose dual is \(\operatorname{Lip}_0(M_t)\), the real Lipschitz functions vanishing at the base point \(o\), with the usual Lipschitz norm. Identify a function with \(x=(f(a_1),f(a_2),f(a_3))\). Its dual unit ball is the three-dimensional centrally symmetric polytope

\[K_t=\left\{x\in\mathbb R^3:\ |x_i|\le1\ (1\le i\le3),\quad |x_i-x_j|\le t\ (1\le i<j\le3)\right\}.\]

For real finite-dimensional spaces the Banach--Mazur distance is invariant under duality, so it suffices to compute the distance of this Lipschitz space to \(\ell_2^3\). For an inner-product quadratic form \(Q\), put

\[m_Q=\min_{x\in\partial K_t}Q(x),\qquad M_Q=\max_{x\in K_t}Q(x).\]

The square of the distortion furnished by this Euclidean form equals \(M_Q/m_Q\). The sought distance squared is the minimum of this ratio over all positive definite quadratic forms, since each such form represents an arbitrary invertible linear change of Euclidean coordinates.

## Proof

**1. Symmetry reduction is globally optimal.** Permuting the three nonbase points leaves \(K_t\) invariant. Given any positive definite quadratic form \(Q\), normalize it so \(1\le Q(x)\le d^2\) for all \(x\in\partial K_t\), with \(d^2=M_Q/m_Q\). Average \(Q\) over the six coordinate permutations. The average remains positive definite and satisfies the same pointwise inequalities, hence gives distortion at most \(d\). The permutation-invariant quadratic forms are exactly the positive multiples of

\[q_r(x)=\sum_{i=1}^3(x_i-\bar x)^2+3r\bar x^2,\qquad \bar x=\frac{x_1+x_2+x_3}{3},\quad r>0.\]

Thus optimizing over the scalar \(r>0\) loses no generality, including no nonsymmetric linear maps.

**2. Maximum of the quadratic form.** A vertex of \(K_t\) must have a saturated coordinate inequality: if all \(|x_i|<1\), a small common translation in the \((1,1,1)\) direction preserves feasibility, preventing extremality. On the face \(x_i=1\), the remaining two coordinates independently range over \([1-t,1]\); this is a square. Its four corners, and the negatives, therefore give all fourteen vertices:

\[(1,1,1),\quad\text{permutations of }(1,1,1-t),\quad\text{permutations of }(1,1-t,1-t),\]

and their negatives (with coincident occurrences counted once). Since \(q_r\) is convex, its maximum is attained at a vertex. The second nonconstant type has the same variance as the first but a smaller absolute mean for \(0<t\le1\), and therefore cannot exceed the first. Hence

\[M(r):=\max_{x\in K_t}q_r(x)=\max\!\left\{3r,\ \frac{2t^2}{3}+\frac{(3-t)^2}{3}r\right\}.\]

The two expressions cross at \(r_c=2t/(6-t)\).

**3. Minimum on the boundary.** The boundary is the union of the active coordinate facets \(|x_i|=1\) and pair-difference facets \(|x_i-x_j|=t\). On any pair-difference facet, the elementary inequality

\[\sum_{i=1}^3(x_i-\bar x)^2\ge\frac{(x_i-x_j)^2}{2}\]

shows \(q_r(x)\ge t^2/2\). Equality occurs at \(x=(t/2,-t/2,0)\), which belongs to \(\partial K_t\), giving the exact pair-facet minimum \(t^2/2\).

On the coordinate facet \(x_1=1\), convexity and the symmetry interchanging the other two coordinates reduce the minimum to vectors \((1,s,s)\) with \(1-t\le s\le1\). There

\[q_r(1,s,s)=\frac23(1-s)^2+\frac r3(1+2s)^2.\]

The unrestricted minimizer is \(s=(1-r)/(1+2r)\). It lies in the permitted interval exactly when \(r\le r_a=t/(3-2t)\). Thus the coordinate-facet minimum is \(3r/(1+2r)\) up to \(r_a\), and afterward is \(2t^2/3+r(3-2t)^2/3\). The latter is strictly greater than \(t^2/2\), and the former first equals \(t^2/2\) at

\[r_0=\frac{t^2}{2(3-t^2)}<r_a.\]

Consequently, for all \(r>0\),

\[m(r):=\min_{x\in\partial K_t}q_r(x)=\min\!\left\{\frac{3r}{1+2r},\frac{t^2}{2}\right\}.\]

**4. Sharp optimization.** The inequalities \(0<r_0<r_c\) and \(r_0\le t/4<t/3\), valid throughout \(0<t\le1\), imply that for \(0<r\le r_0\), with \(A=2t^2/3\) and \(B=(3-t)^2/3\),

\[\frac{M(r)}{m(r)}=\frac{(A+Br)(1+2r)}{3r},\qquad\frac{d}{dr}\frac{M(r)}{m(r)}=-\frac{A}{3r^2}+\frac{2B}{3}<0.\]

Indeed \(B\le3\) and \(r\le r_0<t/3\) make the derivative negative. For \(r\ge r_0\), the denominator is the constant \(t^2/2\) and the numerator is the maximum of two strictly increasing linear functions, so the quotient increases. Therefore \(r_0\) is the unique optimum. Substitution yields

\[\frac{M(r_0)}{m(r_0)}=\frac{4}{3}+\frac{(3-t)^2}{3(3-t^2)}=\boxed{\frac{7-2t-t^2}{3-t^2}}.\]

The derivative of the final expression is \(-2(t-3)(t-1)/(3-t^2)^2<0\) for \(0<t<1\). This proves the theorem, including its boundary values and optimum quadratic form.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library and exact rational arithmetic. It constructs all twelve defining inequalities and enumerates all independent triples of supporting planes, thereby recovering all fourteen vertices for nine rational parameters. It evaluates the proposed extremal quadratic form and six positive perturbations of its symmetry parameter at each parameter value. The output ends in `ALL_EXACT_CHECKS_PASS`. These finitely many checks do not substitute for the universal proof above.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii (2018, Section 2) prove uniform isomorphism bounds for free spaces on finite ultrametrics relative to \(\ell_1\), without this exact Hilbert-distance profile. Alexander, Fradelizi, García-Lirola and Zvavitch (2019, Sections 2--5) develop the finite-metric polytope, graph-isometry and volume-product frameworks, not an exact Hilbert optimization for this family. Kobos and Varivoda (2023) calculate cube--cross-polytope Banach--Mazur distances, while Grundbacher and Kobos (2026) give distances for \(\ell_p\)-direct sums and certain cone constructions. This theorem instead treats a fourteen-vertex three-dimensional Lipschitz ball with coupled coordinate-difference constraints, and supplies its exact minimization in that family.

## Limitations

This theorem covers only real scalars, exactly four metric points and three equal small distances. The degenerate case \(t=0\) is excluded; the limit is a limit of three-dimensional normed spaces, not the distortion of a four-point metric at zero. No classification of arbitrary four-point ultrametrics with unequal small distances, complex scalar spaces or general higher-dimensional ultrametrics is claimed. Finite calculations are corroboration, not an infinite proof.

## References

1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (first posted 10 July 2018), especially Section 2.
2. M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first posted 24 November 2019), Sections 2--5.
3. T. Kobos and M. Varivoda, *On the Banach--Mazur Distance in Small Dimensions*, arXiv:2305.06427 (first posted 10 May 2023).
4. F. Grundbacher and T. Kobos, *Exact Banach--Mazur distances of certain \(\ell_p\)-sums and cones*, arXiv:2603.18268 (first posted 18 March 2026).
