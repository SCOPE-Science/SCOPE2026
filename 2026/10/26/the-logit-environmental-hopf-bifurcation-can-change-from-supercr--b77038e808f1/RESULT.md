# The logit environmental Hopf bifurcation can change from supercritical to subcritical

## Finding

Consider the two-strategy logit-learning feedback game introduced in [1], with an explicit positive environmental adjustment-speed parameter \(\epsilon\). The sign of the cubic Hopf coefficient is *not* fixed by the usual payoff assumptions. It has the exact form
\[
\ell=\frac{-2(1+\omega^2)+Q(1-\omega^2)}{16p},\qquad Q=\frac{a(\theta-1)}{D},\quad p=\frac{\theta}{(1+\theta)^2}.
\]
If \(Q\ge-2\), the Hopf bifurcation is supercritical for every \(\epsilon>0\). If \(Q<-2\), it is supercritical for \(0<\epsilon<\epsilon_c\) and subcritical for \(\epsilon>\epsilon_c\), where
\[
\epsilon_c=\frac{2-Q}{(-2-Q)\beta_h Dp\,n_h(1-n_h)}.
\]
Here *supercritical* means the small periodic orbits are attracting and occur when the rationality parameter exceeds \(\beta_h\); *subcritical* means they are repelling and occur when it is below \(\beta_h\). These are local assertions at a nondegenerate Hopf point; they do not determine global periodic-orbit branches.

## Assumptions and scope

Let \(h>0\), \(r>h\), \(t>0\), \(v>0\), \(0<\theta<1\), \(\epsilon>0\), and \(\beta>0\). Put \(\sigma(y)=1/(1+e^{-y})\), and consider the smooth planar system on \((0,1)^2\):
\[
\begin{aligned}
\dot x&=\sigma(\beta g(x,n))-x,\\
\dot n&=\epsilon n(1-n)((1+\theta)x-1),\\
g(x,n)&=axn+bx+cn+d,\\
a&=v-h-r-t,\quad b=h+r,\quad c=h-v,\quad d=-h.
\end{aligned}
\]
The source's payoff differences are \(\delta_{SP0}=-h\), \(\delta_{RT0}=r\), \(\delta_{TR1}=t\), \(\delta_{PS1}=v\). The explicit \(\epsilon\) is the environmental time-scale parameter present in its background system, Jacobian, and numerical parameter specifications; setting \(\epsilon=1\) reproduces the displayed logit differential equations (LD).

Define \(k=1+\theta\), \(L=\log(1/\theta)\), \(D=r+t+\theta(v-h)>0\), \(p=\theta/k^2\), \(q=(\theta-1)/k\), \(M=k(rv+ht)/D>0\), and the interior-entry threshold \(\beta_{\mathrm{int}}=kL/(r-\theta h)\). For \(\beta>\beta_{\mathrm{int}}\), the interior equilibrium is
\[
x_*=1/k,\qquad n_\beta=\frac{r-\theta h-kL/\beta}{D}.
\]
The Hopf value is
\[
\beta_h=\frac{p^{-1}+akL/D}{M}.
\]
Assume \(\beta_h>\beta_{\mathrm{int}}\), so \(n_h=n_{\beta_h}\in(0,1)\). All subsequent Hopf claims concern this strict interior case, with \(\beta\) varying near \(\beta_h\) while \(\epsilon\) and payoff parameters are fixed.

## Proof

