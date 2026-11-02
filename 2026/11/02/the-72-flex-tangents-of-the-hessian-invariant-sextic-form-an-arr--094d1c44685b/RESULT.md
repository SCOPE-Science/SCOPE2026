# The 72 flex tangents of the Hessian-invariant sextic form a \((12_6,216_3,1728_2)\) line arrangement

## Finding
Over \(\mathbb C\), let \(C\subset\mathbb P^2\) be the smooth plane sextic
\[
F(x,y,z)=x^6+y^6+z^6-10(x^3y^3+x^3z^3+y^3z^3)=0.
\]
Its ordinary inflection points comprise exactly 72 points, six on each of the twelve Hesse reflection lines, and its 72 distinct inflection tangent lines form an arrangement \(\mathcal T\). The singular support of \(\mathcal T\) consists of exactly **12 points of multiplicity six, 216 points of multiplicity three, and 1728 ordinary double points**, with no other points of multiplicity at least two. Thus \(\#\operatorname{Sing}(\mathcal T)=1956\). Each member of \(\mathcal T\) contains exactly one sixfold point, nine triple points and 48 double points. In particular, \(12\binom62+216\binom32+1728\binom22=2556=\binom{72}{2}\).

## Assumptions and scope
Everything is over the complex numbers (characteristic zero). An ordinary inflection means a smooth point with tangent contact order exactly three. An \(m\)-fold line-arrangement point is a point contained in exactly \(m\) distinct lines. The claim concerns the 72 flex tangents, **not** the pre-existing arrangement of twelve Hesse reflection lines. The curve is the sextic invariant of the projective Hessian group of order 216. No statement about real configurations or positive-characteristic specializations is made.

## Proof
**Smoothness.** Put \(U=x^3,V=y^3,W=z^3\), so \(F=Q(U,V,W)\) for \(Q=U^2+V^2+W^2-10(UV+UW+VW)\). Its symmetric matrix has eigenvalues \(-9,6,6\), hence is nonsingular. A singular point of \(C\) with all three coordinates nonzero would make all three derivatives of \(Q\) vanish, impossible. At a point with exactly one zero coordinate, nonsingularity follows from the two remaining equations: the restriction \(V^2-10VW+W^2\) has distinct projective roots, since its discriminant is 96. Coordinate vertices do not lie on \(C\). Thus \(C\) is smooth and has genus ten.

**All ordinary flexes.** Direct differentiation gives the exact identity
\[
\det(\partial_i\partial_j F)=108000xyz(x+y+z)Q_1Q_2Q_3Q_4,
\]
where
\[
\begin{aligned}
Q_1&=x^2-xy-xz+y^2-yz+z^2,\\
Q_2&=x^2-xy-xz+y^2+2yz+z^2,\\
Q_3&=x^2-xy+2xz+y^2-yz+z^2,\\
Q_4&=x^2+2xy-xz+y^2-yz+z^2.
\end{aligned}
\]
Each \(Q_i\) factors into two distinct linear forms over \(\mathbb Q(\omega)\), where \(\omega^2+\omega+1=0\). These twelve lines are precisely the Hesse reflection arrangement. The group of order 216 acts transitively on these lines. On \(x=0\), the intersection with \(C\) is \(r^6-10r^3+1=0\) in the coordinate \(r=z/y\); its six roots are distinct. The Hesse vertices lie outside \(C\), as is also recorded by Artebani--Dolgachev. Thus all twelve reflection lines meet \(C\) in disjoint sets of six simple points, exhausting the \(6\cdot3(6-2)=72\) Hessian intersections. At \(P=[0:1:r]\), the tangent is \(z-r y=0\), and its intersection with \(C\) satisfies
\[
F(x,y,ry)=x^3\bigl(x^3-10(1+r^3)y^3\bigr).
\]
Since \(1+r^3\ne0\), the contact order is exactly three. Transitivity propagates this contact description to all 72 points. Their tangent lines are distinct, as is certified below by reduction modulo 211.

**Exact incidence certificate.** Fix a root \(r\) of \(r^6-10r^3+1\), and take the initial dual line coefficient vector \(\ell_0=(0,-r,1)\). Act projectively using the following four dual generators (the inverse transposes of standard Hessian-group generators):
\[
D_1=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},\quad
D_2=\operatorname{diag}(1,\omega^2,\omega),\quad
D_3=\begin{pmatrix}1&1&1\\1&\omega^2&\omega\\1&\omega&\omega^2\end{pmatrix},\quad
D_4=\operatorname{diag}(1,\omega^2,\omega^2).
\]
These preserve the underlying curve and generate its Hessian action; the orbit of \(\ell_0\) has 72 projectively distinct elements. Each coefficient lies in \(\mathbb Z[\omega]+r\mathbb Z[\omega]\). For three orbit lines the concurrence determinant is therefore a polynomial of degree at most three in \(r\), with coefficients in \(\mathbb Z[\omega]\).

