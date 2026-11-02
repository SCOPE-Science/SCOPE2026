# The exact blocking and skew-line census of smooth binary plane quartics

## Finding

Let \(\mathcal F\) be the set of nonzero homogeneous ternary quartic forms \(F\in\mathbb F_2[X,Y,Z]_4\). Distinct coefficient vectors count as distinct forms; multiplication by nonzero scalars creates no identifications over \(\mathbb F_2\). A form is **smooth** if its plane zero-locus \(C_F\) is geometrically nonsingular. Let
\[
 n(F)=\#C_F(\mathbb F_2),\qquad
 s(F)=\#\{L\in\mathbb P^{2\vee}(\mathbb F_2):L(\mathbb F_2)\cap C_F(\mathbb F_2)=\varnothing\}.
\]
Here \(s(F)\) counts *skew rational lines* (lines with no rational incidence with the curve); a curve is *blocking* exactly when \(s(F)=0\). These are conditions on rational point sets, not geometric intersection multiplicities.

The complete joint distribution among **all geometrically smooth** quartic forms is:

| \(n(F)\) | \(s(F)\) | Number of forms | Projective-equivalence orbits |
| ---: | ---: | ---: | ---: |
| 0 | 7 | 165 | 4 |
| 1 | 4 | 1,008 | 7 |
| 2 | 2 | 2,646 | 18 |
| 3 | 0 | 672 | 4 |
| 3 | 1 | 2,688 | 19 |
| 4 | 0 | 2,016 | 12 |
| 4 | 1 | 525 | 5 |
| 5 | 0 | 1,008 | 7 |
| 6 | 0 | 168 | 1 |
| 7 | 0 | 24 | 1 |
| **Total** | | **10,920** | **78** |

In particular, exactly \(3,888\) of the \(10,920\) smooth forms are blocking, so the **exact probability** for a uniformly random smooth quartic coefficient vector is
\[
 \boxed{\Pr(\text{blocking}\mid\text{geometrically smooth})=\frac{3888}{10920}=\frac{162}{455}.}
\]
The blocking forms occupy exactly \(25\) of the \(78\) projective equivalence orbits; the other \(7,032\) smooth forms lie in \(53\) nonblocking orbits. The possible numbers of skew rational lines are precisely \(0,1,2,4,7\), occurring for respectively \(3,888,3,213,2,646,1,008,165\) forms. Rational point count alone does not determine blocking: both \(n(F)=3\) and \(n(F)=4\) split into blocking and nonblocking types.

## Assumptions and scope

The field is exactly \(\mathbb F_2\), with all \(15\) degree-four monomials retained. There are \(2^{15}-1=32,767\) nonzero forms; the zero polynomial is excluded from \(\mathcal F\), but is included in the comparison probability over all coefficient vectors. Geometric smoothness is checked over an algebraic closure, not merely at the seven rational points. Projective-equivalence orbits refer to the natural \(\operatorname{PGL}_3(\mathbb F_2)=\operatorname{GL}_3(\mathbb F_2)\) action, of order \(168\). No count of isomorphism classes over larger base fields or extension-field rational points is claimed.

## Proof

**(1) Incidence model.** Represent the seven rational projective points by all nonzero vectors \(v\in\mathbb F_2^3\); scalar equivalence is trivial. Each nonzero linear form \(\ell\in(\mathbb F_2^3)^\vee\) specifies a line containing exactly the three nonzero vectors in its kernel, giving all seven lines. For a quartic form represented by its 15-bit coefficient mask, evaluate the 15 monomials at these points. Since evaluations are linear in the coefficients over \(\mathbb F_2\), a bitwise XOR gives its exact seven-bit point mask. For each of the seven lines, test whether at least one incident point lies on \(C_F\). This computes \(n(F)\) and \(s(F)\) exactly, for any coefficient mask.

**(2) Projective symmetries and exhaustive coverage.** The three displayed elementary matrices in `verify_blocking_quartics.py` generate all \(168\) elements of \(\mathrm{GL}_3(\mathbb F_2)\): their closure is explicitly enumerated and checked. Each matrix acts on the 15-dimensional quartic space by exact polynomial substitution over \(\mathbb F_2\). Starting with the lexicographically first unvisited nonzero coefficient mask, repeatedly apply the three generators; mark every visited form and record its orbit size. The exhaustive loop visits every integer coefficient mask from \(1\) through \(32767\), checks no orbit overlaps, and produces exactly \(279\) orbits with total orbit-weight \(32767\). Every orbit size divides \(168\). Thus one representative per orbit suffices for both smoothness and point-line incidence tests, provided its orbit size is used as weight.

**(3) Geometric smoothness, without finite-field sampling.** For each orbit representative, the program forms the four equations \(F=F_X=F_Y=F_Z=0\) in characteristic two. A common geometric projective zero exists precisely when these four equations have a common zero on at least one of the charts \(Z=1\), \(Z=0,Y=1\), and the single remaining point \([1:0:0]\). On the first chart the four dehomogenized polynomials are in \(\mathbb F_2[X,Y]\), and on the second they are in \(\mathbb F_2[X]\). Over an algebraic closure, the weak Nullstellensatz gives that the equations have **no** common zero if and only if they generate the unit ideal. The script computes this condition by a finite, exact Buchberger algorithm over \(\mathbb F_2\), with monic leading terms, S-polynomials, polynomial division, and termination when all pairs reduce to zero or a nonzero constant is produced. The final point is evaluated directly. This is an algebraic-closure criterion, not a search over selected extensions. Smoothness is preserved under the projective group action.

