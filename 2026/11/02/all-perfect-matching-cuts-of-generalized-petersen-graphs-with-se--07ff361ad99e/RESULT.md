# All perfect matching cuts of generalized Petersen graphs with second jump two

## Finding
Let \(G_n=P(n,2)\) be the generalized Petersen graph, for any integer \(n\ge5\), with vertices \(u_i,v_i\) (indices modulo \(n\)), outer edges \(u_i u_{i+1}\), inner edges \(v_i v_{i+2}\), and spokes \(u_i v_i\). A **perfect matching cut** means an edge set equal to the edges crossing some nontrivial vertex bipartition and simultaneously a perfect matching.

**Theorem.** The number of distinct perfect matching cut edge sets in \(G_n\) is exactly
\[
\operatorname{pmc}(G_n)=1+5\,\mathbf1_{5\mid n}.
\]
For every \(n\), the set of all spokes is one such cut. If \(5\mid n\), there are exactly five others, and if \(5\nmid n\), there are no others. More precisely, every valid binary vertex labeling, with edges of differing endpoint labels taken as the cut, is either (i) constant on each vertex layer, with opposite constants on the two layers, or (ii) when \(5\mid n\), an outer-layer bit word obtained by repeating a cyclic rotation of \(11000\) or \(00111\), with the inner-layer labels uniquely determined by the outer ones. There are precisely \(2+10\mathbf1_{5\mid n}\) valid labeled binary vertex colorings; complementary labelings define the same cut.

## Assumptions and scope
Graphs are finite, simple, undirected, and indexed as above. The condition \(n\ge5\) avoids degenerate inner edges. A crossing edge set is a perfect matching if and only if every graph vertex has exactly one neighbor of the opposite color. Only distinct edge cuts are counted, not orientations or ordered bipartitions. The graph \(G_n\) is connected because the outer vertices form a cycle and each inner vertex has a spoke.

## Proof
Assign bits \(x_i\in\{0,1\}\) to \(u_i\), and bits \(y_i\) to \(v_i\). Put
\[
d_i=[x_{i-1}\ne x_i]+[x_{i+1}\ne x_i].
\]
The condition of exactly one differently colored neighbor at \(u_i\) is equivalent to \(d_i\le1\) and the forced rule
\[
y_i=x_i\oplus(1-d_i),
\]
where \(\oplus\) denotes addition modulo two. The condition at \(v_i\) is then precisely
\[
[y_{i-2}\ne y_i]+[y_{i+2}\ne y_i]=d_i.\tag{1}
\]
Consequently, every solution is determined by its cyclic outer word, and these local equations are necessary and sufficient.

Here is a complete finite-state determination of the cyclic outer words satisfying (1). Let \(t=t_0t_1\cdots t_6\) be any seven-bit word. For \(j\in\{1,3,5\}\), compute
\[
\delta_j=[t_{j-1}\ne t_j]+[t_{j+1}\ne t_j].
\]
Admit \(t\) if all three \(\delta_j\le1\), and if, defining \(z_j=t_j\oplus(1-\delta_j)\), one has
\[
[z_1\ne z_3]+[z_5\ne z_3]=\delta_3.\tag{2}
\]
For each admitted seven-bit word, draw a directed edge from its first six bits to its last six bits. A cyclic outer word of length \(n\) yields a closed directed walk of length \(n\) in this graph, and conversely every such closed walk yields a valid cyclic outer word (also for \(n=5,6\), where its seven-bit windows may repeat coordinates).

For completeness, the exact set of **all 28** admitted seven-bit words, obtained by substituting all \(2^7=128\) possibilities in (2), is

```
0000000 0000011 0000100 0000111 0001100 0001111
0010000 0010011 0011000 0011011 0011100 0011111
0110001 0111001 1000110 1001110 1100000 1100011
1100100 1100111 1101100 1101111 1110000 1110011
1111000 1111011 1111100 1111111
```

