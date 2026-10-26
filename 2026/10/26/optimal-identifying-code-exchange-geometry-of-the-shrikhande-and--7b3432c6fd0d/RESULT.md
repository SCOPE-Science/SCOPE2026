# Optimal identifying-code exchange geometry of the Shrikhande and \(4\times4\) rook graphs

## Finding
Let \(S\) be the Shrikhande graph and \(R=K_4\square K_4\) the four-by-four rook graph. Both are strongly regular with parameters \((16,6,2,2)\), but their **minimum closed-neighborhood identifying codes** have sharply different geometry.

The Shrikhande graph has \(\gamma_{\mathrm{ID}}(S)=5\), with exactly \(96\) minimum codes. Define \(H=2\mathbb Z_4\times2\mathbb Z_4\). Every minimum code, *uniquely*, is
\[
 C(q,e)=\big((q+H)\setminus\{q\}\big)\cup e,
 \qquad q\in\mathbb Z_4^2,\quad e\in E(S[N_S(q)]),
\]
where an edge \(e\) is identified with its two endpoints. The neighborhood \(S[N_S(q)]\) is a six-cycle, so the classification gives \(16\cdot6=96\) codes. The natural affine automorphism group acts transitively on them.

For each graph, define the **minimum-code exchange graph**: its vertices are minimum identifying codes, and two codes are adjacent precisely if one code is obtained from the other by replacing one selected vertex with one previously unselected vertex, keeping the minimum cardinality and identification property. Then
\[
 \mathcal E(S)\cong\bigsqcup_{i=1}^{16} C_6.
\]
Thus an optimum Shrikhande code can move within a six-cycle but can never reach a code in another component through optimum-preserving single-site exchanges.

For the rook graph \(\gamma_{\mathrm{ID}}(R)=6\), a **previously known** value. It has exactly \(2208\) minimum identifying codes; their exchange graph is connected, has \(28800\) edges, and has radius and diameter both equal to \(6\). Its vertex-degree distribution is \(192\) at degree \(18\), \(576\) at each of degrees \(20,26,33\), and \(288\) at degree \(30\). The two graphs therefore share all strongly regular parameters but differ in the optimum sensor count and connectedness of optimal sensor replacements.

## Assumptions and scope
Use additive coordinates \(V=\mathbb Z_4\times\mathbb Z_4\), identified with integers \(4x+y\) for \(x,y\in\{0,1,2,3\}\). Define \(S\) by the Cayley difference set
\[
 D=\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}\pmod4,
\]
and \(R\) by joining distinct vertices if they share at least one coordinate. All graphs are finite, undirected and loopless. For a graph \(G\), its closed neighborhood is \(N_G[v]=\{v\}\cup N_G(v)\). A code \(C\subseteq V\) is identifying if the \(16\) sets \(N_G[v]\cap C\), as \(v\) ranges over \(V\), are nonempty and pairwise distinct. The exchange operation allows any replacement vertex, not necessarily a neighbor of the removed code vertex. No statement is made for other graph sizes, Doob products, or alternative detection conventions.

## Proof
**Information-theoretic lower bound.** A code of cardinality \(m\) can give at most \(2^m-1\) distinct nonempty signatures. Distinguishing \(16\) graph vertices therefore requires \(m\ge5\). This immediately gives \(\gamma_{\mathrm{ID}}(S)\ge5\).

**Five-element construction.** The six neighbors of any \(q\in\mathbb Z_4^2\) induce a chordless six-cycle. For \(q=(0,0)\), a cycle order is
\[
(3,3),(3,0),(0,1),(1,1),(1,0),(0,3).
\]
Consider the code \(C=\{(0,2),(2,0),(2,2),(3,0),(3,3)\}\). Label its five elements \(a,b,c,d,e\) in that order. Its sixteen nonempty closed-neighborhood signatures in lexicographic vertex order \((0,0),(0,1),\ldots,(3,3)\) are the distinct strings

`de, ad, a, ae, b, c, ac, ab, bd, bc, ce, bcde, bde, abd, ace, cde`.

Hence \(C\) is an identifying code of size five. Translations together with the twelve linear automorphisms of \(\mathbb Z_4^2\) preserving \(D\) form \(192\) explicit affine automorphisms. Their action is transitive on pairs \((q,e)\), with \(e\) an edge of the local six-cycle. Thus every displayed \(C(q,e)\) is identifying. Moreover, every such code contains exactly three vertices of the unique parity coset \(q+H\), and two outside that coset; the outside two lie in *different* parity cosets. Consequently \(q\) and then \(e\) are uniquely recoverable from \(C(q,e)\); the \(96\) constructions are distinct.

**Exhaustive converse.** The finite condition for a subset \(B\subseteq V\) to be identifying is
\[
 (\forall v\in V)\; B\cap N[v]\ne\varnothing,
 \qquad(\forall v\ne w)\;B\cap(N[v]\mathbin\triangle N[w])\ne\varnothing.
\]
Here \(\triangle\) is symmetric difference. Index vertices as above, encode a subset by a sixteen-bit integer, and examine each of the exactly \(\binom{16}{5}=4368\) subsets with five selected vertices. The accompanying `verify_cpp.cpp` evaluates this predicate (equivalently, pairwise distinct nonzero signature bitmasks) on all such subsets and verifies that the accepted set is *identical* to the explicitly generated \(96\)-member geometric family. The independently written `verify_python.py` instead enumerates combinations of coordinate pairs and constructs actual set-valued closed-neighborhood signatures; its accepted set equals the same family. These are finite exhaustive enumerations over a fully specified universe, not a sample or an inference from the number \(96\) alone. The construction, lower bound, and converse classify **all** minimum Shrikhande codes.

