# Exact prime-field rational singular support of the 33-line octagon arrangement

## Finding

Let \(K=\mathbb Q(\rho)\), with \(\rho^2=2\). Consider the 33-line arrangement \(\mathcal O_{33}\) defined by the integral coefficient triples in `verify.py`, which transcribe the explicit regular-octagon closure of Pokora--Roulleau. The singular support is the set of geometric points lying on at least two **distinct** component lines. The exact arithmetic of this support is as follows.

Over \(\mathbb Q\), **exactly nine of the 169 distinct geometric intersection points are rational**. They are the nine points
\[
\begin{gathered}
[1:0:0],\ [0:1:0],\ [0:0:1],\\
[1:1:0],\ [1:-1:0],\ [1:0:1],\ [1:0:-1],\ [0:1:1],\ [0:1:-1].
\end{gathered}
\]
The other 160 points are individually defined over \(K\) but not over \(\mathbb Q\). Thus \(K\) is the minimal common field of definition of all 169 points. The nine rational points form the dual point configuration of the nine reflection hyperplanes of type \(B_3\).

For any prime \(p\), choose a geometric root of \(T^2-2\) and reduce the 33 integral line forms at that root. Let \(N_p\) count distinct \(\mathbb F_p\)-rational points belonging to the **geometric singular support**. Then
\[
N_p=\begin{cases}
6,&p=2\text{ (reduced five-line support)},\\
13,&p=3,\\
57,&p=7,\\
169,&p\ge5,\ p\ne7,\ \left(\frac2p\right)=1,\\
9,&p\ge5,\ p\ne7,\ \left(\frac2p\right)=-1.
\end{cases}
\]
The result does not depend on the choice of geometric root. Among primes outside the exceptional set, the two values 169 and 9 each occur with natural prime density \(1/2\). In characteristic 3, the singular support contains **every** point of \(\mathbb P^2(\mathbb F_3)\), while in characteristic 7 it contains **every** point of \(\mathbb P^2(\mathbb F_7)\). In characteristic 2, the reduced support consists of five distinct lines with six singular points, four ordinary double points and two ordinary triple points.

## Assumptions and scope

The construction uses the specified coordinate presentation, not an arbitrary projectively transformed integral model. Each line has coefficients in \(\mathbb Z[\rho]\). The 33 coefficient triples in `verify.py` are complete defining data; every tuple \((a,b)\) encodes \(a+b\rho\), and a triple of such tuples gives a linear equation in the projective coordinates. At a prime of inert reduction, the line arrangement itself is generally defined over \(\mathbb F_{p^2}\), but asking whether a geometric singular point has its coordinates in \(\mathbb F_p\) is nevertheless well-defined. At \(p=2\), repeated component lines are discarded before forming the reduced singular support. There is no claim about the scheme structure of singularities of a nonreduced product.

## Proof

**1. Exact arithmetic setup.** Work in the free rank-two integer algebra \(\mathbb Z[\rho]\), with multiplication induced by \(\rho^2=2\) and norm \(\operatorname N(a+b\rho)=a^2-2b^2\). For a line coefficient vector \(L_i\), every pair intersection is represented by \(P_{ij}=L_i\times L_j\); three lines concur exactly if their determinant is zero.

**2. Universal pair distinctness and incidence stability.** Among all \(\binom{33}{2}=528\) pairs, the positive prime divisors of the greatest common divisor of the three cross-product coordinate norms belong only to \(\{2\}\). Thus the 33 lines remain pairwise distinct at every odd prime. Of all \(\binom{33}{3}=5456\) triple determinants, exactly 480 vanish in \(\mathbb Z[\rho]\); the nonzero determinants have algebraic norms with positive prime divisors only in \(\{2,3,7\}\). Consequently every incidence of distinct lines is unchanged upon reduction at \(p\ge5\), \(p\ne7\). Exhaustively grouping the pair intersections by their exact incident-line sets gives 169 distinct points with multiplicities \((n_2,n_3,n_5,n_8)=(108,40,16,5)\). The determinant test proves this statement for **all** qualifying primes rather than only those sampled.

**3. The rational points over the number field.** For each of the 169 exact cross-product representatives \(P\), apply the nontrivial conjugation \(\sigma(\rho)=-\rho\). A projective point \(P\) is \(\mathbb Q\)-rational if and only if \(P\times\sigma(P)=0\). Exactly nine of the 169 pass this criterion, and their coordinates are precisely those displayed above. For each of the other 160 representatives, take the greatest common divisor of the integer norms of all three coordinates of \(P\times\sigma(P)\). Every resulting positive prime divisor belongs to \(\{2,3\}\). Therefore for every prime \(p\ge5\) this cross-product cannot vanish after reduction. The nine rational points remain distinct at these primes unless incidence data change, which is already excluded away from \(p=7\).

