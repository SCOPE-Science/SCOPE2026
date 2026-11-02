# Nine five-round theories of finite affine collinearity structures

## Finding
For a prime power \(s\) and an integer \(d\ge 2\), let \(\mathcal A(d,s)\) be the one-sorted structure whose universe is \(\mathbb F_s^d\), with equality and a single ternary relation \(C(x,y,z)\) meaning that its three entries are collinear. Degenerate triples, including repeated entries, satisfy \(C\). No lines, field operations, or dimension constants are named. Write \(\equiv_5\) for equivalence of all first-order sentences of quantifier rank at most five.

**Theorem.** The structures \(\mathcal A(d,s)\), over all prime powers \(s\) and all \(d\ge2\), have exactly nine \(\equiv_5\)-classes, as follows:

1. \(s=2,d=2\);
2. \(s=2,d\ge3\);
3. \(s=3,d=2\);
4. \(s=3,d\ge3\);
5. \(s=4,d=2\);
6. \(s=4,d\ge3\);
7. \(s\ge5\) odd, \(d=2\);
8. \(s\ge5\) odd, \(d\ge3\);
9. \(s\ge8\) even, \(d\ge2\).

In particular, at five rounds all even-field affine planes of order at least eight are indistinguishable from affine spaces of dimension at least three over any even field of order at least eight, although the analogous plane-versus-space distinction is visible over odd fields. The representatives \(\mathcal A(2,2),\mathcal A(3,2),\mathcal A(2,3),\mathcal A(3,3),\mathcal A(2,4),\mathcal A(3,4),\mathcal A(2,5),\mathcal A(3,5),\mathcal A(2,8)\) contain at most \(125\) points. No smaller maximum representative is possible within this family.

## Assumptions and scope
All fields are finite fields, not arbitrary rings or nearfields. Dimension is at least two. Formulas use first-order equality and the unlabelled collinearity predicate alone. The quantifier rank is at most five, with quantifier alternations allowed. No claim is made about higher ranks, counting logic, or languages with explicit lines or coordinates.

## Proof
**1. Five-round profile recursion.** For an ordered tuple \(\bar a\), let \(\mathrm{At}(\bar a)\) record the equalities and ternary collinearities among its entries. Define \(T_5(\bar a)=\mathrm{At}(\bar a)\), and for tuples of length \(i<5\), recursively set
\[
T_i(\bar a)=\bigl(\mathrm{At}(\bar a),\{T_{i+1}(\bar a,b):b\text{ is a point}\}\bigr).
\]
Standard induction on the remaining game rounds shows that the root \(T_0\) agrees exactly when Duplicator wins the five-round Ehrenfeucht--Fraisse game. Multiplicities do not matter, because first-order quantification supplies one point at a time and repetitions are represented by equality.

**2. The fourth-point profile in sufficiently large fields.** Assume \(s\ge5\). After four distinct points have been chosen, the only case needing a nontrivial geometric invariant is that no three are collinear. Label the four points \(a_0,a_1,a_2,a_3\). There are six determined pair-lines \(L_{ij}\), one for each \(i<j\). For a fifth *new* point, possible collinearities with existing pairs are: no pair-line; precisely one of the six pair-lines; or precisely two pair-lines \(L_{ij},L_{kl}\) with four distinct indices, meeting outside the selected four points. A new point cannot lie on two pair-lines sharing one of the selected points; nor can it lie on three pair-lines of the four-point configuration. Let \(S\) be the subset of the three perfect matchings of \(\{0,1,2,3\}\) whose opposite pair-lines cross in such a new point. Then \(S\) completely determines all fifth-point atomic diagrams. Each singleton pair-line pattern exists, since a pair-line contains at least \(s-2\ge3\) unselected points and is involved in at most one such crossing. A point on none of the pair-lines exists: their union contains at most \(4+6(s-2)=6s-8<s^2\) points in an affine plane, and in higher dimensions the bound remains sufficient.

For four distinct collinear points, a fifth point either lies on the line or off it; both alternatives exist for \(s\ge5\). For exactly three collinear points and a fourth outside the line, a fifth point can lie on that triple-line, on one of the three lines joining the outsider to a triple point, or on none of these lines. Each possibility exists for \(s\ge5\). For four-tuples with repeated points, the analogous extension profiles follow from at most three distinct selected points; the relevant on-line and off-line extensions are also available. Thus the only nontrivial variation of fourth-point profiles in this range is the set \(S\).

**3. Exactly which crossing sets occur.** Fix three noncollinear points by affine coordinates as \(a_0=(0,0),a_1=(1,0),a_2=(0,1)\). A fourth planar point is \(a_3=(u,v)\). Its four-point diagram has no collinear triple exactly when \(uv(u+v-1)\ne0\). In the order of matchings \((01\mid23),(02\mid13),(03\mid12)\), the corresponding pair-lines are parallel precisely when, respectively,
\[
v=1,\qquad u=1,\qquad u+v=0.
\]
Each nonparallel opposite pair yields one crossing in \(S\). In odd characteristic, two of these parallelism equalities can hold without the third: \((u,v)=(1,1)\) gives exactly one crossing. By choosing exactly one or none of the equalities, every labelled crossing set of size two or three is also realized for every odd \(s\ge5\). The all-crossing choice exists because, for \(u,v\notin\{0,1\}\), avoiding both \(u+v=0\) and \(u+v=1\) leaves at least \((s-2)(s-4)>0\) ordered pairs. No odd-characteristic planar quadruple has zero crossings: the first two parallelism equalities force \((u,v)=(1,1)\), and then \(u+v\ne0\).

