# Sharp mean-square timing-jitter margin of a two-step deadbeat double-integrator controller

## Finding

A fixed, exactly two-sample-deadbeat feedback law for a double integrator has a sharp and nonzero tolerance to independent symmetric sampling jitter. For the model below, put \(z=\delta^2\), and let \(z_*\) be the unique root in \((0,1)\) of
\[
3z^3-11z^2+12z-2=0.
\]
Then \(z_*=0.202014738674272\ldots\) and \(\delta_*=\sqrt{z_*}=0.449460497345731\ldots\). For every deterministic nonzero initial state, the mean-square sampled state decays geometrically when \(0\le\delta<\delta_*\), remains uniformly bounded above and away from zero when \(\delta=\delta_*\), and grows geometrically when \(\delta_*<\delta<1\).

More precisely, for each \(0<\delta<1\) there is a positive-definite real matrix \(P_\delta\) and a number \(r(\delta)>0\) such that, for every deterministic initial state \(x_0\in\mathbb R^2\) and all integers \(n\ge0\),
\[
\mathbb E[x_n^{\mathsf T}P_\delta x_n]
=r(\delta)^n x_0^{\mathsf T}P_\delta x_0,
\qquad
r(\delta)\begin{cases}<1,&\delta<\delta_*,\\=1,&\delta=\delta_*,\\>1,&\delta>\delta_*.
\end{cases}
\]
At \(\delta=0\), the sampled state vanishes exactly after two steps. The jitter tolerance is not a worst-case deterministic stability guarantee: in the nonempty interval \(1/3<\delta<\delta_*\), the longer of the two possible fixed sampling intervals is itself unstable, whereas the equiprobable independently mixed scheme is mean-square stable. At \(\delta=2/5\), the two intervals are \(3/5\) and \(7/5\); the \(7/5\) deterministic branch is unstable, yet the random system is mean-square stable, with an explicit rational quadratic Lyapunov certificate below.

## Assumptions and scope

Consider the scalar double-integrator plant and zero-order-held position-velocity state feedback
\[
\dot q(t)=v(t),\qquad \dot v(t)=u(t),\qquad
u(t)=-q(t_n)-\frac32v(t_n)
\quad(t_n\le t<t_{n+1}).
\]
The initial state \(x_0=(q(0),v(0))^{\mathsf T}\) is deterministic. The strictly increasing update times satisfy \(t_0=0\) and \(t_{n+1}-t_n=H_n\), with independent identically distributed intervals
\[
\Pr(H_n=1-\delta)=\Pr(H_n=1+\delta)=\frac12,
\qquad 0\le\delta<1.
\]
Intervals are independent of the initial state, and the feedback gains do not adapt to the realized interval. All equations concern the exact, noiseless plant and the state sampled at update instants; no numerical discretization or floating-point approximation is assumed.

## Proof

**Exact sampled dynamics.** Hold \(u=-q_n-(3/2)v_n\) for duration \(h\). Integrating twice yields
\[
x_{n+1}=A(h)x_n,
\quad
A(h)=\begin{pmatrix}
1-h^2/2&h-3h^2/4\\
-h&1-3h/2
\end{pmatrix}.
\]
Direct multiplication gives \(A(1)^2=0\); hence the periodic, unit-interval controller is exactly two-step deadbeat. Also
\[
\det A(h)=\frac12(h-1)(h-2).
\]
For \(0<\delta<1\), the matrices \(A_-=A(1-\delta)\) and \(A_+=A(1+\delta)\) are invertible.

**Exact second-moment transfer.** Write \(m_n=(\mathbb E q_n^2,\mathbb E q_nv_n,\mathbb E v_n^2)^{\mathsf T}\). Independence of each new interval from the past implies \(m_{n+1}=K(z)m_n\), where \(z=\delta^2\) and
\[
K(z)=\begin{pmatrix}
(1+z)^2/4&(1+3z^2)/4&(1-2z+9z^2)/16\\
(3z-1)/2&(6z-1)/2&(9z-1)/8\\
1+z&1+3z&(1+9z)/4
\end{pmatrix}.
\]
Its determinant identity is
\[
\det(I_3-K(z))=-\frac12(3z^3-11z^2+12z-2).
\]
These are polynomial identities obtained from the two exact matrices, not approximations or numerical spectral fits.

**Positive quadratic Perron functional and all-state equivalence.** Define the adjoint second-moment operator on symmetric matrices by
\[
\mathcal L_\delta^*(P)=\frac12 A_-^{\mathsf T}PA_-+
\frac12 A_+^{\mathsf T}PA_+.
\]
It maps positive-semidefinite matrices to positive-semidefinite matrices. Because \(A_-\) and \(A_+\) are invertible, the map \(P\mapsto \mathcal L_\delta^*(P)/\operatorname{tr}(\mathcal L_\delta^*(P))\) is well-defined and continuous on the compact convex set of positive-semidefinite symmetric \(2\times2\) matrices with trace one. Brouwer's theorem yields a nonzero positive-semidefinite eigenmatrix \(P\) with eigenvalue \(r>0\).

The eigenmatrix is in fact positive definite. If it had rank one, the identity \(\mathcal L_\delta^*(P)=rP\) would imply that both transposed step matrices preserve its one-dimensional range. But their commutator is nonsingular:
\[
\det(A_+A_--A_-A_+)=-\delta^2(1-\delta^2)^2<0.
\]
The transpose matrices have the same nonsingularity property for their commutator; thus they cannot share an invariant real line. The rank-one case is impossible.

