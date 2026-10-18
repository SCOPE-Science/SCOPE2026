# The sharp diameter threshold and unique six-vertex onset of finite multiset partition dimension

## Finding

**Theorem.** Every finite simple connected graph \(G\) with at least two vertices and diameter at most two has \(\operatorname{mpd}(G)=\infty\). The smallest possible diameter of a nontrivial connected graph with finite multiset partition dimension is therefore three, and this boundary is attained on six vertices.

More precisely, among all connected diameter-three graphs with at most six vertices there is exactly one isomorphism class having finite multiset partition dimension. The representative \(H\) with vertex set \(\{0,1,2,3,4,5\}\) has edges
\[
E(H)=\{01,03,04,12,15,23,34\}.
\]
Its multiset partition dimension is exactly \(\operatorname{mpd}(H)=5\). It has precisely **two** resolving multiset partitions (unordered sets of nonempty vertex blocks): all blocks are singletons except the unique two-vertex block, which is either \(\{1,2\}\) or \(\{1,3\}\). Neither the four-block partitions nor the six-block discrete partition resolves \(H\), showing that this resolving property is not preserved by refinement.

## Assumptions and scope

Graphs are finite, connected, undirected, loopless, and simple; their distances are ordinary unweighted shortest-path distances. A partition \(\Pi=\{B_1,\ldots,B_k\}\) consists of nonempty, disjoint blocks covering every vertex. The distance to a block is \(d(v,B_i)=\min_{u\in B_i}d(v,u)\). Its **multiset partition code** is the multiset
\[
R_\Pi(v)=\{\!\{d(v,B_1),\ldots,d(v,B_k)\}\!\}.
\]
The partition resolves when these codes are distinct for every two vertices. The number \(\operatorname{mpd}(G)\) is the minimum such \(k\), or infinity if no resolving partition exists. Part order has no role; two partitions are identified when they consist of the same blocks. Diameter is the largest distance between two vertices. The first statement covers every number of vertices at least two; the finite sharp-onset statement covers all connected diameter-three graphs with at most six vertices, not larger orders.

## Proof

**Unrestricted diameter obstruction.** Fix a connected graph of order \(n\ge2\) and diameter at most two. In a partition into \(k\) blocks, every vertex has exactly one zero among its \(k\) block distances: the zero belongs to its own block. Every other distance is either one or two. Consequently, its multiset code is completely specified by the number of entries equal to one, and **at most \(k\) distinct codes** are possible. Resolving all \(n\) vertices requires \(k\ge n\). As a partition cannot have more than \(n\) blocks, it must be the all-singleton partition. Under this partition, the number of ones in the code of a vertex is precisely its degree. But degrees in a connected simple graph on \(n\) vertices belong to \(\{1,\ldots,n-1\}\), a set of only \(n-1\) values. Two distinct vertices therefore have the same degree and the same code. Contradiction. This proves the unrestricted assertion without any computation.

**Sharp six-vertex census.** For each of the orders four, five and six, enumerate all labelled simple graphs using a binary choice for each unordered pair of vertices. There are respectively \(2^6\), \(2^{10}\), and \(2^{15}\) edge masks. Compute their complete shortest-path distance matrices by breadth-first search; retain exactly the connected graphs whose diameter is three. The respective counts are
\[
12,\quad300,\quad12540.
\]
For each retained graph enumerate **every** set partition by the restricted-growth-word recursion: the first entry is zero, and each subsequent entry may range from zero to one more than the largest preceding entry. This enumeration has respectively \(15,52,203\) distinct partitions; it includes all block counts and identifies permutations of blocks. For each partition compute the exact sorted block-distance tuple for every vertex, rejecting the partition on any repeated tuple.

