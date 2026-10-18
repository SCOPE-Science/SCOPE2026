# Exact orbit-refinement wavefronts in marked ternary Cartesian grids

## Finding
Let \(d\ge 2\) be an integer. Define the graph \(X_d=P_3^{\square d}\) on \(\{0,1,2\}^{d}\), with two vertices adjacent exactly when one coordinate changes by one and every other coordinate is unchanged. Give \(o=(0,\ldots,0)\) one initial colour and all other vertices a second common colour. Colour refinement means the synchronous update consisting of the old colour together with the multiset of neighbouring old colours; round zero is the initial colouring.

For a vertex \(x\), let \(b(x)\) count coordinates equal to \(1\), let \(c(x)\) count coordinates equal to \(2\), and put \(s(x)=b(x)+2c(x)\). For \(b,c\ge 0\) with \(b+c\le d\), set
\[
\Omega_{b,c}=\{x:b(x)=b,\ c(x)=c\}.
\]
**Every intermediate partition is explicit.** For each round \(t\ge1\), the colour classes are the nonempty sets
\[
\Omega_{b,c}\quad\text{with }b+2c\le t,
\qquad
U_{b,t}=\bigcup_{\substack{0\le c\le d-b\\b+2c>t}}\Omega_{b,c}.
\]
In particular, all reached coordinate-count types become separate colour classes, while all unreached types with the same number of \(1\)-coordinates remain merged. At round zero only \(\{o\}\) and its complement are coloured differently.

The **exact least stable round** is
\[
\boxed{R(d)=2d-2.}
\]
At that round, the classes are exactly the orbits of the automorphisms fixing \(o\). Their number and their cardinalities are respectively
\[
\boxed{\binom{d+2}{2}},\qquad
\boxed{|\Omega_{b,c}|=\frac{d!}{(d-b-c)!\,b!\,c!}}.
\]
Thus refinement requires \(2d-2\) strict rounds on a family of \(3^d\)-vertex graphs. Sharpness is witnessed by \(\Omega_{0,d-1}\) and \(\Omega_{0,d}\), which are still merged after round \(2d-3\) but are different rooted automorphism orbits.

## Assumptions and scope
Graphs are finite, simple, undirected, and loopless. Exactly one vertex—the all-zero corner—is individually marked. Coordinates are unlabelled as graph structure; coordinate permutations are automorphisms. The statement holds for every integer \(d\ge2\), not only for the dimensions used in verification. A round is counted only when the equitable partition becomes finer; the partition at \(R(d)+1\) is unchanged.

## Proof
**1. Local state quotient.** Put \(a=d-b-c\). The neighbours of every vertex in \(\Omega_{b,c}\) have state pairs and multiplicities
\[
\begin{array}{c|c}
\text{state}&\text{multiplicity}\\\hline
(b+1,c)&a\\
(b-1,c)&b\\
(b-1,c+1)&b\\
(b+1,c-1)&c
\end{array}
\]
with zero-multiplicity or out-of-range rows omitted. Every vertex has degree \(a+2b+c=d+b\). Coordinate permutations act transitively on each \(\Omega_{b,c}\), so colour refinement cannot split a state \(\Omega_{b,c}\) internally. The graph distance from the marked corner is \(s=b+2c\); every edge changes this distance by exactly one.

**2. Base round.** The first-round colour determines the old colour and the degree \(d+b\), hence determines \(b\). Among unmarked vertices, precisely those of state \((1,0)\) are adjacent to \(o\). Thus \(\Omega_{0,0}\), \(\Omega_{1,0}\), and for each fixed \(b\) all remaining states of distance greater than one have exactly the partition asserted at \(t=1\).

**3. Wavefront induction.** Suppose the asserted partition holds after round \(t\ge1\). In each fixed \(b\)-tail \(U_{b,t}\), at most one state has \(s=t+1\), since admissible distances with fixed \(b\) differ by two. Such a state has a neighbour at distance \(t\) (decrease one positive coordinate); its neighbour therefore has a uniquely identified reached-state colour. No state of the same tail with \(s>t+1\) has any neighbour with a reached-state colour, because graph distance changes by at most one. Hence the state at \(s=t+1\), if present, splits off.

Conversely, every vertex in any unreached state with \(s>t+1\) has only neighbours in unreached tails: precisely \(a+c=d-b\) in the \((b+1)\)-tail and \(2b\) in the \((b-1)\)-tail. These counts do not depend on \(c\). Hence no two such states with the same \(b\) separate at round \(t+1\). Already-separated states stay separated by the inclusion of the old colour in the refinement signature. This completes the induction and proves the partition formula for all \(t\ge1\).

