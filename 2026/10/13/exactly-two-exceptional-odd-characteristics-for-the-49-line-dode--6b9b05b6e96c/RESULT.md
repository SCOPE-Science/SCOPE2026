# Exactly two exceptional odd characteristics for the 49-line dodecagon arrangement

## Finding
Let \(\mathcal O_{49}\) be the 49-line arrangement obtained by joining the intersection points of the twelve extended sides of a regular dodecagon and retaining precisely the lines through at least four of the original side-pair intersections. The exact **geometric intersection-point multiplicity distribution** after reduction is:

| Characteristic | \(n_2\) | \(n_3\) | \(n_4\) | \(n_5\) | \(n_6\) | \(n_7\) | \(n_{12}\) | Total |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| \(p\ge5,\ p\notin\{11,13\}\) | 204 | 96 | 6 | 24 | 6 | 12 | 1 | 349 |
| \(p=11\) | 24 | 12 | 18 | 60 | 6 | 12 | 1 | 133 |
| \(p=13\) | 0 | 96 | 30 | 12 | 18 | 12 | 1 | 169 |

Here \(n_m\) counts geometric points lying on exactly \(m\) component lines. Every reduction has 49 **distinct** lines. Thus the rank-three incidence matroid, or equivalently the entire intersection lattice, agrees with characteristic zero at every prime \(p\ge5\) **except exactly 11 and 13**.

## Assumptions and scope
Work in \(K=\mathbb Q(\sqrt3)\), with ring of integers \(\mathbb Z[\sqrt3]\). Let the polygon's vertices be \(V_j=[2\cos(j\pi/6):2\sin(j\pi/6):2]\) for \(0\le j<12\); their coordinates lie in \(\mathbb Z[\sqrt3]\). Let \(S_j\) be the line through \(V_j,V_{j+1}\), indices taken modulo 12, and \(T\) the set of projective intersections of distinct \(S_j\). There are 66 points in \(T\). Let \(\mathcal O_{49}\) be the set of all distinct lines through at least four points of \(T\); direct calculation gives 49 lines. This is the fixed arrangement described by Pokora and Roulleau, not a newly recomputed closure after reduction. For each component, clear rational denominators and divide the six integer coefficients by their common integer gcd. Reduce the resulting primitive triples under either homomorphism \(\mathbb Z[\sqrt3]\rightarrow\overline{\mathbb F}_p\) for \(p\ge5\). The theorem counts points over an algebraic closure of the residue field; it makes no claim about their being \(\mathbb F_p\)-rational. Primes 2 and 3 are excluded.

## Proof
Represent \(a+b\sqrt3\) as the ordered pair \((a,b)\), with product \((a,b)(c,d)=(ac+3bd,ad+bc)\). In homogeneous coordinates, line joins and intersections are ordinary vector cross products over this ring. Normalize nonzero vectors by their first nonzero entry during characteristic-zero enumeration. The twelve side lines have 66 pairwise distinct intersections. Joining every pair of these 66 points yields 913 candidate lines; exactly 49 contain at least four points of the seed set, with seed-incidence richness distribution \(4^{24},5^6,6^7,11^{12}\). Thus the construction is exhaustive.

The 49 lines give \(\binom{49}{2}=1176\) pairs. The distinct points formed from their pairwise intersections number 349, with the first-row multiplicity distribution. The weighted identity \(\sum_{m\ge2}\binom m2 n_m=1176\) verifies that the pairs have been partitioned exhaustively.

Now choose the primitive integral coefficient vectors specified above. For an algebraic integer \(u=a+b\sqrt3\), the field norm is \(N(u)=a^2-3b^2\). For each of the 49 line triples, the gcd of the absolute norms of its three coefficients has prime support contained in \(\{2,3\}\). The same statement holds for the three coordinates of the cross product of **every** pair of distinct line triples. Consequently, for any prime \(p\ge5\), no line reduces to the zero vector and no two distinct lines coalesce under either residue-field embedding.

Finally, enumerate all \(\binom{49}{3}=18424\) unordered triples of line equations. Exactly 1120 determinants vanish in characteristic zero. The absolute norms of the nonzero determinants take exactly 60 values, with largest value 1944, and their combined prime support is **exactly** \(\{2,3,11,13\}\). If \(p\ge5\) lies outside \(\{11,13\}\), every formerly nonzero triple determinant remains nonzero under every residue-field embedding, while zero determinants remain zero. Since all lines remain distinct, every rank-three dependence and hence the complete intersection lattice is unchanged.

At the two remaining primes, \(3\) is a square: \(\sqrt3\equiv\pm5\pmod{11}\) and \(\sqrt3\equiv\pm4\pmod{13}\). For both roots at both primes, enumerate the distinct cross products of all 1176 unordered pairs of specialized lines and count how many component lines contain each resulting point. The resulting histograms are exactly the second and third rows of the table. They satisfy the same weighted identity 1176, and differ from the characteristic-zero histogram, proving both exceptional primes really are exceptional.

## Verification
Run `python3 verify_dodecagon.py` with Python 3.10 or later; the verifier depends only on the standard library. It rebuilds the polygon and all 49 derived lines, checks all 66 initial intersections, 913 joining candidates, all 18424 triple determinants, the coefficients' nonvanishing and pairwise distinctness outside primes 2 and 3, and both embeddings at primes 11 and 13. It additionally tests prime 23 as a nonexceptional split-field witness. The output ends with `VERIFY_OK`. The proof for all primes rests on integer determinant norms and their complete prime factorization, **not** on sampling finitely many primes. A human-readable independent algebraic proof of the 60-value enumeration is not supplied; instead, it is a finite exact calculation reproduced from the construction by the included exhaustive code.

## Relationship to prior work
Pokora and Roulleau, *Construction of free arrangements using point-line operators*, arXiv:2403.20024, Remark 2.5, construct the 49-line arrangement from the regular twelve-gon and give its characteristic-zero multiplicity distribution and rigidity. Their result implies the first table row only in characteristic zero; it neither implies that 11 and 13 are precisely the new bad primes nor supplies the two degeneration rows. Kühne and Roulleau, *Regular polygons, line operators, and elliptic modular surfaces as realization spaces of matroids*, arXiv:2312.03470, study related polygonal matroid realization spaces and include positive-characteristic considerations, but do not classify reduction of this fixed 49-line closure. The mathematical contribution here is the complete arithmetic bad-characteristic classification of this particular arrangement, not its construction, complex incidence counts, rigidity, or projective symmetry.

## Limitations
Only the specified integral model of the 49 characteristic-zero lines is reduced; a fresh application of the incidence closure operator in finite characteristic may produce other lines. The counts are geometric, not rational-point counts. Freeness after reduction, the behavior in characteristics 2 and 3, and uniqueness of models under arbitrary arithmetic projective changes are not asserted. Prior unindexed calculations may overlap this arithmetic classification, so bibliographic completeness cannot be guaranteed.

## References
1. P. Pokora and X. Roulleau, *Construction of free arrangements using point-line operators*, arXiv:2403.20024v1 (first available 2024-03-29), Remark 2.5. https://arxiv.org/html/2403.20024v1
2. L. Kühne and X. Roulleau, *Regular polygons, line operators, and elliptic modular surfaces as realization spaces of matroids*, arXiv:2312.03470 (first available 2023-12-06), Sections 1, 3 and 4. https://arxiv.org/html/2312.03470v3
