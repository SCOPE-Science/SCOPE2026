# Sharp unrestricted finite-variable classification of connected Ferrers graphs

## Finding
A **connected Ferrers graph** means a finite connected, simple, undirected, bipartite graph with at least one edge and nested open neighborhoods within each bipartition side (equivalently, a connected bipartite graph with no induced \(2K_2\)). The only relational symbols are equality and adjacency; there are no counting quantifiers.

Every such graph has a representation \(F(\mathbf a,\mathbf b)\), where \(m\ge1\), \(\mathbf a=(a_1,\ldots,a_m)\), \(\mathbf b=(b_1,\ldots,b_m)\), and every entry is a positive integer. There are independent vertex blocks \(A_i\), \(B_j\), of sizes \(a_i\), \(b_j\), and all cross-edges are given by
\[
E(A_i,B_j)\quad\Longleftrightarrow\quad j\le i.
\]
The representation is unique up to the simultaneous transformation \((\mathbf a,\mathbf b)\mapsto(\operatorname{rev}(\mathbf b),\operatorname{rev}(\mathbf a))\).

**Theorem.** For every integer \(k\ge3\) and every two connected Ferrers graphs \(G=F(\mathbf a,\mathbf b)\), \(H=F(\mathbf a',\mathbf b')\), ordinary first-order logic with at most \(k\) reusable variables and unrestricted quantifier depth satisfies
\[
G\equiv_{\mathrm{FO}^{k}}H
\quad\Longleftrightarrow\quad
m=m'\ \text{and}\ 
(\operatorname{clip}_k(\mathbf a),\operatorname{clip}_k(\mathbf b))
\sim
(\operatorname{clip}_k(\mathbf a'),\operatorname{clip}_k(\mathbf b')),
\]
where \(\operatorname{clip}_k(t)=\min(t,k)\), applied entrywise, and \(\sim\) means equality or simultaneous side-exchange and reversal.

For each fixed number \(m\) of levels, the number of distinct unrestricted-depth \(k\)-variable theories is exactly
\[
\boxed{\ N_k(m)=\frac{k^{2m}+k^m}{2}\ }.
\]
Each relative theory has a unique smallest graph representative up to isomorphism, obtained by truncating every block size at \(k\). The hierarchy is strict at every width \(k\ge3\): \(K_{1,k}\equiv_{\mathrm{FO}^{k}}K_{1,k+1}\) but \(K_{1,k}\not\equiv_{\mathrm{FO}^{k+1}}K_{1,k+1}\).

## Assumptions and scope
The graphs are finite and have no named bipartition, order, degree, or counting operators. Isolated vertices are excluded by connectedness together with the requirement of an edge. The integer \(m\) is unbounded, as are all block sizes and quantifier depths. The equivalence symbol refers to *all* first-order sentences using at most \(k\) distinct variable names, with unlimited rebinding of those names.

The classical nested-neighborhood definition gives the canonical staircase: arrange the distinct neighborhoods of vertices in one side as a strict increasing sequence \(N(A_1)\subsetneq\cdots\subsetneq N(A_m)\). Every column vertex belongs to exactly one of the nonempty difference sets \(N(A_j)\setminus N(A_{j-1})\), taking \(N(A_0)=\varnothing\). These are the blocks \(B_j\); their neighborhoods are \(A_j\cup\cdots\cup A_m\). Connectedness ensures all blocks are nonempty. The graph admits precisely the two side choices, accounting for the displayed reversal.

## Proof
**Step 1: three-variable definability of the neighborhood preorder.** For vertices \(x,y\) let \(x\prec y\) denote proper inclusion \(N(x)\subsetneq N(y)\), expressed by the three-variable formula
\[
\bigl[\forall z\,(E(x,z)\Rightarrow E(y,z))\bigr]
\land\bigl[\exists z\,(E(y,z)\land\neg E(x,z))\bigr].
\]
Both neighborhoods are nonempty. Since neighborhoods of opposite-side vertices lie in disjoint sides, proper inclusion can occur only inside a single bipartition side. In the staircase representation the \(\prec\)-rank of every vertex in \(A_i\) is \(i-1\), and of every vertex in \(B_j\) it is \(m-j\).

