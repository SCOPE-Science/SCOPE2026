# Hidden subthreshold endemic branches for high-order environmental transmission

## Finding

Consider the six-compartment vaccinated/environmental epidemic system in the next section, with a Hill response of every fixed integer order \(n\geq3\). Fix all positive parameters other than the environmental susceptibility coefficient \(\alpha\), assume \(0<p<1\), \(0<\epsilon\leq\beta\), and fix \(\alpha_2>0\). If the disease-free control reproduction number \(\mathcal R_c<1\), then for **every sufficiently large** \(\alpha\geq\alpha_2\) there are **at least two distinct strictly positive endemic equilibria**, despite local exponential stability of the disease-free equilibrium. Their infected coordinates can be selected to satisfy

\[
\lim_{\alpha\to\infty}\alpha^{1/(n-1)}I_{\mathrm{small}}(\alpha)
=\left[\frac{\kappa K(1-\mathcal R_c)}{S_0(\varphi/\omega)^n}\right]^{1/(n-1)},
\qquad
\lim_{\alpha\to\infty}I_{\mathrm{large}}(\alpha)=\frac{\Lambda}{K},
\]

where \(K=(\xi+\mu)(\gamma+d+\mu)/\xi\), and \(S_0\) is the disease-free susceptible density. These are distinct singular limits, not assertions about the stability of either endemic state. In particular, absence of a local backward transcritical bifurcation does **not** preclude distant subthreshold endemic states in this model.

For a fully positive rational parameter set with \(n=3\), \(\mathcal R_c=5/42\) and \(\alpha=1000\), the equilibrium equation has **exactly two** positive roots; their infected coordinates lie in \((1/20,1/10)\) and \((1/3,1)\), respectively. The leading small-root coefficient is \(\sqrt{37}/4\), while the large root tends to \(2/3\) as \(\alpha\) increases.

## Assumptions and scope

Let \(S,E,I,V,R,C\) denote nonnegative susceptible, exposed, infectious, vaccinated-but-not-fully-protected, recovered, and environmental-contamination quantities. All rates below are strictly positive, except the constrained fraction \(p\in(0,1)\). Let \(\Lambda,\mu,\beta,\epsilon,\sigma,\eta,\gamma,d,\xi,\alpha,\alpha_2,\varphi,\omega,\kappa>0\), with \(\epsilon\leq\beta\) and \(\alpha_2\leq\alpha\). Put

\[
g(C)=\frac{C^n}{C^n+\kappa},\quad n\in\{3,4,5,\ldots\},
\]

and consider the autonomous equations

\[
\begin{aligned}
\dot S&=\Lambda-\beta SI-\sigma S+(1-p)\eta V-\alpha Sg(C)-\mu S,\\
\dot E&=\beta SI+\epsilon VI+\alpha Sg(C)+\alpha_2Vg(C)-(\xi+\mu)E,\\
\dot I&=\xi E-(\gamma+d+\mu)I,\\
\dot V&=\sigma S-\epsilon VI-(\eta+\mu)V-\alpha_2Vg(C),\\
\dot R&=\gamma I+p\eta V-\mu R,\\
\dot C&=\varphi I-\omega C.
\end{aligned}
\]

Here \(\kappa\) is the **denominator constant** for the Hill function, as in the original 2023 preprint; the equivalent half-saturation parametrization replaces it with \(\kappa_{\rm half}^{n}\). The theorem is unchanged under that reparametrization.

The disease-free solution has \(E=I=C=0\) and

\[
S_0=\frac{\Lambda(\eta+\mu)}{\mu(\sigma+\eta+\mu)+p\eta\sigma},\quad
V_0=\frac{\sigma S_0}{\eta+\mu},\quad
R_0=\frac{p\eta V_0}{\mu}.
\]

The symbol \(R_0\) in the last equality names the disease-free recovered **coordinate**, not the reproduction number. The control reproduction number is

\[
\mathcal R_c=\frac{\beta S_0+\epsilon V_0}{K},\qquad
K=\frac{(\xi+\mu)(\gamma+d+\mu)}{\xi}.
\]

Throughout the theorem, all parameters except \(\alpha\) are fixed, \(\mathcal R_c<1\), and \(\alpha\to\infty\). The strength \(\alpha_2\) is held fixed; the claim is not about jointly growing environmental rates or about every possible parametrized model.

## Proof

**1. A positive equilibrium is equivalent to a single scalar equation.** For every \(I>0\) write \(q=\varphi/\omega\), \(g_I=g(qI)\), and

\[
D_I=\epsilon I+\eta+\mu+\alpha_2g_I.
\]

