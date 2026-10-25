# Sharp hold-count and universal minimum-energy loss for a common actuator on consecutive-frequency oscillators

## Finding
For every integer \(m\ge1\), the minimum number of positive-duration constant-control segments needed to reach **every** terminal state of \(m\) consecutive-frequency oscillators over one common period is exactly \(2m+1\), **even when segment boundaries may be chosen nonuniformly**. A uniform design with that minimum number achieves every target with a worst-target minimum-energy penalty strictly below \(\pi^2/4\) relative to fully time-varying controls. The sharp bound approaches \(\pi^2/4\) as \(m\) grows.

More generally, for every integer \(N\ge 2m+1\), uniform zero-order-hold sampling gives the exact energy loss factor \(\operatorname{sinc}^{-2}(m\pi/N)\).

## Assumptions and scope
Fix integers \(m\ge1\) and \(N\ge1\). Set \(T=2\pi\), \(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\), and \(e_1=(1,0)^{\mathsf T}\). Consider the real linear system
\[
\dot x_j(t)=jJx_j(t)+e_1u(t),\qquad x_j(0)=0,\quad 1\le j\le m,
\]
with one real input \(u\). Here \(x_j\in\mathbb R^2\) are the momentum/frequency-scaled-position coordinates of physical oscillators \(\ddot q_j+j^2q_j=u\), specifically \(x_j=(\dot q_j,jq_j)\). The terminal target \(y=(y_1,\ldots,y_m)\in\mathbb R^{2m}\) is unrestricted. No input-amplitude constraints are imposed, and energy is \(\mathcal E(u)=\int_0^{2\pi}|u(t)|^2\,dt\).

A partition is \(0=t_0<t_1<\cdots<t_N=2\pi\). A zero-order-hold input takes an independent real constant value \(u_k\) on each interval \([t_k,t_{k+1})\). The initial state is zero, the common horizon is fixed, and there are no amplitude or endpoint-state restrictions besides the specified target. The number of control segments is \(N\), not the number of internal switches (which is at most \(N-1\)). Define \(\operatorname{sinc}(z)=\sin(z)/z\) for \(z\ne0\) and \(\operatorname{sinc}(0)=1\).

## Proof
**Step 1: a partition-independent obstruction.** The full-period terminal map is
\[
y_j=\int_0^{2\pi} e^{jJ(2\pi-t)}e_1u(t)\,dt
=\int_0^{2\pi} e^{-jJt}e_1u(t)\,dt .
\]
Let \(b_k\in\mathbb R^{2m}\) be the terminal response of input \(1\) on segment \(k\) and zero elsewhere, and set \(B=[b_0\ \cdots\ b_{N-1}]\). Each integer-frequency sine and cosine integrates to zero over the complete period, so
\[
\sum_{k=0}^{N-1}b_k=\int_0^{2\pi}(e^{-jJt}e_1)_{j=1}^m\,dt=0.
\]
Thus \(\operatorname{rank}B\le N-1\), whatever the partition. If \(N\le2m\), the range is a proper subspace of \(\mathbb R^{2m}\); hence not all targets are reachable. This uses no numerical rank approximation.

**Step 2: the exact uniform Gramian.** For \(N\ge2m+1\), take \(\Delta=2\pi/N\), \(t_k=k\Delta\), and \(c_k=(k+1/2)\Delta\). Integration of the rotational exponential yields the \(j\)-th planar block
\[
b_{j,k}=\Delta\operatorname{sinc}(j\Delta/2)
\begin{pmatrix}\cos(jc_k)\\-\sin(jc_k)\end{pmatrix}.
\]
For \(1\le j,\ell\le m\), every positive integer frequency among \(j\), \(j+\ell\), and \(|j-\ell|\) is strictly below \(N\), except for the zero frequency when \(j=\ell\). Therefore the root-of-unity sum \(\sum_{k=0}^{N-1}e^{irc_k}=0\) for each nonzero integer \(r\) with \(|r|<N\) gives
\[
\sum_k\cos(jc_k)\cos(\ell c_k)=\frac N2\delta_{j\ell},\qquad
\sum_k\sin(jc_k)\sin(\ell c_k)=\frac N2\delta_{j\ell},
\]
with all mixed cosine/sine sums zero. In particular, the weighted terminal Gramian, using the energy matrix \(\Delta I_N\), is
\[
W_N=B(\Delta I_N)^{-1}B^{\mathsf T}
=\pi\operatorname{diag}_{j=1}^m
\bigl(\operatorname{sinc}^2(j\pi/N)I_2\bigr).
\]
The diagonal is strictly positive, proving full reachability for the uniform partition when \(N\ge2m+1\). Together with Step 1, the exact minimum is \(N=2m+1\).

