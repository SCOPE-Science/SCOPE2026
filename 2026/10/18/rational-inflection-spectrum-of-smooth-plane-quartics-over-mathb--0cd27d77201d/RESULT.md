# Rational inflection spectrum of smooth plane quartics over \(\mathbf F_3\)

## Finding
Let \(C_F\subset\mathbf P^2_{\mathbf F_3}\) be the zero locus of a nonzero ternary quartic \(F\), considered modulo multiplication by \(\mathbf F_3^\times\). Assume geometric smoothness. Denote by \(r(F)\) the number of \(\mathbf F_3\)-rational points where the tangent line has intersection multiplicity exactly \(3\) (an ordinary rational flex), and by \(h(F)\) the number where that multiplicity is exactly \(4\) (a rational hyperflex). Both counts are of **points**, not merely rational lines.

The complete joint distribution is:

| Ordinary rational flexes | Rational hyperflexes | Equations | Projective orbits |
|---:|---:|---:|---:|
| 0 | 0 | 989,820 | 204 |
| 0 | 1 | 481,104 | 105 |
| 0 | 2 | 81,432 | 20 |
| 0 | 3 | 2,808 | 1 |
| 0 | 4 | 468 | 2 |
| 1 | 0 | 965,952 | 172 |
| 1 | 1 | 353,808 | 67 |
| 1 | 2 | 56,160 | 10 |
| 1 | 4 | 1,872 | 1 |
| 2 | 0 | 665,496 | 125 |
| 2 | 1 | 185,328 | 36 |
| 2 | 2 | 2,808 | 1 |
| 3 | 0 | 202,176 | 36 |
| 3 | 1 | 35,568 | 7 |
| 4 | 0 | 64,584 | 14 |
| 4 | 1 | 9,360 | 3 |
| 6 | 1 | 936 | 1 |
| **All** | | **4,099,680** | **805** |


Thus \(r(F)+h(F)\leq7\), with equality for exactly \(936\) normalized quartic equations, all in one \(\operatorname{PGL}_3(\mathbf F_3)\)-orbit. The stabilizer of any maximizer has order \(6\). Every maximizer has exactly \(6\) ordinary rational flexes and \(1\) rational hyperflex, and its complete rational point set consists of those seven flexes. A representative is
\[
F(X,Y,Z)=X^3Y+2X^3Z+XZ^3+Y^4.
\]
The seven rational points lie on the reducible conic \(Y(X+Y)=0\), the union of two rational lines. At \([0:0:1]\) the tangent \(X=0\) has fourth-order contact, while at the remaining six rational points the contact is exactly third order.

## Assumptions and scope
The coefficient field is exactly \(\mathbf F_3\), and every nonzero quartic equation is identified with its two nonzero scalar multiples. A curve is **geometrically smooth** if it is nonsingular after extension to an algebraic closure. Projective equivalence means equivalence under \(\operatorname{PGL}_3(\mathbf F_3)\), not merely isomorphism over an algebraic closure. The asserted distribution counts equations and rational projective orbits separately, and says nothing about extension-field flexes or the geometric number of inflection points.

The quartic coefficient vector is encoded with fifteen monomials ordered by decreasing \(X\)-exponent and then decreasing \(Y\)-exponent. Its first nonzero coefficient is normalized to \(1\). The integer code is its base-three coefficient expansion in that order, with the first coefficient as the least significant ternary digit. For the displayed maximizer the code is `78753`.

## Proof
**Exhaustive projective domain.** The vector space of ternary quartics has dimension \(15\), so the number of normalized nonzero forms is
\[
(3^{15}-1)/2=7,174,453.
\]
The four substitutions swapping \(X,Y\), swapping \(Y,Z\), sending \(X\) to \(X+Y\), and sending \(X\) to \(2X\) generate \(\operatorname{GL}_3(\mathbf F_3)\) modulo scalar. Their projective image has order \(5616\). Applying them to every normalized equation, breadth-first orbit traversal partitions all \(7,174,453\) equations into exactly \(1,557\) orbits. The program records every orbit size and a representative, and its orbit-size sum independently equals the entire coefficient space.

**Exact geometric smoothness.** Let \(S_d\) be the degree-\(d\) homogeneous part of \(\mathbf F_3[X,Y,Z]\). Form the linear multiplication map
\[
S_4^{\oplus3}\longrightarrow S_7,\qquad(A,B,C)\longmapsto AF_X+BF_Y+CF_Z.
\]
The three partial derivatives are cubics. Their homogeneous ideal has no projective common zero if and only if this map is surjective (rank \(36=\dim S_7\)): if the derivatives have no projective zero, they form a homogeneous regular sequence of degrees \((3,3,3)\), whose Artinian quotient has socle degree \(6\); conversely surjectivity forces the projective zero locus to be empty. Euler's identity \(4F=XF_X+YF_Y+ZF_Z\), with \(4=1\) in characteristic three, shows that the partial derivatives have a projective common zero exactly when \(F=0\) has a geometric singularity. Gaussian elimination over \(\mathbf F_3\) thus supplies an exact smoothness test. Exactly \(805\) orbits, containing \(4,099,680\) normalized equations, pass.

