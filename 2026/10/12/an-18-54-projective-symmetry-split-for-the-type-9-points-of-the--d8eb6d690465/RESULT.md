# An \(18+54\) projective-symmetry split for the type-\(9\) points of the Fermat cubic
## Finding
Let
\[
F:\quad x^3+y^3+z^3=0
\]
be the Fermat cubic over \(\mathbf C\), and let \(T\) be its set of \(72\) type-\(9\) points. Then the full projective automorphism group
\[
G=\operatorname{Aut}_{\mathbf P^2}(F)\cong (\mu_3)^2\rtimes S_3,
\qquad |G|=54,
\]
has exactly two orbits on \(T\), of sizes
\[
18\quad\text{and}\quad54.
\]
The smaller orbit is intrinsically
\[
T_{18}=\{[x:y:z]\in T:x^9=y^9=z^9\}.
\]
Equivalently, it is the set-theoretic intersection
\[
T_{18}=F\cap V(x^6+x^3y^3+y^6).
\]
Every point of \(T_{18}\) has projective stabilizer \(C_3\); every point of the complementary \(54\)-point orbit has trivial stabilizer.

## Assumptions and scope
All varieties and projective transformations are over \(\mathbf C\). A type-\(9\) point is used in the sense of Gattazzo: a point of a smooth plane cubic admitting an irreducible cubic with contact multiplicity \(9\). For a plane cubic these are precisely the \(9\)-torsion points that are not \(3\)-torsion points. The input from Merta--Zięba is that the Fermat cubic has exactly \(72\) such points and that their reduced set is the complete intersection of \(F\) with their displayed degree-\(24\) form
\[
\begin{aligned}
Q(x,y)={}&x^{24}+4x^{21}y^3-17x^{18}y^6-65x^{15}y^9-89x^{12}y^{12}\\
&-65x^9y^{15}-17x^6y^{18}+4x^3y^{21}+y^{24},
\end{aligned}
\]
with
\[
\begin{aligned}
Q(x,y)={}&(x^6+x^3y^3+y^6)\\
&\cdot(x^9-3x^6y^3-6x^3y^6-y^9)\\
&\cdot(x^9+6x^6y^3+3x^3y^6-y^9).
\end{aligned}
\]
No claim is made here about automorphism orbits of type-\(9\) points on a general smooth cubic.

## Proof
The Hessian determinant of \(x^3+y^3+z^3\) is a nonzero scalar multiple of \(xyz\). Any projective automorphism of \(F\) therefore preserves the Hessian triangle and permutes its three coordinate lines. Hence every projective automorphism is represented by a monomial matrix. Preservation of the Fermat equation forces the cubes of its three nonzero entries to agree. Modulo a common projective scalar, the diagonal subgroup is \((\mu_3)^2\) of order \(9\), and coordinate permutations give \(S_3\). Thus
\[
G\cong(\mu_3)^2\rtimes S_3,
\qquad |G|=54.
\]

Every type-\(9\) point has all three coordinates nonzero: Merta--Zięba identify the coordinate-zero points on \(F\) as the flexes, hence as \(3\)-torsion rather than type-\(9\) points. For
\[
P=[x:y:z]\in T,
\qquad [a:b:c]=[x^3:y^3:z^3],
\]
we have \(abc\ne0\) and \(a+b+c=0\). The diagonal subgroup \((\mu_3)^2\) acts freely on such a point, and it does not change the projective cube triple \([a:b:c]\). A permutation \(\sigma\) of the coordinates lifts to a unique projective automorphism fixing \(P\) exactly when that permutation fixes \([a:b:c]\) projectively. Indeed, if the permuted cube triple is \(\kappa[a:b:c]\), choose \(\lambda^3=\kappa\) and set \(d_i=\lambda x_i/x_{\sigma(i)}\); then \(d_i^3=1\), and changing \(\lambda\) only changes the representing matrix by a scalar. Consequently the stabilizer of \(P\) in \(G\) has the same order as the stabilizer of \([a:b:c]\) in \(S_3\).

