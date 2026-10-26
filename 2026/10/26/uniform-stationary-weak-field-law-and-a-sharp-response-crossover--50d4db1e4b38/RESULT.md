# Uniform stationary weak-field law and a sharp response crossover for threshold resetting

## Finding
Consider a one-dimensional drift-diffusion with drift \(h\ne0\), diffusion coefficient \(D>0\), and Poisson resetting at rate one to the origin only while \(|x|>1\). In the mean-field stationary self-consistent model \(D=\alpha\Gamma^\beta\), where \(\Gamma\) is the stationary resetting flux, fix \(\alpha>0\) and \(\beta>1\). For sufficiently small \(h>0\), there exists a stationary low-diffusivity branch with \(D_h\sim\alpha h^\beta\). On any branch with this asymptotic, its stationary density satisfies
\[
\lim_{h\downarrow0}\|p_h-\mathbf1_{(0,1)}\|_{L^1(\mathbb R)}=0,\qquad \|p_h-\mathbf1_{(0,1)}\|_1=O(h+h^{\beta-1}).
\]
Consequently every fixed nonnegative integer \(m\) obeys \(\lim_{h\downarrow0}\mathbb E_h[X^m]=1/(m+1)\); the mean tends \(1/2\), not the resetting threshold \(1\). Reflection gives the uniform law on \((-1,0)\) and mean \(-1/2\) for \(h<0\).

Writing \(M(h)=\mathbb E_h[X]\), the first mean correction has a sharp response phase diagram:
\[
M(h)-\frac12\sim
\begin{cases}
-\alpha h^{\beta-1}, &1<\beta<2,\\
\dfrac{1+\sqrt{1+4\alpha}-4\alpha}{4}\,h, &\beta=2\text{ and }\alpha\ne3/4,\\
\dfrac12h, &\beta>2.
\end{cases}
\]
At the marginal point \(\beta=2,\alpha=3/4\), the linear coefficient vanishes but the next term is strictly positive:
\[
M(h)-\frac12=\frac{45}{16}h^2+o(h^2).
\]
Thus the sign of the leading correction changes across \(\beta=2\); on that line it changes at \(\alpha=3/4\), where a quadratic positive correction replaces the linear response.

## Assumptions and scope
The stationary density is the normalized integrable solution of
\[
0=D p''-h p'-\mathbf1_{\{|x|>1\}}p+\Gamma\delta_0,
\qquad \Gamma=\int_{|x|>1}p(x)\,dx,
\qquad D=\alpha\Gamma^\beta.
\]
Diffusion uses generator \(D\partial_x^2+h\partial_x\), not \((D/2)\partial_x^2\). The threshold and resetting rate are both set to one, and the reset destination is zero. The theorem asserts existence of a low-diffusivity branch, not uniqueness among all self-consistent branches. The limit \(h\to0\) is taken along this branch; an exactly zero bias need not select it. For noninteger moments the uniform limit is valid for every continuous observable of polynomial growth, since the tails below are exponentially decaying with controlled moments.

## Proof
**1. Exact stationary solution for prescribed \(h,D\).** By reflection take \(h>0\). Put
\[
\Delta=\sqrt{h^2+4D},\quad k=\frac2{h+\Delta},\quad \ell=\frac{h+\Delta}{2D},\quad v=\frac hD,\quad a=1-hk=Dk^2,\quad e=e^{-v},
\]
\[
r=\frac{(1-ae)e}{h\ell+1-e},\quad
C=\left[1+\frac1k-r\left(1+\frac1\ell\right)\right]^{-1}.
\]
The stationary density has the nonnegative piecewise representation
\[
p(x)=C\begin{cases}
h r\ell\,e^{\ell(x+1)},& x<-1,\\
(1-ae+r)e^{vx}-r,&-1\le x<0,\\
1-ae^{-v(1-x)},&0\le x<1,\\
h k e^{-k(x-1)},&x\ge1.
\end{cases}
\]
To check, the characteristic equations are \(Dk^2+hk=1\) and \(D\ell^2-h\ell=1\). The displayed pieces solve the stationary differential equation away from \(-1,0,1\), with continuous densities and derivatives at \(\pm1\), and derivative jump \(D[p'(0^+)-p'(0^-)]=-hC(1+r)\). The exterior flux masses equal \(\Gamma_+=hC\) and \(\Gamma_-=hCr\), giving the correct reset source. Integration of the stationary equation and first-moment generator identity \(\mathbb E[X\mathbf1_{|X|>1}]=h\) give the normalizing factor \(C\); direct integration verifies total mass one. Positivity follows from the displayed expressions or regeneration from the source at zero. The fixed-\(D\) stationary solution is unique by the associated killed drift-diffusion resolvent.

