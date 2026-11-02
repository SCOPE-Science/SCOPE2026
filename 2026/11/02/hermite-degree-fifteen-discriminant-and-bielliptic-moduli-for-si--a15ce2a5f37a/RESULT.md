# Hermite degree-fifteen discriminant and bielliptic moduli for six-nodal rational elliptic surfaces

## Finding

The six singular-fiber parameters of a complex rational elliptic surface with section and exactly six Kodaira fibers of type \(I_2\) form precisely the **smooth-squarefree locus of the classical degree-15 Hermite involution hypersurface** in the projective space of binary sextics. Equivalently, their genus-two hyperelliptic double cover is **bielliptic**, so its Jacobian belongs to the discriminant-four Humbert locus. The map from the coarse moduli of these section-marked elliptic fibrations, modulo base changes, to the bielliptic genus-two locus is generically one-to-one and hence birational.

There is an explicit defining equation for the hypersurface, not requiring expansion into seven binary-sextic coefficients. Let \(F(S,T)=\prod_{i=1}^6 L_i(S,T)\) have six distinct linear factors. For a binary quadratic \(q=aS^2+bST+cT^2\), write \(v(q)=(a,b,c)\). For each of the 15 partitions \(\pi=\{\{i,j\},\{k,l\},\{m,n\}\}\) into three unordered pairs, fix any ordering and set
\[
\delta_\pi=\det\left(\begin{array}{c}v(L_iL_j)\\v(L_kL_l)\\v(L_mL_n)\end{array}\right),\qquad
\mathcal H(F)=\prod_{\pi}\delta_\pi.
\]
Choosing a different fixed ordering changes \(\mathcal H\) only by a global sign. The product descends to a nonzero \(\operatorname{SL}_2\)-invariant homogeneous polynomial of degree **15** in the coefficients of \(F\). Thus, within the squarefree sextics, the sought locus is exactly \(\mathcal H(F)=0\). This is the classical Hermite involution invariant; the contribution here is the exact identification with the six-\(I_2\) surface family and its generically birational genus-two modular interpretation.

## Assumptions and scope

Work over \(\mathbb C\). A rational elliptic surface with section means a relatively minimal rational elliptic fibration \(f:X\to\mathbb P^1\) with a distinguished zero section. Isomorphisms may act on the base by \(\operatorname{PGL}_2(\mathbb C)\) but preserve the zero section. All six singular fibers are assumed distinct and exactly Kodaira type \(I_2\); no other singular fibers occur. The associated binary sextic is squarefree. Statements about injectivity of the moduli map are **generic**, not asserted at all loci with enhanced automorphisms. The invariant equation describes the open family, and its entire degree-15 hypersurface gives the closure in \(\mathbb P^6\).

## Proof

**1. The published Weierstrass form.** The classification in Ciliberto--Grassi--Miranda--Verra--Zanardini, Section 2.4, shows that every surface in scope has the form
\[
Y^2=(X-Q_1)(X-Q_2)(X-Q_3),\qquad Q_1+Q_2+Q_3=0,
\]
where the \(Q_i\) are binary quadratics on the base. The three pairwise differences \(r_1=Q_1-Q_2\), \(r_2=Q_2-Q_3\), \(r_3=Q_3-Q_1\) are quadratic and satisfy \(r_1+r_2+r_3=0\). The discriminant of the cubic, up to the harmless customary scalar, is \(-r_1^2r_2^2r_3^2\). Exactly six \(I_2\) fibers imply that the three quadratics have disjoint, simple zero divisors: their product is a squarefree sextic \(F\). In the root pairing naturally induced by \(r_1,r_2,r_3\), their coefficient vectors are dependent, so one \(\delta_\pi\) vanishes and hence \(\mathcal H(F)=0\).

**2. Every squarefree Hermite sextic occurs.** Suppose \(F\) is squarefree and \(\delta_\pi=0\) for a partition \(\pi\). Write its three quadratics as \(q_1,q_2,q_3\). Their coefficient matrix has rank exactly two: rank one would make two quadratics proportional, contradicting disjoint roots. Their unique linear dependence \(\alpha_1q_1+\alpha_2q_2+\alpha_3q_3=0\) has every \(\alpha_i\neq0\), again because two quadratics have disjoint roots. Set \(r_i=\alpha_iq_i\), and recover
\[
Q_1=(2r_1+r_2)/3,\quad Q_2=(r_2-r_1)/3,\quad Q_3=-(r_1+2r_2)/3.
\]
Then \(Q_1+Q_2+Q_3=0\) and the pairwise differences are \(r_1,r_2,r_3\). Since \(F\) is squarefree, at each root precisely one difference vanishes to order one, while the other two and the Weierstrass coefficient \(A\) are nonzero. Hence \(\operatorname{ord}\Delta=2\), \(\operatorname{ord}c_4=0\), giving Kodaira type \(I_2\). There are no other singular fibers. The Weierstrass surface is a rational elliptic surface with section: \(A\) and \(B\) are sections of \(\mathcal O(4)\) and \(\mathcal O(6)\), respectively, with fundamental line-bundle degree one. Minimal resolution does not change the fibers' Kodaira types. This proves the exact image statement.

