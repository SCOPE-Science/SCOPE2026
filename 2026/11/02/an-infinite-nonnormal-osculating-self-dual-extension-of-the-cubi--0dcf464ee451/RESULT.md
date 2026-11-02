# An infinite nonnormal osculating-self-dual extension of the cubic Togliatti surface

## Finding
For each integer \(d\ge3\) over \(\mathbb C\), let \(X_d\subset\mathbb P^5\) be the closure of the image of
\[
\Phi_d:[x:y:z]\dashrightarrow[x^{d-1}y:x^{d-1}z:xy^{d-1}:y^{d-1}z:xz^{d-1}:yz^{d-1}].
\]
The following assertions hold simultaneously.

1. The normalization is the smooth degree-six del Pezzo surface \(S=\operatorname{Bl}_{p_1,p_2,p_3}\mathbb P^2\) at the three coordinate points. The finite birational normalization morphism is induced by six base-point-free sections of the ample class \(L=dH-E_1-E_2-E_3\). The degree of \(X_d\) is \(d^2-3\).
2. At a general point the second-osculating projective space has dimension four, a unique hyperplane. The surface of second-osculating hyperplanes is projectively equivalent to \(X_d\), for *every* \(d\ge3\).
3. \(X_3\) is the classical smooth toric cubic Togliatti surface. For all \(d\ge4\), the nonnormal locus of \(X_d\) is exactly its six torus-invariant boundary coordinate lines, which form a hexagon. Along each of the three boundary lines arising from polygon edges of length \(d-2\), the normalization is generically a degree-\(d-2\) cover. Along each of the other three edges, of length one, the normalization is generically birational, but the transverse completed local ring over the rational function field \(K=\mathbb C(t)\) is \(K[[s^{d-2},s^{d-1}]]\). Its transverse \(\delta\)-invariant equals \((d-3)(d-2)/2\).
4. The osculating hyperplane at the torus point \(\Phi_d([1:1:1])\) pulls back to the plane curve
\[
 -(x-y)(x-z)(y-z)h_{d-3}(x,y,z)=0,
 \qquad h_m(x,y,z)=\sum_{i+j+k=m}x^iy^jz^k.
\]
In particular, the classical three-line contact is the first member of an infinite sequence with a symmetric residual contact curve of degree \(d-3\).

## Assumptions and scope
All schemes and morphisms are defined over \(\mathbb C\). The integer \(d\) is arbitrary with \(d\ge3\). The six homogeneous coordinates in the displayed order matter for the signs below. \(S\) is the toric blow-up at the *coordinate* points, and \(X_d\) is the reduced scheme-theoretic closure of the indicated image. A statement about generic transverse local rings is made over the function field of a boundary line; it is not a classification of special points where boundary components meet. Here second-osculating means derivatives of affine order at most two, giving a projective linear span.

## Proof
**The normalization and degree.** On the dense torus, set \(z=1\); the six exponent vectors in the stated coordinate order are
\[
(d-1,1),\ (d-1,0),\ (1,d-1),\ (0,d-1),\ (1,0),\ (0,1).
\]
Their differences generate \(\mathbb Z^2\): among the differences of the first pair is \((0,1)\), and among the appropriate last pairs and first differences is a primitive horizontal vector. Explicitly, the difference between \((1,0)\) and \((0,1)\) is \((1,-1)\), so these two differences generate the lattice. Hence \(\Phi_d\) is injective on the dense torus. The convex hull is the hexagon with cyclic vertices
\[
(0,1),(1,0),(d-1,0),(d-1,1),(1,d-1),(0,d-1),
\]
whose successive integral edge lengths are \(1,d-2,1,d-2,1,d-2\). Its normalized area, by the shoelace formula, is \(d^2-3\).

The six forms all vanish to order at least one at each coordinate point, and their leading terms there give a base-point-free system after one blow-up. There are no other base points. The strict transforms of the three coordinate lines have \(L\)-degree \(d-2\), while the exceptional curves have \(L\)-degree one. Consequently the toric divisor \(L\) is ample for \(d\ge3\), by the toric ampleness criterion (equivalently, all six polygon edge lengths are positive). The resulting morphism \(S\to X_d\) is finite because it pulls back \(\mathcal O_{\mathbb P^5}(1)\) to an ample bundle, and birational because of torus injectivity. Since \(S\) is normal it is the normalization. Intersection theory gives \(\deg X_d=L^2=d^2-3\).

**Osculating hyperplane.** On the torus, let \(u=x/z\) and \(v=y/z\), so the parametrization is the six monomials \(u^{a_i}v^{b_i}\) with the exponents above. Let \(J_d\) be the six-by-six second jet matrix, whose rows correspond to \(1,a,b,\tfrac12 a(a-1),ab,\tfrac12 b(b-1)\). The column vector
\[
 c=(-1,1,1,-1,-1,1)^\mathsf T
\]
lies in its kernel, for *every* \(d\), by direct substitution. Moreover the minor with rows \(1,a,b,\tfrac12a(a-1),ab\) and columns numbered \(1,2,3,5,6\) has absolute value \((d-2)^2(d-1)^2/2\), nonzero for \(d\ge3\). Thus the jet matrix has rank five. At \((u,v)=(\alpha,\beta)\) the unique hyperplane has homogeneous coefficients \(c_i\alpha^{-a_i}\beta^{-b_i}\); its image as a point in dual projective space is obtained from \(\Phi_d(\alpha^{-1},\beta^{-1})\) by the fixed diagonal transformation \(\operatorname{diag}(c_1,\ldots,c_6)\). This proves osculating self-duality, not merely dimension defect.

