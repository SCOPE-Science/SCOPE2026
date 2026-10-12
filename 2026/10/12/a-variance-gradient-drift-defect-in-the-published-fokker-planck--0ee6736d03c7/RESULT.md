# A variance-gradient drift defect in the published Fokker–Planck epidemic control formulation
## Finding
The epidemic-control model of Parkinson and Roy has a well-defined Itô forward equation, Equation (6), but the paper's claimed divergence-form equation, Equation (8), uses the full gradient of diffusion variance where the half-gradient is required. Moreover, its purported weak formulation, Equation (9), inserts a further factor of one half in the first-order term. Neither transformation is an identity in the generality stated in the article.

For the exact diffusion coefficients used in its experiments, the first discrepancy has an epidemiological interpretation: if Equation (8) is solved as a conservative Fokker–Planck equation in its own right, its implied susceptible and infected drift rates are both shifted downward, changing the stochastic epidemic model whose distribution is being controlled.

## Assumptions and scope
Let \(\Omega\subset\mathbb R^2\) be open, let \(u\) be a fixed control (or a spatially independent bounded measurable time-dependent control at almost every time), let \(F_j\) be continuously differentiable in the state, and let the diagonal Itô diffusion variances \(D_j=\sigma_j^2\) be twice continuously differentiable in the state. Work with smooth densities \(f\) and compactly supported smooth tests in the interior of \(\Omega\); this removes boundary ambiguities from the operator comparison.

Define the forward residuals \(L_6f\) and \(L_8f\) by moving all terms in the printed Equations (6) and (8), respectively, to the left. For statements about the paper's numerical diffusion, use its published \(\sigma_S=-\sigma_I=\sqrt{0.02}(1-\alpha)SI\) with independent Wiener coordinates. The sign of these diagonal noise amplitudes is immaterial for the variances. The claim is local to the PDE identities, and is not a reconstruction of unpublished solver code.

## Proof
Write \(\partial_j\) for differentiation in the \(j\)-th state coordinate. Equation (6) is
\[
\partial_t f+\sum_j\partial_j(F_jf)
=\frac12\sum_j\partial_j^2(D_jf).
\]
Use the identity
\[
\partial_j^2(D_jf)=\partial_j(D_j\partial_j f)+\partial_j((\partial_jD_j)f).
\]
Moving the second term to the left yields exactly
\[
\partial_t f+\sum_j\partial_j\left(\left[F_j-\frac12\partial_jD_j\right]f\right)
=\frac12\sum_j\partial_j(D_j\partial_j f).
\]
Thus the correct nondivergence coefficients on the left of this divergence-diffusion representation are
\[
b_j^{\mathrm{corr}}=F_j-\frac12\partial_jD_j,
\qquad
c^{\mathrm{corr}}=\sum_j\partial_j b_j^{\mathrm{corr}}
=\sum_j\left(\partial_j F_j-\frac12\partial_j^2D_j\right).
\]
The source instead prints
\[
b_j^{\mathrm{pub}}=F_j-\partial_jD_j,
\qquad
c^{\mathrm{pub}}=\sum_j\partial_jb_j^{\mathrm{pub}}.
\]
Subtracting the left-hand residuals gives the *exact operator difference*
\[
L_8f-L_6f=-\frac12\sum_j\partial_j\big((\partial_jD_j)f\big).
\]
In particular, the source's Equation (8) represents the same diffusion \(D\) but the different Itô drift
\[
\widetilde F_j=F_j-\frac12\partial_jD_j.
\]
This last assertion follows by expanding the forward operator of the modified drift and comparing it term by term with Equation (8). The source's no-flux condition (7) is tied to Equation (6); the associated natural no-flux condition for Equation (8) also changes by the same drift correction.

The simulation coefficients in Section 5 satisfy
\[
D_S=D_I=\frac1{50}(1-\alpha)^2S^2I^2.
\]
Therefore
\[
\frac12\partial_S D_S=\frac1{50}(1-\alpha)^2SI^2,
\qquad
\frac12\partial_I D_I=\frac1{50}(1-\alpha)^2S^2I.
\]
The modified drift is consequently
\[
\widetilde F_S=F_S-\frac1{50}(1-\alpha)^2SI^2,
\qquad
\widetilde F_I=F_I-\frac1{50}(1-\alpha)^2S^2I.
\]
For every \(S,I>0\) and \(0\le\alpha<1\), these are nonzero negative shifts. In particular, the infinitesimal generator applied to the coordinate sum \(S+I\) differs by
\[
(\widetilde L-L)(S+I)=-\frac1{50}(1-\alpha)^2SI(S+I).
\]
The difference is not restricted to a formal class of coefficients absent from the experiments.

