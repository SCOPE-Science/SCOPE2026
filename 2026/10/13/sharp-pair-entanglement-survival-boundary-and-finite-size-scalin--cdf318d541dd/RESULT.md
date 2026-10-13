# Sharp pair-entanglement survival boundary and finite-size scaling for lossy Dicke states

## Finding
For an initially pure symmetric \(N\)-qubit Dicke state with exactly \(k\) excitations, subjected independently to the standard zero-temperature amplitude-damping channel on every qubit, the pairwise concurrence has an exact threshold and two sharply distinct large-system scaling regimes. Define
\[
 A=\frac{(N-k)(N-k-1)}{N(N-1)},\qquad B=\frac{k(N-k)}{N(N-1)},\qquad D=\frac{k(k-1)}{N(N-1)}.
\]
Then every two-qubit marginal has concurrence
\[
 C_{N,k}(q)=2q\max\{0,B-\sqrt{D a(q)}\},\qquad a(q)=1-\frac{2kq}{N}+Dq^2.
\]
For every \(N\ge2\) and \(1\le k<N\), the initial concurrence is strictly positive. It remains strictly positive for **every** \(0<q\le1\) exactly when
\[
 k=1\quad\text{or}\quad k(N-k)^2\ge N(N-1)(k-1).
\]
If \(k\ge2\) and the latter inequality is reversed, there is a unique sudden-death boundary \(q_c\in(0,1)\):
\[
 q_c=\frac{k/N-\sqrt{(k/N)^2-D+B^2}}{D},\qquad C_{N,k}(q)>0\ \Longleftrightarrow\ q>q_c.
\]
At \(q=0\), concurrence is zero in all cases; a zero-threshold case means strictly positive concurrence for all \(q>0\), not at the limiting vacuum.

Let \(K_N\) be the largest \(k\in\{1,\ldots,N-1\}\) whose concurrence survives all \(q>0\). Then
\[
 \lim_{N\to\infty}\frac{K_N}{\sqrt N}=\frac1{\sqrt2}.
\]
More precisely, for any integers \(k_N\) with \(k_N/\sqrt N\to c\in(0,\infty)\) and fixed \(q\in[0,1]\),
\[
 \lim_{N\to\infty}N C_{N,k_N}(q)=q\max\{0,1-2c^2(1-q)\}.
\]
For \(k_N/N\to\alpha\in(0,1)\) and any fixed \(s\ge0\), the separate thin-boundary-layer law is
\[
 \lim_{N\to\infty}N C_{N,k_N}(1-s/N)=\max\{0,1-2\alpha^2s\},\qquad
 \lim_{N\to\infty}N(1-q_c)=\frac1{2\alpha^2}.
\]
In particular, macroscopically occupied Dicke states have pair-entanglement loss tolerance of order \(1/N\), while low-excitation families below a sharp square-root threshold retain positive pair entanglement through every finite positive survival probability.

## Assumptions and scope
Take integers \(N\ge2\), \(1\le k\le N-1\), define \(|D_N^k\rangle=\binom Nk^{-1/2}\sum_{|x|=k}|x\rangle\), and apply the same independently acting channel \(\mathcal A_q\) to each qubit, \(0\le q\le1\), with Kraus operators \(E_0=|0\rangle\langle0|+\sqrt q|1\rangle\langle1|\) and \(E_1=\sqrt{1-q}|0\rangle\langle1|\). The pairwise observable is Wootters concurrence of a two-qubit reduced density matrix. No collective emission, thermal excitation, interaction or correlated loss is assumed. Quantifiers in all asymptotic statements are for every integer sequence obeying the stated ratio convergence. The \(1-s/N\) expression is used for sufficiently large \(N\) so that its argument lies in \([0,1]\).

## Proof
**Two-site marginal.** Count Dicke computational basis strings according to their first two bits. The two-site reduced density matrix in the \((00,01,10,11)\) basis is
\[
 \rho_2(1)=\begin{pmatrix}A&0&0&0\\0&B&B&0\\0&B&B&0\\0&0&0&D\end{pmatrix},
 \qquad A+2B+D=1.
\]
Local trace preservation ensures that tracing after the \(N\)-fold channel equals applying \(\mathcal A_q\otimes\mathcal A_q\) to this marginal. It gives
\[
 \rho_2(q)=\begin{pmatrix}a(q)&0&0&0\\0&b(q)&qB&0\\0&qB&b(q)&0\\0&0&0&q^2D\end{pmatrix},
\]
where \(a(q)=A+2(1-q)B+(1-q)^2D=1-2qk/N+q^2D\), \(b(q)=qB+q(1-q)D\). This matrix is normalized, positive and real. The two-qubit \(X\)-state concurrence formula reduces to \(C=2\max\{0,|\rho_{01,10}|-\sqrt{\rho_{00,00}\rho_{11,11}}\}\), yielding the asserted formula (the other anti-diagonal coherence vanishes).

