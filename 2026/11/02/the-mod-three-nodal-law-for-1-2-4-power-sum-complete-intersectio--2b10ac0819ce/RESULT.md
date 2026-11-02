# The mod-three nodal law for \((1,2,4)\) power-sum complete intersections

## Finding
For each integer \(n\ge4\), let \(p_d=\sum_{i=1}^{n}x_i^d\) and consider the projective scheme
\[
X_n=V(p_1,p_2,p_4)\subset\mathbb P^{n-1}_{\mathbb C}.
\]
Then \(X_n\) is a complete intersection of multidegree \((1,2,4)\), degree \(8\), and dimension \(n-4\). It is smooth if and only if \(3\nmid n\). For \(n=3a\ge6\), its singular locus consists of exactly
\[
N_n=\frac{n!}{3(a!)^3}
\]
distinct ordinary quadratic double points. Each such point is represented, up to coordinate permutation, by
\[
[\underbrace{1,\ldots,1}_{a},\underbrace{\omega,\ldots,\omega}_{a},
\underbrace{\omega^2,\ldots,\omega^2}_{a}],\qquad \omega^2+\omega+1=0.
\]
In particular, the numbers of nodes for \(n=6,9,12,15\) are respectively \(30,560,11550,252252\). Every node contributes local Milnor number one; hence the total Milnor number is \(N_n\) in the singular cases.

## Assumptions and scope
The base field is \(\mathbb C\), with ordinary projective space and the scheme structure from the three homogeneous power sums. We take \(n\ge4\). An ordinary quadratic double point means an isolated hypersurface singularity on the smooth local codimension-two section \(V(p_1,p_2)\) whose quadratic term is nondegenerate in the local projective tangent coordinates. All assertions about higher-dimensional varieties and numbers of singular points are exact, not generic-coefficient statements.

## Proof
**1. Regular sequence and degree.** On the hyperplane \(p_1=0\), the quadratic form \(p_2\) is nondegenerate: a vector in its radical must be proportional to \((1,\ldots,1)\), and cannot also satisfy \(p_1=0\) unless it is zero. Since \(n\ge4\), its projective quadric \(Q=V(p_1,p_2)\) is smooth and irreducible. The quartic \(p_4\) does not vanish identically on \(Q\): the vector \((1,-1,i,-i,0,\ldots,0)\) satisfies \(p_1=p_2=0\) but has \(p_4=4\). Therefore the three forms form a regular sequence, so \(X_n\) has the stated dimension and degree.

**2. Jacobian rank and possible coordinate values.** At a projective point of \(X_n\), the Jacobian rows, up to nonzero constants, are
\[
(1,\ldots,1),\quad(x_1,\ldots,x_n),\quad(x_1^3,\ldots,x_n^3).
\]
The first two rows are linearly independent: otherwise all coordinates are equal, and \(p_1=0\) would force the zero vector. Thus the point is singular exactly when there exist \(A,B\in\mathbb C\) with \(x_i^3=A x_i+B\) for every \(i\). Its coordinates consequently take at most three values. One value is impossible by \(p_1=0\). If two distinct values \(u,v\) have positive integer multiplicities \(a,b\), the equalities \(au+bv=au^2+bv^2=0\) imply \(u=v=0\), also impossible.

**3. Three values and a positivity obstruction.** Suppose there are three distinct values \(u,v,w\), of positive multiplicities \(a,b,c\). Because these are the roots of the monic depressed cubic \(T^3-AT-B\), one has \(u+v+w=0\). Together with \(au+bv+cw=0\), this forces either \(a=b=c\) or
\[
(u,v,w)=\lambda(b-c,c-a,a-b)
\]
for a nonzero \(\lambda\in\mathbb C\). In the latter case the condition \(au^2+bv^2+cw^2=0\) becomes
\[
\lambda^2\bigl(a(b-c)^2+b(c-a)^2+c(a-b)^2\bigr)=0.
\]
The parenthesized integer is strictly positive when the positive integers \(a,b,c\) are not all equal. Hence \(a=b=c\), and \(n=3a\). Now \(u+v+w=u^2+v^2+w^2=0\) implies \(uv+uw+vw=0\), so the three distinct nonzero values are proportional to the cubic roots of unity \((1,\omega,\omega^2)\). They indeed satisfy \(p_4=0\), because \(1+\omega^4+(\omega^2)^4=0\). This exhausts all singular points, showing smoothness when \(3\nmid n\).

