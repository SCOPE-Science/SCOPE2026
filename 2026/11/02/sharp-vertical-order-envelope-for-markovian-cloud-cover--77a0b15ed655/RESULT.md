# Sharp vertical-order envelope for Markovian cloud cover

## Finding

**Theorem (complete sharp ordering envelope).** Let \(n\ge2\). Suppose a vertically ordered sequence of \(n\) cloudy levels is modeled by a binary nearest-neighbor Markov chain. Its unordered level cloud fractions are known and sorted as
\[
0<p_1\le p_2\le\cdots\le p_n<1.
\]
For every adjacent pair with fractions \(u,v\), prescribe joint cloudy overlap
\[
O_\alpha(u,v)=\alpha\min\{u,v\}+(1-\alpha)uv,
\qquad 0\le\alpha\le1,
\]
with the **same** \(\alpha\) at every gap. The remaining transition probabilities are determined by these two marginal probabilities and this overlap. The common \(\alpha\) is compatible with equally spaced levels and a fixed exponential overlap-decorrelation length.

Define \(r_j=p_j/(1-p_j)\), \(f_j=1+\alpha r_j\), and \(B=\prod_{j=1}^{n}(1-p_j)\). For any permutation \(\pi\) of the cloud fractions, let \(C(\pi)\) be the probability that at least one level is cloudy. Then the **exact, attainable** range is
\[
\boxed{1-B\prod_{j=1}^{n-1}f_j\ \le\ C(\pi)\ \le\ 1-B\prod_{j=1}^{n-1}f_{\lceil j/2\rceil}.}
\]
A monotone increasing (or decreasing) sequence attains the lower bound on cloud cover; in fact every single-peaked ordering does. The upper bound is attained by alternating the smallest cloud fractions with the largest ones, with the largest fractions acting as separators, as constructed in the proof. The extremal arrangements are **independent of the common overlap weight** \(\alpha\).

The sharp uncertainty width
\[
W(\alpha)=B\left[\prod_{j=1}^{n-1}(1+\alpha r_j)-\prod_{j=1}^{n-1}(1+\alpha r_{\lceil j/2\rceil})\right]
\]
is nondecreasing for \(\alpha\in[0,1]\), and is strictly increasing if \(n\ge3\) and all cloud fractions are distinct. For \(\alpha=0\), all arrangements have identical total cover. For \(\alpha=1\), the minimum cloud cover is exactly \(p_n\). If \(n\ge3\) and the cloud fractions are distinct, a nonmonotone arrangement has strictly greater total cover despite every adjacent pair using maximum overlap.

## Assumptions and scope

- The cloud states are Bernoulli variables on a **path** of \(n\) adjacent vertical levels, with their complete joint law specified by the first-order Markov construction; pairwise marginals alone without this Markov assumption are not enough.
- Marginal fractions belong to \((0,1)\), and one constant interpolation weight \(\alpha\in[0,1]\) governs all adjacent pairs. The result permits equal fractions, \(\alpha=0\), and \(\alpha=1\).
- Only the vertical permutation of the fixed fractions changes. Heights, all adjacent weights, and the Markov construction are fixed. When interpreted by exponential decorrelation, gaps must be equal for the common weight to remain fixed under permutation.
- The observable \(C(\pi)\) is total projected cloud **occurrence probability**, not a radiative flux or liquid-water-path statistic.

## Proof

**1. Valid transitions and the cloud-free product.** For any two fractions \(u,v\in(0,1)\), the stipulated joint cloudy probability \(O_\alpha(u,v)\) interpolates between independent overlap \(uv\) and maximal overlap \(\min\{u,v\}\). Each is a valid Bernoulli coupling, and so is their convex combination. Hence all four joint cell probabilities are nonnegative, and the conditional transitions consistently preserve the prescribed marginals. The joint clear probability equals
\[
\begin{aligned}
P_{00}(u,v)
&=1-u-v+O_\alpha(u,v)\\
&=(1-u)(1-v)\left(1+\alpha\min\left\{\frac{u}{1-u},\frac{v}{1-v}\right\}\right).
\end{aligned}
\]
The Markov property therefore yields for the all-clear event \(Q(\pi)=1-C(\pi)\):
\[
Q(\pi)=B\prod_{j=1}^{n-1}
\left(1+\alpha\min\{r_{\pi(j)},r_{\pi(j+1)}\}\right).
\tag{1}
\]
In particular, the ordering dependence is entirely the product of functions of edgewise minima along a spanning path.

**2. Path-degree lower bound on all-clear probability.** Sort the \(n-1\) values \(\min\{r_{\pi(j)},r_{\pi(j+1)}\}\) in nondecreasing order, naming them \(b_1,\ldots,b_{n-1}\). Because a vertex of a path has degree at most two, among all path edges at most \(2k\) can have their minimum at one of the \(k\) lowest-ranked vertices. Thus, with ties resolved by an arbitrary fixed ranking,
\[
b_j\ge r_{\lceil j/2\rceil}\qquad(1\le j<n).
\]
As \(t\mapsto1+\alpha t\) is nondecreasing for \(\alpha\ge0\), equation (1) gives
\[
Q(\pi)\ge B\prod_{j=1}^{n-1}f_{\lceil j/2\rceil}.
\]
This is attained explicitly. For \(n=2m+1\), take the order
\[
p_{m+1},p_1,p_{m+2},p_2,\ldots,p_{2m},p_m,p_{2m+1};
\]
its edge minima are \(r_1,r_1,r_2,r_2,\ldots,r_m,r_m\). For \(n=2m\), take
\[
p_{m+1},p_1,p_{m+2},p_2,\ldots,p_{2m},p_m;
\]
its edge minima are \(r_1,r_1,\ldots,r_{m-1},r_{m-1},r_m\). The case \(m=1\) is included. These patterns attain the maximum total cloud cover.

