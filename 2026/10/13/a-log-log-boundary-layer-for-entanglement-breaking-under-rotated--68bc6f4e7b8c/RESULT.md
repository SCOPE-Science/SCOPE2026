# A log-log boundary layer for entanglement breaking under rotated qubit dephasing

## Finding
Fix a dephasing visibility \(0<\lambda<1\). Let \(\mathcal D_\lambda\) be the qubit channel that multiplies the \(x\)- and \(y\)-components of the Bloch vector by \(\lambda\), and preserves its \(z\)-component. Let \(\mathcal U_\theta\) rotate a Bloch vector about the \(y\)-axis through angle \(\theta\). Consider repeated, **unfiltered** applications of \(\Phi_{\lambda,\theta}=\mathcal D_\lambda\circ\mathcal U_\theta\), and write \(n_{\mathrm{EB}}(\lambda,\theta)\) for the least positive integer at which the iterate is entanglement breaking (\(+\infty\) if no such integer exists).

**Exact criterion.** Put \(t=(1+\lambda)\cos\theta\) and define two real recurrence sequences by
\[
 r_0=2,\quad r_1=t,\quad r_{n+1}=tr_n-\lambda r_{n-1},\qquad
 v_0=0,\quad v_1=1,\quad v_{n+1}=tv_n-\lambda v_{n-1}.
\]
For every integer \(n\ge1\),
\[
\boxed{\Phi_{\lambda,\theta}^{\,n}\text{ is entanglement breaking}\quad\Longleftrightarrow\quad
 \lambda^n+\sqrt{r_n^2+(1+\lambda)^2\sin^2\theta\,v_n^2}\le1.}
\]
When \(0<\theta<\pi\), this criterion is satisfied for some finite \(n\), whereas \(n_{\mathrm{EB}}(\lambda,0)=n_{\mathrm{EB}}(\lambda,\pi)=+\infty\).

**Sharp small-angle scaling.** Set \(\kappa=-\log\lambda\), \(a_\lambda=(1+\lambda)/[2(1-\lambda)]\) and \(L=\log(1/\theta)\). As \(\theta\downarrow0\),
\[
\boxed{n_{\mathrm{EB}}(\lambda,\theta)=
 \frac{2L-\log L+\log(\kappa/a_\lambda)}{\kappa}+O_\lambda(1).}
\]
More precisely, let \(n=n(\theta)\) be any sequence of positive integers for which \(x_\theta=\kappa n-2L+\log L\to x\in\mathbb R\). Writing \(M_{\lambda,\theta}\) for the Bloch matrix below, the *signed entanglement-breaking defect* has the universal transition profile
\[
\boxed{\lim_{\theta\downarrow0}\frac{\|M_{\lambda,\theta}^{\,n}\|_1-1}{\theta^2L}
=2e^{-x}-\frac{2a_\lambda}{\kappa}.}
\]
The profile changes sign exactly at \(x=\log(\kappa/a_\lambda)\). Consequently a nonzero rotation makes the direct breaking index finite, but its divergence approaching the perfectly aligned axis has a negative \(\log\log(1/\theta)\) correction to the leading logarithm.

## Assumptions and scope
The elementary channel is a composition of a **unitary** qubit \(y\)-rotation and a **unital** qubit phase-damping channel. In the \((x,y,z)\) Bloch basis its real matrix is exactly
\[
M_{\lambda,\theta}=
\begin{pmatrix}
\lambda\cos\theta&0&\lambda\sin\theta\\
0&\lambda&0\\
-\sin\theta&0&\cos\theta
\end{pmatrix}.
\]
The Schatten \(1\)-norm \(\|M\|_1\) means the sum of singular values of a real matrix, *not* an entrywise matrix norm. All statements concern one qubit and arbitrary ancilla dimension, and do not permit filtering operations between channel iterations. The limits hold at each fixed \(\lambda\in(0,1)\), not uniformly at the visibility endpoints. The recurrence criterion applies throughout \(0\le\theta\le\pi\).

## Proof
**1. Exact recurrence from the qubit separability criterion.** For every unital qubit channel with real Bloch matrix \(M\), its Choi state is separable, equivalently the channel is entanglement breaking, precisely when \(\|M\|_1\le1\) [1, Eq. (7)]. Permuting the Bloch coordinates reveals the block decomposition \(M\simeq A\oplus(\lambda)\), where
\[
A=\begin{pmatrix}\lambda\cos\theta&\lambda\sin\theta\\-\sin\theta&\cos\theta\end{pmatrix},
\qquad\det A=\lambda,\quad \operatorname{tr}A=t.
\]
The Cayley--Hamilton identity is \(A^2=tA-\lambda I\). Induction gives \(A^n=v_nA-\lambda v_{n-1}I\), \(\operatorname{tr}A^n=r_n\), and \((A^n)_{12}-(A^n)_{21}=(1+\lambda)\sin\theta\,v_n\). If \(B\) is any real two-by-two matrix with \(\det B>0\), its singular values satisfy
\[
\|B\|_1^2=\|B\|_{\mathrm F}^2+2\det B
=(\operatorname{tr}B)^2+(B_{12}-B_{21})^2.
\]
Apply this with \(B=A^n\), add the third singular value \(\lambda^n\), and invoke the qubit criterion. This proves the stated exact inequality for every integer \(n\ge1\).

