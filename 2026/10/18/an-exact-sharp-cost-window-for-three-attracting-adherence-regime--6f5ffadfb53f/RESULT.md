# An exact sharp cost window for three attracting adherence regimes

## Finding
Consider the deterministic susceptible–infected–recovered–susceptible (SIRS) epidemic coupled to voluntary nonpharmaceutical-intervention adherence, as defined below. For all admissible parameters, at most **three hyperbolic equilibrium sinks** can coexist: at most one at each of zero and full adherence, and at most one with strictly partial adherence. This bound is sharp.

More precisely, fix
\[
(\beta,\gamma,\mu,\delta,\xi,\kappa,\varepsilon,a,e)
=(2,4/5,1/5,4/5,9/10,2/5,1,1,0)
\]
and vary only the positive adherence cost \(c\). Exactly **three hyperbolic equilibrium sinks** occur if and only if
\[
\boxed{\frac1{10}<c<\frac{7-2\sqrt{10}}5.}
\]
They are (i) zero adherence with endemic infection, (ii) partial adherence with endemic infection, and (iii) full adherence with infection absent. Within this entire interval there are also two distinct strictly mixed endemic equilibria (the lower-adherence one unstable), and a disease-free interior-adherence saddle. At the rational choice \(c=3/25\), the two mixed endemic equilibria have exact adherence frequencies \(x_{\pm}=(4\pm\sqrt6)/20\). All three sinks persist under sufficiently small simultaneous changes of the parameters, including changes giving \(0<a,e<1\). This is a classification of **local equilibrium attractors**, not of all recurrent attractors or global basins.

## Assumptions and scope
The state space is \(S\geq0\), \(I\geq0\), \(S+I\leq1\), and \(0\leq x\leq1\). Let \(R=1-S-I\). With baseline transmission \(\beta>0\), recovery \(\gamma>0\), demographic turnover \(\mu>0\), immunity loss \(\delta>0\), private protection \(a\in[0,1]\), source control \(e\in[0,1]\), perceived harm \(\xi>0\), intervention cost \(c>0\), conformity \(\kappa\geq0\), and learning speed \(\varepsilon>0\), define
\[
 b(x)=(1-ax)(1-ex),\qquad
 \alpha(x,I)=-c+a\xi\beta I(1-ex)+\kappa(2x-1).
\]
The system is
\[
\begin{aligned}
 \dot S&=\mu-\beta b(x)SI+\delta(1-S-I)-\mu S,\\
 \dot I&=\beta b(x)SI-(\gamma+\mu)I,\\
 \dot x&=\varepsilon x(1-x)\alpha(x,I).
\end{aligned}
\]
A *hyperbolic equilibrium sink* has every Jacobian eigenvalue in the open left half-plane. The universal ceiling ranges over all parameters just specified. The sharp cost interval pertains **only** to the fixed nine parameters displayed in the Finding, with \(c\) varying.

## Proof
**1. Universal sink ceiling.** For fixed adherence \(x\), put \(\rho=\beta/(\gamma+\mu)\) and \(K=(\delta+\mu)/(\delta+\mu+\gamma)\). A positive endemic equilibrium exists exactly when \(\rho b(x)>1\), in which case its susceptible and infected fractions are uniquely
\[
 S(x)=\frac1{\rho b(x)},\qquad I(x)=K\left(1-\frac1{\rho b(x)}\right).
\]
Otherwise the only feasible epidemiological equilibrium is the disease-free state \((S,I)=(1,0)\). Therefore there is at most one feasible epidemic equilibrium at each adherence boundary \(x=0\) or \(x=1\).

An equilibrium with \(I=0\) and \(0<x<1\) must have \(x=(c+\kappa)/(2\kappa)\), so it exists only when \(\kappa>c\). Its Jacobian has the strictly positive behavioral eigenvalue \(2\varepsilon\kappa x(1-x)\), since at \(I=0\) the infection coordinate decouples to first order from changes of \(x\). No disease-free partial-adherence equilibrium can be a sink.

