# Conditional inversion fluctuations under prescribed increasing-value runs

## Finding
Let \(\pi\) be uniform in the symmetric group on \(n\ge2\) labels. Fix a set \(S\subseteq\{1,\ldots,n-1\}\), and condition on the positive-probability event
\[
\mathcal E_S=\{\pi(i+1)=\pi(i)+1\ \text{for every }i\in S\}.
\]
Join consecutive positions \(i,i+1\) whenever \(i\in S\). Let the resulting contiguous blocks, from left to right, have lengths \(\ell_1,\ldots,\ell_b\), where \(\ell_i\ge1\), \(b=n-|S|\), and \(\sum_i\ell_i=n\). The Kendall inversion count
\[
I(\pi)=\sum_{1\le i<j\le n}\mathbf1\{\pi(i)>\pi(j)\}
\]
has the following **complete conditional law**:
\[
I\mid\mathcal E_S\ \overset d=\ \sum_{1\le i<j\le b}\ell_i\ell_j\mathbf1\{U_i>U_j\},
\]
where \(U_1,\ldots,U_b\) are independent continuous uniform random variables. Equivalently, for formal \(z\),
\[
\mathbb E[z^I\mid\mathcal E_S]
=\frac1{b!}\sum_{\sigma\in\mathfrak S_b}z^{\sum_{i<j}\ell_i\ell_j\mathbf1\{\sigma(i)>\sigma(j)\}}.
\]
In particular, the conditional mean and variance are
\[
\mathbb E[I\mid\mathcal E_S]=\frac{n^2-\sum_i\ell_i^2}{4},
\qquad
\operatorname{Var}(I\mid\mathcal E_S)
=\frac1{12}\left[\sum_i\ell_i^2\left(n-\ell_i-2\sum_{j<i}\ell_j\right)^2+\sum_{i<j}\ell_i^2\ell_j^2\right].
\]

**Single-run positional law.** Force the \(L-1\) successions within the positions \(a+1,\ldots,a+L\), where \(2\le L\le n\), \(h=n-L\), and \(0\le a\le h\). This event allows additional successions elsewhere and at the run boundaries. Then
\[
\mathbb E[I\mid\mathcal E_{a,L}]=\frac{n(n-1)-L(L-1)}4,
\]
which is independent of \(a\), while
\[
\boxed{\operatorname{Var}(I\mid\mathcal E_{a,L})
=\frac{L(L-1)}{12}(h-2a)^2
+\frac{h(6Lh+12L^2+2h^2+3h-5)}{72}.}
\]
Thus the conditional variance is maximal at \(a=0,h\), minimal at \(a=\lfloor h/2\rfloor,\lceil h/2\rceil\), and the maximum-minus-minimum is exactly
\[
\frac{L(L-1)}3\left\lfloor\frac{h^2}4\right\rfloor.
\]
The strict inequality between endpoint and center holds precisely when \(h\ge2\).

**Macroscopic fluctuations.** If \(L=L_n\) satisfies \(L_n/n\to\lambda\in(0,1)\), then at an endpoint
\[
\frac{I-\mathbb E[I\mid\mathcal E_{0,L_n}]}{n^2}
\ \xrightarrow{\ d\ }\ \lambda(1-\lambda)(U-1/2),\qquad U\sim\operatorname{Unif}[0,1].
\]
At any sequence of centers \(a_n\in\{\lfloor(n-L_n)/2\rfloor,\lceil(n-L_n)/2\rceil\}\), the same normalized centered count converges to zero in \(L^2\). The exact centered variance has order \(n^3\) there, compared with order \(n^4\) at an endpoint.

## Assumptions and scope
The model is a uniform permutation, not a Mallows-weighted permutation, and successions require two adjacent positions to contain **consecutive numerical values in increasing order**, not merely an ordinary ascent. Forced successions need not be maximal and are allowed to connect with unforced additional successions. All finite formulas hold for every \(n\ge2\) and every \(S\subseteq\{1,\ldots,n-1\}\), including \(S=\varnothing\) and the complete succession event. The asymptotic assertion assumes one forced run with length fraction tending to a limit strictly between zero and one.

## Proof
**1. Block-order bijection.** Each prescribed position block must be filled by an increasing interval of consecutive values. Choose the left-to-right order of these blocks *on the value axis*; there are exactly \(b!\) possible orders. For a fixed order, start at value \(1\) and assign successive intervals having the corresponding block lengths. These uniquely fill all \(n\) positions and satisfy every prescribed succession. This is a bijection, so the value order is uniformly distributed on \(\mathfrak S_b\) conditional on \(\mathcal E_S\); in particular, \(\mathbb P(\mathcal E_S)=b!/n!\). Inside each block there are no inversions. Whenever the value order reverses two positional blocks, **every** cross-block pair is inverted. This proves the distributional representation and the polynomial.

