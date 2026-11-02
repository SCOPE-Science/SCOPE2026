# Exceptional reduction primes for the 28-line Fermat-quartic bitangent arrangement

## Finding

Let \(k\) be an algebraically closed field of odd characteristic \(p\), choose a primitive eighth root of unity \(\zeta\in k\), and put \(\mu_4=\{1,\zeta^2,\zeta^4,\zeta^6\}\) and \(U=\{\zeta,\zeta^3,\zeta^5,\zeta^7\}\). Consider the following *reduced* arrangement \(\mathcal A_p\) of 28 distinct lines in \(\mathbb P^2_k\):

\[
\begin{aligned}
H^{xy}_u &: x-u y=0,&H^{yz}_u &: y-u z=0,&H^{zx}_u &: z-u x=0 \qquad (u\in U),\\
B_{a,b}&: x+a y+b z=0 &&&& (a,b\in\mu_4).
\end{aligned}
\]

These are the reductions of the 28 characteristic-zero bitangent (including hyperflex) lines of the Fermat, or Dyck, quartic \(x^4+y^4+z^4=0\). Let \(t_m(p)\) denote the number of geometric intersection points incident to exactly \(m\) of the 28 **distinct** lines. Then:

| Characteristic | \(t_2\) | \(t_3\) | \(t_4\) | All other \(t_m\), \(m\ge2\) |
|---|---:|---:|---:|---|
| \(p=3\) | 0 | 0 | 63 | 0 |
| \(p=5\) | 240 | 16 | 15 | 0 |
| \(p=17\) | 144 | 48 | 15 | 0 |
| every other odd \(p\) | 288 | 0 | 15 | 0 |

Thus the **only odd primes at which the full 28-line incidence lattice changes from characteristic zero are \(3,5,17\)**. The 16 new triple points in characteristic five lie on three \(B\)-lines and no \(H\)-line. The 48 new triple points in characteristic seventeen lie on exactly two \(H\)-lines and one \(B\)-line. In characteristic three every intersection is quadruple: the 28 lines form the complete tangent-line configuration of the Hermitian quartic over \(\mathbb F_9\).

The pair-count identity \(\sum_{m\ge2}\binom m2t_m(p)=\binom{28}{2}=378\) holds in every case.

## Assumptions and scope

The base field is algebraically closed, the characteristic is an odd rational prime, and the line arrangement is precisely the stated cyclotomic specialization. All point counts are **geometric**, so they are invariant under replacing \(\zeta\) by another primitive eighth root. The quartic remains smooth at every odd prime since its partial derivatives are \(4x^3,4y^3,4z^3\). At \(p=3\), the 16 \(B\)-lines cease to be ordinary two-contact bitangents and become fourfold-contact tangents; the theorem concerns the specialization of the 28-line arrangement, not a claim that all 28 remain ordinary bitangents. The excluded characteristic two makes the quartic a fourth power and collapses the root-of-unity parameters.

## Proof

**1. Explicit line equations and persistence of distinctness.** Over a field of characteristic other than two, \(U\) consists of four distinct roots of \(u^4=-1\), and \(\mu_4\) consists of four distinct fourth roots of unity. Each \(H\)-line has one zero coefficient; each \(B\)-line has three nonzero coefficients, with its first coefficient normalized to one. Thus the 28 lines are pairwise distinct. On an \(H\)-line, the Fermat equation restricts to the fourth power of the remaining coordinate. On \(B_{a,b}\), set \(A=ay\), \(B=bz\); then the restriction equals

\[
(-A-B)^4+A^4+B^4=2(A^2+AB+B^2)^2.
\]

If \(p\ne3\), the binary quadratic \(A^2+AB+B^2\) has two distinct roots, giving two tangencies of order two. If \(p=3\), it equals \((A-B)^2\), giving a single fourfold contact. The 12 \(H\)-lines are always hyperflex tangents. The complex line configuration is the one studied in the cited 2023 bitangent-arrangement paper; its known \(288\) double and \(15\) quadruple points provide the characteristic-zero baseline, **not a novelty assertion here**.

**2. A characteristic-independent finite determinant certificate.** Work in the free rank-four integer ring

