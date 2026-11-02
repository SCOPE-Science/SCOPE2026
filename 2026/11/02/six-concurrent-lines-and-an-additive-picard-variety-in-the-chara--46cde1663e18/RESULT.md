# Six concurrent lines and an additive Picard variety in the characteristic-five Bring complete intersection

## Finding

Let \(k\) be an algebraically closed field of characteristic \(5\), and let \(B\subset\mathbf P^4_k\) be the projective scheme cut out by the three elementary power-sum equations
\[
\sum_{i=1}^5 X_i=\sum_{i=1}^5 X_i^2=\sum_{i=1}^5 X_i^3=0.
\]
The scheme \(B\) is reduced and is the union of exactly six distinct projective lines over \(\mathbf F_5\). All six pass through \(P=[1:1:1:1:1]\), and no other point lies on two components. The \(S_5\)-action on the six components is transitive, with stabilizer \(\operatorname{AGL}_1(\mathbf F_5)\), of order \(20\).

The only singularity is \(P\). Its six-branch completed local ring has normalization \(\prod_{i=1}^6 k[[t_i]]\), conductor \(\prod_{i=1}^6(t_i^3)\), and delta invariant \(9\). Consequently the connected degree-zero Picard scheme is the split, four-dimensional additive group
\[
\operatorname{Pic}^0(B)\cong\mathbf G_a^4.
\]
The arithmetic genus is \(4\). These assertions concern the literal reduction of the displayed integral complete-intersection model, not the stable reduction or Jacobian of a smooth model after a ramified base change.

## Assumptions and scope

The base field is algebraically closed of characteristic exactly \(5\). The integral model is specified by its three power sums in \(\mathbf P^4\); different integral models of the characteristic-zero Bring curve may have different special fibers. A line component is a reduced projective line over \(k\), and the six-branch local invariant is computed using the ordinary normalization of the reduced curve. The symbol \(\operatorname{Pic}^0\) denotes the identity component of the Picard scheme of this reduced, connected, projective curve.

## Proof

**1. Equations become a projective cone.** Set \(X_5=z\) and \(X_i=z+u_i\) for \(1\le i\le4\). In characteristic five the first equation becomes \(\sum_{i=1}^4u_i=0\). Write \(u_1=u\), \(u_2=v\), \(u_3=w\), and \(u_4=-u-v-w\). Define the homogeneous forms
\[
q_2=u^2+v^2+w^2+(u+v+w)^2,
\quad
q_3=u^3+v^3+w^3-(u+v+w)^3.
\]
The second power sum is \(q_2\), while the third is \(3zq_2+q_3\). Hence \(B\subset\mathbf P^3_{[z:u:v:w]}\) is cut out scheme-theoretically by \(q_2=q_3=0\). These equations are independent of \(z\), so \(B\) is the projective cone with vertex \([1:0:0:0]\) over the finite subscheme \(Z=V(q_2,q_3)\subset\mathbf P^2\).

**2. Six distinct geometric directions.** For every permutation \((a_1,\ldots,a_5)\) of the five elements of \(\mathbf F_5\), the sums of its first, second, and third powers are zero. Thus the point
\[
[a_1-a_5:a_2-a_5:a_3-a_5]\in\mathbf P^2(\mathbf F_5)
\]
solves \(q_2=q_3=0\). Two such permutations produce the same projective point precisely when their five entries are related by one affine transformation \(a\mapsto ca+d\) with \(c\in\mathbf F_5^\times\) and \(d\in\mathbf F_5\): the projective equality forces a common nonzero scaling of every difference from the fifth entry, and translation restores that entry. Each equivalence class has \(5\cdot4=20\) permutations, giving exactly \(5!/20=6\) distinct \(\mathbf F_5\)-points. This also identifies the stabilizer and proves transitivity of the permutation action.

The conic \(q_2=0\) is nonsingular: its polar symmetric matrix has diagonal entries \(4\), off-diagonal entries \(2\) in \(\mathbf F_5\), and nonzero determinant. The cubic \(q_3\) is not divisible by \(q_2\): its coefficients of \(u^3\), \(v^3\), \(w^3\) all vanish, whereas a product \(q_2(au+bv+cw)\) has corresponding coefficients \(2a,2b,2c\); also \(q_3\ne0\), for example at \((1,1,0)\). Therefore \(q_2\) and \(q_3\) have no common component. Bézout's theorem gives length \(\deg Z=2\cdot3=6\) over \(k\). The six constructed distinct points exhaust this length, and \(Z\) is reduced. It follows that \(B\) is exactly the stated union of six reduced lines, whose pairwise intersections are only their common vertex. Every other point is smooth.

