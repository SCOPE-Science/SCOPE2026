# Exact degree-mixing census of cycle mutual-visibility reconfiguration layers

## Finding
For every integer \(n\ge3\), let \(L_n\) be the **three-token layer** of the mutual-visibility reconfiguration graph of the simple cycle \(C_n\). Its vertices are the mutually visible three-element vertex sets; an edge slides one token to an unoccupied adjacent cycle vertex, provided mutual visibility remains true. Write \(N_d\) for the number of vertices of degree \(d\) in \(L_n\), and \(E_{d,e}\) for the number of its (undirected) edges with endpoint-degree multiset \(\{d,e\}\). Every entry not explicitly listed below is zero.

For **even** \(n=2h\ge8\), the complete degree census is
\[
N_3=2n,\qquad N_4=n(h-3),\qquad N_6=\frac{n(h-1)(h-2)}6,
\]
and its complete endpoint-degree edge matrix is

| Degree pair | Exact number of edges |
|---|---:|
| \((3,3)\) | \(n\) |
| \((3,4)\) | \(2n\) |
| \((3,6)\) | \(2n\) |
| \((4,4)\) | \(n(h-4)\) |
| \((4,6)\) | \(2n(h-3)\) |
| \((6,6)\) | \(n(h-3)(h-2)/2\) |

For **odd** \(n=2h+1\ge7\), the degree census is
\[
N_2=n,\qquad N_4=n(h-2),\qquad N_6=\frac{n(h-2)(h-3)}6,
\]
and the edge matrix is

| Degree pair | Exact number of edges |
|---|---:|
| \((2,4)\) | \(2n\) |
| \((4,4)\) | \(n(h-2)\) |
| \((4,6)\) | \(2n(h-3)\) |
| \((6,6)\) | \(n(h-3)(h-4)/2\) |

The remaining complete small-cycle data are:

| Cycle order | Nonzero degree counts | Nonzero edge-type counts |
|---|---|---|
| \(n=3\) | \(N_0=1\) | none |
| \(n=4\) | \(N_2=4\) | \(E_{2,2}=4\) |
| \(n=5\) | \(N_2=5\) | \(E_{2,2}=5\) |
| \(n=6\) | \(N_3=12,\ N_6=2\) | \(E_{3,3}=12,\ E_{3,6}=12\) |

In particular, with \(h=\lfloor n/2\rfloor\), the number of legal three-token slides, counted as undirected edges, is
\[
|E(L_n)|=\begin{cases}
\dfrac n2(h^2+h-4),&n=2h\ge4,\\[2pt]
\dfrac n2h(h-1),&n=2h+1\ge3.
\end{cases}
\]
The known connectivity of these layers gives a simple random-walk interpretation. For even \(n\ge8\), the stationary probability of all degree-three configurations together is exactly \(6/(h^2+h-4)\); for odd \(n\ge7\), the stationary probability of the degree-two configurations is exactly \(2/[h(h-1)]\). Both masses decay quadratically with the cycle order.

## Assumptions and scope
Every graph is finite, simple and undirected; \(C_n\) has its standard cyclic adjacency, with \(n\ge3\). A subset \(S\) is *mutually visible* when each pair of vertices in \(S\) can be joined by a shortest path having no internal vertex from \(S\). Within \(L_n\) all vertex sets have exactly three members; the only allowed moves are token slides, not additions/removals. All counts distinguish positions on the labelled cycle and count undirected configuration edges once. Degrees refer to the layer \(L_n\), not the entire reconfiguration graph. No restriction to configurations up to graph automorphisms is imposed.

