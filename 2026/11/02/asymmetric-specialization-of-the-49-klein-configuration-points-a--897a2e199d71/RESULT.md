# Asymmetric specialization of the 49 Klein-configuration points at the two primes over two

## Finding

Let \(R=\mathbb Z[a]/(a^2+a+2)=\mathcal O_{\mathbb Q(\sqrt{-7})}\). Consider the **specified integral model** of the classical Klein arrangement: the 21 labelled lines in \(\mathbb P^2_R\) whose coefficient rows are the array `L` in `verify_klein_reduction.py`, equivalently the 21 rows in Bauer–Di Rocco–Harbourne–Huizenga–Lundman–Pokora–Szemberg (2014), Section 4.1. Let \(D\) be their sum as an effective Cartier divisor, and let \(Z_K\) be the reduced set of 49 intersections in its generic fibre, comprising 21 quadruple and 28 triple points. Each point defines a section of \(\mathbb P^2\) over the localization at either prime above two.

**Specialization theorem.** For every prime ideal \(\mathfrak p\nmid 2\), the 21 lines and all 49 intersection points remain geometrically distinct, with the same incidence lattice (21 ordinary quadruple points and 28 ordinary triple points). At the two primes \(\mathfrak p_0=(2,a)\) and \(\mathfrak p_1=(2,a+1)\), however, the special Cartier divisors have respective equations, up to units,

\[
D_0:\quad xyz(x+y)^6(x+z)^6(y+z)^6=0,
\]
\[
D_1:\quad xyz(x+y)^2(x+z)^2(y+z)^2(x+y+z)^{12}=0.
\]

Thus the first reduced fibre is the six-line Fano arrangement with the diagonal line deleted; the second is the full seven-line Fano arrangement. Their irreducible-component multiplicity profiles are, respectively, \((6,6,6,1,1,1)\) and \((12,2,2,2,1,1,1)\). Because the numbers of reduced components differ, these two fibres are not projectively isomorphic, although the two residue fields are both \(\mathbb F_2\).

The **49 labelled intersection-point sections** specialize with the following exact collision profiles. In each pair \((r,s)\), \(r\) is the number of generic quadruple-point sections and \(s\) the number of generic triple-point sections specializing to the indicated residue point:

| Residue point class | At \(\mathfrak p_0\) | At \(\mathfrak p_1\) |
| --- | ---: | ---: |
| Each of \((1:0:0),(0:1:0),(0:0:1)\) | \((1,4)\) | \((1,0)\) |
| Each of \((1:1:0),(1:0:1),(0:1:1)\) | \((2,0)\) | \((6,8)\) |
| \((1:1:1)\) | \((12,16)\) | \((0,4)\) |

Each column totals 21 generic quadruple points and 28 generic triple points. Thus at \(\mathfrak p_0\) a single residue point receives 28 generic points, whereas at \(\mathfrak p_1\) each of three residue points receives 14, with the remaining sections distributed over four points.

The reduced special fibres have, respectively, four ordinary triple points plus three nodes and seven ordinary triple points. The Tjurina singularity schemes of these reduced curves have global lengths 19 and 28, respectively, and the reduced curves have arithmetic genera 10 and 15. These are invariants of the **reduced supports**, not the length of the flat 49-section closure and not the singular schemes of the nonreduced degree-21 Cartier fibres.

## Assumptions and scope

All statements concern the explicitly marked, integral, degree-21 line divisor determined by the 21 historical coefficient rows in the ring \(R\). They are not assertions that every integral model of the abstract complex Klein configuration has the same special fibres. The field \(\mathbb Q(\sqrt{-7})\) has ring of integers \(R\) and two distinct primes above two; \(a\) and \(a+1\) have norm two and are local uniformizers for \(\mathfrak p_0\) and \(\mathfrak p_1\), respectively. Incidence is assessed after geometric residue-field extension. A point section means the schematic closure of an individual generic intersection point in the projective plane over a localized discrete valuation ring; the table reports its residue point, not the structure of a 49-point Hilbert-scheme limit.

## Proof

**1. Generic incidence and its odd-characteristic persistence.** Represent every coefficient in \(R\) uniquely as \(u+va\), reducing products by \(a^2=-a-2\). For each of the 210 unordered pairs of lines, form the cross product of their coefficient rows. Exact projective equality, tested by vanishing of three cross-product coordinates, groups these pairs into precisely 49 distinct points: 21 classes incident with four lines and 28 with three lines. Every line is incident with four points of each type. The 1330 unordered triples of line rows have determinant-norm distribution

\[
\begin{array}{c|rrrrrrrr}
N&0&1&2&4&8&16&32&64\\\hline
\#&112&169&228&271&320&156&70&4.
\end{array}
\]

Here the field norm is \(N(u+va)=u^2-uv+2v^2\). Every nonzero triple determinant consequently remains nonzero at every prime not above two. If distinct lines merged or previously distinct intersection points collided modulo such a prime, a previously nonzero triple determinant would vanish there. Therefore the generic incidence lattice survives at every odd residue characteristic. Notice that this includes characteristic seven: special *additional* geometry there need not change the line-incidence lattice.

