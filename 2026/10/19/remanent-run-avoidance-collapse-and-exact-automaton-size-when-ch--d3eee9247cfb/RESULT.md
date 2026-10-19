# Remanent run-avoidance collapse and exact automaton size when \(\chi(G)=\omega(G)\)

## Finding

Let \(G\) be a finite, **nonempty**, simple undirected graph, with clique number \(\omega(G)\) and chromatic number \(\chi(G)\). For an orientation \(H\) of \(G\), form the finite automaton whose states are the vertices, all initial and accepting; a symbol \(+\) follows a directed edge, while \(-\) traverses one backwards. Write \(L(H)\) for its language, and define
\[
\operatorname{Rem}(G)=\bigcap_{H\text{ an orientation of }G}L(H).
\]

**Theorem.** If \(\chi(G)=\omega(G)=k\ge1\), then
\[
\boxed{\operatorname{Rem}(G)=\{w\in\{+,-\}^{*}:\; +^k\text{ and }-^k\text{ are both absent as contiguous factors of }w\}.}
\]
The minimum number of states in a **complete deterministic finite automaton** accepting this language is exactly \(2k\). In particular, every finite perfect graph of chromatic number \(k\) has this same complete remanent language and minimal deterministic state count. Perfectness is sufficient, not necessary: equality of the two invariants for the graph itself is the precise hypothesis used here.

Let \(a_m=|\operatorname{Rem}(G)\cap\{+,-\}^{m}|\). Then
\[
\boxed{\sum_{m\ge0}a_mz^m=\frac{1+z+z^2+\cdots+z^{k-1}}{1-z-z^2-\cdots-z^{k-1}}.}
\]
For \(k=1\), both sums after the constant term are empty, so this fraction equals \(1\). For \(k\ge2\) and \(m\ge1\), \(a_m\) is twice the number of compositions of \(m\) with each part between \(1\) and \(k-1\).

## Assumptions and scope

Graphs are finite, nonempty, loopless, without multiple edges, and need not be connected. All orientations of their edges are included in the intersection. Walks may revisit vertices. The empty word is accepted. Both directional input signs are distinct letters, and all graph vertices are initial **and** final. The formula concerns deterministic recognition of the resulting language, not the minimum size of an oriented graph or a nondeterministic graph representation.

The hypothesis is \(\chi(G)=\omega(G)\) for the **whole** graph. It does not assert that every induced subgraph also satisfies equality, although every perfect graph does. No converse is claimed for graphs with \(\chi(G)>\omega(G)\).

## Proof

**1. A clique–colouring sandwich.** Denote by \(T_k\) the transitive tournament on \(\{0,\ldots,k-1\}\), with arc \(i\to j\) whenever \(i<j\). Fix a clique on \(k\) vertices. In any orientation \(H\) of \(G\), its induced tournament either has a directed cycle or is acyclic. In the first case, every word over \(\{+,-\}\) labels a walk around that directed cycle (moving with an edge on \(+\) and against it on \(-\)). In the second case, every acyclic tournament is transitive and hence isomorphic to \(T_k\). Thus, in either case,
\[
L(T_k)\subseteq L(H).
\]
As this holds for every orientation, \(L(T_k)\subseteq\operatorname{Rem}(G)\).

Conversely, a proper \(k\)-colouring assigns a colour in \(\{0,\ldots,k-1\}\) to every vertex. Orient each edge from lower colour to higher colour. The colouring map is a direction-preserving graph homomorphism into \(T_k\), taking every signed walk to a signed walk. Hence the language of this orientation is contained in \(L(T_k)\), and so
\[
\operatorname{Rem}(G)\subseteq L(T_k).
\]
We conclude that \(\operatorname{Rem}(G)=L(T_k)\). The argument also gives the general sandwich \(L(T_{\omega(G)})\subseteq\operatorname{Rem}(G)\subseteq L(T_{\chi(G)})\) for every nonempty simple graph.

**2. Exact transitive-tournament language.** A block of \(k\) consecutive \(+\) letters cannot be read in \(T_k\), because each step must strictly increase its vertex rank. A block of \(k\) consecutive \(-\) letters cannot be read either. Because acceptance is factor-closed (all states initial and accepting), no accepted word contains either forbidden block.

Conversely, take a nonempty signed word whose maximal monochromatic runs all have lengths between \(1\) and \(k-1\). If the first run is positive, begin its walk at rank \(0\); if negative, begin at rank \(k-1\). A positive run of length \(r\) can traverse from \(0\) to \(k-1\) in exactly \(r\) steps: jump first from \(0\) to \(k-r\), then take \(r-1\) unit steps upward. A negative run can traverse in exactly \(r\) steps from \(k-1\) to \(0\) by reversing the analogous path. Since the signs of maximal runs alternate, their endpoints agree at every junction. The concatenation is an accepting walk. If \(k=1\), no nonempty walk exists, agreeing with the forbidden-run condition; the empty word is accepted. This proves the stated description.

