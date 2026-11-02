# Exceptional-prime reductions of Klein's 28-bitangent line arrangement

## Finding

Fix \(R=\mathbb Z[\alpha]/(\alpha^2+\alpha+2)\), and let \(L_1,\ldots,L_{28}\) be the ordered linear forms in Table 1 of Janasz–Pokora–Zieliński [1] for the 28 bitangents of the complex Klein quartic. Regard those printed coefficient triples as elements of \(R^3\), and form the labeled relative degree-28 divisor \(\mathscr A=V(\prod_{j=1}^{28}L_j)\) in \(\mathbf P^2_R\). The following refers to this specific integral presentation and its line arrangement; in bad characteristics it does **not** assert that the specialized lines are all distinct geometric bitangents to a smooth specialized quartic.

At every geometric prime of residue characteristic \(p\notin\{2,3,7,11\}\), all 28 lines are distinct, and the intersection profile consists of exactly 252 ordinary double points and 21 ordinary quadruple points. There are no other intersection points of multiplicity at least two. The four listed rational primes are exactly those at which the labeled intersection incidence changes.

For odd exceptional primes, every line remains geometrically distinct; the complete profile is:

| Residue characteristic | Number of lines | Double points | Triple points | Quadruple points | Sevenfold points |
| --- | ---: | ---: | ---: | ---: | ---: |
| \(3\) | 28 | 0 | 0 | 63 | 0 |
| \(7\) | 28 | 0 | 28 | 21 | 8 |
| \(11\) | 28 | 0 | 84 | 21 | 0 |
| all other odd primes | 28 | 252 | 0 | 21 | 0 |

More precisely, in characteristic seven the specialized 28 lines are **exactly the 28 secants joining pairs of the eight \(\mathbb F_7\)-rational points** of the smooth conic \(X^2+Y^2+Z^2=0\) in \(\mathbf P^2_{\mathbb F_7}\). The 8 conic points are incident to seven lines, the other 49 rational projective points consist of 21 quadruple and 28 triple points, and all 57 \(\mathbb F_7\)-points occur as arrangement intersections. In characteristic eleven there are two primes of \(R\) above eleven, with \(\alpha\equiv4\) and \(\alpha\equiv6\); both have the same profile. Every specialized line has nine triple points and three quadruple points, exhausting its twelve \(\mathbb F_{11}\)-rational points.

In characteristic two the two primes of \(R\) have different nonreduced fibers:

\[
\begin{aligned}
\alpha\equiv0:&\quad X^4Y^4Z^4(X+Y+Z)^{16}=0,\\
\alpha\equiv1:&\quad (X+Y)^8(X+Z)^8(Y+Z)^8(X+Y+Z)^4=0.
\end{aligned}
\]

The first reduced support consists of four lines in general position (six double points). The second reduced support consists of three concurrent lines plus one further line missing their common point (one triple point and three double points). Counting all original labeled pairs, the first fiber has three distinct intersection-support points each carrying eight line labels and three carrying twenty labels; the second has three carrying twelve labels and one carrying twenty-four labels. Those label counts are not intrinsic Jacobian-scheme lengths.

## Assumptions and scope

The source's \(28\) integer-quadratic coefficient triples, including their ordering, are transcribed verbatim into the attached `verify_klein28.py`, with a pair \((a,b)\) denoting \(a+b\alpha\). Every triple includes a coefficient equal to a unit of \(R\); consequently none of the labeled line equations vanishes identically at any geometric prime. Throughout, a point of multiplicity \(m\) means a geometric projective point incident to exactly \(m\) **distinct reduced lines**. Geometric classification over an algebraic closure and arithmetic rational-point claims over the specified finite fields are distinguished. The characteristic-two factor multiplicities concern the fixed product equation over the chosen ring of integers.

## Proof