**2. Two reductions of the line divisor.** Reduction at \(\mathfrak p_0\) sends \(a\) to zero, while reduction at \(\mathfrak p_1\) sends \(a\) to one. Reducing each of the 21 coefficient rows, and grouping proportional nonzero rows over \(\mathbb F_2\), yields the following multiplicities: at \(\mathfrak p_0\), the coordinate lines occur once each and the three pair-sum lines six times each; at \(\mathfrak p_1\), the coordinate lines occur once, the three pair-sum lines twice, and the diagonal line twelve times. This gives exactly the two displayed equations, including their scheme-theoretic Cartier multiplicities.

**3. Specialization of the 49 sections.** A representative cross product is an integral projective vector. At each localized prime, divide all three coordinates by the associated uniformizer repeatedly until at least one coordinate is a unit. Reducing the resulting primitive vector gives the unique residue point of the section by properness and the valuative criterion. Exact division uses the algebraic conjugate divided by norm two, so all operations are integral and checkable. Applying this process to each of the 49 distinct projective cross-product classes produces the complete table above; the independent normalizations at the two primes are essential because naive reduction of an unnormalized cross product can give a zero vector.

**4. Reduced-support singularities.** The seven nonzero vectors in \(\mathbb F_2^3\) represent the seven Fano lines. All seven together have seven ordinary triple intersections. Deleting the line \(x+y+z=0\) leaves four ordinary triple points and turns the three points lying on that line into nodes. At an ordinary triple point in characteristic two, local linear coordinates give \(f=uv(u+v)\); its partial derivatives generate \((u^2,v^2)\), and the local Tjurina length is four. At a node, \(f=uv\) gives length one. Hence the totals are \(4\cdot4+3=19\) and \(7\cdot4=28\). The arithmetic genera follow either from the degree formula \((d-1)(d-2)/2\) or from normalization and the ordinary multiple-point delta invariants.

## Verification

Run `python3 verify_klein_reduction.py` with the Python 3 standard library. It checks the 21 historical rows, all 210 line pairs, all 1330 triple determinants, the complete norm histogram, every one of the 49 generic point classes, both reductions of every line, the reduced incidence distributions, and the valuation-normalized specialization of each generic point at both primes. It asserts both Tjurina totals and prints `VERIFY_OK`. `verification_output.txt` contains the exact output of one execution from these packaged bytes. The field-theoretic argument in the proof, not finite sampling, extends the determinant certificate to all odd residue characteristics.

## Relationship to prior work

The 2014 paper of Bauer et al. provides the 21 integral coefficient triples, the 49 generic points, and the complex incidence matrix; none of those established facts is claimed as new. Bauer et al. (arXiv:1609.08648, Section 9) discuss positive-characteristic geometry, especially characteristic seven, and study point-ideal invariants; they do not provide the two characteristic-two residual fibres or the 49-point specialization profiles. Gévay–Pokora (2022) and subsequent work develop the classical arrangement and its derived configurations. A contemporary finite-plane account derives covering properties for odd-characteristic realizations; those results do not classify the two split residual fibres over two.

The contribution here is a complete **model-specific arithmetic degeneration classification** at the two distinct split primes over two, including the contrasting 49-section collision profiles, together with a finite exact certificate that no other residue characteristic changes the line-incidence lattice. The line equations make the component multiplicities readily computable, so independent priority checking should focus particularly on the complete collision profiles and their relation to the classical 49-point blowup centres.

## Limitations

The result makes no claim about uniqueness of an integral model up to birational or nonintegral projective change of coordinates. It does not construct or classify the flat scheme structure of the union of the 49 closed sections, only the specializations of its individual geometric points. The Tjurina lengths apply to the reduced supports, not the nonreduced degree-21 fibres. The result does not transfer the characteristic-zero negativity or resurgence invariants to characteristic two. Historical priority is qualified by the accessibility of older geometric formulas and the possibility of unindexed modular computations; no independent audit has been performed.

## References

1. T. Bauer, S. Di Rocco, B. Harbourne, J. Huizenga, A. Lundman, P. Pokora, T. Szemberg, *Bounded Negativity and Arrangements of Lines*, arXiv:1407.2966, initially public 2014-07-10; especially Section 4.1. https://arxiv.org/abs/1407.2966
2. T. Bauer, S. Di Rocco, B. Harbourne, J. Huizenga, A. Seceleanu, T. Szemberg, *Negative curves on symmetric blowups of the projective plane, resurgences and Waldschmidt constants*, arXiv:1609.08648, initially public 2016-09-27; especially Section 9. https://arxiv.org/abs/1609.08648
3. G. Gévay, P. Pokora, *Klein's arrangements of lines and conics*, arXiv:2211.15309, 2022-11-28. https://arxiv.org/abs/2211.15309
4. *Quasi-Configurations Derived by Special Arrangements of Lines*, Axioms 13 (2024), article 321, Section 4. https://www.mdpi.com/2075-1680/13/5/321
