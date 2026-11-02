# Conditional young-forest factorization and orthogonal birth-ranked subtree sizes in random recursive trees

## Finding

Let \(T_n\) be the uniform increasing recursive tree with birth labels \(1,\ldots,n\), for any integer \(n\ge2\). Denote by \(S_i\) the number of descendants of vertex \(i\), counting \(i\) itself. Delete all labels at most \(i\), keeping each edge between two remaining vertices. The resulting labeled *young forest* \(\mathcal F_i\) has connected components \(\mathcal C_i\). The conditional probability-generating function is

\[
\mathbb E[z^{S_i-1}\mid\mathcal F_i]
=\prod_{C\in\mathcal C_i}\left(1-\frac1i+\frac{z^{|C|}}i\right).
\]

Consequently, for every \(1\le i<n\),

\[
\mathbb E[S_i\mid S_{i+1},\ldots,S_n]=\frac ni,
\qquad
\operatorname{Cov}(S_i,S_j)=0\quad(i\ne j).
\]

The zero covariance is not independence: in a four-vertex tree, \(\Pr(S_2=3,S_3=2)=1/6\), whereas the product of the two marginal probabilities is \(1/9\). Thus the conditional statement is directional, not exchangeable under reversal of birth ranks.

More generally, for any deterministic real weights \(a_1,\ldots,a_n\), define the birth-weighted root-path total \(A_n(a)\) as the sum, over all vertices, of the weights along its root path, including both endpoints. Then

\[
\mathbb E A_n(a)=n\sum_{i=1}^n\frac{a_i}i,
\qquad
\operatorname{Var} A_n(a)
=n\sum_{i=2}^n\frac{a_i^2(n-i)(i-1)}{i^2(i+1)}.
\]

## Assumptions and scope

For every \(2\le v\le n\), the parent \(P_v\) is chosen independently and uniformly in \(\{1,\ldots,v-1\}\). Each such parent vector gives one labeled recursive tree; all \((n-1)!\) trees have equal probability. The root is label \(1\). A vertex is its own descendant. The *young forest* \(\mathcal F_i\) consists exactly of the parent edges \(v\to P_v\) with both \(v>i\) and \(P_v>i\), retaining all vertices with label greater than \(i\). Each component \(C\) has a unique root with its original parent at most \(i\). The case \(i=n\) has no young vertices and gives \(S_n=1\); \(i=1\) gives \(S_1=n\). Conditional variables mentioned below are understood on events of positive probability.

A \(\operatorname{BetaBinomial}(N;\alpha,\beta)\) variable is the number of successes in \(N\) Bernoulli trials conditionally on a beta-distributed success probability with parameters \(\alpha,\beta\), or equivalently the red increment in a two-color Pólya urn initially containing \(\alpha\) red and \(\beta\) black balls. We use this distribution for \(i\ge2\), where both parameters are positive.

## Proof

**Independent attachment reconstruction.** Fix \(i\) and condition on the *entire labeled* young forest \(\mathcal F_i\). For a vertex \(r>i\) that is a component root, the forest specifies the event \(P_r\le i\). Given that event, \(P_r\) is uniform on \(\{1,\ldots,i\}\). These conditional parent variables are mutually independent because the original parent choices are independent and the forest restriction factorizes across vertices. Internal parent edges of non-root vertices are fixed by \(\mathcal F_i\).

A young component lies in the subtree of \(i\) if and only if its root attaches directly to \(i\): no other older vertex can lie below \(i\), since birth labels increase strictly along every downward path. The indicator that component \(C\) attaches to \(i\) is therefore an independent \(\operatorname{Bernoulli}(1/i)\) conditional on \(\mathcal F_i\). Summing the component sizes proves the asserted conditional sum representation and generating function, including the deterministic boundary \(i=1\) and the empty-forest case \(i=n\).

**Directional mean independence.** The young components partition exactly \(n-i\) labels. Taking conditional expectations yields

\[
\mathbb E[S_i\mid\mathcal F_i]
=1+\frac1i\sum_{C\in\mathcal C_i}|C|
=\frac ni.
\]

For \(j>i\), every descendant of vertex \(j\) has a greater label; therefore \(S_j\) is determined completely by \(\mathcal F_i\). The tower property gives \(\mathbb E[S_i\mid S_{i+1},\ldots,S_n]=n/i\). For any integrable observable \(g\) of the later subtree-size vector with an integrable product, \(\mathbb E[S_i g]=(n/i)\mathbb E[g]\). Taking \(g=S_j\) gives zero covariance for all \(i<j\), and hence for all unequal indices.

