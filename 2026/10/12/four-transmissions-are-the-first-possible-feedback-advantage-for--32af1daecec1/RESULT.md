# Four transmissions are the first possible feedback advantage for the qubit erasure channel
## Finding
For every blocklength \(n\in\{1,2,3\}\), every integer \(M\ge1\), and every message-independent distribution \((w_S)_{S\subseteq[n]}\) of survivor sets for qubit erasures, the optimal no-feedback average success probability equals the feedback-assisted optimum:
\[
P_{\mathrm{succ}}^{*,\mathrm{nf}}(n,M)
=
P_{\mathrm{succ}}^{*,\mathrm{fb}}(n,M)
=
\sum_{S\subseteq[n]}w_S\min\!\left\{1,\frac{2^{|S|}}{M}\right\}.
\]
Moreover, this equality is attained by deterministic computational-basis encodings; neither nonorthogonal states nor entanglement across the transmitted qubits is needed at these blocklengths.

For independent erasures with probability \(p\), the formula becomes
\[
\mathbb E\!\left[\min\!\left\{1,\frac{2^K}{M}\right\}\right],
\qquad K\sim\operatorname{Bin}(n,1-p).
\]
The primary source proves that for \(n=4\), \(M=4\), and every \(0<p<1\), the optimal no-feedback success probability is strictly below this feedback value, even with arbitrary mixed entangled codewords and a collective decoder. Therefore four transmissions are the first blocklength at which classical feedback can improve the optimum for the qubit erasure channel.

## Assumptions and scope
Messages are equiprobable and performance is average success probability. In the correlated-erasure statement, the survivor set \(S\subseteq[n]\) is sampled independently of the message and the receiver observes which systems were erased. The no-feedback optimization allows arbitrary quantum codewords and arbitrary collective decoding, exactly as in the primary source. The feedback comparison uses the source's model without initial shared entanglement. The result does not assert equality under maximum error without additional symmetrization, does not determine the four-use no-feedback optimum, and does not address input dimensions larger than two.

## Proof
Fix a deterministic binary code \(C=(c_m)_{m=1}^M\), allowing repeated codewords when \(M>2^n\). For a survivor set \(S\), let \(\pi_S(c_m)\) be the restriction of \(c_m\) to the surviving coordinates and define
\[
N_S(C)=\left|\{\pi_S(c_m):m\in[M]\}\right|.
\]
When the computational-basis encoding \(m\mapsto\lvert c_m\rangle\) is sent and exactly the coordinates in \(S\) survive, distinct projected words are orthogonal and are therefore identified perfectly. For each observed projected word, the best decoder chooses one message from its fiber. Since the messages are uniform, the conditional average success probability is exactly
\[
\frac{N_S(C)}{M}.
\]
The state-discrimination dimension bound used in the primary source gives, for every no-feedback quantum code and every fixed survivor pattern,
\[
P_{\mathrm{succ}}(S)\le \min\!\left\{1,\frac{2^{|S|}}{M}\right\}.
\]
Thus it is enough to construct, for each \(n\le3\) and every \(M\), one binary code satisfying
\[
N_S(C)=\min\{M,2^{|S|}\}
\qquad\text{for every }S\subseteq[n].
\]

For \(n=1\), use \(\{0\}\) when \(M=1\); for \(M\ge2\), include both \(0\) and \(1\), repeating either symbol as needed.

For \(n=2\), use respectively
\[
\{00\},\qquad
\{00,11\},\qquad
\{00,01,10\}
\]
for \(M=1,2,3\). For \(M\ge4\), include all four binary words, with repetitions when \(M>4\). The three-word code has both symbols in each one-coordinate projection and has three distinct full words, so it saturates every projection bound.

For \(n=3\), use
\[
\begin{aligned}
M=1:&\quad \{000\},\\
M=2:&\quad \{000,111\},\\
M=3:&\quad \{000,011,101\},\\
M=4:&\quad \{000,011,101,110\}.
\end{aligned}
\]
The \(M=3\) code has two symbols in every one-coordinate projection and three distinct words in every two-coordinate projection. The \(M=4\) code is the even-parity code: every one-coordinate projection has size two and every two-coordinate projection has size four. For \(5\le M\le8\), add any \(M-4\) unused cube vertices to the even-parity code. Its one- and two-coordinate projections remain saturated, while all full words are distinct. For \(M>8\), include all eight cube vertices and repeat arbitrary vertices for the remaining messages. Then every nonempty projection is saturated and the full projection has size eight. The empty projection has size one in all cases. This proves the displayed projection identity for every \(M\).

Consequently, for every message-independent erasure-pattern law, the same single no-feedback code attains the sectorwise dimension bound for every pattern simultaneously. Averaging gives
\[
P_{\mathrm{succ}}^{*,\mathrm{nf}}(n,M)
=
\sum_{S\subseteq[n]}w_S\min\!\left\{1,\frac{2^{|S|}}{M}\right\}.
\]
Corollary 4.3 of the primary source gives exactly the same quantity as the feedback-assisted optimum for message-independent correlated erasures. Finally, Theorem 6.1 of that source proves a strict gap for four qubit transmissions, four messages, and every nontrivial independent erasure probability. Hence the first possible feedback advantage occurs at blocklength four.

## Verification
The proof is finite and analytic: the only short-block constructions requiring inspection are the explicit \(M=3\) code for two coordinates and the \(M=3,4\) cores for three coordinates; all larger message sizes follow by saturation and repetition. A standalone standard-library checker enumerates every coordinate projection of the canonical constructions for representative message sizes and verifies the identity \(N_S(C)=\min\{M,2^{|S|}\}\). The checker is corroborative only; the all-\(M\) proof is the case analysis above.

## Relationship to prior work
Wilde proves the exact feedback-assisted formula, including the message-independent correlated-erasure extension, and proves a strict no-feedback gap for four qubit uses and four messages. The same paper gives several sufficient regimes in which the no-feedback dimension bound is attainable, including \(M\le d\), \(M\ge d^n\), and certain maximum-distance-separable constructions. It does not state that every message size is attainable for all qubit blocklengths \(n\le3\), nor does it state that four is the minimal blocklength for feedback advantage. The missing short cases include \(M=3\) at \(n=2\) and \(M\in\{3,5,6,7\}\) at \(n=3\).

Rosati's earlier no-feedback analysis derives the same numerical upper-bound family and gives nearly matching achievability through classical error-correcting codes. It explicitly notes the scarcity of nontrivial binary maximum-distance-separable codes and does not provide the all-message short-block exact formula above. The present argument instead uses the exact projection counts of a few small nonlinear binary codes.

## Limitations
The theorem is specific to qubit inputs and to at most three transmissions. It identifies the first blocklength at which feedback can help but does not compute the amount of the optimal four-use quantum no-feedback gap. It is an average-success statement; maximum-error equality without feedback is not claimed. The originality comparison cannot exclude an equivalent observation hidden in short-code tables or under orthogonal-array terminology, although targeted searches did not locate one.

## References
1. M. M. Wilde, *Finite-blocklength classical communication over the quantum erasure channel with and without classical feedback*, arXiv:2610.00440v1, 2026. See Theorem 4.1, Corollary 4.3, Theorem 6.1, Remark 6.3, and Section 9.2.
2. M. Rosati, *The n-shot classical capacity of the quantum erasure channel*, Journal of Physics Communications 8 (2024), 085005, DOI 10.1088/2399-6528/ad6f6b.
3. MSC2020, 81P45: Quantum information, communication, networks (quantum-theoretic aspects).
