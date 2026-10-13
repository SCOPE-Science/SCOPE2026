# Exact nestedness–modularity Pareto frontier in connected two-by-\(n\) ecological networks
## Finding
Fix integers \(n\ge2\) and \(1\le c<n\). Consider a binary interaction network with two species in one guild and \(n\) species in the other, no isolated species, and exactly
\[
E=n+c
\]
interactions. The network is automatically connected because a degree-two column joins the two row species.

Let \(\mathcal N\) be classical NODF divided by \(100\), including the standard zero contribution for pairs with equal degree, and let \(Q^\star\) be Barber bipartite modularity maximized over **all partitions** of the complete \(n+2\)-vertex network.

Every column is of type \((1,0)\), \((0,1)\), or \((1,1)\). There are exactly \(c\) shared columns, and the number of exclusive columns is
\[
s=n-c.
\]
Write \(a\) and \(b\) for the exclusive counts of the two rows, so \(a+b=s\), and set
\[
x=\max(a,b),\qquad \left\lceil\frac{s}{2}\right\rceil\le x\le s.
\]
For every such integer \(x\) there is exactly one interaction-network isomorphism class, up to row/column permutations.

The **complete attainable joint-score locus** is
\[
\boxed{\mathcal N_x=\frac{cs+\mathbf 1_{\{2x>s\}}\,c/(n-x)}{1+\binom n2}},
\qquad
\boxed{Q_x^\star=\frac{2x(n-x)}{(n+c)^2}}.
\]
Here the indicator vanishes for exactly equal row degrees.

The complete Pareto frontier, for making both scores as large as possible, consists of exactly the isomorphism classes indexed by
\[
\boxed{x_0\le x\le s,\qquad x_0=\min\!\left(s,\left\lceil\frac n2\right\rceil\right)}
\]
with integer \(x\).

The unique nestedness maximizer is the Ferrers network \(x=s\), in which one row meets all \(n\) columns and the other row meets the \(c\) shared columns. This class **simultaneously maximizes Barber modularity exactly when**
\[
\boxed{c\ge s-1\quad\Longleftrightarrow\quad 2c\ge n-1.}
\]
Below this density threshold a genuine tradeoff is unavoidable; at and above it the Pareto frontier contains just the Ferrers class.

For example, at \(n=6,c=1\) (seven links), all three Pareto classes and their exact scores are
\[
\begin{array}{c|cc}
x & \mathcal N_x & Q_x^\star\\\hline
3&1/3&18/49\\
4&11/32&16/49\\
5&3/8&10/49
\end{array}.
\]
Increasing nestedness along this frontier decreases the best possible modularity.

## Assumptions and scope
The two guilds have sizes \(2\) and \(n\) with \(n\ge2\), and the incidence matrix is binary and simple. Every species has at least one partner. The number of links is \(E=n+c\), where \(1\le c<n\). The shared-column condition \(c\ge1\) forces graph connectivity.

The NODF convention is the unweighted classical version: each unordered pair of rows and each unordered pair of columns contributes one term; a pair of unequal degrees contributes the overlap divided by the smaller degree, whereas equal degrees contribute zero, and the sum is divided by \(K=1+\binom n2\). The usual percentage score is \(100\mathcal N\).

Barber modularity is
\[
Q(g)=\frac1E\sum_{i=1}^{2}\sum_{j=1}^{n}
\left(A_{ij}-\frac{k_i d_j}{E}\right)
\mathbf1_{\{g_i=g_{j+2}\}},
\]
where \(k_i\) is row degree, \(d_j\) is column degree, and community labels \(g\) may form **any** partition of the \(n+2\) vertices. Write \(Q^\star=\max_g Q(g)\).

Two networks are compared by the two scores \((\mathcal N,Q^\star)\). A score pair is Pareto dominated when another network has at least as large a value of both scores and a strict gain in at least one. Network isomorphism respects the two guilds.

