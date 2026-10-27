# One-symbol puncturing rigidity of de Bruijn cycles and the complete near-universal census

## Finding
Fix an alphabet \(\Sigma\) of \(q\ge 2\) labeled symbols and an integer \(n\ge 1\). Write \(N=q^n\). A cyclic word is **\(n\)-window-distinct** when its length-\(n\) cyclic windows, counted at every starting position, are pairwise different. A de Bruijn cycle has length \(N\) and all \(N\) possible windows; a **near-universal cycle** has length \(N-1\) and is \(n\)-window-distinct. Cycles are identified under rotation, never under letter relabeling.

**Classification.** Every near-universal cycle is missing exactly one length-\(n\) word, and that word must be a constant word \(a^n\) for a unique letter \(a\in\Sigma\). Conversely, every near-universal cycle is obtained by deleting one occurrence of \(a\) from the unique circular run \(a^n\) in some de Bruijn cycle. For each near-universal cycle missing \(a^n\), exactly \(q-1\) different de Bruijn cycles, considered modulo rotation, restore it by inserting \(a\).

**Exact edit fragility.** In *every* de Bruijn cycle, precisely \(qn\) of its \(N\) indexed single-symbol deletions leave an \(n\)-window-distinct cycle. These are exactly the \(n\) positions in each of the \(q\) unique constant length-\(n\) windows. They give exactly \(q\) distinct cyclic outcomes, distinguished by their respective missing constant windows. In particular, the success fraction for a uniformly selected deletion position is \(n/q^{n-1}\).

**Exact census.** The number of near-universal cycles up to rotation is
\[
C_q(n)=\frac{(q!)^{q^{n-1}}}{(q-1)q^{n-1}}.
\]
For a prescribed missing constant window \(a^n\), the number is \(C_q(n)/q\). This includes the boundary case \(n=1\).

## Assumptions and scope
All words are circular, windows may wrap across the chosen linear representation's boundary, and deletion joins the two new neighbors. The alphabet is fixed and labeled, \(q\ge2\), \(n\ge1\). The theorem addresses near-universal cycles with precisely one fewer symbol than a full de Bruijn cycle and no repeated length-\(n\) windows; it does not claim anything about arbitrary shorter cycles or multiple deletions. Numerical formulas count rotation classes, not linear representatives.

## Proof
**Step 1: the missing window is forced to be a loop.** Form the directed de Bruijn graph with vertices \(\Sigma^{n-1}\) and one edge labeled by each \(u\in\Sigma^n\), from its length-\(n-1\) prefix to its length-\(n-1\) suffix. For \(n=1\), take a single empty-word vertex with \(q\) labeled loops. Every vertex has indegree and outdegree \(q\).

Reading a circular length-\(N-1\) word with pairwise distinct length-\(n\) windows traces a closed directed trail of \(N-1\) distinct edges. Hence it uses every edge except one \(e\). The used edges form a balanced directed graph, and so do all edges together; therefore the omitted edge itself must contribute equal incoming and outgoing degrees at every vertex. A single directed edge has this property only if it is a loop. A length-\(n\) word with equal length-\(n-1\) prefix and suffix must have all letters equal, so \(e=a^n\) for a unique \(a\). This also proves, without any probabilistic assumption, that an arbitrary nonconstant window cannot be the sole missing window.

**Step 2: insertion and puncturing.** At vertex \(a^{n-1}\), the \(N-1\)-edge trail uses \(q-1\) outgoing edges because its only missing edge is the loop \(a^n\). There are exactly \(q-1\) occurrences of this vertex along the cyclic trail. Inserting the missing loop at any of these vertices gives a closed Eulerian traversal using every edge exactly once and hence a de Bruijn cycle. On the symbol string, this inserts one \(a\) at an occurrence of \(a^{n-1}\), creating the unique window \(a^n\). Conversely, removing any letter from the unique \(a^n\) run of a de Bruijn cycle removes this loop from its traversal and leaves exactly the other edges. This argument is valid for \(n=1\), where the vertex is the empty word and any of the \(q-1\) cyclic positions can receive the missing letter.

