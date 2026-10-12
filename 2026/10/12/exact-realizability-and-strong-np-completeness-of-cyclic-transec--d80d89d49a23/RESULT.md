# Exact realizability and strong NP-completeness of cyclic-transect richness curves

## Finding

**Theorem (complete inverse criterion and complexity).** Fix integers \(n\ge2\) and \(s\ge1\). Consider \(s\) named species in \(n\) circularly arranged habitat cells. Each species occupies at least one cell, occupancy is binary, and different species may overlap or have identical occupancy patterns. For each \(1\le k\le n\), let \(R_k\) be the mean number of distinct species encountered in a uniformly translated cyclic window of exactly \(k\) consecutive cells (all \(n\) starting positions receive weight \(1/n\)).

For any rational input curve \((R_1,\ldots,R_n)\) with \(R_n=s\), define the candidate gap multiplicities
\[
H_j=n(2R_{j+1}-R_j-R_{j+2})\quad(1\le j\le n-2),\qquad H_{n-1}=n(R_n-R_{n-1}).
\]
The curve is realizable by such a binary incidence community **if and only if** every \(H_j\) is a nonnegative integer and the multiset consisting of \(H_j\) items of size \(j+1\), for each \(1\le j\le n-1\), fits into at most \(s\) bins of common capacity \(n\). Unused bins correspond to ubiquitous species. For every realizable curve, the multiset of lengths of all maximal consecutive *absence* runs, pooled across species, is uniquely determined by the curve: it contains precisely \(H_j\) runs of length \(j\).

In the explicit-input decision problem where \(n,s\) are written in unary and the exact rational values of the entire curve are supplied, realizability is **strongly NP-complete**, already on nondecreasing discretely concave curves with denominator dividing \(n\). Thus monotonicity, concavity, and integer-scaled increments do not characterize realizability.

For example, with \(n=5\), \(s=2\), the curve
\[
(R_1,R_2,R_3,R_4,R_5)=(3/5,6/5,9/5,2,2)
\]
is nondecreasing and concave, but is not realizable. Its forced absence-run multiset is \(\{2,2,3\}\), requiring bin-packing item sizes \(\{3,3,4\}\), which do not fit in two bins of capacity \(5\).

## Assumptions and scope

The positions are the cyclic group \(\mathbb Z/n\mathbb Z\). For species \(i\), write \(X_i\subseteq\mathbb Z/n\mathbb Z\) for a nonempty occupied set. A length-\(k\) window starting at \(t\) is \(W_{t,k}=\{t,t+1,\ldots,t+k-1\}\), with cyclic reduction. Set
\[
R_k=\frac1n\sum_{t=0}^{n-1}\sum_{i=1}^s\mathbf1\{X_i\cap W_{t,k}\ne\varnothing\}.
\]
The row masks \(X_i\) are unrestricted apart from nonemptiness; in particular, there is no constraint on column totals, connectivity, distinctness of row masks, dispersal, or observation error. The theorem concerns the arithmetic mean over translations, not the full distribution of richness, independent random subsets of cells, two-dimensional windows, or logarithmic-axis curvature.

A **maximal cyclic absence run** for species \(i\) is a maximal cyclicly consecutive block of cells outside \(X_i\). A fully occupying species has no absence runs. Every absence run has length between \(1\) and \(n-1\), and two distinct such runs in one species are separated by at least one occupied cell.

## Proof

**1. Exact gap formula.** For any species, a translated \(k\)-cell window avoids it exactly when the window is wholly contained in a maximal absence run. A run of length \(g\) contains precisely \((g-k+1)_+=\max\{g-k+1,0\}\) choices of a window's starting cell. These starting sets are disjoint for distinct absence runs. If \(\mathcal G\) denotes the pooled multiset of all absence-run lengths, summing over species gives
\[
n(s-R_k)=\sum_{g\in\mathcal G}(g-k+1)_+\qquad(1\le k\le n).
\]
This identity also covers species occupying all cells, which contribute an empty run multiset. In particular, \(R_n=s\).

**2. Inversion and discrete curvature.** Subtract the identity at successive window widths. For every \(1\le k<n\),
\[
n(R_{k+1}-R_k)=\#\{g\in\mathcal G:g\ge k\}.
\]
Taking one more difference recovers the count of runs of length exactly \(j\). For \(1\le j\le n-2\) this count is \(n(2R_{j+1}-R_j-R_{j+2})\), while the run count for \(n-1\) is \(n(R_n-R_{n-1})\). Thus the prescribed values \(H_j\) must be nonnegative integers, and the pooled absence-run spectrum is uniquely identifiable from the entire mean curve. The tail counts decrease with \(k\), so all realizable curves are nondecreasing and discretely concave on the linear axes. Conversely, if nonnegative integer \(H_j\) are supplied and the constructed occupancy realizes these gaps, the same identity recovers \(R_n=s\) and all differences \(R_{k+1}-R_k\), hence reproduces the complete given curve.

