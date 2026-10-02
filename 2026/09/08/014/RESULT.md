# Cup-trivial but Massey-nonformal balanced presentation 2-complex

## Finding

Let \(K\) be the presentation 2-complex
\[
\langle x,y,z\mid r_1=x^2[y,z]^2,\ r_2=[x,z],\ r_3=[[x,y],z]\rangle,
\qquad [u,v]=uvu^{-1}v^{-1}.
\]
It has one vertex, three edges and three 2-cells. All positive-degree integral cup products vanish, but its singular-cochain differential graded algebra is nonformal over both \(\mathbb Z\) and \(\mathbb Q\). For classes \(Y,Z\) dual to \(y,z\), all eight degree-one triple Massey products have zero indeterminacy. In relator-oriented cellular coordinates, with the first coordinate reduced modulo 2, they are:

| Triple | Value in \(H^2(K;\mathbb Z)\) |
|---|---|
| \(\langle Y,Y,Y\rangle\) | \((0,0,0)\) |
| \(\langle Y,Y,Z\rangle\) | \((0,0,0)\) |
| \(\langle Y,Z,Y\rangle\) | \((0,0,0)\) |
| \(\langle Y,Z,Z\rangle\) | \((0,1,0)\) |
| \(\langle Z,Y,Y\rangle\) | \((0,0,0)\) |
| \(\langle Z,Y,Z\rangle\) | \((0,-2,0)\) |
| \(\langle Z,Z,Y\rangle\) | \((0,1,0)\) |
| \(\langle Z,Z,Z\rangle\) | \((0,0,0)\) |

## Assumptions and scope

This is a finite balanced presentation 2-complex, not a manifold. The homology and cohomology groups are
\[
H_1=\mathbb Z/2\oplus\mathbb Z^2,\quad H_2=\mathbb Z^2,\quad
H^1=\mathbb Z\{Y,Z\},\quad H^2=\mathbb Z/2\oplus\mathbb Z^2.
\]
The Massey sign convention is Dwyer's unitriangular convention with first superdiagonal \(-\alpha,-\beta,-\gamma\). Reversing a 2-cell orientation changes its displayed coordinate sign, not nonvanishing. No universal minimal-cell or historical-first claim is made.

## Proof

The exponent-sum matrix is \(\operatorname{diag}(2,0,0)\), giving the groups above and degree-one coboundary image \((2\mathbb Z,0,0)\). Augmented second Magnus/Fox matrices, in generator order \(x,y,z\), are
\[
\begin{pmatrix}1&0&0\\0&0&2\\0&-2&0\end{pmatrix},\quad
\begin{pmatrix}0&0&1\\0&0&0\\-1&0&0\end{pmatrix},\quad
\begin{pmatrix}0&0&0\\0&0&0\\0&0&0\end{pmatrix}.
\]
These give the recorded cocycle-cup representatives \(YY=ZZ=0\), \(YZ=(2,0,0)\), \(ZY=(-2,0,0)\), all zero modulo coboundaries. Their vanishing is also proved independently below without extending a commutator-relator Fox theorem to \(r_1\). No second-Fox bilinear formula is used on noncocycle bounding cochains.

### Integer bar cochains and the matrix bridge

Let \(G=\pi_1K\). Use normalized inhomogeneous group cochains with trivial coefficients in \(R=\mathbb Z\) or \(\mathbb Q\). For a one-cochain \(s\),
\[
\delta s(g,h)=s(h)-s(gh)+s(g),\qquad
(\alpha\smile\beta)(g,h)=\alpha(g)\beta(h).
\]
A homomorphism \(G\to U_4(R)/\langle I+rE_{14}\rangle\) with first superdiagonal \(-\alpha,-\beta,-\gamma\) has entries \(-s,-t\) in positions 13 and 24. Matrix multiplication gives exactly
\[
\delta s=\alpha\smile\beta,\qquad \delta t=\beta\smile\gamma.
\]
Thus it supplies genuine defining-system bounding cochains. Its triple cocycle is
\[
\lambda(g,h)=\alpha(g)t(h)+s(g)\gamma(h).
\]
The Leibniz rule gives \(\delta\lambda=-\alpha\smile\beta\smile\gamma+\alpha\smile\beta\smile\gamma=0\). Choosing central entry zero as a section of the matrix quotient shows directly that \(\lambda\) is its central-extension two-cocycle: the central defect in the product of two section matrices is the displayed expression. This uses neither finite coefficients nor profinite continuity. Fenn–Sjerve Theorem 3.1 and its proof give the discrete-group integer correspondence.