**Step 3: inequivalent insertions and exact deletion positions.** A near-universal cycle has no nontrivial rotational symmetry: a shorter period would repeat its length-\(n\) windows. For fixed missing \(a\), suppose two of the \(q-1\) insertion positions produced the same full de Bruijn necklace. That necklace has just one \(a^n\) loop. Align the necklaces by this loop and remove it: one obtains a rotation symmetry of the near-universal cycle carrying one insertion vertex to the other, which is impossible unless they were the same position. Thus there are exactly \(q-1\) distinct full cycles above each near-universal cycle.

Every full de Bruijn cycle contains one \(a^n\) window for each \(a\); the \(q\) constant windows are disjoint because their letters differ. If deleting a symbol preserves distinct windows, Step 1 says the missing edge must be \(a^n\) for some \(a\), so the deletion must intersect that unique window: an intact \(a^n\) window would remain after deleting a symbol outside it. Conversely, deleting any of the \(n\) positions within that window removes exactly its loop by Step 2. Therefore the set of successful indexed positions has size precisely \(qn\). All \(n\) deletions from the same constant run yield the same cyclic outcome, and the missing letter distinguishes outcomes from other runs.

**Step 4: exact enumeration.** The classical de Bruijn enumeration formula gives \(D_q(n)=(q!)^{q^{n-1}}/q^n\) rotation classes of full cycles, including \(D_q(1)=(q-1)!\). Double-count pairs consisting of a full cycle and a chosen deleted constant window. Every full cycle contributes \(q\) pairs; every near-universal cycle has exactly \(q-1\) distinct full-cycle preimages by Step 3. Hence \(qD_q(n)=(q-1)C_q(n)\), and the asserted closed form follows. Relabeling symmetry gives exactly \(C_q(n)/q\) cycles for each fixed missing letter. \(\square\)

## Verification
The bundled standalone `verify.py` exhaustively enumerates and canonicalizes all full and near-universal cycles for \((q,n)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(4,1)\). It checks the complete set of one-symbol deletion positions against the constant-window condition, every near-universal output against all possible near-universal cycles, and both counting formulas. Output for \((q,n)=(2,4)\): \(16\) full classes, \(32\) near-universal classes, and \(128\) successful indexed deletions aggregated over full classes. The exhaustive calculation is a finite cross-check, not the proof for arbitrary \(q,n\).

Run `python3 verify.py` with Python 3 and no external libraries.

## Relationship to prior work
The conventional *punctured* or *modified* de Bruijn construction—deleting a symbol from a constant window—is classical. Goresky and Klapper, Section 8.2.4, explicitly describe this construction and insertion into any occurrence of the constant \((n-1)\)-window, and quote the classical number of full de Bruijn cycles. Cameron, Gündoğan and Sawada study arbitrary-length cut-down cycles, including removing a one-symbol loop in their Section 4.2; Nellore and Ward study balanced arbitrary-length counterparts. These facts are background, **not claimed as new**. The present claim packages a converse for every one-deficit window-distinct cycle, a universal *if and only if* classification of successful single deletion positions in every full cycle, and the unrestricted labeled-alphabet enumeration of all such cycles via exact insertion multiplicity. The cited inspected treatments do not explicitly state this combined converse, fragility, and census theorem.

## Limitations
The proof concerns cyclic strings with one missing length-\(n\) window and not linear strings. No statement is made about more than one deletion. The full-cycle counting formula, the loop-deletion construction, and its inverse insertion rule are established background; a stronger unlocated theorem in the literature might imply the converse or this census. The complete asymptotic or algorithmic complexity of arbitrary-length cut-down cycles is not addressed. Finite checks do not establish originality or infinite validity; the graph argument proves the latter. Independent external validation has not been performed.

## References
1. B. Cameron, A. Gündoğan, and J. Sawada, *Cut-Down de Bruijn Sequences*, arXiv:2205.02815 (first public version May 5, 2022), especially Sections 1, 4.2, and 5.2. https://arxiv.org/abs/2205.02815
2. M. Goresky and A. Klapper, *Algebraic Shift Register Sequences* (2011), Section 8.2.4, “Punctured de Bruijn sequences,” p. 176. https://www.math.ias.edu/~goresky/pdf/algebraic0.pdf
3. A. Nellore and R. Ward, *Arbitrary-Length Analogs to de Bruijn Sequences*, arXiv:2108.07759 (2021), for context on arbitrary-length window sequences. https://arxiv.org/abs/2108.07759
4. N. G. de Bruijn, classical enumeration of complete de Bruijn cycles (1946), as recorded in Reference 2.
