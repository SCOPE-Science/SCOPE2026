# Sharp reversal complexity and alphabet threshold for undirected deterministic automata

## Finding

The reversal operation preserves the class of languages recognized by **complete deterministic undirected finite automata** (DUFAs), including those with multiple accepting states. More precisely, for every minimal \(n\)-state DUFA \(A=(Q,\Sigma,\delta,q_0,F)\) with \(n\ge2\) and \(1\le m=|F|<n\), let \(G\le\operatorname{Sym}(Q)\) be its transition group. Then

\[
\operatorname{sc}(L(A)^R)=|G\cdot F|=[G:\operatorname{Stab}_G(F)]\le\binom{n}{m}.
\]

Here \(G\cdot F\) is the family of images of \(F\) under permutations in \(G\). Equality holds if and only if \(G\) acts transitively on the \(m\)-subsets of \(Q\). Every binomial bound is realized by a **ternary** DUFA. Thus, over arbitrary finite alphabets, the largest possible reversal complexity of a minimal \(n\)-state DUFA is

\[
\max_A\operatorname{sc}(L(A)^R)=\binom{n}{\lfloor n/2\rfloor}.
\]

The minimum alphabet size for realizing this largest value is one at \(n=2\), two at \(n=3\), and **three for all \(n\ge4\)**. In particular, no binary complete DUFA on \(n\ge4\) states reaches the central binomial bound.

## Assumptions and scope

A finite input alphabet \(\Sigma\) acts on a finite state set \(Q\). The deterministic transition is total: for each letter \(a\), let \(\sigma_a(q)=\delta(q,a)\). An automaton is *undirected* when \(\delta(p,a)=q\) implies \(\delta(q,a)=p\) for every \(p,q,a\). Thus each letter \(\sigma_a\) is an involution (fixed points permitted). The minimal automaton is assumed reachable and pairwise state-distinguishable; in particular its letter-generated group \(G\) is transitive on \(Q\). A language's state complexity \(\operatorname{sc}(L)\) is the number of states in its minimal complete DFA. Reversal \(L^R\) reverses the order of each word, not the order of letters in the alphabet. All bounds refer to exact finite deterministic state counts.

If \(F=\varnothing\) or \(F=Q\), a minimal DFA has one state and the reversed language is unchanged; the nontrivial theorem treats \(n\ge2\) and \(1\le |F|<n\). The alphabet-threshold assertion concerns the maximum over proper nonempty accepting subsets for a prescribed \(n\), not the minimum alphabet for each separate \(m\).

## Proof

**1. Reverse-subset construction and closure.** Begin with the subset \(F\), apply each input letter by
\[
\widehat\delta(S,a)=\sigma_a(S)=\{\sigma_a(q):q\in S\},
\]
and declare \(S\) accepting exactly when \(q_0\in S\). A word \(w=a_1\cdots a_k\) leads to \(S_w=\sigma_{a_k}\cdots\sigma_{a_1}(F)\). Since every \(\sigma_a^{-1}=\sigma_a\), the condition \(q_0\in S_w\) is equivalent to \(\sigma_{a_1}\cdots\sigma_{a_k}(q_0)\in F\), precisely acceptance of the reversed word \(a_k\cdots a_1\) by \(A\). Moreover, applying the same letter twice maps every subset back to itself, so this reachable subset automaton is again complete, deterministic and undirected. Its reachable states are exactly \(G\cdot F\) because inverses of generating involutions are themselves.

**2. Minimality and the exact orbit formula.** Take two distinct reachable subsets \(S\ne T\). Choose \(x\in S\mathbin{\triangle}T\). As \(A\) is reachable and all letter actions are permutations, \(G\) is transitive on \(Q\). Choose \(g\in G\) carrying \(x\) to \(q_0\), and write \(g\) as a word over the involutive letters. After that word, \(q_0\) belongs to exactly one of \(g(S)\) and \(g(T)\), so the subsets have different right quotients. Therefore all \(G\cdot F\) states are minimal and the state count is their orbit size. Orbit–stabilizer yields \(|G\cdot F|=[G:\operatorname{Stab}_G(F)]\). All orbit subsets have cardinality \(m\), yielding \(|G\cdot F|\le\binom{n}{m}\), with equality precisely when the action on \(m\)-subsets is transitive.

