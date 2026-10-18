# The two characteristic-two collision profiles of the 49 Klein points

## Finding

For the standard explicit integral Klein arrangement, the **only bad residue characteristic for the incidence lattice of the 21 lines and the distinctness of their 49 multiple-point sections is 2**. The two prime ideals of \(\mathbb Z[\omega]\) over 2 have sharply different, completely determined collision profiles of the 21 quadruple-point and 28 triple-point sections. All 49 sections land on the seven points of \(\mathbb P^2(\mathbb F_2)\) in either fiber, but with the following distinct multiplicity distributions:

| Reduction point | \(\omega\equiv0\): quadruple, triple | \(\omega\equiv1\): quadruple, triple |
|---|---:|---:|
| \((1,0,0)\) | 1, 4 | 1, 0 |
| \((0,1,0)\) | 1, 4 | 1, 0 |
| \((0,0,1)\) | 1, 4 | 1, 0 |
| \((1,1,0)\) | 2, 0 | 6, 8 |
| \((1,0,1)\) | 2, 0 | 6, 8 |
| \((0,1,1)\) | 2, 0 | 6, 8 |
| \((1,1,1)\) | 12, 16 | 0, 4 |

Each column contains exactly 21 quadruple and 28 triple sections. The integers count **specializing distinct sections**, not scheme-theoretic point multiplicities.

## Assumptions and scope

Let \(R=\mathbb Z[\omega]\), \(\omega^2+\omega+2=0\). This is the ring of integers of \(\mathbb Q(\sqrt{-7})\). The 21 homogeneous line forms \(L_i\) are precisely those in Innamorati, *Quasi-Configurations Derived by Special Arrangements of Lines*, Section 4, reproduced in `verify_klein_mod2.py` as coefficient triples using \(1,-1,\omega\). Take their 49 multiple intersections in the projective generic fiber over \(K=\mathbb Q(\omega)\); each point extends uniquely to a projective section of \(\mathbb P^2\) over every local discrete valuation ring \(R_{\mathfrak p}\). The assertions concern this **specified integral coordinate model**, not all projectively equivalent models under arbitrary transformations with nonintegral coefficients.

The two primes above 2 are \(\mathfrak p_0=(2,\omega)\) and \(\mathfrak p_1=(2,\omega+1)\), each with residue field \(\mathbb F_2\). No choice of projective affine chart is required.

## Proof

1. **Exact generic incidence and all odd primes.** Represent \(a+b\omega\) by the integer pair \((a,b)\). Multiplication follows from \(\omega^2=-\omega-2\), and the algebraic norm is \(N(a+b\omega)=a^2-ab+2b^2\). For each of the \(\binom{21}{3}=1330\) triples of line coefficient vectors, form its determinant and take the norm. The exhaustive *exact integer* histogram of these norms is

   | Norm | 0 | 1 | 2 | 4 | 8 | 16 | 32 | 64 |
   |---|---:|---:|---:|---:|---:|---:|---:|---:|
   | Triple count | 112 | 169 | 228 | 271 | 320 | 156 | 70 | 4 |

   This is verified by the complete \(1330\)-case certificate in `verify_klein_mod2.py`; no probabilistic or bounded-experiment extrapolation is involved. A nonzero determinant with norm a power of 2 is a unit at every prime of odd residue characteristic. Consequently, the zero/nonzero status of **every triple** is unchanged modulo every such prime. Each pair of original lines occurs in a triple with nonzero determinant, so all 21 lines remain distinct. Exactly the same incidence partition into 21 quadruple and 28 triple intersections follows: no old concurrence disappears and no new concurrence arises. In particular, all 49 multiple-point sections remain distinct at odd primes, including those above 7.

2. **All 49 generic sections.** For each of the \(\binom{21}{2}=210\) line pairs \((i,j)\), compute its intersection vector \(v_{ij}=L_i\times L_j\) in \(R^3\). Determine the complete incidence set of lines through it by checking \(L_k\cdot v_{ij}=0\) in \(R\), equivalently whether its algebraic norm vanishes. The 210 pairs form **49** projectively distinct classes, precisely 28 supported on three lines (each generating three pairs) and 21 on four lines (each generating six pairs). The certificate checks equality of all representatives within each class by exact cross products. This establishes an exhaustive finite list of the projective generic points.

