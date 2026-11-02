# Exact recovery-time order and balance criterion for generalized theta graphic matroids

## Finding

For every integer \(r\ge3\) and every tuple of path lengths \(\ell_1,\ldots,\ell_r\ge2\), define the two-terminal generalized theta graph \(\Theta(\ell_1,\ldots,\ell_r)\). Its \(r\) internally vertex-disjoint terminal-to-terminal paths have lengths \(\ell_i\), and it has \(N=\sum_i\ell_i\) edges. Draw edges independently and uniformly **with replacement**. For an edge \(e\), let \(\tau_e\) be the first number of draws after which the endpoints of \(e\) lie in the same component of the sampled-edge subgraph. Equivalently, \(e\) has entered the closure of the sampled set in the graphic matroid.

For every edge in path \(i\), the expectation is the same value

\[
E_i=N\left(1-\frac1{\ell_i}+\sum_{S\subseteq[r]\setminus\{i\}}\frac{(-1)^{|S|}}{\ell_i+\sum_{j\in S}\ell_j}\right).
\]

Furthermore, for any two paths \(i,j\), the strict order \(E_i<E_j\) is **equivalent** to \(\ell_i<\ell_j\). Therefore the associated graphic matroid is recovery balanced precisely when **all path lengths agree**. For \(r\) equal paths of length \(\ell\), the common expectation is \(r\ell-r+1\), exactly its matroid rank.

This is a complete all-parameter recovery-time profile, not just an algorithm for evaluating individual finite instances. In the three-path case, writing the lengths \(a,b,c\) with \(N=a+b+c\), the expectation for an edge on the path of length \(a\) simplifies to \(N+1-N/(a+b)-N/(a+c)\).

## Assumptions and scope

All graphs are finite, undirected, unweighted and simple. The two common terminals are distinct, no internal vertices are shared, and every path length is at least two. Thus no parallel graph edges arise. A sample is a single edge chosen uniformly from the entire labelled edge set, independently of all previous samples; repetitions count toward the draw number. Recovery means **graphic-matroid closure**, not full reconstruction of a spanning tree or a codeword. In particular, an edge is recovered immediately if it is sampled itself. The endpoints-connectivity criterion is the usual description of closure in a graphic matroid. All mathematical statements concern every allowed tuple, without asymptotic qualifications.

The graph is connected, with \(N-r+2\) vertices and graphic-matroid rank \(N-r+1\). The restriction \(r\ge3\) is necessary for strict comparison; for two paths, their union is a single cycle, irrespective of its subdivision into paths.

## Proof

**1. Characterize recovery without sampling the target edge.** Fix an edge \(e\) on path \(i\). Deleting \(e\) splits its own path into two segments, each attached to one terminal. Any alternate simple route between the endpoints of \(e\) must use **all the other \(\ell_i-1\) edges of path \(i\)** and also **all edges of at least one other terminal-to-terminal path**. Conversely those two conditions provide such an alternate route. This characterization follows directly because the interiors of the other paths have no external attachments.

**2. Convert discrete draws to independent edge appearances.** Embed the draws as independent marks on a rate-one Poisson process, each mark uniformly assigned to one of the \(N\) edges. Then each edge is present by time \(t\) independently with probability \(x=1-e^{-t/N}\). Let \(T_e\) be the continuous time of first recovery. Since the original discrete stopping count \(\tau_e\) is integrable (it is bounded by the full coupon-collector stopping count), the compensated unit-rate Poisson process gives \(\mathbb E\tau_e=\mathbb E T_e\). This can also be checked by conditioning on the sequence of marks: the expected sum of \(\tau_e\) independent mean-one exponential interarrival times equals \(\mathbb E\tau_e\).

The probability that \(e\) is not yet recovered is exactly

\[
\Pr(T_e>t)=(1-x)\left[1-x^{\ell_i-1}\left(1-\prod_{j\ne i}(1-x^{\ell_j})\right)\right].
\]

Indeed, the initial factor means that \(e\) has not appeared. Conditional on this, an alternate route exists precisely when the remaining edges in path \(i\) have all appeared and at least one other whole path has appeared; path-edge appearances are independent. Taking the survival integral, with \(dt=N\,dx/(1-x)\), yields

\[
E_i=N\int_0^1\left[1-x^{\ell_i-1}\left(1-\prod_{j\ne i}(1-x^{\ell_j})\right)\right]dx.
\]

Expanding the finite product and integrating monomials gives exactly the rational sum in the finding.

**3. Prove strict length ordering.** For distinct path indices \(i,j\), put

