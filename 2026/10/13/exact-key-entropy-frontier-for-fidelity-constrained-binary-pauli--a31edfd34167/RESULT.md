# Exact key-entropy frontier for fidelity-constrained binary Pauli randomization
## Finding
Consider the pure binary-qubit setting of Nguyen, Dinh, and Trinh on the fidelity line. Let the two input Bloch vectors have angle \(\theta\in(0,\pi]\), and define
\[
C=\cos^2\!\left(\frac{\theta}{2}\right),\qquad
V=\sin^2\!\left(\frac{\theta}{2}\right),\qquad
\tau=2\eta-1.
\]
In the adapted Pauli frame, write the sensitive-direction contraction as \(\lambda_x\). For a prescribed cap \(t\in[0,1]\), impose
\[
|\lambda_x|\le t.
\]
On the source's fidelity line this is exactly the privacy requirement
\[
D_{1/2,1/2}\le -\log(1-Vt^2).
\]
Among all Pauli channels satisfying this privacy cap and utility at least \(\eta\), feasibility holds if and only if
\[
\tau\le C+tV.
\]
Whenever feasible, the minimum Shannon entropy, in bits, of the classical Pauli-key distribution is
\[
H_{\min}(t)=h_2\!\left(\frac{1-t}{2}\right),
\]
where
\[
h_2(q)=-q\log_2 q-(1-q)\log_2(1-q)
\]
with the usual endpoint convention. A minimizer uses only two gates:
\[
p_I=\frac{1+t}{2},\qquad p_Z=\frac{1-t}{2},\qquad p_X=p_Y=0.
\]
Thus the full four-Pauli optimization has an exact two-gate Shannon-randomness frontier.

At the source-optimal privacy radius, Theorem 4.3 gives
\[
a_*=\begin{cases}
0,&\tau\le C,\\
(\tau-C)/V,&\tau>C.
\end{cases}
\]
Setting \(t=a_*\) yields the exact least key entropy among all Pauli mechanisms attaining that optimal privacy value:
\[
H_{\mathrm{key,opt}}=h_2\!\left(\frac{1-a_*}{2}\right).
\]
Perfect pair erasure therefore costs exactly one Shannon bit, while relaxing privacy along the fidelity frontier decreases the optimal key entropy continuously toward zero.

## Assumptions and scope
The input states are two distinct pure qubit states with equal prior weights. The Pauli frame is adapted as in the source: the sensitive direction is the \(x\)-axis and the common direction, when nonzero, is the \(z\)-axis. The admissible mechanism class is the full qubit Pauli class in this frame. The utility is the source overlap utility and \(\eta\in[0,1]\). The result concerns the fidelity line \(\alpha=z=1/2\) only.

The entropy above is the Shannon entropy of the Pauli probability distribution. It is an asymptotic randomness rate under ordinary source coding; a value below one bit is not asserted to be a literal fractional fixed-length key for a single use.

## Proof
For a Pauli distribution \((p_I,p_X,p_Y,p_Z)\), the source gives
\[
\lambda_x=p_I+p_X-p_Y-p_Z,
\qquad
\lambda_z=p_I-p_X-p_Y+p_Z.
\]
Its adapted-frame utility for the pure pair is
\[
U=\frac12\bigl(1+\lambda_z C+\lambda_xV\bigr).
\]
The source's fidelity calculation gives, for the same pair,
\[
D_{1/2,1/2}=-\log(1-\lambda_x^2V).
\]
Hence \(|\lambda_x|\le t\) is exactly the stated privacy cap.

Since every Pauli channel has \(\lambda_z\le1\), the largest utility compatible with \(|\lambda_x|\le t\) is obtained at \(\lambda_x=t\) and \(\lambda_z=1\). Therefore feasibility is equivalent to
\[
\tau\le C+tV.
\]

