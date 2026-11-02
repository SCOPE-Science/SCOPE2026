# The exact number of shortest reset words in a two-parameter adversarial-synchronization automaton

## Finding
For the Lipin–Volkov deterministic automata \(\mathcal L_m^k\), with **every integer** \(m\ge1\) and \(k\ge2m-1\), the number of distinct input words of minimum resetting length is
\[
\boxed{\frac{(k+2m)!}{6^m}}.
\]
The minimum resetting length is \(k+2m\), a threshold already obtainable from the construction in [1]. The new assertion is the **complete count and characterization of all shortest reset words** in this two-parameter range. These words are in bijection with permutations of \(k+2m\) labeled events satisfying precisely the ordering restrictions given below.

## Assumptions and scope
Fix integers \(m\ge1\) and \(k\ge2m-1\). The alphabet consists of **distinct symbols** \(a_1,\ldots,a_{k+m}\). The states are \(Q=\{0,1,\ldots,k+m\}\), with absorbing state \(0\). For \(1\le i\le k\), \(a_i\) maps \(i\) to \(0\) and fixes every other state. For \(1\le r\le m\), \(a_{k+r}\) cyclically permutes the states
\[
r\longrightarrow r+1\longrightarrow\cdots\longrightarrow k+r\longrightarrow r,
\]
fixing all other states. Products of letters act from left to right on states. A reset word sends all states to one state, necessarily \(0\) here. Distinct reset words mean distinct strings over this fixed indexed alphabet, not state-label or letter-label equivalence classes.

The restrictions \(m\ge1\) and \(k\ge2m-1\) are essential to the proof. No formula is asserted outside them.

## Proof
**1. The minimum length and the event labels.** Regard each initial nonzero state as holding a distinct marked token, retained until its first transition to \(0\). The cycle letters are permutations of nonzero states and therefore never merge live tokens. A low-index letter \(a_i\), \(i\le k\), kills at most one marked token. Thus any reset word needs at least \(k+m\) successful low-index kill moves.

Call states \(1,\ldots,k\) *low* and states \(k+1,\ldots,k+m\) *high*. A high-index cycle \(a_{k+r}\) can move a token from high to low only at its top state \(k+r\), sending it to \(r\). Its only possible low-to-high movement is from state \(k\) to state \(k+1\). To eliminate the \(m\) initially high tokens requires at least \(m\) high-index letters. Hence every reset word has length at least \(k+2m\).

This bound is attained by first removing all initially low tokens and then, in increasing order of their original indices, demoting and removing each initially high token. Explicitly, a reset word of length \(k+2m\) is
\[
 a_1a_2\cdots a_k\;(a_{k+1}a_1)(a_{k+2}a_2)\cdots(a_{k+m}a_m).
\]
Indeed each low token is killed first; each subsequent cycle demotes the token initially at its top high position and the immediately following low-index letter kills it, while other high tokens remain at their original top positions (higher-index tops are outside earlier cycle intervals). Thus the reset threshold is exactly \(k+2m\), consistent with [1].

Consequently, every *shortest* reset word contains precisely \(k+m\) successful kills and \(m\) cycle letters. Each cycle must reduce the number of live high tokens by exactly one, so its top high state must be occupied and its state \(k\) must be unoccupied. No token ever moves back from low to high along a shortest path. Each initially high token is demoted exactly once and killed later.

Label the kill of initial low token \(i\), \(1\le i\le k\), by \(D_i\). Label the cycle that demotes initial high token \(k+h\) by \(C_h\) and its later kill by \(H_h\), \(1\le h\le m\). Thus the \(k+2m\) letters of any shortest reset word acquire distinct event labels. Necessarily \(C_h\prec H_h\) for every \(h\).

**2. Gate constraints.** Enumerate the \(m\) cycle events by their chronological order, \(C_{(1)},\ldots,C_{(m)}\). Then for every \(1\le j\le m\),
\[
D_{k-j+1}\prec C_{(j)}.\tag{1}
\]
To see this, suppose the initial low token \(k-j+1\) remains alive before the \(j\)-th cycle. Because \(k-j+1\ge k-m+1\ge m\), every previous cycle (whose lower endpoint is at most \(m\)) increments this token's position by one. It therefore occupies state \(k\) immediately before the \(j\)-th cycle. That cycle would send it into high state \(k+1\), contradicting the compulsory decrease of the high-token count at every cycle. This proves (1).

**3. The constraints are also sufficient.** Conversely, begin with *any permutation* of the \(k+2m\) distinct symbols
\[
D_1,\ldots,D_k,C_1,\ldots,C_m,H_1,\ldots,H_m
\]
satisfying all \(C_h\prec H_h\) and (1). Decode it from left to right, tracking the individual live tokens: on a \(D_i\) or \(H_h\) event, choose the low-index letter at that token's current position; on a \(C_h\) event choose the high-index cycle whose top is that high token's current position. We show by induction that each move exists and has exactly the desired effect.

