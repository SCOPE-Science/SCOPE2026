# The critical one-fifth-power local-coherence window for one-axis-twisted spin squeezing

## Finding

Let \(n\ge3\). Prepare \(|+\rangle^{\otimes n}\), twist by \(U_\tau=\exp(-i\tau J_z^2)\), and independently phase-damp each qubit by visibility \(\eta\). For every fixed \(a,c>0\), set \(\tau_n=a n^{-3/5}\), \(\eta_n=c n^{-1/5}\). The exact asymptotic Wineland squeezing parameter is

\[
\lim_{n\to\infty}\xi_W^2(n,\tau_n,\eta_n)=f_c(a):=\frac1{c^4a^2}+\frac{a^4}{6c^2}.
\]

Convergence is locally uniform on compact positive parameter sets. The function \(f_c\) has a unique global minimizer and minimum

\[
a_c=(3/c^2)^{1/6},\qquad f_c(a_c)=\frac{3^{2/3}}2c^{-10/3}.
\]

Therefore the critically scaled preparation time \(\tau_n=a_c n^{-3/5}\) asymptotically beats the standard quantum limit exactly for

\[
c>c_*:=\left(\frac{3^{2/3}}2\right)^{3/10}.
\]

For \(c<c_*\), no *fixed* \(a>0\) on this specified time scale has an asymptotic Wineland parameter below one. At equality the limiting value is exactly one, without a statement about the finite-size sign. The result does **not** optimize over all possible \(n\)-dependent twisting times.

## Assumptions and scope

Set \(J_\alpha=\frac12\sum_{i=1}^{n}\sigma_\alpha^{(i)}\) for \(\alpha\in\{x,y,z\}\). The initial qubits are identical pure \(+x\)-polarized states. Apply \(U_\tau=\exp(-i\tau J_z^2)\), then \(\mathcal D_\eta^{\otimes n}\), where on a single-qubit matrix \(\mathcal D_\eta\) leaves the diagonal unchanged and multiplies both off-diagonal entries by \(\eta\), with \(0<\eta\le1\). The state after both operations is \(\rho_{n,\tau,\eta}\). For \(0<\tau<\pi/2\) the mean spin is nonzero and points along the \(x\)-axis. Define

\[
\xi_W^2(n,\tau,\eta)=\frac{n\min_{\|\mathbf v\|=1,\,\mathbf v\perp\langle\mathbf J\rangle}\operatorname{Var}_{\rho}(\mathbf v\cdot\mathbf J)}{\|\langle\mathbf J\rangle\|^2}.
\]

For fixed positive \(a,c\), the specified parameters satisfy \(0<\eta_n\le1\) and \(0<\tau_n<\pi/2\) for all sufficiently large \(n\). All logarithms and powers use their usual real meaning.

## Proof

The Ising identity \(J_z^2=nI/4+\frac12\sum_{i<j}\sigma_z^{(i)}\sigma_z^{(j)}\), the initial product-state expectations, and conjugation by the commuting pair interactions give, for distinct qubits \(i,j\), the exact pre-dephasing moments

\[
\langle\sigma_x^{(i)}\rangle=\cos^{n-1}\tau,\quad
\langle\sigma_y^{(i)}\sigma_y^{(j)}\rangle=\frac{1-\cos^{n-2}(2\tau)}2,\quad
\langle\sigma_y^{(i)}\sigma_z^{(j)}\rangle=\sin\tau\cos^{n-2}\tau.
\]

The last expression can change sign if the opposite sign convention is chosen for the twisting Hamiltonian; only its square enters the eigenvalues below. All one-site \(y,z\) means vanish, all distinct-site \(zz\) correlations vanish, and every one-site Pauli-component variance along \(y,z\) equals one. The dual dephasing map sends \(\sigma_x,\sigma_y\) to \(\eta\sigma_x,\eta\sigma_y\), and fixes \(\sigma_z\). Thus

\[
\langle J_x\rangle=\frac{n\eta}2\cos^{n-1}\tau,
\qquad \operatorname{Cov}(J_y,J_z)=\frac n4 Q,
\]

where

\[
Q=\begin{pmatrix}
1+\frac{(n-1)\eta^2}2(1-\cos^{n-2}(2\tau)) & (n-1)\eta\sin\tau\cos^{n-2}\tau\\
(n-1)\eta\sin\tau\cos^{n-2}\tau &1
\end{pmatrix}.
\]

Write \(A=Q_{11}\), \(B=Q_{12}\), and \(\lambda_-\le\lambda_+\) for its eigenvalues. Since the state has mean spin along \(x\), direct optimization of the quadratic transverse variance gives the exact finite-size identity

\[
\xi_W^2=\frac{\lambda_-}{\eta^2\cos^{2n-2}\tau},\qquad
\lambda_+=\frac{A+1+\sqrt{(A-1)^2+4B^2}}2,\qquad \lambda_- = \frac{\det Q}{\lambda_+}.
\]

In particular,

\[
\det Q=1+\eta^2 H_n(\tau),\qquad
H_n(\tau)=\frac{n-1}{2}(1-\cos^{n-2}(2\tau))-(n-1)^2\sin^2\tau\cos^{2n-4}\tau.
\]

