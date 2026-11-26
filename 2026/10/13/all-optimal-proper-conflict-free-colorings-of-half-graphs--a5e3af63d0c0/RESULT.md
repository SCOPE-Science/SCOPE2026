# All optimal proper conflict-free colorings of half graphs

## Finding

For \(n\ge4\), let \(H_n\) have vertices \(a_1,\ldots,a_n\) and \(b_1,\ldots,b_n\), with \(a_ib_j\) an edge exactly when \(i\le j\). The proper conflict-free chromatic number is already known to be four: \(H_n\) is a chain graph with \(2n-2\) vertices of degree at least two, so Pradhan and Sharma's chain-graph theorem applies [1, Theorem 8]. **The contribution here is the complete description and count of the optimal colorings, not this scalar value.**

In each optimal coloring \(\varphi\), the colors
\[
(c_0,c_1,c_2,c_3)=(\varphi(a_1),\varphi(a_2),\varphi(b_{n-1}),\varphi(b_n))
\]
are pairwise distinct. Fix their names. The full set of optimal colorings is given by the following independent choices:
\[
\begin{aligned}
 &t\in\{c_0,c_1\}, &\quad \varphi(a_3)=\cdots=\varphi(a_{n-1})=t, &\quad \varphi(a_n)\in\{t,c_2\},\\
 &s\in\{c_2,c_3\}, &\quad \varphi(b_2)=\cdots=\varphi(b_{n-2})=s, &\quad \varphi(b_1)\in\{s,c_1\}.
\end{aligned}
\]
Consequently there are exactly \(16\) optimal colorings up to permuting colors, and \(384\) optimal colorings with a fixed palette of four named colors.

## Assumptions and scope

A proper conflict-free coloring is a proper vertex coloring for which each nonisolated vertex has a color used exactly once in its **open** neighborhood [2]. Optimal means using the fewest colors. Only permutations of colors, not graph automorphisms, are factored out in the count of 16. The statement is for the specified half graphs, not for arbitrary chain graphs, whose ordered neighborhoods need not have distinct sizes.

## Proof

The neighborhood of \(b_2\) is \(\{a_1,a_2\}\), so the two vertices have distinct colors. The neighborhood of \(a_{n-1}\) likewise forces distinct colors on \(b_{n-1},b_n\). Each vertex in the first pair is adjacent to each in the second, so properness gives all four inequalities across the pairs. Thus the four core colors are distinct and name the whole optimal palette.

The universal adjacency of \(b_n\) to \(A=\{a_1,\ldots,a_n\}\) excludes \(c_3\) from \(A\). Adjacency to \(b_{n-1}\) excludes \(c_2\) from \(a_1,\ldots,a_{n-1}\). Every prefix of those first \(n-1\) vertices is a neighborhood of some \(b_j\); in the resulting binary color sequence, every prefix must therefore have a singleton. The first two colors differ. The third chooses a majority color \(t\), while the other stays a singleton. Each subsequent binary entry must repeat \(t\): repeating the singleton would make both multiplicities at least two. Since \(n\ge4\), there is such a third position in the restricted prefix. At \(a_n\) the full prefix \(N(b_n)\) still needs a singleton. The only allowed extensions are to repeat \(t\) or to use the new color \(c_2\). The reverse sequence \(b_n,\ldots,b_1\) has the symmetric constraints: \(a_1\) excludes \(c_0\) throughout it, \(a_2\) excludes \(c_1\) through \(b_2\), and the relevant neighborhoods are reversed prefixes. This gives precisely the block color \(s\) and the two choices at \(b_1\).

Conversely, the only colors that can appear on both shores under these rules are \(c_2\) at \(a_n\) and \(c_1\) at \(b_1\). These uses are proper because \(a_n\) has sole neighbor \(b_n\) of color \(c_3\) and \(b_1\) has sole neighbor \(a_1\) of color \(c_0\). The forced singleton survives in each prefix or reversed prefix of length at least three, including the full ones, and the neighborhoods of sizes one and two also have a singleton. The rules therefore give proper conflict-free four-colorings. They are optimal by the four core colors. The two interior blocks are nonempty, and their colors and the two endpoint choices are recoverable from each coloring. With the core colors named this gives \(2^4=16\) distinct assignments, and assigning the four palette labels to the core contributes \(4!\).

## Verification and boundaries

The accompanying Python 3 program `verify.py` enumerates all assignments from palettes of sizes three and four at \(n=3,4,5\), testing each edge and open neighborhood directly. In the recorded run there were zero valid three-color assignments. For \(n=4,5\) the verifier finds 384 named four-colorings and the exact set of 16 forms after fixing the core colors. It also definition-checks every listed form for \(4\le n\le50\). These are bounded checks of the proof, not a substitute for it. Run `python3 verify.py` with assertions enabled.

At \(n=3\) both interior blocks are empty. The core still forces four colors, but either endpoint can choose any of the three colors not forbidden by its sole neighbor: each full prefix or suffix has length three and begins with two distinct colors, so some color is still a singleton. This gives 9 color-permutation classes and 216 named colorings, rather than the stated general census. The classification is not claimed for \(n=3\), for repeated neighborhood classes, or when quotienting by graph symmetries.

## Relationship to prior work

Pradhan and Sharma [1, §4.3, pp. 15–16] determine the scalar invariant on chain graphs; their Observation 3 already gives a canonical four-coloring, corresponding here to \(t=c_1\), \(s=c_2\), with no endpoint reusing a color from the other shore. Their algorithm computes an optimal coloring, not all optimal colorings or their number. The refinement here forces the binary prefix and suffix structure at optimality and enumerates the full set, including patterns with color reuse across shores. The inspected prior theorem does not characterize these patterns. Other optima on different bipartite families do not imply this classification. Earlier or differently indexed classifications beyond the sources examined are not ruled out.

## References

1. Dinabandhu Pradhan and Vaishali Sharma, *Complexity and algorithms for proper conflict-free coloring in graphs*, arXiv:2608.10874v2, §4.3, Observation 3 and Theorem 8. https://arxiv.org/abs/2608.10874v2
2. I. Fabrici, B. Lužar, R. Rindošová and R. Soták, *Proper conflict-free and unique-maximum colorings of planar graphs with respect to neighborhoods*, Discrete Applied Mathematics 324 (2023), 80–92. https://doi.org/10.1016/j.dam.2022.09.011