## Proof
**Column types and isomorphism.** Since every column is nonzero and there are only two rows, its degree is one or two. If there are \(c'\) degree-two columns, the edge count is \(n+c'\), so \(c'=c\). Every other column is exclusive to exactly one row, with counts \((a,b)\) satisfying \(a+b=s\). Thus its isomorphism class is determined by \(x=\max(a,b)\), and every integer \(x\) in the specified range occurs.

**Exact NODF.** The row degrees are \(a+c\) and \(b+c\). If \(a\ne b\), their overlap is the set of \(c\) shared columns and the row-pair contribution is \(c/[c+\min(a,b)]=c/(n-x)\). If \(a=b\), the standard unequal-degree convention sets that contribution to zero. Among column pairs, only a degree-two column paired with a degree-one column contributes: there are \(cs\) such unordered pairs and each has overlap-to-smaller-degree ratio one. All remaining column pairs have equal degrees and contribute zero. Division by \(K=1+\binom n2\) proves \(\mathcal N_x\).

**Exact global Barber modularity.** Put \(k_1=a+c\), \(k_2=b+c\); then \(k_1+k_2=E\). For any one column, the two possible row contributions to \(E^2Q\) are
\[
E A_{1j}-k_1d_j,
\qquad
E A_{2j}-k_2d_j.
\]
If both rows belong to the same community, these two entries sum to \(E d_j-(k_1+k_2)d_j=0\) for each column, so the complete modularity is zero. If the rows lie in different communities, any column can be assigned to either row community or to a separate community, and its best contribution is the maximum of its two displayed entries and zero. These independent best choices are simultaneously realizable in one partition, so this method optimizes over **all partitions**, not merely a preselected two-module family.

For an \((1,0)\) column the best contribution to \(E^2Q\) is \(k_2\); for \((0,1)\) it is \(k_1\); for \((1,1)\) it is \(|k_1-k_2|\). Therefore
\[
E^2 Q^\star
=a k_2+b k_1+c|k_1-k_2|
=2ab+2c\max(a,b).
\]
Taking \(x=\max(a,b)\), using \(ab=x(s-x)\), and observing that \(s-x+c=n-x\), we get
\[
Q_x^\star=\frac{2x(n-x)}{(n+c)^2}.
\]
This is nonnegative and achieved by the partition described above, so the zero-modularity same-row case never improves the maximum.

**Pareto classification.** On the index range \(\lceil s/2\rceil\le x\le s\), the NODF score is strictly increasing with \(x\): when \(s\) is even, the first step jumps from zero row-pair credit to positive credit; otherwise the reciprocal \(c/(n-x)\) strictly increases. Hence a class is dominated precisely if some larger \(x\) has at least its modularity. The modularity numerator \(x(n-x)\) strictly increases up to the quadratic peak at \(n/2\) and strictly decreases thereafter, with equality only for the symmetric pair about \(n/2\). Every class below \(\lceil n/2\rceil\), if any, is dominated by a later class with at least its modularity. Every class \(x\ge\lceil n/2\rceil\) is nondominated because all later classes have strictly less modularity. Intersecting with the feasible range produces
\[
x_0=\min(s,\lceil n/2\rceil),
\]
and the stated frontier.

Finally \(x=s\) uniquely maximizes NODF, while it maximizes \(x(n-x)\) on the feasible integer interval if and only if the immediately preceding feasible class \(x=s-1\) has no larger quadratic value. For \(s\ge2\),
\[
s(n-s)-(s-1)(n-s+1)=n-2s+1=2c-n+1.
\]
This is nonnegative exactly for \(2c\ge n-1\). For \(s=1\), the Ferrers class is the only class and the same condition holds automatically. The theorem follows.

## Verification
An accompanying standalone Python program, `verify_nested_modularity_pareto.py`, recomputes NODF directly from row and column neighbor overlaps and maximizes Barber modularity independently in two ways: by checking every possible two-row-label assignment of the columns, and for \(n\le5\), by enumerating **every set partition** of all vertices. All comparisons use `fractions.Fraction`, hence exact rational arithmetic.

For all \(2\le n\le8\), \(1\le c<n\), it checked 9,322 labeled admissible matrices, 1,927,648 column-label assignments, and 198,158 evaluations across all vertex set partitions, plus all Pareto dominance relations and the common-maximizer threshold. Every assertion passed and the first line of output was `VERIFY_OK`.

Run `python3 verify_nested_modularity_pareto.py` with Python 3 and its standard library. The finite test checks the formulas and examples but is not a proof of their unbounded quantifiers: the preceding column-type, community-partition, and quadratic arguments supply that proof.

## Relationship to prior work
Almeida-Neto and coauthors (2008) introduced NODF with precisely the strict degree ordering and paired-overlap normalization used here. Barber (2007, preprint 11 July 2007) formulated bipartite modularity over arbitrary vertex-community partitions. This theorem combines those established indices without changing their definitions.

Fortuna and coauthors (2010) examined empirical relationships between nestedness and modularity as network connectance changes. Their empirical correlations use distinct normalizations and a different modularity computation; a correlation trend does not determine a fixed-\((2,n,E)\) joint-score Pareto frontier or a common-maximizer condition. Flores and coauthors (2016) provide implementations of NODF and Barber modularity, while Hoeppke and Simmons (2021) investigate attainable NODF maxima at specified network dimensions and link counts. The latter focuses on one index and heuristic numerical optimization, not exact global two-index compatibility.

The contribution here is the full exact achievable locus and the complete closed-form Pareto/classification threshold under connected fixed-link two-row constraints. It does not claim that the indices or empirical tensions between them are new.

## Limitations
The theorem requires exactly two species in one guild, strictly positive degree for every vertex, binary interactions, and \(1\le c<n\). It does not generalize automatically to three-row networks, link weights, structural prohibitions, different NODF variants, degree-preserving null-model corrections, or other modularity null models.

Barber modularity is optimized globally over unrestricted vertex partitions. A prescribed two-community assignment or additional ecological module constraints may change its attainable value.

The connectivity and link-density transition is an exact finite structural result, not a prediction that nestedness and modularity correlations in empirical ecological ensembles switch sign at the same threshold. Published broader network-optimization results outside the inspected sources could still subsume the specific two-row formulas.

## References
1. M. J. Barber, “Modularity and community detection in bipartite networks,” arXiv:0707.1616 (initial public version 11 July 2007); *Physical Review E* 76, 066102 (2007), doi:10.1103/PhysRevE.76.066102.
2. M. Almeida-Neto, P. Guimarães, P. R. Guimarães Jr., R. D. Loyola and W. Ulrich, “A consistent metric for nestedness analysis in ecological systems: reconciling concept and measurement,” *Oikos* 117, 1227–1239 (2008), doi:10.1111/j.2008.0030-1299.16644.x.
3. M. A. Fortuna et al., “Nestedness versus modularity in ecological networks: two sides of the same coin?”, *Journal of Animal Ecology* (2010), doi:10.1111/j.1365-2656.2010.01688.x.
4. C. O. Flores et al., “BiMat: a MATLAB package to facilitate the analysis of bipartite networks,” *Methods in Ecology and Evolution* (2016), doi:10.1111/2041-210X.12458.
5. D. Hoeppke and B. I. Simmons, “maxnodf: An R package for fair and fast comparisons of nestedness between networks,” *Methods in Ecology and Evolution* (2021), doi:10.1111/2041-210X.13545.
6. P. Payrató-Borràs et al., “Breaking the Spell of Nestedness: The Entropic Origin of Nestedness in Mutualistic Systems,” *Physical Review X* 9, 031024 (2019), doi:10.1103/PhysRevX.9.031024.