**2. Singular limit and existence of a self-consistent branch.** Write \(\delta=D/h\) and \(\eta=1/k=(h+\sqrt{h^2+4D})/2\). Uniformly for \(D/(\alpha h^\beta)\) in any fixed compact subset of \((0,\infty)\), \(\delta\to0\), \(e=e^{-1/\delta}\to0\), \(r=O(e)\), \(\eta=O(h+\sqrt D)\), and \(C=1+O(h+\delta)\). In this regime, the interior piece on \((0,1)\) tends to density one, its boundary-layer deficit has total mass at most \(Ca\delta\), the exterior mass is \(hC(1+r)=O(h)\), and the negative interval has mass \(O(\delta)\). Hence
\[
\|p-\mathbf1_{(0,1)}\|_1=O(h+\delta),\qquad \Gamma=hC(1+r)=h[1+O(h+\delta)].
\]
Continuity of the fixed-\(h\) map \(D\mapsto\Gamma(D,h)\) and these uniform estimates imply, by the intermediate-value theorem applied to \(D-\alpha\Gamma(D,h)^\beta\), a self-consistent root between \(\alpha h^\beta/2\) and \(2\alpha h^\beta\) for small \(h\). Every such root satisfies \(D_h/(\alpha h^\beta)\to1\). The exponential outer tails have scales \(1/k\) and \(1/\ell\), which shrink here; dominated integration yields all fixed polynomial moments.

**3. Exact mean and asymptotic regimes.** Applying the stationary generator to \(x\) gives the exterior first-moment relation \(\mathbb E[X\mathbf1_{|X|>1}]=h\). Integrating the two interior pieces yields
\[
M(h)=h+C\left[\frac12-a\left(\delta-\delta^2(1-e)\right)
+(1-ae+r)\left(e\delta-\delta^2(1-e)\right)+\frac r2\right].
\]
Because \(r,e\) are exponentially small, and \(C=(1+\eta)^{-1}+O(e)\), this reduces, with exponentially small error, to
\[
M(h)=h+\frac{\frac12-a\delta-(1-a)\delta^2}{1+\eta}+O(\operatorname{poly}(1/\delta)e^{-1/\delta}).
\]
If \(1<\beta<2\), then \(\delta\sim\alpha h^{\beta-1}\gg h+\sqrt D\), and \(a\to1\). The dominant deficit is \(-\delta\). If \(\beta>2\), then \(\eta\sim h\), \(\delta=o(h)\), and \(M(h)-1/2\sim h/2\). At \(\beta=2\), put \(D=h^2c(h)\), \(Q(c)=(1+\sqrt{1+4c})/2\). Here \(\eta=hQ(c)\), \(a=1-1/Q(c)\), and \(c(h)\to\alpha\), so the coefficient of \(h\) is \(1-Q(\alpha)/2-\alpha[1-1/Q(\alpha)]\), equivalently \((1+\sqrt{1+4\alpha}-4\alpha)/4\). Its only positive zero is \(\alpha=3/4\).

At this marginal coupling, \(c(h)=(3/4)[1+hQ(c(h))]^{-2}+O(e^{-c_*/h})\) for some \(c_*>0\), by the exact resetting-flux equation. Taylor expansion gives \(c(h)=3/4-9h/4+O(h^2)\), \(Q(c(h))=3/2-9h/8+O(h^2)\), and \(a=1/3-h/2+O(h^2)\). Substituting yields \(C=1-3h/2+27h^2/8+O(h^3)\) and the interior-moment bracket \(1/2-h/4+3h^2/4+O(h^3)\); therefore \(M(h)=1/2+45h^2/16+O(h^3)\), completing the proof.

## Verification
The accompanying `checker.py` derives the normalized piecewise density from the generator, checks integration against independent numerical quadrature and the source's resetting-rate relation, solves the self-consistency equation for several parameters, and verifies the asymptotic regimes. At the marginal point, it additionally checks the rational Taylor coefficient exactly using fraction arithmetic. The proof, not the finite numerical samples, establishes the quantified limiting results.

## Relationship to prior work
E. Bertin (2022, arXiv:2205.00817v1; Journal of Physics A 55, 384007) introduced this resetting-dependent diffusivity model, obtained the exact finite-diffusivity stationary equations, and identified a low-diffusivity branch with \(D\sim\alpha|h|^\beta\) for \(\beta>1\). Its small-field discussion suggests localization at the positive or negative threshold. The present theorem determines the full weak-field stationary law instead: the deterministic drift travels through the entire interval before the threshold reset, producing a uniform occupation profile, and specifies the sharp response-correction phase diagram. The source's phase-transition analysis is not claimed as new. Related constant-rate and partial-reset diffusion work involves a different generator or resetting protocol.

## Limitations
The self-consistent stationary model is a mean-field description. No claim concerns nonlinear dynamical stability of a branch, finite-population fluctuations, selection by exactly zero bias, or uniqueness of the global stationary solution. The model requires \(\beta>1\) and \(\alpha>0\), and this conclusion may not extend to position-dependent resetting rates other than the outside-threshold indicator. The source's analytical formulas contain enough information to obtain the limit by further asymptotic analysis; the specific law and phase diagram presented here are therefore an explicit extraction rather than an independent alteration of the model.

## References
1. E. Bertin, *Stochastic resetting of a population of random walks with resetting-rate-dependent diffusivity*, arXiv:2205.00817v1 (public May 2, 2022), *J. Phys. A: Math. Theor.* 55 (2022) 384007, DOI:10.1088/1751-8121/ac8845.
2. O. Tal-Friedman, Y. Roichman, S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363 (2022), DOI:10.1103/PhysRevE.106.054116. The resetting mechanism differs from the threshold model.
3. I. Santra, U. Basu, S. Sabhapandit, *Effect of stochastic resetting on Brownian motion with stochastic diffusion coefficient*, arXiv:2205.00549 (2022); the diffusion coefficient evolves stochastically and resetting also changes it.