For each fixed nonnegative \(r\), define \(P_0(x)=\top\) and
\[
P_{r+1}(x)=\exists y\,(y\prec x\land P_r(y)).
\]
This is a formula with only three reusable variable names, by renaming the bound variables in the recursive occurrence of \(P_r(y)\); its sole free variable is \(x\). It says that the rank of \(x\) is at least \(r+1\). Thus \(R_r(x):=P_r(x)\land\neg P_{r+1}(x)\) defines exactly the two open-neighborhood twin blocks \(A_{r+1}\) and \(B_{m-r}\) when \(0\le r<m\), and no vertices otherwise. Sentences \(\exists x\,P_r(x)\) determine \(m\) exactly.

**Step 2: counting within a twin class with at most \(k\) variables.** The twin relation
\[
T(x,y):=\forall z\,(E(x,z)\leftrightarrow E(y,z))
\]
uses three variable names. For any \(1\le s\le k\), define \(C_s(x)\) to say that there are at least \(s\) distinct vertices in the twin class of \(x\). Choose \(x=x_1,x_2,\ldots,x_s\) pairwise distinct and require \(T(x_i,x_j)\) for each pair. In each conjunct one can quantify a variable name other than \(x_i,x_j\), locally shadowing one of the other selected variables. Consequently the entire formula uses at most \(\max(3,s)\le k\) distinct variable names. For \(s=1\) the formula is a tautology. This variable-shadowing argument does **not** introduce a counting quantifier.

For each rank \(r\) and threshold \(s\le k\), the sentences
\[
\exists x\,(R_r(x)\land C_s(x)),
\qquad
\forall x\,(R_r(x)\Rightarrow C_s(x))
\]
respectively test whether at least one, or both, of the two rank-\(r\) twin blocks have size at least \(s\). Taken over \(s=1,\ldots,k\), they determine the unordered pair of their clipped sizes.

**Step 3: recovering one globally consistent side orientation.** Suppose some rank \(r\) has unequal clipped block sizes. Then for a suitable \(s\le k\), exactly one of its two twin classes satisfies \(C_s\). The unary formula \(M(x):=R_r(x)\land C_s(x)\) picks precisely that class. In a connected Ferrers graph two vertices lie on the same bipartition side exactly if they have a common neighbor:
\[
S(x,y):=\exists z\,(E(x,z)\land E(y,z)).
\]
Define \(U(x):=\exists y\,(M(y)\land S(x,y))\). This is again a \(k\)-variable unary formula: the sole free occurrence of \(x\) in \(S(x,y)\) does not prevent the local bound-variable reuse within \(M(y)\). Hence \(U\) marks one complete bipartition side. For every rank \(j\) and \(s\le k\), the sentence
\[
\exists x\,(U(x)\land R_j(x)\land C_s(x))
\]
recovers the clipped size of the rank-\(j\) class on that marked side. The complementary side is already determined by the unordered pairs from Step 2. Thus a global orientation is recovered up to the single admissible side exchange. If no rank has unequal clipped sizes, every rank pair is symmetric, so the same unordered rank data already specify the clipped representation unambiguously. This proves the **necessity** of the stated condition.

**Step 4: an unrestricted-depth pebble strategy.** Suppose the two clipped representations agree after a possible global reversal. Match their corresponding \(2m\) classes. In the ordinary \(k\)-pebble game, Duplicator maintains that matching and a bijection on the currently pebbled distinct vertices of each class. Before responding to any placement, one pebble has been freed, so at most \(k-1\) distinct vertices remain pebbled in total. If a class has fewer than \(k\) vertices on either side, the two sizes are exactly equal; if both sizes are at least \(k\), an unused counterpart exists. Since all adjacencies are determined by class indices and equality, every position is a partial isomorphism. The strategy works indefinitely, establishing **sufficiency** for all quantifier depths.

