# Arithmetic reduction and rational singular-support spectrum of the decagonal 61-line arrangement

## Finding

A canonical cyclotomic tangent-coordinate model of the regular-decagon line arrangement \(\mathcal O_{61}\) has an explicit, complete arithmetic intersection profile. Over \(\mathbb Q\), its \(551\) geometric singular points split into \(7\) points with rational coordinates, \(20\) points whose least field of definition is \(\mathbb Q(\sqrt5)\), and \(524\) points whose least field of definition is \(\mathbb Q(\zeta_5)\). This coordinate-field statement refers to the specified model, not to every projectively equivalent model.

For a prime \(p\), reduce the **already constructed** \(61\) integral cyclotomic line factors modulo a prime above \(p\), then take their distinct reduced geometric supports. The complete characteristic-dependent census is:

| Characteristic | Distinct lines | Geometric intersection points | Multiplicity distribution \(\{m:n_m\}\) | Rational singular points over \(\mathbb F_p\) |
| --- | ---: | ---: | --- | ---: |
| \(2\) | 6 | 6 | \(\{2:5,5:1\}\) | 2 |
| \(3\) | 51 | 91 | \(\{2:5,5:40,6:40,10:6\}\) | 5 |
| \(5\) | 7 | 7 | \(\{2:6,6:1\}\) | 7 |
| \(11\) | 61 | 131 | \(\{2:5,5:70,6:50,10:1,12:5\}\) | 131 |
| \(19\) | 61 | 341 | \(\{2:65,3:170,4:30,5:70,10:1,12:5\}\) | 21 |
| Other primes | 61 | 551 | \(\{2:335,3:140,5:70,10:1,12:5\}\) | See below |

At every prime \(p\notin\{2,3,5,11,19\}\), the geometric incidence lattice is unchanged. In this range, the exact rational singular-support count is
\[
N_p=\begin{cases}
551,&p\equiv1\pmod5,\\
27,&p\equiv4\pmod5,\\
7,&p\equiv2\text{ or }3\pmod5.
\end{cases}
\]
The three counts occur for sets of primes of natural densities \(1/4\), \(1/4\), and \(1/2\), respectively. Every stated count is of **distinct geometric singular-support points**, not of Jacobian-scheme lengths.

## Assumptions and scope

Work with \(K=\mathbb Q(\zeta)\), where \(\zeta\) is a primitive fifth root satisfying \(\Phi_5(\zeta)=\zeta^4+\zeta^3+\zeta^2+\zeta+1=0\), and set \(t=-\zeta^3\), a primitive tenth root. In \(\mathbb P^2_K\), let \(\mathcal C_{10}\) consist of the ten distinct lines
\[
L_j:\quad X+t^{2j}Y-2t^j Z=0,\qquad 0\leq j<10.
\]
They are tangents at the points \([t^{2j}:1:t^j]\) of the nonsingular conic \(XY=Z^2\). Under the usual complex coordinate change from the conic to the unit circle, these form the sides of a regular decagon. Form the \(45\) pairwise intersections of these ten lines. Define \(\mathcal A\) as the reduced union of every line containing at least three **distinct** points among the \(45\); equivalently, it is the point-line operator \(\Lambda_{\{2\},3}(\mathcal C_{10})\). In characteristic zero this has exactly \(61\) lines.

For reduction, choose the unique primitive integer cyclotomic coefficient vector obtained from each of the \(61\) lines by projective normalization followed by clearing denominators and dividing the integer content across the twelve basis coefficients. Reduce this fixed list in \(\mathbb Z[\zeta]\) modulo each prime ideal above \(p\), discard projectively repeated lines, and base-extend to an algebraic closure. All embedding choices produce the same counts because the original line collection is Galois stable. This is **not** the operation of constructing a new point-line arrangement from a decagon already reduced modulo \(p\).

A rational singular point is a point fixed by coordinatewise \(p\)-Frobenius on the geometric singular set; its coordinates need not be the intersection of two individually \(\mathbb F_p\)-defined component lines.

## Proof

**1. Exhaustive reconstruction in characteristic zero.** Represent an element of \(\mathbb Q[\zeta]\) by its four rational coefficients in \(1,\zeta,\zeta^2,\zeta^3\), with multiplication reduced by \(\Phi_5=0\). For vectors of line or point coordinates, form pairwise cross products and normalize using inversion of their first nonzero coordinate. The resulting \(45\) initial intersections yield \(481\) distinct secants; exactly \(61\) secants contain at least three initial points, with initial-point supports \(40\) lines of size \(3\), \(5\) of size \(4\), \(6\) of size \(5\), and \(10\) of size \(9\). The normalized ten original lines are contained among the \(61\).

Form every cross product of the \(\binom{61}{2}=1830\) pairs of distinct lines. Group projectively equal points and record how many lines contain each point. This exact procedure produces \(551\) points with distribution
\[
(n_2,n_3,n_5,n_{10},n_{12})=(335,140,70,1,5).
\]
The pairwise incidence identity is checked explicitly:
\[
335\binom22+140\binom32+70\binom52+\binom{10}2+5\binom{12}2=1830.
\]
In particular, the last multiplicity is \(12\), as independently certified by the point-to-line incidence calculation.

