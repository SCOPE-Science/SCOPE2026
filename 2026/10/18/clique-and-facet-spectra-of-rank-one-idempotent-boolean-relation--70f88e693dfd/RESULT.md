# Degree distribution and component diameter of commuting rank-one Boolean idempotents

## Finding

Let \(n\ge2\). In the simple commuting graph on nonzero rank-one Boolean idempotents, a vertex is a nonempty rectangle \(E_{U,V}=U\times V\) with \(U\cap V\ne\varnothing\). Write \(s=n-|U\cup V|\) for its number of unused coordinates and \(u=|U\triangle V|\) for its number of unilateral coordinates. Its degree is
\[
d(E_{U,V})=2^u(4^s-3^s).
\]
In particular the complete vertex degree enumerator, counting vertices with multiplicity, is
\[
D_n(z)=\sum_{s=0}^{n-1}\sum_{u=0}^{n-s-1}
  \binom ns\binom{n-s}{u}2^u z^{2^u(4^s-3^s)}.
\]
Vertices with \(s=0\) are isolated. All other vertices form one component, of diameter \(1\) for \(n=2\) and exactly \(3\) for \(n\ge3\). Thus the coordinate pattern determines local commutation counts, while the unused coordinates locate every nonisolated vertex within one edge of the diagonal singleton clique.

## Assumptions and scope

Supports are subsets of a common labeled set \([n]\). Multiplication is Boolean matrix multiplication, or equivalently relational composition. Rank one means that the Boolean matrix is a nonzero outer product. Only idempotents are vertices; zero, square-zero rectangles, and all higher-rank matrices are excluded. Edges are between distinct vertices. The diameter is measured within the nonisolated component, using only vertices of that induced graph.

## Proof

The nonempty rectangle representation is unique. The product \(E_{U,V}E_{A,B}\) is \(E_{U,B}\) if \(V\cap A\ne\varnothing\), and zero otherwise. In particular \(E_{U,V}\) is idempotent exactly when \(U\cap V\ne\varnothing\). If two commuting rectangles have both products nonzero, equality of their supports forces the rectangles themselves to coincide. Exactly one nonzero product cannot commute. Thus two distinct vertices are adjacent precisely when both cross-intersections vanish.

**Degrees.** A neighbor of \(E_{U,V}\) has \(A\subseteq V^c\), \(B\subseteq U^c\) and \(A\cap B\ne\varnothing\). A coordinate in \(U\cap V\) is barred from both \(A\) and \(B\); one in \(U\triangle V\) can belong to only one of them, giving two choices. At each unused coordinate there are four local choices. The intersection \(A\cap B\) can occur only among those unused coordinates, so subtract the \(3^s\) patterns on them with no simultaneous inclusion. This proves the degree formula. In the enumerator, choose the unused and unilateral coordinate sets, and assign one of two unilateral types to each unilateral coordinate. Every remaining coordinate belongs to both \(U\) and \(V\), with at least one such coordinate required. If terms share the same degree their coefficients add. The degree-zero coefficient is \(3^n-2^n\); the total vertex count is the known \(4^n-3^n\).

**The nonisolated component.** Every vertex with an unused coordinate \(t\) is adjacent to \(E_{\{t\},\{t\}}\). All diagonal singleton vertices are mutually adjacent. Thus all nonisolated vertices lie in one component, with distances at most three. At \(n=2\) only the two diagonal singletons have unused coordinates, so that component is an edge. For \(n\ge3\), the idempotents with both supports equal to \([n]\setminus\{1\}\) and \([n]\setminus\{2\}\) are distinct nonadjacent vertices of degree one, with different diagonal singleton neighbors. Their distance is three, giving sharpness.

## Relationship to prior work

The vertex total is classical (OEIS A363232, rank-one column). The [separate clique and maximal-clique enumerators](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-clique-and-maximal-clique-enumerators-for-rank-one-idempotent-bo--a2f16599b2ee/RESULT.md) for the exact same graph already specify the number of edges and the number of isolates as special coefficients. Those counts and the equivalent cross-annihilation criterion are background here, not novelty claims. The degree enumerator gives the distribution of adjacency over individual vertices, which the global edge, isolate and clique-size counts do not supply.

Paulista ([arXiv:2510.23871](https://arxiv.org/abs/2510.23871), §§2.2, 4) gives connectivity and diameter methods for commuting graphs of completely \(0\)-simple semigroups. For trivial group and the nonempty-subset intersection sandwich matrix, the nonzero elements are all nonempty rectangles, not just the idempotents. The distinction affects distances: on three coordinates, the idempotents \(E_{\{3\},\{2,3\}}\) and \(E_{\{1,3\},\{3\}}\) have disjoint unused sets and are nonadjacent. A common idempotent neighbor would require a coordinate unused by both, so they are at distance three in the idempotent graph. The square-zero rectangle \(\{1\}\times\{2\}\) gives a two-edge path in the full nonzero-rectangle graph. Likewise, full Boolean relation centralizer sizes count commuting partners of all ranks, not degrees in the induced idempotent graph. Full matrix-semiring diameter results (Dolžan, Kokol Bukovšek and Oblak, [arXiv:1012.5505](https://arxiv.org/abs/1012.5505)) use a different vertex set as well.

## Verification and limitations

The uniform proofs establish the formulas for all \(n\ge2\). The accompanying standard-library checker `artifacts/verify.py` constructs small Boolean commuting graphs, checks degrees and their full frequency distribution at \(2\le n\le5\), and checks the diameter of their nonisolated components. It retains supplementary checks of clique coefficients. These finite checks are corroboration only. The result concerns the idempotent stratum; neither statistics for wider strata nor historical priority is inferred from the computation. Alternate formulations of the induced-graph degree distribution or metric may exist in the semigroup literature.