**Exact threshold.** Write \(E=B^2-AD\). Direct simplification gives the strict inequality
\[
 E=\frac{k(N-k)}{N^2(N-1)}>0.
\]
Thus every undamped state in this domain is pair-entangled, including \(k=1\). For \(k=1\), \(D=0\), hence \(C=2qB\). For \(k\ge2\), \(a'(q)=-2k/N+2Dq<0\) on \([0,1]\), since \(D<k/N\). Therefore \(B^2-Da(q)\) increases strictly with \(q\), is \(E>0\) at \(q=1\), and has initial limiting value \(B^2-D\) at \(q=0\). If \(B^2\ge D\), this quantity is positive at every \(q>0\). Otherwise there is exactly one zero \(q_c\in(0,1)\), and solving the quadratic yields the displayed expression. For \(k\ge2\), \(B^2\ge D\) is algebraically equivalent to \(k(N-k)^2\ge N(N-1)(k-1)\). The special case \(N=4,k=2\) gives \(q_c=3-\sqrt7\).

**Square-root cutoff.** For real \(1<k<N\), the ratio
\[
 \frac{B^2}{D}=\frac{k(N-k)^2}{N(N-1)(k-1)}
\]
is strictly decreasing in \(k\), since its logarithmic derivative is \(-1/[k(k-1)]-2/(N-k)<0\). Its expansion when \(k/\sqrt N\to c>0\) is
\[
 \frac{B^2}{D}=1+\frac{1/c-2c}{\sqrt N}+o(N^{-1/2}).
\]
Comparison with one proves the cutoff limit \(K_N/\sqrt N\to1/\sqrt2\), including integer rounding effects.

**Critical-scale concurrence profile.** Set \(k/\sqrt N\to c>0\). Uniformly for fixed \(q\), \(B\sim cN^{-1/2}\), \(D\sim c^2N^{-1}\), and
\[
 B^2-Da(q)=[c-2c^3(1-q)]N^{-3/2}+o(N^{-3/2}).
\]
Use the *exact* identity \(B-\sqrt{Da}=(B^2-Da)/(B+\sqrt{Da})\), whose denominator is \(2cN^{-1/2}+o(N^{-1/2})\); multiplication by \(2q\) and the positive part proves the first scaling law, including the zero region.

**Macroscopic-density boundary layer.** If \(k/N\to\alpha\in(0,1)\), then \(B\to\alpha(1-\alpha)>0\), \(D\to\alpha^2\), and \(E=\alpha(1-\alpha)/N+o(N^{-1})\). At \(q=1-s/N\), exact algebra gives
\[
 B^2-Da(q)=E-\frac{2s}{N}DB-\frac{s^2}{N^2}D^2
 =\frac{\alpha(1-\alpha)(1-2\alpha^2s)}{N}+o(N^{-1}).
\]
The same rationalization gives \(N C\to[1-2\alpha^2s]_+\). At the unique critical loss \(\varepsilon_c=1-q_c\), the equation \(E=2\varepsilon_c DB+\varepsilon_c^2D^2\) has positive root
\[
 \varepsilon_c=\frac{E}{D(\sqrt{B^2+E}+B)},
\]
so \(N\varepsilon_c\to1/(2\alpha^2)\). These are limits of exact finite-system formulas, not finite-enumeration extrapolations.

## Verification
A standalone NumPy verifier `verify.py` independently constructs Dicke vectors and traces out the other qubits for \(2\le N\le7\), compares the result before and after applying explicit two-qubit Kraus operators, and compares eigenvalue-based Wootters concurrence against the formula at multiple rational survival probabilities. It also exhaustively checks the stated integer identities with exact `fractions.Fraction` arithmetic for \(2\le N\le64\) and samples large-system limits. Execute with `python verify.py` from the extracted file directory. All asymptotic and all-\(N\) conclusions are analytic, not inferred from these tests.

## Relationship to prior work
Barnea et al. [1] define precisely the independently lossy Dicke-state channel and analyze Bell nonlocality under excitation or particle loss. Their seven-page paper, including its W-state and general-Dicke discussions, does not state the full two-site concurrence survival classification or the two scaling profiles. Xi et al. [2] derive correlations and concurrence/entanglement of formation for undamped Dicke reductions and superpositions, supplying complementary initial-state context rather than the damping threshold. Sohbi et al. [3] treat amplitude/phase damping of symmetric states with multipartite Bell-nonlocality tests, a different predicate. Huang and Zhu [4] supply general two-qubit amplitude-damping entanglement-sudden-death criteria: the elementary concurrence test used here is not claimed novel. The contribution assessed here is the *Dicke-index phase transition* and the distinct universal \(\sqrt N\) and \(N\)-density finite-size scaling laws. A source with an equivalent specialization or asymptotic analysis could affect priority.

## Limitations
This is not a threshold for multipartite entanglement or Bell nonlocality; pairwise concurrence may vanish while other quantum correlations persist. It does not apply to common reservoirs or cooperative Dicke superradiance. The full text of Huang and Zhu [4] was not obtained and may contain closely related formulas. The published-literature comparisons do not certify worldwide or unpublished priority. At \(q=0\), the state is vacuum and has zero concurrence, even in the all-finite-time-survival branch.

## References
[1] T. J. Barnea, G. Pütz, J. B. Brask, N. Brunner, N. Gisin, Y.-C. Liang, *Nonlocality of W and Dicke states subject to losses*, arXiv:1412.5953v1 (first public 2014-12-18), https://arxiv.org/abs/1412.5953.

[2] X. Xi et al., *Pairwise Quantum Correlations for Superpositions of Dicke States*, arXiv:1110.0101v2, https://arxiv.org/abs/1110.0101.

[3] A. Sohbi et al., *Decoherence Effects on the Non-locality of Symmetric States*, arXiv:1411.4489v1, https://arxiv.org/abs/1411.4489.

[4] J.-H. Huang and S.-Y. Zhu, *Necessary and sufficient conditions for the entanglement sudden death under amplitude damping and phase damping*, Physical Review A **76**, 062322 (2007), doi:10.1103/PhysRevA.76.062322.