**Exact rational contact.** There are exactly \(13\) projective rational points. For every rational point \(P\) on a smooth representative, its nonzero gradient defines the unique rational tangent line. Choose a different rational point \(Q\) on that tangent and expand the binary restriction
\[
F(P+sQ)=a_2s^2+a_3s^3+a_4s^4.
\]
The omitted constant and linear coefficients vanish because \(P\) lies on the curve and \(Q\) is tangent. The contact order is exactly \(3\) if \(a_2=0\) and \(a_3\ne0\); it is exactly \(4\) if \(a_2=a_3=0\). The \(a_j\) are computed from exact binomial expansions in \(\mathbf F_3\), not from a classical Hessian, which may degenerate in this characteristic. Smoothness and irreducibility rule out a tangent line contained in the curve. These tests are invariant under the group action, so the orbit sizes weight the entire joint table above.

**Extremal uniqueness and direct verification.** The only smooth orbit with seven rational flex points has representative code `78753` and size \(936\). Its stabilizer order is \(5616/936=6\). Independently of orbit reduction, a second program enumerates all \(7,174,453\) normalized coefficient vectors and identifies every equation with at least seven smooth-rational-point flex contacts. It finds \(6,097\) candidates (including singular curves); exact rank tests leave only \(936\) geometrically smooth candidates, each with six ordinary flexes and one hyperflex. No candidate has precisely eight contacts; forms with more than eight contacts exist but fail the geometric-smoothness test. The other candidates with at least seven contacts likewise fail geometric smoothness. This direct result equals the orbit-size total for the unique maximizer, thereby independently excluding further maximal orbits.

For the explicit maximizer, partial derivatives in characteristic three are \(F_X=Z^3\), \(F_Y=X^3+Y^3\), and \(F_Z=2X^3\); they have no projective common zero, proving smoothness directly. At \(X=0\), the equation forces \(Y=0\), yielding \([0:0:1]\). At \(X=1\), rational evaluation gives \(F(1,Y,Z)=Y(Y+1)\), so \(Y=0\) or \(Y=2\), with three choices of \(Z\) each. Direct tangent restriction gives fourth-order contact at \([0:0:1]\) and third-order contact at all six other points. Their union is the complete rational locus, the two-line conic \(Y(X+Y)=0\).

## Verification
All computational evidence is self-contained under `verify/` and `data/`. The reproducibility instructions in `REPRODUCE.md` compile the finite-field orbit enumerator, independently enumerate the extremal candidate space without quotienting, and cross-check each orbit's smoothness and contact counts using a separate implementation. The embedded output tables are generated from these source files and are required for the stated numerical claims. The independent direct candidate calculation and orbit-level cross-check were executed from the packaged relative paths and agreed exactly with the first census.

The checks are exhaustive **only for the specified finite coefficient space**; no sampling argument or field-uniform inference is used. The elementary smoothness proof of the displayed example does not depend on the census.

## Relationship to prior work
Oyono and Ritzenthaler (2010, Section 5, Proposition 3) show that characteristic-three flexes of a smooth plane quartic are supported on a conic, possibly degenerate; they also establish generic \(S_8\) flex monodromy. This supplies the relevant geometric context and makes the incidence of seven rational flexes on two rational lines natural. Their result does not state the seventeen-stratum \(\mathbf F_3\) distribution or classify its unique maximal orbit. Consequently the conic theorem and elementary finite-plane bounds are **not** presented here as new.

Costa, Harvey and Sutherland (first arXiv version 2022-08-21) develop point-counting and Cartier--Manin methods for smooth plane quartics; their computations do not provide rational contact-order distributions. Bergvall (2023) counts marked classical bitangent and level-two structures, which do not record ordinary inflection points of order three. Liang (2020) computes invariants and bitangents for certain cyclic quartic families over characteristic zero. A previously assembled finite-field census of rational bitangent versus hyperflex counts already determines the **hyperflex marginal** in our table, so that marginal is not claimed as new. The added ordinary-flex coordinate and its unique seven-flex projective orbit are the claimed refinement.

## Limitations
This is a computer-assisted finite classification. Although all loops and linear algebra are fully specified, the exhaustive counts rely on executing the included ordinary C++ verification programs rather than on a short hand enumeration. Independent external audit has not been performed. A previously unpublished or unindexed equivalent rational-flex table cannot be ruled out. The claim is not a statement about curves over larger fields or about geometric flexes over the algebraic closure.

## References
1. R. Oyono and C. Ritzenthaler, *On rationality of the intersection points of a line with a plane quartic*, arXiv:1006.0873v2 (2010), especially Section 5, Proposition 3. https://arxiv.org/abs/1006.0873
2. E. Costa, D. Harvey, and A. V. Sutherland, *Counting points on smooth plane quartics*, arXiv:2208.09890v1 (first posted 2022-08-21), *Research in Number Theory* **9** (2023), article 1. https://arxiv.org/abs/2208.09890
3. O. Bergvall, *Arithmetic and topology of classical structures associated with plane quartics*, *European Journal of Mathematics* **9** (2023), article 117, https://doi.org/10.1007/s40879-023-00711-3
4. D. Liang, *Invariants, bitangents, and matrix representations of plane quartics with 3-cyclic automorphisms*, *New York Journal of Mathematics* **26** (2020), 636--655, https://nyjm.albany.edu/j/2020/26-29p.pdf