For strictly mixed endemic equilibria, assume first \(a>0\). Substituting the fixed-adherence endemic equilibrium into the behavioral payoff yields the exact identity
\[
 G(x)=\alpha(x,I(x))=-c-\kappa+a\xi\beta K\left[(1-ex)-\frac1{\rho(1-ax)}\right]+2\kappa x.
\]
The endemic domain is a connected interval in \((0,1)\), because \(b\) is nonincreasing. There \(1-ax>0\) and
\[
 G''(x)=-\frac{2a^3\xi\beta K}{\rho(1-ax)^3}<0.
\]
Thus \(G\) has at most two distinct zeros. If there are two, the smaller has \(G'(x)>0\), and the larger has \(G'(x)<0\). At a strictly mixed endemic equilibrium, the Jacobian characteristic polynomial has constant term
\[
 C_3=-\varepsilon x(1-x)\beta b(x)I(x)(\mu+\delta+\gamma)G'(x).
\]
This identity, already available in the source model's local-stability analysis, implies that the smaller root has \(C_3<0\) and hence a positive real eigenvalue. A single root with \(G'(x)\geq0\) cannot be a hyperbolic sink either. Therefore there is at most one hyperbolic mixed-endemic sink. When \(a=0\), \(G(x)=-c+\kappa(2x-1)\) is affine and its possible interior zero has positive behavioral derivative, so the ceiling remains valid. Adding the two possible boundary sinks gives at most three.

**2. An exact one-parameter tristability chamber.** For the fixed parameter family, \(\rho=2\), \(K=5/9\), and \(b(x)=1-x\). Endemic infection is possible exactly for \(0\leq x<1/2\), with
\[
 S(x)=\frac1{2(1-x)},\quad I(x)=\frac59\left(1-\frac1{2(1-x)}\right).
\]
The reduced adherence incentive on this branch is
\[
 G_c(x)=\frac35-c+\frac45x-\frac1{2(1-x)}.
\]
It is strictly concave and reaches its unique maximum at \(x_m=1-\sqrt{5/8}\in(1/5,1/4)\), with
\[
 G_c(0)=\frac1{10}-c,\quad G_c(1/2)=-c,\quad
 G_c(x_m)=\frac{7-2\sqrt{10}}5-c.
\]
Consequently, exactly two simple mixed endemic roots occur in \((0,1/2)\) precisely for \(1/10<c<(7-2\sqrt{10})/5\). In that interval the smaller root is below \(x_m\), and the larger is in \((x_m,3/8)\), since at \(c=1/10\) the upper root equals \(3/8\).

The no-adherence endemic equilibrium is \((S,I,x)=(1/2,5/18,0)\). Its epidemiological Jacobian has characteristic polynomial \(\lambda^2+(14/9)\lambda+1\), while its transverse adherence eigenvalue is \(1/10-c\); it is a sink exactly for \(c>1/10\). Full adherence has equilibrium \((S,I,x)=(1,0,1)\); its eigenvalues are \(-1,-1,c-2/5\), so it is a sink for \(c<2/5\), including the entire claimed interval.

