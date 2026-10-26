# A minimal non-partition projection witness in commutative automata

## Finding

For complete commutative deterministic finite automata with exactly one visible letter and a nonempty hidden alphabet, the smallest number of states for which an input DFA minimal for its own language has an infinite projection whose minimal DFA has that same state count, while the input DFA is not a state-partition automaton for that projection, is exactly three.

A witness over alphabet \(\{a,b\}\), projecting onto \(\{a\}^{*}\), has state set \(Q=\{0,1,2\}\), start state \(2\), final set \(F=\{0,2\}\), and transitions

\[
\delta(0,a)=1,\quad \delta(1,a)=0,\quad \delta(2,a)=0,
\]
\[
\delta(0,b)=0,\quad \delta(1,b)=1,\quad \delta(2,b)=1.
\]

The letters commute. The accepted language is \(L=\{\epsilon\}\cup\{w\in\{a,b\}^{*}: |w|_{a}\text{ is odd}\}\), so its projection is

\[
\pi_{\{a\}}(L)=\{\epsilon\}\cup\{a^{2k+1}: k\geq 0\}.
\]

This projected language has minimal DFA size three. The reachable hidden-closure subset states are \(\{1,2\}\), \(\{0\}\), and \(\{1\}\); the first and third overlap. Thus the witness is not a state-partition automaton even though projection retains the full three-state minimal complexity.

## Assumptions and scope

A DFA is complete, has a single start state, and accepts a word exactly when its terminal state is final. The letters commute when \(\delta(q,xy)=\delta(q,yx)\) for every state \(q\) and every pair of letters \(x,y\). The projection erases every hidden letter and retains the unique visible letter \(a\). A state-partition automaton means that the reachable states of the subset construction after taking hidden-letter closures are pairwise disjoint; when the input states are all reachable, these subsets partition the input state set.

The minimality claim is restricted to this one-visible-letter setting, with at least one hidden letter and commuting transitions. It is not a classification for noncommutative automata or projections retaining multiple visible letters.

## Proof

**The witness is commutative.** On states \(0\) and \(1\), the letter \(b\) fixes both states, and on state \(2\), both compositions \(ab\) and \(ba\) lead to state \(0\). Directly, for each \(q\in Q\), \(\delta(q,ab)=\delta(q,ba)\). The automaton is complete, and all three states are reachable from start state \(2\): by \(\epsilon\), \(a\), and \(aa\).

**The language and its projected complexity.** From state \(2\), the empty word ends in final state \(2\). Any word with an odd number of occurrences of \(a\) ends in state \(0\), independent of the number or placement of \(b\)'s, because \(b\) fixes states \(0,1\). Any word with a positive even number of \(a\)'s ends in state \(1\). A nonempty word with no \(a\)'s also ends in state \(1\). This proves the stated description of \(L\) and hence of its projection.

For the unary projected language, the states reached after zero, one, and two visible letters have acceptance pattern accepting, accepting, rejecting; after the second letter the run alternates between the last two states. The start state and the state reached after one \(a\) are distinguished by suffix \(a\); the rejecting state is distinguished from each accepting state by the empty suffix. All three states are therefore pairwise distinguishable, so the minimal projected DFA has exactly three states. The same distinctions (using \(b\) to distinguish states \(2\) and \(0\)) show the input DFA is minimal as well.

**Failure of the state-partition property.** Let \(C(S)\) be the set of states reachable from any state of \(S\) by zero or more hidden-letter transitions. Here \(C(\{2\})=\{1,2\}\). Taking one visible \(a\) and closing again yields \(C(\delta(\{1,2\},a))=\{0\}\); the next visible letter yields \(\{1\}\), and subsequent closures alternate between \(\{0\}\) and \(\{1\}\). Thus the reachable subset states are exactly \(\{1,2\},\{0\},\{1\}\). Since \(\{1,2\}\cap\{1\}=\{1\}\), they are not pairwise disjoint.

**No one- or two-state witness exists.** One state cannot fail the partition property: its only nonempty reachable closure subset is the whole state set. Suppose now that a two-state complete commutative DFA has a projected language whose minimal DFA has two states and is infinite. Because every hidden letter commutes with \(a\), any word can be reordered without changing its action to \(a^k v\), where \(v\) is a hidden-letter word. Thus the projected language is recognized on the original state set with the visible transition \(a\) and accepting set \(E=\{q:\text{some hidden-letter word takes }q\text{ to a final state}\}\). Minimality of the projected language implies both states are reachable and distinguishable under this unary DFA. The visible transition \(a\) is therefore either a transposition or a constant map; it cannot be the identity.

If \(a\) is a transposition, every transformation commuting with it is either the identity or that transposition. If every hidden letter is the identity, the reachable closure subsets are singletons and form a partition. If some hidden letter is the transposition, its hidden closure is the whole state set, and the only reachable subset state is the whole set, also a partition.

If \(a\) is constant with image \(c\), write \(d\) for the other state. Both states being reachable forces the start state to be \(d\). An infinite minimal two-state unary language then requires \(c\in E\) and \(d\notin E\): it is the language of all positive powers of \(a\). Every hidden letter \(h\) commutes with \(a\), so \(h(c)=c\). If \(h(d)=c\), then a hidden word takes \(d\) to the final-reachable state \(c\), forcing \(d\in E\), a contradiction. Hence every hidden letter also fixes \(d\), and all reachable closure subsets are singletons. In every case the two-state automaton is a state-partition automaton. This proves the lower bound and, with the witness, the exact minimum of three.

## Verification

The accompanying `verify.py` uses only the Python standard library. It checks the explicit three-state transition tables, commutation, the accepted-length pattern, the three reachable hidden-closure subsets, and the minimality of the unary projection. It also enumerates every labeled two-state DFA over \(\{a,b\}\) (all transition maps, start states, and final sets), filters for commutativity, and confirms that none has an infinite two-state-minimal projection with overlapping reachable hidden-closure subsets. The enumeration is a finite corroboration of the binary case; the proof above establishes the lower bound for any nonempty hidden alphabet.

## Relationship to prior work

Hoffmann proves that projecting a commutative automaton can be recognized with at most as many states as the input automaton, and gives a commutative non-state-partition example. In that example, the projected languages collapse to the one-state languages \(a^{*}\) or \(b^{*}\); it does not establish that a non-state-partition automaton can retain the full minimal state complexity of an infinite projected language. The present result supplies that sharper witness and proves the exact three-state threshold. Jirásková and Masopust define the state-partition property through pairwise-disjoint reachable subset states and study state-partition representations in general; that representation result does not imply that the particular minimal commutative DFA constructed here is a state-partition automaton.

## Limitations

This is a sharp minimal-witness result for one visible letter and at least one hidden letter, under pairwise commutation of all letter transitions. It gives no general formula for the minimal state complexity of projected languages and no classification of witnesses with four or more states. The literature comparison is bounded by the full texts and searches identified in the accompanying review; an unindexed equivalent example may exist.

## References

1. Stefan Hoffmann, *State Complexity of Projection on Languages Recognized by Permutation Automata and Commuting Letters*, arXiv:2108.06976v1, first posted 2021-08-16, especially Section 6, Theorem 2, and Example 1. https://arxiv.org/abs/2108.06976
2. Galina Jirásková and Tomáš Masopust, *On Properties and State Complexity of Deterministic State-Partition Automata*, IFIP TCS 2012, LNCS 7604, pp. 164–178, DOI: 10.1007/978-3-642-33475-7_12. Open preprint: https://users.math.cas.cz/~masopust/pubs/2012/ifiptcs2012.pdf