**2. Galois orbit and rationality census.** Apply all four automorphisms \(\sigma_a:\zeta\mapsto\zeta^a\) for \(a=1,2,3,4\) to every normalized intersection point. The fixed-point totals are \(551,7,7,27\), respectively. As \(\operatorname{Gal}(K/\mathbb Q)\) is cyclic of order \(4\), its unique involution fixes \(27\) points; of these, \(7\) are fixed by the whole group. Thus the least-coordinate-field orbit sizes occur with frequencies
\[
1^{\times7},\qquad 2^{\times10},\qquad 4^{\times131},
\]
or, counting individual geometric points, \(7,20,524\). The intermediate quadratic field is \(\mathbb Q(\sqrt5)\). The seven rational normalized points are
\[
[0:0:1],\ [1:-1:0],\ [1:1:-1],\ [1:1:0],\ [1:1:1],\ [2:2:-1],\ [2:2:1].
\]
For a good prime \(p\ne5\), arithmetic Frobenius acts on fifth roots via \(\zeta\mapsto\zeta^p\); with the incidence lattice unchanged, a geometric intersection is rational precisely when this action fixes its reduced coordinate. Therefore the above fixed-point totals give \(551,27,7\) according as \(p\bmod5\) is \(1,4,\{2,3\}\). Dirichlet's theorem on primes in reduced residue classes modulo \(5\) gives the displayed natural densities.

**3. Uniform incidence stability away from five specified primes.** Use the \(61\) primitive integral coefficient triples specified above. None reduces to the zero triple at any prime: the greatest common divisor of the four-dimensional algebraic norms of its nonzero coordinate entries is \(1\). Enumerate all \(\binom{61}{3}=35{,}990\) unordered line triples. Exactly \(2{,}060\) determinants are zero in \(K\); the other \(33{,}930\) are nonzero and the **only** rational prime divisors occurring in their algebraic norms are
\[
\{2,3,5,11,19\}.
\]
The complete independently reproducible frequency table of their \(21\) different absolute norm values is built into `verify.py` and asserted, not merely logged. Hence no nonzero determinant vanishes modulo any prime outside this set, and the zero determinants remain zero in every characteristic. Any two distinct lines have a third line yielding a nonzero determinant in characteristic zero; thus they cannot collide at such a prime. Likewise, equality or inequality of intersection points of two line pairs is completely controlled by the concurrence of appropriate line triples. Therefore the whole geometric intersection lattice, including each multiplicity, is constant outside the five exceptional primes.

**4. Exceptional reductions.** For each of the five primes, perform exhaustive arithmetic in an explicit field containing the reduced fifth roots. The minimal polynomials of the chosen images of \(\zeta\), written in ascending coefficient order, are \([1,1,1,1,1]\) over \(\mathbb F_2\) and \(\mathbb F_3\); \([4,1]\) over \(\mathbb F_5\); \([8,1]\) over \(\mathbb F_{11}\); and \([1,5,1]\) over \(\mathbb F_{19}\). Thus the calculations respectively occur in fields of cardinalities \(16,81,5,11,361\). Reduce all \(61\) primitive line triples, normalize them, deduplicate, form every cross product of distinct reduced lines, and count incident lines at each resulting geometric point. Direct application of the \(p\)-Frobenius criterion counts the rational geometric points. This complete finite computation yields the five rows of the table. Every row also satisfies \(\sum_m n_m\binom m2=\binom r2\), where \(r\) is its number of distinct reduced lines. Unlike experiments at sample good primes, these are exhaustive checks of **all relevant points and line pairs** in the actual exceptional finite fields.

## Verification

Run `python3 verify.py` using Python 3 and its standard library only. The executable starts from the ten tangent equations, reconstructs all \(61\) lines and \(551\) characteristic-zero intersection points by exact rational cyclotomic arithmetic, recomputes the full \(35{,}990\)-triple determinant census, and checks the Galois fixed-point and degree counts. It also performs the complete finite-field reduction censuses in all five exceptional characteristics and tests three nonexceptional characteristics. Its successful terminal message starts with `VERIFY_OK`. Finite-field samples for the good characteristics are consistency checks; the infinite-prime assertion rests on the exact determinant norm obstruction calculation and Galois action.

## Relationship to prior work

Pokora and Roulleau [1, Remark 2.5] constructed the \(61\)-line decagonal arrangement and established its complex geometry and freeness. Their original paper already identifies a model over \(\mathbb Q(\sqrt5)\); this work does **not** claim to establish the abstract arrangement's minimal possible field of projective realization. The arithmetic assertions here instead concern the specific canonical cyclotomic tangent-coordinate presentation, its specified integral line factors, their good and bad reduction at every prime, and its singular-point Frobenius spectrum. The printed high-multiplicity entry of the original table differs from the exact, pair-count-consistent \(12\)-fold computation; the present theorem uses the explicit reconstruction rather than treating that printed entry as a certificate. Kühne and Roulleau [2] consider related point-line operators, geometric realizations, and matroid geometry, but not this full arithmetic reduction census for the fixed decagonal model.

## Limitations

The point/line counts and fields of definition are model-relative arithmetic claims; an extension-field projective change of coordinates can alter pointwise rationality. At bad primes, reduction is performed **after** characteristic-zero construction, not by rerunning the point-line operator on the reduced decagon. Counts refer only to reduced geometric line divisors and their singular support. The result does not claim freeness in positive characteristic, Jacobian scheme lengths, or a classification of all integral presentations. Literature overlap searches cannot rule out unindexed earlier calculations, and no independent mathematical audit has been performed.

## References

[1] P. Pokora and X. Roulleau, *Construction of free arrangements using point-line operators*, arXiv:2403.20024v1 (first public version, 2024-03-29), Remark 2.5 and the description of \(\Lambda_{\{2\},3}(\mathcal C_{10})\). https://arxiv.org/html/2403.20024v1

[2] L. Kühne and X. Roulleau, *Regular polygons, line operators, and elliptic modular surfaces as realization spaces of matroids*, arXiv:2312.03470 (first public version, 2023-12-06). https://arxiv.org/abs/2312.03470