**1. Interior equilibrium and transversality.** The equilibrium logit equation is \(\beta g(x_*,n_\beta)=L\). Direct substitution gives the displayed \(n_\beta\). The trace of the interior Jacobian is
\[
T(\beta)=\beta p(b+a n_\beta)-1=pM(\beta-\beta_h).
\]
The off-diagonal Jacobian entries are \(J_{12}=\beta p(a/k+c)=-\beta pD/k<0\) and \(J_{21}=\epsilon k n_\beta(1-n_\beta)>0\). Thus its determinant at Hopf is
\[
\omega^2=\epsilon\beta_hDp\,n_h(1-n_h)>0,
\]
and the eigenvalue real-part crossing speed is \(T'(\beta_h)/2=pM/2>0\).

**2. A normalized cubic coefficient.** Set \(B=\beta_h pD/k>0\), \(u=x-x_*\), and \(w=(B/\omega)(n-n_h)\). The linear equations become \(\dot u=-\omega w\), \(\dot w=\omega u\). Write \(A=ak/D\), \(Q=Aq\), and \(z=\beta_h g(x,n)-L\). Exactly (not just to first order),
\[
 z=\frac{u-\omega w+A\omega uw}{p}.
\]
At \(L\), the three first derivatives of the logistic response are \(p\), \(pq\), and \(p(q^2-2p)\), while \(q^2+4p=1\). Let \(F\) be the nonlinear part of \(\dot u\), and let \(G\) be the nonlinear part of \(\dot w\). The derivatives entering the planar Hopf formula satisfy
\[
\begin{aligned}
F_{uu}&=q/p,&F_{ww}&=q\omega^2/p,\\
F_{uw}&=\omega(A-q/p),&F_{uuu}&=(q^2-2p)/p^2,\\
F_{uww}&=(q^2-2p)\omega^2/p^2-2Aq\omega^2/p.
\end{aligned}
\]
As \(\dot w\) consists of \(\omega u\) plus terms of the forms \(uw\) and \(uw^2\), the other derivatives that can contribute to the planar first Lyapunov coefficient are zero. The standard real-coordinate expression (or independent polar averaging) is
\[
\ell=\frac{F_{uuu}+F_{uww}}{16}
+\frac{F_{uw}(F_{uu}+F_{ww})}{16\omega}
=\frac{-2(1+\omega^2)+Q(1-\omega^2)}{16p}.
\]
This coefficient is the radial cubic coefficient for the stated linear canonical coordinates, \(\dot\rho=(T/2)\rho+\ell\rho^3+\text{higher-order terms}\); its sign does not depend on a positive rescaling of coordinates or time.

**3. Sharp sign classification.** Under the payoff assumptions,
\[
2D-a(\theta-1)=(1+\theta)(r+t+v-h)>0,
\]
so \(Q<2\). The numerator of \(16p\ell\) is \((Q-2)-(Q+2)\omega^2\). It is strictly negative for every \(\omega^2>0\) when \(Q\ge-2\). When \(Q<-2\), it crosses zero once, from negative to positive, at \(\omega^2=(2-Q)/(-2-Q)\). The displayed \(\epsilon_c\) follows from the positive linear dependence of \(\omega^2\) on \(\epsilon\). Algebra gives
\[
D(Q+2)=(3-\theta)(r+t)+(3\theta-1)(v-h),
\]
hence \(Q<-2\) is equivalent to \(\theta<1/3\) and \(v>h+(3-\theta)(r+t)/(1-3\theta)\). Ordinary nondegenerate Hopf theory, together with the positive trace crossing, gives the stated local stability and side of occurrence for \(\ell\ne0\).

**4. Exact sign-changing example.** Choose \((\theta,h,r,t,v)=(1/5,1,2,1,100)\). Then
\[
D=114/5,\quad a=96,\quad p=5/36,\quad Q=-64/19,
\]
\[
\beta_h=228/335+(32/67)\log5,\quad
n_h=\frac{9/5-(6/5)\log5/\beta_h}{114/5}.
\]
Here \(\beta_h>\beta_{\mathrm{int}}=(2/3)\log5\), with \(0<n_h<1\). Put \(\kappa=\beta_hDp\,n_h(1-n_h)\). Exact rational interval arithmetic based on a convergent series for \(\log5\) gives \(9/100<\kappa<1/10\). The coefficient becomes
\[
\ell=\frac9{190}(13\epsilon\kappa-51).
\]
It is negative for \(\epsilon=1\) and positive for \(\epsilon=100\), establishing both distinct Hopf types within the same admissible payoff game. For the source's illustrative payoffs \((\theta,h,r,t,v)=(4/5,1/2,3/2,1/2,1/4)\), \(Q=1/4\), and the coefficient is \(\ell=-81(7+9\omega^2)/1280<0\), justifying the observed local supercritical branch.

## Verification

The standalone `verify.py` checks the derivative-based formula and, independently, computes the same coefficient from polar averaging; verifies the payoff-parameter factorization and the sign-change criterion; and certifies the example with rational interval bounds for \(\log5\). Execute `python verify.py` with Python 3 and SymPy installed. The series bound used is
\[
2\sum_{j=0}^{N-1}\frac{(2/3)^{2j+1}}{2j+1}<\log5<2\sum_{j=0}^{N-1}\frac{(2/3)^{2j+1}}{2j+1}+\frac{2(2/3)^{2N+1}}{(2N+1)(1-4/9)}
\]
with \(N=70\). Exact comparisons and symbolic identities are reproduced without stochastic simulation. The proof, rather than sample trajectories, supplies the infinite-parameter statements.

## Relationship to prior work

Paarporn [1], Sections III–V, derives the logit–environment equilibrium and trace crossing, and explicitly leaves calculation of the first Lyapunov coefficient and stability conditions for cycles to future work. This finding supplies that coefficient and a qualitative distinction absent from the examined text. Gong and collaborators [2] compute Hopf coefficients in a different, replicator–mutator environmentally coupled system, so their formulas do not directly imply the logit coefficient here. Liu and collaborators [3] study nonlinear imitation rather than payoff-logit revision; only its accessible abstract could be examined, leaving publication-priority uncertainty. The formulas for the planar first Lyapunov coefficient are standard; originality is claimed only for their analytical evaluation and sharp sign phase in this particular game family.

## Limitations

The result applies only when the logit game has a strictly interior, transverse Hopf point. It concerns small-amplitude local periodic orbits, not global periodic-orbit uniqueness, the high-rationality global collapse, or the size of basins of attraction. At \(\epsilon=\epsilon_c\) the cubic coefficient vanishes and the existence, nondegeneracy, and type of any higher-order generalized-Hopf bifurcation are *not* established. The original displayed logit model uses \(\epsilon=1\); the general speed dependence is for the explicitly parameterized feedback family. Other literature may contain a stronger equivalent normal-form result not located in the consulted sources.

## References

[1] K. Paarporn, *The madness of people: rational learning in feedback-evolving games*, arXiv:2311.02745v1 (first posted 2023-11-05), Sections III–V, https://arxiv.org/html/2311.02745v1.

[2] Gong et al., *Limit Cycles Analysis and Control of Evolutionary Game Dynamics with Environmental Feedback*, arXiv:2205.10734 (2022), particularly Appendix C, https://arxiv.org/abs/2205.10734.

[3] Liu, Cao and Wu, *General non-linear imitation leads to limit cycles in eco-evolutionary dynamics*, arXiv:2210.10552 (2022), abstract available; full text not inspected, https://arxiv.org/abs/2210.10552.
