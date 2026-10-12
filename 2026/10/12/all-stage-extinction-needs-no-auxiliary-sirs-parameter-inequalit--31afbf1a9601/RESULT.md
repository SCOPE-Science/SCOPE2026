# All-stage extinction needs no auxiliary SIRS parameter inequalities
## Finding
Consider the multistage SIRS system
\[
\begin{aligned}
S'&=\lambda+\alpha R-\mu S-\beta S I_1,\\
I_1'&=\beta S I_1-(\mu+\delta_1+\gamma_1+\theta_1)I_1,\\
I_j'&=\gamma_{j-1}I_{j-1}-(\mu+\delta_j+\gamma_j+\theta_j)I_j,\qquad 2\le j\le n,\\
R'&=\sum_{j=1}^n\theta_j I_j-(\alpha+\mu)R,
\end{aligned}
\]
with \(\gamma_n=0\). For every integer \(n\ge1\), all positive model parameters, and every nonnegative initial condition, define
\[
S^0=\frac{\lambda}{\mu},\qquad
a_1=\mu+\delta_1+\gamma_1+\theta_1,\qquad
\mathcal R_0=\frac{\beta S^0}{a_1}.
\]
If \(\mathcal R_0\le1\), every solution converges to the disease-free equilibrium \((S^0,0,\ldots,0)\). No lower bound on \(\alpha\), no Condition A, and no restriction to initial total population below \(S^0\) is needed. For \(\mathcal R_0<1\) the disease-free equilibrium is globally asymptotically stable, while for \(\mathcal R_0>1\) it is unstable. At \(\mathcal R_0=1\), this result asserts global convergence but does not separately assert Lyapunov stability.

## Assumptions and scope
All state variables are nonnegative. The parameters \(\lambda,\mu,\beta,\alpha,\delta_j,\theta_j\) are positive; \(\gamma_j>0\) for \(j<n\) and \(\gamma_n=0\), matching the model convention in the source. Only the first infectious stage generates new infections. The result concerns the disease-free equilibrium; it does not address global stability of the endemic equilibrium.

The motivating article proves global disease-free stability for two stages under an additional lower bound on \(\alpha\), and for three stages under Condition A. It also observes that on the restricted region where total population is at most \(S^0\), \(I_1\) itself gives a simpler extinction argument. The result here removes both the auxiliary parameter conditions and that initial-population restriction, and it applies to arbitrary \(n\).

## Proof
Let
\[
N=S+R+\sum_{j=1}^n I_j,\qquad z=N-S^0,\qquad
D=\sum_{j=1}^n\delta_j I_j.
\]
Summing the equations gives the exact identity
\[
N'=\lambda-\mu N-D,
\]
hence
\[
z'=-\mu z-D.
\]
With \(c=(N(0)-S^0)_+\), variation of constants and \(D\ge0\) yield
\[
z(t)\le c e^{-\mu t}.
\]
Because \(S\le N\),
\[
S(t)-S^0\le c e^{-\mu t}.
\]

For the first infectious stage,
\[
I_1'=\left[a_1(\mathcal R_0-1)+\beta(S-S^0)\right]I_1.
\]
If \(\mathcal R_0<1\), then
\[
I_1(t)\le I_1(0)
\exp\!\left(
-a_1(1-\mathcal R_0)t+
\frac{\beta c}{\mu}(1-e^{-\mu t})
\right),
\]
so \(I_1(t)\to0\) exponentially.

