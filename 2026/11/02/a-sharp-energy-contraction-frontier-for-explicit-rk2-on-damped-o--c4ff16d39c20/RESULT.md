# A sharp energy-contraction frontier for explicit RK2 on damped oscillators

## Finding
Consider any two-stage, second-order explicit Runge–Kutta method applied to the two-dimensional damped oscillator
\[
\frac{d}{dt}\begin{pmatrix}u_1\\u_2\end{pmatrix}=
\begin{pmatrix}0&-\omega\\\omega&-\gamma\end{pmatrix}
\begin{pmatrix}u_1\\u_2\end{pmatrix},\qquad \gamma>0,\quad\omega>0.
\]
Every such method has the same one-step matrix \(R=I+hL+(hL)^2/2\). Write \(z=\gamma h>0\) and \(v=(\omega/\gamma)^2>0\). For \(0<v<1\), let \(q(v)\) be the unique positive solution to
\[
q\bigl[(vq-1)^2+3\bigr]=8.
\]
Define the sharp energy-nonexpansion threshold
\[
H(v)=\begin{cases}q(v),&0<v<1,\\2/v,&v\ge 1.\end{cases}
\]
Then for **every** \(\gamma>0\), \(\omega>0\), and \(h>0\), and for **every** real or complex initial vector, the Euclidean energy inequality \(\|Ru\|_2\le\|u\|_2\) holds if and only if \(z\le H(v)\). It is strict for every nonzero vector when \(0<z<H(v)\); when \(z>H(v)\), some initial vector has increased energy after one step.

There is a unique global maximizer of the dimensionless permissible timestep:
\[
\max_{v>0}H(v)=\frac83,\qquad
\operatorname*{argmax}_{v>0}H(v)=\left\{\frac38\right\}.
\]
At this optimum the amplifying matrix has spectral radius \(1/3\), but operator norm \(1\). Thus eigenvalue decay alone misses the sharp energy boundary. At the distinct resonance \(v=1,z=2\), the amplifier equals \(-I\), so the boundary is an exact energy-preserving two-cycle.

## Assumptions and scope
The underlying equation is an autonomous homogeneous two-component real linear system. The damping \(\gamma\) and coupling frequency \(\omega\) are strictly positive; no small-step assumption is made. The stability criterion is Euclidean **one-step nonexpansion for all vectors**, equivalently \(\|R\|_2\le1\), not merely spectral-radius stability or boundedness over multiple steps. All two-stage order-two explicit Runge–Kutta tableaux give the stated polynomial on constant-coefficient linear systems. The dimensionless parameters are \(z=\gamma h\) and \(v=(\omega/\gamma)^2\).

## Proof
Divide \(L\) by \(\gamma\), giving \(A=\begin{psmallmatrix}0&-\sqrt v\\\sqrt v&-1\end{psmallmatrix}\). For \(P(z,v)=I+zA+\tfrac12z^2 A^2\), define the real symmetric defect \(B=I-P^{\mathsf T}P\). Direct exact multiplication gives
\[
B_{11}=\frac{vz^3}{4}\bigl[4-(v+1)z\bigr],\qquad
\det B=\frac{vz^4}{16}(vz-2)\Phi_v(z),
\]
where \(\Phi_v(z)=z[(vz-1)^2+3]-8\). The function \(\Phi_v\) increases strictly from \(-8\) to infinity because
\[
\Phi_v'(z)=3(vz)^2-4vz+4
=3(vz-2/3)^2+8/3>0.
\]
Consequently it has exactly one positive root \(q(v)\). Put \(z_0=4/(v+1)\), where \(B_{11}\) changes sign. Two evaluations locate the determinant zeros:
\[
\Phi_v(2/v)=8/v-8,\qquad
\Phi_v(z_0)=-8\frac{(v-1)^3}{(v+1)^3}.
\]
If \(0<v<1\), these identities imply \(q(v)<z_0<2/v\). For \(0<z<q(v)\) both \(B_{11}\) and \(\det B\) are positive, so \(B\) is positive definite; at \(q(v)\), \(B\) is positive semidefinite. For \(q(v)<z<2/v\), \(\det B<0\); for \(z\ge2/v\), \(B_{11}<0\). Therefore nonexpansion occurs exactly for \(z\le q(v)\).

