# Control-dependent diffusion breaks the published SQH projection formula
## Finding
For the Parkinson--Roy Fokker--Planck epidemic-control problem, Theorem 4.3 does not establish its stated contraction, unique-fixed-point, or Hamiltonian-minimum conclusions. As written, the theorem defines \(r(w)\) as a scalar Hamiltonian contribution, but its projected update treats \(r(u^k)\) as a three-vector; even on a one-coordinate affine restriction, the minimizer depends on the coefficient of \(w\), not on the value \(r(u^k)\). More specifically, for the paper's own simulation diffusion \(\sigma_S=-\sigma_I=\sqrt{0.02}(1-w_1)SI\), freezing the state and adjoint at SQH step \(k\) gives \(r_k(w)=c_k+d_{1,k}w_1+d_{2,k}w_2+d_{3,k}w_3+D_k(1-w_1)^2\), where \(D_k=0.01\int_\Omega f^k S^2I^2(q^k_{SS}+q^k_{II})\,dS\,dI\). Hence the first-coordinate augmented subproblem has curvature \(\beta_2+2\varepsilon-2D_k\), and, when this is positive and the unconstrained minimizer lies in the control interval, its minimizer is \((d_{1,k}-\beta_1-2D_k+2\varepsilon u_1^k)/(\beta_2+2\varepsilon-2D_k)\), not the paper's displayed expression. No hypothesis in Theorem 4.3 forces \(D_k=0\) or replaces the scalar \(r\) by the needed coefficient or derivative map. The final fixed-point step also drops the nonnegative proximal term: minimizing \(H(w)+\varepsilon\lvert w-u^*\rvert^2\) at \(u^*\) yields only \(H(u^*)\le H(w)+\varepsilon\lvert w-u^*\rvert^2\), not \(H(u^*)\le H(w)\). This finding diagnoses the convergence proof only; it does not assert divergence of the implemented SQH scheme or invalidate the separate descent statements of Theorems 4.1--4.2.

## Assumptions and scope
Parkinson and Roy study a controlled Fokker--Planck equation for \(X=(S,I)\) with three nonnegative controls. The relevant convergence theorem assumes the mixed control cost
\[
\ell(w)=\frac{\beta_2}2\lvert w\rvert^2+\beta_1\lvert w\rvert_1,
\]
and writes the Hamiltonian as
\[
H(t,f_u,q_u,w)=\frac{\beta_2}2\lvert w\rvert^2+\beta_1\lvert w\rvert_1-r(w).
\]
The theorem defines \(r(w)\) by a spatial integral and therefore as a scalar. The claim here concerns only the proof and sufficient conditions asserted in Theorem 4.3. It does not dispute the existence theorem, the Pontryagin necessary condition for an actual optimum, or the descent identities in Theorems 4.1--4.2.

For the source's numerical model,
\[
\sigma_S=-\sigma_I=\sqrt{0.02}(1-w_1)SI.
\]
At a fixed SQH step, \(f^k\) and \(q^k\) are held fixed while minimizing in \(w\).

## Proof
The drift \(F(X,w)\) is affine in \(w\). Let \(d_{i,k}\) denote its three scalar Hamiltonian coefficients after integrating against \(f^k\nabla q^k\). For the first coordinate one may write explicitly
\[
d_{1,k}=\int_\Omega f^k\,\beta SI\,(q^k_S-q^k_I)\,dS\,dI.
\]
Because both diagonal diffusion coefficients have square
\[
\sigma_j^2=0.02(1-w_1)^2S^2I^2,
\]
the diffusion part of the source's scalar \(r_k(w)\) is
\[
\frac12\sum_{j=1}^2\int_\Omega f^k\sigma_j^2q^k_{x_jx_j}\,dS\,dI
=D_k(1-w_1)^2,
\]
where
\[
D_k=0.01\int_\Omega f^kS^2I^2(q^k_{SS}+q^k_{II})\,dS\,dI.
\]
Thus
\[
r_k(w)=c_k+d_{1,k}w_1+d_{2,k}w_2+d_{3,k}w_3+D_k(1-w_1)^2.
\]
Inside the nonnegative control box, the first-coordinate portion of the augmented Hamiltonian is, up to a constant,
\[
\frac{\beta_2}2w_1^2+\beta_1w_1-d_{1,k}w_1-D_k(1-w_1)^2+\varepsilon(w_1-u_1^k)^2.
\]
Its derivative is
\[
(\beta_2+2\varepsilon-2D_k)w_1+\beta_1-d_{1,k}+2D_k-2\varepsilon u_1^k.
\]
Therefore, whenever \(\beta_2+2\varepsilon-2D_k>0\), the unconstrained minimizer is
\[
\widehat w_1=\frac{d_{1,k}-\beta_1-2D_k+2\varepsilon u_1^k}{\beta_2+2\varepsilon-2D_k},
\]
followed by projection to the first control interval. If the curvature is nonpositive, strict convexity of that scalar subproblem is unavailable. Either way, the source's projected formula with denominator \(\beta_2+2\varepsilon\) does not follow unless additional structure removes the \(D_k\) term.

