# Exact continuous minimax value for the three-copy robust qubit benchmark
## Finding
Consider the binary qubit model
\[
|\psi_0\rangle=|0\rangle,\qquad
|\psi_1\rangle=\cos(\pi/4)|0\rangle+\sin(\pi/4)|1\rangle,
\]
with equal label priors, three copies, and a common unknown rotation
\[
U(\theta)=\exp(-i\theta\sigma_y/2),\qquad -\pi/3\le \theta\le \pi/3.
\]
For a fixed collective measurement, let \(P_{\rm succ}(\theta)\) be its success probability. Then
\[
\sup_M\inf_{|\theta|\le \pi/3}P_{\rm succ}(M,\theta)
=
\frac12+\frac{\sqrt{2114}}{208}
=0.721049306395627\ldots.
\]
A least-favorable nuisance prior is
\[
w_*=\frac5{13}\delta_{-\pi/3}+\frac3{13}\delta_0+\frac5{13}\delta_{\pi/3}.
\]
Moreover an explicit optimal measurement has the continuous success profile
\[
P_*(\theta)=
\frac12+\frac{\sqrt{2114}}{208}
+
\frac{\sqrt{2114}}{219856}
(1-\cos\theta)(2\cos\theta-1)(246\cos\theta+713).
\]
Hence its only worst cases on the nuisance interval are \(\theta=0\) and \(\theta=\pm\pi/3\).

## Assumptions and scope
The parameter values are exactly those of the binary numerical benchmark in Fujiki and Tanaka: \(\alpha=\pi/4\), \(\theta_{\max}=\pi/3\), three copies, and equal label priors. The optimization is over arbitrary two-outcome POVMs on the three-copy Hilbert space, so entangled collective measurements are allowed. The nuisance parameter is continuous over the full closed interval, not restricted to a grid.

Write
\[
|\phi(t)\rangle=\cos(t/2)|0\rangle+\sin(t/2)|1\rangle.
\]
Then the two possible three-copy pure states at nuisance value \(t\) are \(|\phi(t)\rangle^{\otimes3}\) and \(|\phi(t+\pi/2)\rangle^{\otimes3}\). Both lie in the four-dimensional symmetric subspace. No claim is made here for other copy numbers, other state angles, unequal label priors, larger nuisance intervals, or the source paper's qutrit example.

## Proof
Use the normalized Dicke basis \((|D_0\rangle,|D_1\rangle,|D_2\rangle,|D_3\rangle)\) of the symmetric subspace. For \(c=\cos(t/2)\) and \(s=\sin(t/2)\), define
\[
v(t)=\begin{pmatrix}c^3\\ \sqrt3c^2s\\ \sqrt3cs^2\\ s^3\end{pmatrix},
\qquad
\Delta(t)=v(t)v(t)^T-v(t+\pi/2)v(t+\pi/2)^T.
\]
Any binary POVM may be written as \(M_0=(I+B)/2\), \(M_1=(I-B)/2\), where \(B\) is Hermitian and \(\|B\|\le1\). On the symmetric subspace,
\[
P_B(t)=\frac12+\frac14\operatorname{Tr}(\Delta(t)B).
\]
The action of \(B\) outside the symmetric subspace is irrelevant and may be set to zero.

For the upper bound, average over
\[
w_*=\frac5{13}\delta_{-\pi/3}+\frac3{13}\delta_0+\frac5{13}\delta_{\pi/3}.
\]
The averaged Helstrom difference is
\[
\overline\Delta
=
\frac1{416}
\begin{pmatrix}
89&-47\sqrt3&23\sqrt3&-17\\
-47\sqrt3&69&-51&-7\sqrt3\\
23\sqrt3&-51&-21&-47\sqrt3\\
-17&-7\sqrt3&-47\sqrt3&-137
\end{pmatrix}.
\]
Its eigenvalues are
\[
-\frac{\sqrt{2114}}{104},\quad 0,\quad0,\quad\frac{\sqrt{2114}}{104},
\]
so
\[
\|\overline\Delta\|_1=\frac{\sqrt{2114}}{52}.
\]
For every measurement,
\[
\inf_{|t|\le\pi/3}P_B(t)
\le
\int P_B(t)\,dw_*(t)
\le
\frac12+\frac14\|\overline\Delta\|_1
=
\frac12+\frac{\sqrt{2114}}{208}.
\]
This gives the minimax upper bound.

