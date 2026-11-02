# The degree-24 Klein Hessian scheme has a length-21 specialization at characteristic seven

## Finding
Consider the integral Klein quartic \(F=X^3Y+Y^3Z+Z^3X\), and the primitive sextic \(H=X^5Z-5X^2Y^2Z^2+XY^5+YZ^5\), satisfying \(\det\operatorname{Hess}(F)=-54H\). The intersection \(\mathscr Z=V(F,H)\) over \(\mathbb Z_{(7)}\) is finite flat of degree \(24\). Its geometric generic fiber has 24 distinct classical inflection points. Its characteristic-seven fiber has exactly four geometric support points: the three coordinate vertices, each of local length one, and \(P=[1:2:4]\), of local length \(21\). The point \(P\) is the unique singular point of the reduced Klein quartic in characteristic seven.

## Assumptions and scope
All schemes are over the localization \(A=\mathbb Z_{(7)}\); the special-fiber statements remain true after any extension of its residue field to an algebraically closed field \(k\) of characteristic seven. Coordinates are homogeneous on \(\mathbf P_A^2\). The Hessian here is the *fixed primitive integral sextic*, not a putative intrinsic flex scheme on a singular special-fiber curve. At a singular point Hessian intersection multiplicity does not denote a smooth-curve inflection order. Lengths are scheme-theoretic intersection lengths. This statement concerns the specified integral model and does not classify arbitrary models.

## Proof
**Integral Hessian identity.** Direct differentiation of \(F\) and determinant expansion yields \(\det\operatorname{Hess}(F)=-54H\). Since \(54\) is invertible in \(A\), \(H\) defines the classical Hessian divisor and its special fiber correctly.

**Complete support.** In the affine chart \(X=1\), write \(y=Y/X,z=Z/X\). We have \(f=y+y^3z+z^3\) and \(h=z-5y^2z^2+y^5+yz^5\). Exact elimination over \(\mathbf F_7\) gives
\[
\operatorname{Res}_z(f,h)=-y(y-2)^{21}.
\]
This is a nonzero polynomial; therefore these two equations have no common curve component in this chart. For \(y=0\), their only common root is \(z=0\). For \(y=2\), the polynomial greatest common divisor has the sole root \(z=4\) (with multiplicity), so the support in \(X\ne0\) is \([1:0:0]\) and \([1:2:4]\). On \(X=0\), the restrictions \(F=Y^3Z\) and \(H=YZ^5\) show that the only common points are \([0:1:0]\) and \([0:0:1]\). Moreover, \(X=0\) is not itself a common component. Hence the projective special-fiber intersection has dimension zero.

**Lengths and flatness.** The total intersection length is \(4\cdot6=24\) by Bézout's theorem, since the equations have no common projective component. At each coordinate vertex, the differentials of \(F\) and \(H\) are independent modulo 7, so each is an intersection of length one. The only remaining point \(P\) therefore has local length \(24-3=21\). To prove the arithmetic assertion, note that \(F,H\) remain a regular sequence on every special-fiber local ring. The resulting relative complete intersection is flat over the DVR \(A\) by the local criterion for flatness: the special fiber has the required codimension two, and \(A\) is a nonzero divisor in the quotient. The projective morphism is proper, and the zero-dimensional special fiber implies it is quasi-finite in a neighborhood of the closed point; because the base is local and the generic fiber is zero dimensional as well (otherwise specialization gives a positive-dimensional special component), it is finite. Its degree is 24.

**Generic reducedness.** Over \(\mathbf Q\), the affine elimination resultant has degree 22 in \(y\) and is square-free, as certified by the exact Euclidean gcd with its derivative. It follows that the affine 22 points are distinct and reduced: the square-free resultant maps each root \(y\) to precisely one simple point of the finite intersection. The two points on \(X=0\) are independent transverse coordinate intersections. Therefore the generic fiber consists of 24 distinct points, the classical Klein inflection scheme.

**Uniqueness of the singular point.** In characteristic seven the partial derivatives are \(F_X=3X^2Y+Z^3\), \(F_Y=X^3+3Y^2Z\), and \(F_Z=Y^3+3Z^2X\). If any coordinate vanishes at a common zero of these derivatives, the other derivatives force all coordinates to vanish, impossible in projective space. Thus set \(X=1\). Then \(F_Y=0\) gives \(Z=2Y^{-2}\). Substitution into \(F_Z=0\) gives \(Y^7=2\). Over a field of characteristic seven this has the unique root \(Y=2\), and hence \(Z=4\). Direct substitution verifies that \(P\) lies on \(V(F)\) and all partial derivatives vanish. Thus it is the unique singular point.

## Verification
Run `python3 verify_flex.py` from the package directory. It uses exact SymPy rational/integer and finite-field polynomial arithmetic; it verifies the Hessian identity, the resultant identity, gcd support, coordinate-point transversality and the singularity equations. The checker does not substitute for the geometric intersection-theory or flatness arguments. Expected output: `KLEIN_FLEX_MOD7_21_AT_SINGULARITY_PLUS_3_SIMPLE_OK`.

## Relationship to prior work
Classical algebraic geometry gives 24 inflection points on a smooth plane quartic and the Klein equation. Janasz–Pokora–Zieliński's 2023 plane-quartic arrangement study concerns bitangents, not the integral Hessian intersection at characteristic seven. The plane-quartic reduction analysis in *Reduction of Plane Quartics and Cayley Octads* discusses the Klein curve's bad reduction, but its inspected discussion of reduction types (especially Section 7.2.1) does not identify the four-point Hessian fiber or local length 21. The characteristic-seven singular point itself is already known; the novel candidate is its scheme-theoretic multiplicity in the integral Hessian intersection and the complete specialization. Existing work on specialization of inflection tangents in characteristics different from seven likewise does not imply the singular-fiber length calculation.

## Limitations
No claim is made about intrinsic singular-fiber flexes, all arithmetic primes, a semistable model, individual lifting labels of 21 colliding points, or the local algebra isomorphism type at the length-21 point. Historical originality remains subject to unindexed classical or computational calculations. Independent mathematical audit has not been performed.

## References
1. M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514, first posted 2023-08-31.
2. *Reduction of Plane Quartics and Cayley Octads*, arXiv:2309.17381, first posted 2023-09-29; subsequently *Foundations of Computational Mathematics*, DOI:10.1007/s10208-025-09704-y, particularly Section 7.2.1.
3. F. Klein, *Ueber die Transformation siebenter Ordnung der elliptischen Functionen*, *Math. Ann.* 14 (1878), 428–471.
