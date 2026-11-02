# Entanglement-breaking crossover and resonant optima for rotated qubit dephasing

## Finding
For real \(\theta\), \(0<\lambda<1\), and the unital qubit channel
\[
\Phi_{\lambda,\theta}(\rho)=U_\theta\left[\frac{1+\lambda^2}{2}\rho+\frac{1-\lambda^2}{2}\sigma_z\rho\sigma_z\right]U_\theta^\dagger,
\qquad U_\theta=e^{-i\theta\sigma_y/2},
\]
let \(b(\lambda,\theta)\) be the least positive integer \(n\) for which \(\Phi_{\lambda,\theta}^{\,n}\) is entanglement breaking, and set it to \(+\infty\) if none exists. Write \(U_j\) for the standard Chebyshev polynomial of the second kind, with \(U_0=1\), and put \(x=(\lambda+\lambda^{-1})\cos\theta/2\). Then the **exact all-iteration criterion** is
\[
\Phi_{\lambda,\theta}^{\,n}\text{ is entanglement breaking}
\iff
\lambda^n\sqrt{4+(\lambda^{-1}-\lambda)^2U_{n-1}(x)^2}+\lambda^{2n}\le1.
\tag{1}
\]
Moreover \(b(\lambda,\theta)<\infty\) exactly when \(\sin\theta\ne0\). This includes defective and diagonalizable channels on equal footing.

There is a **sharp weak-noise/weak-rotation crossover**. Fix \(c>0\), set \(\lambda=1-\delta\), \(\theta=c\delta\) and let \(\delta\downarrow0\). Then
\[
\delta\,b(1-\delta,c\delta)\longrightarrow\tau(c),
\tag{2}
\]
where \(\tau(c)\) is the unique positive root of
\[
2e^{-t}\sqrt{1+S_c(t)^2}+e^{-2t}=1,
\quad
S_c(t)=\begin{cases}
\displaystyle\frac{\sinh(t\sqrt{1-c^2})}{\sqrt{1-c^2}},&0<c<1,\\
t,&c=1,\\
\displaystyle\frac{\sin(t\sqrt{c^2-1})}{\sqrt{c^2-1}},&c>1.
\end{cases}
\tag{3}
\]
The global minimum across the fixed positive drive/dephasing ratios \(c\) is
\[
\min_{c>0}\tau(c)=L:=\log(1+\sqrt2),
\tag{4}
\]
and it is attained **exactly** at the discrete resonances
\[
c_k=\sqrt{1+(k\pi/L)^2},\qquad k=1,2,\ldots.
\tag{5}
\]
At the exceptional-point scaling \(c=1\), \(\tau(1)=1.2489718449\ldots>L\). The rotationally frozen endpoint \(c=0\) has no finite entanglement-breaking time. These are asymptotic statements for fixed \(c\), not uniform assertions when \(c\) changes with \(\delta\).

## Assumptions and scope
The single-qubit Hilbert space is \(\mathbb C^2\); \(\sigma_y\) and \(\sigma_z\) are the standard Pauli matrices. A channel is entanglement breaking when its local action destroys entanglement with an arbitrary finite-dimensional reference. A positive integer \(n\) counts **uninterrupted repetitions** of the same map; no intermediate filters, adaptive operations, resets or choices of new rotation at each step are allowed. In (2)–(5) the scaling \(\theta=c\delta\) is imposed for each \(\delta\), \(c\) stays fixed before the limit, and \(\lambda=1-\delta\in(0,1)\). The point \(c=1\) is the small-noise limit of the positive exceptional-point curve \(\cos\theta=2\lambda/(1+\lambda^2)\) in the motivating quantum-channel family.

The full exact formula (1) holds for all \(\theta\in\mathbb R\). It uses the real polynomial \(U_{n-1}\) also when \(|x|>1\); there is no division by \(\sqrt{1-x^2}\) at the exceptional point.

## Proof
**1. Real Bloch reduction.** Writing \(\rho=(I+\mathbf r\cdot\boldsymbol\sigma)/2\), the channel maps \(\mathbf r\) through a real matrix with invariant \(y\) direction of multiplier \(\lambda^2\), and with \((x,z)\) block
\[
M=\begin{pmatrix}\lambda^2\cos\theta&\sin\theta\\-\lambda^2\sin\theta&\cos\theta\end{pmatrix}.
\]
Thus its \(n\)-fold Bloch matrix has singular values equal to the singular values of \(M^n\), together with \(\lambda^{2n}\). For unital qubit channels, the standard two-qubit Choi/PPT criterion says that entanglement breaking is equivalent to the Bloch matrix having nuclear (Schatten-one) norm at most \(1\); see Lami–Giovannetti, Section II.1, equation (7), and Ruskai's qubit-channel treatment.