3. **Local integral reduction at 2.** The polynomial \(T^2+T+2\) has two simple roots modulo 2 and therefore unique corresponding \(2\)-adic lifts. Their residues modulo 8 are \(2\) (for \(\mathfrak p_0\)) and \(5\) (for \(\mathfrak p_1\)); direct substitution gives zero modulo 8 in both cases, and its derivative \(2T+1\) is odd. For any vector \(v\in R^3\), evaluate coordinates using the chosen lift and divide all three by their minimum \(2\)-adic valuation. The mod-2 class of the resulting primitive vector is precisely the reduction of the associated projective section, independent of its nonzero scalar representative.

4. **Complete local collision computation.** For every class and for *all* its pairwise-cross-product representatives, the exact certificate finds minimum valuation at most 2. Thus residues modulo 8 determine the normalized projective mod-2 vector without loss of information. It asserts agreement of every representative and sums the 49 reduced sections according to whether the generic incidence is triple or quadruple. The resulting seven-by-two table is exactly the table in the Finding section. The respective distributions have support all seven rational projective points; their sums of both types are 21 and 28. The differing tables are not inferred from the reduced *lines*: they are obtained by reducing every original multiple-point section, so collisions of formerly distinct points are counted.

5. **Interpretation.** For orientation, reducing the product of the 21 line forms gives, up to a unit and in the fixed coordinates, \(xyz(x+y)^6(x+z)^6(y+z)^6\) at \(\mathfrak p_0\), and \(xyz(x+y)^2(x+z)^2(y+z)^2(x+y+z)^{12}\) at \(\mathfrak p_1\). These support reductions provide an independent geometric plausibility check, but **alone do not determine** the section-collision table.

## Verification

Run the packaged, self-contained Python 3 standard-library script `verify_klein_mod2.py`. It performs exact arithmetic in \(R\), checks all 1330 triple determinants, all 210 line-pair intersections, all 49 incident-line sets, projective consistency of every representative, the two lifts modulo 8, and both complete reduced-point profiles. Its final line is `PASS 49 distinct geometric intersection sections; exact 2-adic profiles`. It has no network dependency. These finite checks are exhaustive over the stated finite input and thus certify the exact arithmetic table; the number-theoretic deduction for *all odd primes* uses the computed determinant norm support and is proved in Step 1.

## Relationship to prior work

Bauer, Di Rocco, Harbourne, Huizenga, Seceleanu, and Szemberg (arXiv:1609.08648, first public 27 September 2016) established and studied the 49 Klein blowup centers, especially in characteristic zero, and Section 9 discusses characteristic seven, not this pair of characteristic-two specialization profiles. Innamorati (2024, Section 4) gives the explicit Klein line equations and the generic incidence configuration; its principal finite-characteristic discussion concerns a characteristic-two **Ceva** arrangement and characteristic-seven Klein geometry, rather than the two prime ideals over 2 for the 49 Klein sections. The explicit line list and generic 49-point incidence are prior work; the claim here is the arithmetic all-prime good/bad classification and detailed 2-adic collision table. Relevant later studies of Klein line/conic arrangements were also searched for overlap. The distinction is a **statement and implication** comparison, not a claim of novelty inferred merely from different titles or unsuccessful searches.

## Limitations

The theorem is about reductions of labeled projective *sections* for one fixed integral Klein model. It does **not** describe a flat closure of the 49-point subscheme, local Artin lengths, the singular scheme of the reduced line divisor, special-fiber blowups, their smoothness, or characteristic-dependent ideal containments. A different \(K\)-projective coordinate change with denominators may change the chosen integral model and its primewise behavior. Literature not indexed by the searches may contain equivalent tables. Independent mathematical audit has not been carried out.

## References

- T. Bauer, S. Di Rocco, B. Harbourne, J. Huizenga, A. Seceleanu, T. Szemberg, *Negative Curves on Symmetric Blowups of the Projective Plane, Resurgences and Waldschmidt Constants*, arXiv:1609.08648, originally submitted 2016-09-27; Section 2.2 and Section 9. https://arxiv.org/abs/1609.08648 ; https://arxiv.org/pdf/1609.08648
- S. Innamorati, *Quasi-Configurations Derived by Special Arrangements of Lines*, Axioms 13 (2024), 321, Section 4, DOI:10.3390/axioms13050321. https://www.mdpi.com/2075-1680/13/5/321
- G. Gévay and P. Pokora, *Klein's arrangements of lines and conics*, 2023, arXiv:2211.15309 (related arrangements; abstract-level comparison).
