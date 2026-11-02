# Sharp three-state separation and an exact census for two-step binary rotations

## Finding
Let \(\Sigma=\{0,1\}\). For a word \(w=w_0\cdots w_{n-1}\in\Sigma^n\), let \(\rho_2(w)=w_2\cdots w_{n-1}w_0w_1\), and let \(\operatorname{sep}(u,v)\) be the smallest number of states in a complete deterministic finite automaton that accepts exactly one of \(u,v\). For \(n\ge3\), put \(R(n,2)=\max_{w\ne\rho_2(w)}\operatorname{sep}(w,\rho_2(w))\).

**Theorem.** Every distinct pair \(w,\rho_2(w)\) has separation complexity two or three. The exact worst-case values are \(R(3,2)=2\) and \(R(n,2)=3\) for all \(n\ge4\). For \(n\ge3\), the number \(C_n\) of labeled length-\(n\) words requiring three states is
\[
C_n=\begin{cases}
(5\cdot 2^{n-2}-8)/3,&n\text{ even},\\
(5\cdot 2^{n-2}-10)/3,&n\text{ odd}.
\end{cases}
\]
In particular \(C_n/2^n\to5/12\), and the same limit holds when sampling only words with \(w\ne\rho_2(w)\).

## Assumptions and scope
The alphabet is exactly binary; letters act as arbitrary total maps on the finite state set, with one designated initial state and an arbitrary set of accepting states. Rotation is leftward by exactly two positions and words are counted as labeled linear words, not necklaces. If two paths end at different states, selecting one state as accepting separates the pair; consequently exhaustive transition-map tests suffice. The empty word and equal rotated pairs are excluded from separation complexity. A one-state automaton never separates two words.

## Proof
**1. All two-state obstructions.** A total map on two states is either a permutation (identity or transposition) or a constant. For cyclic conjugates, both words have identical letter counts, so if both letter maps are permutations their actions agree. If both maps are constants, the output is determined by the last letter. If precisely one map is constant, its last occurrence resets the state, after which the other map is an identity or transposition. Thus for unequal binary conjugates \(u,v\) that contain both letters, a two-state automaton separates them if and only if their last letters differ, or their last letters agree and the lengths of their final constant-letter runs have different parity. This criterion also follows by directly considering all sixteen labeled transition pairs.

Write \(a=w_{n-1}\) and let \(s\) be the length of the final run of \(a\) in \(w\). The last letter of \(\rho_2(w)\) is \(w_1\). If \(w_1\ne a\), two states suffice. If \(w_0=w_1=a\) and \(w\) is nonconstant, the rotated suffix run is \(s+2\), so three states are necessary. If \(w_0\ne w_1=a\), the rotated suffix run is exactly one and three states are necessary precisely when \(s\) is odd (provided that \(w\ne\rho_2(w)\)). These are all cases.

**2. Explicit universal three-state witnesses.** Write a transformation as the tuple of its images of states \(0,1,2\), and define \(R=(1,2,0)\), \(T=(0,2,0)\), \(Z=(0,0,0)\). Consider four complete three-state transition tables, written as their maps on letters \(0,1\):
\[
(T,R),\quad(R,T),\quad(Z,R),\quad(R,Z).
\]
All have initial state zero. For an unequal word pair, a table separates it whenever the two final states differ, by choosing one of those final states as accepting.

Write \(w=AB\) with \(|A|=2\), so \(\rho_2(w)=BA\). If \(A=aa\), choose the table in which the letter \(a\) acts as the three-cycle \(R\) and the other letter acts as \(Z\). If \(B\) contains the other letter, let \(r\) be the number of terminal \(a\)'s in \(B\). Reading \(AB\) ends at \(R^r(0)\), whereas reading \(BA\) ends at \(R^{r+2}(0)\). They differ. If \(B\) contains no other letter, the two words coincide.

For \(A\in\{01,10\}\), the first two tables already suffice. The following finite-state lemma is used, with a complete and independently replayable transition certificate in `certificate.tsv`.

**Finite commutation lemma.** For either \(A=01\) or \(A=10\) and every finite binary \(B\), the two tables \((T,R)\) and \((R,T)\), both started at state zero, have equal terminal states on \(AB\) and \(BA\) simultaneously if and only if \(B\in A^*\).

Here is a full finite proof of the lemma. For each table \(i=1,2\), write \(a_i\) for the transformation induced by \(A\). After reading \(B\), record \((p_i,q_i)=(\delta_i(a_i(0),B),\delta_i(0,B))\). The two outputs are \(p_i\) and \(a_i(q_i)\). Appending a symbol applies its transformation to both entries, so the quadruple \((p_1,q_1,p_2,q_2)\) evolves deterministically. In parallel, a three-state pattern recognizer records whether \(B\) is at an even or odd position in the alternating language \(A^*\), or has irrevocably deviated from that language. Its states are phase zero, phase one, and dead: phase zero expects the first letter of \(A\), phase one the second, and any wrong letter enters dead. Phase zero is exactly \(B\in A^*\).

