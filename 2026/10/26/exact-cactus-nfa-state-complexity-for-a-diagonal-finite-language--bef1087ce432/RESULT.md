# Exact cactus-NFA state complexity for a diagonal finite language

## Finding

For every integer \(k\ge1\), let \(\Sigma_k=\{a_1,\ldots,a_k\}\) and \(L_k=\{a_i a_i:1\le i\le k\}\). The minimum number of states of an epsilon-free NFA recognizing \(L_k\) whose underlying simple transition graph is a bipartite cactus is exactly \(k+1+\lceil k/2\rceil\), whereas the unrestricted epsilon-free NFA minimum is \(k+2\).

The restricted-state overhead is therefore \(\lceil k/2\rceil-1\), which is positive for every \(k\ge3\) and grows linearly with the alphabet size.

## Assumptions and scope

For each integer \(k\ge1\), use the alphabet \(\Sigma_k=\{a_1,\ldots,a_k\}\) and the finite language \(L_k=\{a_i a_i:1\le i\le k\}\). An epsilon-free NFA has one initial state, a set of accepting states, and transitions labeled by letters of \(\Sigma_k\), with no epsilon transitions. Its underlying simple transition graph is the undirected graph on states that places an edge between two distinct states whenever any transition joins them. A cactus is a graph in which every edge belongs to at most one simple cycle. A bipartite transition graph has a fixed partition of its states such that every transition crosses the partition. The minimum is taken over all NFAs in the specified class, without assuming determinism or unambiguity.

## Proof

### Upper bound

Partition the indices \(\{1,\ldots,k\}\) into \(m=\lceil k/2\rceil\) blocks, each of size two except for one singleton when \(k\) is odd. Create a nonaccepting initial state \(s\), a distinct nonaccepting state \(q_i\) for each index \(i\), and one accepting state \(f_B\) for each block \(B\). For every \(i\), add transitions

\[
s\xrightarrow{a_i}q_i\xrightarrow{a_i}f_{B(i)},
\]

where \(B(i)\) is the block containing \(i\), and add no other transitions. This NFA accepts exactly \(L_k\) and has \(1+k+m\) states.

For each two-element block \(\{i,j\}\), the underlying graph contains the four-cycle \(s-q_i-f_{\{i,j\}}-q_j-s\). Different such cycles share only \(s\), and a singleton block contributes a length-two path attached at \(s\). Hence every edge lies in at most one cycle. The graph is bipartite with parts \(\{s\}\cup\{f_B:B\text{ a block}\}\) and \(\{q_i:1\le i\le k\}\). This proves the upper bound \(1+k+\lceil k/2\rceil\).

### Lower bound

Consider any epsilon-free NFA for \(L_k\) with a cactus underlying graph. Remove states that are unreachable from the initial state or cannot reach an accepting state; this preserves the language and the cactus property, so it suffices to consider a trimmed NFA. Since the language contains no word of length zero or one, the initial state is nonaccepting and every accepting path has exactly two transitions. For each \(i\), choose an accepting path \(s\xrightarrow{a_i}q_i\xrightarrow{a_i}f_i\), with \(f_i\) accepting.

The states \(q_i\) are pairwise distinct. Indeed, if \(q_i=q_j\) for distinct \(i,j\), the transition labeled \(a_j\) from that shared state to an accepting state would make \(a_i a_j\) accepted, contrary to the definition of \(L_k\). None of the \(q_i\) is the initial state or an accepting state, so the initial state, the \(k\) middle states, and all accepting states are disjoint sets.

A single accepting state can serve as \(f_i\) for at most two indices. If one final state \(f\) were reached from three distinct middle states \(q_i,q_j,q_\ell\) along their respective second-letter transitions, the graph would contain the three four-cycles formed by \(s,f\) and each pair of middle states. In particular, an edge such as \(\{s,q_i\}\) would belong to two distinct cycles, contradicting the cactus condition. Since the chosen accepting paths cover all \(k\) indices and each final state serves at most two, there must be at least \(\lceil k/2\rceil\) accepting states. Therefore every such NFA has at least \(1+k+\lceil k/2\rceil\) states. Combined with the construction, this proves the exact minimum. The lower bound uses only the cactus condition; the matching construction is also bipartite.

Without the cactus restriction, the same distinct-middle-state argument gives a lower bound of \(k+2\) states, and one shared final state attains it. This proves the unrestricted comparison in the claim.

## Verification

The construction has exactly one initial state, \(k\) middle states, and \(\lceil k/2\rceil\) final states. Its only accepting paths are the designated paths labeled \(a_i a_i\). Each two-index block creates one four-cycle, and no edge is shared by two cycles. The lower bound applies to arbitrary nondeterministic branching and does not assume a particular automaton normal form. No finite enumeration or external certificate is used as a proof.

## Relationship to prior work

The recent paper *Every Regular Language Has a Bipartite Cactus Automaton* establishes the existence of epsilon-free NFAs with bipartite cactus transition graphs for all regular languages. The present statement is a state-minimum result for the explicit finite family \(L_k\), rather than another existence theorem. Work on finite automata with undirected transition graphs studies a different model, requiring symmetric transitions; its unary characterization does not imply this multi-symbol result. General NFA union constructions explain the unrestricted \(k+2\)-state upper bound, but do not impose the cactus constraint used in the exact lower bound here.

## Limitations

The formula is proved for the family \(L_k\) over \(k\) distinct symbols and for epsilon-free NFAs. It does not classify the minimum for arbitrary finite languages, for automata with epsilon transitions, or for other graph restrictions. The lower bound is valid for all cactus NFAs, while the exhibited optimum is bipartite; no broader state-complexity classification is claimed.

## References

1. Mario Grobler, Till Koziel, and Sebastian Siebertz, “Every Regular Language Has a Bipartite Cactus Automaton,” arXiv:2610.11717, first public version 2026-10-08. https://arxiv.org/abs/2610.11717. DOI: https://doi.org/10.4204/EPTCS.454.9.
2. Martin Kutrib, Andreas Malcher, and Christian Schneider, “Finite automata with undirected state graphs,” *Acta Informatica* 59 (2022), 163–181; published online 2021-05-24. https://doi.org/10.1007/s00236-021-00402-0.
3. Markus Holzer and Martin Kutrib, “Unary Language Operations and Their Nondeterministic State Complexity,” DLT 2002 / LNCS 2450 (2003), 162–172. https://doi.org/10.1007/3-540-45005-X_14.
