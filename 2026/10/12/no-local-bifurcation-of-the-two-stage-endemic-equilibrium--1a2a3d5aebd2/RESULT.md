# No local bifurcation of the two-stage endemic equilibrium
## Finding
For the two-stage \(n=2\) SIRS system introduced by Somnic, Gasparyan, and Rao, every positive endemic equilibrium is locally asymptotically stable throughout the entire positive parameter region in which it exists. Thus, when \(\mathcal R_0>1\), no extra lower bound on the immunity-loss rate \(\alpha\) is required for local stability, even though the source's global Lyapunov theorem imposes an additional sufficient inequality involving \(\alpha\).

More precisely, assume \(\lambda,\mu,\beta,\alpha,\delta_1,\delta_2,\gamma_1,\theta_1,\theta_2>0\). Whenever the unique endemic equilibrium \(E^*\) exists, all four eigenvalues of its Jacobian have strictly negative real part. Hence \(E^*\) cannot lose stability through a Hopf crossing or a zero eigenvalue at any interior positive parameter value.

## Assumptions and scope
The source model for \(n=2\) is
\[
\begin{aligned}
\dot S&=\lambda+\alpha R-\mu S-\beta S I_1,\\
\dot I_1&=\beta S I_1-(\mu+\delta_1+\gamma_1+\theta_1)I_1,\\
\dot I_2&=\gamma_1 I_1-(\mu+\delta_2+\theta_2)I_2,\\
\dot R&=\theta_1 I_1+\theta_2 I_2-(\alpha+\mu)R.
\end{aligned}
\]
All listed parameters are strictly positive, as in the source. The source proves existence and uniqueness of a positive endemic equilibrium exactly when \(\mathcal R_0>1\). The present result concerns local asymptotic stability of that equilibrium only. It does not claim global asymptotic stability outside the source's sufficient Lyapunov region, nor does it address models with more than two infectious stages or transmission from later infectious stages.

## Proof
Set
\[
x_1=\mu+\delta_1+\gamma_1+\theta_1,\qquad
x_2=\mu+\delta_2+\theta_2,\qquad
a=\alpha+\mu.
\]
At a positive endemic equilibrium, the \(I_1\)-balance gives \(\beta S^*=x_1\). Define \(q=\beta I_1^*>0\). In the coordinate order \((S,I_1,I_2,R)\), the Jacobian is
\[
J^*=\begin{pmatrix}
-(\mu+q)&-x_1&0&\alpha\\
q&0&0&0\\
0&\gamma_1&-x_2&0\\
0&\theta_1&\theta_2&-a
\end{pmatrix}.
\]
Direct determinant expansion gives
\[
\begin{aligned}
p(z)=&\det(zI-J^*)\\
=&z(z+a)(z+x_2)(z+\mu+q)
+x_1q(z+a)(z+x_2)\\
&-\alpha q\bigl[\theta_1(z+x_2)+\theta_2\gamma_1\bigr]\\
=&z^4+A_1z^3+A_2z^2+A_3z+A_4.
\end{aligned}
\]
The coefficients are
\[
\begin{aligned}
A_1&=a+x_2+\mu+q,\\
A_2&=ax_2+a(\mu+q)+x_2(\mu+q)+x_1q,\\
A_3&=ax_2(\mu+q)+x_1q(a+x_2)-\alpha q\theta_1,\\
A_4&=q\left[x_1ax_2-\alpha(\theta_1x_2+\theta_2\gamma_1)\right].
\end{aligned}
\]
Each is strictly positive. For example,
\[
x_1ax_2-\alpha(\theta_1x_2+\theta_2\gamma_1)
=\mu x_1x_2+\alpha\left[(\mu+\delta_1)x_2+\gamma_1(\mu+\delta_2)\right]>0,
\]
which proves \(A_4>0\); the other three follow immediately after the same substitutions.

