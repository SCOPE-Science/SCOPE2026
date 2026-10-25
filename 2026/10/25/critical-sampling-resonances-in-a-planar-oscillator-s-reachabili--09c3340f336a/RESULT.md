# Critical sampling resonances in a planar oscillator's reachability matrix

## Finding

For the continuously controllable planar oscillator
\[
\dot{x}(t)=Ax(t)+Bu(t),\qquad A=\omega\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad B=\begin{pmatrix}1\\0\end{pmatrix},\quad \omega>0,
\]
let \(A_h=e^{hA}\), \(B_h=\int_0^h e^{sA}B\,ds\), and \(W_h=[B_h,A_hB_h]\). The matrix \(W_h\) is singular exactly at the positive sampling periods \(h_m=m\pi/\omega\), \(m=1,2,\ldots\), despite continuous-time controllability. As \(h\to h_m\) through nonresonant values,
\[
\sigma_{\min}(W_h)\sim\begin{cases}\sqrt{2}|h-h_m|,&m\text{ odd},\\ \omega|h-h_m|^2/\sqrt{2},&m\text{ even},\end{cases}
\]
so \(\|W_h^{-1}\|_2\) grows like \(1/(\sqrt{2}|h-h_m|)\) at odd resonances and \(\sqrt{2}/(\omega|h-h_m|^2)\) at even resonances. An exact-tracking construction that solves through \(W_h^{-1}\) is therefore undefined at the resonances and increasingly ill-conditioned nearby.

## Assumptions and scope

The input is scalar and held constant on each interval of length \(h>0\); the plant is the exact zero-order-hold discretization of the system above. The frequency \(\omega\) is fixed and positive. The conclusion concerns the feedforward/feedback exact-tracking construction using the sampled reachability matrix. It does not address the separate static-feedback theorem in the same paper, which assumes a nilpotent plant matrix.

## Proof

The continuous-time controllability matrix is \([B,AB]=\begin{pmatrix}1&0\\0&\omega\end{pmatrix}\), with determinant \(\omega\ne0\). Put \(\theta=\omega h\). Direct integration gives
\[
A_h=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix},\qquad B_h=\frac1\omega\begin{pmatrix}\sin\theta\\1-\cos\theta\end{pmatrix}.
\]
Let \(r=\|B_h\|_2=2|\sin(\theta/2)|/\omega\). Rotation preserves norm and \(B_h^\top A_hB_h=r^2\cos\theta\), so
\[
W_h^\top W_h=r^2\begin{pmatrix}1&\cos\theta\\\cos\theta&1\end{pmatrix}.
\]
Hence the singular values are exactly \(r\sqrt{1+|\cos\theta|}\) and \(r\sqrt{1-|\cos\theta|}\). Also
\[
\det W_h=\frac{4\sin^2(\theta/2)\sin\theta}{\omega^2}.
\]
Thus \(W_h\) is singular exactly when \(\theta=m\pi\); at odd multiples its columns are nonzero and opposite, while at even multiples \(B_h=0\).

For odd \(m\), write \(\theta=m\pi+\delta\), with \(\delta=\omega(h-h_m)\). Then \(r\to2/\omega\) and \(\sqrt{1-|\cos\theta|}\sim|\delta|/\sqrt2\), giving \(\sigma_{\min}(W_h)\sim\sqrt2|h-h_m|\). For even \(m\), \(r\sim|\delta|/\omega\) and the same square-root factor is \(|\delta|/\sqrt2\), giving \(\sigma_{\min}(W_h)\sim\omega|h-h_m|^2/\sqrt2\). Taking reciprocals proves the inverse-norm laws.

## Verification

The proof is analytic and uses exact matrix identities and trigonometric expansions; singularity is not inferred from a failed numerical solve. The included standard-library script checks the determinant identity, closed-form singular values, and both asymptotic ratios at several test points. The computation corroborates, but does not replace, the proof.

## Relationship to prior work

The motivating preprint states in its single-input exact-tracking section that continuous-time controllability implies controllability of \((A_h,B_h)\) and invertibility of \(W_h\). The oscillator above disproves that unrestricted implication. Sampling-induced loss of controllability is classical, so the contribution here is not that broad fact alone: it is the exact singular-value formula and the distinct first- versus second-order blow-up of \(\|W_h^{-1}\|_2\) at odd and even resonances for this reachability matrix. The available abstracts of earlier sampled-data controllability papers do not state these parity-dependent asymptotics; full-text overlap remains a residual risk.

## Limitations

This is a two-dimensional, single-input, exact zero-order-hold calculation. It does not establish a resonance law for arbitrary matrices, quantify noise propagation through the complete nonlinear controller, or invalidate the separate static-feedback theorem under its nilpotent-plant assumption. The inverse norm gives worst-case amplification; an individual state/control vector need not attain it.

## References

1. A. Polyakov, D. Efimov, and X. Ping, *Consistent discretization of finite/fixed-time controllers*, arXiv:2207.03235, first public version 7 July 2022.
2. A. Polyakov, D. Efimov, and X. Ping, *Consistent discretization of homogeneous finite/fixed-time controllers for LTI systems*, Automatica 155 (2023), article 111118, DOI: 10.1016/j.automatica.2023.111118.
3. M. L. J. Hautus, *Controllability and stabilizability of sampled systems*, IEEE Transactions on Automatic Control 17(4) (1972), 528–531, DOI: 10.1109/TAC.1972.1100045.
4. J. J. Yamé, *Some Remarks on the Controllability of Sampled-Data Systems*, SIAM Journal on Control and Optimization, DOI: 10.1137/090765304.