The cancellation in \(H_n\) is essential. Binomially expanding \(\cos^k u\) at \(u=0\), with the remainder bounded uniformly whenever \(n\tau^2=o(1)\), yields

\[
H_n(\tau)=-(n-1)\tau^2+
\frac{(n-1)(6n-11)}3\tau^4+
\frac{(n-1)(15n^3-270n^2+945n-934)}{90}\tau^6+O(n^5\tau^8).
\]

For completeness, the uniform remainder follows by writing \(\cos^k u=\sum_{j\ge0}\binom kj(\cos u-1)^j\), retaining all terms through \(u^6\), and bounding the tail by the exponential series in \(k|\cos u-1|\). The coefficients are polynomials in \(k\) of degree at most the respective Taylor order. On compact positive \(a,c\) sets, the same remainder bound is uniform for \(\tau=a n^{-3/5}\).

Substitute \(\tau=a n^{-3/5}\), \(\eta=c n^{-1/5}\). Then

\[
\eta^2 H_n(\tau)\longrightarrow \frac{c^2a^6}{6},\quad
A\sim c^2a^2n^{2/5},\quad
\lambda_+\sim c^2a^2n^{2/5},\quad
\cos^{2n-2}\tau\longrightarrow1.
\]

Indeed \(B=O(n^{1/5})\), whence \(B^2/A^2=O(n^{-2/5})\), so the asserted large eigenvalue estimate follows from the explicit eigenvalue formula. Therefore

\[
\xi_W^2=\frac{1+\eta^2H_n(\tau)}{\eta^2\lambda_+\cos^{2n-2}\tau}
\longrightarrow\frac{1+c^2a^6/6}{c^4a^2}
=\frac{1}{c^4a^2}+\frac{a^4}{6c^2}.
\]

Finally \(f_c(a)\to\infty\) at both endpoints of \((0,\infty)\), while its derivative has precisely one positive zero determined by \(a^6=3/c^2\). Substitution gives the claimed minimum and the sharp threshold relative to one. Strict inequalities of the limit imply the corresponding inequalities for sufficiently large finite \(n\), separately for each fixed \(a,c\).

## Verification

The standalone exact-moment and asymptotic checker `verify.py` evaluates the covariance formula at high precision for large integers, independently extracts its decisive sixth-order polynomial coefficient in symbolic arithmetic, and tests convergence on both sides of the threshold. The separate `check_small_n.py` constructs the full density matrix for three, four, and five qubits, applies dephasing entrywise, and compares the measured covariance to the formula. Execute `python verify.py` with `mpmath` and `sympy` installed, and `python check_small_n.py` with `numpy` installed. These are finite checks, not replacements for the analytic bounds.

## Relationship to prior work

One-axis twisting and spin squeezing originate in Kitagawa and Ueda (1993). Zhong et al. (arXiv:1309.4842, originally posted September 2013) calculate spin squeezing and Fisher information in OAT, and discuss **collisional collective** dephasing. Ji, Liu and Jin (arXiv:1312.3743v1, December 2013) derive exact moments and asymptotic scaling for the many-body Lindbladian generated by a **single collective \(J_z\)**. That Lindbladian multiplies Dicke-basis coherences according to their *magnetization difference squared* and is not the tensor product of independent per-qubit phase-damping channels here. The present one-fifth-power visibility critical window and mean-spin-normalized limiting function are not direct special cases of those collective-noise models. This distinction and the possibility of an equivalent calculation in broader independent-noise metrology literature remain the relevant priority questions.

## Limitations

The result is about \(\xi_W^2\), not the unnormalized Kitagawa–Ueda variance criterion or quantum Fisher information. It treats a fixed family of critically scaled preparation times and constant positive coefficients; the threshold is not claimed globally optimal over all time sequences, and the finite-size behavior at exact equality is unresolved. The independent phase damping is applied after ideal twisting, not a model with noncommuting relaxation or noise during control. No experimental implementation or independent literature-priority certification is claimed.

## References

- M. Kitagawa and M. Ueda, “Squeezed spin states,” *Physical Review A* **47** (1993), 5138–5143, DOI: 10.1103/PhysRevA.47.5138.
- W. Zhong, J. Liu, J. Ma and X. Wang, “Quantum Fisher information and spin squeezing in one-axis twisting model,” arXiv:1309.4842v1 (first submitted 2013-09-19), https://arxiv.org/abs/1309.4842.
- C. G. Ji, Y. C. Liu and G. R. Jin, “Spin Squeezing of One-Axis Twisting Model in The Presence of Phase Dephasing,” arXiv:1312.3743v1 (first submitted 2013-12-13), https://arxiv.org/abs/1312.3743.
- Y.-H. Ma, Q.-Z. Ding and T. Yu, “Persistent spin squeezing of a dissipative one-axis twisting model embedded in a general thermal environment,” *Physical Review A* **101** (2020), 022327, DOI: 10.1103/PhysRevA.101.022327 (numerical non-Markovian setting; cited for distinction).