**3. Explicit sharp witnesses with three involutions.** For each \(n\ge2\), take \(Q=\mathbb Z/n\mathbb Z\) and define three letter actions
\[
u(i)=-i\pmod n,\qquad v(i)=1-i\pmod n,\qquad
w(i)=\begin{cases}1&i=0,\\0&i=1,\\i&i\notin\{0,1\}.\end{cases}
\]
Each action is its own inverse. Composing \(v\) after \(u\) moves \(i\mapsto i+1\pmod n\); conjugates of the adjacent transposition \(w=(0\;1)\) by powers of this cycle include transpositions \((i\;i+1)\) for \(0\le i<n-1\), which generate the full symmetric group \(S_n\). Set \(q_0=0\) and \(F=\{0,\ldots,m-1\}\), with \(1\le m<n\). Because \(S_n\) acts transitively on ordered pairs of distinct points and \(F\) is nonempty and proper, any two different forward states can be sent respectively inside and outside \(F\), and all forward states are reachable; hence the forward DUFA is minimal with \(n\) states. The full symmetric group moves \(F\) to all \(m\)-subsets, so its reversal has exactly \(\binom{n}{m}\) states. Maximizing over \(m\) yields the central binomial coefficient.

**4. Sharp minimal alphabet for the global maximum.** Let a reachable binary DUFA have involutive letter permutations \(s,t\), generating \(G\). The cyclic subgroup \(H=\langle st\rangle\) is normal of index at most two in \(G\), because \(s(st)s=(st)^{-1}\). Transitivity of \(G\) on the \(n\) states entails that \(H\) has either one orbit of size \(n\) or two equal-sized orbits of size \(n/2\); indeed \(G/H\) acts transitively on the set of \(H\)-orbits. Since the permutation \(st\) is a single cycle on each \(H\)-orbit, its order is \(n\) or \(n/2\) respectively. Consequently \(|G|\le2n\) and the size of every \(G\)-orbit on subsets divides \(|G|\). This holds for *every* binary DUFA, independent of its accepting set.

For \(n\ge6\), \(\binom{n}{\lfloor n/2\rfloor}>2n\): it is true at \(n=6\) (\(20>12\)), and the central binomial coefficient strictly more than doubles when \(n\) increases by two, whereas \(2n\) grows by less than a factor of two. More explicitly, \(\binom{n+2}{\lfloor (n+2)/2\rfloor}>2\binom{n}{\lfloor n/2\rfloor}\) for \(n\ge2\). Hence the binary orbit cannot attain the central bound for \(n\ge6\).

For \(n=4\), transitivity requires \(4\mid |G|\) and the preceding argument gives \(|G|\le8\). Thus \(|G|\) is \(4\) or \(8\), and no subset orbit of size \(\binom42=6\) can divide \(|G|\). For \(n=5\), the normal cyclic subgroup must be transitive (two equal-sized orbits are impossible), so \(st\) is a 5-cycle and \(G\) is a subgroup of the standard order-ten dihedral action on a pentagon. Every unordered pair of pentagon vertices is fixed setwise by a reflection: for vertices \(i,j\in\mathbb Z/5\mathbb Z\), the reflection \(k\mapsto i+j-k\) interchanges them. All these reflections lie in \(G\), since the two distinct involutive generators and the five-cycle generate the order-ten dihedral group. Hence each two-subset has stabilizer of size at least two, its orbit has size at most five, and the central bound \(\binom52=10\) is unattainable. Complements give the same conclusion for three-subsets. Together these cases exclude any binary maximal witness for \(n\ge4\).

