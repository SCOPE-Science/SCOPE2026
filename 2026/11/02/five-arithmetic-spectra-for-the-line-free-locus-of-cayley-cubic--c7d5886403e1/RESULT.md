# Five arithmetic spectra for the line-free locus of Cayley cubic twists

## Finding
Let \(k=\mathbb F_q\) have odd characteristic, and let \(E\) be any degree-four finite étale \(k\)-algebra. Write
\[
\operatorname{Nm}_{E/k}(t+z)
=t^4+e_1(z)t^3+e_2(z)t^2+e_3(z)t+e_4(z),
\]
and let \(X_E\subset\mathbb P(E)\) be the cubic surface \(e_3(z)=0\). Over an algebraic closure, \(X_E\) is Cayley's four-nodal cubic. Let \(U_E\) be the complement of **all nine geometric lines** on \(X_E\), equipped with its natural reduced open structure.

If \(\lambda\) is the partition of four consisting of degrees of the field factors of \(E\), then the exact numbers of rational points are:

| \(\lambda\) | \(\#U_E(\mathbb F_q)\) |
|:--|:--|
| \((1,1,1,1)\) | \((q-3)^2\) |
| \((2,1,1)\) | \(q^2-2q-1\) |
| \((2,2)\) | \((q-1)^2\) |
| \((3,1)\) | \(q^2\) |
| \((4)\) | \(q^2-1\) |

In particular, \(U_E(\mathbb F_q)\) is empty **if and only if** \(q=3\) and \(E\cong k^4\). All five cases occur over every odd finite field; in fact they exhaust all finite-field forms of Cayley's four-nodal cubic.

The complete zeta functions \(Z(U_E,T)=\exp(\sum_{n\ge1}\#U_E(\mathbb F_{q^n})T^n/n)\) are:

| \(\lambda\) | \(Z(U_E,T)\) |
|:--|:--|
| \((1,1,1,1)\) | \(\dfrac{(1-qT)^6}{(1-q^2T)(1-T)^9}\) |
| \((2,1,1)\) | \(\dfrac{(1-qT)^4(1+qT)^2}{(1-q^2T)(1-T)^4(1+T)^5}\) |
| \((2,2)\) | \(\dfrac{(1-qT)^4(1+qT)^2}{(1-q^2T)(1-T)^5(1+T)^4}\) |
| \((3,1)\) | \(\dfrac{(1-q^3T^3)^2}{(1-q^2T)(1-T^3)^3}\) |
| \((4)\) | \(\dfrac{(1-qT)^2(1+qT)^2(1+q^2T^2)}{(1-q^2T)(1-T)^2(1+T)^3(1+T^2)^2}\) |

The formulas hold over every finite extension of \(k\): to obtain \(\#U_E(\mathbb F_{q^n})\), replace the Frobenius permutation \(\sigma\) on the four embeddings of \(E\) by \(\sigma^n\), and replace \(q\) by \(q^n\) in the corresponding row of the first table.

## Assumptions and scope
Here finite étale means \(E\cong\prod_i\mathbb F_{q^{d_i}}\), where each \(d_i\) is positive and \(\sum_i d_i=4\). A geometric line means a projective line defined over an algebraic closure and contained in the geometric cubic surface, not necessarily individually defined over \(k\). The union of the nine lines is Galois-stable, so \(U_E\) descends canonically to \(k\). Every \(k\)-form of Cayley's cubic is isomorphic to some \(X_E\): its geometric automorphism group is \(S_4\), as proved below, and finite-field twists are classified by Frobenius conjugacy classes in that group. Odd characteristic is essential for the stated seven-line incidence structure; characteristic two is not included. Characteristic three is explicitly included.

## Proof
**1. The nine lines.** After extension to a separable closure, choose the four algebra embeddings of \(E\) and coordinates \(z_1,z_2,z_3,z_4\). The equation becomes
\[
\sum_{1\le i<j<k\le4}z_iz_jz_k=0.
\]
There are six edge lines, obtained by setting any chosen pair of coordinates to zero, and three pairing lines, indexed by the three partitions \(\{i,j\}\mid\{k,l\}\) of four indices into two pairs and given by \(z_i+z_j=z_k+z_l=0\).

These exhaust the lines. Any line contained in a coordinate hyperplane lies in a union of its three coordinate-edge lines, hence is one of them. Otherwise its four coordinate functions on a parameter \([s:t]\in\mathbb P^1\) are nonzero linear forms \(L_i\). Dividing the cubic identity by \(L_1L_2L_3L_4\) gives \(\sum_i1/L_i=0\) as a rational-function identity. At each pole of the distinct projective linear factors, cancellation requires at least two factors with the same zero. Four nonzero linear forms which are not all proportional therefore split into two proportional pairs. Cancellation in each pair forces their sum to be zero; this is one of the three pairing lines. This argument works over every odd characteristic, including three. The four coordinate vertices are the only singularities: where all coordinates are nonzero, the reciprocal expression has a nonvanishing derivative along the surface, and with exactly two coordinates nonzero one derivative is the product of those two; at each vertex the quadratic tangent cone is nondegenerate when \(2\) is invertible. Because the hyperplane bundle is anticanonical, every surface automorphism extends to a projective linear transformation. It must permute the four nodes. After a permutation, an automorphism fixing all nodes is diagonal, and equality of the four cubic monomial coefficients forces its four diagonal entries to be proportional. Thus the full geometric automorphism group is exactly \(S_4\). Standard Galois descent identifies its finite-field forms with the five quartic étale algebra types in the table.

**2. A birational inversion identifying the open surface.** The complement of the six edge lines has all four coordinates nonzero: setting one coordinate to zero in the defining cubic forces a second coordinate to vanish. In those coordinates, \(e_3(z)=\operatorname{Nm}(z)\operatorname{Tr}(z^{-1})\). Thus inversion \([z_i]\mapsto[y_i]=[z_i^{-1}]\) is an isomorphism between the coordinate-nonzero locus of \(X_E\) and the coordinate-nonzero locus of the plane \(\sum_i y_i=0\). Under this map a pairing line becomes the corresponding additional plane line \(y_i+y_j=0\), equivalently \(y_k+y_l=0\). Inversion is defined over \(k\) using the inverse in the étale algebra. Therefore \(U_E\) is isomorphic over \(k\) to the complement of seven geometric lines in \(\mathbb P(\ker\operatorname{Tr}_{E/k})\): four coordinate lines and three pairing lines.

**3. Intersections and Frobenius.** In odd characteristic these seven lines have exactly six ordinary triple intersections, indexed by unordered pairs \(\{i,j\}\) of labels, and three ordinary double intersections, indexed by the pairing line *excluded* from the pair that meets. Each triple intersection lies on the two coordinate lines indexed by its pair and on the unique pairing line containing that pair. Distinct intersections remain distinct because \(2\ne0\). The normalization of the seven-line union has seven copies of \(\mathbb P^1\), and the fibres above the nine intersection points contain 18 and 6 geometric branches respectively.

Let \(\sigma\in S_4\) represent arithmetic Frobenius on the four embeddings. Put \(v=\#\operatorname{Fix}(\sigma\mid\{1,2,3,4\})\), \(m=\#\operatorname{Fix}(\sigma\mid\text{three pairings})\), and let \(b\) be the number of fixed incidences \((\{i,j\},i)\) between one of the six unordered pairs and one of its two endpoints. The six triple points have their branches fixed in \(b+e\) cases, where \(e\) is the number of fixed unordered pairs; the three double points have their branches fixed in \(m(m-1)\) cases. The normalization, branch, and point correction is
\[
\#D(\mathbb F_q)=(q+1)(v+m)-\bigl(b+e+m(m-1)\bigr)+(e+m).
\]
Subtracting from \(\#\mathbb P^2(\mathbb F_q)=q^2+q+1\) yields
\[
\boxed{\#U_E(\mathbb F_q)=q^2+(1-v-m)q+1-v-2m+b+m(m-1).}
\]
The five conjugacy types give the following exhaustive fixed-point data:

| \(\lambda\) | \(v\) | \(m\) | \(e\) | \(b\) |
|:--|--:|--:|--:|--:|
| \((1,1,1,1)\) | 4 | 3 | 6 | 12 |
| \((2,1,1)\) | 2 | 1 | 2 | 2 |
| \((2,2)\) | 0 | 3 | 2 | 0 |
| \((3,1)\) | 1 | 0 | 0 | 0 |
| \((4)\) | 0 | 1 | 0 | 0 |

These values produce the five claimed point-count polynomials. Since every partition of four corresponds to an actual finite étale algebra over \(k\), the classification is complete.

**4. Extensions and zeta functions.** After replacing the Frobenius permutation by its \(n\)-th power, the same argument works over \(\mathbb F_{q^n}\). The resulting periodic coefficients are sufficient to compute the five rational zeta functions by the identity \(-\log(1-aT)=\sum_{n\ge1}a^nT^n/n\). For example, the \((4)\) type has coefficient pairs \((0,-1),(-2,1),(0,-1),(-6,9)\) as \(n\) runs through residues \(1,2,3,0\) modulo four; this gives precisely the last rational function in the table. The remaining four cases follow in the same manner.

**5. The sharp empty case.** The first polynomial vanishes for odd \(q\ge3\) only at \(q=3\). For the other four partitions, their polynomials are strictly positive for all odd \(q\ge3\). This proves the claimed criterion.

## Verification
The standalone `verify_cayley_open.py` enumerates all 24 permutations of the four labels and checks the five fixed-point formulas against an independently constructed normalization/branch incidence calculation. It independently enumerates the split Cayley surface and its line-free points over \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11}\), checks coordinate inversion, and directly constructs all five quartic étale algebras over \(\mathbb F_3\) with finite-field arithmetic to verify the corresponding point counts \(0,2,4,9,8\). The exact script and its execution transcript are included. These finite checks test the general proof; the proof itself is the geometric isomorphism and complete \(S_4\) enumeration, not extrapolation from selected fields.

## Relationship to prior work
Heath-Brown's 2002 treatment of rational points on Cayley's cubic defines the complement of its nine lines and supplies the standard explicit lines. That work proves an integer-height asymptotic order over \(\mathbb Q\), not the five finite-field twisted point counts or their zeta functions. The classical four-nodal model and its permutation symmetry are not new. The split count \((q-3)^2\) can also be derived directly from the characteristic polynomial of the corresponding seven-line arrangement; the additional statement here is the **complete arithmetic descent across all five quartic étale types** and all finite extensions. No claim of a new cubic-surface geometry or new line classification is made.

## Limitations
The characteristic-two seven-line arrangement has a different incidence pattern and is excluded. The finding addresses the reduced complement of the entire geometric line configuration, not the full surface, the minimal resolution, or rational points of bounded height over number fields. Historical priority for the exact five-case arithmetic table is provisional, in particular because the classical line equations make such a calculation accessible.

## References
1. D. R. Heath-Brown, *The density of rational points on Cayley's cubic surface*, arXiv:math/0210333v1, first submitted 2002-10-21, especially Section 1 for the equation and nine geometric lines. https://arxiv.org/abs/math/0210333
2. B. Hunt, *Nice modular varieties*, Experimental Mathematics 9 (2000), 613–622, DOI:10.1080/10586458.2000.10504664. Its bibliographic metadata and abstract were accessible; a complete text inspection was not obtained.
3. J. Baez, *Cayley's Nodal Cubic Surface*, Visual Insight, 2016-08-15, for an expository description of the four nodes, nine lines, and symmetric-group action. https://blogs.ams.org/visualinsight/2016/08/15/cayleys-nodal-cubic-surface/