At each mixed endemic equilibrium with adherence coordinate \(z\), direct differentiation gives the characteristic polynomial \(\lambda^3+C_1\lambda^2+C_2\lambda+C_3\), where
\[
\begin{aligned}
 C_1&=\frac{14-10z}{9}-\frac45z(1-z),\\
 C_2&=1-2z-\frac{4z(1-z)(14-10z)}{45}+\frac{z(1-2z)}{2(1-z)},\\
 C_3&=z(1-2z)\left[\frac1{2(1-z)}-\frac45(1-z)\right].
\end{aligned}
\]
At the lower root \(G_c'(z)>0\), so \(C_3<0\) and the equilibrium is unstable. At the upper root \(z\in(x_m,3/8)\), one has \(C_3>0\). A rational Bernstein-basis certificate on the wider interval \([1/5,3/8]\) proves \(C_1>0\), \(C_2>0\), and \(C_1C_2-C_3>0\): the respective numerators \(45C_1\), \(90(1-z)C_2\), and \(4050(1-z)(C_1C_2-C_3)\) have **strictly positive Bernstein coefficients** on this interval. Their explicit polynomials and coefficients are reproduced by the accompanying `verify.py`. By the cubic Routh–Hurwitz criterion the upper mixed endemic equilibrium is a hyperbolic sink for the specified \(\varepsilon=1\).

Finally, the only disease-free partial-adherence equilibrium is \((S,I,x)=(1,0,1/2+5c/4)\), which lies in \(1/2<x<1\) throughout the cost window and has a positive adherence eigenvalue. Thus it is not another sink. Outside the displayed cost window either the no-adherence state is not a hyperbolic sink or there are not two simple endemic roots with a stable upper branch; in fact, for costs above the upper endpoint the endemic roots disappear entirely. There can therefore be no three hyperbolic sinks outside the interval for this fixed family.

At \(c=3/25\), multiplication of \(G_c(x)=0\) by the positive denominator yields \(40x^2-16x+1=0\), giving \(x_\pm=(4\pm\sqrt6)/20\) and
\[
 (S_\pm,I_\pm,x_\pm)=\left(\frac{16\pm\sqrt6}{25},\frac{9\mp\sqrt6}{45},\frac{4\pm\sqrt6}{20}\right).
\]
The hyperbolic sink at \(x_+\), the hyperbolic no-adherence sink, and the hyperbolic full-adherence disease-free sink persist under small parameter perturbations by the implicit-function theorem and continuity of eigenvalues. The full-adherence equilibrium remains infection-free for sufficiently small perturbations because its disease-invasion eigenvalue is strictly negative at the displayed parameters. Taking slightly \(a<1\) and \(e>0\) therefore gives models with both protective effects strictly positive and less than one.

## Verification
Run `python3 verify.py` in the extracted package directory. The standalone script uses only the Python standard library (`fractions` and `math`) to recompute the rational coefficients of the characteristic-polynomial inequalities, produce the exact Bernstein positivity certificate, confirm the exact quadratic-root and endpoint identities, and check strict rational enclosures of the two algebraic equilibria. It is a finite verification of the stated exact algebraic certificate; the universal result and the full continuum of costs are proved in the preceding analytic argument.

## Relationship to prior work
Kumata, Ito, and Yamamichi introduce the identical coupled SIRS–adherence model, derive the endemic prevalence curve and Jacobian criterion, and illustrate low/high adherence bistability and partial/high adherence coexistence. Their Figure S3 legend also explicitly lists the **possibility** of low/partial/high multistability; this qualitative possibility is not presented as a new discovery here. Earlier analysis has already established the at-most-two mixed-endemic root bound and a different exact example of abandonment–partial-adherence bistability; that bound is acknowledged rather than re-claimed. The present finding is the **sharp analytic one-parameter cost interval**, its proof of three simultaneous hyperbolic sinks at a fixed updating rate, the exact rational/algebraic witness, and the achieved universal three-sink ceiling. The original figure-based parameter classifications and previously established qualitative classes do not give these exact thresholds or this parameter-specific complete classification. Saad-Roy and Traulsen use a different adherence payoff and report no simultaneously stable endemic adherence states; Martin, Castella, and Hamelin analyze a different SIS imitation model and report only one stable endemic adherence regime at a time.

## Limitations
The theorem concerns deterministic local equilibria, not global convergence, stochastic extinction, empirical mask efficacy, or total attractor counts when cycles occur. In the exact family, perfect private protection \(a=1\) and zero source control \(e=0\) simplify the algebra, but persistence shows a nearby open set with both effects strictly interior. The quantitative cost interval is not asserted for arbitrary parameters. This is an analytical extension of a previously defined system, not a new disease transmission mechanism. The motivating paper already identifies multistability qualitatively in its figures; equivalent parameter-specific formulas in unindexed literature remain an originality risk.

## References
1. R. Kumata, H. Ito, and M. Yamamichi, *Voluntary nonpharmaceutical intervention as a feedback-evolving game*, arXiv:2610.12519v1 (first posted 2026-10-07). Full main text, Supplementary Sections S1–S4, and Figures 4 and S3: https://arxiv.t3mt.com/html/2610.12519v1.
2. C. M. Saad-Roy and A. Traulsen, *Dynamics in a behavioral–epidemiological model for individual adherence to a nonpharmaceutical intervention*, PNAS 120 (2023), e2311584120, DOI:10.1073/pnas.2311584120. Full open-access text: https://pmc.ncbi.nlm.nih.gov/articles/PMC10622941/.
3. H. Martin, F. Castella, and F. Hamelin, *Wearing face masks to protect oneself and/or others: Counter-intuitive results from a simple epidemic model accounting for selfish and altruistic human behavior*, J. Theor. Biol. 624 (2026), 112395, DOI:10.1016/j.jtbi.2026.112395 (abstract accessible; complete text not retrieved).
