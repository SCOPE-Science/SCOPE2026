# The exact Gaussian deterioration frontier for a two-mode Nyström spectral preconditioner

## Finding

Consider a symmetric positive definite Hessian \(H=I+A\) with \(A=\operatorname{diag}(a,b)\) and \(a>b>0\). Form a rank-one, one-pass Nyström approximation to \(A\) from a Gaussian vector \(\omega\), and the scaled rank-one spectral limited-memory preconditioner with oracle scale \(\theta=1+b\). **The preconditioned matrix is worse conditioned than \(H\) if and only if one explicit positive cubic is negative.** The unique positive crossing is strictly between zero and one. For standard isotropic Gaussian sketches the probability of deterioration is an explicit Cauchy tail; the same probability for Gaussian sketches of covariance \(A+A^2\) is strictly smaller. With \(b\) fixed and \(a\to\infty\), the former probability decays as \(a^{-1}\), the latter as \(a^{-2}\), with explicit nonzero constants.

Set \(L=1+a\), \(m=1+b\), and
\[
Q_{a,b}(z)= bLm+m(a-b)(L+1)z-b\bigl[L(L+m)+m^2\bigr]z^2-am(L+m)z^3.
\]
There is exactly one positive root \(\zeta_{a,b}\in(0,1)\). If \(\omega_1\ne0\), put \(z=(b\omega_2/(a\omega_1))^2\). Then the split-preconditioned matrix \(B\), defined below, obeys
\[
\kappa_2(B)>\frac Lm\quad\Longleftrightarrow\quad z>\zeta_{a,b},
\]
where \(\kappa_2\) is the spectral condition number. Equality occurs at the unique crossing; the null directions \(\omega_1\omega_2=0\) have probability zero for the Gaussian laws considered.

For \(\omega\sim N(0,I_2)\),
\[
\boxed{p_{\rm iso}(a,b)=\frac2\pi\arctan\left(\frac{b}{a\sqrt{\zeta_{a,b}}}\right).}
\]
For \(\omega\sim N(0,A+A^2)\),
\[
\boxed{p_{\rm informed}(a,b)=\frac2\pi\arctan\left(\frac{\sqrt{b^3(1+b)}}{\sqrt{a^3(1+a)}\sqrt{\zeta_{a,b}}}\right).}
\]
Both probabilities are strictly positive, and \(p_{\rm informed}<p_{\rm iso}\) for all \(a>b>0\). With fixed \(b\), define
\[
z_\infty(b)=\frac{\sqrt{b^2+4(1+b)^2}-b}{2(1+b)}\in(0,1).
\]
Then \(\zeta_{a,b}\to z_\infty(b)\) as \(a\to\infty\), and
\[
\boxed{p_{\rm iso}\sim\frac{2b}{\pi\sqrt{z_\infty(b)}}a^{-1},\qquad
p_{\rm informed}\sim\frac{2\sqrt{b^3(1+b)}}{\pi\sqrt{z_\infty(b)}}a^{-2}.}
\]

## Assumptions and scope

The dimension is exactly two; \(a>b>0\); all matrices and random variables are real; computations defining the theorem are in exact arithmetic. Use the rank-one specialization of one-pass Nyström approximation, namely
\[
y=A\omega,\qquad v=\frac y{\|y\|_2},\qquad
\widehat\lambda=\frac{\|y\|_2^2}{\omega^{\mathsf T}A\omega}.
\]
Thus \(A_N=\widehat\lambda vv^{\mathsf T}\), with \(\widehat\lambda\) the nonzero eigenvalue of the Nyström approximation \(A\omega(\omega^{\mathsf T}A\omega)^{-1}(A\omega)^{\mathsf T}\). The specified oracle scale \(\theta=m\) is an analytic benchmark rather than a data-driven choice. Define the scaled spectral inverse preconditioner and its symmetric square root by
\[
P=I+\left(\frac{m}{1+\widehat\lambda}-1\right)vv^{\mathsf T},\qquad B=P^{1/2}HP^{1/2}.
\]
The numerical event is strictly worse spectral conditioning than the unpreconditioned Hessian: \(\kappa_2(B)>\kappa_2(H)=L/m\). The informed Gaussian is an **exactly imposed model covariance**; its motivation is the approximate right-hand-side-difference covariance in Proposition 1 of the source. The theorem does not assert that practical ensemble differences have an exact Gaussian distribution.

