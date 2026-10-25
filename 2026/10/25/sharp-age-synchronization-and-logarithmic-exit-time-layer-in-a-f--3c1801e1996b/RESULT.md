# Sharp age synchronization and logarithmic exit-time layer in a farthest-reset Brownian swarm

## Finding
Consider the deterministic infinite-swarm stationary **Model B** (farthest-particle renewal resetting) of Meerson and Vilk [1], in which particles perform one-dimensional scaled Brownian motion between resets and are returned to the origin when they reach the stationary absorbing support boundary. Write \(H>0\) for the anomalous diffusion exponent, \(r>0\) for the per-particle reset flux and \(D>0\) for the generalized diffusivity. The source work establishes the stationary free-boundary model and its support radius; these are not new claims here.

Let \(T_H\) be the lifetime of a particle injected at zero until it is reset at either edge in this deterministic stationary hydrodynamic description. Let \(A_H\) be the age since the last reset of a particle sampled from the normalized stationary population. Let \(B_s\) be standard one-dimensional Brownian motion with generator \(\partial_{xx}\), started at zero, and let \(S=\inf\{s>0:|B_s|=1\}\). Set \(p=1/(2H)\), \(M(p)=\mathbb E[S^p]\), \(\mu=\mathbb E[\log S]\), and \(W=\log S-\mu\).

The exact renewal identities are
\[
 rT_H\ \overset{d}{=}\ \frac{S^p}{M(p)},\qquad
 f_{rA_H}(a)=\mathbb P\!\left(\frac{S^p}{M(p)}>a\right)\quad(a\ge0),
\]
where \(f_{rA_H}\) is a density. As \(H\to\infty\),
\[
 \frac{rT_H-1}{p}\ \longrightarrow\ W\quad\text{in }L^1\text{ under this coupling},
 \qquad rA_H\longrightarrow\operatorname{Unif}(0,1)
 \quad\text{in total variation}.
\]
The convergence rate is sharp:
\[
 \boxed{\lim_{H\to\infty} H\,d_{\mathrm{TV}}\!\left(
 \mathcal L(rA_H),\operatorname{Unif}(0,1)\right)
 = C_*:=\frac14\mathbb E|W|=0.1606639484570\ldots>0.}
\]
Furthermore, the nontrivial boundary layer of the stationary age density is
\[
 \boxed{\lim_{H\to\infty}f_{rA_H}(1+py)=\mathbb P(W>y)}
\]
locally uniformly in \(y\in\mathbb R\). It is a non-Gaussian profile determined by logarithmic Brownian interval-exit time. In particular the age layer is of width \(1/(2H)\) in units of \(1/r\). These limit statements are for the deterministic hydrodynamic stationary model, not a joint finite-population limit.

## Assumptions and scope
The scaled Brownian displacement started at an injection/reset time zero is \(X_t=\sqrt D\,B_{t^{2H}}\), so its variance is \(2Dt^{2H}\). The two absorbing edges of the stationary hydrodynamic population occur at \(\pm L_H\), where \(L_H\) is chosen by the stationary mass-one condition for injection flux \(r\). Spatially, the model solves \(\partial_t n=2HDt^{2H-1}\partial_{xx}n\) with initial mass \(r\delta_0\), absorbing edges, and no bulk losses [1]. A single injected lifetime corresponds to the killed heat-kernel survival. A stationary population age is sampled by normalizing the age-resolved mass, not by selecting reset events. For each \(H>0\), \(r,D\) are fixed and positive. The asymptotic \(H\to\infty\) is taken only after the hydrodynamic stationary description has been specified.

## Proof
**1. Exact lifetime normalization.** Let \(S\) be the first exit of \(B\) from \((-1,1)\), whose generator is \(\partial_{xx}\). Brownian scaling and the deterministic clock yield
\[
 T_H\ \overset d=\ \left(\frac{L_H^2}{D}\right)^p S^p.
\]
If \(n_H(x,t)=r\,k_{(-L_H,L_H)}(x,0;Dt^{2H})\) is the age-resolved mass with killed heat kernel \(k\), its age marginal is \(r\mathbb P(T_H>t)\). Conservation of stationary mass is exactly \(1=r\int_0^\infty\mathbb P(T_H>t)dt=r\mathbb ET_H\). Thus \((L_H^2/D)^p M(p)=1/r\), giving the first stated identity. This step does not assume independence among finitely many interacting particles; it uses the deterministic stationary free-boundary model.

**2. Stationary-age law.** A particle of age \(t\) is present if its sampled lifetime exceeds \(t\). Therefore the normalized stationary-age density is \(g_H(t)=r\mathbb P(T_H>t)\). Under \(a=rt\), \(f_{rA_H}(a)=\mathbb P(rT_H>a)\), and its integral is one by the preceding mean-lifetime identity.

**3. Mellin data and logarithmic moments.** The killed Brownian heat kernel gives the absolutely convergent survival expansion for every \(s>0\):
\[
 \mathbb P(S>s)=\frac4\pi\sum_{n=0}^{\infty}
 \frac{(-1)^n}{2n+1}\exp\!\left(-\frac{\pi^2(2n+1)^2}{4}s\right).
\]
For real \(q>0\), integrate the positive-moment tail to obtain
\[
 M(q)=\frac4\pi\,\Gamma(q+1)\left(\frac4{\pi^2}\right)^q
 \beta(2q+1),\qquad
 \beta(z)=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^z},
