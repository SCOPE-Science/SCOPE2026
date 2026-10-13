# Exact six-state binary weakly acyclic three-set synchronization threshold \(7\)
## Finding
Let \(A=(Q,\{a,b\},\delta)\) be a complete deterministic weakly acyclic automaton with \(|Q|=6\), and let \(S\subseteq Q\) have size \(3\). If \(S\) is synchronizable, then some word of length at most \(7\) synchronizes it, and the bound is sharp.

Moreover, all equality cases form one class under simultaneous relabeling of the six states and exchange of the two letters. Thus there are exactly \(1440\) ordered labeled automaton--subset triples attaining length \(7\).

One representative on states \(0,1,2,3,4,5\) is
\[
\delta_a=(0,2,3,4,4,5),\qquad
\delta_b=(1,5,5,5,4,5),\qquad
S=\{0,1,4\}.
\]
Its shortest synchronizing word is `aaabaaa`.

## Assumptions and scope
A deterministic automaton is weakly acyclic when its only directed cycles are self-loops. Equivalently, its states admit a topological ordering \(q_0,\ldots,q_5\) such that every transition from \(q_i\) goes to some \(q_j\) with \(i\le j\).

A word synchronizes \(S\) when all states in \(S\) have the same image after reading the word. The claim concerns binary complete deterministic automata and distinguished three-element subsets.

## Proof
Fix a topological ordering and label the states \(0,1,\ldots,5\) in that order. For one letter, the image of state \(i\) may be any state in \(\{i,i+1,\ldots,5\}\), so there are
\[
6\cdot5\cdot4\cdot3\cdot2\cdot1=720
\]
possible transition maps. Hence there are \(720^2=518400\) ordered binary automata in a fixed topological order. Every six-state weakly acyclic binary automaton has at least one such topological relabeling, so this finite universe covers every isomorphism type.

For each ordered pair of transition maps, construct its subset automaton on the \(63\) nonempty subsets of \(Q\). Breadth-first search in the reverse subset graph, with all six singleton subsets as sources, gives the exact shortest synchronization distance of every synchronizable subset. Checking all \(20\) three-element subsets for all \(518400\) transition pairs gives maximum distance \(7\). Exactly four fixed-topological-order presentations attain this value.

Each of those four presentations is independently replayed by forward breadth-first search from its distinguished subset. Canonicalizing the four equality cases under all \(6!\) state permutations and both letter orders gives a single canonical class.

For the displayed representative, forward breadth-first search gives the shortest word `aaabaaa`. Directly,
\[
\{0,1,4\}\xrightarrow{aaa}\{0,4\}
\xrightarrow{b}\{1,4\}
\xrightarrow{aaa}\{4\}.
\]
The combined state-relabeling and letter-exchange orbit of this representative has size \(2\cdot6!=1440\), so the unique equality class contains exactly \(1440\) ordered labeled triples.

## Verification
Run `python3 verify.py` beside `verify.cpp` and `certificate.json`.

The verifier regenerates all \(720\) monotone transition maps for a fixed topological ordering, all \(518400\) ordered binary automata, and all twenty three-subsets. It computes exact synchronization distances in the complete subset automaton, independently replays every equality case by forward breadth-first search, canonicalizes under every state permutation and letter exchange, checks the orbit size \(1440\), and verifies the representative word `aaabaaa`.

## Relationship to prior work
Ryzhikov proved that a synchronizable \(k\)-set in an \(n\)-state weakly acyclic automaton always has a synchronizing word of length at most
\[
\frac{k(2n-k-1)}2.
\]
The same paper gives a binary construction of length \((k-1)(n-k)\). At \((n,k)=(6,3)\), these published bounds are \(6\le L\le12\), where \(L\) is the extremal shortest synchronization length. The present result closes this small binary case exactly at \(L=7\) and classifies its equality cases.

The later literature on monotonic and weakly acyclic subset synchronization focuses on asymptotic bounds, complexity, constrained synchronization, and subset-mapping problems. No inspected source states the six-state binary three-set value \(7\), the unique equality class, or the count \(1440\).

## Limitations
This is a finite six-state result. It does not determine the exact binary weakly acyclic three-set threshold for larger numbers of states, nor the general \((n,k)\) extremal function.

The exhaustive classification is up to state relabeling and exchange of the two input letters. An unindexed computation could contain the same small census even though no such statement was located in the inspected literature.

## References
1. A. Ryzhikov, “Synchronization Problems in Automata without Non-trivial Cycles,” arXiv:1702.08144v1, first public version 2017-02-27; Theoretical Computer Science 787 (2019), 77–88, DOI 10.1016/j.tcs.2018.12.026.
2. A. Ryzhikov and A. Shemyakov, “Subset Synchronization in Monotonic Automata,” arXiv:1703.06356v1, first public version 2017-03-18; Fundamenta Informaticae 162 (2018), 205–221, DOI 10.3233/FI-2018-1721.
