# Sharp discrimination memory between isospectral exceptional and Pauli qubit channels

## Finding

Fix \(0<\lambda<1\), and choose \(\theta\in(0,\pi/2)\) by
\[\cos\theta=\frac{2\lambda}{1+\lambda^2},\qquad
\sin\theta=\frac{1-\lambda^2}{1+\lambda^2}.\]
Let \(U_\theta=\exp(-i\theta\sigma_y/2)\), and define the exceptional qubit channel
\[\Phi_\lambda(X)=K_0XK_0^\dagger+K_1XK_1^\dagger,\quad
K_0=\sqrt{\frac{1+\lambda^2}{2}}U_\theta,\quad
K_1=\sqrt{\frac{1-\lambda^2}{2}}U_\theta\sigma_z.\]
Define a Pauli channel \(\Psi_\lambda\) with probabilities
\[p_I=\frac{(1+\lambda)^2}{4},\quad p_y=\frac{(1-\lambda)^2}{4},\quad
p_x=p_z=\frac{1-\lambda^2}{4}\]
acting as \(\Psi_\lambda(X)=\sum_{a\in\{I,x,y,z\}}p_a\sigma_a X\sigma_a\), with \(\sigma_I=I\).

These are CPTP channels with the **same superoperator eigenvalues** \(\{1,\lambda^2,\lambda,\lambda\}\); \(\Phi_\lambda\) is defective, whereas \(\Psi_\lambda\) is diagonalizable. For every integer \(n\ge1\), their exact, unhalved diamond-norm distance is
\[\boxed{\|\Phi_\lambda^n-\Psi_\lambda^n\|_\diamond
=n(1-\lambda^2)\lambda^{n-1}.}\]
An unentangled pure-qubit input and a single two-outcome projective qubit measurement achieve this norm, regardless of \(n\). For equally likely channels and **one uninterleaved \(n\)-fold transformation**, the maximal discrimination success probability, even permitting a passive entangled ancilla and arbitrary final joint measurement, is
\[P_{\rm succ}(n,\lambda)=\frac12+\frac14 n(1-\lambda^2)\lambda^{n-1}.\]
Writing \(q_\lambda=\lambda/(1-\lambda)\), the optimal positive integer \(n\) is \(\lceil q_\lambda\rceil\), with the additional tied optimizer \(q_\lambda+1\) precisely if \(q_\lambda\) is an integer. As \(\lambda\uparrow1\), if \(n(1-\lambda)\to s\in(0,\infty)\), the diamond distance converges to \(2s e^{-s}\), and the optimal-distance limit is \(2/e\). Thus the individual one-step channels become arbitrarily close to the identity while their appropriately repeated dynamics remain distinguishable with nonzero limiting advantage.

## Assumptions and scope

The diamond norm is the completely bounded trace norm: \(\|T\|_\diamond=\sup_{k\ge1}\sup_{\|X\|_1=1}\|(T\otimes\mathrm{id}_k)(X)\|_1\). No Markovian divisibility assumption is made. The powers mean sequential application of the **same** channel with no intervening operations. All results concern finite-dimensional qubit channels, \(0<\lambda<1\), and finite \(n\ge1\); the final expression concerns the specified joint limit. The source channel is the explicit qubit exceptional-point model of Brandão (2026); the isospectral physical Pauli comparator and the sharp operational optimization are specified here.

## Proof

**Physicality and equal spectra.** The two displayed Kraus operators satisfy \(K_0^\dagger K_0+K_1^\dagger K_1=I\). The Pauli probabilities are nonnegative and sum to one. Write any trace-one Hermitian qubit operator as \(X=(I+\mathbf r\cdot\boldsymbol\sigma)/2\). In \((x,y,z)\)-Bloch coordinates, the two maps are \(\mathbf r\mapsto M\mathbf r\) and \(\mathbf r\mapsto D\mathbf r\), where
\[D=\operatorname{diag}(\lambda,\lambda^2,\lambda),\qquad
M=D+b\,\mathbf u\mathbf v^{\mathsf T},\]
\[b=\frac{1-\lambda^2}{1+\lambda^2},\quad
\mathbf u=(1,0,\lambda)^{\mathsf T},\quad
\mathbf v=(-\lambda,0,1)^{\mathsf T}.\]
Directly substituting \(\cos\theta\) and \(\sin\theta\) in the rotated-dephasing Bloch matrix gives this decomposition. Since \(D\mathbf u=\lambda\mathbf u\), \(\mathbf v^{\mathsf T}D=\lambda\mathbf v^{\mathsf T}\), and \(\mathbf v^{\mathsf T}\mathbf u=0\), the perturbation \(N=b\mathbf u\mathbf v^{\mathsf T}\) is nonzero, square-zero and commutes with \(D\). It changes neither the characteristic polynomial nor the eigenvalues; on the \(x,z\) plane it creates a size-two Jordan block at \(\lambda\). The Pauli map is diagonal.

**Exact power difference.** The nilpotence and commutation give, for every positive integer \(n\),
\[M^n-D^n=n\lambda^{n-1}b\,\mathbf u\mathbf v^{\mathsf T}.\]
The identity components of both channels agree. Thus their difference \(T_n=\Phi_\lambda^n-\Psi_\lambda^n\), extended complex-linearly to arbitrary operators, is
\[T_n(X)=c_n\operatorname{Tr}(A X)B,\quad
c_n=\frac{n\lambda^{n-1}b}{2},\quad
A=\mathbf v\cdot\boldsymbol\sigma,\quad B=\mathbf u\cdot\boldsymbol\sigma.\]
This follows from \(\operatorname{Tr}(\sigma_jX)\) being the Bloch-coordinate functional on the traceless part.