The standalone verifier `verify_tangents.py` enumerates this orbit symbolically in the ring above. To classify which triples *might* concur, it reduces the orbit at \(211\), using \(\omega\mapsto14\) and \(r\mapsto29\), both roots of their respective monic defining polynomials modulo \(211\). The 72 reduced lines are distinct. Their pairwise intersections have exactly 12 sixfold points, 216 triple points and 1728 double points. It then proves *exactly in* \(\mathbb Z[\omega,r]\), **not merely modulo 211**, that every additional line at each reduced point of multiplicity at least three passes through the first two defining lines: 264 independently checked zero determinant polynomials. These yield genuine characteristic-zero intersections of the predicted multiplicities. Any further intersection coincidence in characteristic zero would give a coincidence after reduction at 211, contradicting the finite-field exhaustive enumeration. This implication is valid because the minimal polynomial \(r^6-10r^3+1\) is irreducible over \(\mathbb Q(\omega)\) and the chosen reduction is an evaluation homomorphism from the integral coefficient ring; nonzero reduced line coefficients guarantee well-defined projective images. Therefore the listed intersection multiplicities are exhaustive. Finally, the verifier counts exactly 1 sixfold, 9 triple and 48 double points on every one of the 72 lines.

## Verification
Using Python with no external libraries, run `python3 verify_tangents.py`: it prints `MASCHKE_72_TANGENTS_INCIDENCE_OVER_CHARACTERISTIC_ZERO_PASS` and the point profile. The symbolic concurrence proof uses exact integer pairs representing Eisenstein integers; modulus 211 is only an **exclusion** device, while 264 separate zero identities certify positive incidences in characteristic zero. Using Python with SymPy, run `python3 verify_curvature.py`: it prints `MASCHKE_HESSIAN_FACTOR_SMOOTH_SLICE_TANGENCY_IRREDUCIBILITY_PASS`; this checks the Hessian factorization, base tangent contact, squarefreeness and irreducibility needed for the reduction argument. The smoothness proof and group-theoretic identification are explicit above. The two scripts and their complete dependencies are included with this result.

## Relationship to prior work
Artebani and Dolgachev describe the Hessian group, the twelve reflection lines, and the smooth invariant sextic, including its equation and exclusion of the Hesse vertices. These are **antecedents**, not discoveries claimed here. Badr and Bars study smooth plane-sextic automorphism groups in a preprint first posted in 2022 (and published in 2025); their classification explicitly recognizes this exact curve as the unique sextic with projective automorphism group of order 216. Yoshida studies simple primitive automorphism groups and explicitly excludes the Hessian group. The specific new statement is the **complete incidence multiplicity profile of the 72 inflection tangent lines**, notably the 216 triple intersections and 1728 double intersections; the cited sources' results about invariant sextics, Hesse reflection lines, K3 covers and automorphism strata do not imply these intersection counts.

## Limitations
The statement concerns the underlying line arrangement and its reduced singular support, not its Jacobian singular subscheme, freeness, characteristic polynomial, fundamental group, or characteristic-\(p\) behavior. The symbolic incidence certificate depends on the exact supplied program and can be independently rerun. The literature comparison is substantial but cannot exclude all unpublished or unindexed earlier calculations. The result has not undergone an independent mathematical audit.

## References
- Michela Artebani and Igor Dolgachev, *The Hesse pencil of plane cubic curves*, published 2009, especially §§4,6. https://sites.lsa.umich.edu/idolga-new/wp-content/uploads/sites/1467/2024/08/hesse09.pdf
- Yusuke Yoshida, *Projective plane curves whose automorphism groups are simple and primitive*, arXiv:2008.13427, first posted 2020-08-31. https://arxiv.org/abs/2008.13427
- Eslam Badr and Francesc Bars, *The stratification by automorphism groups of smooth plane sextic curves*, arXiv:2208.12749, first posted 2022-08-26; *Annali di Matematica Pura ed Applicata* (2025), DOI 10.1007/s10231-025-01558-z. https://arxiv.org/abs/2208.12749
