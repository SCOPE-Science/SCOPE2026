# First failure of general-position log-concavity in the triangular graph \(T_{30}\)

## Finding

Let \(T_n=L(K_n)=J(n,2)\) be the triangular graph on the two-element subsets of \([n]\), where intersecting pairs are adjacent, for every integer \(n\ge3\). A vertex subset \(S\) is in *general position* when no geodesic of \(T_n\) contains three members of \(S\). Write \(\Psi_n(z)=\sum_{k\ge0}a_{n,k}z^k\) for its general-position polynomial, including the empty set.

**Theorem (sharp first failure).** The nonzero coefficient sequence of \(\Psi_n(z)\) is log-concave for all \(3\le n\le29\). It fails log-concavity for \(n=30\), because

\[
\begin{aligned}
a_{30,28}&=4575989857607826108600,\\
a_{30,29}&=73770312933671827650,\\
a_{30,30}&=1208883745669600000,\\
a_{30,29}^2-a_{30,28}a_{30,30}&=-89780688879179441682809722027255477500<0.
\end{aligned}
\]

Thus \(30\) is the least triangular-graph order at which the coefficient sequence ceases to be log-concave. This is a *first-failure theorem*, not a claim that log-concavity fails for every larger order.

## Assumptions and scope

All graphs are finite, simple and undirected. The empty set counts as one general-position set. A nonnegative finite sequence without internal zero coefficients is log-concave if \(a_k^2\ge a_{k-1}a_{k+1}\) at each internal index. Here the polynomial degree is \(n\) when \(3\mid n\), and \(n-1\) otherwise; coefficients from degree zero to the degree are strictly positive. All comparisons in the theorem involve integer coefficients and ordinary, rather than dual, general position.

The structural description of the admissible configurations as disjoint unions of stars and triangles is part of previous general-position work; it is reproved below to justify the counting identities and is not claimed as a new classification.

## Proof

**Step 1: Geodesic translation.** A vertex of \(T_n\) represents an edge of \(K_n\). For \(n\ge4\), distinct vertices of \(T_n\) have distance one when their base edges intersect, and distance two otherwise. Therefore three selected vertices violate general position exactly when their base edges form a simple three-edge path (the middle edge intersects the disjoint first and last edges). At \(n=3\) no such base path exists, and \(T_3\) is complete. Thus a selected edge family is in general position if and only if its spanning base graph has no three-edge path as a *subgraph* (not only as an induced subgraph).

**Step 2: Components.** Every connected graph with no three-edge path is a single isolated vertex, an edge, a two-edge star, a triangle, or a star with at least three edges. Indeed, take a spanning tree of a connected component with at least four vertices. It contains no path of three edges, so its diameter is at most two and it is a star. Adding any edge between two leaves would create a three-edge path through a third leaf; no extra edge is permitted. A three-vertex component can additionally be a triangle. Consequently, general-position configurations are precisely sets of edge-disjoint stars and triangles with pairwise vertex-disjoint base supports, together with isolated base vertices.

**Step 3: Exact enumeration.** The exponential generating function for those labelled components, where \(u\) marks base vertices and \(z\) selected edges, is

\[
\sum_{n\ge0}\frac{\Psi_n(z)}{n!}u^n
=\exp\!\left(u e^{zu}-\frac{zu^2}{2}+\frac{z^3u^3}{6}\right).
\]

The subtraction corrects the two presentations of a two-vertex star, and the cubic term adds triangles. Marking the component containing base label one gives an exact recurrence, starting at \(\Psi_0(z)=1\):

\[
\begin{aligned}
\Psi_n(z)={}&\Psi_{n-1}(z)+(n-1)z\Psi_{n-2}(z)\\
&+\binom{n-1}{2}(3z^2+z^3)\Psi_{n-3}(z)\\
&+\sum_{s=4}^{n}s\binom{n-1}{s-1}z^{s-1}\Psi_{n-s}(z),
\end{aligned}
\]

where terms with negative polynomial indices are omitted. The factors count, respectively, an isolated label, a two-vertex edge, one of the three two-edge stars or the triangle on three vertices, and a star whose centre may be any one of \(s\) labels.

