# Sharp suffix-run endpoint bounds in tournament path automata

## Finding
Let \(T\) be an arbitrary loopless tournament on \(n\ge 2\) vertices. Encode traversal along an arc by \(0\) and traversal against an arc by \(1\). Every vertex is initially reachable, and every vertex is accepting. For a binary word \(w\), let \(R_T(w)\) be the set of possible ending vertices after reading \(w\). If \(w\) contains no constant block of length \(n\), and its final constant run has length \(r\) (with \(r=0\) for the empty word), then

\[
\boxed{|R_T(w)|\ge n-r.}
\]

This is sharp for every \(n\) and \(0\le r<n\): in the transitively oriented clique, the word consisting of \(r\) zeros has precisely \(n-r\) possible endpoints. In particular, after any change of direction the number of reachable endpoints returns to at least \(n-1\), regardless of the preceding history.

As consequences, the remanent language of the undirected complete graph \(K_n\), namely the intersection of these languages across all orientations, is precisely the binary language avoiding runs of \(n\) identical letters. More generally, **every finite simple graph \(G\) with \(\omega(G)=\chi(G)=n\ge2\)** has this same remanent language. Its number \(a_{n,m}\) of words of length \(m\) satisfies

\[
\sum_{m\ge0}a_{n,m}z^m=\frac{1-z^n}{1-2z+z^n},
\]

and its minimal complete deterministic automaton has exactly \(2n\) states.

## Assumptions and scope
A tournament is a complete simple graph with exactly one orientation assigned to each undirected edge. A walk may revisit vertices and edges; there are no loops. A word is readable if there is a walk whose successive arcs agree with its forward/reverse bits. The subset \(R_T(w)\) begins at the entire vertex set, not at a chosen distinguished initial state. The bounds concern all finite words with no run of length \(n\), even words much longer than the number of vertices. Graphs in the remanent consequence are finite, simple, loopless, with nonzero edges. The clique number \(\omega\) and chromatic number \(\chi\) are standard graph invariants; the equality class includes all finite perfect graphs.

## Proof
**1. Set transitions and terminal sets.** For a nonempty subset \(S\) of a tournament's vertices, write

\[
F_0(S)=\{v:\exists u\in S,\ u\to v\},\qquad
F_1(S)=\{v:\exists u\in S,\ v\to u\}.
\]

A subset \(S\) is *zero-terminal* when every vertex outside \(S\) points into at least one vertex of \(S\). It is *one-terminal* when every vertex outside \(S\) receives an arc from at least one vertex of \(S\). If \(|S|\ge2\), then \(F_0(S)\) is zero-terminal and \(F_1(S)\) is one-terminal. Indeed, if \(x\notin F_0(S)\), then \(x\to s\) for every \(s\in S\setminus\{x\}\). The induced tournament on \(S\) has an arc, hence \(F_0(S)\cap(S\setminus\{x\})\ne\varnothing\) (if \(x\in S\) is excluded from \(F_0(S)\), it is the unique source of the induced tournament and all other vertices lie in \(F_0(S)\)). Thus \(x\) points to \(F_0(S)\). The other assertion follows by reversing every arc. Also, by considering the arcs internal to \(S\),

\[
|F_i(S)\cap S|\ge|S|-1\quad(i\in\{0,1\}),
\]

since at most one vertex of a tournament on \(S\) has no predecessor (or no successor) inside \(S\).

**2. Direction-switch restoration.** If \(S\) is zero-terminal, then every vertex outside \(S\) lies in \(F_1(S)\), so

\[
|F_1(S)|\ge(n-|S|)+(|S|-1)=n-1.
\]

Dually, a one-terminal \(S\) satisfies \(|F_0(S)|\ge n-1\). The claimed terminal property persists through every valid step. When \(|S|\ge2\), this follows from step 1. A singleton zero-terminal set must be the global sink of the tournament; its zero transition is empty, while its one transition is all other vertices and is one-terminal. A singleton one-terminal set is the global source; its one transition is empty and its zero transition is all other vertices and zero-terminal. No transition to the empty set occurs in the induction below.

**3. Induction on the word.** Begin with \(R_T(\varepsilon)=V(T)\). For a first bit, the internal-arc bound yields at least \(n-1\) endpoints and the terminal property for that bit. Suppose the word prefix has a final constant run of length \(r<n\), has no length-\(n\) run, and its endpoint set \(S\) satisfies \(|S|\ge n-r\) together with the terminal property of its last bit. If the next bit repeats the last bit, the new run length \(r+1<n\) implies \(|S|\ge n-r\ge2\). The internal-arc bound gives \(|F_i(S)|\ge|S|-1\ge n-(r+1)\), and the terminal lemma preserves the property. If the next bit changes, step 2 yields at least \(n-1\) endpoints; step 1 handles \(|S|\ge2\), and the explicit global-source/global-sink observation handles \(|S|=1\). Thus the terminal property persists in either case and the endpoint bound holds for all permitted words.

