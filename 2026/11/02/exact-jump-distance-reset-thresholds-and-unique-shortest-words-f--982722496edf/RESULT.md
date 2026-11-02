# Exact jump-distance reset thresholds and unique shortest words for cyclic unitary automata

## Finding
For every integer \(n\ge 2\) and every integer \(1\le d<n\), consider the deterministic automaton with state set \(Q=\mathbb Z/n\mathbb Z\) and exactly two input letters. Letter \(b\) rotates states by \(b(x)=x+1\pmod n\); letter \(a\) fixes all nonzero states and sends \(a(0)=d\). A reset word is a finite word mapping all states to one state.

**Theorem.** This automaton admits a reset word if and only if \(\gcd(n,d)=1\). In the coprime case, its exact reset threshold is
\[
\ell(n,d)=1+(n-2)(n-d+1),
\]
and its **only** shortest reset word, as a literal word over the fixed alphabet \(\{a,b\}\), is
\[
w_{n,d}=a(b^{n-d}a)^{n-2}.
\]
The word sends every state to \(d\).

## Assumptions and scope
Both letters and the orientation of the cycle are fixed as defined above. Concatenated letters act on a state from left to right. The theorem covers \(n=2\) and \(d=n-1\), but does not assert uniqueness up to state relabelings or under exchanging generator conventions. No third input letter is allowed. The reset threshold is infinity when the machine does not synchronize.

## Proof

### 1. Modular obstruction
Put \(g=\gcd(n,d)\). Under \(a\), a state's residue modulo \(g\) does not change: the only moved state makes the jump \(0\mapsto d\), a multiple of \(g\). Under \(b\), every state's residue increases by one modulo \(g\). Therefore, after any common input word, the difference between the residues of any two trajectories modulo \(g\) remains their initial difference. If \(g>1\), trajectories starting at \(0\) and \(1\) can never coincide. Hence synchronization requires \(g=1\).

### 2. Necessary numbers of each letter
Suppose now that \(g=1\) and \(w\) is a reset word. Let \(A\) and \(B\) be the counts of its letters \(a\) and \(b\). For each initial state \(x\in Q\), let \(K_x\) denote the number of occurrences of \(a\) during which that individual trajectory is at state \(0\), and hence actually jumps from \(0\) to \(d\). A letter \(a\) applied when the trajectory is elsewhere fixes that trajectory. Consequently the final state of the trajectory from \(x\) is
\[
 x+B+dK_x\pmod n.
\]
All \(n\) final states coincide, so, since \(d\) is invertible modulo \(n\), the \(n\) nonnegative integers \(K_x\) occupy different residue classes modulo \(n\). There is therefore at least one trajectory with \(K_x\ge n-1\), which already implies \(A\ge n-1\).

Follow such a trajectory. Immediately after each effective \(a\) it is at state \(d\). Before its next effective \(a\), it must return to \(0\). During this interval, any other \(a\) acts trivially on that trajectory, and each \(b\) advances by one. Hence at least \(n-d\) occurrences of \(b\) must lie between consecutive effective uses of \(a\). These intervals are disjoint, so
\[
 B\ge(K_x-1)(n-d)\ge(n-2)(n-d).
\]
It follows that every reset word satisfies
\[
 |w|=A+B\ge(n-1)+(n-2)(n-d)=1+(n-2)(n-d+1).
\]
This argument also applies when \(n=2\), with zero intervening intervals.

### 3. Constructing a word meeting the bound
Let \(T=ab^{n-d}\). Direct calculation shows
\[
T(0)=0,\qquad T(x)=x-d\pmod n\quad(x\ne0).
\]
As \(\gcd(n,d)=1\), each initial state has a unique representation \(x=jd\pmod n\), where \(0\le j<n\). The map \(T\) decreases \(j\) by one until reaching \(0\), and then holds the state at zero. Hence \(T^{n-2}\) sends all starting states to \(0\) except the state with \(j=n-1\), which it sends to \(d\). A final \(a\) sends \(0\) to \(d\) and fixes \(d\). Thus
\[
 T^{n-2}a=(ab^{n-d})^{n-2}a=a(b^{n-d}a)^{n-2}
\]
resets the automaton to \(d\), has the claimed length, and meets the lower bound.