In characteristic two, any two of the displayed parallelism equalities imply the third. Hence a planar quadruple cannot have exactly one crossing. The point \((u,v)=(1,1)\) realizes zero crossings. Precisely one parallelism equality realizes two crossings, and avoiding all three realizes all three crossings. The last construction is available for every even field of order at least eight by the same positive count. Consequently, the realized crossing subsets in the plane are all labelled subsets of sizes \(1,2,3\) for odd \(s\ge5\), and all labelled subsets of sizes \(0,2,3\) for even \(s\ge8\).

Four affinely independent points are available when \(d\ge3\), and they have zero crossings, six singleton line patterns, and the no-line pattern. Hence, for odd \(s\ge5\), dimensions at least three realize all four crossing cardinalities \(0,1,2,3\), while the plane realizes only \(1,2,3\). For even \(s\ge8\), both the plane and higher dimensions realize the same possibilities \(0,2,3\). The preceding catalogue is independent of the value of \(s\) within either regime. Starting with at most three selected points, all equality/collinearity patterns and all listed fourth-point profiles are realizable uniformly in the stated regimes. Induction through the recursion in step 1 proves the three large-field classes.

**4. The small fields.** When \(s=2\), no three *distinct* points are collinear, so the structure reduces, for quantifier rank at most five, to pure equality on \(2^d\) points. This separates \(d=2\) (four points) from every \(d\ge3\) (at least eight points). When \(s=3\) or \(4\), all dimensions \(d\ge3\) are five-round equivalent: through the fourth move Duplicator preserves the complete affine-coordinate relations among the selected points using a partial affine isomorphism. If the four points span a three-dimensional affine space and Spoiler's fifth selection lies outside that span in a higher-dimensional opponent, a response within the three-space avoiding all six pair-lines has the required ternary diagram. Such a response exists: for \(s\ge2\), \(s^3>4+6(s-2)\) (and for \(s=2\) all pair-lines contain only their selected endpoints). Repeated points and lower affine ranks are handled by ordinary affine-basis extension.

The plane is distinguished from higher dimension in each of these two small fields by selecting four affinely independent points in dimension three and then exploiting a fifth-point extension profile. For \(s=3\), every planar four-point cap has exactly one crossing and its six pair-lines cover the nine-point plane; a fifth point outside all six lines exists in dimension three but not in that plane. For \(s=4\), any planar four-point cap has either zero or two crossings. If two, a fifth point at one of the crossings distinguishes it from the independent quadruple; if zero, it is a characteristic-two parallelogram and its six pair-lines cover all sixteen planar points, whereas a fifth point avoiding them exists in dimension three. The required games may switch the side on the final move.

**5. Separation of all nine classes.** Existence of \(j\) pairwise distinct collinear points is expressed by a sentence of rank \(j\) for \(j=3,4,5\); these separate field sizes \(2,3,4\) and the large-field regimes. The small-field dimension splits were proved in step 4; the odd large-field dimension split is forced by the zero-crossing quadruple available only in dimension at least three. Odd versus even large-field structures are separated by the exactly-one-crossing four-point extension profile: realizable in odd characteristic, impossible in characteristic two even in higher dimension. In each case a Spoiler strategy first selects the four witnessing points and, if the responder cannot match their full extension profiles, selects a fifth point from the symmetric difference of the profiles. These distinctions are exact at rank five.

The nine class representatives given above have cardinalities \(4,8,9,27,16,64,25,125,64\). The odd-field high-dimensional class cannot have a smaller representative than \(\mathcal A(3,5)\), so the maximal minimal representative size \(125\) is sharp.

## Verification
The independent proof is finite-field uniform; it does not rely on extrapolating from experiments. A Python standard-library verifier enumerates affine-group tuple orbits, calculates the complete five-round recursive types, and checks the predicted class equalities and distinctions for field orders \(2,3,4,5,7,8,9,11,16\) in the dimensions recorded by its output. A second, direct vertex-tuple recursion (without affine-orbit reduction) computes small-plane five-round types for orders \(2,3,4\). Reproduce the recorded runs with `python verification/affine_rank5_probe.py` and `python verification/affine_direct_small.py`. The complete programs and recorded stdout are supplied alongside this document.

## Relationship to prior work
Ehrenfeucht--Fraisse game characterization and recursive finite-model types are classical methods, described, for example, in Libkin's *Elements of Finite Model Theory* (2004). Aiello and van Benthem's *A Modal Walk Through Space* (2001) discusses the expressive powers of spatial and affine languages, including the first-order setting, but concerns mainly real betweenness and modal languages, rather than these finite-field point-collinearity five-round classes. Earlier bounded-rank classifications of two-sorted affine-plane incidence structures do not imply the stated one-sorted rank-five result: the languages and quantifier budgets differ, and the present characteristic-sensitive plane/dimension collapse is additional. No equivalent or more general classification was identified in the inspected references and available mathematical research index; this is not a proof that no such result exists.

## Limitations
The result is only about the ternary collinearity reduct in dimension at least two, not line-sorted incidence or field operations. The result does not classify quantifier rank six or higher. Historical priority has not been independently exhaustively established. The finite verification programs do not independently certify the infinite field-uniform case; that is proved using the extension-profile catalogue and the affine-basis argument.

## References
- Leonid Libkin, *Elements of Finite Model Theory*, Springer, 2004, ISBN 9783540212027; DOI: 10.1007/978-3-662-07003-1 (verified 2004-07-02 edition release).
- Marco Aiello and Johan van Benthem, *A Modal Walk Through Space*, University of Amsterdam technical report PP-2001-23 (2001), https://eprints.illc.uva.nl/id/document/152 .