**3. Polynomial equation and degree.** Each determinant \(\delta_\pi\) is linear in each of the six root linear forms, hence \(\mathcal H\) has multidegree \((15,\ldots,15)\). A root permutation changes the product by a constant sign, since it permutes its factors and may reverse their ordered rows. The sign is trivial: the test sextic with root tuple \((0,0,1,2,3,4)\) has \(\mathcal H\neq0\), while a transposition of the equal roots fixes this tuple; transpositions generate the symmetric group. Consequently the product is symmetric in the six roots and descends through \(\operatorname{Sym}^6\mathbb P^1\simeq\mathbb P^6\) to a degree-15 homogeneous polynomial. Under a base change \(g\in\operatorname{GL}_2\), every quadratic coefficient determinant scales by \((\det g)^3\); their product has weight \(45\), the correct weight for a degree-15 invariant of binary sextics. The locus is irreducible because configurations invariant under a fixed-point-free projective involution are parametrized irreducibly by the involution and three unordered orbits. The product is not multiplied by the sextic discriminant (it is nonzero at the one-double-root example); it is generically reduced because the example \(\{-3,-2,-1,1,2,3\}\) has exactly one vanishing factor, with nonzero first derivative when any root is perturbed. Thus it is a scalar multiple of the classical degree-15 Hermite invariant.

**4. Involution and genus-two geometry.** Three disjoint root pairs \(q_i\) with dependent coefficient vectors lie in a pencil of binary quadratics. That pencil defines a degree-two morphism \(\mathbb P^1\to\mathbb P^1\), whose nontrivial deck transformation is a projective involution swapping the two points in each pair. Conversely an involution with three two-element orbits produces a pencil of degree-two fiber divisors, and their quadratics are dependent. Conjugating the involution gives six branch points \(\{\pm a,\pm b,\pm c\}\), and the associated genus-two curve becomes
\[
w^2=(t^2-a^2)(t^2-b^2)(t^2-c^2).
\]
The lift \((t,w)\mapsto(-t,w)\) has two fixed points and hence elliptic quotient by Riemann--Hurwitz. Thus the genus-two curve is bielliptic. Conversely a nonhyperelliptic involution of a genus-two curve descends to an involution of its hyperelliptic base, and, after choosing the appropriate lift, its six Weierstrass branch points divide into three exchanged pairs. The classical bielliptic locus is the discriminant-four Humbert locus for genus-two Jacobians; this last identification is prior literature.

**5. Generic birationality.** At a general sextic on the Hermite divisor, the projective involution is unique (the explicit root set \(\{\pm1,\pm2,\pm3\}\) has precisely the identity and sign involution in its projective stabilizer; uniqueness holds on a nonempty open subset). Thus its three-pair partition is uniquely determined. The relation among the resulting quadratics is unique up to common scaling, which rescales \(X,Y\) in the Weierstrass equation; permuting the three \(Q_i\) leaves the cubic unchanged. Consequently a generic branch sextic reconstructs exactly one section-marked surface up to isomorphism and base reparametrization. Since both the surface moduli and the bielliptic locus are irreducible surfaces and the map is dominant and generically injective in characteristic zero, it is birational. This conclusion is restricted to coarse moduli and their dense open loci.

For a concrete instance, the branch set \(\{\pm1,\pm2,\pm3\}\) admits \(r_1=5(t^2-1)\), \(r_2=-8(t^2-4)\), \(r_3=3(t^2-9)\). They sum to zero and yield a Weierstrass discriminant \(-14400\prod_{j=1}^{3}(t^2-j^2)^2\), with six fibers of type \(I_2\).

## Verification

The standalone `verify.py` performs exact integer and rational arithmetic to enumerate the 15 pairings, check nonzero/generic and vanishing/special Hermite values, all 720 relabelings of two test root sets, a repeated-root specialization excluding an alternating product, an explicit simple zero, a complete Möbius-stabilizer check of the special sextic, and the cubic/Weierstrass discriminant and fiber-type identities. It prints `VERIFY_OK` on success. These tests supplement the all-parameter geometric proof; they do not replace it, and no independent audit has been performed.

## Relationship to prior work

Ciliberto--Grassi--Miranda--Verra--Zanardini (2026), Section 2.4, prove the quadratic-root normal form and, in their Section 2.7 Question 25, specifically ask for the equation of the six-singular-fiber hypersurface and the genus-two divisor condition. Their results establish the input geometry, not the identification in this finding.

The degree-15 Hermite invariant and the involution locus of binary sextics are classical and are explicitly described by Abdesselam--Chipalkatti (2010/2019), Section 1.5. Weintraub (2010) studies discriminant-four Humbert divisors on the level-two genus-two moduli space. Neither the classical degree, the classical bielliptic/Humbert correspondence, nor the general invariant theory are claimed as new. The distinct conclusion is that these objects **exactly coincide with the image and birational moduli of the 2026 six-\(I_2\) elliptic-surface family**, with an explicit inverse construction.

## Limitations

Only characteristic zero and six distinct \(I_2\) singular fibers are addressed. This is not a classification of non-squarefree boundary points, their Kodaira degenerations, stable compactifications, integral structures, or the precise fiber of the moduli map at enhanced-automorphism points. The Hermite equation is given in a factored root-coordinate form that descends to an ordinary homogeneous coefficient polynomial; no expanded 7-coefficient expression is supplied. Classical constructions might contain an implicit version of this precise elliptic-surface identification, so historical priority remains subject to broader specialist verification. Self-review is not independent validation.

## References

1. C. Ciliberto, A. Grassi, R. Miranda, A. Verra, A. Zanardini, *Rational elliptic surfaces with six singular double fibres*, arXiv:2602.11725v1 (public 2026-02-12), especially Sections 2.4 and 2.7, Question 25. https://arxiv.org/abs/2602.11725
2. A. Abdesselam, J. Chipalkatti, *Quadratic involutions on binary forms*, arXiv:1008.3117, Section 1.5 (original 2010, version 3 dated 2019-03-21). https://arxiv.org/abs/1008.3117
3. S. H. Weintraub, *Involutions, Humbert surfaces, and divisors on a moduli space*, Rend. Lincei Mat. Appl. 21 (2010), 415–440, doi:10.4171/RLM/581. https://doi.org/10.4171/RLM/581
