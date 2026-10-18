# Arithmetic reduction and point collisions of the icosahedral reflection arrangement

## Finding

For the explicitly specified integral model of the \(H_3\) icosahedral reflection arrangement, the entire incidence lattice of its fifteen projective lines is unchanged in **every odd residue characteristic**, including characteristic five. The only rational prime at which the line arrangement degenerates is two. At that prime, the fifteen-line divisor has three simple components and one component of multiplicity twelve; its thirty-one characteristic-zero intersection-point sections specialize to exactly eight distinct points with the collision profile below.

## Assumptions and scope

Put \(R=\mathbb Z[\varphi]\), where \(\varphi^2=\varphi+1\). Define fifteen lines in \(\mathbb P^2_R\) by the primitive row vectors
\[
(1,0,0),\qquad (0,1,0),\qquad (0,0,1),
\]
and by all twelve vectors obtained from the **cyclic** permutations of \((1,\varphi,\varphi-1)\), independently changing the signs of its second and third entries after permutation. Each vector \((a,b,c)\) specifies the line \(ax+by+cz=0\). These are the standard fifteen icosahedral reflection hyperplanes in a golden-ratio coordinate model. The claim is about **this integral model**, not about arbitrarily modified lattices or models related by changes of coordinates with nonunit determinant over \(R\).

For a characteristic-zero intersection point, its *section* means the projective \(R\)-point obtained from the cross product of any two defining normals, divided by the maximal common power of two, and subsequently regarded as an \(R\)-primitive triple. The section is well-defined because the determinant census below excludes any common odd-prime divisor, and two such primitive representatives for the same intersection differ by a unit of \(R\). Collision counts concern distinct characteristic-zero point **sections**, not scheme lengths of their special fibers.

## Proof

**1. Complete determinant certificate.** Addition and multiplication in \(R\) are explicitly
\[
(a+b\varphi)(c+d\varphi)=(ac+bd)+(ad+bc+bd)\varphi.
\]
The field norm is \(N(a+b\varphi)=a^2+ab-b^2\). An exact enumeration, with the fully specified fifteen normals above, of all \(\binom{15}{3}=455\) determinant triples gives precisely
\[
\begin{array}{c|rrrrr}
\text{determinant norm}&0&1&4&16&64\\ \hline
\text{number of triples}&70&37&156&188&4
\end{array}
\]
where the nonzero norms are **absolute** norms. The accompanying standard-library Python certificate independently constructs the normals, computes each determinant from integer pairs, and asserts this exhaustive table. No sampling or interpolation is involved.

**2. Uniform odd-characteristic incidence.** A nonzero algebraic integer whose absolute norm is a power of two cannot vanish in a residue field of odd characteristic. Consequently the zero/nonzero status of **every** determinant of three normals is identical over the fraction field and over every odd residue field. Every pair of normals is independent at those primes: otherwise each determinant involving the pair would vanish, contradicting a nonzero norm among the remaining triples. Hence triple dependence data, and thus the full rank-two flat/intersection-point incidence lattice, are preserved. An exhaustive exact comparison of the 105 pairwise cross products yields exactly fifteen double, ten triple and six quintuple points in characteristic zero. These counts therefore persist at all odd primes, including the ramified prime over five.

**3. Characteristic two as a nonreduced divisor.** The prime two is inert in \(R\) since \(u^2+u+1\) is irreducible over \(\mathbb F_2\). Write \(\alpha=\varphi\bmod2\), so \(\mathbb F_4=\mathbb F_2[\alpha]\). All signs disappear. The three cyclic permutations of \((1,\alpha,\alpha^2)\) are projectively proportional, since cyclic permutation is multiplication of all coordinates by a nonzero power of \(\alpha\). Thus the twelve mixed lines coalesce, whereas the three coordinate lines stay distinct. Reduction of the product of all fifteen defining forms gives, up to a nonzero scalar,
\[
D_{\mathbb F_4}:\quad xyz\,(x+\alpha y+\alpha^2z)^{12}=0.
\]
The exponent twelve is the scheme-theoretic multiplicity **of the divisor**; it is not the multiplicity of any limiting point section.

**4. Exact specialization of the thirty-one point sections.** For each of the 105 pairs, compute the cross product over \(R\). Two such products represent the same characteristic-zero point exactly when their exterior product is zero. This produces 31 classes. For each class divide out the largest common power of two, reduce its three coordinate coefficients modulo two, then normalize the first nonzero coordinate to one in \(\mathbb F_4\). The resulting eight fibers (entries give numbers of original double, triple and quintuple sections) are:

| Point in \(\mathbb P^2(\mathbb F_4)\) | Doubles | Triples | Quintuples |
| --- | ---: | ---: | ---: |
| \((1:0:0)\), \((0:1:0)\), \((0:0:1)\), separately | 1 each | 0 | 0 |
| \((0:1:\alpha^2)\), \((1:0:\alpha)\), \((1:\alpha^2:0)\), separately | 0 | 2 each | 2 each |
| \((1:1:1)\) | 0 | 4 | 0 |
| \((1:\alpha:\alpha^2)\) | 12 | 0 | 0 |

The counts sum to \(15\) double, \(10\) triple and \(6\) quintuple sections. Each representative of every one of the 105 pairs was independently reduced and checked to land at its class's listed limit. This exhausts possible specializations, since every original intersection arises from a pair.

## Verification

Run `python3 verify_icosahedral_reduction.py` using Python 3 and its standard library. The script independently checks all 455 determinants in \(R\), all 105 intersection pairs, the projective equivalences producing 31 original points, the complete \(\mathbb F_4\) line-divisor support and multiplicities, and all eight collision classes, ending in `VERIFY_OK`. The exhaustive calculations are a finite exact proof certificate; the odd-characteristic conclusion then follows from the norm argument, **not** from enumerating finitely many finite fields.

## Relationship to prior work

Hoge and Röhrle classify nice reflection arrangements in their 2015 preprint, including the relevant Coxeter family, but niceness does not imply this arithmetic reduction classification. Calvo's 2022 treatment explicitly studies the **same complex 15-line, 31-point configuration**, describing its \((15,10,6)\) double/triple/quintuple distribution and the ideal's Waldschmidt constant. That characteristic-zero classification does not by itself determine exceptional residue primes, multiplicities of the reduced divisor, or the eight specialization fibers. The broader arithmetic-arrangement framework of Kamiya–Takemura–Terao makes reduction of intersection lattices a natural question, but does not supply this fifteen-line determinant-norm table or the collision profile.

## Limitations

The classification is for the specified \(R\)-integral arrangement and for intersections of its original characteristic-zero lines. It neither computes the Waldschmidt constant in positive characteristic nor claims a result about the classifying invariant rings or logarithmic derivations in characteristic two. The numbers of old point sections meeting after reduction are **not** Hilbert–Samuel multiplicities of point schemes. Literature comparison was targeted, not exhaustive, and an unindexed prior computation of the same special fiber remains possible.

## References

1. T. Hoge and G. Röhrle, *Nice reflection arrangements*, arXiv:1505.04603, first publicly posted 18 May 2015.
2. S. Calvo, *The icosahedral line configuration and Waldschmidt constants*, arXiv:2209.01499, 3 September 2022, especially Sections 1–2 and Remark 2.1.
3. H. Kamiya, A. Takemura, and H. Terao, *Periodicity of hyperplane arrangements with integral coefficients modulo positive integers*, Hokkaido University Preprint Series 839, 30 March 2007, DOI:10.14943/83989.
