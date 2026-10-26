# Finite thermodynamic limit of stabilizer Rényi entropy in the high-area Dyck–Fredkin phase

## Finding
For the colorless, spin-\(1/2\), area-weighted Dyck–Fredkin ground state of length \(2n\), fix a deformation \(t>1\) and a **real** stabilizer Rényi order \(\alpha>1\). Set \(q=t^{-2}\) and
\[
P(q)=\prod_{j=1}^{\infty}(1-q^j)^{-1}.
\]
Then the stabilizer Rényi entropy \(M_\alpha(n,t)\) has a finite thermodynamic limit \(L_\alpha(t)\), with the uniform bound
\[
0\le M_\alpha(n,t)\le\frac{2\alpha}{\alpha-1}\log_2 P(q)
\]
and the explicit finite-size estimate
\[
\left|M_\alpha(n,t)-L_\alpha(t)\right|
\le \frac{4\alpha P(q)^{2\alpha}\sqrt{2P(\sqrt q)}}{(\alpha-1)\ln 2}\,q^{n/4},\qquad n\ge1.
\]
In particular the finite limit exists and the convergence is exponentially fast in the half-chain length for every fixed \(t>1\), uniformly over chain sizes. **The theorem does not assert that the limit is strictly positive, nor does it cover \(t\le1\).** It makes the numerically observed bounded-phase saturation mathematically rigorous, and includes all real orders \(\alpha>1\), not just the even integer indices treated computationally in the motivating work.

## Assumptions and scope
A Dyck path \(w\) of semilength \(n\) is a word of \(n\) up-steps and \(n\) down-steps whose partial heights remain nonnegative. Encode up and down as the qubit computational states \(\lvert0\rangle\), \(\lvert1\rangle\). Its area \(A(w)\) is the sum of the heights after the first \(2n-1\) steps. Write
\[
\lvert\psi_n(t)\rangle
=\frac{1}{\sqrt{C_n(t)}}\sum_{w\in\mathcal D_n}t^{A(w)/2}\lvert w\rangle,
\qquad C_n(t)=\sum_{w\in\mathcal D_n}t^{A(w)}.
\]
The stabilizer Rényi entropy of a normalized pure state on \(N\) qubits is, for any real \(\alpha>1\),
\[
M_\alpha(\psi)=\frac{1}{1-\alpha}\log_2 F_\alpha(\psi),\qquad
F_\alpha(\psi)=2^{-N}\sum_{R\in\{I,X,Y,Z\}^{\otimes N}}
\bigl|\langle\psi\lvert R\rvert\psi\rangle\bigr|^{2\alpha}.
\]
We take \(N=2n\) when evaluating \(M_\alpha(n,t)\). Pure stabilizer product ancillas do not change this quantity, allowing centered embeddings between different chain lengths. The infinite product \(P(q)\) converges for \(0<q<1\).

## Proof
**1. Defect partitions.** The maximum-area path is \(0^n1^n\), with area \(n^2\). Let \(d(w)\) count pairs consisting of a down-step preceding a later up-step. Each adjacent exchange \(01\mapsto10\) lowers the area by \(2\), so
\[
A(w)=n^2-2d(w),\qquad C_n(t)=t^{n^2}Z_n(q),\quad
Z_n(q)=\sum_{w\in\mathcal D_n}q^{d(w)}.
\]
For the \(i\)-th up-step, let \(b_i\) be the number of preceding down-steps. Then \(0=b_1\le\cdots\le b_n\), with \(b_i\le i-1\) by the Dyck condition, and \(d(w)=\sum_i b_i\). Reversing this sequence gives a partition \(\lambda=(b_n,\ldots,b_1)\) satisfying \(\lambda_j\le n-j\); conversely each such partition reconstructs exactly one Dyck word. Thus
\[
Z_n(q)=\sum_{\lambda\subseteq(n-1,n-2,\ldots,1,0)}q^{\lvert\lambda\rvert}.
\]
These staircase sets are nested as \(n\) increases and exhaust all integer partitions. Therefore \(1\le Z_n(q)\uparrow P(q)\). If a partition of size \(k<n\) has \(\lambda_i>0\), then \(\lambda_i+i\le k+1\le n\), since its first \(i-1\) rows each contain at least one box. Consequently it fits the staircase. With \(p(k)\) denoting the integer partition number,
\[
0\le P(q)-Z_n(q)\le\sum_{k\ge n}p(k)q^k
\le q^{n/2}P(\sqrt q).
\]

**2. Aligned quantum states.** Padding a length-\(2n\) Dyck word by \(m-n\) zeros on the left and \(m-n\) ones on the right preserves its defect partition. Such padding is an isometric embedding into the length-\(2m\) Hilbert space and adjoins only stabilizer product qubits. In terms of defect partitions, the normalized amplitudes are \(q^{\lvert\lambda\rvert/2}/\sqrt{Z_n(q)}\). Hence, for \(m\ge n\), the embedded states have overlap
\[
\bigl|\langle\psi_n\mid\psi_m\rangle\bigr|^2
=\frac{Z_n(q)}{Z_m(q)}.
\]
Let \(\rho_n\) and \(\rho_m\) be their pure density matrices in the common Hilbert space. Then
\[
\lVert\rho_n-\rho_m\rVert_2
=\sqrt{2\left(1-\frac{Z_n(q)}{Z_m(q)}\right)}
\le\sqrt{2P(\sqrt q)}\,q^{n/4}.
\]
Here \(\lVert\cdot\rVert_2\) is the Hilbert–Schmidt norm.

