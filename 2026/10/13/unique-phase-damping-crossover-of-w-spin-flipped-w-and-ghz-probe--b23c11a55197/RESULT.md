# Unique phase-damping crossover of W–spin-flipped-W and GHZ probes under fixed-axis sensing

## Finding
Fix an integer \(n\ge3\). Let \(|D_n^1\rangle\) and \(|D_n^{n-1}\rangle\) be normalized symmetric Dicke states with respectively one and \(n-1\) excitations. Prepare
\[
|\mathrm{WW}_n\rangle=\frac{|D_n^1\rangle+|D_n^{n-1}\rangle}{\sqrt2},\qquad
|\mathrm{GHZ}_n\rangle=\frac{|0^n\rangle+|1^n\rangle}{\sqrt2}.
\]
Independently dephase every qubit, multiplying each off-diagonal single-qubit matrix element by \(1-p\), for \(0\le p\le1\). Encode an unknown phase using \(\exp(-i\theta J_z)\), where \(J_z=\frac12\sum_{j=1}^n\sigma_z^{(j)}\). Define \(z=(1-p)^2\). The exact symmetric-logarithmic-derivative quantum Fisher information (QFI) for this fixed generator is
\[
\boxed{F_{\mathrm{WW}}(n,p)=
(n-2)^2z^{n-2}\frac{(n-1)(1+z)-(n-2)z^2}{1+(n-1)z}},
\qquad
\boxed{F_{\mathrm{GHZ}}(n,p)=n^2z^n}.
\]
At \(p=1\) both QFI values vanish. For every \(n\ge3\), there exists a **unique** \(p_c(n)\in(0,1)\) such that \(F_{\mathrm{WW}}(n,p_c(n))=F_{\mathrm{GHZ}}(n,p_c(n))\). It is the number \(p_c(n)=1-\sqrt{z_c(n)}\), where \(z_c(n)\in(0,1)\) is the unique root of the cubic
\[
(n-2)^2\bigl[(n-1)(1+z)-(n-2)z^2\bigr]
=n^2z^2\bigl[1+(n-1)z\bigr].
\]
The GHZ probe has larger fixed-axis QFI for \(0\le p<p_c(n)\); the W–spin-flipped-W probe has larger fixed-axis QFI for \(p_c(n)<p<1\). The crossover obeys the sharp mesoscopic law
\[
\boxed{\lim_{n\to\infty}np_c(n)=\frac12.}
\]
More precisely, for each fixed \(\lambda\ge0\), at \(p=\lambda/n\) and sufficiently large \(n\),
\[
\frac{F_{\mathrm{WW}}(n,\lambda/n)}{F_{\mathrm{GHZ}}(n,\lambda/n)}
=1+\frac{8\lambda-4}{n}+O_{\lambda}(n^{-2}),
\qquad
\frac{F_{\mathrm{GHZ}}(n,\lambda/n)}{n^2}\longrightarrow e^{-2\lambda}.
\]

## Assumptions and scope
The noise is independent, local, identical **pure phase damping**, represented on each qubit by the Kraus operators \(\sqrt{1-p}\,I\), \(\sqrt p\,|0\rangle\langle0|\), and \(\sqrt p\,|1\rangle\langle1|\). Noise occurs before phase imprinting. The parameter generator is **fixed** to \(J_z\); there is **no maximization over collective-spin directions**. QFI is the quantum measurement optimum for this fixed state family and encoding. The comparison does not assert that these probes are globally optimal among quantum states or encodings, or that the W–spin-flipped-W state outperforms GHZ after transverse-axis optimization. Boundary cases \(p=0\) and \(p=1\) are included as stated.

## Proof
1. **Exact channel output.** Index one-excitation strings by their unique excited site and \((n-1)\)-excitation strings by their unique empty site. The two sets are disjoint when \(n\ge3\). In this \(2n\)-dimensional support the noisy W–spin-flipped-W density matrix is
\[
\rho=\frac1{2n}\begin{pmatrix}A&B\\B&A\end{pmatrix},\quad
A=(1-z)I_n+z\mathbf1\mathbf1^{\mathsf T},\quad
B=z^{(n-2)/2}\bigl[(z-1)I_n+\mathbf1\mathbf1^{\mathsf T}\bigr].
\]
The entries follow from the exact Hamming distances: two distinct one-excitation strings differ at two bits; a one-excitation and an \((n-1)\)-excitation string with matching labels differ at \(n\) bits, and with different labels differ at \(n-2\) bits.

2. **Spectral reduction.** Matrices \(A\) and \(B\) commute. Their common uniform eigenvector has eigenvalues \(a_0=1+(n-1)z\) and \(b_0=z^{(n-2)/2}(n-1+z)\). Each of the remaining \(n-1\) eigenvectors has \(a_1=1-z\) and \(b_1=-z^{(n-2)/2}(1-z)\). On each two-dimensional paired block, the generator is diagonal with eigenvalue separation \(n-2\). The standard SLD formula gives block QFI \((n-2)^2b_j^2/(na_j)\) when \(0<p<1\). Summing the uniform and orthogonal blocks yields
\[
F_{\mathrm{WW}}=\frac{(n-2)^2z^{n-2}}n\left(
\frac{(n-1+z)^2}{1+(n-1)z}+(n-1)(1-z)\right),
\]
which simplifies algebraically to the boxed formula. Continuity establishes the endpoint values. The GHZ off-diagonal coherence is attenuated by \((1-p)^n\), so its two-level SLD formula is \(n^2(1-p)^{2n}=n^2z^n\).