**3. Necessary packing inequality.** Consider one species with absence-run lengths \(g_1,\ldots,g_r\). It has at least \(r\) occupied cells, one separating consecutive cyclic absence runs. Since the entire cycle has \(n\) cells,
\[
\sum_{a=1}^{r}(g_a+1)\le n.
\]
Assign each of its runs to that species' bin. The pooled list of items, one of size \(g+1\) for each absence run of length \(g\), therefore fits in \(s\) capacity-\(n\) bins. A fully occupied species contributes an empty bin.

**4. Sufficient construction.** Conversely, suppose these items can be assigned to \(s\) bins, with total item size in each bin at most \(n\). For a nonempty bin holding lengths \(g_1,\ldots,g_r\), construct the cyclic word
\[
0^{g_1}1\,0^{g_2}1\cdots0^{g_r}1\,1^{\,n-\sum_a(g_a+1)}.
\]
It has length \(n\), contains an occupied cell, and its maximal cyclic zero runs have precisely the assigned lengths. Its last and first blocks do not create an extra zero run. For an empty bin use the all-one cyclic word. Making one species from each bin realizes the exact pooled gap counts and therefore, by Step 2, the prescribed curve. This proves the if-and-only-if assertion, including both boundaries \(r=0\) and the equality case \(\sum_a(g_a+1)=n\).

**5. Membership in NP.** In the explicit decision encoding, both \(n\) and \(s\) are unary and the rational curve is fully listed. An \(s\)-by-\(n\) binary incidence matrix is a polynomial-size certificate. Check every row's nonemptiness and compute all \(n^2\) cyclic-window species counts with exact integer arithmetic; comparison to the input fractions is polynomial-time. Alternatively, a gap-to-bin assignment is a polynomial-size certificate once all \(H_j\) are nonnegative.

**6. Strong NP-hardness.** Reduce from the classical strongly NP-complete 3-PARTITION problem. An instance has \(3m\) positive integers \(a_1,\ldots,a_{3m}\), a target \(B\), \(B/4<a_i<B/2\), and \(\sum_i a_i=mB\). Multiplying all numbers and \(B\) by a fixed factor if needed ensures \(a_i\ge2\). Construct a curve with \(n=B\) and \(s=m\):
\[
R_k=m-\frac1B\sum_{i=1}^{3m}(a_i-k)_+\qquad(1\le k\le B).
\]
The inversion in Step 2 forces exactly one absence run of length \(a_i-1\) for each input item (counted with multiplicities); the associated bin-packing item sizes are exactly \(a_i\). All such items have total size \(mB\), equal to total bin capacity, so feasibility of the curve is equivalent to partitioning the \(3m\) integers into \(m\) bins of capacity \(B\). Every bin must have exactly three items because \(B/4<a_i<B/2\), hence this is precisely the original 3-PARTITION instance. The constructed \(R_k\) is nondecreasing, discretely concave, and a multiple of \(1/B\); every entry is computable by a sum of \(3m\) integers. Strong NP-completeness of 3-PARTITION allows restricting \(B\) to polynomially bounded size, so the unary values \(n=B,s=m\) and the \(B\) rational entries are produced in polynomial time. Thus the restricted richness-curve realizability problem is strongly NP-hard, and together with Step 5 strongly NP-complete.

**7. Explicit concave-but-infeasible boundary.** For \(n=5,s=2\), the candidate gap lengths \(2,2,3\) induce the stated sequence \((3/5,6/5,9/5,2,2)\). The increments are \((3/5,3/5,1/5,0)\), so concavity and denominator constraints hold. But item sizes \(3,3,4\) cannot be packed into two bins of size \(5\): each of the three items requires its own bin. The converse in Step 4 rules out any occupancy realization. This is an explicit obstruction separate from mere curve-shape testing.

## Verification

A standalone, standard-library Python checker is included as `verify_gap_curve.py`; run it with `python3 verify_gap_curve.py`. It directly counts translated windows on each incidence matrix, independently extracts its maximal cyclic zero runs, reconstructs the curve from those runs, inverts the curve, and tests the packing criterion by exact backtracking.

The checked instance classes comprise every nonempty species-row choice for \((n,s)\) equal to \((2,1),(3,2),(4,2),(4,3),(5,2),(5,3),(6,2)\), totalling \(38{,}373\) incidence matrices and \(195\) distinct curve signatures summed across those seven parameter pairs. For \(n\le5\) in those cases, the checker additionally exhausts every nonnegative gap histogram whose total compulsory size is at most \(ns\), and confirms that packability exactly matches direct realizability. It also checks the specified infeasible curve and a positive instance of the partition construction. Computations use `fractions.Fraction` and exact integers, without numerical tolerances. These tests are finite corroboration; the unrestricted theorem rests on Steps 1–6, not on enumeration.