**4. Split and inert prime counts.** When \(2\) is a quadratic residue modulo a prime \(p\ge5\), all 33 lines and hence all their intersections are defined over \(\mathbb F_p\). Away from characteristic 7, there are exactly 169. When \(2\) is a nonresidue, Frobenius on \(\mathbb F_{p^2}\) acts as \(\sigma\) on the reduced coefficient field. By step 3 exactly nine intersection points are Frobenius-fixed, yielding \(N_p=9\). Their number-field coordinates persist and are explicitly rational; the remaining 160 cannot acquire accidental Frobenius fixity for these primes.

**5. Exceptional fibers.** In characteristic 3, direct exhaustive pairwise cross products over \(\mathbb F_9=\mathbb F_3[\rho]/(\rho^2-2)\) give 89 geometric intersections, with multiplicity counts \((n_2,n_3,n_4,n_5,n_8)=(12,40,16,16,5)\), and exactly 13 have normalized coordinates in \(\mathbb F_3\). In characteristic 7, for either root of \(T^2-2\), the same exhaustive construction over \(\mathbb F_7\) gives 57 points, with \((n_2,n_4,n_5,n_8)=(4,24,24,5)\). All these points are \(\mathbb F_7\)-rational. The equalities \(\#\mathbb P^2(\mathbb F_3)=13\) and \(\#\mathbb P^2(\mathbb F_7)=57\) give the saturation assertions. In characteristic 2, \(\rho\) specializes to 0; the normalized 33 equations specialize to precisely \(x=0\), \(y=0\), \(z=0\), \(x+y=0\), and \(x+y+z=0\). Their reduced singular support has six rational points, consisting of four double and two triple intersections.

**6. Densities.** For odd primes, quadratic reciprocity shows \(\left(\frac2p\right)=1\) exactly when \(p\equiv1,7\pmod8\). Dirichlet's theorem supplies density \(1/2\) for that union of two reduced residue classes, and density \(1/2\) for the complementary union \(p\equiv3,5\pmod8\). The finitely many exceptional primes do not affect these densities.

## Verification

The accompanying self-contained `verify.py` uses only the Python standard library. Execute `python3 verify.py`. It carries the original 33 exact line equations, checks 528 pair-cross-product norm gcds, all 5,456 triple determinants, the complete 169-point incidence partition, the nine fixed points and the conjugation obstruction norms, and all exceptional finite-field point counts. It also checks representative ordinary split and inert primes as consistency tests. Expected final output begins with `VERIFY_OK:`. These finite-field checks are supplements to the prime-support proof; the latter supplies the infinite-prime quantifier.

## Relationship to prior work

Pokora and Roulleau constructed the 33-line octagon arrangement, proved its characteristic-zero freeness and determined its complex incidence multiplicities (Theorem B and the 33 line equations in arXiv:2403.20024v1). Those established geometric facts, as well as the modular incidence multiplicity tables, are not presented as new here. Kühne and Roulleau analyzed related polygonal line operators and matroid realization spaces (arXiv:2312.03470); that work addresses different modular geometric structures. The contribution here is the **complete individual point-of-definition profile** of the 169 intersections and the exact number of rational singular points over every prime field, including the six-point reduced characteristic-two case. Combinatorial incidence counts alone do not determine this arithmetic profile.

## Limitations

The rational-point counts are for the displayed integral model and concern reduced geometric support, not multiplicity-weighted schemes. Freeness after reduction, étale specialization of singularity schemes, and arithmetic for other presentations are not asserted. Originality was checked against the cited available full texts and relevant indexed records; unindexed arithmetic calculations on the same arrangement remain a bibliographic risk. No independent verification has been performed.

## References

1. P. Pokora and X. Roulleau, *Construction of free arrangements using point-line operators*, arXiv:2403.20024v1, first public 2024-03-29; especially Theorem B and the 33 defining line equations. https://arxiv.org/abs/2403.20024
2. L. Kühne and X. Roulleau, *Regular polygons, line operators, and elliptic modular surfaces as realization spaces of matroids*, arXiv:2312.03470v1, first public 2023-12-06. https://arxiv.org/abs/2312.03470