**3. Path-forest upper bound on all-clear probability.** Fix a rank \(k\). The induced subgraph of the path on the \(n-k\) vertices whose rank exceeds \(k\) is a forest, with at most \(n-k-1\) edges. Consequently, at least \(k\) edges have a minimum at one of the \(k\) lowest-ranked vertices, so
\[
b_k\le r_k\qquad(1\le k<n).
\]
Equation (1) now gives \(Q(\pi)\le B\prod_{j=1}^{n-1}f_j\). Sorting the fractions monotonically achieves equality because the edge minima are \(r_1,\ldots,r_{n-1}\). So does any single-peaked order: each rank except the peak appears exactly once as an adjacent-pair minimum. This proves both sharp cloud-cover bounds.

**4. Growth of the order-uncertainty width.** For each \(j<n\), \(r_j\ge r_{\lceil j/2\rceil}\ge0\). The coefficient of \(\alpha^k\) in either product defining \(W\) is the \(k\)th elementary symmetric polynomial in its corresponding nonnegative coordinate vector. Such coefficients are nondecreasing in each coordinate. Thus every coefficient of the polynomial \(W(\alpha)\) is nonnegative, its constant coefficient is zero, and \(W\) is nondecreasing for nonnegative \(\alpha\). If \(n\ge3\) and the fractions are distinct, at least one coordinate inequality is strict, so the coefficient of \(\alpha\) is positive and \(W\) is strictly increasing. For \(\alpha=1\), \(f_j=1/(1-p_j)\); the upper bound for \(Q\) reduces to \(1-p_n\), proving the asserted minimum cover \(p_n\).

## Verification

The standalone standard-library checker `verify_cloud.py` reconstructs the two-state conditional Markov chain independently from the odds-factorization, enumerates all \(n!\) permutations for \(2\le n\le8\) with four rational overlap weights, checks repeated-fraction examples, and tests the exact sharp constructions and monotone uncertainty width. It completed **369,986 assertions**. These finite computations check formulas and examples; the degree/forest argument above establishes the arbitrary-\(n\) theorem.

With cloud fractions \((1/10,1/5,2/5,3/5)\) and \(\alpha=1/2\), the sharp bounds are
\[
C_{\min}=\frac{454}{625}=0.7264,\qquad
C_{\max}=\frac{3917}{5000}=0.7834,
\]
a difference of exactly \(57/1000\) (5.7 percentage points) at unchanged individual cloud fractions and adjacent overlap weight.

## Relationship to prior work

Bergman and Rasch (2002) formulate exponential cloud-overlap interpolation and construct the full subcolumn distribution by nearest-neighbor Markov transitions (their equations 8–13). They numerically use permutations of example cloud fractions to study **vertical-resolution convergence**, not the sharp extremal coverage order for an arbitrary unordered multiset. Lebrun, Dufresne and Villefranque (2023), Section 2, derive clear-column probabilities as products of such transitions and investigate subgrid representation and radiative properties. These two papers establish the probability model and product methodology; neither is claimed as new here. The new assertion is the explicit global minimum/maximum **over all vertical orderings**, with extremizing constructions for every layer count and the monotone ordering-uncertainty width.

Barker (2008) studies observed overlap and its radiative sensitivity, including a stochastic construction for a given ordered cloud-fraction profile; the inspected Sections 1, 4 and 6 do not optimize cloud cover over all permutations of a fixed unordered profile. Earlier equivalent rearrangement observations in atmospheric modeling or combinatorial optimization remain a priority risk. A negative literature search does not prove priority.

## Limitations

The sharp inequalities require a Markov chain with a common adjacent \(\alpha\); they need not hold with height-dependent weights, prescribed nonadjacent pair correlations, or non-Markov multi-level dependence. Reordering cloud layers is a counterfactual uncertainty analysis, not a physical control. Fractional cloud area is not enough to infer radiative forcing: optical depth, water content and three-dimensional transport are not modeled. Equalities need not have unique configurations when cloud fractions tie or \(\alpha=0\). No independent mathematical audit or empirical validation has been performed.

## References

1. Bergman, J. W., and Rasch, P. J. (2002). *Parameterizing Vertically Coherent Cloud Distributions*. Journal of the Atmospheric Sciences **59**, 2165–2182. DOI: `10.1175/1520-0469(2002)059<2165:PVCCD>2.0.CO;2`. Author-uploaded full text: https://www.researchgate.net/publication/253105389_Parameterizing_Vertically_Coherent_Cloud_Distributions.
2. Lebrun, R., Dufresne, J.-L., and Villefranque, N. (2023). *A Consistent Representation of Cloud Overlap and Cloud Subgrid Vertical Heterogeneity*. Journal of Advances in Modeling Earth Systems **15**, e2022MS003592. https://doi.org/10.1029/2022MS003592.
3. Barker, H. W. (2008). *Overlap of fractional cloud for radiation calculations in GCMs: A global analysis using CloudSat and CALIPSO data*. Journal of Geophysical Research **113**, D00A01. https://doi.org/10.1029/2007JD009677.
