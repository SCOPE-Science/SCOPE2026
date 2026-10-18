# The ten rational-locus strata of smooth binary plane quintics

## Finding

Let \(k=\mathbf F_2\), and let \(V=k[X,Y,Z]_5\), a vector space of dimension \(21\). For each nonzero \(F\in V\), denote by \(C_F\) the corresponding plane quintic. A curve is **blocking** if its rational points meet every rational projective line, and **smooth** means geometrically smooth over an algebraic closure.

There are ten \(\operatorname{PGL}_3(k)\)-orbits of subsets of the seven points of \(\mathbf P^2(k)\). The number of *geometrically smooth nonzero quintic equations for each fixed rational-point subset* is exactly as follows. The orbit multiplicity is the number of different subsets of the listed kind, not the number of projective-coordinate classes of curves.

| Rational-point configuration | Number of subsets | Smooth quintics per fixed subset | Blocking? |
| --- | ---: | ---: | --- |
| Empty | 1 | 15,792 | No |
| One point | 7 | 10,422 | No |
| Two points | 21 | 7,544 | No |
| Three collinear points | 7 | 5,000 | Yes |
| Three noncollinear points | 28 | 5,840 | No |
| Four-point quadrangle (complement of a line) | 7 | 5,016 | No |
| Four points containing a line | 28 | 4,233 | Yes |
| Five points | 21 | 3,350 | Yes |
| Six points | 7 | 2,420 | Yes |
| Seven points | 1 | 1,512 | Yes |

Weighting the third column by the second gives exactly \(688128\) smooth quintic equations, including exactly \(242326\) smooth blocking equations, so
\[
\Pr(C_F\text{ blocking}\mid C_F\text{ smooth})=\frac{242326}{688128}=\frac{17309}{49152}\approx0.352153.
\]
There are precisely \(1516\) projective-coordinate classes of smooth blocking quintics and \(2688\) of smooth nonblocking quintics, or \(4204\) classes altogether. The ten-subset-stratum counts and their blocking refinement, not the previously known aggregate \(4204\), are the asserted new classification.

Among all **nonzero** quintic forms the blocking fraction is \(1048575/2097151\), nearly one half. The corresponding probability on the full coefficient vector space including the zero polynomial is exactly \(1/2\); the zero polynomial is not counted as a plane curve.

## Assumptions and scope

All equations have total homogeneous degree five in three variables over \(k=\mathbf F_2\). As \(k^\times=\{1\}\), distinct nonzero coefficient vectors give distinct plane equations up to scalar. Smoothness is tested over the algebraic closure; rational-point membership is evaluated only over \(k\). The seven points of \(\mathbf P^2(k)\) are the nonzero binary triples. A rational line is the kernel of a nonzero binary linear functional. The study concerns the incidence of the *specified plane embedding*, not arbitrary abstract embeddings of a genus-six curve.

## Proof

**Interpolation into seven fibers.** Evaluation at the seven projective points defines a surjective linear map \(V\to k^7\). For example, the seven homogeneous degree-five monomials \(X^5,Y^5,Z^5,X^4Y,X^4Z,Y^4Z,X^3YZ\) restrict to the seven squarefree monomials of positive support on \(k^3\setminus\{0\}\), a basis of all functions on those seven points. Therefore every prescribed zero/nonzero evaluation pattern has exactly \(2^{14}\) coefficient vectors, including the zero polynomial only in the pattern vanishing at every rational point.

**Rational-configuration orbits.** The group \(\operatorname{PGL}_3(k)\) is \(\operatorname{GL}_3(k)\) of order \(168\). Its action on subsets of the Fano plane gives exactly the ten types and multiplicities in the table. Three-point subsets split into collinear triples and noncollinear triangles; four-point subsets split into quadrangles (the complements of lines) and subsets containing a line. Each three-point collinear subset blocks, whereas each noncollinear triple does not. Each four-point subset containing a line blocks, whereas a quadrangle is disjoint from its complementary line. Every set with at least five points blocks, and no set with at most two does.

**Geometric smoothness certificate.** Put \(S=k[X,Y,Z]\), and for \(F\in V\), let \(I_F=(F_X,F_Y,F_Z)\subset S\). Since the degree is five and the characteristic is two, Euler's identity reads \(F=XF_X+YF_Y+ZF_Z\). Thus \(C_F\) is geometrically smooth precisely when the three degree-four partials have no common projective zero over the algebraic closure. Equivalently, they form a regular sequence of three quartics in \(S\), so the complete-intersection quotient \(S/I_F\) has socle degree \(3(4-1)=9\). Hence the following entirely finite rank criterion is **equivalent** to geometric smoothness:
\[
\operatorname{rank}\left(S_6^{\oplus3}\longrightarrow S_{10},\ (A,B,C)\longmapsto AF_X+BF_Y+CF_Z\right)=\dim_k S_{10}=66.
\]
Conversely, if this rank is \(66\), then \((S/I_F)_{10}=0\), so the quotient has finite length and the partial derivatives have no projective common zero. The equivalence holds over the algebraic closure; no finite-extension sampling is used for the proof.