## Proof
**1. Gap model.** Orient the cycle to define an order. Three occupied vertices have strictly positive cyclic gap lengths \((a,b,c)\), adding to \(n\). Put \(h=\lfloor n/2\rfloor\). Between any consecutive occupied pair, the unique arc with no third occupied vertex is a geodesic precisely when its gap length is at most \(h\). Therefore mutual visibility is equivalent to
\[
a,b,c\in\{1,\ldots,h\},\qquad a+b+c=n.\tag{1}\]
If a token lies between gaps \(a\) and \(b\), a slide one step into gap \(a\) is possible precisely when \(a\ge2\) and \(b<h\), since the new gaps are \(a-1,b+1\). Symmetrically a step into \(b\) is possible precisely when \(b\ge2\) and \(a<h\). Thus the layer degree of a gap configuration is the exact expression
\[
\delta(a,b,c)=\sum_{\text{cyclic adjacent }(u,v)}
\left(\mathbf1_{u\ge2,\ v<h}+\mathbf1_{v\ge2,\ u<h}\right),\tag{2}
\]
where the sum ranges over the three cyclic consecutive gap pairs. This counts each legal token slide once. Equation (1) forces that, for even \(n=2h\ge6\), the only gap types are: one gap \(h\) and one gap \(1\) (degree \(3\)); one gap \(h\), with the other two at least \(2\) (degree \(4\)); or no gap \(h\) (degree \(6\)). For odd \(n=2h+1\ge5\), the types are: two gaps \(h\) and one gap \(1\) (degree \(2\)); one gap \(h\), with the other two at least \(2\) (degree \(4\)); or no gap \(h\) (degree \(6\)). Whenever the last type occurs all gaps are at least two. The cases \(n=3,4\) are checked directly.

**2. Degree counts.** An admissible occupied triple has exactly three ways to choose a distinguished occupied vertex. Conversely, there are \(n\) choices for the distinguished vertex position for each ordered gap triple satisfying (1). Consequently, the number of occupied triples is \(n/3\) times the number of such ordered compositions. Elementary upper-bounded stars-and-bars gives
\[
\#\{(a,b,c)\text{ satisfying (1)}\}=\begin{cases}
(h-1)(h+4)/2,&n=2h,\\
h(h+1)/2,&n=2h+1.
\end{cases}\tag{3}
\]
For even \(n=2h\ge6\), degree-three configurations have ordered gaps a permutation of \((h,1,h-1)\), giving \(2n\) configurations. Degree-four configurations have one gap \(h\) and an ordered pair of other gaps at least \(2\) summing to \(h\); there are \(h-3\) choices per placement of \(h\), giving \(n(h-3)\). Subtract these from (3) to obtain \(N_6=n(h-1)(h-2)/6\). For odd \(n=2h+1\ge5\), the \(n\) configurations with gaps \((h,h,1)\) in cyclic order have degree two. The remaining degree-four configurations have gap \(h\) and an ordered pair of at-least-two gaps summing to \(h+1\), yielding \(n(h-2)\) configurations. Subtraction gives \(N_6=n(h-2)(h-3)/6\). The exceptional degree count for \(n=4\) follows from gaps \((2,1,1)\).

**3. Edge-type census for odd cycles.** Suppose \(n=2h+1\ge7\). From a degree-two configuration, both legal moves lead to degree-four configurations. Hence \(E_{2,4}=2n\). A degree-four configuration has gaps \((h,b,c)\) in some cyclic order with \(2\le b,c\le h-1\) and \(b+c=h+1\). Exactly four moves are admissible: either donate from gap \(h\) to one neighboring gap, or move one unit between \(b\) and \(c\) in either direction. Exactly **two** of those four moves lead to another degree-four configuration. To verify this at the endpoints, if \(b=2,c=h-1\) (or reversed), one move reaches degree two, two reach degree four, and one reaches degree six; when \(h=3\) and \(b=c=2\), two reach degree two and two reach degree four. In the interior \(b,c\ge3\), the two transfers between \(b\) and \(c\) preserve degree four, and the two donations from \(h\) reach degree six. Thus \(E_{4,4}=N_4=n(h-2)\). The degree-four and degree-six handshake equations now uniquely determine
\[
E_{4,6}=4N_4-E_{2,4}-2E_{4,4}=2n(h-3),
\quad E_{6,6}=\frac{6N_6-E_{4,6}}2
=\frac{n(h-3)(h-4)}2.
\]
This proves every odd-cycle entry.

