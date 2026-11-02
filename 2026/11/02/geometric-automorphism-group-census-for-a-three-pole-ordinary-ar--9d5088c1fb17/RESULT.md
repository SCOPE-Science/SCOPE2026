# Geometric automorphism-group census for a three-pole ordinary Artin--Schreier family

## Finding
Let \(p\ge5\) be prime, let \(k=\overline{\mathbb F}_p\), and consider the smooth projective model \(Y_{a,b,c}/\mathbb F_p\) of
\[
 y^p-y=a x+\frac{b}{x}+\frac{c}{x-1},\qquad a,b,c\in\mathbb F_p^\times.
\]
Count geometric isomorphism classes **represented by these prime-field coefficient triples**, not all curves of the same genus. Their full geometric automorphism groups and numbers of classes are exactly:

| Full geometric automorphism group | Number of geometric classes |
| --- | --- |
| \(C_p\) | \(\frac{(p-2)(p-3)}6\) if \(p\equiv2\pmod3\), otherwise \(\frac{(p-1)(p-4)}6\) |
| \(C_p\rtimes_{-1}C_2\cong D_{2p}\) | \(p-2\) |
| \(C_p\rtimes C_3\), with faithful action | \(1\) if \(p\equiv1\pmod3\), otherwise \(0\) |
| \(C_p\rtimes_{\operatorname{sgn}}S_3\) | \(1\) |

The group \(D_{2p}\) here has order \(2p\). For the final row, the order-three subgroup acts trivially on \(C_p\), while every transposition acts by inversion. The listed isomorphism classes are disjoint, and every member appears in exactly one row.

## Assumptions and scope
Throughout \(p\) is any prime at least five, and all curves, automorphisms and isomorphisms are considered after base change to \(k\). The coefficients \(a,b,c\) range over \(\mathbb F_p^\times\) and need not be pairwise different. No classification of every \(k\)-valued coefficient triple is asserted. The rational function has exactly three distinct simple poles at \(\{\infty,0,1\}\). The Artin--Schreier genus and Deuring--Shafarevich formulas give
\[
 g(Y_{a,b,c})=2(p-1),\qquad f_p(Y_{a,b,c})=2(p-1),
\]
so all these curves are ordinary. Their function fields are separable and their smooth projective models are geometrically irreducible.

## Proof
**1. Descent to the branch line.** The Valentini--Madan uniqueness theorem, in the form stated in Tafazolian--Kazemifard, Proposition 2.2, applies to every member. Indeed, the exceptional single-branch-point families have \(p\)-rank zero, the three-branch-point exceptional family exists only in characteristic three, and the exceptional curve \(y^p-y=d/(x^p-x)\) has \(p\) simple poles and genus \((p-1)^2\), unequal to \(2(p-1)\) for \(p\ge5\). Thus any geometric isomorphism between two members carries the unique rational degree-\(p\) subfield to the other and induces a Möbius transformation permuting the three branch points. The full base stabilizer is \(S_3\).

**2. Equivalence of coefficient vectors.** An isomorphism with base map \(M\) maps the Artin--Schreier generator to \(u y+h(x)\) with \(u\in\mathbb F_p^\times\) and \(h\in k(x)\), so the two rational functions differ by \(h^p-h\) after the base substitution and scalar multiplication. Because their poles all have order at most one, \(h\) cannot have a pole: a pole of \(h\) would induce a pole of \(h^p-h\) of order divisible by \(p\). Consequently \(h\) is constant. Every constant is of the form \(h^p-h\) over \(k\), so two members are geometrically isomorphic precisely when their nonzero coefficient vectors lie in the same orbit of \(S_3\times\mathbb F_p^\times\).

For \(f_{a,b,c}(x)=a x+b/x+c/(x-1)\), direct partial fractions give
\[
 f_{a,b,c}(1-x)=-f_{a,c,b}(x)+a,
 \qquad f_{a,b,c}(1/x)=f_{b,a,-c}(x)-c.
\]
The two substitutions generate the branch-point \(S_3\). Quotienting common scalars and writing \(u=b/a\), \(v=c/a\) identifies the class set with orbits on \(T=(\mathbb F_p^\times)^2\) for the two involutions
\[
 s(u,v)=(v,u),\qquad t(u,v)=(u^{-1},-v/u).
\]
The corresponding formulas are identities of rational functions over the prime field, up to constants; no asymptotic or unverified classification assumption is used.