## Proof

**Step 1: Exact one-vector Nyström and preconditioned spectrum.** For any vector with \(\omega_1\omega_2\ne0\), put \(z=(b\omega_2/(a\omega_1))^2>0\). Direct substitution gives
\[
\widehat\lambda=\frac{ab(1+z)}{b+az},\quad
c:=\frac{m}{1+\widehat\lambda}=\frac{m(b+az)}{bL+amz},\quad
R:=v^{\mathsf T}Hv=\frac{L+mz}{1+z}.
\]
Since \(a>b>0\), one has \(m/L<c<1\). The projection \(vv^{\mathsf T}\) is rank one, hence the trace and determinant of \(B\) are exactly
\[
\operatorname{tr} B=L+m+(c-1)R,\qquad \det B=cLm.
\]
These identities remain valid for both Gaussian covariance models; no stochastic approximation is involved.

**Step 2: Reduction to one cubic and uniqueness.** For every positive definite two-by-two matrix with ordered eigenvalues \(\eta_1\ge\eta_2>0\),
\[
\frac{(\operatorname{tr} B)^2}{\det B}=\kappa_2(B)+2+\kappa_2(B)^{-1}.
\]
The right side is strictly increasing for condition numbers greater than one. Consequently, \(\kappa_2(B)>L/m\) if and only if
\[
[\operatorname{tr} B]^2>c(L+m)^2.
\]
Setting \(r=R/(L+m)\), the difference of the two sides equals
\[
(1-c)(L+m)^2\bigl[1-2r+(1-c)r^2\bigr].
\]
Algebraic elimination of \(c\) and \(r\) yields the **exact sign identity**
\[
1-2r+(1-c)r^2
=-\frac{(a-b)Q_{a,b}(z)}{(1+z)^2(L+m)^2(bL+amz)}.
\]
All factors outside \(-Q_{a,b}(z)\) are positive. The leading coefficient of \(Q\) is negative, the quadratic coefficient negative, and the linear and constant coefficients positive; Descartes' sign rule therefore permits at most one positive zero. Moreover \(Q(0)=bLm>0\) and \(Q(1)=-b(L+m)^2<0\). The intermediate value theorem supplies one root in \((0,1)\). Uniqueness and the leading sign establish the claimed if-and-only-if and boundary.

**Step 3: Exact Gaussian probabilities.** Let \(Z_1,Z_2\) be independent standard normals. For isotropic sketches,
\[
z=\left(\frac ba\right)^2\left(\frac{Z_2}{Z_1}\right)^2.
\]
For informed sketches, the two coordinate variances are \(aL\) and \(bm\), so
\[
z=\frac{b^3m}{a^3L}\left(\frac{Z_2}{Z_1}\right)^2.
\]
The absolute ratio \(|Z_2/Z_1|\) has tail \(\Pr(|Z_2/Z_1|>t)=2\arctan(1/t)/\pi\) for \(t>0\). Applying it with \(z>\zeta_{a,b}\) proves both probability formulas. Since \(bm<aL\), the informed ratio coefficient is strictly smaller, establishing \(0<p_{\rm informed}<p_{\rm iso}<1\).

**Step 4: The high-contrast asymptotic.** Holding \(b>0\) fixed while \(a\to\infty\), division of the defining cubic by \(a^2\) yields uniform coefficient convergence on \([0,1]\):
\[
a^{-2}Q_{a,b}(z)\longrightarrow z\bigl[m-bz-mz^2\bigr].
\]
The right side is positive for fixed \(z\in(0,z_\infty(b))\), negative for fixed \(z\in(z_\infty(b),1]\). Because the finite cubic has only one positive zero, its root converges to the displayed positive root \(z_\infty(b)\). Both arctangent arguments in Step 3 tend to zero. Using \(\arctan t\sim t\) and \(L\sim a\) gives the asserted positive first-order constants and exponents.

## Verification