A transposition can fix \([a:b:c]\) only if two of \(a,b,c\) are equal. This never occurs for a type-\(9\) point. Indeed, using \(t=x^3/y^3\), the source equation becomes
\[
q(t)=t^8+4t^7-17t^6-65t^5-89t^4-65t^3-17t^2+4t+1,
\]
and
\[
q(1)=-243\ne0.
\]
The same argument applies to every coordinate pair because the source gives the equal ideals \((F,Q(x,y))=(F,Q(x,z))=(F,Q(y,z))\).

A nontrivial three-cycle fixes \([a:b:c]\) projectively precisely when
\[
[a:b:c]=[1:\omega:\omega^2]
\quad\text{or}\quad
[1:\omega^2:\omega],
\]
where \(\omega^2+\omega+1=0\). These are exactly the cube triples satisfying
\[
a^3=b^3=c^3,
\]
and hence exactly the points satisfying
\[
x^9=y^9=z^9.
\]
Each of the two cube triples has \(9\) projective preimages under the coordinatewise cube map on the projective torus, because its kernel has order \(3^3/3=9\). Thus there are exactly \(18\) such points. Their permutation stabilizer is \(C_3\), so their \(G\)-orbit has size \(54/3=18\). They therefore form one orbit.

For these two cube triples, the Fermat relation also gives
\[
x^6+x^3y^3+y^6=0.
\]
Conversely, on \(F\) with nonzero coordinates, this sextic equation says that \(x^3/y^3\) is a primitive cube root of unity, and the Fermat equation forces the third cube to be the remaining primitive-root value. Hence the sextic factor cuts out exactly the same \(18\) points.

For every remaining type-\(9\) point, no nonidentity permutation fixes its cube triple projectively, so its stabilizer in \(G\) is trivial. There are \(72-18=54\) such points, equal to \(|G|\), and therefore they form one orbit of size \(54\).

## Verification
The accompanying script `verification/verify_orbits.py` uses exact symbolic arithmetic. It checks the displayed factorization of \(Q\), the value \(q(1)=-243\), the two projective cube triples and their exact \(C_3\) permutation stabilizers in \(\mathbf Q(\omega)/(\omega^2+\omega+1)\), the kernel size \(9\) of the coordinatewise cube map on the projective torus, and the resulting orbit arithmetic \(18+54=72\). The proof above, rather than finite sampling, supplies the exhaustive stabilizer argument.

A fresh replay was performed with SymPy \(1.14.0\) from the installed package path and terminated with
`VERIFY_OK group_order=54 orbit_sizes=18,54 small_stabilizer=C3 small_locus=x9=y9=z9 sextic_factor=exact`.

## Relationship to prior work
Merta--Zięba prove that the type-\(9\) locus consists of \(72\) points, give explicit coordinates, identify it as a complete intersection of type \((3,24)\), and print the factorization of the degree-\(24\) equation into one sextic and two nonics. They also study tangent cycles and conic arrangements. The inspected full text does not organize the \(72\) points into projective-automorphism orbits or identify the sextic factor as a stabilizer-defined orbit.

Szemberg--Szpond posed the explicit-coordinate and degree-\(24\) questions that Merta--Zięba answer. Gattazzo's classical work supplies the general count of type-\(9\) points on a smooth cubic. Targeted searches for projective-automorphism orbit decompositions, the \(18+54\) split, and the characterization \(x^9=y^9=z^9\) did not locate a covering statement.

## Limitations
The result concerns the projective automorphism group of this fixed plane Fermat model; it does not classify the action of larger abstract symmetries of auxiliary level structures. The originality search cannot exclude an older or poorly indexed treatment of the same \(9\)-division geometry in classical Hesse or theta-function language. The source factorization itself is prior work; the new statement is its interpretation as the exact two-orbit decomposition and the stabilizer classification.

## References
1. Łukasz Merta and Maciej Zięba, *Sextactic and type-9 points on the Fermat cubic and associated objects*, arXiv:2406.13802v1, 19 June 2024; Journal of Algebra 662 (2025), 502--513, DOI 10.1016/j.jalgebra.2024.08.013.
2. Tomasz Szemberg and Justyna Szpond, *Sextactic points on the Fermat cubic curve and arrangements of conics*, arXiv:2211.00494; Journal of Symbolic Computation 120 (2024), 102228.
3. R. Gattazzo, *Points of type 9 on an elliptic cubic*, Rendiconti del Seminario Matematico della Università di Padova 61 (1979), 285--301.
