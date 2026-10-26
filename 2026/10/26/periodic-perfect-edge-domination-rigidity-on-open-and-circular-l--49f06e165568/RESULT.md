# Periodic perfect-edge-domination rigidity on open and circular ladders

## Finding
Let \(L_n=P_n\square K_2\) be the two-row ladder with \(n\ge1\) rungs, and let \(Q_n=C_n\square K_2\) be its circular counterpart for \(n\ge3\). An edge set \(F\subseteq E(G)\) is *perfect edge dominating* (PED) if each omitted edge is adjacent to exactly one selected edge. The condition imposes no restriction on selected edges. Write
\[
\mathcal E(G;z)=\sum_{F\text{ PED}}z^{|F|}.
\]
Then \(\mathcal E(L_1;z)=z\), and for every integer \(n\ge2\),
\[
\boxed{\mathcal E(L_n;z)=z^{3n-2}+\bigl(2+2\mathbf{1}_{\{n\equiv2\pmod3\}}\bigr)z^n.}
\]
For every integer \(n\ge3\),
\[
\boxed{\mathcal E(Q_n;z)=z^{3n}+6\mathbf{1}_{\{6\mid n\}}z^n.}
\]
Consequently, all nontrivial PED sets have cardinality exactly \(n\): there are two or four on an open ladder, depending on \(n\bmod3\), and there are six on a circular ladder precisely when \(6\mid n\). The only remaining PED set is the full edge set. All these nontrivial PED sets have adjacent selected edges, so neither family (apart from the single-edge \(L_1\)) has a dominating induced matching. In particular the family \(Q_n\) exhibits a sharp periodic transition between possessing and not possessing any proper PED set, even though each \(Q_n\) lacks a dominating induced matching.

## Assumptions and scope
Graphs are finite, simple and undirected. \(P_n\) denotes the path on \(n\) vertices and \(C_n\) the cycle on \(n\ge3\) vertices. The Cartesian product has two rows \(t_i,b_i\); for \(L_n\), horizontal edges connect columns \(i\) and \(i+1\), \(0\le i<n-1\); for \(Q_n\), the index \(i\) is cyclic modulo \(n\). In both graphs the rung is \(t_ib_i\). Distinct sets of *labelled graph edges* are counted separately; no quotient by rotations, reflections or row swapping is taken. The exponent in \(\mathcal E\) is the number of selected edges, not vertices. A proper PED set differs from the entire edge set; a dominating induced matching (DIM) additionally dominates every selected edge exactly once and therefore has pairwise nonadjacent selected edges.

## Proof
For each column \(i\), define three bits \(r_i,a_i,b_i\): the rung and the upper and lower outgoing horizontal edge, respectively. For an open ladder we set the two outgoing horizontal bits at the last column to zero. On a circular ladder they are cyclic. Encode each triple as \(t_i=4r_i+2a_i+b_i\), where \(0\le t_i\le7\). For all genuine edges, the defining condition is equivalent to the following three local implications:
\[
\begin{aligned}
r_i=0&\Longrightarrow a_{i-1}+b_{i-1}+a_i+b_i=1,\\
a_i=0&\Longrightarrow a_{i-1}+a_{i+1}+r_i+r_{i+1}=1,\\
b_i=0&\Longrightarrow b_{i-1}+b_{i+1}+r_i+r_{i+1}=1.
\end{aligned}
\]
For an open ladder the second and third implications apply only to the existing horizontal edges, and missing horizontal bits before the first column equal zero. They follow simply by listing the edges incident with the two endpoints of an omitted edge, excluding the edge itself.

Construct a directed graph on \(8^2=64\) states \((x,y)\) with \(0\le x,y\le7\). There is an arc \((x,y)\to(y,z)\) exactly when the displayed three implications hold for the middle triple \(y\), with previous triple \(x\) and next triple \(z\). In numeric state labels, \((x,y)\) has label \(8x+y\). There are exactly 102 arcs, obtained by checking the \(8^3\) triples; the standalone verifier enumerates every one.

For the open ladder, start with the virtual preceding triple zero, so initial states have labels \(0,1,\ldots,7\). After \(n-1\) transitions the state is \((t_{n-2},t_{n-1})\). The terminal triple has zero outgoing horizontal bits, and the final rung is either selected or has exactly one selected incoming horizontal neighbour. Thus the terminal-state set is exactly
\[
T=\{8x+y:y\in\{0,4\},\ y=4\ \text{or}\ a(x)+b(x)=1\},
\]
where \(a(x),b(x)\) are the last two bits of \(x\). The intersection of states reachable from an initial state with states capable of reaching \(T\) consists of precisely the following 14 states. Each row gives **all successors remaining in this intersection**:

```text
state  successors
  1    12,13
  2    20,22
  4    (none)
  5    40
  6    48
  7    60,63
 12    (none)
 13    40
 20    (none)
 22    48
 40    2
 48    1
 60    (none)
 63    60,63
```