A positive-definite eigenmatrix also shows that \(r\) equals the spectral radius of the covariance transfer: every real symmetric matrix \(Q\) lies between \(-cP\) and \(cP\) for some \(c>0\), and positivity then bounds iterates of \(\mathcal L_\delta^*\) in norm by a constant times \(r^n\); \(r\) is itself an eigenvalue. Taking the adjoint expectation yields the exact energy identity for every \(n\). Norm equivalence of \(P\) and the Euclidean metric makes the classification valid for **every** nonzero deterministic initial state, not merely for a generic covariance or a special eigenvector.

**Unique transition.** The spectral radius \(r(\delta)\) is continuous on \([0,1]\). At \(\delta=0\), the two-step nilpotence gives \(r(0)=0\). At the endpoint \(\delta=1\), the covariance transfer has eigenvalues \(5,1/2,1/2\), and \(r(1)=5\). Any crossing through \(r=1\) requires \(\det(I-K(\delta^2))=0\). Set \(F(z)=3z^3-11z^2+12z-2\). Then \(F(0)=-2\), \(F(1)=2\), and \(F'(z)=9z^2-22z+12\) is positive up to its only critical point in \((0,1)\), \(z=(11-\sqrt{13})/9\), and negative afterwards. Its value at the right endpoint remains positive, so \(F\) has exactly one zero in \((0,1)\). By continuity, this must be the only crossing of \(r\) through one, with the asserted strict signs on either side. At the crossing, the exact \(P\)-energy is constant and bounds the expected squared Euclidean norm both above and away from zero.

**An individually unstable branch under stable random mixing.** For a fixed \(h\in(0,2)\), the trace and determinant are
\[
\operatorname{tr}A(h)=2-\frac{3h}{2}-\frac{h^2}{2},\qquad
\det A(h)=1-\frac{3h}{2}+\frac{h^2}{2}.
\]
The three strict degree-two Schur conditions reduce to \(h(3-h)/2>0\), \(h^2>0\), and \(4-3h>0\). Consequently this deterministic branch is Schur stable exactly for \(0<h<4/3\). The longer random interval is \(h=1+\delta\); it is individually unstable for \(\delta>1/3\), even when the mixture is stable for \(\delta<\delta_*\). To verify the strict rational example at \(\delta=2/5\), set
\[
P=\begin{pmatrix}
69675/10916&92725/21832\\
92725/21832&204927/43664
\end{pmatrix}.
\]
Its leading entry is positive, and its determinant is \(1420090775/119159056>0\). Direct rational multiplication gives
\[
P-\frac12\big(A(3/5)^{\mathsf T}PA(3/5)+A(7/5)^{\mathsf T}PA(7/5)\big)=I_2.
\]
Thus random mean-square stability at \(\delta=2/5\) has an exact strict Lyapunov certificate, while the longer individual branch fails the Schur condition since \(4-3(7/5)=-1/5<0\).

## Verification

The included `verify.py` uses only the Python 3 standard library. It computes the sampled matrices independently as formal polynomials in \(\delta\), forms the exact second-moment map, verifies the determinant and commutator identities coefficient by coefficient, checks the rational Lyapunov equality and principal minors, and compares covariance recursion against exhaustive finite sample-path enumeration for several rational jitter strengths and initial states. It also encloses the polynomial root using rational bisection. Run `python3 verify.py` from the extracted package directory. The numerical root approximation and finite-path tests are supplementary; the quantified spectral and root-uniqueness arguments above establish the full theorem for every real \(0\le\delta<1\) and all horizons.

## Relationship to prior work

General matrix-vectorization criteria for moment stability with random sampling intervals and communication delays are already in Sun, Sun and Chen (2021). The present result does **not** assert originality of the second-moment spectral-radius criterion or random-switching stability analysis. It supplies a closed, exact all-jitter classification for a physically elementary two-step deadbeat double-integrator controller, including the unique algebraic boundary and a strict constructive example where an unstable individual sampling branch is made mean-square stable by independent mixing. These concrete constants and the all-initial-state threshold were not established by the accessible material inspected here. Vallarella and Haimovich (2022) analyze nonuniform sampling for nonlinear sampled-data systems from a uniform-in-sampling small-period perspective, without this stochastic two-point threshold. Su, Li and Lu (2021) analyze stochastic channel transmission delays on a fixed sampling clock, not independent random physical sampling periods. Broad random-switching theory may imply general aspects of the example; this exact specialization should not be mistaken for a new general stability theorem.

## Limitations

The analysis addresses exact plant states at discrete sampling instants, with no communication delay, measurement noise, parameter mismatch, actuation saturation, or adaptive feedback gains. Its sharp threshold is specific to the fixed feedback \((-1,-3/2)\), independent equiprobable two-point intervals of mean one, and the scalar double integrator. The result does not give an optimal feedback law, almost-sure Lyapunov exponents, or a theorem for arbitrary interval laws. Complete full-text comparison with Sun, Sun and Chen (2021) was not possible, so a highly specific previously published specialization cannot be ruled out. No independent scientific audit has been performed.

## References

- W. Su, J. Li, and J. Lu, *Mean-Square Input-Output Stability and Stabilizability of a Networked Control System with Random Channel Induced Delays*, arXiv:2108.12795 (initially public 2021-08-29), https://arxiv.org/abs/2108.12795.
- H. Sun, J. Sun, and J. Chen, *Analysis and synthesis of networked control systems with random network-induced delays and sampling intervals*, Automatica 125 (2021), article 109385, https://doi.org/10.1016/j.automatica.2020.109385.
- A. J. Vallarella and H. Haimovich, *On the stability of nonlinear sampled-data systems and their continuous-time limits*, arXiv:2202.10549 (initially public 2022-02-21), https://arxiv.org/abs/2202.10549.
