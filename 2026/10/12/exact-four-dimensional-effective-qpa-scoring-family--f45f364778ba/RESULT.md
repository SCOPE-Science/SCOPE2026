# Exact four-dimensional effective QPA scoring family
## Finding
For the quantum parameterized attention scoring circuit defined by Eq. (7) of arXiv:2605.25365v1, the effective dimension used in that work is exactly \(d_Q=4\). The paper proves only \(2\le d_Q\le4\). The upper endpoint is attained: four independent local variations of the scalar score occur at one explicit parameter point and four explicit inputs.

Equivalently, among the five trainable parameters \((\theta_s,\gamma_d,\gamma_s,\alpha,\beta)\), precisely one local functional direction is redundant for this scoring family. A convenient reparameterization is
\[
\omega_d=\theta_s+2\gamma_d,\qquad \omega_s=\theta_s+2\gamma_s.
\]
The score depends on the original five parameters only through \((\omega_d,\omega_s,\alpha,\beta)\), and all four of these combinations are genuinely active.

## Assumptions and scope
The circuit is the two-qubit QPA score circuit in Eq. (7) of arXiv:2605.25365v1, with the encoding angles
\[
\phi_0=\frac{\pi}{4}+\frac{\omega_d+\omega_s}{2}q+\frac{\omega_s-\omega_d}{2}k,
\]
\[
\phi_1=\frac{\pi}{4}+\frac{\omega_s-\omega_d}{2}q+\frac{\omega_d+\omega_s}{2}k,
\]
and entangling angle \(t=\alpha(q+k)\). The mixer is \(R_X(2\beta)\otimes R_X(2\beta)\), and the scalar score is the probability of even computational-basis parity.

Here \(q,k\in\mathbb R\). Effective dimension means the maximum local functional rank of the source-defined QPA score family with respect to its trainable parameters. The claim does not concern Fisher effective dimension, statistical generalization dimension, or the dimension of the entire downstream image-classification model.

## Proof
Let
\[
\lambda_1=\frac{\omega_d+\omega_s}{2},\qquad
\lambda_2=\frac{\omega_s-\omega_d}{2}.
\]
Then \(\phi_0=\pi/4+\lambda_1q+\lambda_2k\) and \(\phi_1=\pi/4+\lambda_2q+\lambda_1k\). With \(c_0=\cos(\phi_0/2)\) and \(s_0=\sin(\phi_0/2)\), the real state immediately before the mixer has amplitudes
\[
\left(
 c_0\cos\frac{\phi_1+t}{2},
 s_0\cos\frac{\phi_1-t}{2},
 s_0\sin\frac{\phi_1-t}{2},
 c_0\sin\frac{\phi_1+t}{2}
\right).
\]
The even-parity projector is \(\Pi=(I+Z\otimes Z)/2\). Conjugating \(Z\otimes Z\) through the identical \(X\)-axis mixers and evaluating on the state above gives
\[
\mu(q,k)=\frac12\left[
1+\cos^2(2\beta)\cos\phi_0
-\sin^2(2\beta)\left(
\cos\phi_0\sin\phi_1\cos t+\cos\phi_1\sin t
\right)
\right].
\]
This formula depends on the original five parameters only through \((\omega_d,\omega_s,\alpha,\beta)\), so \(d_Q\le4\).

For the matching lower bound, take
\[
(\omega_d,\omega_s,\alpha,\beta)
=\left(\frac\pi2,\frac\pi3,\frac\pi4,\frac\pi8\right)
\]
and evaluate the four score functions at
\[
(q,k)\in\{(-2,2),(-1,-2),(1,2),(2,2)\}.
\]
Their Jacobian with respect to \((\omega_d,\omega_s,\alpha,\beta)\) is
\[
J=\begin{pmatrix}
-\frac12-\frac{\sqrt2}{4}&0&0&-\frac12+\frac{\sqrt2}{2}\\
-\frac{\sqrt2}{16}&-\frac{3\sqrt2}{16}&-\frac{3\sqrt2}{8}&-1-\frac{\sqrt2}{2}\\
\frac18&-\frac38&-\frac{3\sqrt2}{8}&\frac{\sqrt2}{2}\\
0&\frac{-\sqrt6+\sqrt2+2\sqrt3}{8}&-\frac{\sqrt6+\sqrt2}{4}&-\frac14+\frac{\sqrt2+\sqrt6}{4}
\end{pmatrix}.
\]
Direct exact evaluation gives
\[
\det J=
\frac{111}{512}
+\frac{87\sqrt2}{512}
+\frac{45\sqrt3}{256}
+\frac{129\sqrt6}{1024}>0.
\]
Therefore the four score values have local rank four. The smooth section \(\theta_s=0\), \(\gamma_d=\omega_d/2\), \(\gamma_s=\omega_s/2\) lifts this witness to the original five-parameter family. Thus \(d_Q\ge4\), and consequently \(d_Q=4\).

## Verification
The embedded script `artifacts/verify.py` symbolically differentiates the closed score formula, evaluates the four-input Jacobian at the stated parameter point, checks every displayed matrix entry, and verifies the exact algebraic determinant. Its successful terminal condition is `VERIFY_OK`.

The script is a replay of a finite algebraic certificate. The dimension conclusion itself follows analytically from the reparameterization upper bound and the nonzero Jacobian determinant; no numerical rank threshold or finite-sampling extrapolation is used.

## Relationship to prior work
Zhang, Wang, Ye, Liao and coauthors introduce the QPA score family and prove the interval \(2\le d_Q\le4\), with the same four-parameter reduction supplying their upper bound. The present finding closes that interval by proving that the upper endpoint is actually attained.

Haug, Bharti and Kim develop general geometric notions of parameterized-quantum-circuit capacity and effective quantum dimension. That broader framework motivates rank-based analysis but does not compute the scalar QPA family in arXiv:2605.25365v1 or imply the explicit rank-four witness above. Public secondary summaries of the QPA preprint repeat the interval \(2\le d_Q\le4\) rather than an exact value.

## Limitations
The statement is specific to the scalar QPA score and the gate ordering in Eq. (7) of arXiv:2605.25365v1. It does not assert the same Jacobian certificate for a differently ordered circuit convention. It also does not identify \(d_Q\) with Fisher effective dimension, establish a training advantage, or prove a generalization bound.

The rank-four witness is local. It proves the maximum effective dimension is four, but it does not claim rank four at every parameter point or every input set.

## References
1. W. Zhang, J. Wang, T. Ye, C. Liao et al., *Quantum Parameterized Self-Attention Network for Image Classification*, arXiv:2605.25365v1, 2026.
2. T. Haug, K. Bharti and M. S. Kim, *Capacity and Quantum Geometry of Parametrized Quantum Circuits*, PRX Quantum 2, 040309 (2021), DOI: 10.1103/PRXQuantum.2.040309.