\[
Q_{ij}(x)=\prod_{k\notin\{i,j\}}(1-x^{\ell_k}).
\]

Subtracting the two preceding integrals and canceling the cross terms gives the exact identity

\[
E_j-E_i=N\int_0^1
\left(x^{\ell_i-1}-x^{\ell_j-1}\right)
\left(1-Q_{ij}(x)\right)\,dx.
\]

Since \(r\ge3\), the second factor is strictly positive for \(0<x<1\). The first factor is strictly positive, identically zero, or strictly negative according as \(\ell_i<\ell_j\), \(\ell_i=\ell_j\), or \(\ell_i>\ell_j\). Thus the expectation comparison has exactly the same sign as the path-length comparison. Every edge on a given path has the same survival probability and therefore the same expectation. Equal expectations across the entire edge set occur exactly when all lengths match.

**4. Evaluate the balanced case.** When \(\ell_i=\ell\) for every \(i\), the integral becomes

\[
E_i=N\left(1-\frac1\ell+\int_0^1x^{\ell-1}(1-x^{\ell})^{r-1}\,dx\right)
=N\left(1-\frac1\ell+\frac1{r\ell}\right)
=r\ell-r+1.
\]

The substitution \(u=x^\ell\) evaluates the displayed integral to \(1/(r\ell)\). This equals the rank \(N-r+1\), in agreement with the general mean-rank identity for recovery-balanced matroids.

**5. Sharp boundary.** For \(r=2\), the product \(Q_{ij}\) is empty and equals one, so the pairwise difference vanishes regardless of the individual path lengths. This is the cycle case and shows why \(r\ge3\) cannot be dropped from the strict criterion.

## Verification

The self-contained script `verify_theta_recovery.py` constructs each graph directly, and, for every target edge, enumerates all subsets of *other* edges. It tests endpoint connectivity using graph traversal, evaluates an independent exact rational formula by subset size, and compares with the proposed integral expansion. It also verifies that the sum of all edge expectations equals \(N(N-r+1)\), and checks every strict comparison against path lengths. The rational calculations use the standard-library `Fraction` class. Nine families were tested, including equal and unequal paths and instances with three through five paths; the checker reports `VERIFY_OK`.

These finite tests are corroboration only; the universal proof above is the argument for every allowed size.

## Relationship to prior work

The random-access balance invariant for linear codes was introduced by Gruica, Bar-Lev, Ravagnani and Yaakobi in 2024. Bar-Lev, López, Matthews and Salizzoni's October 2026 work provides a general matroid formula for coordinatewise recovery expectations and proves duality of recovery balance. The present theorem **specializes to a structured but unbounded graphic-matroid family** and derives a complete strict comparison and if-and-only-if balance classification by graph connectivity and Poissonization. The general coefficient formula can be used to calculate any one finite instance, but it does not state or evaluate the closed theta-family profile and strict order. Chen, Jin and Ma's contemporaneous combinatorial work concerns a different invariant, the multiplicative Merino–Welsh inequality, and emphasizes matroid series and parallel classes; it supplies structural context, not a previous recovery theorem.

The theta-configuration homology, directed edge polytope, and graph spectral results found in the mathematical-record comparison concern distinct invariants and do not imply the recovery-time order. The priority judgment remains qualified by the possibility of an equivalent result using other terminology.

## Limitations

This theorem treats uniform independent sampling with replacement and graphic matroids of generalized theta graphs having at least three parallel terminal paths of length at least two. It does not claim an analogous order for arbitrary series-parallel graphs, sampling with nonuniform edge weights, distributions of complete stopping times, or more general code families. It does not independently establish historical priority or external verification. The general formula used for context is prior work, not a newly claimed invention.

## References

1. J. Chen, X. Jin and T. Ma, *On minimum-size matroid counterexamples to the multiplicative Merino–Welsh inequality*, arXiv:2610.27706v1 (first public 2026-10-20), https://arxiv.org/html/2610.27706v1.
2. D. Bar-Lev, H. H. López, G. L. Matthews and F. Salizzoni, *A Matroidal Framework for Random Access in Linear Codes*, arXiv:2610.28820v1 (first public 2026-10-20), https://arxiv.org/html/2610.28820v1.
3. A. Gruica, D. Bar-Lev, A. Ravagnani and E. Yaakobi, *A Combinatorial Perspective on Random Access Efficiency for DNA Storage*, arXiv:2401.15722 (first public 2024-01-28), https://arxiv.org/abs/2401.15722.