\[
R=\mathbb Z[Z]/(Z^4+1).
\]

For each of the \(\binom{28}{3}=3276\) unordered triples of the explicit row vectors of line coefficients in \(R^3\), compute the determinant \(d\in R\). Its field norm is exactly the determinant of the \(4\times4\) integer multiplication matrix \(m_d:R\to R\). The complete frequency table for \(|N(d)|\), including zero, is:

| \(|N(d)|\) | 0 | 1 | 2 | 4 | 8 | 9 | 16 | 17 | 32 | 36 | 64 | 256 | 400 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| triples | 60 | 384 | 64 | 864 | 384 | 192 | 560 | 192 | 96 | 192 | 192 | 64 | 32 |

For finer control, the triples with norm \(17\) have **exactly two** \(H\)-lines and one \(B\)-line; the triples with norm \(400\) have **zero** \(H\)-lines. The 60 triples of norm zero consist of 12 all-\(H\) and 48 all-\(B\) triples, corresponding to the already-present 15 quadruple points. The exact verifier computes the full four-way stratification by the number of \(H\)-lines, not merely the displayed totals.

An algebraic integer with nonzero norm remains nonzero modulo any prime not dividing that norm, in every specialization of this cyclotomic ring to a field. Consequently **no new triple concurrency is possible outside \(p=3,5,17\)**. Moreover, the original 15 quadruple points persist as 3 coordinate-pencil points for \(H\) and 12 points of fourfold \(B\)-concurrency: fixing \(a\), fixing \(b\), or fixing the ratio \(b/a\) gives four lines through one point in each of four choices, totaling twelve. These 15 points are pairwise distinct at every odd characteristic other than possibly three; the characteristic-three case is treated separately below. In the other odd characteristics no new triple can appear, so counting pairs forces exactly 288 double points.

**3. Characteristic five: 16 new all-\(B\) triples.** Here \(\mu_4=\mathbb F_5^\times\). Via projective duality, the 16 \(B\)-lines correspond to the \(4\times4\) punctured affine grid \((a,b)\in(\mathbb F_5^\times)^2\). Grid lines \(a=\mathrm{constant}\), \(b=\mathrm{constant}\), and \(b=c a\) for \(c\in\mathbb F_5^\times\) contain four grid points: 12 quadruple concurrences. The remaining affine lines that contain three grid points have the form \(b=m a+n\), with \(m,n\in\mathbb F_5^\times\); each contains \(5-2=3\) points of the grid. There are exactly 16 such lines, hence exactly 16 all-\(B\) triple concurrences. Every line determined by two grid points is defined over \(\mathbb F_5\), so this description exhausts the \(B\)-only incidences. The norm table excludes new triple concurrences involving an \(H\)-line at \(p=5\). The unchanged three \(H\)-quadruples and the twelve \(B\)-quadruples give \(t_4=15\); pair counting then gives \(t_2=378-3(16)-6(15)=240\).

**4. Characteristic seventeen: 48 new mixed triples.** Choose \(\zeta=2\in\mathbb F_{17}\), a primitive eighth root because \(2^4=-1\). The intersection of \(H^{xy}_{2}\) and \(H^{yz}_{2}\) is \([4:2:1]\); it also lies on the \(B\)-line \(x+13y+4z=0\), since \(4+13\cdot2+4=34=0\) modulo 17. The diagonal fourth-root rescalings and coordinate permutations of the Fermat quartic act transitively on the 48 intersections of two \(H\)-lines from distinct coordinate pencils. Therefore each such pair has at least one \(B\)-line through its intersection. The norm table shows that **all newly vanishing triple determinants in characteristic seventeen have precisely two \(H\)-lines**. No extra all-\(B\), single-\(H\), or all-\(H\) triple concurrence appears, and the 15 old quadruples persist unchanged. Since 48 different pairs from distinct \(H\)-pencils have distinct intersection points (an additional \(H\) would give an excluded new all-\(H\) triple), and no two \(B\)-lines can pass through such a point (that would give a new single-\(H\) triple), the 48 points are exactly triple. Pair counting gives \(t_2=378-3(48)-6(15)=144\).