**4. Projective orbit count.** There are \(n!/(a!)^3\) assignments of the three ordered values to the \(n\) coordinates. Multiplying all coordinates by \(\omega\) cyclically permutes the three values without changing the projective point; this free threefold identification is the only scalar identification. Thus there are exactly \(N_n=n!/[3(a!)^3]\) distinct projective singular points.

**5. Nondegenerate local quadratic terms.** Scale one singular point so that all coordinates \(x_i^3=1\). On the smooth affine cone of \(Q\), the tangent subspace is
\[
W=\{v\in\mathbb C^n:\ \sum_i v_i=\sum_i x_i v_i=0\}.
\]
The differential of \(p_4\) equals \(4\,dp_1\) at this point. Hence its constrained Hessian on \(W\) is the form \(12\sum_i x_i^2v_i^2\). If \(v\) is in the radical of the associated bilinear form on \(W\), then the vector \((x_i^2v_i)_i\) lies in \(\operatorname{span}\{(1)_i,(x_i)_i\}\). As \(x_i^3=1\), this means \(v_i=A x_i+B x_i^2\). The condition \(\sum_i x_i v_i=0\) gives \(B\sum_i x_i^3=Bn=0\), hence \(B=0\). Therefore the radical is exactly the radial line \(\mathbb C x\). Passing to the projective tangent space \(W/\mathbb C x\) yields a nondegenerate quadratic form of rank \(n-3\). Thus every singular point is an ordinary quadratic double point on the dimension-\(n-4\) complete intersection.

## Verification
The standalone standard-library script `verify.py` can be run with `python3 verify.py`. It independently enumerates projective coordinate-label orbits for \(n=6,9,12\), checks the node-count formula for \(n=6,9,12,15\), verifies Hessian ranks over the finite field of size \(1009\) at representatives in five sizes \(n=6,9,12,15,18\), and checks the positive-integer multiplicity obstruction for \(4\le n\le31\). It prints a `VERIFY_OK` line. These checks provide reproducibility and consistency evidence; the characteristic-zero proof above is what establishes the unlimited-dimensional statement.

## Relationship to prior work
Giménez, Gottig, Palacios, Pérez, and Privitelli (2026) investigate general power-sum varieties, with complete-intersection and singular-locus *dimension* estimates over finite fields. Conca, Singh, and Soundararajan (2025), particularly Theorem 2.3, establish complete-intersection, normality, and factoriality results for general collections of power sums in characteristic zero. Neither source's inspected statements determine the exact singular points, the mod-three smoothness criterion, or the all-dimensional nodal counts here.

The size-six orbit of \(30\) points is **not new as a coordinate configuration**: Beauville (2013), citing earlier work, explicitly records this orbit as the node set of generic \(S_6\)-invariant quartic threefolds. The subject here is a different complete-intersection scheme, and the contribution beyond that familiar low-dimensional orbit is the complete classification for every number of variables, including new higher-dimensional numerical cases. Melánová, Sturmfels, and Winter (2021) study fibers and solutions of power-sum maps but do not assert this precise special-fiber singularity theorem in the inspected material.

## Limitations
Only the exponent pattern \((1,2,4)\), the zero fiber, and characteristic zero are covered. The theorem is about singular support and analytic node type, not the general behavior of arbitrary fibers or fields of positive characteristic. Its finite checks cannot independently certify all dimensions. The historical literature on symmetric quartic hypersurfaces may encode some higher-dimensional special cases implicitly; the precise literature priority remains conditional on fuller specialist comparison. Independent mathematical validation has not been performed.

## References
1. N. Giménez, J. F. Gottig, M. Palacios, M. Pérez, M. Privitelli, *Power Sum Varieties over Finite Fields* (2026), arXiv:2610.32056v1, first publicly posted 2026-10-23. https://arxiv.org/abs/2610.32056
2. A. Conca, A. K. Singh, K. Soundararajan, *Ideals Generated by Power Sums*, Rev. Roumaine Math. Pures Appl. 70 (2025), 49–71, Theorem 2.3. https://www.math.utah.edu/~singh/publications/conca_singh_soundararajan.pdf
3. H. Melánová, B. Sturmfels, R. Winter, *Recovery from Power Sums* (2021), arXiv:2106.13981. https://arxiv.org/abs/2106.13981
4. A. Beauville, *Non-rationality of the \(S_6\)-symmetric quartic threefolds*, Rend. Sem. Mat. Univ. Politec. Torino 71 (2013), 385–388, p. 385. https://seminariomatematico.polito.it/rendiconti/71-34/0.pdf#page=116
