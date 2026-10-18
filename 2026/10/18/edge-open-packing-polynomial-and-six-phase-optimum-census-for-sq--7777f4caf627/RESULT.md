# Edge-open-packing polynomial and six-phase optimum census for squared paths

## Finding

Let \(G_n=P_n^2\) be the square of the path on ordered vertices \(1,\ldots,n\), meaning that two distinct vertices are adjacent exactly when their indices differ by at most two. Let an *edge-open-packing* (EOP) be a subset \(B\subseteq E(G_n)\) for which no two different selected edges admit a third graph edge joining an endpoint of one to an endpoint of the other. Define its complete size enumerator by
\[
E_n(z)=\sum_{B\text{ EOP in }G_n}z^{|B|}.
\]
For the empty path take \(E_0(z)=1\). Set
\[
T(x,z)=z(x^2+x^3)+z^2(2x^4+x^5).
\]
Then the following identity of formal power series determines **every** EOP coefficient for **every** integer \(n\ge0\):
\[
\boxed{\sum_{n\ge0} E_n(z)x^n
=\frac1{1-x}+\frac{T(x,z)}{(1-x)(1-x-x^2T(x,z))}.}
\]
Equivalently, each EOP has a **unique** left-to-right decomposition into isolated selected edges and selected two-edge stars, with at least two unused vertices between the endpoint spans of successive components. Isolated edges have spans of two or three vertices (one pattern each); two-edge stars have spans of four or five vertices (two and one patterns, respectively).

For \(n\ge1\), write \(n=6k+r\), \(0\le r\le5\). The maximum possible selected-edge cardinality is
\[
\boxed{\rho_e^o(G_n)=2k+\begin{cases}
0,&r\in\{0,1\},\\
1,&r\in\{2,3\},\\
2,&r\in\{4,5\}.
\end{cases}}
\]
The **exact number** \(M_n=[z^{\rho_e^o(G_n)}]E_n(z)\) of maximum EOPs is \(M_1,M_2,M_3,M_4,M_5=(1,1,3,2,5)\); for every \(k\ge1\),
\[
\boxed{M_{6k+r}=\begin{cases}
2^{k-3}(11k^2+17k+8),&r=0,\\
2^{k-4}(15k^3+47k^2+50k+16),&r=1,\\
(k+1)2^k,&r=2,\\
3(k+1)(k+2)2^{k-1},&r=3,\\
2^{k+1},&r=4,\\
(3k+5)2^k,&r=5.
\end{cases}}
\]
The powers with negative exponents in the first two branches when \(k=1\) are rational factors multiplying integers and yield the stated integral counts.

More explicitly, for every \(n\ge0\) and \(k\ge1\), let \(a_{n,k}=[z^k]E_n(z)\). If \(t=s+d\), where \(s,d\ge0\) and \(s+2d=k\), and if
\[
L=n-2s-j-4d-h-2(t-1),
\]
then
\[
\boxed{a_{n,k}=\sum_{\substack{s,d\ge0\\s+2d=k}}\binom{s+d}{d}
\sum_{j=0}^{s}\sum_{h=0}^{d}\binom{s}{j}\binom{d}{h}2^{d-h}
\binom{L+t}{t},}
\]
where each summand is zero when \(L<0\), and \(a_{n,0}=1\). This is a finite, parameter-explicit enumeration of every feasible cardinality.

## Assumptions and scope

All graphs are finite, simple and undirected. The path \(P_n\) uses the fixed ordered vertex labels \(1,\ldots,n\), and its square uses graph-distance at most two in that path, rather than the Cartesian product or the square of an adjacency matrix. EOP is the standard common-third-edge condition, **not** ordinary edge matching or vertex open packing. The family is indexed by every integer \(n\ge1\); the empty path is introduced solely for the formal generating function. Counts are of **labeled edge subsets** in the fixed path, not isomorphism classes. The maximum number and maximum-set count above are consequences of the full enumerator, not separate assumptions.

## Proof

**1. Structural restriction.** For any EOP \(B\), each component of the graph on endpoints of its selected edges is a star. If three selected edges formed a path, its middle edge would be a forbidden third edge for the first and third. A triangle also excludes any two selected triangle edges, because the third triangle edge connects their endpoints. If three selected edges shared one center, two of their leaves would be adjacent in \(P_n^2\): four possible neighbor indices are offsets \(-2,-1,1,2\), and an independent subset of these offsets has size at most two. Thus selected components have one edge or two edges sharing one center.

For a singleton edge, its endpoints are distance one or two in path-index order, hence its endpoint span has width two or three, one pattern of each width at a specified left endpoint. For a two-edge star its leaves must be nonadjacent, so their indices differ by at least three. Necessarily they lie on opposite sides of the center and yield the offset pairs \((-2,1)\), \((-1,2)\), or \((-2,2)\). These create respectively two width-four patterns and one width-five pattern.

Any distinct selected components have disjoint endpoint spans separated by at least two unused vertices: if the rightmost endpoint of the left component and the leftmost endpoint of the right component were at index distance one or two, they would be joined by a forbidden third edge. Interleaving spans is also impossible, as every index in a component's span lies within distance at most one of an endpoint of that component, and hence an endpoint from a second interleaving component would create such a third edge. Conversely, any disjoint sequence of the four specified tiles with at least two unused vertices between successive endpoint spans is EOP, because no edge of the square path can connect endpoints of distinct components and leaves of each selected two-edge star are nonadjacent. This proves the claimed *unique* decomposition and all its boundary cases.