**3. Minimal deterministic state count.** The usual run-length automaton has one start state, \(k-1\) states remembering a final positive run of length \(1,\ldots,k-1\), \(k-1\) analogous negative-run states, and one rejecting sink. It is complete and recognizes precisely the language proved above, giving \(2k\) states (also for \(k=1\), when only the start and sink remain).

Every state is reachable: the start by the empty word, the positive and negative run states by \(+^r\) and \(-^r\), and the sink by \(+^k\). The sink is distinguished from every other state by the empty continuation. Two positive-run states of lengths \(r<s\) are distinguished by \(+^{k-s}\): this suffix kills the state of length \(s\) but not the one of length \(r\); the same reasoning works for two negative-run states. A positive-run state of length \(r\) is distinguished from every negative-run state and from the start by \(+^{k-r}\): it reaches the sink from the positive state but is accepted from either of the other two. Finally, a negative-run state is distinguished from the start by \(-^{k-r}\) for its corresponding length \(r\). All states therefore lie in distinct Myhill–Nerode classes, proving the lower bound \(2k\).

**4. Counting.** For \(m>0\), choose the first sign in \(2\) ways and then uniquely specify the lengths of alternating maximal runs, each in \(\{1,\ldots,k-1\}\). Writing \(S(z)=z+\cdots+z^{k-1}\), the ordinary generating function is \(1+2\sum_{j\ge1}S(z)^j=(1+S(z))/(1-S(z))\). This gives the claimed exact formula.

**5. A genuine boundary outside the equality class.** The five-cycle has \(\omega(C_5)=2\) and \(\chi(C_5)=3\). Orient its edges as \(0\to1,\;2\to1,\;2\to3,\;4\to3,\;0\to4\). Starting from all vertices, the successive reachable sets when reading \(++-++\) are
\[
\{0,1,2,3,4\},\quad\{1,3,4\},\quad\{3\},\quad\{2,4\},\quad\{1,3\},\quad\varnothing.
\]
Thus this word is absent from the intersection over orientations, even though it avoids \(+^3\) and \(-^3\) and is accepted by \(T_3\). This illustrates why the common-invariant hypothesis cannot simply be omitted.

## Verification

The included standalone Python checker `verify.py` independently implements signed walks, exhaustive orientation intersections for seven small equal-invariant graphs, the explicit complete deterministic automata, partition-refinement minimization, and run-composition enumeration. For each \(1\le k\le11\), it compares the transitive-tournament language with forbidden runs on every input of length at most \(11\) and verifies that the proposed automaton has exactly \(2k\) reachable, pairwise inequivalent states. For seven explicit graphs, it exhaustively checks **every orientation** against every input of length at most \(8\). It also checks the five-cycle boundary witness and the length enumerator through length \(12\) for \(1\le k\le8\). See `checker-output.txt` for the reproducible output.

These finite checks support, but do not replace, the proof for all graph sizes and word lengths.

## Relationship to prior work

Pujol, *Graph-based automata* (arXiv:2609.08843v1, first posted 8 September 2026), defines \(\operatorname{Rem}(G)\) as the intersection over all orientations in Definition 32. Proposition 4 relates directed cycles to acceptance of every signed word; Corollary 34 detects the chromatic number using monochromatic directed paths; and Theorem 36 proves the special bipartite case. The present result describes **all** signed words for every graph with \(\chi=\omega\), not merely monochromatic directed paths or bipartite graphs; it additionally obtains the complete minimal deterministic automaton size and enumerator. Its clique–colouring sandwich uses the same basic orientation model but supplies a new full-language collapse.

The run-avoidance language and its standard run-counter automaton are elementary once the collapse is established. Novelty is not claimed for their general automata-theoretic definitions or for elementary run-composition counting considered in isolation.

## Limitations

The theorem does not characterize remanent languages when the clique and chromatic numbers differ. The cycle example only shows that a universal extension to every graph is false, not that equality of clique and chromatic numbers is necessary for the conclusion. It does not address minimum nondeterministic or graph-based representation size. The exact historical novelty of the resulting graph-homomorphism specialization has not been independently certified; a less explicitly stated equivalent result could exist in earlier oriented-graph literature.

## References

1. Cyril Pujol, *Graph-based automata*, arXiv:2609.08843v1 (first submitted 2026-09-08), especially Definition 32, Propositions 2 and 4, Corollary 34, and Theorem 36. https://arxiv.org/pdf/2609.08843v1
2. Myhill–Nerode theorem (standard minimal complete DFA criterion), used only for the state-minimality argument.