Solving the stationary vaccinated and susceptible equations, followed by the remaining linear compartment equations, gives

\[
\begin{aligned}
S_\alpha(I)&=\frac{\Lambda}{\beta I+\sigma+\mu+\alpha g_I-(1-p)\eta\sigma/D_I},\\
V_\alpha(I)&=\frac{\sigma S_\alpha(I)}{D_I},\qquad
E(I)=\frac{\gamma+d+\mu}{\xi}I,\\
C(I)&=qI,\qquad
R_\alpha(I)=\frac{\gamma I+p\eta V_\alpha(I)}{\mu}.
\end{aligned}
\]

These expressions are strictly positive for all \(I>0\): since \(D_I>\eta+\mu\), one has \((1-p)\eta\sigma/D_I<\sigma\), making the denominator of \(S_\alpha\) strictly positive. The only remaining equation is the exposed balance, which is equivalent to

\[
Q_\alpha(I)=S_\alpha(I)\left(\beta+\alpha\frac{g_I}{I}\right)
+V_\alpha(I)\left(\epsilon+\alpha_2\frac{g_I}{I}\right)-K=0.
\]

Every positive zero generates a unique strictly positive full equilibrium, and every strictly positive equilibrium arises in this way. As \(n\geq3\), \(g_I/I\to0\) when \(I\downarrow0\), and therefore

\[
Q_\alpha(0^+)=\beta S_0+\epsilon V_0-K=-K(1-\mathcal R_c)<0,
\]

independently of \(\alpha\).

**2. A small positive branch is forced on a singular scale.** Let \(h=\alpha^{-1/(n-1)}\), \(I=hy\), and keep \(y>0\) bounded away from zero and infinity. Since

\[
\frac{\alpha g(qhy)}{hy}=\frac{q^n y^{n-1}}{\kappa+q^n h^n y^n},\qquad
\alpha g(qhy)=\frac{h q^n y^n}{\kappa+q^n h^n y^n},
\]

all expressions in \(Q_{h^{-(n-1)}}(hy)\) extend smoothly to \(h=0\) near a positive \(y\). The limiting scalar equation is

\[
Q_{h^{-(n-1)}}(hy)\longrightarrow
\frac{S_0q^n}{\kappa}y^{n-1}-K(1-\mathcal R_c).
\]

It has the unique positive zero

\[
y_*=\left[\frac{\kappa K(1-\mathcal R_c)}{S_0q^n}\right]^{1/(n-1)}.
\]

Its derivative with respect to \(y\) at \(y_*\) is strictly positive. The ordinary implicit-function theorem at \((h,y)=(0,y_*)\) supplies a smooth local root \(y(h)>0\), whence \(I_{\rm small}=h y(h)\) and the first asserted limit.

**3. A separated large positive branch is forced by recruitment balance.** For any fixed \(I>0\), \(g_I>0\). In the limit \(\alpha\to\infty\),

\[
\alpha S_\alpha(I)g_I\to\Lambda,\qquad
S_\alpha(I)\to0,\qquad V_\alpha(I)\to0,
\]

locally smoothly in \(I\) on compact subsets of \((0,\infty)\). Therefore

\[
Q_\alpha(I)\longrightarrow\frac{\Lambda}{I}-K.
\]

The limiting equation has one positive root \(I_*=\Lambda/K\) and derivative \(-\Lambda/I_*^2\neq0\). With parameter \(t=1/\alpha\), the formula for \(S_\alpha\) is smooth at \(t=0\) for \(I>0\); the implicit-function theorem yields \(I_{\rm large}(\alpha)\to\Lambda/K\). Because the small branch tends to zero and this limit is positive, the two roots are different for all sufficiently large \(\alpha\). The positivity formulas in Step 1 finish existence of two full endemic states.