Immediately before cycle event \(C_{(j)}\), all surviving originally low tokens lie below \(k\). For an initial low token \(q\le k-m\), at most \(j-1\) earlier cycles incremented it, so its position is at most \(q+j-1\le k-1\). For an initial low token \(q=k-t+1\) with \(1\le t\le m\), it has already been killed if \(t\le j\), by (1), while if \(t>j\), its position is at most \(k-t+j\le k-1\). A previously demoted original high token starts at a low position at most \(m\), and before the \(j\)-th cycle at most \(j-2\) later cycles have acted on it, so its position is at most \(m+j-2\le2m-2\le k-1\). Therefore **no live low token occupies state \(k\)** before a cycle; choosing the high letter at the selected high token's current top position demotes that one token without elevating any low token. Other high tokens remain high, and every low token remains low. At a \(D_i\) or \(H_h\) event, its designated live token is low by the event inequalities and can be killed by precisely the letter indexed by its current low position. All events are therefore legal, and the final word resets the automaton in exactly \(k+2m\) moves.

Conversely, the letter sequence determines the token trajectories and hence the unique event label of every move along any shortest reset word. Thus decoding is injective, and the necessary-and-sufficient event conditions prove a **bijection**.

**4. Count the admissible event permutations.** Assign independent uniform continuous arrival times \(U_E\in[0,1]\) to the \(k+2m\) event labels, and order events by arrival time. Every labeled permutation is equally likely. Conditional on the \(m\) cycle arrival times \(t_h=U_{C_h}\), the probability that all \(H_h\) occur later is \(\prod_h(1-t_h)\). If \(t_{(1)}<\cdots<t_{(m)}\) are the ordered cycle times, each of the \(m\) distinct gate kills \(D_{k-j+1}\) independently must arrive before \(t_{(j)}\). Its conditional probability is \(\prod_jt_{(j)}=\prod_ht_h\). Therefore the unconditional probability that a uniformly random labeled event permutation satisfies exactly the constraints is
\[
\int_{[0,1]^m}\prod_{h=1}^m t_h(1-t_h)\,dt_1\cdots dt_m
=\left(\int_0^1t(1-t)\,dt\right)^m=6^{-m}.
\]
Multiplication by the total \((k+2m)!\) labeled permutations completes the proof of the claimed count. \(\square\)

## Verification
The standalone `verify.py` implements the transition maps literally and counts **all distinct shortest reset words** by reverse-independent forward breadth-first subset dynamic programming (the script counts distinct input-letter strings, including convergent subset paths). This confirms the formula for 37 pairs with \(1\le m\le5\), \(2m-1\le k\le12\), and \(k+m\le15\). Separate exhaustive labeled-event enumeration, decoding, and injectivity tests cover four small parameter pairs, supplemented by 1,008 seeded valid-permutation simulations at larger parameters. The checker also documents that the formula is not asserted at \(k=2,m=2\): the actual count is 16, not 20. Run `python3 verify.py` in a directory containing the standalone script; output is in `verify_output.txt`. These finite checks support, but do not replace, the all-parameter proof above.

## Relationship to prior work
Lipin and Volkov [1] define the automata \(\mathcal L_m^k\) in their adversarial-synchronization analysis and establish their relevant reset-length behavior. The exact minimum length is **prior work**, not claimed new here. The present statement concerns the previously unenumerated multiplicity of length-minimizing words and gives a structural event-order characterization. General shortest-reset-word algorithms [2] and factor-minimal reset-language results [3] do not themselves give this two-parameter factorial-over-six formula. Search of relevant mathematical-research records identified shortest-word counts for *different* automata (Wielandt-type, \(D_n\), and specific small-state examples), not an implication covering these letter actions. A later related conference treatment by the same authors [4] was identified, but only bibliographic metadata and its abstract could be read, so its full content remains a priority risk. Negative search results do not prove worldwide publication priority.

## Limitations
The theorem only covers the displayed automaton and \(m\ge1,k\ge2m-1\). A different count can occur below this threshold (for example \(k=m=2\)). It counts word multiplicity, not number of automata, game strategies, or all reset words of longer lengths. No independent validation or exhaustive publication-priority certification has been performed.

## References
1. A. E. Lipin and M. V. Volkov, *Adversarial Synchronization*, arXiv:2601.18362 (first public 26 January 2026), https://arxiv.org/abs/2601.18362 .
2. A. Kisielewicz, J. Kowalski and M. Szykuła, *Computing the shortest reset words of synchronizing automata*, Journal of Combinatorial Optimization (online 2013), https://doi.org/10.1007/s10878-013-9682-0 .
3. E. Rodaro, *Synchronizing automata and the language of minimal reset words*, arXiv:1708.04864 (2017), https://arxiv.org/abs/1708.04864 .
4. A. E. Lipin and M. V. Volkov, *Adversarial Synchronization and Reset Length*, CiE 2026, pages 358–373, DOI: 10.1007/978-3-032-31348-5_24 (abstract and metadata inspected; full text not inspected).
