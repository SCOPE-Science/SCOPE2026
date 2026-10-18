# Complete projective and arithmetic census of smooth plane-cubic nets over \(\mathbf F_2\)

## Finding

Let \(V=\mathbf F_2[X,Y,Z]_3\) be the ten-dimensional vector space of homogeneous ternary cubics. Call a nonzero subspace \(W\subset V\) *all-smooth* if every nonzero \(F\in W\) defines a geometrically smooth curve \(F=0\) in \(\mathbf P^2\). Then:

1. There are exactly **864** three-dimensional all-smooth subspaces \(W\) with the ambient coordinates fixed. Under \(\mathrm{PGL}_3(\mathbf F_2)\), they form **eight** orbits: five of cardinality 168 and three of cardinality 8.
2. Every one of these nets has seven geometrically smooth rational members, has no common \(\mathbf F_2\)-rational base point, and has one of exactly five sorted multisets of rational-point counts. The complete distribution is:

| Sorted values of \(\#\{F=0\}(\mathbf F_2)\) for the seven members | Number of nets |
|:--|--:|
| \((1,1,2,4,4,4,5)\) | 168 |
| \((1,1,3,3,3,5,5)\) | 168 |
| \((1,2,2,3,4,4,5)\) | 336 |
| \((2,2,2,3,3,4,5)\) | 168 |
| \((3,3,3,3,3,3,3)\) | 24 |

Asgarli--Ghioca--Reichstein already proved that **projective dimension two is the maximum** for smooth plane-cubic systems over \(\mathbf F_2\), as part of a general theorem. That maximality, and the existence of such systems, are **not** claimed as new. The contribution here is the exhaustive classification of **all** maximal nets, their eight projective orbits, five point-count strata, and rational-base-point structure. The 336 individual smooth binary plane cubics form a known input population.

## Assumptions and scope

All coefficients lie in \(\mathbf F_2\); smoothness means smooth over its algebraic closure. The three-dimensional subspaces are counted as distinct subspaces of the fixed ten-dimensional coefficient space, not modulo change of coordinates. A net is the projective plane \(\mathbf P(W)\), whose seven \(\mathbf F_2\)-rational points correspond bijectively to the nonzero cubic forms in \(W\). Every individual smooth plane cubic has genus one; the seven members need not be geometrically isomorphic. The stated eight projective orbits are of *linear systems*, not of individual elliptic curves.

For exact reproduction, order the monomials as

\[
(M_0,\ldots,M_9)=(X^3,X^2Y,X^2Z,XY^2,XYZ,XZ^2,Y^3,Y^2Z,YZ^2,Z^3)
\]

and encode \(F=\sum_i b_iM_i\) by the integer \(\sum_i b_i2^i\), with \(b_i\in\{0,1\}\). For instance, one maximal net has basis with encodings **100, 387, 537**, i.e.

\[
\begin{aligned}
F_0&=X^2Z+XZ^2+Y^3,\\
F_1&=X^3+X^2Y+Y^2Z+YZ^2,\\
F_2&=X^3+XY^2+XYZ+Z^3.
\end{aligned}
\]

All seven nonzero binary linear combinations of these three forms are geometrically smooth.

## Proof

**1. An exact geometric smoothness test.** In characteristic two, Euler's identity for a cubic gives \(F=XF_X+YF_Y+ZF_Z\). Thus a geometric singularity of \(F=0\) is exactly a nonzero projective common zero of the three quadratic partial derivatives. Let \(S=\mathbf F_2[X,Y,Z]\) and \(I=(F_X,F_Y,F_Z)\). The cubic is geometrically smooth if and only if the map

\[
\Phi_F:S_2^{\oplus3}\longrightarrow S_4,\qquad (A,B,C)\longmapsto AF_X+BF_Y+CF_Z
\]

is surjective. Indeed, surjectivity implies \(I_4=S_4\), so the partial derivatives have no common projective zero. Conversely, if they have no common projective zero, \(I\) has height three. Its three homogeneous quadratic generators form a regular sequence in the Cohen--Macaulay ring \(S\); hence \(S/I\) has Hilbert series \((1+t)^3\), and its degree-four component vanishes. The criterion is therefore equivalent to exact rank **15** for the binary matrix of \(\Phi_F\) (18 generators, 15 degree-four monomials). It is an algebraic-closure test, not a test at a finite list of extension-field points.

**2. Exhaustive enumeration without overcounting.** Apply that rank criterion to each of the \(2^{10}-1=1023\) nonzero coefficient vectors. Exactly **336** pass. A two-dimensional subspace of this set is uniquely determined by its three nonzero elements \(\{a,b,a\oplus b\}\). Enumerating all such three-element sets with all entries smooth gives exactly **5,544** all-smooth two-dimensional subspaces (pencils).

For each pencil, add a vector \(v\) outside it and accept the seven-element set

\[
\{a,b,a\oplus b,v,a\oplus v,b\oplus v,(a\oplus b)\oplus v\}
\]

precisely when all seven encodings pass the geometric rank criterion. Removing duplicates by sorting the seven nonzero elements leaves exactly **864** all-smooth three-dimensional subspaces. Any four-dimensional all-smooth subspace would contain one of these nets. For each of the 864, testing every possible vector \(v\) outside the net for all eight required new smooth translates \(v\oplus w\), with \(w\in W\), produces **zero** extensions. Thus no four-dimensional all-smooth subspace exists, and no higher-dimensional one exists either. This also independently checks the **previously published** sharp bound of Asgarli--Ghioca--Reichstein; the new finite classification does not rely on that bound. Every loop has a finite, explicitly specified domain; no statistical or heuristic step enters the conclusion.

**3. Projective equivalence.** The invertible \(3\times3\) binary matrices form \(\operatorname{GL}_3(\mathbf F_2)\), of order 168. Because its scalar subgroup is trivial, this is \(\operatorname{PGL}_3(\mathbf F_2)\). Substituting the three linear forms determined by each matrix into every cubic induces a permutation of the 864 nets. Full orbit enumeration produces the eight representative bases and orbit sizes below. The encoding convention is as above; a row specifies the span of the three encodings, not a single cubic.

| Representative basis encodings | Orbit size | Sorted rational-point counts |
|:--|--:|:--|
| `100,387,537` | 168 | \((1,2,2,3,4,4,5)\) |
| `100,387,554` | 168 | \((1,1,3,3,3,5,5)\) |
| `100,389,543` | 168 | \((2,2,2,3,3,4,5)\) |
| `100,421,523` | 8 | \((3,3,3,3,3,3,3)\) |
| `102,405,527` | 168 | \((1,1,2,4,4,4,5)\) |
| `102,405,655` | 168 | \((1,2,2,3,4,4,5)\) |
| `162,357,590` | 8 | \((3,3,3,3,3,3,3)\) |
| `162,359,620` | 8 | \((3,3,3,3,3,3,3)\) |

The orbit cardinalities add to 864. The groups stabilizing the five 168-orbits are trivial; each eight-orbit has stabilizer order 21.

**4. Arithmetic spectra and base points.** There are seven rational points of \(\mathbf P^2(\mathbf F_2)\). Direct evaluation of each of the seven members of every net at these points yields exactly the five spectra and multiplicities asserted above. An independent incidence identity explains their common sum. At any rational point \(P\), evaluation \(W\to\mathbf F_2\) is linear. If \(P\) is a base point, all seven nonzero forms vanish; otherwise its kernel contains exactly three nonzero forms. Thus, writing \(b\) for the number of rational base points,

\[
\sum_{0\ne F\in W}\#\{F=0\}(\mathbf F_2)=21+4b.
\]

Each of the five enumerated spectra has sum 21, forcing \(b=0\) for every all-smooth net. This claim is only about rational base points, not the complete geometric base locus.

## Verification

Both standalone scripts are included alongside this report and need only standard Python. Run from the package root:

```bash
python3 code/verify_cubic_nets.py
python3 code/check_smooth_by_extensions.py
```

The first reconstructs the exact Macaulay maps, rank-tests all 1,023 nonzero cubic forms, enumerates all smooth pencils, nets and attempted four-dimensional extensions, applies all 168 projective substitutions, and computes seven-member rational-point spectra. Expected principal results: smooth cubic forms **336**; all-smooth pencils **5,544**; all-smooth nets **864**; four-dimensional extensions **0**; orbit lengths **8,8,8,168,168,168,168,168**. All are asserted directly by the supplied program.

The second independently implements polynomial differentiation and finite-extension point testing, retaining exactly the same 336 smooth cubics after checking degrees one through four. Extension-field testing alone is **not** an infinite geometric smoothness proof. Only the proven Macaulay-map criterion justifies the complete geometric conclusion.

## Relationship to prior work

Asgarli, Ghioca and Reichstein, *Linear Families of Smooth Hypersurfaces over Finitely Generated Fields*, arXiv:2207.00918 (first public July 2, 2022), **already prove** that for plane cubics over \(\mathbf F_2\) the maximal all-smooth projective dimension is exactly two. Their Theorem 2 supplies the upper bound in any field and existence over finite fields when the characteristic does not divide \(\gcd(d,n+1)\). Neither their theorem nor the inspected proof contains a census of the 864 maximal binary nets, their eight projective orbits, or the five seven-member point-count spectra. The already-known maximality is context and a cross-check, not part of the novel claim.

Asgarli and Ghioca, *Smoothness in Pencils of Hypersurfaces over Finite Fields*, arXiv:2203.07169 (March 14, 2022), pose the broader parameterized Question 1.1 and treat the conic examples. Their question motivates the enumeration, but their examples do not determine the cubic-net strata.

Asgarli and Ghioca, *Linear System of Geometrically Irreducible Plane Cubics over Finite Fields*, arXiv:2407.18104 (July 25, 2024), explicitly cite the Asgarli--Ghioca--Reichstein theorem as a **previously resolved** smooth-cubic maximal-dimension result. Their own complete arithmetic study concerns **geometric irreducibility**, a weaker requirement than smoothness, and the appendix tabulates example four-generator systems that are geometrically irreducible rather than a full simultaneous smoothness classification. In particular, their statement on maximal dimension is already known and does not imply this new eight-orbit census.

Ishitsuka, *Linear Determinantal Representations of Smooth Plane Cubics over Finite Fields*, arXiv:1604.00115, analyzes projective equivalence classes of **individual** smooth plane cubics. Those results do not determine which sets of seven cubic forms span a jointly all-smooth net, nor the number or orbit structures of the nets.

Hattori, Papazachariou and Zanardini, *Nets of Quadric Surfaces and Plane Cubics and Their GIT Stability*, arXiv:2603.17521 (2026), treat GIT stability and Gale correspondences. GIT stability, or smoothness of a general member, does not entail that **each \(\mathbf F_2\)-rational member** is geometrically smooth. Their stated results do not supply this net census.

## Limitations

The classification is over the fixed ground field \(\mathbf F_2\) and concerns simultaneous smoothness of **the rational members** of a linear system. The discriminant will generally intersect the geometric parameter plane at nonrational points, so not every geometric member is asserted smooth. The eight orbit counts are under projective coordinate changes; no classification modulo arbitrary birational transformations is claimed. The computed rational-point spectra do not assert isomorphism or isogeny classifications of the individual members. The finite certificate is independently reproducible but has not received an external mathematical audit. Searches did not identify an equivalent earlier census, but absence from searchable literature cannot establish absolute novelty.

## References

1. S. Asgarli, D. Ghioca and Z. Reichstein, *Linear Families of Smooth Hypersurfaces over Finitely Generated Fields*, arXiv:2207.00918 (July 2, 2022), Theorem 2. https://arxiv.org/pdf/2207.00918
2. S. Asgarli and D. Ghioca, *Smoothness in Pencils of Hypersurfaces over Finite Fields*, arXiv:2203.07169v1 (March 14, 2022), especially Question 1.1 and Examples 1.5–1.6. https://arxiv.org/pdf/2203.07169
3. S. Asgarli and D. Ghioca, *Linear System of Geometrically Irreducible Plane Cubics over Finite Fields*, arXiv:2407.18104v1 (July 25, 2024), Theorem 2 and Appendix A. https://arxiv.org/pdf/2407.18104
4. Y. Ishitsuka, *Linear Determinantal Representations of Smooth Plane Cubics over Finite Fields*, arXiv:1604.00115 (April 1, 2016). https://arxiv.org/pdf/1604.00115
5. M. Hattori, T. S. Papazachariou and A. Zanardini, *Nets of Quadric Surfaces and Plane Cubics and Their GIT Stability*, arXiv:2603.17521 (March 18, 2026). https://arxiv.org/pdf/2603.17521
