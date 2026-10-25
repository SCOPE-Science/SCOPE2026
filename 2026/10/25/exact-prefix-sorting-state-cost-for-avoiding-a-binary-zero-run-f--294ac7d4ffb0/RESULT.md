# Exact prefix-sorting state cost for avoiding a binary zero-run factor

## Finding
Let \(r\ge 1\) be an integer and let \(L_r\subseteq\{0,1\}^*\) be the set of finite words that do **not** contain the contiguous factor \(0^r1\), with ordered alphabet \(0<1\). For trim **partial** deterministic finite automata (undefined transitions reject), the minimum DFA for \(L_r\) has exactly \(r+1\) states and its maximum admissible co-lexicographic state order has width exactly \(r+1\). Nevertheless, \(L_r\) is Wheeler, and its smallest deterministic Wheeler automaton has **exactly \(2r+1\) states**. Consequently, the exact state cost of imposing a Wheeler order on this natural forbidden-factor family is \(r\) extra states, even though the ordinary minimum DFA is maximally co-lexicographically incomparable.

## Assumptions and scope
A deterministic automaton has a single initial state, all states are accessible and coaccessible, and its transition map may be partial: a missing transition rejects. Every accepted word determines a unique reached state. Our automata accept prefix-closed languages and hence all their states are final; there is *no* additional rejecting sink. A Wheeler order is a total order on states with the initial state least, with every transition into a given state carrying a consistent label, with any \(0\)-edge target preceding any \(1\)-edge target, and with monotone targets for pairs of equally labeled edges whose sources are ordered. The co-lex order of words is the lexicographic order of their reversals, with a proper prefix placed before its extension. The width of a DFA means the minimum width of a state partial order obeying the usual co-lex axioms; equivalently, under the maximal such order, states must be incomparable if their sets of reaching words interleave in co-lex order. These definitions correspond to trim partial DFAs, not complete DFAs augmented with a sink.

## Proof
**Ordinary minimization and right languages.** For an accepted word let \(j\in\{0,\ldots,r\}\) be the number of trailing zeros, truncated at \(r\). The right language depends exactly on \(j\). Its transition on \(0\) sends \(j\) to \(\min(j+1,r)\); its transition on \(1\) sends every \(j<r\) to \(0\); and the \(1\)-transition from \(r\) is undefined. All \(r+1\) states are reached by \(0^j\). For \(0\le i<j\le r\), the suffix \(0^{r-j}1\) is rejected from state \(j\) and accepted from state \(i\). Thus the \(r+1\) right languages are pairwise different; Myhill–Nerode proves ordinary minimality.

**Maximal co-lex width of the ordinary minimum.** Fix \(0\le i<j\le r\). The three accepted words \(0^i\), \(0^j\), and \(10^i\) satisfy the *strict* co-lex inequalities
\[
0^i\prec 0^j\prec 10^i.
\]
The first and third reach right-language state \(i\), while the middle reaches state \(j\). The standard separation property for co-lex state orders says that comparable states have all words reaching the lower state preceding all words reaching the higher state. Hence neither state \(i\) nor state \(j\) can precede the other. Every pair is incomparable, and the width is \(r+1\), the full state count.

**Explicit Wheeler DFA.** Introduce \(2r+1\) accepting states \(A_0,\ldots,A_r\) and \(B_0,\ldots,B_{r-1}\), starting at \(A_0\). Define the partial transitions:
\[
\begin{aligned}
A_j\xrightarrow{0}A_{\min(j+1,r)}&\quad(0\le j\le r),\\
A_j\xrightarrow{1}B_0&\quad(0\le j<r),\\
B_j\xrightarrow{0}B_{j+1}&\quad(0\le j<r-1),\\
B_{r-1}\xrightarrow{0}A_r,&\\
B_j\xrightarrow{1}B_0&\quad(0\le j<r).
\end{aligned}
\]
There is no \(1\)-edge from \(A_r\). An induction on word length gives the following exact reached-word sets: \(A_0\) receives only the empty word; for \(1\le j<r\), \(A_j\) receives only \(0^j\); \(A_r\) receives precisely the accepted words ending in at least \(r\) zeros; and \(B_j\) receives precisely the accepted words whose final \(1\) is followed by exactly \(j<r\) zeros. This description covers every accepted word once, and the absent \(1\)-edge rules out exactly the forbidden factor.