For triples, use Dwyer's defining-system correspondence with homomorphisms
\(G\to U_4(\mathbb Z)/Z(U_4(\mathbb Z))\). The class is the central obstruction to lifting to \(U_4(\mathbb Z)\). Write
\[
a=\alpha(y),\ b=\beta(y),\ c=\gamma(y),\quad
d=\alpha(z),\ e=\beta(z),\ f=\gamma(z).
\]
All these classes kill \(x\). The relation \(r_1\) forces the second-superdiagonal entries of the image of \(x\) to be
\[
x_{13}=-(ae-db),\qquad x_{24}=-(bf-ec).
\]
These equations hold for every defining system, regardless of the freely chosen second-superdiagonal entries of \(y,z\). The central defect of \(r_2\) is therefore
\[
x_{13}z_{34}-z_{12}x_{24}=aef-2dbf+dec.
\]
The image of \([x,y]\) is central, so \(r_3\) has zero defect.

Set all other second-superdiagonal entries of \(y,z\) and all initially free central entries to zero. Exact matrix evaluation gives, in table order, central relator vectors
\[
(0,0,0),(0,0,0),(2,0,0),(2,1,0),
(-2,0,0),(-2,-2,0),(0,1,0),(0,0,0).
\]
All relators are central, so these images define homomorphisms to the quotient for every six integer coefficients \(a,b,c,d,e,f\). Projection to the upper-left \(U_3\) block gives \(\delta s=\alpha\smile\beta\) for any pair \(\alpha,\beta\), proving that every degree-one cup vanishes already on \(G\), and therefore on \(K\). All other positive-degree cups vanish by dimension.

For the cellular coordinates, lift the generator images to \(U_4\). Around an oriented 2-cell the product of these lifts is central; its exponent is the obstruction to extending the lift over the cell. Changing generator lifts by central integers changes that cochain by the exponent-sum matrix, namely \((2\mathbb Z,0,0)\). Thus it represents the pulled-back central-extension class \([\lambda]\) without a commutator-subgroup hypothesis on the relators. With the zero choices specified above, the first defect is always twice an integer and the last is zero. Reduction modulo \((2\mathbb Z,0,0)\) gives the complete table, including its torsion coordinate. Triple indeterminacy is \(\alpha H^1+H^1\gamma=0\); the three nonzero middle coordinates cannot be removed by changing the defining system.

The classifying map \(K\to BG\) induces an isomorphism on \(H^1\) and an injection on \(H^2\): \(BG\) is obtained by attaching cells of dimension at least 3. Group triple products pull back to those of \(K\); both have zero indeterminacy. The nonzero middle coordinate survives over \(\mathbb Q\). Under differential-graded-algebra quasi-isomorphisms a defined triple with zero indeterminacy is preserved; in the zero-differential cohomology algebra, zero bounding cochains give value zero. The strict nonzero triple consequently obstructs formality over both rings.

## Verification

Run python artifacts/verify.py --check. The exact stdlib-only verifier recomputes presentation exponents, second Magnus/Fox coefficients for cocycle cups, all eight integer unitriangular relator vectors, and equality with artifacts/results.json. Its final line is VERIFY_OK: corrected U4 integral triple table and cocycle cups.

The unitriangular proof, not a second-Fox bilinear expression on bounding noncocycles, supplies the triple-product calculation.

## Relationship to prior work

Dwyer's theorem supplies a general method, not this exact example. Fenn–Sjerve Section 3 supplies the integer discrete-group bridge; its Section 4 numerical commutator-relator formulas do not directly cover \(r_1\), whose \(x\) exponent sum is 2. The contribution is this explicit balanced witness and its integral triple table. The earlier table's zero value for \(\langle Z,Y,Z\rangle\) and negative middle coordinate for \(\langle Z,Z,Y\rangle\) are corrected here; the principal cup-trivial nonformality conclusion survives.

## Limitations

Bounded searches cannot exclude an unindexed earlier identical presentation. No global historical priority, smallest-complex classification, proof-assistant verification, or external expert attestation is claimed.

## References

- W. G. Dwyer, *Homology, Massey products and maps between groups* (1975), [DOI:10.1016/0022-4049(75)90006-7](https://doi.org/10.1016/0022-4049(75)90006-7).
- J. Mináč and N. D. Tân, *Triple Massey products and Galois theory*, [primary published text](https://ems.press/content/serial-article-files/32174), Theorem 3.1, restating Dwyer's correspondence.
- R. Fenn and D. Sjerve, *Massey products and lower central series of free groups*, [primary published text](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/291C7ED73FAF27895E70B09BFBFA8942/S0008414X00005071a.pdf/massey_products_and_lower_central_series_of_free_groups.pdf), Theorem 3.1 with proof, and Section 4.