**2. Closed nuclear norm.** One has \(\det M=\lambda^2\), \(\operatorname{tr}M=2\lambda x\). Set \(H=\lambda^{-1}M-xI\); then \(\operatorname{tr}H=0\) and \(H^2=(x^2-1)I\). By the Cayley–Hamilton/Chebyshev identity,
\[
M^n=\lambda^n[T_n(x)I+U_{n-1}(x)H],
\]
where \(T_n\) is the Chebyshev polynomial of the first kind. The Frobenius inner product of \(I\) and \(H\) is zero, and \(\|H\|_F^2=\lambda^2+\lambda^{-2}-2x^2\). Also \(\det(M^n)=\lambda^{2n}>0\). For any real \(2\times2\) matrix \(A\), \(\|A\|_*^2=\|A\|_F^2+2|\det A|\). Consequently,
\[
\begin{aligned}
\lambda^{-2n}\|M^n\|_*^2
&=2T_n(x)^2+[\lambda^2+\lambda^{-2}-2x^2]U_{n-1}(x)^2+2\\
&=4+(\lambda-\lambda^{-1})^2U_{n-1}(x)^2,
\end{aligned}
\]
where the final step uses \(T_n(x)^2+(1-x^2)U_{n-1}(x)^2=1\). This proves (1) for every \(x\in\mathbb R\), including \(x=\pm1\).

**3. Finiteness and the nonrotating boundary.** If \(\sin\theta=0\), then \(M\) has singular values \(1,\lambda^2\) at every power up to signs, and the full norm is \(1+2\lambda^{2n}>1\) for each finite \(n\). If \(\sin\theta\ne0\), write \(M=R_\theta\operatorname{diag}(\lambda^2,1)\), where \(R_\theta\) is a planar rotation. Equality \(\|Mv\|_2=\|v\|_2\) requires \(v\) to lie on the \(z\) axis, while its rotation acquires a nonzero \(x\) component. Hence \(\|M^2\|_{\mathrm{op}}<1\); by compactness the maximum is strictly less than one. It follows that \(M^n\to0\), and since \(\lambda^{2n}\to0\), the nuclear norm ultimately falls below one. Once a channel becomes entanglement breaking, later compositions remain entanglement breaking.

**4. Critical-window limit and uniqueness.** With \(\lambda=1-\delta\), \(\theta=c\delta\), direct Taylor expansion gives
\[
M=I+\delta B_c+O(\delta^2),\qquad
B_c=\begin{pmatrix}-2&c\\-c&0\end{pmatrix},
\qquad \lambda^2=1-2\delta+O(\delta^2).
\]
Therefore, whenever \(\delta n\to t\ge0\), the power matrices tend to \(e^{tB_c}\) and the scalar \(y\) multiplier tends to \(e^{-2t}\). Write \(B_c=-I+K_c\), with \(K_c^2=(1-c^2)I\) and \(\operatorname{tr}K_c=0\). It follows that
\[
e^{tB_c}=e^{-t}[C_c(t)I+S_c(t)K_c],
\]
where \(C_c(t)=\cosh(t\sqrt{1-c^2})\) for \(c<1\), equals \(1\) for \(c=1\), and is \(\cos(t\sqrt{c^2-1})\) for \(c>1\). As \(\det(e^{tB_c})=e^{-2t}\) and \(\|K_c\|_F^2=2(1+c^2)\), the same Frobenius/determinant calculation yields
\[
\|e^{tB_c}\|_*=2e^{-t}\sqrt{1+S_c(t)^2}.
\]
Denote by \(F_c(t)\) the left side of (3). Then \(F_c(0)=3\), and \(F_c(t)\to0\) for every \(c>0\): the eigenvalues of \(B_c\) have negative real parts, being \(-1\pm\sqrt{1-c^2}\) in the overdamped regime and \(-1\pm i\sqrt{c^2-1}\) in the oscillatory regime.

For \(c>0\), every matrix \(e^{sB_c}\) with \(s>0\) is a strict Euclidean contraction. Indeed, if \(v(s)=e^{sB_c}v(0)\), then \(d\|v\|_2^2/ds=-4v_x(s)^2\). Equality of the initial and final norms would require \(v_x\equiv0\), forcing \(cv_z\equiv0\), hence \(v\equiv0\). Compactness of the unit sphere makes the operator norm strictly less than one. Consequently \(\|e^{(s+t)B_c}\|_*\le\|e^{sB_c}\|_{\rm op}\|e^{tB_c}\|_*<\|e^{tB_c}\|_*\), and \(F_c\) is continuous and strictly decreasing. The root \(\tau(c)\) exists and is unique.

