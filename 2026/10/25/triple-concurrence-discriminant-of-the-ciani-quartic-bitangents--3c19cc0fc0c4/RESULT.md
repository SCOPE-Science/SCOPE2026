# Triple-concurrence discriminant of the Ciani quartic bitangents

## Finding
For every complex parameter \(\lambda\notin\{-2,-1,2\}\), let \(C_\lambda\subset\mathbb P^2_{\mathbb C}\) be the smooth plane quartic
\[
 x^4+y^4+z^4+\lambda(x^2y^2+x^2z^2+y^2z^2)=0.
\]
Let \(n_j(\lambda)\) be the number of points incident to exactly \(j\) of its 28 distinct bitangent lines, counting hyperflex lines as bitangents. Define the following polynomials:
\[
 P_4(\lambda)=\lambda+5,
\]
\[
\begin{aligned}
P_{12}(\lambda)={}&(25\lambda+34)(\lambda+10)(\lambda^2-\lambda+2)\\
&\cdot(\lambda^3+2\lambda^2+4\lambda+4)\\
&\cdot(\lambda^3-4\lambda^2+13\lambda+34),
\end{aligned}
\]
\[
\begin{aligned}
P_{24}(\lambda)={}&(5\lambda+6)(\lambda^2+3\lambda+6)\\
&\cdot(\lambda^3+13\lambda^2+64\lambda+68)\\
&\cdot(\lambda^3-2\lambda^2+60\lambda+72)\\
&\cdot(\lambda^4-\lambda^3+10\lambda^2+4\lambda+8).
\end{aligned}
\]
The *complete intersection-multiplicity distribution* of the bitangent arrangement is:

| Condition on \(\lambda\) | \(n_2\) | \(n_3\) | \(n_4\) |
| --- | ---: | ---: | ---: |
| \(P_4(\lambda)=0\) | 312 | 4 | 9 |
| \(P_{12}(\lambda)=0\) | 288 | 12 | 9 |
| \(P_{24}(\lambda)=0\) | 252 | 24 | 9 |
| \(\lambda=0\) | 288 | 0 | 15 |
| \(\lambda^2+3\lambda+18=0\) | 252 | 0 | 21 |
| All remaining smooth parameters | 324 | 0 | 9 |

All the displayed exceptional conditions are disjoint on the smooth locus. There are exactly **24 smooth complex parameters with triple bitangent concurrence**: one root of \(P_4\), ten roots of \(P_{12}\), and thirteen roots of \(P_{24}\). There are no points incident to five or more bitangents for any smooth parameter. In particular the ordinary triple points form a new, finite incidence-jump stratum that is absent in the three previously tabulated special quartics.

## Assumptions and scope
The base field is \(\mathbb C\), characteristic zero. The parameter is finite. The quartic is smooth exactly when \(\lambda\notin\{-2,-1,2\}\). Counts refer to intersections of its 28 **distinct lines** in the ambient plane, not to tangency points of those lines on the quartic, and a point is counted only at its exact number of incident lines. The claim covers every smooth parameter, including algebraic exceptional roots and the generic transcendental parameter.

## Proof
**1. Uniform parametrization of all 28 lines.** Choose any \(t\in\mathbb C\) satisfying
\[
 \lambda=-\frac{2(t^4+1)}{(t^2+1)^2},\qquad a=\frac{t^2-1}{t^2+1}.
\]
For every smooth \(\lambda\), the associated quartic in \(t\) has four nonzero roots with \(t^2+1\ne0\); they are related by \(t\mapsto-t\) and \(t\mapsto1/t\). The following 28 projective lines are independent of that choice as an unordered set:

* Four lines \(x+\epsilon y+\delta z=0\), where \(\epsilon,\delta\in\{1,-1\}\).
* Twelve coordinate-pair lines. For each unordered coordinate pair \((X_i,X_j)\), take \(X_i\pm tX_j=0\) and \(tX_i\pm X_j=0\).
* Twelve lines. For every distinguished coordinate \(X_i\), with the remaining coordinates \(X_j,X_k\) ordered increasingly, take \(\eta aX_i+X_j+\epsilon X_k=0\), where \(\eta,\epsilon\in\{1,-1\}\).

For the first four lines, set \(Q=x^2+y^2+z^2\) and \(P=-x^4-y^4-z^4+2(x^2y^2+x^2z^2+y^2z^2)\). Then \(P\) is, up to the displayed sign normalization, the product of the four linear equations and
\[
 F_\lambda=\frac{\lambda+2}{4}Q^2+\frac{\lambda-2}{4}P.
\]
Thus its restriction to any of these lines is a square. For a coordinate-pair line, the restriction is a quadratic polynomial in the square of the omitted coordinate, and the required square identity follows from
\[
\lambda(t^2+1)^2+2(t^4+1)=0.
\]
For a line of the third type, after scaling and permuting the coordinates, put \(y=-x-uz\), and write the restriction as \(r_4w^4+r_2w^2+r_0\), with \(w=x+uz/2\). A direct expansion gives
\[
 4r_4r_0-r_2^2=4(\lambda-2)(u^2-1)(\lambda+u^2+1).
\]
The third family has \(u^2=a^2=-\lambda-1\), so this also vanishes. On the smooth locus the 28 displayed lines are pairwise distinct: no cross-family coincidence is possible unless \(a=0\) or \(a=\pm1\), and the coordinate-pair slopes are distinct unless \(t\in\{0,\pm1,\pm i\}\); all these cases are excluded by smoothness or a pole. A smooth complex plane quartic has exactly 28 distinct bitangents (including hyperflex lines), so these are all of them.