**4. Sharpness and remanence.** In a transitive tournament on \(n\) totally ordered vertices, \(r\) successive forward moves have precisely \(n-r\) possible endpoints when \(0\le r<n\). A run of \(n\) forward moves, or \(n\) backward moves, is impossible in this orientation. By step 3, every run-avoiding word is readable in every tournament. These two facts give the claimed language for \(K_n\). If \(G\) has \(\omega(G)=\chi(G)=n\), then every orientation of \(G\) contains an oriented \(K_n\), hence reads every run-avoiding word by step 3. Conversely, fix a proper \(n\)-coloring and orient each edge from its lower to its higher color class. Along a forward (respectively backward) walk, colors strictly increase (respectively decrease), so no block of \(n\) forward or backward moves is possible. Thus its remanent language contains no other words.

**5. Enumeration and minimal states.** Every nonempty word avoiding runs of length \(n\) decomposes uniquely into alternating zero- and one-runs of lengths in \(\{1,\ldots,n-1\}\). With \(B(z)=z+\cdots+z^{n-1}\), the generating function is \(1+2B(z)/(1-B(z))=(1-z^n)/(1-2z+z^n)\). A complete deterministic recognizer has one initial state, one rejecting sink, and one state for each choice of last letter and run length \(1,\ldots,n-1\), totaling \(2n\). These states are pairwise Myhill--Nerode inequivalent: distinct zero-run lengths are separated by extending zeros to exactly length \(n\), and similarly for ones. A zero-run and a one-run state are separated by a suffix of zeros that just completes the zero-run to length \(n\); the other accepts it. The initial state differs from a zero- or one-run state by a suffix completing that state's run to length \(n\). The sink is distinguished by the empty suffix. Hence the complete DFA is minimal.

## Verification
The standalone `verify.py` enumerates every labeled tournament with \(n\in\{2,3,4,5,6\}\), namely \(2,8,64,1024,32768\) orientations respectively. For each, it explores the full reachable product of the tournament's powerset automaton and a trailing-run automaton, so the check ranges over **all lengths of run-avoiding words** for each of those finite values of \(n\), not just words of a prescribed maximum length. It checks the sharper lower bound on the number of endpoints after every product transition. It also minimizes the explicit run-avoiding DFA for \(2\le n\le8\) and compares exact word counts through length \(12\) with the rational-function recurrence. The output ends with `VERIFY_OK`. This finite verification is corroboration, not proof of the universal claim.

## Relationship to prior work
C. Pujol, *Graph-based automata*, arXiv:2609.08843v1 (first public version September 8, 2026), Section 5.2, introduces remanent languages; Corollary 34 relates their constant-direction paths to chromatic number, Theorem 36 determines the bipartite case, and Proposition 4 observes that cyclic orientations read every word. The graph-based automaton conventions and these earlier results are credited. The present quantitative claim differs: it determines a sharp surviving-endpoint count for **each** permissible binary word in **every** tournament, regardless of the number of direction reversals. The full language and minimal-state consequences extend the explicit classifications to all graphs whose clique and chromatic numbers coincide. The basic classification of the complete graph alone also follows from the prior acyclic-orientation observation; it is not asserted to be independently novel. Related previously recorded results for the five-cycle concern a different graph and do not imply the uniform tournament endpoint inequality.

## Limitations
The endpoint bound requires every run of a fixed direction to be shorter than \(n\); outside this range, a transitive tournament may have no compatible walk. The sharpness statement optimizes across tournaments and words of a specified final-run length; it does not assert that every individual tournament attains equality. The graph-wide remanent characterization is asserted only for \(\omega(G)=\chi(G)\), not for arbitrary graphs. No statement about simple/injective paths, shortest accepting walks, reset thresholds, or decoding complexity is made. Full-text comparisons were conducted for the relevant parts of the initiating work, but equivalent formulations in unindexed literature remain possible. Scientific review here is self-review only; no independent audit has been conducted.

## References
1. C. Pujol, *Graph-based automata*, arXiv:2609.08843v1, 2026-09-08, https://arxiv.org/html/2609.08843v1 ; especially Sections 2.1 and 5.2 (Definition 32, Proposition 33, Corollary 34, Proposition 35, Theorem 36).
2. J. Myhill, *Finite automata and the representation of events*, WADD Technical Report 57-624, 1957; A. Nerode, *Linear automaton transformations*, Proceedings of the AMS 9 (1958), 541–544 (standard minimal-DFA distinguishability principle).