If \(v>1\), the ordering instead is \(2/v<z_0<q(v)\). For \(0<z<2/v\), \(B\) is positive definite, and at \(2/v\) it is positive semidefinite. Between \(2/v\) and \(q(v)\), the determinant is negative, and beyond \(q(v)\) the first diagonal entry is negative. Hence the sharp threshold is \(2/v\). When \(v=1\), \(\Phi_1(z)=(z-2)(z^2+4)\); direct substitution yields \(P(2,1)=-I\), while \(B\) is positive definite for \(0<z<2\) and has a negative diagonal entry for \(z>2\). This establishes the complete if-and-only-if classification, including endpoints.

To optimize, parameterize the root for \(0<v<1\) by \(s=vq(v)\). Since \(\Phi_v(q)=0\),
\[
q=\frac{8}{(s-1)^2+3},\qquad
v=\frac{s[(s-1)^2+3]}8.
\]
Here \(s\) increases strictly from \(0\) to \(2\) as \(v\) increases from \(0\) to \(1\), since \(dv/ds=(3s^2-4s+4)/8>0\). The displayed formula for \(q\) is maximized uniquely at \(s=1\), giving \(v=3/8\) and \(q=8/3\). The branch \(v\ge1\) has \(H(v)=2/v\le2\), so this maximum is global.

For the optimal parameters, direct substitution gives
\[
P\bigl(8/3,3/8\bigr)=
\frac19\begin{pmatrix}-3&2\sqrt6\\-2\sqrt6&5\end{pmatrix}.
\]
Its eigenvalues are \((1\pm2\sqrt2\,i)/9\), with modulus \(1/3\), whereas the eigenvalues of \(P^{\mathsf T}P\) are \(1\) and \(1/81\). Therefore the operator norm is exactly \(1\), even though every eigenmode decays by a factor of three. The case \(v=1,z=2\) gives \(P=-I\) by substituting in the stability polynomial. All conclusions follow.

## Verification
A standalone Python checker, `verify_rk2.py`, confirms the exact symbolic identities for \(B_{11}\), \(\det B\), monotonicity, optimal parametrization, the sharp resonance, and both singular values at the optimum. It also checks 108 numerical points bracketing the theoretical stability frontier for twelve different positive coupling ratios. Run using the packages listed in `requirements.txt`:

`python verify_rk2.py`

Expected completion begins `VERIFY_OK`. The finite floating-point spot checks are corroborative, not substitutes for the global algebraic sign proof above.

## Relationship to prior work
Strong stability in the energy norm and the difference between eigenvalue and operator-norm criteria are established concepts. Sun and Shu (arXiv:1811.10680, Sections 1–3) give a general energy-method framework and classify the two-stage order-two polynomial as **not** strongly stable across the entire class of semi-negative linear systems. Achleitner, Arnold and Jüngel (arXiv:2308.05689, Sections 0.1–0.4; arXiv:2310.19758, Sections 1–2) relate strong stability to hypocoercivity indices and scheme order. Those statements do not specify a sharp finite timestep for the present canonical two-component damped family, nor the global extremal coupling ratio and the boundary spectral/energy separation. No directly implying special-case theorem was identified in the inspected material; a specialized earlier derivation elsewhere cannot be excluded.

## Limitations
The theorem is exact only for this two-dimensional constant-coefficient damped family and the second-order two-stage explicit RK stability polynomial. It does not assert strong stability for arbitrary dissipative matrices, nonautonomous problems, nonlinear systems, or other integrators. At the endpoint \(z=H(v)\), nonexpansion is nonstrict; repeated-step asymptotic stability is a separate question. The numerical verifier cannot certify novelty or extend the theorem beyond the stated matrix family. Independent mathematical and priority review has not been performed.

## References
1. Zheng Sun and Chi-Wang Shu, *Strong stability of explicit Runge–Kutta time discretizations* (arXiv:1811.10680, first version 2018-11-26), https://arxiv.org/abs/1811.10680.
2. Franz Achleitner, Anton Arnold, and Ansgar Jüngel, *Necessary and sufficient conditions for strong stability of explicit Runge-Kutta methods* (arXiv:2308.05689, first version 2023-08-10), https://arxiv.org/abs/2308.05689.
3. Franz Achleitner, Anton Arnold, and Ansgar Jüngel, *Hypocoercivity for Linear ODEs and Strong Stability for Runge–Kutta Methods* (arXiv:2310.19758, first version 2023-10-30), https://arxiv.org/abs/2310.19758.