**2. Exhaustive concurrency certificate.** Represent each line by its homogeneous coefficient vector in \(\mathbb Q[t]^3\), clearing \(t^2+1\) where appropriate. For each of the \(\binom{28}{3}=3276\) unordered triples, compute its \(3\times3\) determinant. Exactly 36 triple determinants are identically zero. Of the remaining 3240, exact factorization gives 45 different monic irreducible factors in \(\mathbb Q[t]\). One factor \(t^2+1\) arises only from cleared denominators and never corresponds to a finite parameter. For every other factor \(g(t)\), eliminate \(t\) against
\[
 \lambda(t^2+1)^2+2(t^4+1)=0
\]
using the resultant, and take the unique nonconstant irreducible factor in \(\mathbb Q[\lambda]\). The resulting 16 distinct irreducible parameter polynomials are precisely the thirteen irreducible factors of
\[
 \lambda(\lambda^2+3\lambda+18)P_4(\lambda)P_{12}(\lambda)P_{24}(\lambda)
\]
together with the three singular-parameter factors \(\lambda+2\), \(\lambda+1\), and \(\lambda-2\). The 13 smooth factors are squarefree and pairwise coprime, and none vanishes at a singular parameter.

For each irreducible factor \(g(t)\) above a smooth exceptional parameter, a triple of lines is concurrent exactly when its determinant is identically zero or divisible by \(g(t)\). For each distinct pair of lines, collect the pair and every third line concurrent with it. These sets are exactly the intersection points; each line pair belongs to exactly one such set. Exhaustive exact-rational-polynomial arithmetic produces, for every factor in each stratum, the table of \((n_2,n_3,n_4)\) given above. In the generic case it yields \((324,0,9)\). The identity
\[
 n_2+3n_3+6n_4=\binom{28}{2}=378
\]
holds in every smooth case; no higher-multiplicity point occurs. These are finite exact polynomial calculations, not sampling of numerical roots. Complete executable source is provided in `verify.py` and regenerates all 3276 determinants, their factors, the parameter resultants, coprimality checks and intersection counts.

**3. Excluded parameters.** The singular locus follows directly from the three partial derivatives \(2x(2x^2+\lambda(y^2+z^2))\) and its cyclic analogues. For \(\lambda\notin\{-2,-1,2\}\), simultaneous vanishing with \(F_\lambda\) is impossible. At \(\lambda=2\) the quartic is a doubled conic, at \(\lambda=-2\) a product of four lines, and at \(\lambda=-1\) it has singular points with \(x^2=y^2=z^2\); these values must not be used in the incidence count.

## Verification
Run `python verify.py` with Python 3 and SymPy. The exact-arithmetic execution printed:

`VERIFY_OK: 28 bitangents, 3276 triple determinants, 16 parameter strata, 27 smooth exceptional parameters`

The program also verifies the polynomial identities underlying bitangency, that the thirteen smooth exceptional factors have 27 distinct roots in all, and that every conjugate parametrization gives the same counts. The proof includes the finite determinant-exhaustion algorithm; the executable is the reproducibility certificate for the finite factorization and incidence step.

## Relationship to prior work
Janasz, Pokora and Zieliński, *On arrangements of smooth plane quartics and their bitangents* (first publicly posted 2023-08-31), investigate this exact pencil. Their Propositions 3.1–3.3 tabulate double and quadruple points for the Klein, Dyck and Komiya–Kuribayashi quartics; Proposition 3.8 establishes at least nine quadruple points for every smooth member, but not the all-parameter triple-concurrence discriminant. The three tabulated cases have no triple points. The new classification recovers those values and identifies 24 additional smooth parameters with 4, 12, or 24 triple points. Classical involution-count results explain quadruple incidence but do not determine triples and do not imply the exceptional polynomials. Exact semantic and primary-literature comparisons found no prior statement covering this classification.

## Limitations
The result is over \(\mathbb C\) only, excludes the three singular fibers, and concerns incidence multiplicities rather than a complete labeling of the intersection lattice or its topological type. It does not classify bitangent arrangements of arbitrary smooth quartics. Discovery of earlier unindexed classical formulas or tables could affect originality; no independent audit or validation is claimed.

## References
1. M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514, first version 2023-08-31; published in *Fundamenta Mathematicae* 268 (2025), 151–170, DOI:10.4064/fm240105-13-12. https://arxiv.org/abs/2308.16514
2. E. Ciani, *I varii tipi possibili di quartiche piane più volte omologico-armoniche*, *Rendiconti del Circolo Matematico di Palermo* 13 (1899), 347–373; cited by reference 1.
3. I. Dolgachev, *Automorphisms of del Pezzo surfaces in odd characteristic*, *J. Lond. Math. Soc.* (2024), background on automorphism groups and exceptional smooth quartics. https://doi.org/10.1112/jlms.12905
