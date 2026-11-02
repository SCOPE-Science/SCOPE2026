# Dyadic splitting and marked-point specialization of the integral Klein line arrangement

## Finding

Let \(R=\mathbb Z[\alpha]/(\alpha^2+\alpha+2)\), the full ring of integers of \(\mathbb Q(\sqrt{-7})\). In \(\mathbb P^2_R\) take the effective divisor \(\mathcal D\) cut out by the product of the twenty-one linear forms \(\ell_1,\ldots,\ell_{21}\) displayed below. Its generic geometric fiber is Klein's classical twenty-one-line arrangement. The divisor \(\mathcal D\to\operatorname{Spec}R\) is flat of relative degree \(21\).

**Complete reduction theorem.** At every nonzero prime of \(R\) not lying over \(2\), the geometric fiber consists of twenty-one distinct lines, whose intersections are precisely twenty-one ordinary quadruple points and twenty-eight ordinary triple points. There are no double points or higher intersections. In particular, **the prime above \(7\) is not exceptional for this integral coordinate model**.

There are two primes above \(2\): \(\mathfrak p_0=(2,\alpha)\) and \(\mathfrak p_1=(2,\alpha+1)\), both with residue field \(\mathbb F_2\). The **whole scheme-theoretic** special fibers are respectively

\[
\mathcal D_{\mathfrak p_0}:\quad XYZ(X+Y)^6(X+Z)^6(Y+Z)^6=0,
\]
\[
\mathcal D_{\mathfrak p_1}:\quad XYZ(X+Y)^2(X+Z)^2(Y+Z)^2(X+Y+Z)^{12}=0.
\]

Thus the first reduced fiber is the six-line deletion of \(X+Y+Z=0\) from the Fano plane, with four triple and three double intersection points. The second reduced fiber is the full Fano seven-line arrangement, with seven triple points. The exponents in the displayed equations are exact scheme-theoretic component multiplicities.

The twenty-one generic quadruple points and twenty-eight generic triple points are all defined over \(\operatorname{Frac}(R)\). Their individual projective closures have well-defined reductions at both dyadic primes, and their specialization multiplicity *as distinct labelled generic points* is completely given by the following table. These are counts of coincident sections, not lengths of a Jacobian scheme.

| \(P\in\mathbb P^2(\mathbb F_2)\) | Quadruple at \(\mathfrak p_0\) | Triple at \(\mathfrak p_0\) | Quadruple at \(\mathfrak p_1\) | Triple at \(\mathfrak p_1\) |
|---|---:|---:|---:|---:|
| \([1:0:0]\) | 1 | 4 | 1 | 0 |
| \([0:1:0]\) | 1 | 4 | 1 | 0 |
| \([0:0:1]\) | 1 | 4 | 1 | 0 |
| \([1:1:0]\) | 2 | 0 | 6 | 8 |
| \([1:0:1]\) | 2 | 0 | 6 | 8 |
| \([0:1:1]\) | 2 | 0 | 6 | 8 |
| \([1:1:1]\) | 12 | 16 | 0 | 4 |

Each quadruple column totals \(21\), and each triple column totals \(28\).

## Assumptions and scope

All line and point claims are relative to this *specified integral coordinate presentation*. They are not assertions that every projectively equivalent model over a number field has the same reduction: a change of coordinates with nonunit determinant may alter its special fiber. The base is the entire Dedekind ring \(R\), and geometric fibers mean base change to an algebraic closure of the appropriate residue field. The term ordinary multiple point refers to a transverse intersection of the specified number of **distinct reduced** lines. It does not assert that the nonreduced dyadic fibers have isolated intrinsic singular schemes.

The complete list of defining forms, in the indicated order, is

\[
\begin{aligned}
&X,\ Y+Z,\ \alpha X+Y-Z,\ \alpha X-Y+Z,\ -Y+Z,\\
&X+\alpha Y-Z,\ \alpha X-Y-Z,\ -X+Y+\alpha Z,\ \alpha X+Y+Z,\\
&-X+\alpha Y+Z,\ -X-Y+\alpha Z,\ X+Z,\ -X+\alpha Y-Z,\\
&X+\alpha Y+Z,\ -X+Z,\ X-Y+\alpha Z,\ X+Y+\alpha Z,\\
&Z,\ -X+Y,\ X+Y,\ Y.
\end{aligned}
\]

These are the equations printed by Gévay and Pokora in the source cited below, now interpreted integrally. Every form has a coefficient \(\pm1\), so no fiber acquires an identically zero factor.

## Proof

**1. Finite arithmetic certificate of the good-prime assertion.** Work in the free rank-two integral algebra \(R\), representing elements by \((u,v)\) for \(u+v\alpha\). Multiplication uses \(\alpha^2=-\alpha-2\), and the field norm is

\[
N(u+v\alpha)=u^2-uv+2v^2.
\]

Compute the determinants of all \(\binom{21}{3}=1330\) triples of coefficient vectors. The complete *exact integer* norm histogram is

| Determinant norm | Number of triples |
|---:|---:|
| \(0\) | 112 |
| \(1\) | 169 |
| \(2\) | 228 |
| \(4\) | 271 |
| \(8\) | 320 |
| \(16\) | 156 |
| \(32\) | 70 |
| \(64\) | 4 |

The sum is \(1330\). For every prime outside \(2\), all \(1218\) originally nonzero determinants are units, so no new concurrence occurs upon reduction. The \(112\) identically zero determinants continue to vanish. Distinctness of lines also persists: if two were proportional after reduction, then every triple containing that pair would have zero determinant, contrary to the existence of a unit-determinant triple for that pair. The resulting incidence hypergraph is therefore unchanged from the generic one. Direct incidence grouping of all \(\binom{21}{2}\) pairs gives exactly \(21\) quadruple and \(28\) triple supports; indeed \(21\binom42+28\binom32=210\). The cited literature independently establishes these generic counts. The included exact verifier computes both the norm histogram and the incidence grouping directly from the displayed twenty-one forms.

