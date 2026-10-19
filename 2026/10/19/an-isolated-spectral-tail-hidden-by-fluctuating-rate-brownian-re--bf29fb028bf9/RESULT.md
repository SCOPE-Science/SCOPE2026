# An isolated spectral tail hidden by fluctuating-rate Brownian resetting

## Finding
Consider Brownian motion on the real line with generator \(D\partial_x^2\), reset to the origin at instantaneous rate \(\lambda_t\). Independently of position and reset events, the rate is redrawn at Poisson times of intensity \(\mu>0\), each new rate having an exponential law of mean \(L>0\). Initialize the rate in its stationary exponential law. Write \(p(x)\) for the stationary position density.

Define, for \(s>0\),
\[
B(s)=\frac{e^{s/L}}{L}E_1(s/L)
=\int_0^\infty\frac{e^{-v/L}}{L(s+v)}\,dv,
\]
where \(E_1(z)=\int_z^\infty e^{-u}u^{-1}\,du\). There is a unique \(s_*\in(0,\mu)\) solving \(\mu B(s_*)=1\). Put
\[
\delta=\mu-s_*,\qquad
A=\frac{Ls_*}{\mu\delta},\qquad
\kappa=\sqrt{\delta/D}.
\]
Then \(0<A<1\), and \(p\) is **exactly a positive mixture of two-sided exponential densities**:
\[
p(x)=\frac{A\kappa}{2}e^{-\kappa|x|}
+\frac12\int_0^\infty
\sqrt{\frac{\mu+v}{D}}\,e^{-|x|\sqrt{(\mu+v)/D}}\,\rho(v)\,dv,
\]
where, for every \(v>0\),
\[
\rho(v)=\frac{e^{-v/L}/L}
{\left[1+(\mu/L)e^{-v/L}\operatorname{Ei}(v/L)\right]^2+
\left[(\pi\mu/L)e^{-v/L}\right]^2},\qquad
\int_0^\infty\rho(v)\,dv=1-A.
\]
Here \(\operatorname{Ei}\) is the usual real exponential integral on positive arguments. In particular, for every fixed \(\mu,L,D>0\),
\[
\boxed{\displaystyle
p(x)\sim\frac{A\kappa}{2}e^{-\kappa|x|}
\quad (|x|\to\infty).}
\]
The continuum of decay rates begins strictly above this isolated rate: \(\sqrt{\mu/D}>\kappa\). The small-wave-number/moment-defined effective rate
\[
r_{\mathrm{mom}}=\frac{1-\mu B(\mu)}{B(\mu)}
=\frac{2D}{\mathbb E[X^2]}
\]
strictly exceeds the genuine spatial-tail rate \(\delta\). For slow refreshing, with \(L,D\) fixed and \(\mu/L\downarrow0\),
\[
\begin{aligned}
s_*&=Le^{-\gamma-L/\mu}(1+o(1)),\\
\delta&=\mu-Le^{-\gamma-L/\mu}(1+o(1)),\\
A&=\frac{L^2}{\mu^2}e^{-\gamma-L/\mu}(1+o(1)),\\
r_{\mathrm{mom}}&\sim\frac{L}{\log(L/\mu)}.
\end{aligned}
\]
Here \(\gamma\) is the Euler--Mascheroni constant. Thus the true far-tail rate is asymptotic to \(\mu\), even though the moment-defined rate is much larger and the slowest exponential carries exponentially small mass.

## Assumptions and scope
All stated identities require \(D,L,\mu>0\), a stationary exponential redraw law for \(\lambda_t\), Poisson redraws independent of particle motion and resets, and reset-to-origin events conditionally Poisson at the current \(\lambda_t\). Neither a finite observation window nor the strictly frozen environment \(\mu=0\) is included in the fixed-parameter tail assertion. The stationary random position is denoted \(X\). The notation \(p(x)\) refers to its density, not to the distribution of the instantaneous rate.