**Step 3: exact least energy.** A target is reached by vectors \(u\in\mathbb R^N\) satisfying \(Bu=y\). The least discrete energy is \(\min\{\Delta\|u\|_2^2:Bu=y\}=y^{\mathsf T}W_N^{-1}y\), by orthogonal projection or Lagrange multipliers. Hence
\[
\mathcal E_N(y)=\frac1\pi\sum_{j=1}^m
\frac{\|y_j\|_2^2}{\operatorname{sinc}^2(j\pi/N)}.
\]
For unrestricted \(u\in L^2[0,2\pi]\), the continuous terminal Gramian is \(W_*=\int_0^{2\pi}v(t)v(t)^{\mathsf T}dt=\pi I_{2m}\), with \(v(t)=(e^{-jJt}e_1)_{j=1}^m\), again by Fourier orthogonality. Thus \(\mathcal E_*(y)=\pi^{-1}\|y\|_2^2\).

**Step 4: the sharp loss.** On \((0,\pi)\), the sinc function is positive and strictly decreasing (since \(z\cos z-\sin z<0\)). As \(j\pi/N\in(0,\pi)\), the largest ratio \(\mathcal E_N(y)/\mathcal E_*(y)\) for nonzero \(y\) occurs exactly for targets supported on the highest-frequency mode \(j=m\). Consequently
\[
\sup_{y\ne0}\frac{\mathcal E_N(y)}{\mathcal E_*(y)}
=\operatorname{sinc}^{-2}(m\pi/N).
\]
At \(N=2m+1\), one has \(0<m\pi/(2m+1)<\pi/2\), hence \(\operatorname{sinc}(m\pi/(2m+1))>2/\pi\), giving a strict upper bound \(\pi^2/4\). Sending \(m\to\infty\) makes the argument tend to \(\pi/2\); therefore the constant is sharp as a supremum across oscillator counts.

## Verification
The accompanying standalone `verify.py` constructs every segment-response column from exact integral formulas, directly multiplies the weighted Gramian, compares it with the claimed block diagonal for several oscillator counts and uniform partition sizes, tests the partition-independent zero-sum dependence on irregular partitions, checks its rank deficiency for undersampled controls, and compares finite-dimensional least energies to the theoretical ratio. The numerical test is supplementary; the root-of-unity proof above establishes the general result for all integers and all admissible partitions.

## Relationship to prior work
Berlin, Galyaev and Lysenko [1] study the same shared-actuator physical oscillator equations for two frequencies, with bounded-amplitude controls and a **time-minimization** objective; they derive optimal relay switching equations. Our result fixes the horizon to one common period, allows arbitrary real sample-hold amplitudes, determines the minimal number of independent hold segments for complete reachability over *every* target, and gives an exact least-energy spectrum for the uniform design. Their time-optimal switching conditions do not directly imply the stated sampled-energy factor.

Bourdin and Trélat [2] prove that fixed-time reachability persists under sufficiently fine sampled control for regular systems. Their result does not determine the exact finite threshold for this resonant family or quantify the minimum-energy loss. Their linear-quadratic sampled-data theory [3] supplies the general setting but not, in the inspected materials, the specific Fourier diagonalization and sharp budget/loss constant. The subsequent convergence analysis [4] concerns the fine-mesh limit rather than the minimal full-period hold count. The new result is a concrete, quantitative specialization, not a general replacement for those theories.

## Limitations
All frequencies must be consecutive positive integers in exactly the stated normalization, and the horizon must be exactly \(2\pi\). The optimality statement for the number of segments permits arbitrary partitions, but the closed-form energy and uniform loss bound are for uniform partitions only, not asserted minimax among all possible partitions. Inputs have no amplitude constraints; the result is not a bang-bang or minimum-time theorem. The continuous comparison concerns \(L^2\) minimum energy and may differ from numerical implementation cost. It remains possible that an equivalent harmonic-sampling computation exists in older Fourier/control literature under another formulation.

## References
[1] L. Berlin, A. Galyaev, P. Lysenko, *Time-Optimal Control Problem of Two Non-Synchronous Oscillators*, Mathematics **10** (2022), 3552, first published 2022-09-29. DOI: https://doi.org/10.3390/math10193552 (primary MSC 49N05).

[2] L. Bourdin and E. Trélat, *Robustness under control sampling of reachability in fixed time for nonlinear control systems*, arXiv:2006.10983 (first posted 2020-06-19), https://arxiv.org/abs/2006.10983.

[3] L. Bourdin and E. Trélat, *Linear-quadratic optimal sampled-data control problems: convergence result and Riccati theory*, arXiv:1604.06350 (2016), https://arxiv.org/abs/1604.06350.

[4] L. Bourdin and E. Trélat, *Convergence in nonlinear optimal sampled-data control problems*, arXiv:2302.02965 (2023), https://arxiv.org/abs/2302.02965.