The convergences of \(M^{\lfloor t/\delta\rfloor}\) and \(\lambda^{2\lfloor t/\delta\rfloor}\) are uniform for \(t\) in every compact interval. For any \(0<\eta<\tau(c)\), the nuclear norm exceeds one at \(t=\tau(c)-\eta\) and is below one at \(t=\tau(c)+\eta\) once \(\delta\) is sufficiently small. Because the channel's entanglement-breaking property persists under later composition, these inequalities trap \(\delta b(1-\delta,c\delta)\) between the two times up to \(O(\delta)\). This proves (2).

**5. Sharp resonance classification.** For every \(c>0\) and \(t\ge0\), \(\sqrt{1+S_c(t)^2}\ge1\), hence
\[
F_c(t)\ge 2e^{-t}+e^{-2t}.
\]
The right side reaches one at the unique positive value \(L=\log(1+\sqrt2)\). Since \(F_c\) decreases strictly, \(\tau(c)\ge L\). Equality requires and is implied by \(S_c(L)=0\). For \(0<c<1\), \(S_c(L)>0\); for \(c=1\), \(S_1(L)=L>0\); and for \(c>1\), \(S_c(L)=0\) exactly if \(L\sqrt{c^2-1}=k\pi\) for a positive integer \(k\). These are exactly (5). At \(c=1\), solving \(2e^{-t}\sqrt{1+t^2}+e^{-2t}=1\) gives the stated root. This proves the full claimed theorem.

## Verification
The standalone program `verify_rotated_dephasing.py` independently constructs Kraus-output matrices and the two-qubit Choi matrix. It compares its partial-transpose eigenvalues with (1), and checks the closed trace-norm formula against direct matrix powers for pseudorandom parameters. It further tests the claimed scaling against finite repeated applications and verifies nilpotence of the exceptional-point traceless block. The program uses NumPy and SciPy as listed in `requirements.txt`. Execute from the folder containing both files with `python verify_rotated_dephasing.py`. The included program passed 619 assertions in the recorded run. Its finite computations support, but do not substitute for, the algebraic and asymptotic proofs above.

## Relationship to prior work
Brandão, arXiv:2610.13622v1, gives the exact rotated-dephasing channel, its defective spectral curve, and operational measurement signatures of Jordan modes. It does not derive an all-iteration entanglement-breaking index or the weak-noise drive-ratio crossover. Lami and Giovannetti (2015) define entanglement-breaking indices and give the general unital-qubit nuclear-norm criterion, which is used here rather than claimed new. Cuevas et al. (2017) study a related rotated phase-damping apparatus and demonstrate a two-step entanglement-breaking/amendment experiment; that study does not provide the full \(n\)-step Chebyshev identity, the asymptotic \(c\)-dependent boundary, or the discrete resonant optimizer set.

A broader previously derived optimization across **all** repeated qubit unitaries and a distinct diamond-norm analysis of the exact exceptional channel are related but do not imply the claimed fixed-axis, fixed-per-run rotation index or its resonant weak-noise crossover. Specifically, the unrestricted unitary optimization permits drive configurations beyond the one-axis family in this theorem. The new statement is the exact channel-specific index and restricted critical-limit optimum, not the definition of entanglement breaking, the known unital criterion, or existence of nonnormal eigenvalue degeneracies.

## Limitations
The results describe ideal single-qubit channels with independent repetitions, no channel parameter drift within a given run, and no interspersed recovery/feedback operations. The scaling requires a fixed ratio \(c>0\) as \(\delta\downarrow0\). The resonance optimality is **only within this fixed-ratio one-axis weak-noise family**, not among all unital channels or arbitrary unitaries, and it is an asymptotic optimization of the scaled first entanglement-breaking iteration, not an exact finite-\(\delta\) optimizer. Neither experimental error bars nor an implementation proposal are provided. The priority assessment remains best-knowledge and is not an independent literature-wide certification.

## References
1. P. A. Brandão, *Operational signatures of exceptional quantum channels*, arXiv:2610.13622v1 (first public 2026-10-09), https://arxiv.org/abs/2610.13622.
2. L. Lami and V. Giovannetti, *Entanglement–Breaking Indices*, J. Math. Phys. 56, 092201 (2015), arXiv:1411.2517, https://arxiv.org/abs/1411.2517.
3. Á. Cuevas et al., *Amending entanglement-breaking channels via intermediate unitary operations*, Phys. Rev. A 96, 022322 (2017), arXiv:1707.00161, https://arxiv.org/abs/1707.00161.
4. M. B. Ruskai, *Qubit entanglement breaking channels*, Rev. Math. Phys. 15, 643–662 (2003), arXiv:quant-ph/0302032, https://arxiv.org/abs/quant-ph/0302032.
5. E. Kopel, *Measuring the entanglement-breaking index of a qubit collision channel on a quantum processor*, arXiv:2609.09350 (2026), https://arxiv.org/abs/2609.09350; related finite-index operational context in a different channel family.