**1. Norm certificate excluding any other bad primes.** In the imaginary quadratic ring \(R\), conjugation sends \(\alpha\) to \(-1-\alpha\); hence for \(v=a+b\alpha\),
\[
N(v)=a^2-ab+2b^2.
\]
For each of the \(\binom{28}{3}=3276\) unordered triples \(i<j<k\), compute \(\Delta_{ijk}=\det(L_i,L_j,L_k)\in R\) using \(\alpha^2=-\alpha-2\). The exact exhaustive norm histogram is:

| Norm | Number of triples | Norm | Number of triples | Norm | Number of triples |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 84 | 1 | 48 | 2 | 276 |
| 4 | 368 | 7 | 36 | 8 | 696 |
| 9 | 24 | 11 | 36 | 14 | 80 |
| 16 | 508 | 18 | 96 | 22 | 60 |
| 28 | 156 | 32 | 420 | 36 | 24 |
| 44 | 60 | 56 | 28 | 64 | 204 |
| 72 | 24 | 88 | 12 | 112 | 8 |
| 128 | 28 | | | | |

Its entries add to 3276. Every **nonzero** norm is divisible only by primes among \(2,3,7,11\); all four occur. Thus any triple of source forms which is independent in characteristic zero remains independent over every prime ideal not above those four rational primes. Moreover, if two lines became identical outside those characteristics, every triple containing the pair would become dependent, contrary to the presence of unit-norm triple determinants. A collection of generic intersection points merges precisely if at least three distinct lines become concurrent. Therefore the absence of new zero determinants excludes new concurrences and any change in the complete generic incidence profile outside the stated primes.

**2. Generic incidence.** Calculate the projective cross products \(L_i\times L_j\), for all \(\binom{28}{2}=378\) pairs, over the characteristic-zero fraction field \(\mathbb Q(\alpha)\), normalizing without floating point arithmetic. They produce 252 distinct points belonging to one line pair and 21 points belonging to six line pairs each. The incidence totals check as \(252+21\binom42=378\), giving precisely 252 ordinary double and 21 ordinary quadruple points. This recovers the already published complex configuration [1], and supplies the comparison baseline rather than a new result about the generic arrangement.

**3. Special fibers and their completeness.** The polynomial \(T^2+T+2\) splits over \(\mathbb F_2\) as \(T(T+1)\), is irreducible over \(\mathbb F_3\), has the unique double root \(3\) over \(\mathbb F_7\), and splits over \(\mathbb F_{11}\) with roots \(4,6\). Reduce each of the 28 coefficient triples in the corresponding residue field (\(\mathbb F_9\) for characteristic three), normalize its line in the appropriate projective dual plane, and enumerate all 378 labeled pair cross products. Equal line forms are tracked separately. Distinct projective intersection points are identified by exact field arithmetic and their sets of incident distinct lines recorded. These exhaustive finite field calculations yield the displayed profiles, including both distinct dyadic factorization patterns. The incidence identities independently check the odd-prime results:
\[
\begin{aligned}
p=3:&\quad 63\binom42=378,\\
p=7:&\quad 8\binom72+21\binom42+28\binom32=378,\\
p=11:&\quad 21\binom42+84\binom32=378.
\end{aligned}
\]
All projective incidence points in these residue fields are explicitly enumerated, so the arithmetic statements over \(\mathbb F_3^2\), \(\mathbb F_7\) and \(\mathbb F_{11}\) automatically imply the same geometric incidence profiles over their algebraic closures. For the dyadic fibers, directly collect repeated reduced linear factors; since all four distinct factors have unit coefficients their geometric support is exactly the indicated four-line arrangement.

**4. Characteristic-seven conic.** In \(\mathbf P^2(\mathbb F_7)\), enumerate the eight points of \(Q:X^2+Y^2+Z^2=0\). It is a smooth conic, as the diagonal matrix is nondegenerate in characteristic seven. Every one of the 28 reduced line forms at \(\alpha=3\) vanishes at exactly two of the eight points; their unordered contact pairs are all distinct. Since \(\binom82=28\), the reduced forms exhaust the secants. Pairwise intersection enumeration identifies the eight conic points as the sevenfold concurrence points and the remaining 49 points as 21 quadruple and 28 triple points. Since the total number of points of \(\mathbf P^2(\mathbb F_7)\) is 57, this is all of them.

