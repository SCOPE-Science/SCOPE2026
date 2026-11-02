# Perfect matching cuts of \(P(n,3)\): two nonspoke resonance periods

## Finding

**Theorem.** Let \(n\ge 7\) be an integer and let \(P(n,3)\) be the generalized Petersen graph with outer vertices \(u_i\), inner vertices \(v_i\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\) (indices in \(\mathbb Z/n\mathbb Z\)). A *perfect matching cut* is the set of all crossing edges of a bipartition into two nonempty vertex classes, with exactly one crossing edge incident to each vertex. Count cuts as edge sets, without orienting the two shores. Then the number of perfect matching cuts is

\[
\boxed{c(P(n,3))=1+2\mathbf 1_{4\mid n}+5\mathbf 1_{5\mid n}.}
\]

Every cut belongs to exactly one of these classes:

1. The spoke cut (one cut), which has all \(n\) spokes as crossing edges.
2. If \(4\mid n\), two cuts whose crossings contain no spokes. Their shore colorings are represented by the repeated outer and inner color words \(a=b=(0011)^{n/4}\) and its cyclic translates.
3. If \(5\mid n\), five cuts with exactly \(n/5\) crossing spokes. Their shore colorings are represented by \(a=(00011)^{n/5}\) and \(b=(01011)^{n/5}\) and cyclic translates.

Thus a nonspoke perfect matching cut exists if and only if \(4\mid n\) or \(5\mid n\). In particular \(c(P(8,3))=3\), \(c(P(10,3))=6\), and \(c(P(20,3))=8\).

## Assumptions and scope

All graphs are simple, undirected and finite. The usual generalized Petersen definition requires \(1\le k<n/2\), so the parameter \(k=3\) starts at \(n=7\). The graph is connected because the outer rim forms a cycle and all inner vertices have spokes to that rim. A cut is determined uniquely, up to swapping shores, by its crossing-edge set in any connected graph. We distinguish a *perfect matching cut*, in which the crossing-edge set itself is a perfect matching, from a *disconnected perfect matching*, whose removal merely disconnects the graph; the latter is not enumerated here.

## Proof

Write \(a_i\in\{0,1\}\) for the shore color of \(u_i\) and \(b_i\in\{0,1\}\) for that of \(v_i\). Since the graph is cubic, its crossing edges form a perfect matching exactly when

\[
[a_i\ne a_{i-1}]+[a_i\ne a_{i+1}]+[a_i\ne b_i]=1,
\tag{1}
\]
\[
[b_i\ne b_{i-3}]+[b_i\ne b_{i+3}]+[b_i\ne a_i]=1
\tag{2}
\]

for every \(i\in\mathbb Z/n\mathbb Z\), where brackets are indicator functions. These two sets of equations already imply that the color classes are nonempty, since every vertex must have an opposite-color neighbor.

**Unique inner extension.** Equation (1) forbids \(a_{i-1}=a_{i+1}\ne a_i\). If both outer neighbors have color \(a_i\), it forces \(b_i=1-a_i\). If precisely one outer neighbor has the other color, it forces \(b_i=a_i\). Hence any permissible outer sequence determines the entire inner sequence uniquely. Define the partial function \(\tau:\{0,1\}^3\longrightarrow\{0,1\}\) by

\[
\tau(x,y,z)=\begin{cases}
1-y,&x=y=z,\\
y,&\text{exactly one of }x,z\text{ differs from }y,\\
\text{undefined},&x=z\ne y.
\end{cases}
\]

Then \(b_i=\tau(a_{i-1},a_i,a_{i+1})\). Equation (2) depends only on the nine consecutive outer colors \(a_{i-4},\ldots,a_{i+4}\): define \(L=\tau(a_{i-4},a_{i-3},a_{i-2})\), \(M=\tau(a_{i-1},a_i,a_{i+1})\), and \(R=\tau(a_{i+2},a_{i+3},a_{i+4})\). The local nine-bit window is *admissible* precisely when all three values are defined and

\[
[M\ne L]+[M\ne R]+[M\ne a_i]=1.
\tag{3}
\]

**Exact finite-state reduction.** Encode an eight-bit word \((x_0,\ldots,x_7)\) by the integer \(s=\sum_{j=0}^{7}2^j x_j\). Form a directed graph on the 256 integers \(s\in\{0,\ldots,255\}\). For each \(q\in\{0,1\}\), include the arc

\[
s\longrightarrow \lfloor s/2\rfloor+128q
\tag{4}
\]

if the nine-bit word consisting of the eight bits of \(s\) followed by \(q\) is admissible under (3), with the center at the fifth bit. By the overlapping-window construction, valid cyclic colorings of length \(n\) correspond *bijectively* to length-\(n\) closed directed walks with a distinguished starting position in this graph. This bijection applies for all \(n\ge7\), including windows that wrap the same cycle more than once; each closed walk specifies a consistent \(n\)-periodic outer coloring and therefore its unique inner coloring.