**2. Angle endpoints and eventual breaking.** At either \(\theta=0\) or \(\theta=\pi\), the singular values of \(M^n\) are \(1,\lambda^n,\lambda^n\), so their sum exceeds \(1\) at every finite \(n\). At any \(0<\theta<\pi\), both eigenvalues of \(A\) lie strictly inside the unit circle. Indeed the quadratic \(z^2-tz+\lambda\) satisfies the degree-two Schur stability inequalities \(1-\lambda>0\), \(1-t+\lambda=(1+\lambda)(1-\cos\theta)>0\), and \(1+t+\lambda=(1+\lambda)(1+\cos\theta)>0\). Thus \(A^n\to0\), and also \(\lambda^n\to0\); eventually the exact nuclear norm is less than \(1\). Since \(\|M\|_{\mathrm{op}}=1\), the nuclear norms \(\|M^n\|_1\) are nonincreasing, so once the threshold is reached it remains reached.

**3. Uniform boundary-layer estimate.** In a fixed sufficiently small angular interval, the two real eigenvalues \(\mu_+(\theta)\) and \(\mu_-(\theta)\) of \(A\) are analytic even functions and satisfy
\[
\mu_+(\theta)=1-a_\lambda\theta^2+O_\lambda(\theta^4),\qquad
\mu_-(\theta)=\lambda(1+a_\lambda\theta^2+O_\lambda(\theta^4)).
\]
The identities \(r_n=\mu_+^n+\mu_-^n\) and \(v_n=(\mu_+^n-\mu_-^n)/(\mu_+-\mu_-)\) give, uniformly for integers \(n=O_\lambda(L)\),
\[
r_n=1+\lambda^n-a_\lambda n\theta^2(1-\lambda^n)+O_\lambda(n^2\theta^4),\qquad
v_n=\frac{1-\lambda^n}{1-\lambda}+O_\lambda(n\theta^2).
\]
In the narrower transition range \(\kappa n=2L-\log L+O(1)\), where \(\lambda^n=\Theta_\lambda(\theta^2L)\), taking the square root in the exact criterion gives
\[
\|M^n\|_1-1=2\lambda^n-a_\lambda n\theta^2
+O_\lambda(\theta^2+n^2\theta^4).
\]
Here the remainder is \(o(\theta^2L)\), because \(n\asymp_\lambda L\) and \(\theta^2L\to0\). Moreover, \(\lambda^n=\theta^2Le^{-x_\theta}\) and \(n/L\to2/\kappa\), yielding the displayed crossover profile. Bracket the unique sign transition with fixed large positive and negative shifts of \(x\), use the nonincreasing nuclear norm, and obtain the breaking-index estimate with \(O_\lambda(1)\) integer-rounding uncertainty. This establishes every claim.

As a transparent finite-angle boundary check, when \(\theta=\pi/2\) one has \(A^2=-\lambda I\), so \(\|M^{2m}\|_1=2\lambda^m+\lambda^{2m}\) and \(\|M^{2m+1}\|_1=(1+\lambda)\lambda^m+\lambda^{2m+1}\) for every nonnegative integer \(m\).

## Verification
The accompanying standalone `verify.py` independently constructs the channel Bloch matrices, computes singular values of their powers, and computes the minimal eigenvalue of the partially transposed two-qubit Choi state. It compares these to the recurrence criterion for 128 finite parameter cases. It additionally checks 69 right-angle identities and 12 high-precision small-angle scaling cases. The replay prints `VERIFY_OK recurrence_PPT_cases=128 exact_right_angle=69 small_angle_scaling=12`. These calculations corroborate rather than certify the universal inequalities or the asymptotic theorem; all quantifiers are established in the analytic proof above. Run with `python verify.py`; dependencies are `numpy` and `mpmath`.

## Relationship to prior work
Lami and Giovannetti [1] introduced direct entanglement-breaking indices and established the unital-qubit nuclear-norm criterion used here. Their treated examples and general theory do not state the small-misalignment log-log transition. Cuevas and collaborators [2] investigate repeated rotated phase-damping maps, primarily experimentally at two channel uses with an optional intermediate unitary filter, rather than the arbitrary-number unfiltered iterates and \(\theta\downarrow0\) scaling addressed here. Hanson, Rouzé and França [3] prove broader eventual-entanglement-breaking properties for quantum Markov dynamics, without an equivalent explicit recurrence or this boundary-layer law in the relevant results inspected. The structural contribution here is the complete direct-iteration criterion for this fixed channel family and, especially, its logarithmic/log-log boundary layer; it is not a new general qubit entanglement-breaking criterion.

## Limitations
The index is a direct, unfiltered index and cannot be substituted for the unitary-filtered index. The asymptotic term \(O_\lambda(1)\) is intentionally not a complete integer rounding formula, and the small-angle statement is not uniform in \(\lambda\) as \(\lambda\to0\) or \(1\). The analysis does not cover nonunital amplitude damping, correlated environments, higher-dimensional systems, or arbitrary changing rotations. An equivalent specialized formula could exist in less accessible studies of phase-damping channel iteration or singular-value recurrences; literature screening cannot establish uniqueness of the result.

## References
[1] L. Lami and V. Giovannetti, *Entanglement-Breaking Indices*, arXiv:1411.2517 (first publicly submitted 2014-11-10), *Journal of Mathematical Physics* 56, 092201 (2015), doi:10.1063/1.4931482.

[2] Á. Cuevas and collaborators, *Amending entanglement-breaking channels via intermediate unitary operations*, arXiv:1707.00161 (2017), *Physical Review A* 96, 022322, doi:10.1103/PhysRevA.96.022322.

[3] E. P. Hanson, C. Rouzé and D. S. França, *Eventually Entanglement Breaking Markovian Dynamics: Structure and Characteristic Times*, *Annales Henri Poincaré* (2020), doi:10.1007/s00023-020-00906-4.