**2. Formal enumerator.** Each unused vertex carries size weight \(x\). The four tiles have bivariate total weight \(T(x,z)=z(x^2+x^3)+z^2(2x^4+x^5)\). For \(t\ge1\) selected components, one has arbitrary unused prefixes and suffixes and at least two unused vertices in each of the \(t-1\) internal gaps. Consequently their generating function is
\[
\frac{T(x,z)^t x^{2(t-1)}}{(1-x)^{t+1}}.
\]
The no-component contribution is \((1-x)^{-1}\). Summing the geometric series over \(t\) proves the rational generating function with equality as formal power series. Fixing \(s\) singleton tiles and \(d\) double-star tiles, choosing the order, selecting \(j\) long singletons and \(h\) long double stars, and distributing the \(L\) remaining unused vertices among \(t+1\) gaps gives the explicit coefficient formula. The distribution count is \(\binom{L+t}{t}\), by stars and bars. These choices are disjoint and exhaustive by the decomposition.

**3. Maximum cardinality.** If an EOP has \(d\) two-edge stars and \(s\) singletons, with \(k=2d+s\) selected edges and \(t=d+s\) components, its vertex budget obeys
\[
n\ge4d+2s+2(t-1)=6d+4s-2=3k+s-2.
\]
For fixed positive \(k\), the smallest possible \(s\) is zero for even \(k\) and one for odd \(k\). Both resulting inequalities are sharp: concatenate width-four two-edge stars separated by exactly two unused vertices, with a final width-two singleton when \(k\) is odd. Hence the exact minimum number of path vertices required for \(k\) selected edges is \(3k-2\) for even \(k\), and \(3k-1\) for odd \(k\). Solving these inequalities gives the six-residue maximum formula, including the small paths.

**4. Maximum multiplicities.** In the coefficient formula, write \(n=6k+r\) and substitute the just-proved maximum cardinality. The minimal-width estimate bounds the number of singleton tiles: in residues \(r=2,3,4,5\), respectively, only the all-short optimal block patterns and at most one added width/gap unit occur; in residues \(r=0,1\), at most one two-star-to-two-singleton replacement can occur. Separating the number of longer tiles and distributing the remaining at most three free vertices among gaps yields, after elementary binomial simplification, the six displayed \(M_{6k+r}\) expressions. For example, residue \(r=2\) consists of \(k\) width-four stars and one width-two singleton in any of \(k+1\) positions, giving \((k+1)2^k\). Residue \(r=4\) consists of \(k+1\) width-four stars, giving \(2^{k+1}\). For residue \(r=0\), the alternatives \(s=0\) or \(s=2\) give exactly \(2^{k-3}(11k^2+17k+8)\), and for residue \(r=1\) their at-most-three-unit slacks give \(2^{k-4}(15k^3+47k^2+50k+16)\). The remaining two branches follow by one-unit slack and the binomial distribution formula. The verifier independently checks these reductions through order fifty; the symbolic binomial count proves them for arbitrary \(k\).

## Verification

The standalone standard-library program `verify.py` constructs the actual graph edges \(|i-j|\in\{1,2\}\), forms the forbidden edge-pair relation by searching for third graph edges, and enumerates all EOP subsets for \(0\le n\le11\) without using the tile theorem. It compares this independent brute-force size distribution with both the tile recursion and the finite closed coefficient formula. It also compares the latter two descriptions and the maximum formula for \(12\le n\le50\). The checks were executed on the packaged source, and their original output is stored in `verify_output.txt`.

## Relationship to prior work

Chelladurai, Kalimuthu and Soundararajan introduced EOP sets (2022, DOI 10.1051/ro/2022171). Brešar and Samadi (arXiv:2403.00750, publicly available 1 March 2024) developed complexity, algorithms and extremal bounds; Brešar, Dravec, Hedžet and Samadi (arXiv:2406.04020) analyzed products and trees. These results do not state the displayed polynomial or six-residue multiplicity census for squared paths. Santra (arXiv:2510.16236, Section 2) subsequently supplied a general polynomial-time algorithm for computing the scalar EOP number of proper interval graphs; squared paths belong to this superclass, so **the scalar optimization problem already has an algorithmic solution**. The new claim is instead the explicit complete size distribution, unique four-tile encoding, and exact count of all maximizers. Bu, Chen and Zhu's 2022 work on injective edge coloring of powers of paths determines a distinct parameter—the number of colors needed to partition all edges into EOP classes—not the number of individual EOP edge subsets of each size. Its full text was not accessible for a definitive comparison; this is a residual priority risk, not evidence of noncoverage.

## Limitations

This theorem addresses only squares of **paths**, not higher path powers, cycle squares, or arbitrary proper interval graphs. It enumerates edge-open-packing subsets, not the number of complete injective edge colorings. Finite experiments check instances only and cannot by themselves prove the unrestricted result. Although the structural proof and finite counts were checked, no independent scientific audit or comprehensive bibliographic priority certificate has been performed. The power-graph injective-coloring proceedings paper was available by abstract but not full text, so a possible unindexed enumerative consequence remains unresolved.

## References

1. G. Chelladurai, K. Kalimuthu and S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research 56 (2022), 3765–3776. DOI: https://doi.org/10.1051/ro/2022171.
2. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750 (first public 2024-03-01). https://arxiv.org/abs/2403.00750.
3. B. Brešar, T. Dravec, J. Hedžet and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020 (first public 2024-06-06). https://arxiv.org/abs/2406.04020.
4. K. Santra, *Edge open packing on subclasses of chordal graphs*, arXiv:2510.16236 (first public 2025-10-17). https://arxiv.org/abs/2510.16236.
5. Y. Bu, W. Chen and J. Zhu, *Injective Edge Coloring of Power Graphs and Necklaces*, AAIM 2022, pp. 413–420. DOI: https://doi.org/10.1007/978-3-031-16081-3_36.
