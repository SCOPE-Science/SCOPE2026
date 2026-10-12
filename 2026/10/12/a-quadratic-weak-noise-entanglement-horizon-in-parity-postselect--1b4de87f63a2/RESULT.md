# A quadratic weak-noise entanglement horizon in parity-postselected double-rail graph states

## Finding

A two-qubit Bell pair can be extracted from a redundantly connected graph state even when every entangling edge is independently erased with probability \(p\), but the length-independent *first derivative* of its conditional fidelity does not mean indefinite robustness. For the precise graph and heralded protocol below, let \(n\) be an even number of internal double-qubit layers, and let \(\rho_{n,p}\) be the corrected, conditioned terminal density matrix. Along every sequence \(p\downarrow0\), \(n\in2\mathbb N\), and \(np^2\to c\in[0,\infty)\), its computational-basis entries converge to

\[
\langle ab|\rho_c|a'b'\rangle=\frac{(-1)^{ab+a'b'}}4\begin{cases}
1,&a=a',\ b=b',\\
e^{-2c},&\text{exactly one of }a\ne a'\text{ and }b\ne b',\\
e^{-7c/2},&a\ne a',\ b\ne b'.
\end{cases}
\]

Here all endpoint bits lie in \(\{0,1\}\). In particular, the limiting overlap with the ideal two-qubit graph state and the limiting two-qubit negativity are, respectively,

\[
F(c)=\frac{1+2e^{-2c}+e^{-7c/2}}4,\qquad
\mathcal N(c)=\max\left\{0,\frac{2e^{-2c}+e^{-7c/2}-1}{4}\right\}.
\]

The unique solution \(c_*>0\) to \(2e^{-2c_*}+e^{-7c_*/2}=1\) is \(c_*\approx0.458661867647\). The limiting state is entangled for \(c<c_*\) and separable for \(c\ge c_*\). When \(np^2\to\infty\), the corrected conditional state instead converges to \(I_4/4\). For finite positive \(c\), the price of heralding is quantified by \(p\log P_{\mathrm{acc}}(n,p)\to-3c\); thus success probability tends to zero even in part of the surviving-entanglement regime. These are scaling-limit assertions, not exact finite-\(n\) threshold claims.

## Assumptions and scope

For every even integer \(n\ge2\), use two terminal qubits labeled \(L,R\) and \(n\) ordered internal layers, each with two qubits. Place two edges from \(L\) to layer 1, two from layer \(n\) to \(R\), and all four possible edges between each pair of neighboring internal layers; there are exactly \(4n\) nominal edges. Initialize every qubit in \(|+\rangle\). Independently retain each edge's controlled-\(Z\) gate with probability \(1-p\), or replace that gate by the identity with probability \(p\). The resulting preparation is a classical mixture, not a coherent amplitude-level erasure.

Measure every internal qubit in the Pauli-\(X\) basis. Retain a measurement record precisely when both measurements in each layer have the same sign \((-1)^{r_j}\) for \(r_j\in\{0,1\}\). On each accepted record apply the fixed, ideal-record byproduct correction \(Z_L^{\oplus_{j\ \mathrm{even}}r_j}Z_R^{\oplus_{j\ \mathrm{odd}}r_j}\). Sum the *unnormalized* corrected terminal density matrices over the accepted records and all edge-erasure configurations; only then normalize, giving \(\rho_{n,p}\). The reference state for even \(n\) is \(|G\rangle=(|00\rangle+|01\rangle+|10\rangle-|11\rangle)/2\). Define \(P_{\mathrm{acc}}\) as the unconditional probability of the accepted event. No information about the actual erasures is revealed or used for correction.

## Proof

**Exact sixteen-state reduction.** A pair of computational-basis assignments to one two-qubit layer is a four-bit state \(s=(z_1,z_2,\tilde z_1,\tilde z_2)\in\{0,1\}^4\). Write \(\pi(s)=z_1\oplus z_2\oplus\tilde z_1\oplus\tilde z_2\). Define \(P_e\) to be the diagonal projector onto \(\pi(s)=e\). Introduce the real symmetric transfer matrix and boundary column vectors

\[
T_{s,t}(p)=(2p-1)^{D(s,t)},\quad
D(s,t)=\sum_{i,j=1}^{2}\bigl((z_iw_j)\oplus(\tilde z_i\tilde w_j)\bigr),
\]
\[
\beta_{aa'}(s;p)=(2p-1)^{\sum_{i=1}^{2}\bigl((az_i)\oplus(a'\tilde z_i)\bigr)}
\]