3. **One and only one crossing.** For \(0<z\le1\), form
\[
R_n(z)=\frac{F_{\mathrm{WW}}}{F_{\mathrm{GHZ}}}
=\frac{(n-2)^2}{n^2}\frac{P_n(z)}{z^2[1+(n-1)z]},\quad
P_n(z)=(n-1)(1+z)-(n-2)z^2.
\]
Let \(B_n(z)=nP_n(z)/[1+(n-1)z]\). Direct differentiation gives
\[
zB_n'(z)-2B_n(z)=\frac{n(n-1)(1+z)}{[1+(n-1)z]^2}
\bigl[(n-2)z^2-(3n-4)z-2\bigr].
\]
For \(n\ge3\), the final quadratic is strictly negative for \(0<z\le1\): it starts at \(-2\), and its derivative is at most \(-n\) on the interval. Consequently \(R_n'(z)<0\). Moreover, \(R_n(z)\to\infty\) as \(z\downarrow0\), whereas \(R_n(1)=(n-2)^2/n^2<1\). The intermediate value theorem and strict monotonicity establish the unique cubic root and the inequalities. At the fully dephased endpoint \(p=1\), both QFI values equal zero; there is no strict advantage there.

4. **Sharp crossover scale.** For fixed bounded \(x\), direct expansion of the exact rational ratio at \(z=1-x/n\) yields
\[
R_n(1-x/n)=1+\frac{4x-4}{n}+O_x(n^{-2}).
\]
For any fixed \(0<\varepsilon<1\), substitution of \(x=1-\varepsilon\) and \(x=1+\varepsilon\) gives opposite signs relative to one for all sufficiently large \(n\). Uniqueness brackets \(n(1-z_c(n))\) between these two numbers, hence \(n(1-z_c(n))\to1\). Because \(1-\sqrt z=(1-z)/(1+\sqrt z)\), this gives \(np_c(n)\to1/2\). Finally at \(p=\lambda/n\), \(z=(1-\lambda/n)^2=1-2\lambda/n+O(n^{-2})\); substituting into the expansion proves the stated QFI ratio and GHZ limit.

## Verification
The companion `verify.py` constructs the entire computational-basis dephased state independently from Hamming distances, diagonalizes it, and computes QFI using the two-sided spectral SLD formula with no use of the block-reduction derivation. It compares this QFI with the displayed closed form for \(n=3,\ldots,12\) at ten dephasing strengths including both endpoints. It additionally checks the unique-root bracketing for these sizes, checks the crossover asymptotic numerically for larger sizes, and checks ratio monotonicity on a rationally specified parameter grid. Running `python verify.py` with the listed numerical dependency returns `VERIFY_OK 207`. These finite checks support—but do not replace—the all-size analytical proof.

For illustration, at \(n=12\) the unique threshold is approximately \(p_c(12)=0.0503737872539358\). At \(p=0.08\), the directional W–spin-flipped-W QFI is approximately \(24.0597\), versus \(19.4657\) for GHZ.

## Relationship to prior work
Sudha, Karthik, Akhilesh, and Usha Devi (2026, first public January 30) consider Dicke superpositions in noisy quantum metrology. Their Section III.2 defines precisely the phase-damping channel used here and compares W-superposition, GHZ, and near-optimal Dicke probes in finite-size plots, noting that a detailed analytical explanation is not provided. Li and Ren (2023) already study W–spin-flipped-W metrology, derive noiseless results, and supply optimized-over-axis phase-damping QFI formulas for three and four qubits. Those optimized expressions are **not** the fixed-\(J_z\) QFI in this theorem: in particular, a fully dephased state may retain transverse-axis QFI while its \(J_z\) QFI vanishes. Their previously observed qualitative noise sensitivity, and the GHZ damping formula known from earlier literature, are not claimed as discoveries here. Ren and Li (2023) additionally study particle-loss robustness, including noisy reduced states, a different question. The present claim consists solely of the closed all-size **fixed-axis** formula, the unique dephasing-strength crossover, and its sharp system-size limit.

## Limitations
The comparison is for a specific pair of probes, an idealized independent phase-damping channel, and fixed longitudinal phase encoding. It is not a claim of optimal metrology under free generator direction, adaptive protocols, quantum error correction, correlated noise, transverse encoding, finite-sample estimator performance, or experimental advantage. For a fixed nonzero dephasing probability, both QFI values tend to zero exponentially as qubit number grows even though their ratio has a definite ordering. The root in the cubic is characterized uniquely but not given as a radical expression. The proof is mathematical, with finite numerical cross-checks; no independent external review has been performed.

## References
1. Sudha, B. N. Karthik, K. S. Akhilesh, and A. R. Usha Devi, *Dicke superposition probes for noise-resilient Heisenberg and super-Heisenberg metrology*, arXiv:2601.23043 (first posted January 30, 2026), especially Section III.2 and equations (8), (29). https://arxiv.org/abs/2601.23043 .
2. Y. Li and Z. Ren, *Quantum metrology with an N-qubit W superposition state under noninteracting and interacting operations*, Physical Review A **107**, 012403 (2023), especially Section III.C.2 and equations (34)–(37). https://doi.org/10.1103/PhysRevA.107.012403 .
3. Z. Ren and Y. Li, *Characterizing entanglement robustness of an N-qubit W superposition state against particle loss from quantum Fisher information*, Results in Physics **53**, 106954 (2023). https://doi.org/10.1016/j.rinp.2023.106954 .
4. J. Ma, Y.-x. Huang, X. Wang, and C. P. Sun, *Quantum Fisher information of the Greenberger–Horne–Zeilinger state in decoherence channels*, Physical Review A **84**, 022302 (2011), with publisher erratum. https://doi.org/10.1103/PhysRevA.84.022302 .
