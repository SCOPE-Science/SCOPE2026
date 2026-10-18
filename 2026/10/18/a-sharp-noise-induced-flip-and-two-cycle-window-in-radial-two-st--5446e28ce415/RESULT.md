# A sharp noise-induced flip and two-cycle window in radial two-stepsize SQP

## Finding
For a unit-circle constrained two-stepsize stochastic SQP iteration with constant outer step \(\alpha=3\), the conditional-unbiased tangent noise of fixed magnitude has a deterministic squared-radius iteration. It exhibits an exact transition from a repelling fixed radius and attracting two-cycle to an attracting fixed radius. The transition is controlled solely by the squared tangent step \(\eta\):
\[
\eta_- = \frac{3(5-\sqrt{13})}{10},\qquad \eta_c=\frac32\left(1-\frac1{\sqrt5}\right).
\]
For \(\eta_-<\eta<\eta_c\), the unique positive distinct two-cycle is locally attracting; for \(\eta>\eta_c\), the unique positive fixed point is locally attracting. Both thresholds are sharp for the stated local stability claims. At \(\eta=3/5\), the two-cycle has squared radii \(3/5\) and \(3\), and zero two-step radial multiplier.

## Assumptions and scope
Work in \(\mathbb R^2\setminus\{0\}\), let \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\), and consider the constraint \(c(z)=(\|z\|^2-1)/2=0\) and constant expected objective \(f=0\). Use the generic normal/tangential SQP decomposition of O'Neill (2024), with Hessian model \(H=I\), outer step \(\alpha=3\), tangential multiplier \(\beta>0\), and unbiased oracle \(g_k=\varepsilon_k\sigma Jz_k/\|z_k\|\), where \(\sigma>0\) and the signs are iid equiprobable. The oracle has conditional mean zero and constant conditional squared norm \(\sigma^2\). It is an unbiased gradient estimator as required by the generic oracle assumption; individual oracle realizations are not asserted to be gradients of globally single-valued random potentials. The global regularity hypotheses of the motivating complexity theorem, and its sufficient outer-stepsize restrictions, are **not** asserted for this circle example. All assertions concern the formal, well-defined generic update.

## Proof
Set \(s=\|z\|^2>0\). Because \(\nabla c(z)=z\), the SQP subproblem \(\min_p g^\mathsf Tp+\|p\|^2/2\) subject to \(c(z)+z^\mathsf Tp=0\) gives the orthogonal parts \(v=-c(z)z/s\) and \(u=-g\), since \(g\perp z\). Thus
\[
z^+=z+3(v+\beta u)=\frac{3-s}{2s}z-3\beta\varepsilon\sigma\frac{Jz}{\sqrt{s}}.
\]
Orthogonality of \(z\) and \(Jz\) gives the **samplewise** exact squared-radius map
\[
F_\eta(s)=\frac{(s-3)^2}{4s}+\eta,\qquad\eta=9\beta^2\sigma^2>0.
\]
It maps every positive \(s\) into \([\eta,\infty)\), so no iterate reaches the singular origin.

The fixed-point equation is \(3s^2+(6-4\eta)s-9=0\), with exactly one positive root
\[
s_*(\eta)=\frac{2\eta-3+\sqrt{(3-2\eta)^2+27}}{3}.
\]
This root grows strictly with \(\eta\). Since \(F_\eta'(s)=1/4-9/(4s^2)<1\), its multiplier has modulus less than one exactly when \(s_*>3/\sqrt5\), equivalent to \(\eta>\eta_c=3(1-1/\sqrt5)/2\). Below the threshold it is repelling; at the threshold the multiplier equals \(-1\) and linear stability is neutral.

For distinct period-two radii \(r,t>0\), subtracting \(F_\eta(r)=t\) and \(F_\eta(t)=r\) shows \(rt=9/5\). Adding the two equations gives \(r+t=6-4\eta\). Consequently, distinct positive period-two radii exist **precisely** when \(0<\eta<\eta_c\), and are
\[
s_\pm=3-2\eta\pm\sqrt{(3-2\eta)^2-9/5}.
\]
They genuinely exchange under \(F_\eta\), as substitution or the factored numerator of \(F_\eta^2(s)-s\) verifies. Their two-step multiplier is
\[
\mu_2=F_\eta'(s_-)F_\eta'(s_+)=\frac94-\frac{25}{9}\left(\frac32-\eta\right)^2.
\]
It rises strictly from \(-4\) to \(1\) on the two-cycle existence interval. Thus \(|\mu_2|<1\) exactly when \(\eta_-<\eta<\eta_c\), where \(\eta_-=3(5-\sqrt{13})/10\). At \(\eta=3/5\) the two radii are \(3/5,3\), and \(F_\eta'(3)=0\), giving a superattracting cycle. Its constraint values, \(-1/5\) and \(1\), are nonzero.

## Verification
Run `python sqp_circle_checker.py` with SymPy installed. The checker reconstructs the exact radial recurrence from the planar update for both signs of the noise, verifies the fixed-point polynomial, period-two roots and multipliers symbolically, and verifies the rational superattracting cycle. Its successful execution is a finite algebraic verification; the universal parameter assertions follow from the displayed deductions and exact inequalities, not sampling.

## Relationship to prior work
O'Neill (arXiv:2408.16656, first submitted 2024-08-29) defines the two-stepsize SQP normal/tangential update and establishes worst-case complexity under diminishing/noise-controlled steps and global assumptions. The present example applies the **generic update**, not the convergence theorem, to investigate fixed-parameter radial dynamics. The existence of flip bifurcations and rational-map periodic points is classical; neither phenomenon in the abstract is claimed as novel. The contribution assessed here is the samplewise SQP radial reduction with conditional-unbiased tangential noise, its exact two stability thresholds, and its superattracting numerical feasibility two-cycle. No covering assertion was located in the inspected motivating text or targeted literature searches, but alternative treatments of rational maps or constrained stochastic SQP may exist.

## Limitations
This is a model-specific local stability classification, not a theorem of global convergence to the fixed point or two-cycle, nor an assertion about angular convergence. The circle constraint has a singular Jacobian at the origin and cannot satisfy the motivating paper's global uniform-Jacobian assumptions; the positive noise level nevertheless keeps each positive-radius trajectory away from the origin. The model has a positive, deliberately large outer stepsize, outside the source's sufficient convergence conditions. The stochastic oracle is unbiased and bounded-variance but not claimed to be a gradient of individual global sample objectives. The two multipliers equal \(-1\) at the respective boundary values; no nonlinear attraction assertion is made there. The abstract rational dynamics may be described in other terminology.

## References
1. Michael J. O'Neill, *A Two Stepsize SQP Method for Nonlinear Equality Constrained Stochastic Optimization*, arXiv:2408.16656 (first version 2024-08-29), especially the SQP system (5), normal/tangential decomposition (9)–(10), Algorithm 1 and stochastic oracle Assumption 3.
2. Albert S. Berahas, Frank E. Curtis, Daniel P. Robinson, and Baoyu Zhou, *Sequential Quadratic Optimization for Nonlinear Equality Constrained Stochastic Optimization*, SIAM Journal on Optimization, DOI 10.1137/20M1354556.
3. Classical local theory of flip bifurcations of one-dimensional maps (background only); compare standard derivations of the second iterate and its multiplier.