**Step 5: exact count, minimality, and sharpness.** The truncated data at level count \(m\) are \(2m\) symbols from a \(k\)-letter alphabet, modulo one involution that reverses the sequence and exchanges sides. The involution fixes exactly \(k^m\) strings, out of \(k^{2m}\). Burnside's lemma yields \(N_k(m)=(k^{2m}+k^m)/2\). Replacing each block of size above \(k\) by exactly \(k\) vertices is the unique size-minimizing representative of that orbit. Finally, \(K_{1,k}\) and \(K_{1,k+1}\) have the same truncated data at width \(k\), but not width \(k+1\), proving strictness for every \(k\ge3\).

## Verification
Two standalone standard-library Python programs are included. `verify_structure.py` constructs 819 positive-block staircase graphs (levels one to three, each block size in \(\{1,2,3\}\)), checks connectedness, symmetry, all open-neighborhood twin classes and the rank-two-class property, and independently enumerates Burnside orbit counts for \(k=2,3,4\) and \(m=1,2,3\). Its recorded output ends `STRUCTURE_PASS`.

`verify_logic.py` computes stable **set-based** (not counting-multiset) \(k\)-tuple replacement colors, hence finite \(k\)-variable formula types, on 524 additional canonical graph instances. It checks the predicted three-variable partitions at levels one, two and three, and the sharp \(k\)-versus-\(k+1\) star-pair examples for \(k=3,4\). The recorded output ends `LOGIC_PASS`. Both scripts were run from the included source files; output text is embedded as independent evidence. These are finite corroborations; the unrestricted theorem is proved in Steps 1–5.

## Relationship to prior work
Hammer, Peled, and Sun introduced difference graphs. Ehrenborg and van Willigenburg treat Ferrers graphs through spanning-tree, Hamiltonian-path, and chromatic enumerators; Burns provides bijective enumerative proofs. These sources give the canonical graph family, not the unrestricted finite-variable logical equivalence criterion. Grohe and Otto supply the general plain-pebble-game correspondence but do not give this staircase classification. Fortin's three-variable property concerns **structures carrying a linear order** together with suitably monotone relations; that richer signature does not imply the present classification in the bare graph signature, which has unbounded twin multiplicities.

Related published classifications for complete multipartite and threshold graphs do not subsume the result: every connected Ferrers graph with at least two staircase levels contains an induced \(P_4\), whereas complete multipartite and threshold graphs have no induced \(P_4\). An earlier rank-three census of chain graphs with named bipartition sides remains a bounded-depth, enriched-signature result; it does not determine the present unrestricted-depth pure-graph equivalence. Previous bounded-quantifier-rank work on half-graphs is likewise logically different from unrestricted-depth fixed-variable equivalence. The key additional work here is recovering a global, unnamed side orientation while respecting the exact \(k\)-variable counting cutoff.

## Limitations
The statement concerns connected Ferrers graphs with an edge; it does not include isolated vertices or disconnected unions. It does not classify widths one and two, signatures with a named bipartition or linear order, counting logic, or arbitrary bipartite graphs. Literature searches and inspections did not establish absolute historical priority; a broad unlocated decomposition theorem could conceivably imply the result. Finite computational cases are supporting evidence rather than a substitute for the proof. No independent mathematical audit has been performed.

## References
1. P. L. Hammer, U. N. Peled and X. Sun, *Difference graphs*, Discrete Applied Mathematics **28** (1990), 35–44, DOI: 10.1016/0166-218X(90)90092-Q.
2. J. Burns, *Bijective Proofs for “Enumerative Properties of Ferrers Graphs”*, arXiv:math/0312282, first posted 15 December 2003.
3. R. Ehrenborg and S. van Willigenburg, *Enumerative properties of Ferrers graphs*, Discrete & Computational Geometry **32** (2004), 481–492; arXiv:0706.2918, posted 20 June 2007.
4. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990, first posted 9 April 2012.
5. M. Fortin, *FO = FO3 for Linear Orders with Monotone Binary Relations*, arXiv:1904.00189, posted 30 March 2019.