**3. Dimension-free Pauli-moment continuity.** For two pure density matrices \(\rho,\sigma\) on the same \(N\)-qubit space, set \(a_R=\operatorname{Tr}(\rho R)\), \(b_R=\operatorname{Tr}(\sigma R)\). They lie in \([-1,1]\), and for any \(\alpha>1\),
\[
\bigl|\lvert a\rvert^{2\alpha}-\lvert b\rvert^{2\alpha}\bigr|
\le2\alpha\lvert a-b\rvert(\lvert a\rvert+\lvert b\rvert).
\]
Pauli orthogonality gives \(2^{-N}\sum_R a_R^2=\operatorname{Tr}\rho^2=1\) and similarly for \(\sigma\), while \(2^{-N}\sum_R(a_R-b_R)^2=\lVert\rho-\sigma\rVert_2^2\). Cauchy–Schwarz therefore yields
\[
\lvert F_\alpha(\rho)-F_\alpha(\sigma)\rvert
\le4\alpha\lVert\rho-\sigma\rVert_2.
\]
As a consequence \(F_\alpha(n,t)\) is Cauchy and has a limit, with error bounded by \(4\alpha\sqrt{2P(\sqrt q)}q^{n/4}\).

**4. Uniform positivity and the logarithm.** Let \(p_x\) be the computational-basis probabilities of \(\psi_n\). The mountain configuration has \(p_{0^n1^n}=1/Z_n(q)\). Restricting the Pauli sum defining \(F_\alpha\) to diagonal \(Z\)-strings and using Fourier orthogonality gives
\[
2^{-N}\sum_{b\in\{0,1\}^N}\langle Z^b\rangle^2
=\sum_x p_x^2\ge Z_n(q)^{-2}.
\]
Jensen's inequality applied to \(u\mapsto u^\alpha\) on \([0,1]\) then implies
\[
F_\alpha(n,t)\ge Z_n(q)^{-2\alpha}\ge P(q)^{-2\alpha}>0.
\]
Also \(F_\alpha\le F_1=1\), so the entropy is nonnegative and obeys the displayed uniform upper bound. On the interval \([P(q)^{-2\alpha},1]\), the function \(u\mapsto\log_2 u\) is Lipschitz with constant \(P(q)^{2\alpha}/\ln2\). Apply this to the moment Cauchy estimate and send \(m\to\infty\) to obtain exactly the announced exponential error bound for \(M_\alpha\). This completes the proof.

## Verification
The standalone `verify.py` enumerates Dyck paths for \(1\le n\le6\), verifies \(A(w)=n^2-2d(w)\), matches exact defect polynomials to staircase-partition counts, and evaluates the pure-state Pauli moment \(F_2\) numerically for \(1\le n\le4\) at \(q=1/4\). It checks the exact two-defect-state identity
\[
F_2(2,t)=1-\frac{4q(1-q)^2}{(1+q)^4}.
\]
To reproduce with Python 3 and NumPy, run `python verify.py` in this package. The script returns `All finite checks passed` when successful. The partition tail bound, all-order moment inequality, and thermodynamic limit are proved analytically above, not inferred from finite calculations.

## Relationship to prior work
Y. Lee, *Sub-extensive non-stabilizerness in the Dyck-Fredkin spin chain*, arXiv:2609.09545 (first posted September 9, 2026), defines the same weighted state and stabilizer Rényi entropies, provides exact finite-size dynamic programming at even integer indices, and presents **numerical evidence** for constant scaling when \(t>1\). It does not establish an all-real-order finite thermodynamic limit with an explicit uniform exponential finite-size error. O. Salberger et al., *Deformed Fredkin Spin Chain with Extensive Entanglement*, arXiv:1611.04983 (2016), establish the weighted ground state and use the partition/Young-diagram bound to prove an entanglement-entropy area law. The present argument takes that combinatorial control into the different Pauli-moment nonlinear functional and proves its uniform continuity and limit. T. Haug and L. Piroli, arXiv:2207.13076 (2022), develop matrix-product-state methods for stabilizer Rényi entropies; their transfer-matrix framework is not a statement covering these unbounded-bond-dimension staircase states at all real orders.

## Limitations
This theorem proves a finite limit and an explicit exponential approach, **not** a positive lower bound for the limiting entropy, an exact value for the limit, a sharp rate, or convergence uniform as \(t\downarrow1\) or \(\alpha\downarrow1\). The constant diverges near those endpoints. The result concerns only the colorless ground-state family, not colored Fredkin or Motzkin chains, excited states, gaps, or dynamical properties. Prior-art assessment is based on the identified papers and bounded searches, not a guarantee of priority.

## References
1. Y. Lee, *Sub-extensive non-stabilizerness in the Dyck-Fredkin spin chain*, arXiv:2609.09545, 2026. https://arxiv.org/abs/2609.09545
2. O. Salberger, T. Udagawa, Z. Zhang, H. Katsura, I. Klich, V. Korepin, *Deformed Fredkin Spin Chain with Extensive Entanglement*, arXiv:1611.04983, 2016. https://arxiv.org/abs/1611.04983
3. T. Haug, L. Piroli, *Quantifying nonstabilizerness of matrix product states*, arXiv:2207.13076, 2022. https://arxiv.org/abs/2207.13076
4. L. Leone, S. F. E. Oliviero, A. Hamma, *Stabilizer Rényi Entropy*, arXiv:2106.12587, 2021. https://arxiv.org/abs/2106.12587