**4. The disease-free equilibrium remains locally exponentially stable.** At \(I=C=0\), \(g(0)=g'(0)=0\). In a suitable variable order, the linearization has diagonal blocks consisting of the susceptible/vaccinated \(2\)-by-\(2\) matrix (negative trace, determinant \(\mu(\sigma+\eta+\mu)+p\eta\sigma>0\)), the exposed/infectious matrix (negative trace, determinant \(\xi K(1-\mathcal R_c)>0\)), and the scalar entries \(-\mu\) and \(-\omega\). Every eigenvalue has negative real part. No stability of either positive branch is used or inferred.

**5. An exact all-positive witness.** Set \(n=3\), \(\Lambda=4\), \(p=1/2\), \(\beta=1/4\), \(\epsilon=1/8\), \(\alpha_2=1\), \(\alpha=1000\), and set every other listed rate and \(\kappa\) equal to \(1\). Then \(K=6\), \(S_0=16/7\), \(V_0=8/7\), and \(\mathcal R_c=5/42\). The rational function \(Q_{1000}(z)\) reduces to \(-2P(z)/H(z)\), where

\[
\begin{aligned}
P(z)={}&3z^8+12094z^7+280472z^6-192058z^5
 +12164z^4+184768z^3-128061z^2+70z+296,\\
H(z)={}&z^8+4032z^7+96176z^6+2z^5+4056z^4
+64288z^3+z^2+24z+112.
\end{aligned}
\]

All coefficients of \(H\) are positive. Exact substitution gives

\[
Q_{1000}(1/20)<0<Q_{1000}(1/10),\qquad
Q_{1000}(1/3)>0>Q_{1000}(1).
\]

Hence two separate positive roots occur; an exact rational Sturm count for \(P\) gives **exactly two** strictly positive real roots. In this witness the asymptotic small-root constant specializes to \(\sqrt{37}/4\), and the large-root limit to \(2/3\). The roots are approximately \(0.05021667366\) and \(0.66181378353\), quoted only as orientation; the rational signs, Sturm calculation, and general proof do not depend on numerical root solvers.

## Verification

Run the included `verify.py` from the same folder with Python 3 and SymPy. It reconstructs the scalar equation from the six original balances, checks their identities exactly, certifies all four rational sign substitutions, computes the exact positive-root count of \(P\) by Sturm machinery, verifies both singular limits in this witness symbolically, and checks \(\mathcal R_c=5/42\). The successful checker run does not replace the implicit-function argument for the theorem's infinitely many parameter values.

## Relationship to prior work

Gökçe, Gürbüz and Rendall (first public arXiv version July 24, 2023) introduce this six-compartment environmental-transmission model. Their Theorem 3.1 excludes **generic backward transcritical bifurcation** for \(n\ne2\), and their Section 4 treats coexistence of two subthreshold endemic states for \(n=2\), not the all-\(n\ge3\) strong-environmental-transmission branches or their two singular scales. The distinction between a local transcritical direction and global equilibrium multiplicity is essential.

Penitente, Foryś and Gürbüz (2026), studying the related full system with \(g(C)=C^n/(C^n+\kappa_{\rm half}^{n})\), establish disease-free local stability and, for supercritical reproduction number, uniform persistence and endemic existence. Their sections on nonlinear incidence, disease-free thresholds, and persistence do not establish this subthreshold branch theorem. A 2024 conference abstract by Foryś and Pernitente mentions attempted counts of positive steady states for arbitrary \(n\); no corresponding detailed theorem was accessible in the inspected material, which remains a priority risk.

Martcheva's 2019 study surveys generic bifurcation methods and discusses other epidemic equations; the implicit-function method here is standard and not claimed as novel. The contribution is the model-specific global subthreshold coexistence theorem together with **both exact branch scales** for arbitrary integer \(n\ge3\), plus an exact strictly positive witness.

## Limitations

The theorem proves existence and singular asymptotics for fixed baseline parameters and sufficiently strong \(\alpha\). It does not prove stability, uniqueness, exact saddle-node thresholds, global attraction, or epidemiological plausibility of very large environmental transmission rates. The two branches do not imply that all trajectories reach endemic infection. The full model is phenomenological; strong environmental transmission need not describe a particular pathogen. Some potentially relevant unpublished conference work and general bifurcation consequences remain unverified. No independent scientific audit or publication-priority certification has been performed.

## References

1. A. Gökçe, B. Gürbüz and A. D. Rendall, *Dynamics of a mathematical model of virus spreading incorporating the effect of a vaccine*, first public version 2023-07-24, arXiv:2307.12707v1; journal DOI 10.1016/j.nonrwa.2024.104097. https://arxiv.org/abs/2307.12707
2. E. Penitente, U. Foryś and B. Gürbüz, *Global stability and uniform persistence in an epidemic model with saturating fomite-mediated transmission*, first public version 2026-03-30, arXiv:2603.28285. https://arxiv.org/abs/2603.28285
3. M. Martcheva, *Methods for deriving necessary and sufficient conditions for backward bifurcation*, Journal of Biological Dynamics 13 (2019), 538–566. https://doi.org/10.1080/17513758.2019.1647359
4. U. Foryś and E. Pernitente, *On the dynamics of a mathematical model of virus spreading incorporating the effect of a vaccine by Gökçe et al.*, conference abstract, September 2024. https://kkzmbm.mimuw.edu.pl/sprawozdania/spr29/Forys.pdf