The initially accessible states within this table are \(1,2,4,5,6,7\); the terminal states within it are \(4,12,20,40,48,60\). The table is an exact finite reduction, not a sample of finitely many ladder lengths. A path starting at 7 must follow the self-loop at 63 and eventually exit to 60; it gives exactly the full-edge set, including the length-two case. State 4 gives \(L_1\). Every other allowed path starts at one of \(1,2,5,6\), traverses as needed the single directed six-cycle
\[
1\to13\to40\to2\to22\to48\to1,
\]
and exits to one of \(12,20,40,48\). Checking the four starting states and these exits gives, for \(n\ge2\), respectively \(2,2,4,2,2,4\) paths when \(n\bmod6\) is \(0,1,2,3,4,5\). The cyclic core advances six columns per turn. Inspection of each start-to-exit segment shows its number of selected edges equals the number of columns it covers; an extra full turn adds six columns and six selected edges. Thus every nontrivial open-ladder PED set has exactly \(n\) selected edges. The full set has \(3n-2\) edges. This proves the first polynomial.

For a circular ladder, a valid edge configuration is a closed walk of length \(n\) in the same 64-state graph, with its column bits determined uniquely by the successive second components. Exhaustively checking the arcs shows that the graph's only cyclic strongly connected components are the singleton loop at state 63 and the directed six-cycle displayed above. Every closed walk therefore lies entirely in one of these components. The singleton gives the full-edge set (weight \(3n\)); the six-cycle gives exactly six walks if and only if \(6\mid n\), each having weight \(n\) because one tour selects six edges across six columns. This proves the circular formula.

Finally, every nontrivial path or cycle in the displayed six-state component contains (or, in the two-column open boundary case, terminates in) a pair of adjacent selected edges; the explicit bit values of states \(13=(1,5)\), \(22=(2,6)\), \(40=(5,0)\), \(48=(6,0)\), \(12=(1,4)\), and \(20=(2,4)\) show such pairs directly. Hence none of the nontrivial PED sets is an induced matching. The full-edge set has adjacent edges for all cases under discussion, except \(L_1\). This proves the DIM assertion.

## Verification
The included standalone `verify.py` constructs the 64-state graph from the original edge-local implications, independently generates the 14-state accessibility table, checks both recurrent components, and evaluates exact weight enumerators for small orders. It separately enumerates subsets of the **actual graph edge set** (without using the transfer states) for open ladders through six rungs and circular ladders through six rungs. Both checks agree with the stated formulas. The independent direct enumeration is finite corroboration, whereas the complete 64-state reduction and closed-walk/path argument establish the result for every allowed order. To reproduce, run `python verify.py` in a standard Python 3 installation; no third-party packages are needed. Expected standard output is included in `verify_output.txt`.

## Relationship to prior work
Grippo, Lin, Moyano and Vera (2026) study the number of perfect edge dominating sets, prove extremal results for trees, forests and chordal graphs, and give linear-time counting algorithms for generalized series-parallel and chordal graphs. The open ladders are a natural generalized-series-parallel family, but that counting algorithm by itself does not state the closed periodic polynomial or the complete cardinality rigidity. Circular ladders provide a separate cyclic closure with the stronger six-divisibility threshold. The earlier paper by Grippo, Lin and Vera (2025/2026) examines minimum and counting algorithms for a different hereditary graph class and studies the existence problem for proper PED sets in graphs without DIMs. Our exact periodic presence/absence classification provides explicit examples in that setting. A published result about PED enumeration on bouquets of cycles concerns graphs with a single common cycle hub, structurally distinct from two-row ladders, and does not imply the present formula. General efficient edge domination theory supplies terminology but not these specific enumerations.

## Limitations
The theorem is restricted to exactly two rows and the specified open or ordinary cyclic boundary. It does not assert a formula for Möbius ladders, for strips of greater width, or for arbitrary generalized-series-parallel graphs. The originality assessment is based on the inspected primary literature, topical published-record searches, and claim comparison; unindexed or inaccessible earlier exact ladder formulas remain a bibliographic risk. Computational verification is not an independent mathematical audit.

## References
1. L. N. Grippo, M. C. Lin, V. Moyano and C. Vera, *Counting perfect edge dominating sets: extremal results and linear-time algorithms*, arXiv:2607.03894v1 (first posted 2026-07-04), https://arxiv.org/abs/2607.03894.
2. L. N. Grippo, M. C. Lin and C. Vera, *Perfect Edge Domination in P6-free Graphs and in Graphs Without Efficient Edge Dominating Sets*, arXiv:2509.04598 (first posted 2025-09-04), https://arxiv.org/abs/2509.04598.
3. M. C. Lin, V. Lozin, V. A. Moyano and J. L. Szwarcfiter, *Perfect Edge Domination: Hard and Solvable Cases*, arXiv:1705.08379 (2017), https://arxiv.org/abs/1705.08379.