**5. Characteristic-eleven uniformity.** For each of the two roots \(4\) and \(6\), the finite field projective census finds precisely 84 triple and 21 quadruple points. For every one of the 28 distinct line equations, direct incidence counting gives exactly nine of the former and three of the latter, totaling twelve \(\mathbb F_{11}\)-points, the full rational point set of that line. Thus the claimed uniform line incidence is exact at both primes.

All algebraic identities and finite enumerations in steps 1–5 are independently reproduced from the displayed coefficient inputs by the accompanying standalone exact script. The finite enumeration is exhaustive for the explicitly finite domains. The all-characteristics exclusion is the algebraic norm-divisibility argument in step 1, **not** an extrapolation from tests in a few finite fields.

## Verification

Run `python3 verify_klein28.py` with the Python 3 standard library. It computes the exact 3276-term norm histogram, rational characteristic-zero projective pair incidence, residue-field line reductions and incidence at both primes above two and eleven and the primes above three and seven, and the eight-point conic secant equivalence. Expected completion marker: `KLEIN28_EXACT_ALL_PRIMES_2_3_7_11_INCIDENTS_AND_CONIC_PASS`. The script needs no computer algebra system, external services, or prerecorded results; the asserted outputs are independently recomputed from its input coefficient table.

## Relationship to prior work

Janasz–Pokora–Zieliński [1] published all 28 linear forms and the complex profile \((252,0,21)\) for double, triple, and quadruple intersections. Neither the printed forms nor the complex counts are new. The characteristic-three 63-quadruple-point profile is compatible with the classical Hermitian-curve degeneration and is explicitly **not** claimed independently novel. Bethea–Brazelton [2] discuss the symmetry action on the 28 bitangents in characteristic zero. Dolgachev–Martin [3] discuss exceptional characteristic phenomena for the Klein quartic, particularly characteristic seven, but treat a different geometric question. The finite-projective-plane 28-secant geometry of a conic over \(\mathbb F_7\) is classical; the identification with the *specific reduced 28 printed forms* is the contribution here. The result additionally classifies the prime eleven incidence jump and the two nonreduced dyadic specializations, and it proves the exclusion of all other primes by an exact determinant certificate.

## Limitations

This is an arithmetic theorem about the literal integral coefficient model \(\mathscr A\); other integral models obtained by nonintegral projective transformations can have different bad reduction. In particular, the characteristic-seven plane Klein quartic of the corresponding literal model may be singular and need not be the good-reduction model of an abstract Klein curve. Reducing classical bitangent equations does not imply that every reduced line remains a bitangent of a smooth quartic in the exceptional characteristics. No assertion is made about scheme-theoretic singularity lengths of the divisor from its labeled section-counts. The result does not prove historical priority against unindexed or inaccessible mathematical work; the source of the model and known characteristic-three phenomenon are credited. External independent mathematical audit has not been performed.

## References

[1] M. Janasz, P. Pokora, and M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514, first posted 31 August 2023. https://arxiv.org/abs/2308.16514 . Table 1: 28 Klein-bitangent coefficient triples; Proposition 3.1: complex incidence profile.

[2] C. Bethea and T. Brazelton, *Bitangents to symmetric quartics*, arXiv:2410.09242, first posted 11 October 2024. https://arxiv.org/abs/2410.09242 . Symmetry and bitangent orbits.

[3] I. Dolgachev and G. Martin, *Automorphisms of del Pezzo surfaces in odd characteristic*, Journal of the London Mathematical Society 109 (2024), article e12905. https://doi.org/10.1112/jlms.12905 . Relevant exceptional-characteristic Klein quartic discussions.

[4] N. Elkies, *The Klein Quartic in Number Theory*, 1999. Background on the Klein quartic and characteristic-dependent geometry; an accessible overview was consulted, but complete-text coverage was not established.