**Exact ten-fiber enumeration.** Represent a quintic by its \(21\) binary monomial coefficients. Choose one zero/nonzero evaluation pattern from each of the ten Fano-subset orbits. The independent direct-fiber program tests all \(2^{21}-1\) nonzero coefficient vectors, retains those with each target pattern, and applies the rank criterion above using a \(66\)-row, \(84\)-column binary matrix. Its resulting counts for the ten representatives, in table order, are
\[
(15792,10422,7544,5000,5840,5016,4233,3350,2420,1512).
\]
The group action preserves geometric smoothness, so these are uniform across each subset orbit. Multiplying by the respective orbit sizes gives the stated totals. This is an exhaustive finite calculation, not a random sample.

**Equation-orbit refinement.** A second program explicitly constructs all \(168\) invertible ternary coordinate substitutions and partitions all \(2^{21}-1\) nonzero quintics into their projective-coordinate orbits. It independently computes geometric smoothness by column elimination in the same mathematically certified multiplication map, and tests blocking by the seven line incidences. It finds \(1516\) smooth blocking orbits and \(2688\) smooth nonblocking orbits. The full distribution reproduces the ten-fiber totals. In particular \(1516+2688=4204\), agreeing with the independently published number of smooth plane-quintic isomorphism classes over \(k\).

## Verification

Compile and run the two standalone source files with a standard C++17 compiler:

```sh
g++ -std=c++17 -O3 -o quintic_fibers quintic_fibers.cpp
./quintic_fibers
g++ -std=c++17 -O3 -o quintic_census quintic_census.cpp
./quintic_census
```

The two programs use separate monomial orderings and distinct matrix-elimination algorithms (row elimination for each fixed evaluation fiber versus column elimination on projective equation orbits). Their output was actually reproduced. The first prints the ten smooth-per-fiber counts; the second reports \(688128\) smooth equations, \(242326\) smooth blocking equations, and the projective-orbit counts. The published weighted point count \(2^{12}=4096\) for the plane-quintic genus-six stratum agrees with the independent identity \(688128/168=4096\).

## Relationship to prior work

Asgarli, Ghioca and Yip (2022, *Plane curves giving rise to blocking sets over finite fields*) frame smooth blocking curves as a geometric question. In *Most plane curves over finite fields are not blocking* (2022), their Example 7.1 computes the unconditioned one-half proportion for binary curves of degree at least three, and their Theorem 1.5 establishes asymptotic independence of smoothness and blocking as the field size grows. Neither gives the degree-five exact ten-fiber joint distribution.

Huang, Kedlaya and Lau (2024, *A census of genus 6 curves over \(\mathbf F_2\)*) enumerate the complete genus-six moduli space, including the plane-quintic stratum, and state its aggregate count of \(4204\) isomorphism classes and weighted count \(4096\). These published counts are used as consistency checks, not claimed anew. Their paper does not present the Fano rational-locus orbit-conditioned smoothness counts or the blocking-conditioned fraction. Their downloadable full equation census could in principle be postprocessed to recover these values; this limits priority claims about unpublished tabulations.

The all-seven-point fiber count \(1512\) and special maximal rational-point configurations have also been investigated separately. The new claim is the *entire ten-stratum refinement and its blocking dependence*, rather than the seven-point extremal slice.

## Limitations

The result is specific to geometrically smooth quintic *plane equations* over \(\mathbf F_2\) and does not assert a formula for other fields or degrees. The direct enumeration is finite but exhaustive; the algebraic regular-sequence argument, not numerical testing over field extensions, justifies geometric smoothness. Projective-coordinate orbit counts do not assert a new classification of abstract genus-six curves. The existing exhaustive genus-six database creates a residual priority risk: the newly stated incidence table may be recoverable from previously distributed but unindexed data. Self-review do not constitute independent audit.

## References

1. S. Asgarli, D. Ghioca, C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, first public preprint 2022-08-28, arXiv:2208.13299. https://arxiv.org/abs/2208.13299
2. S. Asgarli, D. Ghioca, C. H. Yip, *Most plane curves over finite fields are not blocking*, first public preprint 2022-11-15, arXiv:2211.08523, especially Theorem 1.5, Section 6 and Example 7.1. https://arxiv.org/abs/2211.08523
3. Y. Huang, K. S. Kedlaya, J. B. Lau, *A census of genus 6 curves over \(\mathbf F_2\)*, first public preprint 2024-02-01, arXiv:2402.00716, Section 3.3 and Table 1. https://arxiv.org/abs/2402.00716