**4. Exact depth.** For fixed \(b\), the candidate distances are \(b,b+2,\ldots,2d-b\). Its tail comprises at most one state precisely once the second-largest such distance, \(2d-b-2\), has been reached (unless there is only one state). The largest of these thresholds over \(0\le b<d\) is \(2d-2\), attained at \(b=0\). At the preceding round, the distinct states \((0,d-1)\) and \((0,d)\) are both unreached and hence share a colour. At round \(2d-2\) every tail is at most one orbit, so the partition is stable. The depth is therefore exactly \(2d-2\).

**5. Automorphism orbits.** Every coordinate permutation preserves the graph and the corner, and its orbits are exactly the sets \(\Omega_{b,c}\). To exclude further rooted automorphisms, observe that the neighbours of \(o\) are the unit vectors \(e_i\). Every automorphism fixing \(o\) permutes these. Among the neighbours of \(e_i\) at distance two from \(o\), the vertex \(2e_i\) has degree \(d\), while every \(e_i+e_j\), \(j\ne i\), has degree \(d+2\). Therefore \(2e_i\) is recovered canonically from \(e_i\). Once the action on the \(e_i\)'s is fixed, that on the \(2e_i\)'s is fixed; and for every \(x\),
\[
\operatorname{dist}(2e_i,x)-\operatorname{dist}(o,x)=2-2x_i.
\]
These distances recover every coordinate of \(x\), so an automorphism fixing \(o\) and all \(e_i\) is the identity. The full rooted stabilizer is exactly the coordinate-permutation group \(S_d\), proving the orbit claim and orbit counts.

## Verification
Two standalone Python programs, using only the standard library, are included. Run `python verify_full.py` and `python verify_quotient.py` from the directory containing these files. `verify_full.py` constructs the actual vertex graph and performs synchronous colour refinement in dimensions \(2\) through \(8\), comparing every round's *full vertex partition* with the theorem and checking the exact stable round and orbit counts. `verify_quotient.py` separately implements the multiplicity-weighted state quotient, comparing every round's partition for dimensions \(2\) through \(18\), then \(20,25,30,35,40,50,60\). Its transition counts and indexing do not reuse the vertex-level construction. Logs `verification_full.log` and `verification_quotient.log` give the actual executions.

The proof's induction and automorphism argument establish all dimensions; experiments provide finite checks, not an infinite certificate.

## Relationship to prior work
Colour refinement, its connection with two-variable counting logic, and orbit-refinability are developed by Arvind, Köbler, Rattan and Verbitsky (2015) and by Kiefer, Schweitzer and Selman (2015). Krebs and Verbitsky (2014) investigate general logical-depth lower bounds for colour refinement; Kiefer and McKay (2020) establish sharp extremal iteration bounds. Those theorems do not, by their statements, determine the complete round-by-round partition or exact marked-corner depth for the Cartesian power of the three-vertex path. Albertson (2005) and Imrich–Klavžar (2006) investigate distinguishing vertex labelings of Cartesian powers, a symmetry-breaking invariant different from synchronous counting refinement of one specified corner. The present theorem concerns a different family from two-dimensional rectangular grids and from hypercubes, and its dimension-uniform depth and tail wavefront are not immediate from either family's individual results. No claim is made that a literature search establishes publication priority.

## Limitations
This result establishes an exact partition and depth only for a single specifically marked corner of \(P_3^{\square d}\). It does not establish colour-refinement identification against arbitrary competing graphs, general path-factor lengths, arbitrary extra vertex colours, or universal stabilization bounds for graph products. A specialized earlier derivation cannot be ruled out without exhaustive independent bibliographic review.

## References
- M. O. Albertson, *Distinguishing Cartesian Powers of Graphs*, Electronic Journal of Combinatorics 12 (2005), #N17, first public 2005-09-19, https://doi.org/10.37236/1984.
- W. Imrich and S. Klavžar, *Distinguishing Cartesian powers of graphs*, Journal of Graph Theory 53 (2006), 250–260, https://doi.org/10.1002/jgt.20190.
- A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first public 2014-07-11, https://arxiv.org/abs/1407.3175.
- V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first public 2015-02-04, https://arxiv.org/abs/1502.01255.
- S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first public 2015-03-30, https://arxiv.org/abs/1503.08792.
- S. Kiefer and B. McKay, *The Iteration Number of Colour Refinement*, arXiv:2005.10182, 2020, https://arxiv.org/abs/2005.10182.