## Proof
**1. Exact renewal resolvent.** Let \(\Phi(t)=\mathbb E[\exp(-\int_0^t\lambda_u\,du)]\) for the stationary rate process. Conditional on the first rate-refresh time,
\[
\Phi(t)=g(t)+\mu\int_0^t g(u)\Phi(t-u)\,du,
\qquad g(t)=\frac{e^{-\mu t}}{1+Lt}.
\]
Consequently, for \(q\ge0\),
\[
S(q):=\int_0^\infty e^{-qt}\Phi(t)\,dt
=\frac{B(\mu+q)}{1-\mu B(\mu+q)}.
\]
Since \(\mu B(\mu)<1\), \(S(0)<\infty\). Conditional no-reset probabilities give the stationary age density \(-\Phi'(t)\); its Fourier mixture is
\[
\widehat p(k)=1-Dk^2S(Dk^2).
\]
This also follows directly from the exact Fourier formula in Arutkin and Reuveni (2025). The stationary survival probability tends to zero since the rate process is ergodic with positive mean.

**2. The isolated pole and positive continuum.** The function \(B(s)\) is a Stieltjes transform. On \(s>0\), it is strictly decreasing, diverges as \(s\downarrow0\), and satisfies \(\mu B(\mu)<1\). Hence the stated \(s_*\) exists uniquely. If \(\operatorname{Im}s>0\), then \(\operatorname{Im}B(s)<0\); therefore \(1-\mu B(s)\) has no nonreal zero. In \(q\)-coordinates the unique off-cut pole of \(S(q)\) is \(q=-\delta\); the continuous cut begins at \(q=-\mu\). Differentiating the exponential integral gives
\[
-B'(s_*)=\frac{1}{L}\left(\frac1{s_*}-\frac1\mu\right)
=\frac{\delta}{L\mu s_*},
\]
so the pole residue is
\[
\operatorname{Res}_{q=-\delta}S(q)
=\frac{B(s_*)}{-\mu B'(s_*)}
=\frac{Ls_*}{\mu\delta}=A.
\]
On the upper lip of the cut, for \(v>0\),
\[
B(-v+i0)=-\frac{e^{-v/L}}{L}\bigl(\operatorname{Ei}(v/L)+i\pi\bigr),
\quad
-\frac1\pi\operatorname{Im}S(-\mu-v+i0)=\rho(v).
\]
Because \(\operatorname{Im}S(q)<0\) in the upper half-plane, \(S(q)>0\) for positive real \(q\), and \(qS(q)\to1\) as \(q\to+\infty\), the Stieltjes representation and boundary-value inversion yield the probability measure
\[
S(q)=\frac{A}{q+\delta}+
\int_0^\infty\frac{\rho(v)}{q+\mu+v}\,dv,
\qquad A+\int_0^\infty\rho(v)\,dv=1.
\]
The density is strictly positive for all \(v>0\), so \(0<A<1\). No atom occurs at the cut endpoint, because \(S(q)\) remains bounded as \(q\to-\mu\) from the right (its limit there is \(-1/\mu\)). The transform uniquely identifies
\[
\Phi(t)=Ae^{-\delta t}+
\int_0^\infty e^{-(\mu+v)t}\rho(v)\,dv.
\]

**3. Spatial inversion and exact tail.** Differentiating the last positive mixture shows that the stationary age density mixes exponential waiting laws with precisely these weights. For each \(u>0\),
\[
\int_0^\infty u e^{-ut}\frac{e^{-x^2/(4Dt)}}{\sqrt{4\pi Dt}}\,dt
=\frac12\sqrt{\frac{u}{D}}e^{-|x|\sqrt{u/D}}.
\]
Termwise positive integration gives the claimed exact spatial mixture. Since \(\mu>\delta\), the continuum is \(o(e^{-\kappa|x|})\): choose any fixed \(x_0>0\) and dominate its density at \(x>x_0\) by its finite value at \(x_0\), multiplied by \(e^{-(x-x_0)\sqrt{\mu/D}}\). Thus the isolated pole alone sets the asymptotic rate and positive prefactor.

**4. Different moment and tail scales.** Fourier expansion at zero gives \(\mathbb E[X^2]=2DS(0)\). From the mixture,
\[
S(0)=\frac{A}{\delta}+\int_0^\infty\frac{\rho(v)}{\mu+v}\,dv
<\frac{A+\int_0^\infty\rho(v)\,dv}{\delta}=\frac1\delta.
\]
Hence \(r_{\mathrm{mom}}=1/S(0)>\delta\). Finally, as \(s/L\downarrow0\),
\[
B(s)=L^{-1}\left[-\gamma-\log(s/L)+O((s/L)|\log(s/L)|)\right].
\]
Solving \(\mu B(s_*)=1\) yields the stated exponentially small \(s_*\), and substitution into \(A=Ls_*/(\mu\delta)\) gives its asymptotic. As \(\mu/L\downarrow0\), \(\mu B(\mu)\to0\) and \(B(\mu)\sim L^{-1}\log(L/\mu)\), proving the remaining statements.

## Verification
The provided `check.py` runs numerical tests of (i) the unique pole and atom, (ii) the exact mass normalization and Stieltjes identity over several refresh rates and transform arguments, (iii) the second-moment identity, (iv) exponentially small pole/residue asymptotics, (v) numerical eigenvalues of independent Gauss--Laguerre discretizations of the refreshed-rate operator, and (vi) spatial dominance of the isolated pole. These are finite cross-checks, not substitutes for the Stieltjes inversion and asymptotic proof. The proof covers all positive \(D,L,\mu\) independently of the sampled test values.

## Relationship to prior work
Arutkin and Reuveni (2025), sections 3--4, derive the model's stationary Fourier transform and describe an exponential far-field regime with an effective rate estimated from the small-wave-number expansion. Those formulas and the physical model are prior work. The new conclusion is the **exact positive pole-plus-continuum decomposition**, its all-parameter spectral gap and spatial prefactor, and the exponentially weak isolated mode that separates the genuine ultimate spatial-tail scale from the second-moment scale. A small-wave-number Taylor coefficient determines the second moment; by itself it does not identify the nearest complex singularity and hence cannot identify the ultimate spatial decay. The original article's qualitative exponential-tail observation is consistent with the existence of the isolated pole, while its slow-refresh moment-based decay-rate estimate describes a distinct observable. Evans and Majumdar (2014) treat constant-rate resetting, and Rose, Touchette, Lesanovsky and Garrahan (2018) treat spectral shifts with an external fixed reset rate; neither analyzed this independently refreshing continuous intensity law. General Stieltjes and rank-one perturbation theory supplies standard methods used here, and may imply elements of the derivation after model-specific reduction.

## Limitations
The exponentially small weight \(A\) means the ultimate tail may be observable only at very large spatial distances for slow refresh; the theorem does not assert that the asymptotic is a good finite-window approximation. Results are for an exponentially redrawn rate under Poisson environmental refresh, stationary initialization and one-dimensional Brownian motion. No assertion is made for nonstationary driving, rate-dependent diffusion, other rate laws, partial resets, higher dimensions or first-passage statistics. The infinite-distance and zero-refresh limits are not interchangeable. The quantitative novelty claim is restricted to the spectral decomposition and its consequences, not to the previously published Fourier solution or the general theory of Stieltjes transforms.

## References
1. M. Arutkin and S. Reuveni, *Diffusion with doubly stochastic resetting*, arXiv:2509.25365v1 (first publicly posted 2025-09-29), https://arxiv.org/abs/2509.25365 . Relevant material: sections 3--4, especially stationary Fourier expressions (23)--(24), slow/fast-refresh discussion, and asymptotic discussion.
2. M. R. Evans and S. N. Majumdar, *Diffusion with resetting in arbitrary spatial dimension*, Journal of Physics A: Mathematical and Theoretical **47** (2014), 285001; arXiv:1404.4574, https://arxiv.org/abs/1404.4574 . Relevant material: section 2, stationary constant-rate distributions.
3. D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, Physical Review E **98** (2018), 022129; arXiv:1806.01298, https://arxiv.org/abs/1806.01298 . Relevant material: sections II--IV, fixed-rate reset generator and Brownian example.