**Exchange components in the Shrikhande graph.** The parity class containing three members of a minimum code is unchanged by a one-for-one replacement: every other parity class contains at most one member, so a single replacement cannot produce a new class with three members. If the absent vertex \(q\) in this parity class changed to another \(q'\), the outside pair would have to remain unchanged and form an edge common to both \(S[N(q)]\) and \(S[N(q')]\). For two distinct vertices in the same parity class, their common neighbors are an opposite pair at difference \((2,0)\), \((0,2)\), or \((2,2)\), hence are **not adjacent**. Thus \(q\) is invariant under an exchange. For fixed \(q\), codes correspond exactly to the edges of the six-cycle \(S[N(q)]\); replacement of one of the two extra vertices corresponds to two such edges sharing an endpoint. The exchange component is therefore the line graph of \(C_6\), again \(C_6\). There are exactly sixteen components, indexed by \(q\).

**The rook comparison.** The established theorem of Gravier–Moncel–Semri proves \(\gamma_{\mathrm{ID}}(K_n\square K_n)=\lfloor3n/2\rfloor\), giving the rook minimum \(6\) when \(n=4\). Independently, both packaged programs examine every subset of the rook graph up to size six (including all \(\binom{16}{6}=8008\) six-sets), find none of smaller size, and obtain exactly \(2208\) six-codes. Each program enumerates all \(2208\) states; it joins two if their intersection contains exactly five vertices, which is equivalent to a single replacement. They independently obtain \(28800\) undirected exchange edges and one component. An exhaustive breadth-first search **from every one of the 2208 states**, with all exchanges included, gives eccentricity \(6\) at each state. This establishes both radius and diameter \(6\); no bound is extrapolated beyond the finite state space.

## Verification
The self-contained C++17 file `verify_cpp.cpp` and Python 3 file `verify_python.py` have no downloaded graph data or third-party library dependencies. From a directory containing the two scripts, run:

```sh
g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_cpp.cpp -o verify_cpp
./verify_cpp
python3 verify_python.py
```

Both scripts first construct \(S\) and \(R\) from the adjacency definitions and check degree six and exactly two common neighbors for every unordered vertex pair. The C++ implementation exhaustively examines all bitmasks through the minimum size, generates exchange neighbors by a one-bit removal plus a one-bit insertion, and computes every component and vertex eccentricity. The Python implementation independently enumerates size-specific combinations, tests unordered-set signatures, builds exchange edges by **pairwise** code-set intersection, and performs its own graph searches. Both check the geometric Shrikhande classification; Python also verifies a single orbit under the \(192\) coordinate affine symmetries. Outputs from actual executions are retained in `cpp_output.txt` and `python_output.txt`. The command exits unsuccessfully if a claimed count or structural equality fails. This establishes all finite statements by replayable exhaustive checks rather than treating precomputed logs as proof.

## Relationship to prior work
Gravier, Moncel and Semri (2008) determined the minimum identifying-code cardinality for square Cartesian products of cliques. Their theorem already yields \(\gamma_{\mathrm{ID}}(R)=6\); this known value is background here. Their paper does not analyze the Shrikhande graph or the number and exchange geometry of the \(4\times4\) rook minima. Gravier, Parreau, Rottey, Storme and Vandomme (2015) study identifying codes in vertex-transitive and strongly regular graphs, discuss the clique Cartesian products, and derive fractional and asymptotic bounds; their inspected relevant sections do not imply this finite geometric classification or reconfiguration comparison.

Other published calculations distinguish this strongly regular pair using *independence-complex* or *Čech-complex* homotopy. Those are different invariants: they neither count closed-neighborhood identifying codes nor determine their one-for-one replacement adjacency. The present result complements, rather than follows from, those distinctions. The original identifying-code framework dates to Karpovsky, Chakrabarty and Levitin (1998).

## Limitations
The theorem concerns precisely the two specified sixteen-vertex graphs, ordinary closed-neighborhood identifying codes, and unrestricted fixed-cardinality single-vertex exchanges. The rook minimum size is prior art. The graph-specific enumerations provide no formula for higher-order Doob graphs or larger rook graphs, and disconnectedness under these exchanges does not rule out transformations that temporarily use more sensors. A comprehensive search cannot exclude equivalent unindexed finite tables or future independent priority disputes. Independent external scientific validation has not been performed.

## References
1. S. Gravier, J. Moncel and A. Semri, *Identifying Codes of Cartesian Product of Two Cliques of the Same Size*, Electronic Journal of Combinatorics **15** (2008), #N4, published 2008-02-11, DOI: 10.37236/879. Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v15i1n4/pdf/.
2. S. Gravier, A. Parreau, S. Rottey, L. Storme and E. Vandomme, *Identifying Codes in Vertex-Transitive Graphs and Strongly Regular Graphs*, Electronic Journal of Combinatorics **22** (2015), #P4.6, DOI: 10.37236/5256. Author full text: https://orbi.uliege.be/bitstream/2268/186885/1/identifying_codes_arXiv.pdf.
3. M. G. Karpovsky, K. Chakrabarty and L. B. Levitin, *On a New Class of Codes for Identifying Vertices in Graphs*, IEEE Transactions on Information Theory **44** (1998), 599–611.
4. A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, sections on strongly regular graphs and the exceptional Shrikhande/rook pair. https://aeb.win.tue.nl/2WF02/spectra.pdf.