\]
where the beta series converges in its displayed use \(z=2q+1>1\). The first-exit density has superexponentially small lower-time probability and exponentially small upper-time probability, so \(\mathbb E[S^q]\) is finite for all real \(q\), and \(\log M(q)\) is smooth around zero. Hence
\[
 \mu=-\gamma_E+\log(4/\pi^2)+2\beta'(1)/\beta(1),
 \qquad \log M(p)=\mu p+O(p^2).
\]
The derivatives use the analytic continuation of the Dirichlet beta function. Numerically \(\mu=-0.989161905925814\ldots\).

**4. Lifetime limit.** Write \(Y=\log S\). The exact coupling \(Q_p=rT_H=e^{pY-\log M(p)}\) and \(\log M(p)=p\mu+O(p^2)\) imply
\[
 \frac{Q_p-1}{p}\longrightarrow Y-\mu=W
 \quad\text{in }L^1\text{ (in fact in }L^2\text{)}.
\]
A Taylor remainder is dominated by \(Cp(1+Y^2)e^{\varepsilon|Y|}\) after division by \(p\); the required exponential moments of \(|Y|\) follow from the two-sided moments of \(S\). This proves both the centered lifetime limit and that \(\mathbb E|W|\) is finite and strictly positive.

**5. Sharp total-variation identity.** Because \(Q_p>0\) has mean one, the age density is \(f_p(a)=\mathbb P(Q_p>a)\). Direct Fubini integration gives the exact equality
\[
 2d_{\mathrm{TV}}(f_p,\mathbf1_{(0,1)})
 =\int_0^1\mathbb P(Q_p\le a)da
 +\int_1^\infty\mathbb P(Q_p>a)da
 =\mathbb E|Q_p-1|.
\]
Consequently \(d_{\mathrm{TV}}/p\to\mathbb E|W|/2\), and \(p=1/(2H)\) establishes the coefficient \(C_*=\mathbb E|W|/4\). Since \(\mathbb EW=0\), integration by parts yields an exponentially convergent expression:
\[
 C_*=\frac12\int_{e^\mu}^{\infty}\frac{\mathbb P(S>s)}s\,ds
 =\frac2\pi\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}
 E_1\!\left(\frac{\pi^2(2n+1)^2e^\mu}{4}\right),
\]
where \(E_1(z)=\int_z^\infty e^{-u}du/u\). This gives the stated positive numerical constant without simulation.

**6. Edge profile.** For each fixed \(y\),
\[
 f_p(1+py)=\mathbb P((Q_p-1)/p>y)\to\mathbb P(W>y).
\]
The first-exit law of Brownian motion has a continuous positive density, so \(W\) has a continuous distribution. Uniform convergence of cumulative distributions to a continuous limit gives convergence uniformly in \(y\), on any fixed bounded interval (indeed uniformly on the real line where the transformed threshold is defined). The fact that \(W\) is non-Gaussian follows, for instance, from the exponential upper tail of \(S\), which gives a double-exponential right tail for \(W\), unlike a normal law.

## Verification
A standalone Python program `verify.py` numerically checks the Mellin identity against independently solved exit-time moment boundary-value problems, evaluates the logarithmic moments and exponential-integral coefficient, checks the exact finite-\(H\) total-variation series, and confirms convergence of the scaled coefficient for a sequence of \(H\) values. It returned **53 deterministic checks passed** using mpmath 1.3.0. These calculations are finite corroboration; Steps 1–6 above constitute the proof for all \(H>0\) and the asymptotic limit. In particular, no finite numerical evaluation is used as a substitute for uniform integrability or total-variation convergence.

## Relationship to prior work
Meerson and Vilk [1] established the hydrodynamic age-structured PDE, its killed-heat-kernel solution, the stationary radius \(L_H\), and the large-\(H\) *radius* limit. Consequently the exact age marginal and its Brownian time-change representation are implicit in their published solution and are not independently asserted as new. The present claim is the **sharp total-variation convergence rate**, its explicit nonzero constant, and the **non-Gaussian stationary age boundary layer**. This requires centering the logarithmic exit-time law and comparing the entire probability density, rather than merely taking a spatial or temporal marginal. The earlier normal-diffusion Model B [2] establishes the special baseline \(H=1/2\) and finite-population spatial/radius fluctuations. Independent Poisson renewal resetting [3] instead gives exponential reset lifetimes and has no farthest-particle free boundary. Standard Brownian exit-time and renewal-reward identities are used as prior mathematics.

## Limitations
The sharp result concerns the deterministic infinite-swarm stationary free-boundary model only. It is not an estimate for the microscopic finite-\(N\) process, nor does it justify simultaneous limits in population size and \(H\). The exact stationary age marginal is a consequence of [1]; only the quantified singular large-\(H\) behavior and its boundary profile are advanced as additional results. While no matching theorem was located in the inspected literature and indexed comparisons, the primary paper's complete age-dependent Green function creates a material implicit-coverage risk. Independent novelty assessment is not yet available.

## References
[1] B. Meerson and O. Vilk, *Age-structured hydrodynamics of ensembles of anomalously diffusing particles with renewal resetting*, arXiv:2512.14345v1 (first public version 2025-12-16); Phys. Rev. Research **8**, 023103 (2026), DOI: 10.1103/sxf5-674q.

[2] O. Vilk, M. Assaf and B. Meerson, *Fluctuations and first-passage properties of systems of Brownian particles with reset*, arXiv:2205.10273v4 (2022); Phys. Rev. E **106**, 024117 (2022).

[3] A. S. Bodrova, A. V. Chechkin and I. M. Sokolov, *Scaled Brownian motion with renewal resetting*, Phys. Rev. E **100**, 012120 (2019), DOI: 10.1103/PhysRevE.100.012120.
