# Five involutive letters attain the sharp projection blow-up at every even state size

## Finding
For every integer \(k\ge 2\), there exists a **minimal** complete deterministic undirected finite automaton (DUFA) with \(2k\) states, **five input letters**, exactly **one erased letter**, and exactly **one accepting state**, such that every letter induces an involution and the projected language has minimal deterministic state complexity
\[
\boxed{2^k-1.}
\]
The erased letter acts without fixed points, pairing the \(2k\) states into \(k\) two-element orbits. Every nonempty union of these orbits occurs as a reachable state in the standard deterministic projection automaton, and the \(2^k-1\) reachable states are pairwise distinguishable. This is the largest possible count for any permutation automaton with this fixed-point-free involutive erased letter, by its orbit-partition upper bound.

Moreover, for every \(k\ge2\), the projected language **cannot** be recognized by a deterministic undirected automaton (or by any permutation automaton). Thus letter erasure does not preserve the class of deterministic undirected languages.

## Assumptions and scope
A complete deterministic undirected automaton is a finite deterministic automaton such that a transition from \(p\) to \(q\) under letter \(x\) exists exactly when the reverse transition from \(q\) to \(p\) under the **same** letter exists. Equivalently, each letter acts as an involutive permutation on the state set. State complexity means the number of states in the **minimal complete deterministic** automaton, with no restriction on the output automaton.

The erasing homomorphism \(\pi\) maps one specified input letter \(a\) to the empty word and leaves four other letters unchanged. Its image language contains all observed strings that result from deleting arbitrary numbers of \(a\)-letters from accepted original strings. All statements are for integers \(k\ge2\); the input alphabet is constant-size (five letters), although its transition permutations depend on \(k\). No minimality of this alphabet size is claimed.

## Proof
**1. Orbit upper bound.** Suppose a permutation automaton has \(2k\) states and the sole erased letter \(a\) is a fixed-point-free involution. Its hidden transition orbits form a partition into \(k\) disjoint pairs. The standard epsilon-closure construction for erasure starts from the hidden orbit of the original initial state. After each visible letter, it applies the visible permutation to the current nonempty subset and takes hidden closure again. Every reachable state is consequently a nonempty union of hidden pairs. There are exactly \(2^k-1\) such unions. This establishes the asserted general upper bound, without assumptions on the visible alphabet size or final-state set.

**2. Explicit five-letter automata.** Fix \(k\ge2\), and write the state set as
\[
Q=\{(i,j):i\in\mathbb Z/k\mathbb Z,\ j\in\{0,1\}\}.
\]
For every \(i\), denote the hidden pair by \(P_i=\{(i,0),(i,1)\}\). Let the initial state and the unique accepting state both be \((0,0)\). The alphabet is \(\{a,b,c,d,e\}\); letter \(a\) alone is erased. Define its transitions by
\[
\begin{aligned}
 a(i,j)&=(i,1-j),\\
 b(i,j)&=(\tau(i),j),\\
 c(i,j)&=(-i,j),\\
 d(i,j)&=(1-i,j),
\end{aligned}
\]
where \(\tau\) interchanges \(0\) and \(1\) and fixes the remaining pair indices. Finally, \(e\) interchanges \((0,0)\) with \((1,0)\) and fixes every other state. Indices in the displayed formulas are taken modulo \(k\). Each displayed map is an involution; for \(k=2\), some visible letters happen to have identical or identity actions, which causes no difficulty. Therefore this is a complete DUFA.

The permutations of pair indices induced by \(b,c,d\) generate the entire symmetric group on the \(k\) pairs. Indeed, the composition \(d\circ c\) is the cyclic shift \(i\mapsto i+1\), and conjugating \(\tau=(0\ 1)\) by its powers gives all cyclically adjacent transpositions. In particular the ordinary adjacent transpositions are available; these generate the symmetric group. Any permutation of the pair indices can therefore be performed by an observable word over \(\{b,c,d\}\), without enlargement of a union of hidden pairs.

**3. Reachability of every nonempty union.** Identify a hidden-closed subset \(\bigcup_{i\in R}P_i\) with its nonempty index set \(R\subseteq\mathbb Z/k\mathbb Z\). The starting closure is \(R=\{0\}\). The letters \(b,c,d\) act by arbitrary pair permutations, as just proved. The letter \(e\), followed by the hidden closure, has the following precise effect: if exactly one of \(0,1\) belongs to \(R\), it adds the other index; if both or neither belong to \(R\), it leaves \(R\) unchanged. For example, if \(0\in R\) and \(1\notin R\), then \(e\) moves \((0,0)\) to \((1,0)\) while leaving \((0,1)\) in place, so the subsequent \(a\)-closure includes both \(P_0\) and \(P_1\).

Every singleton \(R\) is reachable by a pair permutation. Suppose a particular nonempty \(R\) is reachable and \(j\notin R\). Choose \(i\in R\) and a visible pair-permutation word carrying \(i\) to \(0\) and \(j\) to \(1\). After this word the index set contains \(0\) but not \(1\). Read \(e\), adding \(1\), then perform the inverse pair permutation, which is again realizable over \(\{b,c,d\}\). The result is exactly \(R\cup\{j\}\), with no other additions. Induction on cardinality proves that all \(2^k-1\) nonempty index sets are reachable.