For a monic quartic with positive coefficients, the remaining Routh--Hurwitz conditions are
\[
\Delta_2=A_1A_2-A_3>0,
\qquad
\Delta_3=A_1A_2A_3-A_3^2-A_1^2A_4>0.
\]
Exact expansion in the primitive positive variables \(\mu,\delta_1,\gamma_1,\theta_1,\delta_2,\theta_2,\alpha,q\) gives \(\Delta_2\) as a sum of 36 distinct monomials with positive integer coefficients and \(\Delta_3\) as a sum of 331 distinct monomials with positive integer coefficients. The bundled verifier derives \(\det(zI-J^*)\) independently by the 24-term determinant formula, checks it against the displayed characteristic polynomial, forms \(A_1,\ldots,A_4,\Delta_2,\Delta_3\) by exact multivariate integer-polynomial arithmetic, and verifies that every expanded coefficient is positive. Therefore all quartic Routh--Hurwitz determinants are strictly positive, so every root of \(p\) has negative real part.

## Verification
Run `python verify.py` with a standard Python 3 interpreter. The program uses only integer arithmetic and the standard library. It reconstructs the characteristic determinant from the Jacobian, verifies the closed characteristic-polynomial identity, and checks coefficient positivity after exact expansion. Its expected terminal line begins with `VERIFY_OK`; in the reviewed package it reports 36 monomials for \(\Delta_2\) and 331 for \(\Delta_3\), with minimum coefficient 1 in both expansions.

The proof is symbolic rather than numerical: there is no sampling of the positive parameter region. The only external mathematical input is the classical quartic Routh--Hurwitz criterion.

## Relationship to prior work
Somnic, Gasparyan, and Rao analyze exactly this SIRS model with recovery and disease-induced death allowed at every infectious stage. For \(n=2\), they derive sufficient conditions for global asymptotic stability using a constructed Lyapunov function; their discussion emphasizes that simulations can remain stable even when those sufficient conditions fail. The present result resolves the local question for the two-stage endemic equilibrium on the entire positive parameter region: failure of the published global Lyapunov condition cannot by itself create a local equilibrium instability.

Röst and Tekeli prove that endemic equilibria are always stable for up to three stages in a multistage SIS progression model. Their model has a constant total population, direct progression through infectious stages, and return to susceptibility; it does not include the separate recovered compartment with immunity loss together with stage-specific recovery and disease-induced death used here. The 2026 source explicitly identifies those additional recovery and death pathways as the feature not covered by that earlier stability result. Guo, Li, and Shuai prove global threshold dynamics for a broad class of staged-progression infection models, but the inspected statement does not supply this four-dimensional SIRS-with-waning-immunity Hurwitz calculation or imply the present claim under the 2026 model's added recovered-compartment feedback without an applicability argument.

## Limitations
This theorem is local. It does not prove that every positive trajectory converges to \(E^*\), does not remove the source's sufficient conditions for global asymptotic stability, and does not exclude nonlocal invariant sets coexisting with a locally stable endemic equilibrium. It also does not extend to \(n\ge3\) or to variants in which later infectious stages contribute directly to transmission. The originality comparison is strongest against the motivating 2026 paper and the closely related Röst--Tekeli stage-progression result; as with any literature search, an unindexed equivalent theorem remains a residual risk.

## References
1. J. Somnic, M. Gasparyan, and S. Rao, “Stability analysis of a multistage compartmental model of infection,” *Journal of Biological Dynamics* 20 (2026), article 2728357. DOI: 10.1080/17513758.2026.2728357. First public online date: 2026-09-16.
2. G. Röst and T. Tekeli, “Stability and oscillations of multistage SIS models depend on the number of stages,” *Applied Mathematics and Computation* 380 (2020), 125259. DOI: 10.1016/j.amc.2020.125259.
3. H. Guo, M. Y. Li, and Z. Shuai, “Global Dynamics of a General Class of Multistage Models for Infectious Diseases,” *SIAM Journal on Applied Mathematics* 72 (2012), 261–279. DOI: 10.1137/110827028.