**4. Edge-type census for even cycles.** Suppose \(n=2h\ge8\). A degree-three configuration has gaps cyclically \((h,1,h-1)\). It has exactly three legal slides, and their resulting configurations have degrees \(3,4,6\), one of each. Therefore
\[
E_{3,3}=\frac{N_3}{2}=n,\quad E_{3,4}=N_3=2n,\quad E_{3,6}=N_3=2n.
\]
For degree four, exactly one gap is \(h\), and the ordered neighboring gaps are \((b,h-b)\) with \(2\le b\le h-2\). There are exactly \(n\) configurations for each such \(b\). A legal slide joins another degree-four configuration precisely when a unit is transferred between these two nonmaximal gaps without creating a gap \(1\). Hence the number of degree-four neighbors of this configuration equals \(\mathbf1_{b>2}+\mathbf1_{b<h-2}\). Summing over \(b\) and dividing by two gives
\[
E_{4,4}=\frac n2\sum_{b=2}^{h-2}
\bigl(\mathbf1_{b>2}+\mathbf1_{b<h-2}\bigr)=n(h-4).
\]
The handshake equations on the degree-four and degree-six classes give
\[
E_{4,6}=4N_4-E_{3,4}-2E_{4,4}=2n(h-3),\qquad
E_{6,6}=\frac{6N_6-E_{3,6}-E_{4,6}}2
=\frac{n(h-3)(h-2)}2.
\]
For \(n=6\), the gap types are permutations of \((3,1,2)\) (twelve degree-three configurations) and \((2,2,2)\) (two degree-six configurations). Their slides give twelve degree-three/degree-three edges and twelve degree-three/degree-six edges. For \(n=3,4,5\), direct inspection yields the table.

**5. Consequences.** Summing the edge-type entries proves the displayed edge-count formula, including its small cases. For a simple random walk on a finite connected undirected graph, the stationary probability of a vertex is proportional to its degree. The established connectivity of each \(L_n\) (Fresán-Figueroa–Goldfeder–Lozano-Piña, Theorem 6.3) therefore yields the displayed exact boundary stationary masses by dividing the total boundary degree by \(2|E(L_n)|\).

## Verification
The standalone `verify.py` uses Python standard-library exact integer arithmetic. Run `python verify.py`. It (i) checks the composition and clockwise-slide formulas against the complete degree and joint-degree table for every \(3\le n\le180\); (ii) independently constructs the original cycle, tests all three visibility pairs of every candidate triple using breadth-first shortest-path comparisons, builds the induced token-slide graph, and checks the same counts for every \(3\le n\le27\); (iii) checks all handshake identities and parity boundaries. An observed `VERIFY_OK` confirms these finite checks, which independently corroborate the all-order proof; they are not substituted for it.

## Relationship to prior work
Fresán-Figueroa, Goldfeder, and Lozano-Piña (2026, arXiv:2610.24324v1) introduce the token-addition/removal and token-sliding reconfiguration graph, prove the cycle gap criterion (their Lemma 6.2), and prove connectivity of all cycle layers (their Theorem 6.3). The present theorem is an enumerative refinement: it supplies the complete degree distribution, joint endpoint-degree edge counts, and boundary stationary mass in the nontrivial maximum layer. Their gap characterization establishes feasible local moves but does not state these degree-mixing counts in the relevant inspected section.

Tonny K B and Shikhi M (2025, arXiv:2507.01851) study visibility polynomials, which count configurations by their cardinality, not endpoint degrees of token-slide transitions. A previously recorded exact distance result for visible triples on cycles establishes isometry and a pairwise reconfiguration distance formula but does not state or enumerate this joint-degree mixing matrix. These distinctions concern **claims and their implications**, not merely different titles; general gap or distance descriptions underlie the proof but do not directly provide the closed polynomial edge-type census without the boundary-transition count.

## Limitations
The theorem concerns the maximum-cardinality (three-token) visibility layer of ordinary cycles, not all layers of other graph families. It gives one-step transition degree counts and a random-walk stationary-mass consequence, not a mixing-time bound or a spectral-gap estimate. The explicit edge-mixing census has not received independent mathematical audit. Historical priority is provisional: some earlier general reconfiguration enumerations and parts of related papers were not fully available for comparison.

## References
1. J. A. Fresán-Figueroa, I. A. Goldfeder, A. Lozano-Piña, *Reconfiguration graphs of mutual-visibility sets*, arXiv:2610.24324v1 (first public 2026-10-16), especially Lemma 6.2 and Theorem 6.3. https://arxiv.org/abs/2610.24324
2. Tonny K B and Shikhi M, *On the Visibility Polynomial of Graphs*, arXiv:2507.01851v1 (2025-07-02). https://arxiv.org/abs/2507.01851