For Equation (9), test Equation (8) against any \(\varphi\in C_c^\infty(\Omega)\) and integrate by parts only on the right-hand diffusive divergence. The result is
\[
\int_\Omega\left[f_t\varphi+
\sum_jb_j^{\mathrm{pub}}(\partial_jf)\varphi
+c^{\mathrm{pub}}f\varphi+
\frac12\sum_jD_j(\partial_jf)(\partial_j\varphi)\right]dx=0.
\]
The printed Equation (9) has \(\tfrac12\sum_jb_j^{\mathrm{pub}}\partial_jf\,\varphi\) instead. Thus it disagrees with Equation (8) whenever the missing half-advection contribution is nonzero.

For an elementary *independent* witness, take constant variances \(D_S=D_I=1\), constant drift \(F=(2,0)\), and \(f(S,I,t)=1+S-2t\) in any interior rectangle where \(f>0\). This solves Equation (6) pointwise and also Equation (8), because \(f_t=-2\), \(F\cdot\nabla f=2\), and \(\Delta f=0\). Equation (9), however, has integrand
\[
-2\varphi+\frac12(2)(1)\varphi+\frac12\partial_S\varphi=-\varphi+\frac12\partial_S\varphi.
\]
The compact support of \(\varphi\) makes the derivative integrate to zero, leaving \(-\int_\Omega\varphi\ne0\) whenever \(\varphi\ge0\) is not identically zero. Hence even spatially constant diffusion does not make the printed weak definition equivalent to its stated PDE.

Finally, integrating Equation (6) directly against \(\varphi\in C_c^\infty(\Omega)\) gives the corrected conservative weak identity
\[
\int_\Omega\left[f_t\varphi-Ff\cdot\nabla\varphi+
\frac12\sum_j\partial_j(D_jf)\partial_j\varphi\right]dx=0.
\]
The boundary terms disappear by the choice of test space.

## Verification
The bundled `verification/verify.py` reconstructs Equations (6) and (8) as exact symbolic differential operators for the paper's Section 5 incidence-dependent diffusion and the paper's controlled SIR drift. It verifies that their difference equals the displayed half-variance-gradient divergence and that the associated modified drift is exact. A separate symbolic test reproduces the nonzero Equation (9) residual in the constant-diffusion witness. The checker uses rational arithmetic for the coefficient \(0.02=1/50\); no numerical ODE or PDE simulation enters the proof.

## Relationship to prior work
Annunziato and Borzì (2018) establish the general Fokker–Planck control framework and its connection with Itô forward equations. Bonicatto, Ciampa, and Crippa (2025) analyze weak solutions of the general forward equation with spatially variable diffusion. Their work supplies the standard forward-operator context, not a source-specific diagnosis of the displayed formulas in Parkinson and Roy.

The motivating paper itself states Equation (6) correctly and gives the forward flux in Equation (7). It subsequently labels Equation (8) an equivalent divergence-form rewriting and calls Equation (9) a weak solution of Equation (6). These claims cannot simultaneously hold under the printed coefficients. The same mismatches occur in the accessible arXiv preprint and journal versions.

Other published findings concerning this source address the rank of transmission-noise covariance or the SQH minimizer calculation; they do not imply the strong/weak forward-operator discrepancy proved here.

## Limitations
The conclusion is an exact mathematical comparison of *printed* PDE formulations. It does not identify which PDE was actually discretized by the authors' Chang–Cooper implementation, nor does it claim that all of the paper's plots or control conclusions are invalid. Its Section 3 existence argument explicitly invokes the non-equivalent weak Equation (9), so the printed derivation alone does not establish the asserted equivalence of the weak and forward problems; the result does not rule out a separate valid existence proof for Equation (6).

The drift interpretation assumes Equation (8) is assigned its own natural conservative flux. If Equation (8) is instead paired with the different flux prescribed by Equation (7), its boundary formulation must also be reconciled. The counterexamples use interior compactly supported tests, so the mathematical inequivalence does not depend on a contested boundary condition.

## References
1. C. Parkinson and S. Roy, “A Fokker-Planck framework for control of epidemics,” Journal of Mathematical Biology **93** (2026), article 47, DOI: 10.1007/s00285-026-02462-7; first arXiv posting arXiv:2601.20181 (28 January 2026).
2. M. Annunziato and A. Borzì, “A Fokker–Planck control framework for stochastic systems,” EMS Surveys in Mathematical Sciences **5** (2018), 65–98, DOI: 10.4171/EMSS/27.
3. P. Bonicatto, G. Ciampa, and G. Crippa, “A regularity result for the Fokker–Planck equation with non-smooth drift and diffusion,” Nonlinear Analysis **254** (2025), 113748, DOI: 10.1016/j.na.2025.113748; arXiv:2310.12625.