The graph in (4) has exactly 90 arcs. To determine its cycles, iteratively discard every vertex without an incoming or without an outgoing arc *within the current retained vertex set*. Each discarded vertex lies on no closed directed walk, and this remains true at every round. Starting with 256 vertices, the retained sizes after three rounds are, respectively,

\[
256\longrightarrow42\longrightarrow20\longrightarrow16.
\tag{5}
\]

The final 16 states, listed in increasing order, are

\[
0,24,49,51,57,99,102,115,140,153,156,198,204,206,231,255.
\]

Their **entire** induced directed edge set is the following five disjoint directed cycles (the first two are loops):

\[
(0),\qquad(255),\qquad(51,153,204,102),
\]
\[
(24,140,198,99,49),\qquad(57,156,206,231,115).
\tag{6}
\]

Equations (3)–(4) and the finite explicit lists (5)–(6) constitute a 256-state, 512-candidate exact certificate. The standalone source `verify.cpp` generates all 512 candidate transitions, independently repeats the three pruning rounds, checks every state and arc in (6), and makes no appeal to experimental extrapolation. Checking the 512 explicitly defined Boolean cases is a finite proof of the asserted state graph, while the closed-walk bijection proves its validity for every \(n\).

**Counting.** A directed cycle of length \(d\) contributes exactly \(d\) closed walks of length \(n\) when \(d\mid n\), and none otherwise. The 1-, 1-, 4-, 5-, 5-cycle decomposition therefore gives exactly

\[
2+4\mathbf1_{4\mid n}+10\mathbf1_{5\mid n}
\]

ordered shore colorings. Connectedness makes global color complementation a fixed-point-free pairing of colorings defining the same cut. Dividing by two gives the displayed formula.

Reading the cyclic words from (6) yields the constant, period-four, and period-five representatives stated above. For the constant outer word, every spoke crosses. The period-four word has \(b=a\) everywhere, hence no spokes cross. The period-five word has precisely one mismatch between \(a\) and \(b\) per five positions; cyclic shifts and complementation preserve that count. These three crossing-spoke counts distinguish the classes and finish the proof.

## Verification

The self-contained C++17 program `verify.cpp` checks the 90 candidate arcs and exact three-round core reduction, verifies that the 16 retained states induce precisely the five cycles in (6), and compares the resulting closed-walk counts with the theorem for every \(7\le n\le100\). Separately, it enumerates all \(2^{2n-1}\) shore-colorings with \(a_0=0\) directly against the original graph's crossing-edge conditions for every \(7\le n\le12\), totaling 11,182,080 tested assignments. It checks both cut counts and spoke-count strata and constructs witnesses for both nontrivial periods through \(n=100\). Compile and run with `c++ -std=c++17 -O2 verify.cpp -o verify && ./verify`. Its observed completion string is `VERIFY_OK`.

The full-coloring enumerations test finitely many orders. The exact Boolean-state certificate and closed-walk correspondence, not finite numerical extrapolation, establish the theorem for all \(n\ge7\).

## Relationship to prior work

Le and Telle (2021) formalize perfect matching cuts as vertex bipartitions with exactly one crossing neighbor at each vertex and study computational complexity and graph classes admitting efficient recognition; their conclusion explicitly identifies counting and enumeration of perfect matching cuts as a topic for further work. Bonnet, Chakraborty, and Duron (2023) establish hardness even for 3-connected cubic bipartite planar graphs, noting the equivalent partition of a cubic graph into monochromatic induced cycle unions. Neither inspected paper determines the number, periodic structure, or spoke spectrum of perfect matching cuts in \(P(n,3)\).

The spoke cut exists in every generalized Petersen graph and is not a new existence assertion. A known special calculation for the jump-two family does not imply the jump-three count: the jump-three family develops an additional primitive period four, and \(P(n,3)\) is not generally isomorphic to \(P(n,2)\). The assessed result is the exact exhaustive classification and count for the jump-three family. Related work on matching preclusion, Hamiltonian cycles and ordinary 2-factors concerns distinct invariants and does not automatically classify cuts that are themselves perfect matchings.

## Limitations

The result is specific to the standard simple cubic family \(P(n,3)\) with \(n\ge7\). It does not count perfect matchings whose deletion disconnects a graph but that are not crossing-edge sets; such objects can strictly contain an edge cut. No formula is asserted for arbitrary jump \(k\). Exhaustive literature searches cannot exclude unindexed equivalent results, and no independent mathematical audit has been performed.

## References

1. Van Bang Le and Jan Arne Telle, *The Perfect Matching Cut Problem Revisited*, arXiv:2107.06399, initial version 13 July 2021. https://arxiv.org/html/2107.06399v1
2. Édouard Bonnet, Dibyayan Chakraborty, and Julien Duron, *Cutting Barnette graphs perfectly is hard*, arXiv:2302.11667, initial version 22 February 2023. https://arxiv.org/html/2302.11667v1