The state order
\[
A_0 < A_1 < \cdots < A_r < B_{r-1} < B_{r-2} < \cdots < B_0
\]
is Wheeler. To check this directly, every \(0\)-edge targets some \(A_j\) with \(j\ge1\) or some \(B_j\) with \(j\ge1\); every \(1\)-edge targets \(B_0\), the greatest state. Within the displayed order, the \(0\)-targets are nondecreasing with their sources: along \(A_0,\ldots,A_r\) they run through \(A_1,\ldots,A_r,A_r\); along \(B_{r-1},B_{r-2},\ldots,B_0\) they run through \(A_r,B_{r-1},\ldots,B_1\) (for \(r=1\) the last segment consists solely of \(A_1\)). The \(1\)-targets are all \(B_0\). Every target state other than \(A_0\) has a single incoming label, and \(A_0\) has no incoming transitions. These facts verify both Wheeler axioms, including their strict cross-label requirement. Hence at most \(2r+1\) Wheeler states are needed.

**Sharp Wheeler lower bound.** In any deterministic Wheeler automaton, the set of accepted words reaching each state is co-lex convex: if accepted \(u\prec v\prec w\) have \(u\) and \(w\) reaching the same state, then \(v\) reaches it as well. Indeed, the Wheeler axioms order reachable states consistently with the co-lex order of their reaching words; if \(u\) and \(w\) reached a fixed state while \(v\) reached a different one, that ordering would force an impossible strict inequality. States accepting the same words of continuation may split but cannot merge different Myhill–Nerode classes. For each \(0\le j<r\), the two accepted words \(0^j\) and \(10^j\) are in the same Myhill–Nerode class \(j\), yet \(0^{j+1}\), of *different* class \(j+1\), lies strictly between them in co-lex order. They therefore cannot reach the same Wheeler state. So each of the \(r\) classes \(j<r\) needs at least two Wheeler states; class \(r\) needs at least one. Any deterministic Wheeler automaton has at least \(2r+1\) states. The explicit construction meets this lower bound.

## Verification
The standalone `CHECKER.py` constructs each automaton for every integer \(1\le r\le 10\), checks Wheeler axioms by every ordered pair of edges, independently enumerates every binary input word through length \(\min(2r+5,14)\), compares acceptance against forbidden-factor detection, and tests the co-lex triples and the ordinary right-language separating suffixes. It passed all \(218358\) input-word checks. The all-\(r\) conclusion rests on the proof above, not on finite enumeration. Run with `python CHECKER.py` using Python 3 without dependencies.

## Relationship to prior work
Alanko–D'Agostino–Policriti–Prezza (2019/2020) introduced the Wheeler-language/Myhill–Nerode convex-interval characterization and minimum-Wheeler minimization; this result applies that theory to a fully specified infinite forbidden-factor family and proves exact state counts and the maximal width of its ordinary minimum. Cotumaccio–D'Agostino–Policriti–Prezza (2022/2023) formalized the co-lex width of partial automata and the difference between minimizing width and minimizing ordinary state count. Alanko–Cotumaccio–Prezza (2021) and Becker et al. (2024) study Wheeler minimization and co-lex width algorithmically. The later 'Universally Wheeler Languages' theorem (2025) covers Wheeler existence for a broader locally-testable class; **Wheeler existence alone is not claimed as new here**. The new claim is the *exact* simultaneous \(r+1\), \(r+1\), and \(2r+1\) state/width profile with matching family-specific lower bounds, which is not implied as a numerical identity by those general theorems alone. Search-based originality is provisional, not a proof that unindexed literature lacks this example.

## Limitations
The state counts concern trim **partial** deterministic automata without a rejecting sink; adding a sink changes ordinary complete-DFA conventions and can invalidate naive state comparisons. The alphabet order is fixed at \(0<1\); the forbidden factor has the specific form \(0^r1\). This theorem makes no claim about other patterns, stochastic automata, or minimum nondeterministic Wheeler size. Some general literature could contain an unnoticed equivalent worked example. Self-review is not an independent audit.

## References
- J. Alanko, G. D'Agostino, A. Policriti, N. Prezza, *Regular Languages meet Prefix Sorting* (first public preprint 2019-02-04), arXiv:1902.01088, https://arxiv.org/abs/1902.01088 .
- J. Alanko, N. Cotumaccio, N. Prezza, *Linear-time Minimization of Wheeler DFAs* (2021), arXiv:2111.02480, https://arxiv.org/abs/2111.02480 .
- N. Cotumaccio, G. D'Agostino, A. Policriti, N. Prezza, *Co-lexicographically Ordering Automata and Regular Languages — Part I* (2022 preprint; JACM 2023), arXiv:2208.04931, https://arxiv.org/abs/2208.04931 .
- R. Becker et al., *On the Complexity of Computing the Co-lexicographic Width of a Regular Language* (2024), arXiv:2410.04771, https://arxiv.org/abs/2410.04771 .
- *Universally Wheeler Languages* (2025), arXiv:2504.19537, https://arxiv.org/abs/2504.19537 .