### 4. Literal uniqueness of the shortest word
If a reset word has that minimum length, the inequalities in Section 2 must all be equalities. In particular, \(A=n-1\), and the distinguished trajectory has exactly \(K_x=n-1\) effective \(a\)-jumps. Therefore **every** occurrence of \(a\) in the entire word is effective for this trajectory. It must start with \(a\), because any initial \(b\) would consume one of the exactly \((n-2)(n-d)\) available rotation letters outside the intervening intervals. Between successive occurrences of \(a\) there must be exactly \(n-d\) occurrences of \(b\), and no rotation letter may follow the final \(a\). Thus the literal word must be \(a(b^{n-d}a)^{n-2}\), proving uniqueness. For \(n=2\), equality forces the sole letter \(a\), as required.

## Verification
The standalone executable `verify.py` performs an **independent shortest-path computation in the subset automaton** for every \(2\le n\le11\) and \(1\le d<n\). It compares exact shortest lengths and counts of shortest words with the theorem and independently tests unsynchronizability for the non-coprime cases. It also generates the explicit reset witness through \(n=100\). The program reports `VERIFY_OK exhaustive_n=2..11 cases=55 sync=41 nonsync=14 witness_n=2..100 shortest_word_multiplicity=1`. The proof above, not finite enumeration, establishes the statement for arbitrary parameters.

## Relationship to prior work
Henk Don, *The Černý conjecture and 1-contracting automata* (2015), Proposition 2, proves that a circular automaton with a rank-deficient letter is synchronizing when the excluded-to-contracting distance is coprime to the cycle size; it gives the general upper bound \((n-1)^2\), not the jump-dependent exact optimum or unique optimal word established here. Igor Rystsov's *Černý's Conjecture for Automata with Simple Idempotents* (2022), Theorem 3, gives a uniform bound for automata with simple idempotents and a regular permutation group. Rystsov and Szykuła's *Primitive Automata that are Synchronizing* (2023), Section 4.2, characterizes synchronization for permutation/unitary-letter automata, again without this exact two-generator length and uniqueness classification. The classical Černý extremal corresponds to \(d=1\) under the present conventions, while the other coprime jumps yield systematically smaller thresholds. The general bounds and structural criteria are credited, not asserted to be new.

## Limitations
The originality comparison does not exclude an unlocated equivalent specialization in earlier literature, particularly in older studies of simple idempotents. A few older articles are available mainly through abstracts or incomplete text extraction, so independent bibliographic verification remains appropriate. The finite checker cannot certify arbitrary \(n\), whereas the proof does. This result concerns this explicit family only; it is not a statement about reset thresholds for arbitrary circular automata.

## References
- Henk Don, *The Černý conjecture and 1-contracting automata*, arXiv:1507.06070 (initial submission July 22, 2015), especially Proposition 2. https://arxiv.org/abs/1507.06070
- I. Rystsov, *Černý's Conjecture for Automata with Simple Idempotents*, *Cybernetics and Systems Analysis* 58 (2022), 1–7, DOI:10.1007/s10559-022-00428-3. https://doi.org/10.1007/s10559-022-00428-3
- Igor Rystsov and Marek Szykuła, *Primitive Automata that are Synchronizing*, arXiv:2307.01302 (first submitted July 3, 2023), especially Section 4.2. https://arxiv.org/abs/2307.01302
- Michalina Dzyga, Robert Ferens, Vladimir Gusev and Marek Szykuła, *Attainable Values of Reset Thresholds*, MFCS 2017, DOI:10.4230/LIPIcs.MFCS.2017.40. https://doi.org/10.4230/LIPIcs.MFCS.2017.40