for \(t=(w_1,w_2,\tilde w_1,\tilde w_2)\). These are exact because for each possibly missing controlled-\(Z\) edge, averaging its relative computational phase gives \(1\) if the two replica edge parities coincide, and \(2p-1\) otherwise. Summing the accepted equal-sign records gives the projector \(P_{b\oplus b'}\) at odd layers and \(P_{a\oplus a'}\) at even layers; this follows from the stated byproduct correction. Put \(n=2L\), \(e=a\oplus a'\) and \(f=b\oplus b'\). The exact, unnormalized entry, up to its common positive normalization, is

\[
\mathcal G_{ab,a'b'}=\beta_{aa'}^{\mathsf T}P_f
\bigl(P_fTP_eTP_f\bigr)^{L-1}
TP_e\beta_{bb'}.
\]

The physical acceptance probability and corrected state satisfy \(P_{\mathrm{acc}}=2^{-3n-2}\operatorname{tr}\mathcal G\) and \(\rho_{n,p}=\mathcal G/\operatorname{tr}\mathcal G\), with the latter trace taken in the two-terminal four-dimensional space. This finite expression holds for every allowed \(n,p\), including endpoints.

**Exact isolated-eigenvalue calculation.** Set \(A_{ef}=P_fTP_eTP_f\). At \(p=0\), for each \(e,f\in\{0,1\}\), \(A_{ef}(0)\) has rank one, its unique nonzero eigenvalue is 64, and its other fifteen eigenvalues vanish. To see the rank, in a fixed parity block write the original layer-bit parity as \(x\), the replica parity as \(x\oplus f\), and similarly \(y,y\oplus e\) at the neighboring layer. Then the noiseless block transfer sign is \((-1)^{ey+fx+ef}\), a separated product of signs. Its eight-by-eight singular value is 8. The isolated eigenvalue \(\lambda_{ef}(p)\) is therefore analytic near zero. Exact differentiation of the sixteen-by-sixteen matrices gives

\[
\begin{aligned}
\lambda_{00}(p)&=64-384p+1536p^2+O(p^3),\\
\lambda_{01}(p)=\lambda_{10}(p)&=64-384p+1280p^2+O(p^3),\\
\lambda_{11}(p)&=64-384p+1088p^2+O(p^3).
\end{aligned}
\]

For reproducibility, let \(T(p)=T_0+pT_1+p^2T_2+O(p^3)\) and \(A_{ef}=A_0+pA_1+p^2A_2+O(p^3)\), define \(E=A_0/64\), and take the trace. The coefficients are exactly \(\operatorname{tr}(EA_1)=-384\) and \(\operatorname{tr}(EA_2)+\operatorname{tr}(EA_1(P_f-E)A_1)/64\), the latter equal to the three displayed quadratic values. Every entry of \(T_j\) is an explicit integer \((-1)^D\binom Dj(-2)^j\), so the identities are finite exact arithmetic, reproduced in the independent verifier. At \(p=0\), a direct boundary contraction similarly gives \(\beta_{aa'}^{\mathsf T}P_fT_0P_e\beta_{bb'}=64(-1)^{ab+a'b'}\) for every choice of four endpoint bits.

**Joint weak-noise and large-length limit.** By continuity of the simple leading eigenspaces and decay of the remaining eigenvalues, the leading coefficient of each entry is \(64(-1)^{ab+a'b'}\lambda_{ef}(p)^{L-1}\), up to a factor \(1+O(p)\) near \(p=0\). Hence

\[
\log\frac{\lambda_{01}}{\lambda_{00}}=-4p^2+O(p^3),\quad
\log\frac{\lambda_{11}}{\lambda_{00}}=-7p^2+O(p^3).
\]

When \(np^2\to c<\infty\), multiplication by \(L-1\sim n/2\) gives \(-2c\) and \(-7c/2\); the denominator is asymptotically four equal diagonal terms. This proves the full entrywise limit. If \(np^2\to\infty\), both ratios tend to zero, giving \(I_4/4\). At \(c=0\) with bounded \(n\), use direct continuity at \(p=0\), with the same limit. For the heralding law, the diagonal-sector eigenvalue gives \(P_{\mathrm{acc}}=(1+O(p))(\lambda_{00}/64)^{L-1}\) whenever \(L\) increases, and \(\log(\lambda_{00}/64)=-6p+O(p^2)\). Thus \(p\log P_{\mathrm{acc}}\to-3c\) when \(0<c<\infty\).

**Entanglement boundary.** Let \(u=e^{-2c}\), \(v=e^{-7c/2}\). The limiting state is diagonal in the orthonormal graph-state \(Z\)-error basis with eigenvalues \((1+2u+v)/4\), \((1-v)/4\) twice, and \((1-2u+v)/4\). The two-qubit Bell-diagonal partial-transpose criterion says it is separable if and only if its largest eigenvalue is at most one half. This yields \(2u+v\le1\) and the negativity formula. The left side is continuous and strictly decreases from 3 to 0, proving uniqueness of the threshold.

## Verification

Run `python artifacts/verify.py` with the dependencies in `requirements.txt`. The executable reconstructs the complete exact integer Taylor matrices for all four parity sectors and checks all first- and second-order eigenvalue coefficients, all sixteen noiseless boundary contractions, 256 possible edge-erasure patterns times four accepted records at two layers against a directly propagated computational-basis circuit for four noise levels, and four explicit large-length comparisons. It also recomputes the partial-transpose negativity and the critical root. Its recorded terminal outcome is `VERIFY_OK 4 exact Taylor sectors, 16 exact boundary identities, 4096 weighted physical branches over 4 noise levels, 4 scaling limits, negativity, cutoff 0.458661867647`.

The analytic perturbation and transfer-product proof establishes the infinite statements; the numerical experiments alone would not. The verifier uses no source data beyond the mathematical definitions above.

## Relationship to prior work

Numajiri et al., *Phase Transitions and Noise Robustness of Quantum Graph States* (arXiv:2510.00548, first public 2025-10-01), initiated the recent statistical-mechanics/transfer-matrix focus on noise-induced graph-state crossovers, but study **unconditioned** whole-graph fidelities under local IID Pauli noise, not endpoint entanglement conditioned on parity outcomes after **edge omissions**. Trinh et al., *Full-Rank Noise Forbids Long-Range Entanglement Swapping* (arXiv:2609.11021, first public 2026-09-10), prove a general full-rank independent-link entanglement horizon, not this redundant, correlated graph-state extraction limit or its exact coefficient.

The older, directly relevant Szymański–Vandré–Gühne paper, *Useful entanglement can be extracted from noisy graph states* (arXiv:2402.00937, initial version 2024), introduced this crazy-graph family, the compatible measurement and erasure model, and its **length-independent first-order fidelity susceptibility**. Its Section 5 and Appendix B show robustness to isolated missing internal edges and finite-length numerical curves. Those premises are prior results, not new. The present claim concerns the previously unquantified joint limit \(p\to0\), \(n\asymp p^{-2}\), the complete two-terminal conditional state, its exact entanglement threshold, and the acceptance-cost exponent. A fixed-length first derivative cannot imply or determine those claims. No identified published statement or mathematical-record entry subsumes the quantitative scaling theorem; earlier implicit derivation remains a priority risk.

## Limitations

Only even-length, two-qubit-per-layer fully joined strips and the specified equal-sign \(X\)-measurement postselection are treated. The result does not claim a finite-length exact threshold, success at a fixed nonzero probability as \(p\to0\), optimality among other measurement/decoding strategies, or immunity to local state-preparation, measurement, or gate noise other than independent erasure of controlled-\(Z\) gates. In the critical scaling with positive \(c\), the accepted event becomes very rare. The two-terminal notion of entanglement is the standard bipartite partial-transpose criterion.

## References

1. T. Numajiri, S. Yamashika, T. Tanizawa, R. Yoshii, Y. Takeuchi, and S. Tsuchiya, *Phase Transitions and Noise Robustness of Quantum Graph States*, arXiv:2510.00548 (first posted 2025-10-01), https://arxiv.org/abs/2510.00548.
2. X. D. Trinh, N. Pardave, A. Huang, X. Meng, and N. Yu, *Full-Rank Noise Forbids Long-Range Entanglement Swapping*, arXiv:2609.11021 (first posted 2026-09-10), https://arxiv.org/abs/2609.11021.
3. K. Szymański, L. Vandré, and O. Gühne, *Useful entanglement can be extracted from noisy graph states*, arXiv:2402.00937 (initial version 2024), https://arxiv.org/abs/2402.00937, especially Section 5 and Appendix B.