**Diamond-norm upper bound.** For every ancillary dimension and trace-class input \(Y\),
\[(T_n\otimes\mathrm{id})(Y)=c_n B\otimes \operatorname{Tr}_{\rm qubit}[(A\otimes I)Y],\]
with harmless rearrangement of tensor factors. Trace-norm duality gives
\[\|\operatorname{Tr}_{\rm qubit}[(A\otimes I)Y]\|_1
\le\|A\|_\infty\|Y\|_1.\]
Both \(A\) and \(B\) are traceless Hermitian Pauli combinations with eigenvalues \(\pm\sqrt{1+\lambda^2}\). Therefore \(\|A\|_\infty=\sqrt{1+\lambda^2}\), \(\|B\|_1=2\sqrt{1+\lambda^2}\), and
\[\|T_n\|_\diamond\le |c_n|\|A\|_\infty\|B\|_1
=n\lambda^{n-1}(1-\lambda^2).\]

**Saturation without an ancilla.** Choose the pure input state with Bloch vector \(\mathbf v/\sqrt{1+\lambda^2}\). Its output difference is a scalar multiple of \(B\) and has trace norm exactly the preceding upper bound. Measuring the spin observable \(B/\sqrt{1+\lambda^2}\) is its optimal Helstrom measurement (with outcome labels swapped if appropriate). No ancilla can increase the distance. With equal priors, Helstrom's formula yields \(P_{\rm succ}=1/2+\|T_n\|_\diamond/4\).

**Exact optimal repetition count and crossover.** Let \(d_n=n(1-\lambda^2)\lambda^{n-1}\). Then
\[\frac{d_{n+1}}{d_n}=\lambda\frac{n+1}{n}.\]
This is above, equal to, or below one according as \(n\) is below, equal to, or above \(q_\lambda=\lambda/(1-\lambda)\), giving the stated complete optimizer list. Set \(\varepsilon=1-\lambda\). If \(n\varepsilon\to s>0\), then \(n(1-\lambda^2)\to2s\) and \(\lambda^{n-1}\to e^{-s}\), proving the crossover. The optimal count satisfies \(n\varepsilon\to1\), hence the optimized distance tends to \(2/e\).

## Verification

The standalone `verify.py` runs rational-arithmetic matrix-power identities for five rational values of \(\lambda\) and integers \(1\le n\le15\), verifies the physical Pauli probabilities, checks exact optimizer ties, and numerically checks the critical-scale limit. It produces `PASS: 75 rational Bloch-power identities; Pauli CP checks; sharp-time ties; critical-scale limits.` using standard Python only. The infinite ancillary supremum and the asymptotic claims are proved analytically above, not inferred from these checks.

## Relationship to prior work

Brandão, arXiv:2610.13622v1, gives the exceptional qubit channel, its Jordan decomposition and the complete probability expression for arbitrary Bloch preparations and projective measurements (notably its Eqs. 18--34). The present result uses that physical model but introduces a specific isospectral *diagonalizable CPTP comparator*, computes an exact diamond norm over **all** passive ancillas, determines an attaining qubit-only protocol, and optimizes the repetition count with a nonzero weak-noise/long-time limit. Wong--Zeng--Li investigate experimental channel exceptional points and interpolation; vom Ende proves generic diagonalizability of channels in norm. Neither source, in the inspected relevant sections, supplies the matched isospectral discrimination formula. The diamond norm's operational interpretation is standard (Kliesch--Roth).

## Limitations

The comparator is canonical for matching the three Pauli damping eigenvalues on the same coordinate axes; the result does **not** minimize distance over every conceivable isospectral CPTP comparator. It does not optimize a fully adaptive multi-query discrimination task with operations inserted between channel uses, nor claim a convergent Lindblad generator or metrological noise advantage. Ancilla uselessness is proved only for the displayed *uninterleaved-power comparison*. The limiting \(2/e\) pertains to the specified \(\lambda\uparrow1\) and optimized repetition regime. Priority remains conditional on the literature inspected; general rank-one map inequalities and Jordan-binomial expansions are established ingredients.

## References

1. P. A. Brandão, *Operational signatures of exceptional quantum channels*, arXiv:2610.13622v1 (first posted 2026-10-09), https://arxiv.org/html/2610.13622v1 .
2. W. C. Wong, B. Zeng and J. Li, *Non-Markovian exceptional points by interpolating quantum channels*, arXiv:2507.16049 (first posted 2025-07-21); *npj Quantum Information* **12**, 63 (2026), https://www.nature.com/articles/s41534-026-01205-2 .
3. F. vom Ende, *Almost All Quantum Channels Are Diagonalizable*, arXiv:2403.19643 (first posted 2024-03-28), https://arxiv.org/html/2403.19643v1 .
4. M. Kliesch and I. Roth, *Theory of Quantum System Certification*, *PRX Quantum* **2**, 010201 (2021), https://doi.org/10.1103/PRXQuantum.2.010201 .