It remains to attain it over the entire continuum. Put
\[
\lambda=\frac{\sqrt{2114}}{104},\qquad B_0=\frac{\overline\Delta}{\lambda}.
\]
Then \(B_0\) has eigenvalues \(-1,0,0,1\). An orthonormal basis for its kernel is
\[
u_1=\frac1{2\sqrt{37}}
\begin{pmatrix}-5\sqrt3\\-8\\3\\0\end{pmatrix},
\qquad
u_2=\frac1{2\sqrt{117327}}
\begin{pmatrix}60\\-153\sqrt3\\-308\sqrt3\\333\end{pmatrix}.
\]
On this kernel define
\[
K=\frac1{1443}
\begin{pmatrix}
-2\sqrt{2114}&82\sqrt2\\
82\sqrt2&2\sqrt{2114}
\end{pmatrix}.
\]
Since the eigenvalues of \(K\) are \(\pm4/39\), the operator
\[
B_*=B_0+[u_1\ u_2]K[u_1\ u_2]^T
\]
has eigenvalues \(-1,-4/39,4/39,1\) on the symmetric subspace. Thus \(\|B_*\|=1\), so it defines a valid two-outcome POVM.

Direct trigonometric simplification gives
\[
P_{B_*}(t)-\left(\frac12+\frac{\sqrt{2114}}{208}\right)
=
\frac{\sqrt{2114}}{219856}
(1-\cos t)(2\cos t-1)(246\cos t+713).
\]
For \(|t|\le\pi/3\), one has \(1/2\le\cos t\le1\). Every factor on the right is therefore nonnegative, and the last factor is strictly positive. Equality occurs exactly when \(t=0\) or \(t=\pm\pi/3\). The lower bound matches the upper bound, proving the formula.

## Verification
The algebra above can be replayed with `artifacts/verify.py`. The checker independently constructs the symmetric-subspace states, the three-point averaged Helstrom matrix, the kernel correction, and the resulting measurement. It verifies numerically at high precision that the averaged matrix has the stated spectrum, that the measurement is a contraction with the stated spectrum, that the three active nuisance points equal the claimed value, and that the closed-form profile agrees with direct matrix evaluation on a dense deterministic grid.

The finite replay corroborates the displayed exact identities; the proof of the continuum bound is the analytic factorization above, not the grid check.

## Relationship to prior work
Fujiki and Tanaka formulate the common-unitary nuisance problem, prove the finite-grid minimax/least-favorable-prior duality, and use a \(41\)-point optimization grid plus a \(401\)-point evaluation grid for this binary three-copy benchmark. Their Table 1 reports the global collective worst-case success probability as \(0.72\), and their discussion explicitly notes that the finite-grid SDP solves the discretized problem rather than the continuous problem directly. The result here identifies the exact continuous optimum, gives an exact least-favorable prior, and supplies a closed-form optimal success profile.

D'Ariano, Sacchi, and Kahn develop minimax quantum-state discrimination when the state-label prior itself is unknown. Their binary minimax is over the two label-conditioned detection probabilities, whereas the present problem keeps the label prior fixed and takes the minimax over a common external unitary nuisance parameter acting on both states. Their theorems therefore do not imply the exact nuisance-interval value above.

DiMario and Becerra study robustness of binary coherent-state receivers to experimental imperfections. That setting concerns optical coherent states and receiver imperfections rather than this three-copy finite-dimensional common-rotation nuisance family, and it does not provide the displayed value or least-favorable prior.

## Limitations
This is an exact solution of one natural benchmark, not a general solution of continuous robust quantum discrimination. The proof exploits the source benchmark's special three-copy symmetric-subspace reduction and the algebraic angles \(\pi/4\) and \(\pi/3\). It does not establish a formula for arbitrary \(n\), \(\alpha\), or \(\theta_{\max}\), and it does not address local-product or adaptive-LOCC restrictions.

A residual literature risk remains that an equivalent four-dimensional semi-infinite binary detection calculation may have appeared under substantially different robust-control or group-covariant terminology. Targeted searches of the source paper's cited minimax literature, robust binary discrimination literature, and semantic-result databases did not locate such a covering statement.

## References
1. D. Fujiki and F. Tanaka, *Robust multi-hypothesis quantum-state discrimination under unknown common unitary perturbations via least favorable priors*, arXiv:2609.04020v1 (first public 3 September 2026), especially Secs. III, IV.2, V.4, and Appendix A.
2. G. M. D'Ariano, M. F. Sacchi, and J. Kahn, *Minimax quantum state discrimination*, Phys. Rev. A 72, 032310 (2005), arXiv:quant-ph/0504048.
3. M. T. DiMario and F. E. Becerra, *Robust measurement for the discrimination of binary coherent states*, Phys. Rev. Lett. 121, 023603 (2018).
4. C. W. Helstrom, *Quantum Detection and Estimation Theory*, Academic Press (1976).