Now partition the Pauli alphabet according to the sign with which conjugation acts on the adapted \(x\)-coordinate. Put
\[
q=p_Y+p_Z=\frac{1-\lambda_x}{2}.
\]
The Shannon chain rule for this two-class partition gives
\[
H(p)=h_2(q)+(1-q)H(p\mid\{I,X\})+qH(p\mid\{Y,Z\}),
\]
so
\[
H(p)\ge h_2\!\left(\frac{1-\lambda_x}{2}\right).
\]
Because binary entropy is symmetric and decreases as \(|\lambda_x|\) increases on \([0,1]\), every channel with \(|\lambda_x|\le t\) obeys
\[
H(p)\ge h_2\!\left(\frac{1-t}{2}\right).
\]
Equality is attained by
\[
(p_I,p_X,p_Y,p_Z)=\left(\frac{1+t}{2},0,0,\frac{1-t}{2}\right).
\]
For this channel, \(\lambda_x=t\) and \(\lambda_z=1\), so it is feasible whenever the feasibility inequality holds. This proves the all-parameter minimum.

Finally, the source's Theorem 4.3 states that the smallest sensitive contraction compatible with utility is \(a_*=0\) when \(\tau\le C\), and \(a_*=(\tau-C)/V\) otherwise. Substitution \(t=a_*\) proves the optimal-privacy specialization. In the zero-radius branch, \(a_*=0\), so the minimum is \(h_2(1/2)=1\) bit. At \(a_*=1\), the minimizing channel is the identity and the entropy is zero.

## Verification
The proof is analytic. The accompanying checker verifies the Pauli-contraction identities, the feasibility equality of the two-gate extremizer, the source-optimal specialization for representative angles and utility thresholds, and a finite simplex grid showing that no sampled feasible distribution violates the Shannon grouping lower bound. These computations are corroborative rather than a substitute for the entropy chain-rule proof.

## Relationship to prior work
Nguyen, Dinh, and Trinh formulate utility-constrained Pauli--Weyl randomization, explicitly note that admissible sets may encode key-randomness budgets, and prove the exact pure-binary fidelity frontier. Their Lemma 4.1 gives the Pauli probabilities realizing reduced contractions, and Theorem 4.3 gives the source-optimal sensitive contraction. The paper does not state a Shannon-key optimum or the full key-entropy/privacy/utility frontier above.

Bouda and Ziman studied Shannon key entropy for private quantum channels. For perfect single-qubit privacy they show that one bit is sufficient for any plaintext set not generating the whole state space, and for approximate privacy they optimize entropy for the entire Bloch sphere. The one-bit endpoint here is consistent with that earlier theorem. The present statement is different: it is pair-specific, uses the 2026 overlap-utility constraint and fidelity-line privacy radius, and gives the exact entropy at every allowed sensitive contraction. Ambainis and Smith's approximate-encryption constructions address uniform approximate randomization of arbitrary quantum messages and do not imply this binary utility-constrained frontier.

## Limitations
The claim does not address mixed binary inputs, more than two protected states, general \(\alpha\)-\(z\) parameters, arbitrary random-unitary alphabets, or non-Pauli channels. It minimizes Shannon entropy, not worst-case fixed-length key length or circuit cost. No claim is made that the two-gate mechanism remains entropy-optimal outside the full adapted Pauli class considered here.

## References
1. N. H. Minh, T. H. Dinh, and L. C. Trinh, *Utility-Constrained Pauli–Weyl Randomization for Robust Quantum \(\alpha\)-\(z\) Rényi Privacy*, DOI 10.21203/rs.3.rs-10148794/v1, posted 2026-07-03.
2. J. Bouda and M. Ziman, *Optimality of private quantum channels*, Journal of Physics A 40 (2007), 5415–5426, arXiv:0710.2004, DOI 10.1088/1751-8113/40/20/011.
3. A. Ambainis and A. Smith, *Small Pseudo-Random Families of Matrices: Derandomizing Approximate Quantum Encryption*, arXiv:quant-ph/0404075.