**5. Characteristic three: a Hermitian unital.** The Fermat quartic is the Hermitian curve \(x^{3+1}+y^{3+1}+z^{3+1}=0\) over \(\mathbb F_9\). Both fourth-root sets lie in \(\mathbb F_9\). The fourth-power restrictions in Step 1 show that all 28 distinct lines are tangents at \(\mathbb F_9\)-points of this Hermitian curve, and its \(3^3+1=28\) rational points have exactly 28 distinct tangent lines. Every point of \(\mathbb P^2(\mathbb F_9)\) outside this curve lies on exactly \(3+1=4\) of those tangent lines by Hermitian polarity (its polar line meets the curve in four \(\mathbb F_9\)-points). Since \(|\mathbb P^2(\mathbb F_9)|=9^2+9+1=91\), there are exactly \(91-28=63\) fourfold points. They account for all \(63\binom42=378\) line pairs, so there are no further geometric intersections or singularity multiplicities.

This completes the classification for every odd prime and algebraically closed residue field.

## Verification

The supplied standalone `verify_reduction.py` uses only Python's standard library. It implements exact multiplication in \(\mathbb Z[Z]/(Z^4+1)\), exact Bareiss determinants for multiplication norms, all 3276 line-triple determinants, and the complete norm histogram refined by \(H\)-line count. Separately, it constructs the 28 lines and **exhaustively tests all 378 line pairs against all 28 lines** in finite residue fields in characteristics 3, 5, 7 (control), and 17. The exact finite-field models use \(\mathbb F_9\), \(\mathbb F_{25}\), \(\mathbb F_{49}\), and \(\mathbb F_{17}\), respectively; these contain all displayed line coefficients. The verifier checks that all 28 lines remain distinct, each pair meets, total pair-incidence is 378, every claimed multiplicity count is exact, and the new triples have the asserted types.

Run `python3 verify_reduction.py`; the concluding line is `FERMAT_28_BITANGENTS_ARITHMETIC_INCIDENCE_EXACT_OK`. The universal conclusion rests on the integer-norm argument; finite-field computations alone would not exclude additional bad primes.

## Relationship to prior work

Janasz, Pokora and Zieliński (2023, Proposition 3.2) already determine the complex configuration as 288 double points and 15 quadruple points. Their paper expressly works over \(\mathbb C\). Merta and Zieliński (2024, Lemma 2.1) already determine the 12-line complex hyperflex subarrangement as 48 double and 3 quadruple points. Bethea and Brazelton (2024) establish the symmetry-orbit decomposition of the 28 bitangents, including the 12-plus-16 split. **None of those known complex results is claimed as new.** The new assertion is the complete list of odd residue characteristics with changed concurrency and the exact exceptional incidence tables, especially the distinct characteristic-five and characteristic-seventeen triple-point mechanisms. A known characteristic-zero lattice, even with explicit line equations, does not determine the prime support of all nonzero cyclotomic concurrence determinants without additional arithmetic analysis.

## Limitations

The theorem classifies the **geometric incidence lattice's multiplicity profile** under these particular cyclotomic reductions. It does not classify all projective equivalences of reductions, flat limits of the dual bitangent scheme, scheme structures of the bitangent parameter space, freeness of the line arrangements, or the topology of complements. In characteristic three the arrangement's lines are hyperflex tangents rather than 16 ordinary two-contact bitangents. Historical priority beyond the inspected literature remains a possible risk; the exact arithmetic and source comparisons do not prove absolute novelty.

## References

1. M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514, first public 2023-08-31, Proposition 3.2 and Section 3.2; https://arxiv.org/abs/2308.16514.
2. Ł. Merta, M. Zieliński, *On quartics with the maximal number of the maximal tangency lines*, arXiv:2410.13997, first public 2024-10-17, Lemma 2.1 and Section 2; https://arxiv.org/abs/2410.13997.
3. C. Bethea, T. Brazelton, *Bitangents to symmetric quartics*, arXiv:2410.09242, first public 2024-10-11, Section 4.2; https://arxiv.org/abs/2410.09242.