## Relationship to prior work

Tjørve, Kunin, Polce, and Tjørve (2008) analyze the effects of occupancy and aggregation on species–area curves, explicitly including wrapped-around sampling windows in modeled grids and discussing the possibility of inferring spatial patterns from SAR shape. That source motivates treating spatially explicit incidence data as an inverse problem, but its random-placement formulas and numerical grid comparisons do not establish the pooled zero-run spectrum, a complete single-dimensional realizability criterion, or computational hardness. Its convex/concave descriptions in logarithmic coordinates are not statements about the present linear-coordinate discrete concavity.

Colwell, Mao, and Chang (2004) derive incidence-based accumulation curves under exchangeability or random ordering of quadrat samples. Their independent/quadrat-order-averaged protocol does not preserve the adjacency of the translated cyclic windows used here. Storch (2016) compares sampling designs including sliding windows and geometric constraints on species–area relationships, without classifying which exact cyclic mean curves arise from binary occupancy communities. The classic Garey–Johnson 3-PARTITION theorem supplies the known complexity premise; its ecological embedding and the gap-packing equivalence are the statements proved here. Published circular binary-run counts concern enumeration of runs. Ota and Manada (2024) reconstruct a single existing circular word from frequencies of all substrings under an automaton condition; their much richer single-word measurements do not imply existence or feasibility of an aggregate multispecies zero-window profile.

## Limitations

The claimed inverse uniquely identifies only the **pooled multiset of absence-run lengths**, not the individual species' assignments, positions, occupancy patterns, or habitat correlations. The NP-completeness result concerns the exact finite input problem with unary dimensions, not approximate inference from noisy field measurements. Strong NP-completeness does not prohibit efficient algorithms for fixed numbers of species, restricted gap sizes, or typical ecological data. The proof does not extend automatically to irregular sampling layouts, open-boundary linear transects, arbitrary two-dimensional neighborhoods, random quadrat subsets, or unequal translation weights. The exact reference and literature comparison do not constitute an independent novelty certification; coverage in less readily searchable sources remains possible.

## References

1. Tjørve, E., Kunin, W. E., Polce, C., and Tjørve, K. M. C. (2008). “Species–area relationship: separating the effects of species abundance and spatial distribution.” *Journal of Ecology* 96, 1141–1151. DOI: 10.1111/j.1365-2745.2008.01433.x. First published 15 October 2008. https://doi.org/10.1111/j.1365-2745.2008.01433.x
2. Colwell, R. K., Mao, C. X., and Chang, J. (2004). “Interpolating, extrapolating, and comparing incidence-based species accumulation curves.” *Ecology* 85, 2717–2727. DOI: 10.1890/03-0557. Author-hosted full text: https://www.robertkcolwell.org/publications/7532.pdf
3. Storch, D. (2016). “The theory of the nested species–area relationship: geometric foundations of biodiversity scaling.” *Journal of Vegetation Science* 27, 880–891. DOI: 10.1111/jvs.12428. https://doi.org/10.1111/jvs.12428
4. Garey, M. R., and Johnson, D. S. (1975). “Complexity results for multiprocessor scheduling under resource constraints.” *SIAM Journal on Computing* 4, 397–411. DOI: 10.1137/0204035. https://doi.org/10.1137/0204035
5. Garey, M. R., and Johnson, D. S. (1979). *Computers and Intractability: A Guide to the Theory of NP-Completeness*. W. H. Freeman. 3-PARTITION, problem SP15.
6. Leitner, W. A., and Rosenzweig, M. L. (1997). “Nested species-area curves and stochastic sampling: A new theory.” *Oikos* 79, 503–512. DOI: 10.2307/3546894. https://doi.org/10.2307/3546894
7. Makri, F., Psillakis, Z., and Arapis, A. (2013). “Counting runs of ones with overlapping parts in binary strings ordered linearly and circularly.” *International Journal of Statistics and Probability* 2(3), 50. DOI: 10.5539/ijsp.v2n3p50. https://doi.org/10.5539/ijsp.v2n3p50
8. Ota, T., and Manada, A. (2024, advance publication 2023). “A Reconstruction of Circular Binary String Using Substrings and Minimal Absent Words.” *IEICE Transactions on Fundamentals of Electronics, Communications and Computer Sciences* E107-A, 409–416. DOI: 10.1587/transfun.2023TAP0015. https://doi.org/10.1587/transfun.2023TAP0015