**3. Stabilizers in the finite torus.** The three transposition fixed sets are
\[
 u=v,\qquad u=-1,\qquad v=-1,
\]
each of size \(p-1\). All pairwise intersections coincide with their common point \((-1,-1)\), so their union has \(3p-5\) elements. A three-cycle is fixed exactly at
\[
 u^3=-1,\qquad v=u^{-1}.
\]
There are \(h=\gcd(3,p-1)\) such points. One is \((-1,-1)\), with full stabilizer \(S_3\). If \(p\equiv1\pmod3\), the other two form a single orbit with stabilizer \(C_3\); otherwise there are none. Every remaining point in the transposition union has stabilizer exactly \(C_2\), giving \(3p-6\) points in \(p-2\) orbits of size three. The number of points with trivial stabilizer is
\[
 (p-1)^2-(3p-5)-(h-1)=p^2-5p+7-h.
\]
Dividing by six yields \(\frac{(p-2)(p-3)}6\) when \(h=1\) and \(\frac{(p-1)(p-4)}6\) when \(h=3\).

**4. Full automorphism group structure.** The deck transformations form a normal subgroup \(C_p\); the preceding descent and stabilizer argument gives \(1\to C_p\to\operatorname{Aut}_k(Y)\to H\to1\), with \(H\le S_3\) the point stabilizer. Since \(p\ge5\), Schur--Zassenhaus splits the extension. At transposition-fixed points, the comparison scalar is \(-1\) and the induced conjugation on deck translations is inversion. For a noncentral three-cycle fixed point, the scalar has order three and is nontrivial, giving a faithful \(C_3\)-action. At \((-1,-1)\), the three-cycles have scalar \(1\), whereas transpositions have scalar \(-1\), yielding the sign action. These are precisely the four groups in the table. This proves the statement for all \(p\ge5\).

## Verification
The accompanying standalone, standard-library-only program `verify.py` enumerates the complete torus \(T\) and its \(S_3\)-orbits in each of the twenty-three primes from \(5\) through \(97\). It checks the fixed-point formulas, the four stabilizer-orbit counts and the free-orbit formulas directly; it prints `VERIFY_OK` on success. For instance, the class counts by group sizes \(p,2p,3p,6p\) are \((1,3,0,1)\) for \(p=5\) and \((3,5,1,1)\) for \(p=7\). The infinite-prime conclusion is proved in the preceding paragraphs, not inferred from the finite test.

## Relationship to prior work
Tafazolian--Kazemifard classify which genus and \(p\)-rank pairs admit an Artin--Schreier curve with the minimal full geometric group \(C_p\); their three-or-more-pole construction proves existence, not this isomorphism-class-by-group census. Duque-Rosero--Lorenzo García--Malmskog--Scheidler (2026), Section 6.3, identify the finite \(S_3\times\mathbb F_p^\times\) standard-form equivalence action for three equal-order poles and study invariant rings; they do not give this prime-field coefficient-torus stabilizer spectrum. Ho--Pries (2022), Proposition 5.1 and Theorem 5.3, compute weighted finite-field mass formulas for Artin--Schreier covers, not the present unweighted geometric isomorphism and full-automorphism distribution. Those methods make the calculation natural, but weighted masses alone do not determine the stated four group frequencies. Closely related coordinate presentations remain a residual historical-priority risk.

## Limitations
This is a classification of the finite set of geometric curves arising from \(\mathbb F_p\)-valued nonzero coefficient triples, not of all points in the two-dimensional moduli locus over \(k\). The geometric counts do not count distinct \(\mathbb F_p\)-isomorphism classes or arithmetic twists. No new result on point counts, Newton polygons, or endomorphism rings is asserted. The prior-work comparison does not certify historical novelty, and independent verification has not been performed.

## References
1. Tafazolian and Kazemifard, *Artin--Schreier Curves of Prescribed p-Rank Without Extra Automorphisms* (2026), arXiv:2610.13279v1, Theorem 1.1 and Proposition 5.5, https://arxiv.org/abs/2610.13279.
2. Duque-Rosero, Lorenzo García, Malmskog and Scheidler, *Computing Invariants of Artin-Schreier Curves* (2026), arXiv:2602.22435v1, Section 6.3, https://arxiv.org/abs/2602.22435.
3. Ho and Pries, *A Mass Formula For Artin--Schreier Curves Over Finite Fields* (2022), arXiv:2203.10187v1, Proposition 5.1 and Theorem 5.3, https://arxiv.org/abs/2203.10187.
4. Valentini and Madan, *A Hauptsatz of L. E. Dickson and Artin--Schreier extensions* (1980), Theorem 6; descent statement quoted and applied via reference 1.
