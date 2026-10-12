# Complete four-state classification for maximal synchronizing-word state complexity
## Finding
Let \(\mathcal A=(\{a,b\},Q,\delta)\) be a complete deterministic binary semi-automaton with \(|Q|=4\). The state complexity of its synchronizing-word language satisfies
\[
\operatorname{sc}(\operatorname{Syn}(\mathcal A))\le 12.
\]
Equality has the following complete characterization.

After interchanging the letters if necessary and cyclically labeling the states, one letter is
\[
b(q)=q+1\pmod 4
\]
and the other letter \(a\) has rank \(3\). Let \(\{u,v\}\) be the unique two-element kernel class of \(a\), let \(t\) be their common image, and let \(s\) be the unique state omitted from \(a(Q)\). Then
\[
\operatorname{sc}(\operatorname{Syn}(\mathcal A))=12
\]
if and only if it is not simultaneously true that
\[
v=u+2\pmod 4
\qquad\text{and}\qquad
s=t+2\pmod 4.
\]

For the normalized cycle \(b(q)=q+1\pmod 4\), there are \(144\) rank-\(3\) maps \(a\). Exactly \(128\) give maximal state complexity and exactly \(16\) fail; those \(16\) are precisely the maps satisfying both antipodality conditions above.

Across all \(4^8=65{,}536\) ordered labeled binary transition pairs, exactly \(1536\) attain state complexity \(12\). Modulo simultaneous relabeling of the four states and interchange of the two letters, these form exactly \(32\) isomorphism classes, each having orbit size \(48\).

## Assumptions and scope
A word \(w\) is synchronizing when it maps all states to one state. The synchronizing-word language is
\[
\operatorname{Syn}(\mathcal A)=\{w:|\delta(Q,w)|=1\}.
\]
Its state complexity is the number of states in the minimal deterministic automaton recognizing this language.

The standard subset automaton starts from \(Q\), applies letters to subsets, and treats singleton subsets as accepting. All singleton states are equivalent, and the empty subset is unreachable, giving the general upper bound \(2^4-4=12\).

The classification is for ordered binary transition pairs on four labeled states, together with the stated quotient by state relabeling and alphabet interchange. It does not classify larger automata.

## Proof
The proof is a complete finite classification.

There are
\[
4^{2\cdot4}=65{,}536
\]
ordered labeled binary transition pairs. For each pair, construct the reachable part of the subset automaton from the full set \(Q\). Minimize that deterministic automaton by partition refinement, with singleton subsets accepting and all other reachable subsets rejecting. This gives the exact state complexity of \(\operatorname{Syn}(\mathcal A)\).

The census finds \(1536\) automata with state complexity \(12\). Every one has exactly one letter that is a \(4\)-cycle and exactly one letter of rank \(3\). Hence every maximal automaton can be normalized, after swapping letters and relabeling states, to
\[
b(q)=q+1\pmod4
\]
with \(a\) of rank \(3\).

There are \(144\) rank-\(3\) self-maps of a four-element set. Exhausting those maps against the fixed cycle gives \(128\) maximal and \(16\) nonmaximal cases. For each rank-\(3\) map, record its unique two-element kernel class \(\{u,v\}\), the common image \(t=a(u)=a(v)\), and the omitted state \(s\notin a(Q)\). The \(16\) nonmaximal maps are exactly those for which both pairs
\[
\{u,v\},\qquad \{s,t\}
\]
are antipodal in the four-cycle. Conversely every one of the other \(128\) maps has state complexity \(12\). This proves the stated if-and-only-if criterion.

For the isomorphism count, act on an ordered transition pair by all \(24\) simultaneous state relabelings and by the interchange of the two letters. Canonicalizing each of the \(1536\) maximal pairs gives \(32\) classes. Each orbit has size \(48\), so the orbit count is exact.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier uses two independent tests for maximal state complexity. The first constructs the reachable subset automaton and minimizes it by repeated partition refinement. The second does not minimize: it checks reachability of every non-singleton subset and then uses a table-filling distinguishability procedure on pairs of subset states. The two tests agree on all \(65{,}536\) binary four-state automata.

It then fixes the standard four-cycle and independently checks the structural antipodality criterion against exact minimization for all \(4^4=256\) possible second letters. Among the \(144\) rank-\(3\) maps, the split is exactly \(128\) maximal versus \(16\) exceptional.

Finally, the verifier canonicalizes every maximal automaton under all state permutations and the letter swap, recovering \(32\) classes, all of orbit size \(48\). It separately checks the four-state example printed in the primary source.

## Relationship to prior work
Hoffmann proves the general upper bound
\[
\operatorname{sc}(\operatorname{Syn}(\mathcal A))\le 2^n-n
\]
and develops sufficient criteria for circular automata with a rank-\((n-1)\) letter to attain it. The paper also proves that every completely reachable binary automaton with more than two states is circular with the other letter of rank \(n-1\).

Crucially, Hoffmann gives an explicit four-state circular example with maximal state complexity \(12\) for which the stated sufficient criteria do not apply. The paper's conclusion says that obtaining sufficient and necessary criteria for the binary circular rank-\((n-1)\) setting is natural and that a finer analysis is needed.

The present finding supplies that finer analysis completely at the first nontrivial four-state level. Hoffmann's printed example has
\[
a=(1,2,1,3),\qquad b=(1,2,3,0).
\]
Its kernel pair \(\{0,2\}\) is antipodal, but its omitted state \(0\) and double-image state \(1\) are adjacent, so it lies on the maximal side of the criterion.

Targeted searches for a four-state census, a normalized rank-\(3\) classification, the counts \(128\), \(1536\), and \(32\), and an antipodality criterion did not locate a covering published result.

## Limitations
This is an exhaustive four-state classification. It does not provide a necessary-and-sufficient criterion for arbitrary \(n\), which remains substantially broader.

The count \(1536\) is for ordered labeled transition pairs. The count \(32\) quotients only by simultaneous state relabeling and interchange of the two input letters.

An unindexed computation or unpublished small-state census could contain the same classification.

## References
1. S. Hoffmann, “State Complexity of the Set of Synchronizing Words for Circular Automata and Automata over Binary Alphabets,” arXiv:2011.14404v1, first public version 2020-11-29; LATA 2021, DOI 10.1007/978-3-030-68195-1_25.
2. S. Hoffmann, “Completely Reachable Automata, Primitive Groups and the State Complexity of the Set of Synchronizing Words,” arXiv:2007.09104v1, first public version 2020-07-17; LATA 2021, DOI 10.1007/978-3-030-68195-1_24.