At \(n=3\), two reflections \(u,v\) already generate \(D_3=S_3\), attaining \(\binom31=3\) for a singleton accepting set; a single involution has orbits of size at most two and cannot produce a reachable minimal three-state DUFA. At \(n=2\), the single swap letter, a singleton accepting set, and two reachable states suffice. Thus the alphabet minima are respectively \(1,2,3\) in the stated regimes.

## Verification

The accompanying `verify.py` builds the three-involution witness and its reverse-subset automaton for every \(2\le n\le9\) and every \(1\le m<n\), checks all letter actions are involutive, enumerates the full orbit, and separately minimizes the resulting transition tables by stable partition refinement. It compares forward-reversal membership with subset acceptance for all input words of length at most seven. It additionally enumerates all transitive pairs of involutions for \(2\le n\le5\), checks the reverse orbit bound and confirms the binary obstruction at \(n=4,5\). Running `python verify.py` prints `VERIFY_OK parameters 36 word_membership_checks 118080 exhaustive_transitive_two_letter_pairs 159 largest_witness_reverse 126`. These bounded checks are auxiliary; the proof above establishes all-parameter claims.

## Relationship to prior work

Kutrib, Malcher and Schneider introduced deterministic and nondeterministic undirected automata and, in the full open-access 2021 journal article (Section 4 and its conclusion), explicitly left both closure of DUFA languages under reversal and its deterministic state complexity unresolved beyond the one-accepting-state case. Their 2018 DCFS chapter is the earliest verified public source motivating this investigation. Their different **nondeterministic** undirected automata are not reversal closed; the present theorem makes no claim about that model.

Hospodár and Mlynárčik (2020, Lemma 7, Theorem 8 and Theorem 11) already proved reversal closure and the same central binomial worst-case bound for the **larger** class of permutation automata. Their sharp binary witness uses a full \(n\)-cycle letter (not an involution for \(n\ge3\)), so it does not establish closure within the involutive DUFA subclass, its sharpness for that subclass, or the ternary-versus-binary alphabet separation. The orbit/minimality argument for general permutations is aligned with their Lemmas 1, 6 and 7; the novelty claimed here is strictly limited to the undirected specialization and its exact subgroup-orbit and alphabet-sharp consequences. The main DUFA article's explicit open statement is consistent with this distinction even though the permutation-automata article predates its journal publication.

## Limitations

This result concerns **complete deterministic** undirected automata, not incomplete transitions or nondeterministic undirected automata. The exact orbit count depends on the given transition group, not only on \(n,m\), except for the worst-case bound. The ternary minimum concerns attainment of the *central* maximum, and does not prohibit binary smaller reversal complexities or unary/binary witnesses for particular \(m\). Full group generation and orbit-stabilizer provide an infinite proof; the verifier's finite cutoff establishes only checks for those indicated parameters. A complete novelty guarantee is not available: equivalent unindexed or later results could exist. No independent mathematical audit has been performed.

## References

1. M. Kutrib, A. Malcher and C. Schneider, *Finite Automata with Undirected State Graphs*, in *Descriptional Complexity of Formal Systems* (DCFS 2018), LNCS 10952, pp. 212–223, Springer, DOI: `10.1007/978-3-319-94631-3_18` (proceedings print edition released 11 July 2018, eBook 14 July 2018).
2. M. Kutrib, A. Malcher and C. Schneider, *Finite automata with undirected state graphs*, *Acta Informatica* 59, pp. 163–181 (online 24 May 2021), DOI: `10.1007/s00236-021-00402-0`, especially Sections 3–4 and 6. Open-access full text: `https://link.springer.com/article/10.1007/s00236-021-00402-0`.
3. M. Hospodár and P. Mlynárčik, *Operations on Permutation Automata*, *Developments in Language Theory* (2020), pp. 122–136, DOI: `10.1007/978-3-030-48516-0_10`, especially Lemmas 1, 6–7, Theorems 8 and 11. Author-uploaded complete text: `https://www.researchgate.net/publication/341627890_Operations_on_Permutation_Automata`.
