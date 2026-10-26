# The minimum-degree ample-canonical member of a rational loop-fourfold class

## Finding

Among well-formed quasismooth six-variable loop hypersurfaces with exponents \(b_i\ge2\), primitive well-formed ambient weights, and determinant rationality condition \(d=|\det B|\), the least weighted degree for which \(d>\sum_{i=0}^{5}a_i\) is \(17279\). A witness is
\[
f=x_0^4x_1+x_1^6x_2+x_2^5x_3+x_3^6x_4+x_4^6x_5+x_5^4x_0
\]
in \(\mathbb P(3723,2387,2957,2494,2315,3389)\), of weighted degree \(d=17279\). Its weight sum is \(17265\), so \(K_X\sim_{\mathbb Q}14H\) is ample.

## Assumptions and scope

Work over \(\mathbb C\). Let \(H\) denote the ample hyperplane \(\mathbb Q\)-Cartier class restricted to \(X\). The exponent vector is \((b_0,\ldots,b_5)\in\mathbb Z_{\ge2}^{6}\). The loop exponent matrix \(B\) has diagonal entries \(b_i\) and cyclic next-column entries \(1\). The class under study consists of well-formed quasismooth hypersurfaces arising from tuples for which the primitive positive solution of \(B\mathbf a=d\mathbf 1\) gives a well-formed ambient weighted projective space, the least common denominator of the entries of \(B^{-1}\mathbf 1\) equals \(|\det B|\), and \(d>\sum_i a_i\). For the lower-bound search, ambient well-formedness alone is filtered, so the computation checks a superset of the target class; the witness itself is well-formed because its weights are pairwise coprime and the hypersurface meets the ambient singular locus only in finitely many coordinate points. The minimum is not asserted for chains, sums of loop atoms, other rationality constructions, or all rational weighted hypersurfaces.

## Proof

For six variables, the determinant expansion gives
\[
|\det B|=\prod_{i=0}^{5}b_i-1.
\]
For the displayed exponent vector, \(\prod_i b_i=17280\), hence \(d=17279\). The weights satisfy the six cyclic equations
\[
\begin{aligned}
4(3723)+2387&=17279,\\
6(2387)+2957&=17279,\\
5(2957)+2494&=17279,\\
6(2494)+2315&=17279,\\
6(2315)+3389&=17279,\\
4(3389)+3723&=17279.
\end{aligned}
\]
Their greatest common divisor is \(1\), they are pairwise coprime, and their sum is \(17265\). Thus the ambient weighted projective space is well-formed and the primitive weight vector has denominator \(d=|\det B|\).

The affine cone is smooth away from the origin. Indeed,
\[
\frac{\partial f}{\partial x_i}=b_i x_i^{b_i-1}x_{i+1}+x_{i-1}^{b_{i-1}},
\]
with cyclic indices. If one coordinate vanishes at a common zero of all partial derivatives, the equation for that coordinate forces the preceding coordinate to vanish, and iteration forces every coordinate to vanish. If all coordinates are nonzero, multiplying the six derivative equations forces \(\prod_i b_i=1\), contradicting \(\prod_i b_i=17280\). Hence the hypersurface is quasismooth. A reducible hypersurface cone would have intersecting components away from the origin, so quasismoothness also gives irreducibility. Since the ambient singular locus consists only of coordinate points and the hypersurface meets it in at most six points, the intersection has codimension four in \(X\); hence the hypersurface is well-formed.

Esser's determinant criterion for invertible Delsarte hypersurfaces applies: the loop matrix is invertible, the hypersurface is irreducible in a well-formed weighted projective space, and \(d=|\det B|\). Therefore \(X\) is rational. By adjunction,
\[
K_X\sim_{\mathbb Q}(d-\sum_i a_i)H=14H,
\]
so its canonical \(\mathbb Q\)-Cartier class is ample.

The example is not canonical. At the coordinate point of weight \(2315\), the local quotient type is \(\frac1{2315}(3723,2387,2957,2494)\). For the first group element, the Reid--Tai age is
\[
\frac{1408+72+642+179}{2315}=\frac{2301}{2315}<1.
\]
This explains why rationality is compatible here with an ample canonical class: the singularities are not canonical.

For minimality, any smaller degree in this class would have \(\prod_i b_i\le17279\). The supplied script exhaustively enumerates every exponent multiset with product at most \(17280\), every ordering after fixing a minimum exponent in the first position (a reduction by cyclic rotation), and filters by positive weights, primitivity, ambient well-formedness, and \(\sum_i a_i<d\). This is a superset search, so its lower bound also applies to the well-formed hypersurfaces in the claim. It checks \(537221\) normalized ordered tuples and finds no candidate of smaller degree than \(17279\); the displayed vector attains the bound.

## Verification

Run `python verify_minimum.py` from the artifact directory. The script uses exact integer arithmetic and asserts the degree equations, primitive and well-formed weights, the minimum-degree bound, and the noncanonical age calculation. Its recorded output is included in `VERIFICATION.md`. The finite search is complete for the stated class because any lower degree has exponent product below the witness product.

## Relationship to prior work

Esser's *Rational Weighted Projective Hypersurfaces* proves that an irreducible invertible Delsarte hypersurface in a well-formed weighted projective space is rational when its weighted degree equals the absolute determinant of its exponent matrix; the paper also notes that this construction can produce examples with ample canonical class. Those results imply rationality of the witness, but they do not state the minimum-degree result for six-variable loop polynomials. Hwang and Keum previously constructed singular rational surfaces with ample canonical divisor by a different method; their surface constructions do not classify this fourfold loop family.

## Limitations

The minimum is restricted to single six-variable loop polynomials with all exponents at least two and the determinant rationality criterion. It is not a minimum over all Delsarte polynomials, all weighted hypersurfaces, or all rational varieties. The example has a noncanonical quotient singularity; no terminality or canonicity claim is made. The literature search cannot rule out an unindexed prior table, and independent audit has not been performed.

## References

1. L. Esser, *Rational Weighted Projective Hypersurfaces*, arXiv:2409.01333v1 (first public version, 2024-09-02), especially §3.1 and Theorem 3.2.
2. D. Hwang and J. Keum, *Constructions of singular rational surfaces of Picard number one with ample canonical divisor*, arXiv:1007.1936 (2010).
