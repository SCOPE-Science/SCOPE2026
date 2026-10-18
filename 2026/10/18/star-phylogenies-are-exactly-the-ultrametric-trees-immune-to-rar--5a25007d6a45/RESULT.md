# Star phylogenies are exactly the ultrametric trees immune to rarefaction losses from abundance balancing

## Finding

Let a rooted ultrametric phylogenetic tree have strictly positive branch lengths, a positive-integer abundance at each tip, and uniform fixed-size sampling without replacement. A **unit balancing transfer** moves one individual from species \(i\) to species \(j\) when their abundances satisfy \(a_i\ge a_j+2\). Let \(E_T(m;\mathbf a)\) be expected rooted Faith phylogenetic diversity of a sample of \(m\) individuals.

**Star characterization.** All unit balancing transfers weakly increase \(E_T(m;\mathbf a)\) for every admissible census and sampling depth if and only if all pairs of distinct tips have the same phylogenetic distance (a phylogenetic star, allowing a common stem before the single branching level).

**Universal nonstar reversal.** On every other rooted ultrametric tree with positive branches, some strictly positive integer abundance profile and a unit balancing transfer satisfy simultaneously
\[
E_T(2;\mathbf a')<E_T(2;\mathbf a),\qquad
E_T(N-1;\mathbf a')>E_T(N-1;\mathbf a).
\]
Here \(N\) is the population size, unchanged by the transfer.

**Sharp census threshold.** For every ultrametric tree and every positive-integer population of \(N\le5\) individuals, all unit balancing transfers weakly increase expected rooted phylogenetic diversity at every sampling depth. Six individuals, and at least three tip species, are therefore necessary and sufficient for a loss at some sampling depth and a subsequent gain under the same transfer.

Specifically, take three species \(A,B,C\), with \(B,C\) forming a cherry. Let the root-to-tip height be \(1\), the root-to-\(BC\) internal edge length be \(1-\varepsilon\), and the terminal edges to \(B,C\) have length \(\varepsilon\), where \(0<\varepsilon<1\); the edge to \(A\) has length \(1\). For the balancing transfer
\[
(3,1,2)\longmapsto(2,2,2),
\]
the six expected-diversity differences, in order of sampling depths \(m=1,\ldots,6\), are exactly
\[
\left(0,\frac{2\varepsilon-1}{15},\frac{5\varepsilon-2}{20},
\frac{4\varepsilon-1}{15},\frac{\varepsilon}{6},0\right).
\]
For \(\varepsilon=1/3\), these are
\[
\left(0,-\frac1{45},-\frac1{60},\frac1{45},\frac1{18},0\right),
\]
so the response changes strictly from negative at three draws to positive at four draws, while the abundance profile becomes more even.

## Assumptions and scope

The tree \(T\) is finite, rooted, and ultrametric: every species tip is at the same distance \(H>0\) from the fixed root. Branches have positive lengths; redundant degree-two vertices may be suppressed. There are at least two species, each with a positive-integer abundance. The sample contains exactly \(1\le m\le N\) **labeled individuals** chosen uniformly from the \(\binom Nm\) subsets of the complete \(N\)-individual census. Rooted Faith phylogenetic diversity is the total length of the minimal subtree joining the root to every species represented in the sample. Tree topology and branch lengths remain unchanged by the transfer. A transfer is allowed only when \(a_i\ge a_j+2\), so all abundances stay positive. An all-equal pairwise-tip-distance tree is called star-like, even if a common unbranched stem precedes the single branching level.

## Proof

**1. Layer representation and discrete concavity.** For a clade of \(u\) individuals, put
\[
f_m(u)=1-\frac{\binom{N-u}{m}}{\binom Nm},
\]
where a binomial coefficient is zero if its upper argument is smaller than the lower. At height \(t\) from the root, let \(\Pi_t\) be the partition of tip species into descendant clades intersected by a horizontal cut. Integrating the number of sampled clades over height yields the exact expectation
\[
E_T(m;\mathbf a)=\int_0^H\sum_{B\in\Pi_t}f_m\!\left(\sum_{i\in B}a_i\right)\,dt.
\]
The discrete increments obey
\[
f_m(u+1)-f_m(u)=\frac{\binom{N-u-1}{m-1}}{\binom Nm},
\]
which is nonincreasing in \(u\). Thus \(f_m\) is discretely concave for every \(m\), including the cases where the increments vanish.

**2. Stars satisfy the transfer principle.** On a star-like tree every horizontal cut either has just one clade containing all species or separates every species into its own clade. The first kind contributes the fixed value \(f_m(N)=1\). For the second, a transfer from \(a_i\) to \(a_j\) changes \(\sum_r f_m(a_r)\) by
\[
\bigl[f_m(a_j+1)-f_m(a_j)\bigr]
-\bigl[f_m(a_i)-f_m(a_i-1)\bigr]\ge0
\]
because \(a_i-1\ge a_j+1\). Integrating proves universal nondecrease.

**3. The two-draw distance law.** Write \(d_{rs}\) for the patristic distance between tips \(r\) and \(s\). An unordered two-individual sample has rooted diversity \(H+d_{rs}/2\) when its members belong to distinct species, and \(H\) otherwise. Consequently,
\[
E_T(2;\mathbf a)
=H+\frac{1}{N(N-1)}\sum_{r<s}a_ra_sd_{rs}.
\]
Under a unit transfer \(i\to j\), the change in the numerator is exactly
\[
(a_i-a_j-1)d_{ij}
+\sum_{k\ne i,j}a_k(d_{jk}-d_{ik}).\tag{1}
\]

**4. Every nonstar reverses.** A nonstar ultrametric has three distinct tips \(i,j,k\) with \(d_{jk}<d_{ik}=d_{ij}\). Assign \(a_i=3\), \(a_j=1\), \(a_k=M\), and one individual to every other tip. In (1), the coefficient of \(M\) is the strictly negative quantity \(d_{jk}-d_{ik}\), whereas every other term is independent of \(M\). Choosing a sufficiently large integer \(M\) therefore makes the two-draw expected diversity decrease strictly.

At sample size \(N-1\), exactly one labeled individual is omitted, uniformly. The transfer eliminates the only singleton at species \(j\); its loss from the complete tree would have removed precisely its terminal pendant length \(\ell_j>0\). Species \(i\) still has at least two individuals, and every other species retains its abundance. Thus
\[
E_T(N-1;\mathbf a')-E_T(N-1;\mathbf a)=\frac{\ell_j}{N}>0.
\]
This proves the reversal and the converse direction of the characterization. No claim is made about the exact intermediate transition depths on an arbitrary tree.

**5. Why fewer than six individuals cannot work.** If \(N\le5\), a nontrivial transfer involving only two species is a move toward equality of their two positive abundances. Every horizontal cut has either one clade or two singleton-species clades, and concavity makes each cut's contribution nonnegative.

With three or more species, the only nontrivial transfer possible for \(N\le5\) is, up to relabeling,
\[
(3,1,1)\longmapsto(2,2,1)
\qquad(N=5).
\]
At any ultrametric cut, the partition of these three species has one block, three singleton blocks, or one doubleton block plus one singleton block. The one-block contribution is unchanged, and the three-block contribution increases by concavity. For a doubleton-plus-singleton cut, the donor and recipient are either in the same block (no change), on opposite sides with masses \((3,2)\to(2,3)\) (no change), or on opposite sides with masses \((4,1)\to(3,2)\) (nonnegative by concavity). There are no other cases. The layer integral therefore proves nondecrease for all \(m\) and all tree shapes. With at least four species and \(N\le5\), the required two-unit donor-recipient abundance difference cannot occur. This proves the sharp lower bound.

**6. Six-individual realization.** In the three-tip tree stated above, the descendant sets of the four edges are \(\{A\}\), \(\{B,C\}\), \(\{B\}\), and \(\{C\}\), with respective lengths \(1\), \(1-\varepsilon\), \(\varepsilon\), and \(\varepsilon\). Substitution into the layer expectation from step 1 for the two profiles yields the six displayed affine expressions. Setting \(\varepsilon=1/3\) gives strict negative and positive neighboring sample-depth differences, with all edge lengths strictly positive. Two species are necessarily star-like, so three species are also sharp.

## Verification

Run `python3 phylogenetic_transfer_check.py` with Python 3 and no external packages. The program computes the four-edge expected diversity from exact rational clade-detection probabilities and, independently, from enumeration of every subset of six labeled individuals. It checks the complete depth sequence, checks the affine parameter formula at five distinct branch-length ratios, checks a weakly resolved example with a larger third-species population, and exhausts every feasible positive labeled census, donor-recipient choice, sample depth, and clade partition for populations of at most five individuals. These last tests comprise \(186\) exact cut comparisons. The unrestricted star/nonstar conclusions and sharpness proof do not rely on extrapolation from those checks.

## Relationship to prior work

Nipperess and Matsen (2013) derived exact mean and variance formulas for rooted and unrooted phylogenetic diversity under rarefaction. Chao and colleagues (2015) developed related rarefaction/extrapolation estimators and comparisons, and Nipperess (2016) connected the early rarefaction slope to Rao-type quadratic phylogenetic entropy and phylogenetic evenness. These works provide the underlying sampling formulas and the ecological motivation; the standard two-draw distance representation is not claimed as new. Cadotte and colleagues (2010) developed abundance-sensitive phylogenetic diversity and clade-imbalance indices, a particularly relevant separate concept.

The result here concerns a **transfer between two fixed species abundances**, characterizes exactly which ultrametric trees retain monotonicity for every such transfer, proves that every other tree can exhibit opposite responses at two distinct sampling depths, and establishes the sharp census minimum. These statements are not consequences merely of monotonically increasing diversity *within one rarefaction curve*. The accessible full technical texts inspected did not state a corresponding all-tree characterization or six-individual sharp threshold. Complete technical text for Cadotte and colleagues (2010) could not be inspected; that publication and possible older equivalent formulations remain bibliographic risks.

## Limitations

The theorem is restricted to rooted Faith phylogenetic diversity, known positive integer abundances, uniform individual-based rarefaction without replacement, fixed ultrametric trees, and transfers between two species satisfying the stated donor-recipient inequality. The result is not an assertion about unrooted diversity, non-ultrametric tips, random or uncertain phylogenies, observational detection error, ecological mechanisms that cause abundance transfers, or sampling with replacement. While every nonstar admits some reversal, a prescribed profile or transfer on that tree need not reverse. The proof yields the first possible census size and the three-tip example, not a classification of all larger-census reversal patterns. Bibliographic independence has not been externally certified.

## References

- Cadotte, M. W., Davies, T. J., Regetz, J., Kembel, S. W., Cleland, E., and Oakley, T. H. (2010). Phylogenetic diversity metrics for ecological communities: integrating species richness, abundance and evolutionary history. *Ecology Letters* 13, 96–105. DOI: 10.1111/j.1461-0248.2009.01405.x.
- Nipperess, D. A., and Matsen, F. A. IV (2013). The mean and variance of phylogenetic diversity under rarefaction. *Methods in Ecology and Evolution* 4, 566–572. DOI: 10.1111/2041-210X.12042.
- Chao, A., Chiu, C.-H., Hsieh, T. C., Davis, T., Nipperess, D. A., and Faith, D. P. (2015). Rarefaction and extrapolation of phylogenetic diversity. *Methods in Ecology and Evolution* 6, 380–388. DOI: 10.1111/2041-210X.12247.
- Nipperess, D. A. (2016). The Rarefaction of Phylogenetic Diversity: Formulation, Extension and Application. In *Biodiversity Conservation and Phylogenetic Systematics*, chapter 10. DOI: 10.1007/978-3-319-22461-9_10.