The resulting number of labelled connected diameter-three graphs admitting at least one resolving multiset partition is respectively
\[
0,\quad0,\quad720.
\]
The verifier then tests every one of the 720 passing six-vertex masks against the witness \(H\) under all six-vertex permutations and verifies that **all 720 are isomorphic to \(H\)**. This is exhaustive: every simple graph on the relevant vertex sets occurs in the edge-mask loops, every set partition occurs in the restricted-growth recursion, each code is computed from the graph distance matrix, and every isomorphism is tested by vertex permutations. The explicit, self-contained Python code `verifier.py` performs all loops, contains the coverage assertions, and is therefore an exact finite certificate, not sampling or extrapolation. Orders below four cannot have diameter three.

**The witness and all its optimal partitions.** For the representative \(H\), one resolving partition consists of the blocks
\[
\{0\},\quad\{1,2\},\quad\{3\},\quad\{4\},\quad\{5\}.
\]
Its six codes, in vertex order zero through five, are
\[
\begin{array}{c|l}
0&(0,1,1,1,2)\\
1&(0,1,1,2,2)\\
2&(0,1,2,2,2)\\
3&(0,1,1,1,3)\\
4&(0,1,1,2,3)\\
5&(0,1,2,3,3)
\end{array}
\]
where tuples are written in sorted order and stand for multisets. The codes are all distinct. The second resolving partition merges \(\{1,3\}\), leaving the other vertices as singleton blocks. Exhaustive evaluation of **all 203** partitions of this fixed graph yields exactly these two, each with five parts, and no others. Thus \(\operatorname{mpd}(H)=5\), and splitting the two-vertex block in either case yields the nonresolving six-singleton partition. The uniqueness and the two-partition classification follow.

## Verification

Running `python3 verifier.py` with a standard Python 3 interpreter requires no external packages. The code independently generates all labelled graphs of orders four, five and six, computes graph distances from edge masks, enumerates all nonempty set partitions exactly once, and checks every sorted multiset-partition code. It reports the exact diameter-three counts \(12,300,12540\), the corresponding resolving labelled graph counts \(0,0,720\), and confirms that each of the 720 is isomorphic to the stated graph. It also verifies exactly two five-part bases on the witness and no other resolving partition. `verification_output.txt` records the actual run; the unbounded diameter-two proof above is mathematical and does not depend on this finite enumeration.

## Relationship to prior work

Albejania, Lin, Ryan and Sugeng introduced the multiset partition dimension in a 2026 paper [1], proving general restrictions, exact values for paths, cycles and selected grid families, and infinitude for complete graphs, wheels, friendship graphs, fans and related families. The paper's listed infinitude families are all covered by the diameter-two theorem when their graphs have diameter at most two. In contrast, no all-connected-graphs diameter-two obstruction or complete six-vertex diameter-three onset classification was found in the inspected presentation. The same authors' survey [2] separately proposed and discussed this parameter; its Section 8.1 does not supply the asserted threshold or census. The other contemporary multiset-parameter survey [3] concerns mainly vertex-landmark variants and should not be conflated with multiset **partition** dimension. These prior differences are comparisons of hypotheses and conclusions, not evidence that absence of a matching phrase proves novelty.

## Limitations

The finite uniqueness claim is deliberately restricted to graph order at most six and diameter three; it gives no characterization for all larger diameter-three graphs. The universal impossibility claim covers diameter at most two only. The six-vertex uniqueness requires executing or inspecting the complete finite enumerator and has not been independently audited. Bibliographic priority is provisional: an equivalent theorem in older distance-histogram or unordered-partition terminology could exist. No claim is made about the computational complexity of multiset partition dimension.

## References

1. A. Albejania, Y. Lin, J. Ryan, and K. A. Sugeng, *Multiset Partition Dimension of Graphs*, first public arXiv version 8 July 2026, arXiv:2607.07407. https://arxiv.org/abs/2607.07407
2. A. Albejani, Y. Lin, J. Ryan, and K. A. Sugeng, *A Survey on Multiset Dimension and Its Variations*, arXiv:2607.08128. https://arxiv.org/abs/2607.08128
3. M. Farhan, S. Klavžar, D. Kuziak, and I. G. Yero, *Multiset resolvability parameters in graphs: A survey with new results and open problems*, arXiv:2607.10311. https://arxiv.org/abs/2607.10311