The reachable product has exactly **31 states** for each choice of \(A\). In the complete certificate, the phase counts are \(2,2,27\). Every state has both labeled outgoing edges inside the tabulated set, and comparison \(p_1=a_1(q_1)\) together with \(p_2=a_2(q_2)\) holds exactly at the two phase-zero states, never at the other 29. These assertions are verified row by row in `certificate.tsv`, whose fields give all four coordinates, the phase, the comparison, and both successor indices. The companion `verify.py` reconstructs all reachable tuples and checks exact equality with every certificate row. Since the table is closed under both input letters, this finite verification proves the lemma for arbitrarily long \(B\), not merely for the tested lengths. Finally, binary words \(A,B\) commute freely when \(|A|=2\) and \(A\) is alternating precisely if \(B\in A^*\): equality \(AB=BA\) forces each successive two-letter block of \(B\) to equal \(A\), and permits no final unpaired symbol. Thus every unequal \(AB,BA\) is separated by a listed three-state table.

**3. Exact census.** In the first three-state case \(w_0=w_1=w_{n-1}=a\), there are \(2^{n-2}-2\) nonconstant words. In the other case \(w_0=b\ne a=w_1=w_{n-1}\), require an odd terminal run of \(a\) and exclude the two alternating words when \(n\) is even. For terminal length \(s\le n-3\), odd, the preceding letter is forced to be \(b\); the count for each choice of \(a\) is \(2^{n-s-3}\). At even \(n\), the two additional words \(ba^{n-1}\) exactly balance the two excluded alternating words. Hence the second case contributes
\[
2\sum_{j=0}^{\lfloor(n-4)/2\rfloor}2^{n-4-2j}.
\]
Adding the first case and summing the geometric progression gives the displayed even and odd formulas. At \(n=3\) the count is zero. For each \(n\ge4\), the explicit nonconstant word \(0010^{n-3}\) lies in the first case and therefore needs three states; hence the stated maxima. The number of rotation-fixed binary words is at most four, so removing them does not change the limiting fraction.

## Verification
Run `python3 verify.py` beside `certificate.tsv`. It checks the closed 31-state product transition certificate for each alternating two-letter prefix and independently enumerates all 16 labeled two-state transition pairs for every binary word of lengths three through fourteen. It also tests the four explicit three-state witnesses on each unequal pair and checks the count formula. In total it independently evaluates 32,724 unequal rotation pairs. The successful output is included in `verification_output.txt`. The finite enumeration is a diagnostic; the infinite upper bound follows from the closed 31-state lemma, not from the word-length cutoff.

## Relationship to prior work
Demaine, Eisenstat, Shallit and Wilson (2011) defined this exact separating-word invariant and gave the three-state example `0010` versus `1000`, which is the smallest nontrivial instance here. Their general near-suffix arguments do not give a length-independent sharp classification for all two-step rotations. Nicol (2026) defined \(R(n,k)\) for conjugate words and proved the explicit upper bound \(R(n,k)\le2\min(k,n-k)+1\); at \(k=2\), this gives five states, not the sharp three states or exact three-state census. Tran (2023) studied the stronger every-start-state condition and global extremal profiles rather than this pairwise cyclic-shift invariant. The separate state complexity of the *language of all conjugates of a word* is not the same invariant as the size of a DFA separating one prescribed pair.

## Limitations
The exact classification is only for binary words rotated by two positions, not rotations by arbitrary \(k\) or larger alphabets. It does not determine minimum automata counts or nondeterministic separation. The finite commutation lemma is checked by an exhaustive 31-state closure with the complete table provided for scrutiny. No independent mathematical review has been performed, and unindexed equivalent results remain a publication-priority risk.

## References
- E. D. Demaine, S. Eisenstat, J. Shallit, D. A. Wilson, *Remarks on Separating Words*, arXiv:1103.4513v1 (public March 23, 2011), https://arxiv.org/abs/1103.4513.
- J. W. Nicol, *Further Remarks on Separating Words*, arXiv:2608.30928v1 (public August 31, 2026), https://arxiv.org/html/2608.30928v1.
- N. Tran, *Separating Words from Every Start State with Horner Automata*, arXiv:2309.02766 (public September 6, 2023), https://arxiv.org/abs/2309.02766.
- D. Gabric, S. Holub, J. Shallit, *Maximal State Complexity and Generalized de Bruijn Words*, arXiv:1903.05442 (2019), https://arxiv.org/abs/1903.05442.