For a second, algebraically independent expression, put \(j=n-k\), \(C(u)=ue^u-u^2/2\). Extracting coefficients after substituting \(zu=v\) yields

\[
a_{n,k}=\frac{n!}{j!}\sum_{t=0}^{\lfloor k/3\rfloor}\frac1{6^tt!}
\sum_{h=0}^{\min(j,k-3t)}\frac{(-1)^h\binom jh(j-h)^{k-3t-h}}{2^h(k-3t-h)!},
\]

where \(0^0=1\). Both representations are finite and exact over the rationals or integers, not asymptotic identities.

**Step 4: Exhaustive finite certificate for the sharp cutoff.** Evaluate the displayed integer recurrence for each \(0\le n\le30\), checking \(a_{n,k}>0\) throughout the degree range and every determinant \(a_{n,k}^2-a_{n,k-1}a_{n,k+1}\) at its internal indices for all \(3\le n\le29\). The embedded standalone `verify.py` performs those exact tests using arbitrary-precision integers, and independently calculates *every* coefficient for \(0\le n\le30\) by the separate signed rational coefficient formula, demanding agreement and integrality. Thus no order or coefficient comparison below \(30\) is omitted. At \(n=30\), the last three coefficients displayed in the theorem give the stated strictly negative determinant. The independently computed integer expression equals the negative integer displayed, completing the proof of the *least* failing order. This is an exact finite arithmetic certificate derived from a general identity, not a graph-subset sample.

## Verification

The package contains `verify.py` and `verification_output.txt`, with no third-party dependencies. Run `python3 verify.py` to reproduce the exact coefficient comparisons for every \(3\le n\le30\). A separate direct graph-level test independently enumerates all \(33,864\) subsets of \(V(T_n)\) for \(3\le n\le6\) and directly checks geodesic triples, agreeing with the generated coefficients. These small graph tests corroborate the translation but do not replace the algebraic counting proof. The exact coefficient computation suffices for the bounded first-failure theorem; nothing about all higher orders is inferred from it.

## Relationship to prior work

Ghorbani, Klavžar, Maimani, Momeni, Rahimi Mahid, and Rus (2019) determine maximum general-position cardinalities for line graphs of complete graphs, among other families. Di Stefano, Klavžar, Krishnakumar, Tuite, and Yero (2023, Section 5, Theorem 5.2) explicitly invoke the pre-existing star/triangle decomposition to determine the *minimum size of a maximal* general-position set for the same family. Iršič and collaborators (2024) introduce and study general-position polynomials and questions about coefficient shapes. The present claimed refinement is **only** the exact least order where log-concavity fails in the triangular-graph family, with a complete finite certificate; the structural classification and graph-theoretic scalar values are credited to those sources. Direct searches for synonymous \(J(n,2)\), triangular-graph and line-graph formulations and for other coefficient/tabular formulations did not identify a prior proof of this precise first failure. A negative search is not a novelty proof.

## Limitations

The proof does not classify log-concavity for \(n>30\), and does not determine global unimodality, real-rootedness, or the exact shapes of all coefficients at arbitrarily large orders. The cutoff relies on a fully specified exact finite integer computation (source included), rather than on a short hand calculation for every order. General-position star/triangle structure and its routine exponential-formula enumeration are not independently claimed as original. Equivalent finite enumerations or an unindexed earlier cutoff remain bibliographic risks. Independent external validation has not been performed.

## References

1. M. Ghorbani, S. Klavžar, H. R. Maimani, M. Momeni, F. Rahimi Mahid, and G. Rus, *The general position problem on Kneser graphs and on some graph operations*, arXiv:1903.04286v1 (first released 2019-03-11), https://arxiv.org/abs/1903.04286.
2. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite, and I. G. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965v1 (first released 2023-06-16), especially Section 5, https://arxiv.org/abs/2306.09965.
3. V. Iršič et al., *General position polynomials*, arXiv:2401.05696v1 (first released 2024-01-11), https://arxiv.org/abs/2401.05696.
