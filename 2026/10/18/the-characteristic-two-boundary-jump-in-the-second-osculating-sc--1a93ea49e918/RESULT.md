# The characteristic-two boundary jump in the second-osculating scheme of the Togliatti del Pezzo projection

## Finding
Let \(Y_{\mathbb Z}\subset\mathbb P^5_{\mathbb Z}\) be the projective toric surface defined by the six oriented degree-three monomials
\[
[x:y:z]\dashrightarrow[x^2y:x^2z:xy^2:y^2z:xz^2:yz^2],
\]
with closure taken scheme-theoretically in the toric sense. Its hexagonal toric atlas is smooth over \(\mathbb Z\). Let \(L=\mathcal O_Y(1)\), and let
\[
j^2: \mathcal O_Y^{\oplus6}\longrightarrow\mathcal P^2_{Y/\mathbb Z}(L)
\]
be the relative principal-parts (Hasse 2-jet) map of the six coordinate sections. Write \(Z\) for the determinantal subscheme defined by its \(5\times5\) minors, i.e. the locus of second-jet rank at most four.

**Integral local structure.** Every toric vertex chart is isomorphic to \(\operatorname{Spec}\mathbb Z[u,v]\), and on each such chart the *entire determinantal ideal* is
\[
\boxed{I_5(j^2)=(2u^2,\ uv,\ 2v^2).}
\]
For every algebraically closed field \(k\), the generic rank of \(j^2_k\) is five, and the special fibers have a sharp dichotomy:

* If \(\operatorname{char}(k)\ne2\), then \(Z_k\) consists scheme-theoretically of the six torus fixed points, each with completed ideal \((u,v)^2\) and length three. Hence \(\operatorname{length}(Z_k)=18\). The jet ranks are five away from these six points and three at them.
* If \(\operatorname{char}(k)=2\), then \(Z_k\) is **exactly the reduced toric boundary**: a cycle of six projective lines meeting successively at six torus fixed points. Its local ideal at a vertex is \((uv)\), with rank three at the vertex, rank four at every other boundary point and rank five on the dense torus. This boundary has degree six, arithmetic genus one and Hilbert polynomial \(6d\) with respect to \(L\).

In particular the second-osculating rank-drop scheme is not flat over \(\operatorname{Spec}\mathbb Z\); its fiber jumps from six isolated length-three schemes to a reduced divisor in characteristic two.

## Assumptions and scope
The ground field is algebraically closed only for the global geometric description; the local determinantal identity holds over \(\mathbb Z\) and is valid after arbitrary base change. Here \(\mathcal P^2\) denotes principal parts of *order two*, so the rows use Taylor/Hasse coefficients rather than ordinary second derivatives; this distinction is necessary in characteristic two. The variety is the **degree-six del Pezzo monomial projection in \(\mathbb P^5\)**, not the unrelated nodal quintic sometimes called a Togliatti surface. The result concerns the determinantal 5-minor scheme of the relative second-jet map, not the singular scheme of \(Y\), which is smooth.

## Proof
The six exponent vectors of the displayed monomials form a smooth lattice hexagon. At the vertex corresponding to \(x^2y\), put \(u=z/y\), \(v=y/x\); the six normalized sections are
\[
(1,u,v,uv^2,u^2v,u^2v^2).
\]
Their ratios generate the chart ring \(\mathbb Z[u,v]\), which is an affine plane. Every other vertex chart is isomorphic by permuting \(x,y,z\). These six affines cover the projective toric closure. It follows directly that \(Y_{\mathbb Z}\) is a smooth relative toric surface, with boundary the six invariant lines.

In the row order \((0,0),(1,0),(0,1),(2,0),(1,1),(0,2)\), the Hasse-jet matrix is
\[
J(u,v)=\begin{pmatrix}
1&u&v&uv^2&u^2v&u^2v^2\\
0&1&0&v^2&2uv&2uv^2\\
0&0&1&2uv&u^2&2u^2v\\
0&0&0&0&v&v^2\\
0&0&0&2v&2u&4uv\\
0&0&0&u&0&u^2
\end{pmatrix}.
\]
The identity follows from \(H_{r,s}(u^av^b)=\binom ar\binom bs u^{a-r}v^{b-s}\), with zero whenever \(r>a\) or \(s>b\). Its full determinant is zero. Exactly 18 of its 36 maximal proper (size-five) minors are nonzero; each is a single monomial with signed coefficient one or two. Every minor lies in \((2u^2,uv,2v^2)\), and minors \(-2u^2\), \(-uv\), and \(-2v^2\) occur. Thus the determinantal ideal is **exactly** the boxed integral ideal, not merely its radical. The 36-minor enumeration can be reproduced without external packages using the supplied checker.