Now take the borderline \(\mathcal R_0=1\). Define
\[
Q(t)=I_1(t)
\exp\!\left[-\frac{\beta c}{\mu}(1-e^{-\mu t})\right].
\]
The preceding bound gives \(Q'(t)\le0\). Thus \(Q(t)\) has a finite limit, and because the exponential factor also has a finite positive limit, \(I_1(t)\) has a finite limit \(L\ge0\). If \(L>0\), then eventually \(I_1(t)\ge L/2\), so
\[
D(t)\ge \delta_1 L/2.
\]
The scalar equation for \(z\) then implies that, for all sufficiently large \(t\),
\[
z(t)\le-\frac{\delta_1L}{4\mu}.
\]
Since \(S-S^0\le z\), the first-stage equation at \(\mathcal R_0=1\) gives
\[
I_1'\le-\frac{\beta\delta_1L}{4\mu}I_1
\]
eventually, contradicting \(I_1(t)\to L>0\). Hence \(L=0\).

For \(j\ge2\), each equation is a stable scalar linear equation forced by the preceding stage:
\[
I_j'=\gamma_{j-1}I_{j-1}-a_jI_j,
\qquad a_j=\mu+\delta_j+\gamma_j+\theta_j>0.
\]
Variation of constants therefore gives \(I_j(t)\to0\) successively. The recovered equation is likewise a stable linear equation forced by \(\sum_j\theta_jI_j\), so \(R(t)\to0\). Consequently \(D(t)\to0\), and the stable equation \(z'=-\mu z-D\) gives \(z(t)\to0\). Thus \(N(t)\to S^0\), and finally \(S(t)=N(t)-R(t)-\sum_jI_j(t)\to S^0\).

When \(\mathcal R_0<1\), the Jacobian at the disease-free equilibrium is triangular after ordering the infection cascade: its relevant diagonal entries are \(a_1(\mathcal R_0-1)<0\), \(-a_j<0\) for \(j\ge2\), \(-\mu\), and \(-(\alpha+\mu)\). Hence the equilibrium is locally asymptotically stable; together with global attraction, it is globally asymptotically stable.

If \(\mathcal R_0>1\), the first-stage linearization has eigenvalue \(a_1(\mathcal R_0-1)>0\), so the disease-free equilibrium is unstable.

## Verification
The exact total-population identity and the first-stage comparison are symbolic consequences of the displayed equations. The bundled checker reconstructs the cancellation in \(N'\), the reproduction-number factorization, and representative cascade identities for multiple values of \(n\). A direct numerical stress test at \(\mathcal R_0=1\) with five infectious stages and initial populations both far above and below \(S^0\) was also consistent with the proved convergence; that experiment is only a check and is not used as proof.

The proof of the borderline case depends essentially on \(\delta_1>0\), which is part of the source's positive-parameter assumptions. If disease-induced death in the first stage were allowed to vanish, the contradiction step would need a separate argument.

## Relationship to prior work
Somnic, Gasparyan, and Rao analyze exactly this SIRS architecture. Their two-stage global disease-free theorem assumes both \(\mathcal R_0\le1\) and a lower bound on \(\alpha\); their three-stage theorem assumes \(\mathcal R_0\le1\) and Condition A. They explicitly note that on the smaller region where total population is at most \(S^0\), the two-stage disease-free argument needs no extra condition on \(\alpha\), and their simulations remain stable outside the sufficient parameter region. The present argument closes the disease-free side for arbitrary initial total population and arbitrary stage count.

Shuai and van den Driessche give a general matrix-theoretic Lyapunov construction. For this model its nonlinear remainder in the newly infected component is \(\beta(S^0-S)I_1\), so their nonnegativity condition is automatic only when \(S\le S^0\); it does not by itself cover arbitrary initial states with \(S>S^0\). The exponentially decaying upper envelope for \(N-S^0\) is the extra ingredient used here.

Guo, Li, and Shuai prove an all-stage threshold theorem for a broad progression model, but their removed class is permanently outside the infection process; it does not return to susceptibility. Röst and Tekeli prove extinction for a multistage SIS progression chain with constant total population and return from the last infectious stage directly to susceptibility. Their model has neither the recovered compartment with waning immunity nor recovery and disease-induced death from every infectious stage. A delayed multi-group SIRS theorem of Muroya, Kuniya, and Enatsu is also broader in another direction, but it is a group-mixing model rather than this sequential stage-progression architecture.

## Limitations
No claim is made about global stability of the endemic equilibrium, which can have genuinely different behavior in multistage models. At the critical value \(\mathcal R_0=1\), global convergence is proved, but Lyapunov stability of the disease-free equilibrium is not claimed here. The proof uses the source assumption \(\delta_1>0\). The novelty assessment is based on the inspected source, the general multistage and general disease-model theorems described above, the multistage SIS comparator, the multi-group SIRS comparator, and semantic searches; an unlocated theorem specialized to this exact SIRS stage architecture remains a residual literature risk.

## References
1. J. Somnic, M. Gasparyan, S. Rao, “Stability analysis of a multistage compartmental model of infection,” Journal of Biological Dynamics 20 (2026), article 2728357. DOI: 10.1080/17513758.2026.2728357.
2. Z. Shuai, P. van den Driessche, “Global Stability of Infectious Disease Models Using Lyapunov Functions,” SIAM Journal on Applied Mathematics 73 (2013), 1513–1532. DOI: 10.1137/120876642.
3. H. Guo, M. Y. Li, Z. Shuai, “Global Dynamics of a General Class of Multistage Models for Infectious Diseases,” SIAM Journal on Applied Mathematics 72 (2012), 261–279. DOI: 10.1137/110827028.
4. G. Röst, T. Tekeli, “Stability and oscillations of multistage SIS models depend on the number of stages,” Applied Mathematics and Computation 380 (2020), 125259. DOI: 10.1016/j.amc.2020.125259.
5. Y. Muroya, T. Kuniya, Y. Enatsu, “Global stability of a delayed multi-group SIRS epidemic model with nonlinear incidence rates and relapse of infection,” Discrete and Continuous Dynamical Systems B 20 (2015), 3057–3091. DOI: 10.3934/dcdsb.2015.20.3057.