**3. Local conductor and delta invariant.** In the affine chart \(z=1\) the completed local ring at the vertex is
\[
R=k[[u,v,w]]/(q_2,q_3).
\]
The normalization is \(\widetilde R=\prod_{j=1}^6 k[[t_j]]\), obtained by restricting polynomials to the six directions. Its homogeneous graded subring is the coordinate ring \(S=k[u,v,w]/(q_2,q_3)\). Since the two forms form a regular sequence of degrees \(2\) and \(3\),
\[
H_S(T)=\frac{(1-T^2)(1-T^3)}{(1-T)^3},
\]
and the dimensions of its graded pieces are \(1,3,5,6,6,\ldots\). Under evaluation on the six reduced points of \(Z\), the degree-\(d\) part embeds into \(k^6\) with exactly these ranks: this is the standard homogeneous coordinate ring realization on the six disjoint lines. For \(d\ge3\), evaluation is surjective. Hence
\[
\operatorname{length}_k(\widetilde R/R)
=(6-1)+(6-3)+(6-5)=9,
\]
with the differences coming from degrees \(0,1,2\). Surjectivity for every degree at least three shows that the conductor of \(R\) in \(\widetilde R\) is precisely \(\prod_{j=1}^6t_j^3k[[t_j]]\): no lower-degree element can lie in the conductor, because multiplying by arbitrary branch idempotents would require a full degree-\(0\), \(1\), or \(2\) evaluation fiber, where its image is proper; more concretely, the image at degree two is the hyperplane of quadratic evaluations, and no nonzero vector of that space remains inside it after all componentwise idempotent multiplications (the six points impose one relation with all six coefficients nonzero, as shown below). In degrees zero and one the same conclusion follows by multiplication to degree two. Thus the delta invariant is \(9\). As an independent check, the normalization has six genus-zero components and one singular point with six branches, giving \(p_a(B)=\delta-6+1=4\), the usual genus of a \((2,3)\) complete intersection in \(\mathbf P^3\).

For the conductor assertion in degree two, note that a smooth conic containing six distinct points has unique quadratic equation up to scalar. The unique dependence among their six quadratic evaluation functionals has no zero coefficient: if some coefficient vanished, five distinct points on a nonsingular conic would impose fewer than five independent conditions on conics, contradicting the fact that two conics without a common component meet in at most four points. Hence the degree-two evaluation image contains no individual coordinate vector. Consequently it contains no nonzero coordinatewise ideal of \(k^6\); this proves the stated conductor bound.

**4. The generalized Jacobian is split additive.** The normalization exact sequence of unit sheaves gives the identity component of \(\operatorname{Pic}(B)\) as the local unit discrepancy \(\widetilde R^\times/R^\times\) modulo the six independent constant scalings from the global units on the six normalization components. Constant scalings remove its toric part; what remains canonically as an algebraic group is
\[
\frac{1+\prod_{j=1}^6t_jk[[t_j]]}{1+\mathfrak m_R}.
\]
Both unit groups are trivial beyond the common conductor \(\prod_jt_j^3k[[t_j]]\). In characteristic \(5\), the truncated logarithm \(\log(1+s)=s-s^2/2\) is a polynomial group isomorphism from units congruent to one modulo the branch maximal ideals, modulo their cubes, to the corresponding additive spaces. The dimension of the quotient is the rank deficit of evaluation in degrees one and two:
\[
(6-3)+(6-5)=4.
\]
Thus \(\operatorname{Pic}^0(B)\cong\mathbf G_a^4\) as an algebraic group over \(k\). No multiplicative torus remains because all six components are joined at a single ordinary multi-branch support, and the constant scalar parameters are exhausted by global units on the normalization components.

## Verification

The included standalone standard-library Python program `verify.py` independently constructs all \(120\) permutations, checks that their projective directions have exactly six affine-equivalence classes, enumerates all \(\mathbf P^2(\mathbf F_5)\)-solutions of \(q_2=q_3=0\), tests nonsingularity of the quadratic form, and computes exact ranks of the evaluation matrices for degrees \(0\) through \(4\), obtaining \(1,3,5,6,6\). These are finite checks of explicit identities. Bézout, regular-sequence Hilbert series, normalization, and the algebraic-group logarithm supply the infinite/algebraic-closure statements; the finite enumeration alone would not suffice.

## Relationship to prior work

The characteristic-zero \(S_5\)-symmetric model and genus-four complex geometry are classical. Braden--Northover (2012), Section 1, displays the exact three power-sum equations and studies periods and related complex analytic models; it does not establish the characteristic-five special-fiber description. Braden--Disney-Hogg (first preprint 2022; published 2023/2024) treats the geometry, automorphisms, and quotient structure over characteristic zero, not the six-line fiber or its additive Picard scheme. A targeted comparison of known equivalent descriptions and mathematical database results did not locate the conjunction of the special-fiber decomposition, conductor, and Picard-group classification. Nevertheless, it may be implicitly derivable from a more general positive-characteristic compactification or from unpublished computations, and independent bibliographic priority is not certified.

## Limitations

This describes exactly the special fiber of the stated integral complete-intersection equations. It does **not** identify the stable model after extension, potential good reduction of the smooth generic fiber, the Néron model, or arithmetic invariants of other integral presentations. The six-line geometry and split additive Picard identity are proved for characteristic five over an algebraically closed field. The explicit comparison with existing published literature is limited to the inspected sources, so historical priority remains open to independent confirmation.

## References

- H. W. Braden and T. P. Northover, *Bring's Curve: its Period Matrix and the Vector of Riemann Constants*, arXiv:1206.6004v1 (first public 26 June 2012), SIGMA 8 (2012), 065. https://arxiv.org/abs/1206.6004 ; https://doi.org/10.3842/SIGMA.2012.065 .
- H. W. Braden and L. Disney-Hogg, *Bring's curve: old and new*, arXiv:2208.13692 (2022 preprint), European Journal of Mathematics 10 (2024), article 3. https://arxiv.org/abs/2208.13692 ; https://doi.org/10.1007/s40879-023-00706-0 .
- Standard classical results used: Bézout's theorem for plane curves; Hilbert series of a homogeneous regular sequence; normalization exact sequence for the Picard scheme of a reduced projective curve.