Repeatedly remove every six-bit state having zero incoming or zero outgoing edges **within the remaining graph**, and all incident edges. This removes respectively \(20,4,2\) states in three rounds. The surviving graph has exactly the following 12 edges (the seven-bit words are written as edges), with six-bit overlap defining their endpoints:

```
0000000 1111111
0001100 0011000 0110001 1100011 1000110
0011100 0111001 1110011 1100111 1001110
```

Each surviving vertex has indegree and outdegree one. The graph consists of two loops, at \(000000\) and \(111111\), and two directed five-cycles:

```
000110 -> 001100 -> 011000 -> 110001 -> 100011 -> 000110
001110 -> 011100 -> 111001 -> 110011 -> 100111 -> 001110
```

Removing a zero-indegree or zero-outdegree state cannot delete any directed closed walk, so the surviving graph contains **all** possibilities for a cyclic outer word. The two loops give the two constant words. The five-cycles yield words periodic with minimal period five: the respective complementary patterns are rotations of \(11000\) and \(00111\), which occur exactly when \(5\mid n\). There are five rotations of each. This proves the classification of binary labelings.

By connectedness, an edge cut uniquely determines its bipartition up to swapping the two colors. Therefore, the number of distinct perfect matching cuts is half the number of binary colorings, namely \(1+5\mathbf1_{5\mid n}\). The theorem follows.

## Verification
The self-contained Python 3 program `verify.py` recomputes every seven-bit admissibility decision, the successive pruning counts, the complete cyclic core, and its component lengths. Separately, it builds actual generalized Petersen graph edges and exhaustively examines vertex colorings with one fixed root color for \(5\le n\le10\), comparing the original exactly-one-crossing-neighbor condition against the outer-word formulas. It checks all outer binary words through \(n=18\) and constructs the nontrivial period-five patterns through \(n=210\). Executing the program prints `VERIFY_OK`. The infinite result follows from the proved finite-state equivalence and complete 128-case computation, not extrapolation from tested finite graph orders. The admitted-word table and the two core cycles above are human-readable finite certificates independent of any external software.

## Relationship to prior work
Perfect matching cuts and their equivalence to bipartitions with exactly one neighbor across at each vertex are standard; Le and Telle [2] analyze computational complexity and algorithmic graph classes. Bonnet, Chakraborty, and Duron [1] prove NP-completeness for connected cubic bipartite planar graphs and describe cubic matching cuts as partitions into induced cycles. Their results do not give the exact number or classification for \(P(n,2)\). Chia and Thomassen [3] determine Hamiltonian-cycle counts for \(P(n,2)\); Hamiltonian-cycle enumeration does not determine the two-color-compatible perfect matchings classified here. The result should also be compared with other names for a perfect matching cut: a perfect matching that is a graph cut, a \((2,\mathbb N,\{1\})\)-partition, and a bipartition into two induced 2-regular subgraphs in the cubic case.

## Limitations
No result is asserted for generalized Petersen graphs with an arbitrary inner jump \(k\ne2\), nor for disconnected perfect matchings (whose complement is disconnected but which need not themselves be edge cuts). General perfect-matching or Hamiltonian-cycle enumerations count different objects. While no prior statement equivalent to the exact modulo-five formula was identified in the material inspected, an unindexed older specialization or a stronger general theorem could supersede publication priority. The verification is finite, and no independent external review or audit was performed.

## References
[1] É. Bonnet, D. Chakraborty, and J. Duron, *Cutting Barnette graphs perfectly is hard*, arXiv:2302.11667 (first posted 2023-02-22), https://arxiv.org/abs/2302.11667.
[2] V. B. Le and J. A. Telle, *The Perfect Matching Cut Problem Revisited*, arXiv:2107.06399 (first posted 2021-07-13), https://arxiv.org/abs/2107.06399.
[3] G. L. Chia and C. Thomassen, *Grinberg's Criterion Applied to Some Non-Planar Graphs*, Ars Combinatoria 100 (2011), 3–7, https://combinatorialpress.com/article/ars/Volume%20100/volume-100-paper-1.pdf.