**(4) Weighted, exact aggregation.** For every representative passing (3), its orbit size is added to the bin indexed by \((n(F),s(F))\) from (1). The resulting ten pairs of bin counts are those in the Finding table. Their sum is \(10,920\); the number of qualifying orbits is \(78\). Summing the five bins with \(s=0\) gives
\[
 672+2016+1008+168+24=3888,
\]
and summing their orbit multiplicities gives \(4+12+7+1+1=25\). The complement has \(10,920-3888=7032\) nonblocking forms. Every integer in this proof is calculated exactly by the complete, independently executable finite procedure; no asymptotic heuristic or incomplete sample enters the assertion.

**(5) Incidence-profile interpretation.** The ten possible \((n,s)\) pairs are also all incidence types of arbitrary subsets of the seven-point Fano plane. For \(n=3\), a collinear triple meets every line and gives \(s=0\), whereas a triangle misses its complementary line and gives \(s=1\). For \(n=4\), a complement of a line has \(s=1\), whereas the other four-point sets contain a full line and have \(s=0\). For \(n\ge5\), every subset meets all seven lines. The table determines the precise relative frequencies of these incidence patterns *among smooth quartics*.

## Verification

Execute `python3 verify_blocking_quartics.py` using Python 3 and its standard library. Expected final success sentinel: `COMPLETE_BINARY_QUARTIC_BLOCKING_CENSUS_PASS`. Its assertions independently check the size of the acting group; the partition of all \(32,767\) nonzero quartic forms into \(279\) orbits; the exact ten incidence bins; the \(10,920\) smooth forms and \(78\) smooth projective orbits; the \(25\) blocking orbits; and the equality of the blocking probability to \(162/455\). For comparison, a direct check of all nonzero forms gives \(16,383\) blocking forms, so adding the zero form gives \(16,384\) blocking forms among \(32,768\) coefficient vectors, exactly one half. This agrees with the previously proved unconditional binary-field probability. An independent symbolic Gröbner-ideal evaluation on all 279 representatives was also compared with the exact finite census; it agreed on all 78 smooth orbits and their incidence totals. That comparison is corroboration; the standalone code is the replayable certificate.

The calculation is exhaustive in its specified finite parameter space. Buchberger's algorithm supplies the geometric (infinite-algebraic-closure) singularity criterion; counting rational-point masks alone would **not** suffice for geometric smoothness. The finite proof is valid conditional on inspecting the supplied algorithm and its exact implementation; no independent external validation is asserted.

## Relationship to prior work

Asgarli–Ghioca–Yip, *Most plane curves over finite fields are not blocking*, proves that the unconditional blocking probability for uniformly chosen binary ternary forms of degree at least three is \(1/2\), and provides asymptotic estimates conditioned on smoothness as degree grows. Those results do **not** state the exact degree-four conditional probability or its joint incidence table. Their separate work *Plane curves giving rise to blocking sets over finite fields* motivates the smooth-plane-curve blocking question, including the existence of rational lines avoiding the curve's rational point set. The present count is a fully finite degree-four specialization with geometric smoothness imposed; it is not an extrapolation from their limiting formulas.

Nart–Ritzenthaler classify the \(78\) \(\mathbb F_2\)-isomorphism classes of smooth nonhyperelliptic genus-three curves; the \(78\) smooth projective orbits computed here agree with that known classification. Their published count is not itself a tabulation of the rational point versus skew-line incidence pairs or a count of coefficient vectors satisfying both smoothness and blocking. The earlier classification does provide a theoretical alternative route to the finite enumeration and remains the closest source for possible implicit coverage.

## Limitations

This is a finite, machine-assisted exact enumeration, not a theorem for arbitrary fields, degrees, or genera. Although the Buchberger test checks geometric smoothness, the verifier has not undergone independent audit. The 25 blocking orbits are counts of projective equivalence classes, not counts of inequivalent curves over an algebraic closure. Its significance is the explicitly motivated finite smooth-quartic conditional distribution and full incidence refinement; generalization to other degrees is not established. Earlier comprehensive classifications of binary quartics may permit reconstruction of the answer from their models, and unindexed treatments of blocking incidence remain a priority risk. No assertion of independently certified novelty is made.

## References

1. S. Asgarli, D. Ghioca, and C. H. Yip, *Most plane curves over finite fields are not blocking*, arXiv:2211.08523 (first public posting 2022-11-15), https://arxiv.org/abs/2211.08523 .
2. S. Asgarli, D. Ghioca, and C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299 (2022), https://arxiv.org/abs/2208.13299 .
3. E. Nart and C. Ritzenthaler, *Non-hyperelliptic curves of genus three over finite fields of characteristic two*, arXiv:math/0312366 (2003), https://arxiv.org/abs/math/0312366 .