**Marginal distribution and variance.** At birth time \(i\), the descendants of \(i\) number one, and the other existing vertices number \(i-1\). At each later birth, the new vertex falls inside the subtree of \(i\) with probability equal to the current subtree size divided by the current total vertex count. Thus \(S_i-1\) follows the two-color Pólya urn with \(n-i\) draws, initial counts \(1\) and \(i-1\). The standard beta-binomial moments, which also follow directly by conditioning on \(U\sim\operatorname{Beta}(1,i-1)\), yield

\[
\mathbb E S_i=\frac ni,
\qquad
\operatorname{Var}S_i=\frac{n(n-i)(i-1)}{i^2(i+1)}\qquad(2\le i\le n).
\]

Since \(S_1=n\) deterministically, its variance is zero as well.

**Weighted paths and nonindependence.** Double counting pairs \((i,v)\) in which \(i\) is an ancestor of \(v\) gives \(A_n(a)=\sum_i a_i S_i\). Linear expectation and the just-proved diagonal covariance matrix give both stated moment formulas for all real deterministic weights, without any independence assumption. For \(n=4\), the event \(S_2=3,S_3=2\) occurs precisely when \(P_3=2\) and \(P_4=3\), of probability \(1/2\cdot1/3=1/6\). The Pólya marginals give \(\Pr(S_2=3)=\Pr(S_3=2)=1/3\), proving dependence despite zero covariance.

## Verification

The accompanying `verify.py` is standalone Python 3 code requiring only the standard library. It enumerates every parent vector for \(2\le n\le8\) (5,913 trees), reconstructs every young-forest stratum and verifies the full conditional generating-function coefficients using exact rational arithmetic, not merely the mean. It independently checks all pairwise mixed moments, beta-binomial variances, several weighted sums, and the four-vertex dependence witness. The extracted verifier reports **9,326 exact assertions passed**. This finite replay is a consistency check; the preceding component-attachment and Pólya arguments establish the result for every \(n\ge2\).

## Relationship to prior work

Holmgren and Janson (2014; first public arXiv version 2014-06-26, primary MSC 60C05) study global counts of fringe subtrees of specified sizes or types and their joint asymptotic laws. Their full available text treats those aggregated counts, rather than the birth-indexed conditional young-forest factorization proved here. Grübel and Michailow (2014) develop boundary and subtree-mass representations, but use Harris-tree coordinates and path-length functionals rather than the explicit finite birth-ranked conditional product law.

Dobrow and Fill (1999) analyze classical total path length, its moments and limiting distribution. They explicitly use the subtree rooted at label \(2\) for a decomposition. The well-known unweighted path-length variance is therefore not presented as a new contribution. Fuchs (2008) studies the global number of fringe subtrees of each size, again a different statistic. The new claim concerns the finer labeled young-forest conditioning, all later birth-ranked subtree sizes jointly, and the diagonal variance form for *arbitrary* deterministic birth weights. A prior equivalent conditional statement implicit in general recursive-tree or reinforced-urn theory is an unresolved historical-priority risk.

## Limitations

The conditional independence is among the Bernoulli *component attachment indicators after fixing the younger forest*, not among the subtree sizes themselves. The ancestor weights must be deterministic (or fixed independently of the tree); weights that depend on the sampled tree need not satisfy the diagonal covariance formula. The conclusion is specific to uniform independent-parent recursive trees; preferential-attachment and other growing-tree models require new arguments. No claim of independent certification or exhaustive historical novelty is made.

## References

1. C. Holmgren and S. Janson, *Limit Laws for Functions of Fringe Trees for Binary Search Trees and Recursive Trees*, arXiv:1406.6883, first submitted 2014-06-26, https://arxiv.org/abs/1406.6883 .
2. R. Grübel and I. Michailow, *Random Recursive Trees: A Boundary Theory Approach*, arXiv:1406.7614, first submitted 2014-06-30, https://arxiv.org/abs/1406.7614 .
3. R. P. Dobrow and J. A. Fill, *Total Path Length for Random Recursive Trees*, Combinatorics, Probability and Computing 8 (1999), 317–333, https://doi.org/10.1017/S0963548399003855 .
4. M. Fuchs, *Subtree Sizes in Recursive Trees and Binary Search Trees: Berry–Esseen Bounds and Poisson Approximations*, Combinatorics, Probability and Computing 17 (2008), https://doi.org/10.1017/S0963548308009243 .