There is also a more basic mismatch. The theorem's displayed definition makes \(r(w)\) scalar, but the proposed update adds \(r(u^k)\) to the three-vector \(2\varepsilon u^k-\beta_1\mathbf 1\). Even after choosing a broadcasting convention, a scalar value is not the coefficient or gradient needed to minimize a nonlinear scalar Hamiltonian. For example, on one coordinate with \(r(w)=dw\), exact minimization uses \(d\), whereas substituting the value \(r(u^k)=du^k\) generally gives a different point.

Finally, if \(u^*\) minimizes the augmented function \(H(w)+\varepsilon\lvert w-u^*\rvert^2\), the conclusion is only
\[
H(u^*)\le H(w)+\varepsilon\lvert w-u^*\rvert^2.
\]
The positive last term cannot be deleted without another argument. A scalar check on \([0,1]\) is \(H(w)=-w^2\), \(u^*=0\), and \(\varepsilon=2\): then \(H(w)+2w^2=w^2\) is minimized at \(0\), but \(H(1)=-1<H(0)=0\). Hence the fixed-point inference in the proof is not valid as a general implication.

## Verification
The bundled `verify.py` checks by exact rational arithmetic the coefficient expansion, the corrected first-coordinate minimizer, a numerical rational instance where the printed value-based update differs from the true minimizer, and the proximal fixed-point counterexample. The exact source formulas used above were independently read in the open-access full text: the scalar definition of \(r\), the projected update, the fixed-point step, the drift, and the control-dependent diffusion.

## Relationship to prior work
The motivating article first appeared as arXiv:2601.20181v1 on 2026-01-28 and the journal version lists primary MSC 92D30. Campana, Katz, and Giordano (2024) analyze SQH for a different ODE epidemic-control setting with a smooth cost and report rigorous global convergence guarantees; that result does not imply the projected formula above for a Fokker--Planck Hamiltonian with control-dependent diffusion. Borzì's 2023 monograph develops SQH broadly, including stochastic and PDE control, while Hofmann and Borzì (2025) analyze a distinct discrete-time neural-network setting. None of the inspected material states the source-specific \(D_k(1-w_1)^2\) correction or repairs Theorem 4.3.

A previous result concerning the same Parkinson--Roy paper addresses the covariance implied by independent compartment noises versus transmission-rate noise. That statement neither uses nor implies the present Hamiltonian-minimization correction.

## Limitations
The result is a diagnosis of Theorem 4.3 as written. It does not prove that the implemented SQH iterations diverge, that a suitable modified convergence theorem is impossible, or that \(D_k\) is nonzero at every iteration. A corrected theorem could impose a vector derivative or coefficient-map hypothesis and enough curvature or monotonicity to obtain a contraction. The open repository copy of the closely related Campana--Katz--Giordano paper was discoverable but its linked PDF was inaccessible during inspection, so comparison to that paper used its bibliographic record and abstract; this remains a literature-access risk, not evidence of novelty.

## References
1. C. Parkinson and S. Roy, “A Fokker--Planck framework for control of epidemics,” *Journal of Mathematical Biology* 93, 47 (2026), DOI 10.1007/s00285-026-02462-7; arXiv:2601.20181v1.
2. F. Calà Campana, R. Katz, and G. Giordano, “Sequential-Quadratic-Hamiltonian Optimal Control of Epidemic Models With an Arbitrary Number of Infected and Non-Infected Compartments,” *IEEE Control Systems Letters* 8 (2024), 1805--1810, DOI 10.1109/LCSYS.2024.3412775.
3. A. Borzì, *The Sequential Quadratic Hamiltonian Method: Solving Optimal Control Problems*, Chapman & Hall/CRC, 2023, ISBN 9780367715526.
4. S. Hofmann and A. Borzì, “The Pontryagin Maximum Principle for Training Convolutional Neural Networks,” *SIAM Journal on Mathematics of Data Science* 7 (2025), 1616--1642, DOI 10.1137/24M1675369.
