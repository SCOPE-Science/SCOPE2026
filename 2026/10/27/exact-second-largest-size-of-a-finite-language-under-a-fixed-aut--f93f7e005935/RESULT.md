# Exact second-largest size of a finite language under a fixed automaton budget

## Finding
Let \(\Sigma\) be a finite alphabet with \(|\Sigma|=q\ge2\). Consider finite languages \(L\subseteq\Sigma^*\) whose minimal complete deterministic finite automaton has exactly \(n\ge2\) non-dead states and exactly \(f\) accepting states, where \(1\le f\le n\). The unique dead sink is excluded from the count \(n\). Define

\[
M_{q,n,f}=\sum_{j=n-f}^{n-1}q^j.
\]

Then \(M_{q,n,f}\) is the maximum possible value of \(|L|\), attained by the language

\[
L_{\max}=\bigcup_{j=n-f}^{n-1}\Sigma^j.
\]

The largest possible cardinality strictly below \(M_{q,n,f}\) is exactly \(M_{q,n,f}-\Delta_{q,n,f}\), where

\[
\Delta_{q,n,f}=\begin{cases}
1,& n=2,\ f=1,\\
(q-1)q^{n-3},& n\ge3,\ f=1,\\
(q-1)q^{n-f-1},& 2\le f<n,\\
q^{n-2},& f=n.
\end{cases}
\]

Thus the theorem gives both the extremal language size and the exact first gap below it, with an explicit construction attaining each value.

## Assumptions and scope
Automata are complete and deterministic over a fixed alphabet of size \(q\ge2\). The language is finite, so the minimal DFA has a unique dead sink and its other \(n\) states form an acyclic transition graph. All non-dead states are reachable and have a path to an accepting state. The parameter \(f\) counts accepting states among those \(n\) non-dead states. The theorem covers \(n\ge2\) and \(1\le f\le n\); it makes no claim for a unary alphabet or for \(n=1\).

## Proof
Write the non-dead states in topological order \(v_0,\ldots,v_{n-1}\), with initial state \(v_0\). Since every non-dead state is coaccessible, the last state \(v_{n-1}\) must be accepting. Let \(e_i\in\{0,1\}\) indicate whether \(v_i\) is accepting, and put

\[
B_i=\sum_{j=i}^{n-1}e_jq^{j-i},\qquad B_n=0.
\]

Here \(B_i\) is the number of accepted suffixes from \(v_i\) in the chain automaton that sends every letter from \(v_i\) to \(v_{i+1}\), with the last state sending every letter to the dead sink. Let \(A_i\) be the actual number of accepted suffixes from \(v_i\). Backward induction gives \(A_i\le B_i\): every transition from \(v_i\) goes to a later state or the dead sink, and \(B_i=e_i+qB_{i+1}\), while \(B_{i+1}>B_j\) for every \(j>i+1\). Equality at every state requires every letter from \(v_i\) to go to \(v_{i+1}\). Therefore

\[
|L|=A_0\le B_0=\sum_{i=0}^{n-1}e_iq^i.
\]

For fixed \(f\), this weighted sum is maximized by making exactly the last \(f\) states accepting, giving \(M_{q,n,f}\). The chain construction is minimal because the maximum accepted suffix length from \(v_i\) is \(n-1-i\), distinct for every state.

It remains to find the least loss from the maximum among non-extremal automata. If the final-state pattern differs from the last-\(f\)-states pattern, then necessarily \(2\le f<n\); moving a final state from position \(n-f\) to position \(n-f-1\) is the smallest possible loss in the weighted bound, namely \((q-1)q^{n-f-1}\). For \(f=1\), the last state is the only possible accepting state; for \(f=n\), every state is accepting. In these two cases the final-state pattern is forced, so a non-extremal automaton must have a transition that skips the next state or goes to the dead sink.

Suppose the final-state pattern is extremal, and let \(i\) be the first state with a transition not going to \(v_{i+1}\). All earlier transitions form a chain, so there are exactly \(q^i\) prefixes reaching \(v_i\). The loss is at least \(q^i(B_{i+1}-B_{i+2})\). For the extremal final-state pattern this lower bound equals

\[
q^i(B_{i+1}-B_{i+2})=\begin{cases}
q^{n-2},&i+1\ge n-f,\\
q^{n-f-2}(q^f-1),&i+1<n-f.
\end{cases}
\]

When \(f=1\), the smallest such loss is \((q-1)q^{n-3}\) for \(n\ge3\), and it is \(1\) for \(n=2\). When \(2\le f<n\), every transition loss is at least \(q^{n-2}\) or \(q^{n-f-2}(q^f-1)\), both no smaller than \((q-1)q^{n-f-1}\). When \(f=n\), the loss is at least \(q^{n-2}\). These cases establish the stated lower bound on every non-extremal language.

Each bound is attained. For \((n,f)=(2,1)\), send one letter from the initial state to the dead sink and the other \(q-1\) letters to the final state. For \(n\ge3,f=1\), send one letter from the initial state to \(v_2\) and the other \(q-1\) letters to \(v_1\), then use the chain to the sole final state. For \(2\le f<n\), use the chain and make precisely \(v_{n-f-1}\) and \(v_{n-f+1},\ldots,v_{n-1}\) accepting. For \(f=n\), use the chain but send one letter from \(v_{n-2}\) to the dead sink and the remaining letters to \(v_{n-1}\). All these automata are accessible and coaccessible; their states have distinct maximum accepted suffix lengths, so they are minimal. Their language sizes are respectively \(M_{q,n,f}-\Delta_{q,n,f}\). This proves the theorem.

## Verification
The proof is analytic and covers all \(q\ge2\), \(n\ge2\), and \(1\le f\le n\). The accompanying standard-library checker enumerates topologically ordered acyclic DFA transition tables, all final-state sets, and filters for accessibility, coaccessibility, and minimality. It checked every final-state count for \(q=2\), \(n=2,3,4,5\), and \(q=3\), \(n=2,3,4\), printing `PASS: 7 (q,n) cases; final-state strata all match.` This finite census is a sanity check only, not the proof for arbitrary parameters.

## Relationship to prior work
The literature on finite-language automata includes exact enumeration of minimal acyclic automata via generalized parking functions and exact enumeration of acyclic deterministic automata. Those works count automata or study their structural ranks; the reviewed statements do not give the accepted-language cardinality spectrum conditional on both the number of non-dead states and the number of accepting states. The present result supplies a direct extremal argument for the top two distinct cardinalities, rather than a count of automata. This comparison is limited to the sources and sections reviewed; it is not an absolute claim that no earlier equivalent statement exists.

## Limitations
The result concerns complete deterministic automata recognizing finite languages, over alphabets of size at least two. It excludes unary alphabets, incomplete automata, nondeterministic automata, and the one-non-dead-state case. It identifies only the maximum and second-largest distinct cardinalities, not the full spectrum of possible language sizes.

## References
1. *Enumeration of minimal acyclic automata via generalized parking functions*, arXiv:1411.4757, first public version 2014-11-18. https://arxiv.org/abs/1411.4757
2. V. A. Liskovets, *Exact enumeration of acyclic deterministic automata*, Discrete Applied Mathematics 154 (2006), 537–551. DOI: 10.1016/j.dam.2005.06.009.
3. *Asymptotics of Minimal Deterministic Finite Automata Recognizing a Finite Binary Language*, LIPIcs AofA 2020, DOI: 10.4230/LIPIcs.AofA.2020.11.