**2. Orthogonal decomposition.** Let \(Z_{ij}=\mathbf1\{U_i>U_j\}-1/2\), for \(i<j\). The conditional expectations are \(\mathbb E[Z_{ij}\mid U_i]=U_i-1/2\) and \(\mathbb E[Z_{ij}\mid U_j]=-(U_j-1/2)\). Put
\[
R_{ij}=Z_{ij}-(U_i-1/2)+(U_j-1/2).
\]
Each residual is orthogonal to all centered one-variable functions of the independent \(U_i\). Moreover, distinct residuals are uncorrelated: when their pairs are disjoint, this is independence; when they share one index, conditioning on the shared variable gives zero covariance because both residuals have zero conditional mean given it. Also,
\[
\operatorname{Var}(R_{ij})=\frac14-\frac1{12}-\frac1{12}=\frac1{12}.
\]
The coefficient of \(U_i-1/2\) in the weighted sum is
\[
\ell_i\left(\sum_{j>i}\ell_j-\sum_{j<i}\ell_j\right)
=\ell_i\left(n-\ell_i-2\sum_{j<i}\ell_j\right).
\]
Since all linear terms and all residuals are pairwise orthogonal, summing their variances proves the general variance formula; expectation follows from pairwise inversion probability \(1/2\).

**3. One forced run.** Its length vector is \((\underbrace{1,\ldots,1}_{a},L,\underbrace{1,\ldots,1}_{h-a})\). Substitute in the general mean and variance and simplify. This yields the displayed quadratic, symmetry, sharp extrema and variance gap, including boundary cases \(h=0,1\).

**4. Distinct fluctuation regimes.** With the large block first, the \(h\) singleton labels have a uniform relative permutation \(\tau\in\mathfrak S_h\), and independently the large block has a uniformly chosen rank \(R\in\{0,\ldots,h\}\) on the value axis. Consequently
\[
I\mid\mathcal E_{0,L}\ \overset d=\ I(\tau)+LR,
\]
with the two summands independent. A uniform permutation on \(h\) letters has inversion variance \(h(h-1)(2h+5)/72=O(h^3)\); hence its centered fluctuations divided by \(n^2\) vanish in \(L^2\). Since \(R/h\Rightarrow\operatorname{Unif}[0,1]\) and \(Lh/n^2\to\lambda(1-\lambda)\), the endpoint uniform limit follows. For central placement the proved variance formula gives \(\operatorname{Var}(I\mid\mathcal E_{a_n,L_n})=O(n^3)\), proving its \(n^2\)-scale degeneration in \(L^2\).

## Verification
A standalone standard-library Python checker, `verify.py`, enumerates every uniform permutation for orders \(2\) through \(7\), all subsets of potential prescribed successions, and all possible single-run lengths and positions. It compares the full conditional inversion histogram with the predicted weighted-inversion histogram, computes exact rational moments, and checks all variance formulas and extremal identities. Additional block-order enumerations at orders \(8\) and \(9\) provide further exact instances. The verifier reported **505 passing assertions**. These are finite checks; the unrestricted claim rests on the displayed bijection and orthogonality argument.

## Relationship to prior work
The combinatorial phenomenon of *successions* (consecutive numerical values in adjacent positions) has an established enumerative and probabilistic history. Diaconis, Evans, and Graham prove that the entire random set of successions has the same distribution as a certain random set of fixed points. Their section 2 gives the count \((n-|S|)!\) for prescribed successions, which supplies the first counting ingredient above; the present weighted inversion law, positional conditional variance, and macroscopic disparity concern a different statistic. Johnson and Fu derive distributions of increasing consecutive-value sequences by finite Markov chains; those statistics count runs rather than the inversion total under a prescribed run. Burstein studies joint distributions of adjacent **descending** consecutive values with descents, major index, and another Mahonian statistic; the inspected theorems do not give the present location-conditioned Kendall inversion distribution. Rawlings and subsequent Mallows-pattern results treat ordinary *order-isomorphic consecutive patterns*, which allow arbitrary numerical gaps; these should not be conflated with forced numeric-successions. The weighted-inversion decomposition can be regarded as a positional refinement of known block enumeration; earlier inversion-refined succession literature may contain implicit equivalents.

## Limitations
The result is for the **conditional** law given specified increasing-value successions, not for conditioning on the exact set of all successions or on maximal-run events. The limiting distribution is proved at endpoint positions and vanishing at central positions on scale \(n^2\); no central-scale \(n^{3/2}\) limit is claimed. A literature comparison does not prove historical uniqueness. Independent verification of the broader priority literature remains necessary. The experiment counts do not serve as an infinite proof.

## References
Diaconis, P., Evans, S. N., and Graham, R. (2013). *Unseparated pairs and fixed points in random permutations*. Berkeley Statistics Technical Report 822, dated 2013-08-01. https://statistics.berkeley.edu/tech-reports/822 .

Johnson, B. C., and Fu, J. C. (2000). *The distribution of increasing l-sequences in random permutations: a Markov chain approach*. Statistics & Probability Letters 49, 337–344. https://www.academia.edu/33468735/The_distribution_of_increasing_l_sequences_in_random_permutations_a_Markov_chain_approach .

Burstein, A. (2010). *On joint distribution of adjacencies, descents and some Mahonian statistics*. DMTCS Proceedings AN, 601–612. https://dmtcs.episciences.org/en/articles/2846 .

Rawlings, D. (2007). *The q-exponential generating function for permutations by consecutive patterns and inversions*. Journal of Combinatorial Theory, Series A 114, 184–193. https://digitalcommons.calpoly.edu/math_fac/60/ .