Run `python verify.py` with NumPy and SciPy installed. The program constructs the rank-one Nyström eigenvalue and the split SPD preconditioned matrix directly, compares its two eigenvalues against the polynomial crossing over seven parameter pairs and 110 deterministic angular ratios per pair, checks the two Cauchy-tail probabilities against seeded Gaussian samples, and checks the fixed-\(b\) asymptotic constants. Its execution prints `PASS 793 independent algebra/matrix/probability/asymptotic checks`; this is finite consistency evidence, not a substitute for Steps 1–4. For \(a=9,b=1\), the unique root is approximately \(0.7253181280679402\), and the two deterioration probabilities are approximately \(0.08258996546836081\) and \(0.012379763352523217\).

## Relationship to prior work

Daužickaitė, Gürol, Destouches, Berre, and Weaver (2026), arXiv:2605.23571, introduce the EDA-informed sketch and its approximate covariance \(A+A^2\), scaled spectral LMP, and Nyström construction. Those ingredients, and the possibility of unfavorable preconditioning in practice, are not claimed as new. The present result supplies a sharp exact **two-dimensional Gaussian law for condition-number deterioration**, including the Nyström rather than Rayleigh eigenvalue correction, its unique polynomial boundary, and a power-law difference between isotropic and covariance-informed sampling. In contrast, Giraud and Gratton (2004/2006) analyze perturbation sensitivity of spectral corrections without this stochastic two-mode law; Carson and Daužickaitė (2024) provide finite-precision Nyström error and condition-number bounds for a related but differently scaled preconditioner; Frangella, Tropp, and Udell (2023) analyze a regularized Nyström-PCG scheme using different scaling and probabilistic guarantees. The original 2026 EDA paper was inspected in full mathematical HTML form (sections 3.1–3.2.3, Algorithm 3.1, 4.2.1, appendices).

A closely related, earlier public mathematical claim analyzes **Rayleigh** spectral inverse correction for a top-mode-plus-identity model. Its Rayleigh quotient and spectral baseline differ from the harmonic Nyström estimate and two-positive-eigenvalue Hessian treated here; it does not imply the exact informed-versus-isotropic exponents. This mathematical overlap is acknowledged rather than claiming novelty for the mere existence of misalignment risk.

## Limitations

The theorem is only about a rank-one sketch of a two-by-two positive definite matrix with \(a>b>0\), a fixed oracle scale \(\theta=1+b\), and exactly Gaussian isotropic or exactly Gaussian \(A+A^2\) sketches. The result does not establish a general-purpose scale selector, iteration-count improvement of conjugate gradients, full operational EDA behavior, higher-rank sketch laws, non-Gaussian robustness, or finite-precision behavior. Generic angular sensitivity was previously known, and no novelty is claimed for it. Older specialized spectral-preconditioning work may contain stronger comparisons; independent historical-priority verification remains outstanding.

## References

1. I. Daužickaitė, S. Gürol, M. Destouches, L. Berre, A. T. Weaver, *Accelerating an ensemble of variational data assimilations with randomized preconditioning*, arXiv:2605.23571, first version 2026-05-22. https://arxiv.org/html/2605.23571v2
2. E. Carson and I. Daužickaitė, *Single-Pass Nyström Approximation in Mixed Precision*, SIAM J. Matrix Anal. Appl. 45 (2024), 1361–1391, arXiv:2205.13355. https://doi.org/10.1137/22M154079X
3. L. Giraud and S. Gratton, *On the Sensitivity of Some Spectral Preconditioners*, CERFACS technical report TR/PA/04/108 (2004), SIAM J. Matrix Anal. Appl. 27 (2006), 1089–1105. https://doi.org/10.1137/040617546
4. Z. Frangella, J. A. Tropp, M. Udell, *Randomized Nyström Preconditioning*, SIAM J. Matrix Anal. Appl. 44 (2023), 718–752, arXiv:2110.02820.
5. I. Daužickaitė et al., *Randomised preconditioning for the forcing formulation of weak constraint 4D-Var*, arXiv:2101.07249.
6. Y. Diouane et al., *A Spectral Preconditioner for the Conjugate Gradient Method with Iteration Budget*, arXiv:2603.28969.