**Nonnormality at all six boundary lines.** A normal toric surface has strata indexed by the faces of its polytope. The normalization just established is an isomorphism over the dense torus. For a one-dimensional polygon edge, the function-field degree of the map between the corresponding one-dimensional boundary orbits equals the index in the edge lattice generated by differences of the exponent points lying on the edge. Only the endpoints are among our six exponent points. On each of the three edges of length \(d-2\), this index is \(d-2\), so for \(d\ge4\) the map has generic degree greater than one; the image is nonnormal there.

For a short edge, say the right edge with \(a=d-1\), its two exponent points differ by a primitive vector, so the edge function field is \(K=\mathbb C(t)\). Relative to that edge the other four monomials have inward valuations \(d-2\) or \(d-1\); both are attained, and after extending to \(K\) the generated transverse local algebra is exactly \(K[s^{d-2},s^{d-1}]_{(s^{d-2},s^{d-1})}\). The completed ring is \(K[[s^{d-2},s^{d-1}]]\). For \(d\ge4\), it is nonnormal, because \(s\) is integral but absent, and its \(\delta\)-invariant is the number of gaps of the semigroup generated by coprime consecutive positive integers \(d-2,d-1\), namely \((d-3)(d-2)/2\). The other short edges are symmetric. Every nonnormal point must lie on one of the six image boundary lines since the torus part is normal; since the nonnormal locus is closed and contains the generic point of each line, it equals their union. At \(d=3\), all edges have primitive length one and their vertex semigroups are free unimodular cones; the monomial model coincides with the classical smooth cubic Togliatti embedding.

**Contact divisor.** Substitute the signed jet-kernel coefficients at \((1,1)\) into the six homogeneous monomials to get
\[
F_d=-x^{d-1}y+x^{d-1}z+xy^{d-1}-y^{d-1}z-xz^{d-1}+yz^{d-1}.
\]
It is the alternant \(\det\!\begin{psmallmatrix}1&x&x^{d-1}\\1&y&y^{d-1}\\1&z&z^{d-1}\end{psmallmatrix}\), with a consistent choice of column ordering. Dividing this alternant by the Vandermonde factor \((x-y)(x-z)(y-z)\) yields the one-row Schur polynomial \(h_{d-3}\) (the bialternant formula, or induction using \(h_m\)'s generating function \(\prod_{t\in\{x,y,z\}}(1-tT)^{-1}\)). Therefore \(F_d=-(x-y)(x-z)(y-z)h_{d-3}\) as a polynomial identity for all integers \(d\ge3\). This proves the divisor assertion.

## Verification
The accompanying `verify.py` checks the symbolic second-jet kernel and a nonzero symbolic minor for arbitrary parameter \(d\), plus exact polynomial contact factorizations and polygon identities for degrees \(3\) through \(13\). It separately checks the numerical semigroup gap formula on those samples. The complete arbitrary-degree proof is the algebraic argument above, not the finite sample of degrees. 

## Relationship to prior work
The case \(d=3\) is the classical smooth Togliatti example, not a new construction. Vallès (2006) and Mezzetti–Miró-Roig–Ottaviani (2011/2012) study Togliatti-type osculation and the cubic monomial example; the latter also proves general statements about order-\((d-1)\) rather than *fixed second-order* osculation. Mulliken's 1995 thesis treats many affine monomial osculating self-dual varieties by exponent configurations, and Lvovski (2016) gives broad projective osculating self-duality constructions. The stated new candidate is the uniform six-coordinate series with its explicit alternating nonnormal boundary behavior and residual contact factor, not a claim that osculating self-duality or toric normalization is novel. A different toric exposition or a specialization of broad self-duality results could subsume portions of this work; historical priority requires external assessment.

## Limitations
Only the torus-generic local singularity type on each of the six boundary lines is classified; special points at their intersections are not. No assertion is made that the residual contact curve \(h_{d-3}=0\) is irreducible, or that its singularities are classified, for arbitrary \(d\). These embedded models do not classify arbitrary Togliatti systems or all osculating-self-dual surfaces. The sources located provide strong relevant background, but an equivalently explicit earlier family might exist under other toric coordinates. Independent validation and a comprehensive historical-priority audit have not been performed.

## References
- Jean Vallès, *Variétés de type Togliatti*, C. R. Math. Acad. Sci. Paris 343 (2006), 411–414, doi:10.1016/j.crma.2006.08.004.
- E. Mezzetti, R. Miró-Roig and G. Ottaviani, *Laplace equations and the weak Lefschetz property*, arXiv:1110.5239 (2011), Canad. J. Math. (2012).
- Serge Lvovski, *Some remarks on osculating self-dual varieties*, arXiv:1602.07450 (2016).
- John C. Mulliken, *Lotsa Dots: Self-Dual Affine Monomial Varieties*, Reed College thesis, May 1995.