If \(2\) is invertible, this becomes \((u,v)^2\). Since each vertex chart contains only one torus fixed point at \(u=v=0\), globalizing over the six charts produces six disjoint length-three schemes. If \(2=0\), the ideal becomes \((uv)\), so on each chart it is exactly the reduced union of its two coordinate axes. The six charts glue those axes to the toric boundary cycle. The listed ranks follow by inspection of \(J\): at \((0,0)\) the first three rows span a rank-three subspace; over characteristic two, at a point with exactly one coordinate zero the matrix has rank four, while for \(uv\ne0\) a size-five minor \(-uv\) is nonzero. For odd characteristic the 5-minors vanish only at the six vertices, and rank there is again three.

Each boundary component is a line because setting one toric chart coordinate to zero leaves just two independent linear coordinate sections; adjacent components meet transversely at their common torus fixed point. Inclusion–exclusion for the six-line cycle gives \(\chi(\mathcal O_{Z_k}(d))=6(d+1)-6=6d\) in characteristic two. Therefore it has degree six and arithmetic genus one. In every odd characteristic the length is \(6\cdot3=18\). Different Hilbert polynomials prove the integral determinantal family is not flat.

## Verification
Run \(\texttt{python3 verify.py}\) from the package. The standalone Python standard-library script constructs all Hasse entries by integer binomial coefficients, computes all 36 size-five minors by the Leibniz determinant formula, checks the zero size-six determinant and 18 nonzero monomial minors, certifies the three displayed universal ideal generators and containment of every minor, and checks characteristic-two ranks \((3,4,4,5)\) at the four possible coordinate-support patterns. The script was executed successfully and reported \(\texttt{VERIFY_OK}\). This is a complete finite exact computation for the fixed six-section matrix; the six-chart transitivity and toric gluing are mathematical arguments, not inferred from finite-field sampling.

## Relationship to prior work
The six-monomial Togliatti del Pezzo projection and its defective generic second osculating space are classical. Perkinson's *Inflections of Toric Varieties* (2000), especially Example 2.4 and the general discussion of monomial Fitting ideals, studies exactly this hexagon over \(\mathbb C\), recording the fixed-point and boundary rank profiles in characteristic zero. Lanteri–Mallavibarrena (2001), Proposition 4.3, explicitly proves rank five away from the six vertices and rank three at them in the complex setting. Both prior results are fully credited here; the characteristic-zero support and ranks are **not** claimed as new. Vallès (2006) and Michałek–Miró-Roig (2013) provide related classical explanations and monomial-system classification.

The increment here is the exact *integral* rank-drop ideal and especially the characteristic-two scheme-theoretic degeneration to a reduced toric boundary divisor, with all three rank strata and its Hilbert polynomial. The complex computations do not state the positive-characteristic boundary jump; they must be replaced by Hasse jets rather than naively reducing ordinary derivatives. No checked cited source supplies this integral identity or the characteristic-two boundary theorem.

## Limitations
The finding does not classify other Togliatti systems, other jet orders, or deformations of the embedding. The full general theory of toric jets, notably Perkinson's combinatorial Fitting-minor framework, contains tools from which related computations may be made. An implicit computation of the same local ideal in further literature cannot be ruled out, and no independent audit has been performed. The work does not assert that the original surface becomes singular in characteristic two: only the **osculating-rank degeneracy scheme** changes dimension.

## References
1. D. Perkinson, *Inflections of toric varieties*, Michigan Math. J. 48 (2000), 483–515, DOI 10.1307/mmj/1030132730. Full text: https://people.reed.edu/~davidp/homepage/publications/inflections.pdf. Particularly Example 2.4 and the Fitting-minor discussion.
2. A. Lanteri and R. Mallavibarrena, *Osculatory behavior and second dual varieties of Del Pezzo surfaces*, Adv. Geom. 1 (2001), 345–363, Proposition 4.3. Full text: https://paperzz.com/doc/7006127/osculatory-behavior-and-second-dual-varieties-of-del-pezzo.
3. J. Vallès, *Variétés de type Togliatti*, arXiv:math/0604023v1 (2006-04-03), https://arxiv.org/abs/math/0604023.
4. M. Michałek and R.-M. Miró-Roig, *Smooth monomial Togliatti systems of cubics*, arXiv:1310.2529v1 (2013-10-09), https://arxiv.org/abs/1310.2529.
5. D. Perkinson, *Principal parts of line bundles on toric varieties*, Compos. Math. 104 (1996), 27–39, https://www.numdam.org/item/CM_1996__104_1_27_0/.