**2. Two genuinely distinct dyadic fibers.** The polynomial \(T^2+T+2\) reduces to \(T(T+1)\) modulo \(2\). Reducing each of the twenty-one forms with \(\alpha\mapsto0\) or \(\alpha\mapsto1\) gives, by direct grouping of identical forms over \(\mathbb F_2\), exactly the two homogeneous factorizations in the Finding. Their products are nonzero and homogeneous of degree \(21\). For \(\alpha=0\), the reduced lines are the three coordinate axes and the three pair sums; counting their intersections over \(\mathbb F_2\) yields four triple and three double points. For \(\alpha=1\), the extra line \(X+Y+Z\) completes the seven Fano lines, with seven triple points. All these intersections remain distinct over algebraic closures, as they are intersections of explicitly distinct \(\mathbb F_2\)-linear forms.

**3. Specialization of marked intersections.** For each generic intersection support \(I\subseteq\{1,\ldots,21\}\), select any two indices \(i,j\in I\). Its projective coordinates are their coefficient-vector cross product in \(R^3\). At \(\mathfrak p_0\), divide out the highest common power of the local uniformizer \(\alpha\); at \(\mathfrak p_1\), divide out the highest common power of \(\alpha+1\). Reducing the resulting primitive vector gives a nonzero point of \(\mathbb P^2(\mathbb F_2)\), independently of the selected pair. In coordinates, division of \(u+v\alpha\) by the local uniformizer is exact via

\[
\frac{u+v\alpha}{\alpha}=\frac{2v-u}{2}-\frac{u}{2}\alpha
\quad\text{when }u\equiv0\pmod2,
\]
\[
\frac{u+v\alpha}{\alpha+1}=v-\frac{u-v}{2}\alpha
\quad\text{when }u-v\equiv0\pmod2.
\]

Applying these identities to all \(49\) generic supports and checking independence from every pair representing each support produces the seven-row table above. By the valuative criterion for properness, this primitive reduction is exactly the specialization of each corresponding \(\operatorname{Frac}(R)\)-rational point of the projective plane.

**4. Flatness.** Each of the twenty-one defining forms has some unit coefficient; hence their product is not the zero polynomial modulo any prime. Over every discrete valuation localization of \(R\), the homogeneous quotient by this primitive product has no torsion over the valuation ring (Gauss divisibility), so it is flat. Since flatness is local on the Dedekind base, \(\mathcal D\to\operatorname{Spec}R\) is flat.

## Verification

Run the self-contained file `verify_klein.py` with Python 3; it imports only standard-library modules and does not use floating point or any external data files. It checks all \(1330\) characteristic-zero triple determinant norms, reconstructs all \(49\) generic intersection supports, factors the two dyadic special fibers from the list of forms, verifies the exact reduced incidence patterns, and recomputes the specialization of every marked generic intersection point by local primitive division. It also checks that alternative line pairs defining each generic point give the same specialized image.

A complete run prints `KLEIN_21_INTEGRAL_ARITHMETIC_REDUCTION_AND_49_SPECIALIZATIONS_PASS`. These exhaustive finite operations are an exact certificate for the stated finite incidence and arithmetic determinant assertions, not a finite sample from infinitely many primes. The no-other-prime conclusion follows from the norm-unit argument in the proof.

## Relationship to prior work

Gévay and Pokora, *Klein's arrangements of lines and conics* (first public preprint 2022-11-28, arXiv:2211.15309), Section 2.1, give the twenty-one equations over the quadratic field and the coordinates of the twenty-one quadruple and twenty-eight triple intersection points **over the complex numbers**. Pokora and Roé, *The 21 reducible polars of Klein's quartic* (arXiv:1803.06411, first public 2018-03-16), describe the classical group-invariant arrangement and its complex incidence geometry. These inputs and the complex intersection counts are not claimed as new.

The present result concerns the integral line divisor in that specific quadratic-integer model: its exhaustive good-prime criterion, two different dyadic scheme fibers, and the complete reduction of its individually marked generic intersection points. The inspected relevant primary sections do not give these arithmetic conclusions. General identifications of \(\mathrm{PSL}_2(7)\) with Fano-plane symmetry do not themselves determine the component multiplicities or the two distinct arithmetic reductions of these equations.

## Limitations

The statement is tied to the explicit integral presentation. Different integral lattices or coordinate models can have different bad fibers, even when their characteristic-zero arrangements are projectively equivalent. No assertion is made about a canonical reduction independent of model, the intrinsic singular schemes of the nonreduced dyadic divisors, their log-resolutions, or the flat limit of a Jacobian ideal. The marked-point specialization counts are not local intersection lengths. The calculation provides no independent external mathematical validation; its novelty remains subject to the possibility of previously unindexed arithmetic studies.

## References

1. Gábor Gévay and Piotr Pokora, *Klein's arrangements of lines and conics*, arXiv:2211.15309 (first publicly posted 2022-11-28), especially §2.1. https://arxiv.org/abs/2211.15309
2. Piotr Pokora and Joaquim Roé, *The 21 reducible polars of Klein's quartic*, arXiv:1803.06411 (first publicly posted 2018-03-16), especially §1. https://arxiv.org/abs/1803.06411
3. Noam D. Elkies, *The Klein Quartic in Number Theory*, in *The Eightfold Way*, MSRI Publications 35 (1999), pp. 51–102. https://dash.harvard.edu/entities/publication/73120378-7d3e-6bd4-e053-0100007fdf3b