**4. Pairwise distinguishability.** In a hidden-closed subset, acceptance of the empty observed suffix holds exactly when index \(0\) is present, because \((0,0)\) is the unique accepting original state. For two distinct index sets \(R,T\), select \(i\) in their symmetric difference. An observable word over \(\{b,c,d\}\) can send \(i\) to \(0\) while permuting all index sets bijectively and without enlargement. Following that word, precisely one of \(R,T\) contains index \(0\). The two projected right languages are different. Hence all reachable subsets are inequivalent, proving exact minimal state complexity \(2^k-1\).

**5. The original DUFA is minimal.** Its transition group is transitive on \(Q\): the pair-permuting letters move any state to the same lane of pair \(0\), and the erased involution \(a\) exchanges the two lanes. With a singleton final state, transitivity and bijectivity imply state distinguishability: for any distinct \(p,q\), some transition word sends \(p\) to \((0,0)\), while necessarily sending \(q\) elsewhere. All \(2k\) states are reachable from the initial state by transitivity. Therefore the input DUFA is minimal and has precisely \(2k\) states.

**6. Non-closure under erasure.** In the minimal projected automaton, letter \(e\) sends both distinct states \(\{P_0\}\) and \(\{P_1\}\) to \(\{P_0,P_1\}\). This transition is not injective. Any language recognized by a complete permutation automaton has a minimal deterministic automaton whose letter actions are still permutations (taking Myhill--Nerode classes preserves the identities satisfied by the original permutations, since each letter has a positive-word inverse). The minimal projected automaton is therefore not a permutation automaton, and hence not a DUFA. This also proves the asserted non-closure.

## Verification
The standalone `verify.py` uses only the Python standard library. It constructs all five state permutations and verifies their involution identities; performs subset reachability over the four visible letters with hidden closure; minimizes the reachable projected automaton by partition refinement; and checks that the original automaton is fully reachable. All nine parameters \(k=2,3,\ldots,10\) give exactly \(2^k-1\) reachable and pairwise inequivalent projected subsets. The largest checked case has \(1023\) projected states.

For \(k=2,3,4\) it additionally enumerates all visible words through length five and independently runs the original deterministic automaton with zero or one hidden-letter insertion at **each** boundary between visible letters. Because \(a^2\) is the identity, these are all possible erased insertions up to equivalence. All \(4095\) tested words agree with the projected subset construction. Run `python3 verify.py`; observed output: `VERIFY_OK configurations=9 independent_projected_words=4095 largest_projected_states=1023`.

These finite checks corroborate the construction and the semantics of erasure; the theorem for every \(k\ge2\) follows from the symbolic group-generation, reachability, distinguishability and upper-bound arguments above.

## Relationship to prior work
Hoffmann (arXiv:2108.06976, first public version 16 August 2021) proved the general permutation-automaton projection upper bound depending on the states moved by hidden letters. The present upper bound is the specialization in which all \(2k\) states are moved by one erased involution; **the upper bound itself is prior work**. The explicit seven-letter lower-bound construction in Hoffmann's Theorem 2 has parameter hypotheses \(0<2m+1<n\) and therefore does not provide the endpoint where all states belong to nontrivial erased orbits. Hoffmann expressly asks whether his seven-letter alphabet can be reduced. The contribution here is an explicit **five-letter, fully involutive, minimal** witness at the full-matching endpoint, together with the complete reachable-subset characterization and restricted-class nonclosure consequence.

Kutrib, Malcher and Schneider (2021 open-access article, with related earlier conference material) define DUFAs and study state complexity for Boolean operations, concatenation, iteration and reversal. Their deterministic results do not give the present erasure witness. The five-letter construction uses three observable involutions acting as a full symmetric group on the hidden pairs, plus one local splitting involution; it is not a substitution of arbitrary visible permutations into the known seven-letter witness. A search for an equivalent restricted full-matching projection construction did not identify one, but a previously unindexed equivalent witness remains possible.

## Limitations
No claim is made about odd numbers of input states, multiple erased letters, or the smallest possible input alphabet attaining the upper bound. The result does not improve Hoffmann's numerical upper bound for arbitrary permutation automata. The exact novelty claim is about its attainment at the full-matching endpoint **inside the narrower class of involutive-letter automata**, with a fixed alphabet of five letters. The 2021 literature inspection and indexed searches reduce but do not eliminate the possibility of an earlier equivalent construction. The verification program tests finite cases only. No independent mathematical audit has been performed.

## References
1. S. Hoffmann, *State Complexity of Projection on Languages Recognized by Permutation Automata and Commuting Letters*, arXiv:2108.06976, v1 dated 16 August 2021, https://arxiv.org/abs/2108.06976. See Sections 3--5, especially the projection upper bound, Theorem 2 and Remark 1 on alphabet size.
2. M. Kutrib, A. Malcher and C. Schneider, *Finite automata with undirected state graphs*, *Acta Informatica* **59** (2022), 163--181, first online 24 May 2021, https://doi.org/10.1007/s00236-021-00402-0. See especially Sections 2--4 and 6.
