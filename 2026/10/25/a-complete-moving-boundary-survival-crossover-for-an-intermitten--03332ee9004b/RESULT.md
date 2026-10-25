# A complete moving-boundary survival crossover for an intermittent map

## Finding
Fix \(0<\alpha<1\) and the Liverani–Saussol–Vaienti map
\[
T_\alpha(x)=\begin{cases}
x(1+2^\alpha x^\alpha),&0\le x\le1/2,\\
2x-1,&1/2<x\le1.
\end{cases}
\]
Let \(\mu_\alpha\) be its unique normalized absolutely continuous invariant probability. Take **any** deterministic sequence \(0<h_n<1/2\) with \(h_n\to0\). The horizon-dependent absorbing hole is \((h_n,1]\), and the survivor set includes times zero through \(n\):
\[
E_n=\{x\in[0,1]:T_\alpha^j(x)\in[0,h_n]\quad(0\le j\le n)\}.
\]
Set \(c_\alpha=\alpha2^\alpha\), \(\eta=(1-\alpha)/\alpha\), and \(\theta_n=n h_n^\alpha\). The invariant probability has the established local mass asymptotic
\[
\mu_\alpha([0,y])\sim K_\alpha y^{1-\alpha},\qquad
K_\alpha=\frac{\rho_\alpha(1/2)}{2^{\alpha+1}(1-\alpha)}>0,
\]
where \(\rho_\alpha=d\mu_\alpha/dx\) is normalized. Then
\[
\boxed{\quad\mu_\alpha(E_n)\sim K_\alpha(h_n^{-\alpha}+c_\alpha n)^{-\eta}.\quad}
\]
This equivalent formula covers arbitrary moving cutoffs, not just powers of \(n\).

For the process result, let \(X_n\) have conditional law \(\mu_\alpha(\cdot\mid E_n)\). Define \(\mathcal I_n(v_0,\ldots,v_n)\) as the continuous piecewise-linear function equal to \(v_j\) at \(t=j/n\), with linear interpolation between consecutive nodes. Let \(B\) be a random variable in \((0,1)\) with
\[
\Pr(B\le z)=z^{1-\alpha}\quad(0\le z\le1).
\]
Convergence below is weak convergence of random elements of \(C([0,1])\) under its uniform norm.

If \(\theta_n\to\theta\in[0,\infty)\), then
\[
\mathcal I_n\bigl(T_\alpha^jX_n/h_n:0\le j\le n\bigr)
\ \Longrightarrow\ Z_\theta,
\quad Z_\theta(t)=\bigl((1+c_\alpha\theta)B^{-\alpha}-c_\alpha\theta t\bigr)^{-1/\alpha}.
\]
If \(\theta_n\to\infty\), then
\[
\mathcal I_n\bigl(n^{1/\alpha}T_\alpha^jX_n:0\le j\le n\bigr)
\ \Longrightarrow\ Z_\infty,
\quad Z_\infty(t)=\bigl[c_\alpha(B^{-\alpha}-t)\bigr]^{-1/\alpha}.
\]
The second limit is a continuous finite-valued function almost surely because \(\Pr(B=1)=0\).

In particular, \(h_n=\lambda n^{-\beta}\), \(\lambda,\beta>0\), yields three exact regimes: \(\beta>1/\alpha\) gives \(\theta=0\) and a constant beta-distributed conditional path; \(\beta=1/\alpha\) gives \(\theta=\lambda^\alpha\) and a nontrivial continuum of crossover path laws; \(\beta<1/\alpha\) gives the universal aging path \(Z_\infty\). Corresponding survivor masses have exponents \(\beta(1-\alpha)\) above criticality and \((1-\alpha)/\alpha\) at or below criticality, with the exact positive constants determined by the boxed formula.

## Assumptions and scope
The source measure is the invariant probability of the **closed** LSV map and is conditioned on a different survival event for each horizon. At horizon \(n\), the boundary \(h_n\) is held fixed throughout its \(n+1\) observations. This is not a time-dependent within-orbit moving boundary. All cutoff sequences are deterministic and converge to zero. The lower endpoint \(0\) is included; its invariant-measure mass is zero.

The source's local invariant-density expansion used here is \(\rho_\alpha(x)=\kappa_\alpha x^{-\alpha}+O(1)\) as \(x\downarrow0\), with \(\kappa_\alpha=\rho_\alpha(1/2)/2^{\alpha+1}\). This follows from the inverse-branch density formula and bounded remainder in Korepanov–Wei–Wormell, §6, equations (6.1)–(6.3), Lemma 6.3. It is a quoted established input, not a new density theorem.

## Proof
**1. Exact geometry.** Write \(F(x)=x(1+2^\alpha x^\alpha)\) for the increasing left branch, and define \(a_n=F^{-n}(h_n)\), where each inverse uses \(F^{-1}:[0,1]\to[0,1/2]\). Because \(F(x)>x\) for \(x>0\), an orbit starting below \(h_n<1/2\) and staying below the boundary is entirely on the left branch and is monotone nondecreasing. Hence, without excluding any additional branches,
\[
E_n=[0,a_n],\qquad F^n(a_n)=h_n.
\]
The domain and all endpoint conventions are thus exact.

**2. Uniform inverse-time estimate.** For \(x>0\), put \(u=x^{-\alpha}\). The left-branch update in this coordinate is
\[
\Psi(u):=u\left(1+\frac{2^\alpha}{u}\right)^{-\alpha}
=u-c_\alpha+O(u^{-1})\quad(u\to\infty).
\]
For every orbit in \(E_n\) and every \(0\le j\le n\), one has \(u_j=(F^j x)^{-\alpha}\ge h_n^{-\alpha}\). Taylor's theorem consequently supplies a constant \(C_\alpha\), independent of \(n\) and \(x\in E_n\setminus\{0\}\), such that
\[
\sup_{0\le j\le n}|u_j-u_0+c_\alpha j|
\le C_\alpha n h_n^\alpha.
\]
At the upper survivor endpoint \(a_n\), substitute \(u_n=h_n^{-\alpha}\). This proves
\[
a_n^{-\alpha}=h_n^{-\alpha}+c_\alpha n+O(nh_n^\alpha),
\qquad a_n\sim(h_n^{-\alpha}+c_\alpha n)^{-1/\alpha}.
\]
The relative error indeed vanishes: \(n h_n^\alpha/(h_n^{-\alpha}+n)\le h_n^\alpha\to0\). This argument remains valid for exponentially small or highly oscillating cutoff sequences.

**3. Conditional initial-state law and survivor probability.** From the density asymptotic in the assumptions,
\[
\mu_\alpha([0,y])\sim K_\alpha y^{1-\alpha}.
\]
Condition on \(E_n=[0,a_n]\). For every \(0\le z\le1\),
\[
\Pr(X_n/a_n\le z)=\frac{\mu_\alpha([0,z a_n])}{\mu_\alpha([0,a_n])}
\longrightarrow z^{1-\alpha}.
\]
Thus \(B_n:=X_n/a_n\Rightarrow B\). Combining this with the estimate for \(a_n\) gives the boxed probability asymptotic without any unproven infinite-enumeration step.

**4. Finite crossover.** Assume \(\theta_n=n h_n^\alpha\to\theta<\infty\). The estimate in step 2 gives
\[
\frac{a_n^{-\alpha}}{h_n^{-\alpha}}\to1+c_\alpha\theta,
\quad
h_n^\alpha u_{\lfloor nt\rfloor}
=\left(\frac{h_n}{a_n}\right)^\alpha B_n^{-\alpha}-c_\alpha\theta_n t+o(1)
\]
uniformly over \(t\in[0,1]\) and over samples with \(B_n\ge\delta\), for each fixed \(\delta>0\). The error after multiplying by \(h_n^\alpha\) is bounded by \(C_\alpha n h_n^{2\alpha}=C_\alpha\theta_n h_n^\alpha=o(1)\). The limiting denominator is at least \(1\), so inversion by the continuous function \(v\mapsto v^{-1/\alpha}\) is uniform on the relevant compact ranges. The one-step polygonal interpolation error vanishes by the same uniform estimate. Because \(\lim_{\delta\downarrow0}\Pr(B<\delta)=0\), truncation and the continuous-mapping theorem establish convergence in \(C([0,1])\) to \(Z_\theta\). The endpoint \(\theta=0\) follows with no separate approximation.

**5. Diverging crossover.** Assume \(\theta_n\to\infty\). Then \(a_n^{-\alpha}/n\to c_\alpha\), and
\[
\frac{u_{\lfloor nt\rfloor}}n
=\frac{a_n^{-\alpha}}n B_n^{-\alpha}-c_\alpha t+o(1)
\longrightarrow c_\alpha(B^{-\alpha}-t).
\]
The error \(O(h_n^\alpha)\) is uniform in \(t\). On compact sets \(\delta\le B_n\le1-\delta\), the last denominator is bounded away from zero, giving uniform convergence of the polygonal paths after rescaling by \(n^{1/\alpha}\). As \(\Pr(B\in\{0,1\})=0\), allowing \(\delta\downarrow0\) proves weak convergence in \(C([0,1])\) to \(Z_\infty\). Notice that the value at \(t=1\) is finite almost surely, despite the formula's singular exceptional point \(B=1\).

**6. Sharpness and interpretation.** In each convergent regime, the endpoint law is nondegenerate. For \(\theta\in[0,\infty)\), its CDF at \(0<y<1\) is
\[
\Pr(Z_\theta(1)\le y)=
\left(\frac{1+c_\alpha\theta}{y^{-\alpha}+c_\alpha\theta}\right)^\eta.
\]
For \(\theta_n\to\infty\), the endpoint CDF at \(y>0\) is
\[
\Pr(Z_\infty(1)\le y)=
\left(\frac{c_\alpha}{y^{-\alpha}+c_\alpha}\right)^\eta.
\]
These formulas differ for finite \(\theta\), including \(\theta=0\), and the cutoff exponent \(1/\alpha\) follows from the unique balance \(n h_n^\alpha\asymp1\). The result therefore locates an actual transition in the full conditioned orbit geometry, not merely a change in a loose upper bound.

## Verification
The proof uses only the exact monotone survivor interval, a Taylor remainder controlled uniformly along every surviving orbit, and a literature-supported invariant-density asymptotic. The inverse-time estimate has an explicit uniform bound \(C_\alpha n h_n^\alpha\); neither a finite numerical test nor an approximate eigenvalue is used to prove the infinite-horizon assertions. Independent checks at \(\alpha=1/2\) and representative power-law cutoffs confirm the endpoint and inverse-branch scalings numerically, but are supplementary only.

## Relationship to prior work
Wang–Su (2026), arXiv:2610.21175v1, establishes conditional Birkhoff-sum limits for **fixed** holes bounded away from the neutral fixed point, with inducing/renewal methods. Its fixed-hole theorem neither allows horizon-dependent absorbing complements \((h_n,1]\) nor identifies the \(C([0,1])\)-valued crossover indexed by \(n h_n^\alpha\). Korepanov–Wei–Wormell (2026), arXiv:2610.01879v1, supplies fine invariant-density and Abel-coordinate methods, not an open-system conditional path law. Froyland–Murray–Stancevic (2011), arXiv:1012.2149v1, studies escape from a *fixed small neighborhood* of the neutral point and records inverse-branch scaling and absence of a natural absolutely continuous conditionally invariant probability for that retained neighborhood. It does not state simultaneous moving-boundary conditional path limits. Demers–Todd (2017) studies fixed-hole thermodynamic escape regimes and measure dependence. Bonanno–Tikekar (2026), arXiv:2601.15908v1, studies the opposite hole orientation \([0,\varepsilon]\) and its shrinking-hole escape rate. The new step here is the uniform two-scale coupling of horizon and retained-neighborhood size, for the invariant initial distribution, with the complete conditioned path limits.

## Limitations
The result is restricted to the specified one-dimensional LSV family with \(0<\alpha<1\). No assertion is made for infinite invariant measure, arbitrary nonmonotone neutral branches, randomly changing within-orbit holes, conditionally invariant densities, or independent validation. The density coefficient is quoted from existing analysis and its numerical value is not claimed here. The limit \(Z_\infty\) has heavy upper tails; uniform integrability of unbounded functionals is not inferred merely from path convergence. The originality comparison covers the named sources and searches but cannot certify exhaustive priority; the older inverse-branch literature is a genuine residual risk.

## References
1. C. Wang and Y. Su, *Conditional limit laws for open intermittent dynamics*, arXiv:2610.21175v1, 15 October 2026. Full HTML, §§1–8.
2. A. Korepanov, Y. Wei and C. Wormell, *Rigorous and effective numerics for Liverani–Saussol–Vaienti maps*, arXiv:2610.01879v1, 1 October 2026, especially §6 and Lemma 6.3.
3. G. Froyland, R. Murray and O. Stancevic, *Spectral degeneracy and escape dynamics for intermittent maps with a hole*, arXiv:1012.2149v1 (2010); published version (2011), §§2–3.
4. M. F. Demers and M. Todd, *Slow and fast escape for open intermittent maps*, 2017 preprint, especially Introduction and Theorems 1.7–1.9.
5. C. Bonanno and S. Tikekar, *On the escape rate for intermittent maps with holes shrinking around the indifferent fixed point*, arXiv:2601.15908v1, §3.
6. M. F. Demers and B. Fernandez, *Escape rates and singular limiting distributions for intermittent maps with holes*, Trans. Amer. Math. Soc. **368** (2016), 4907–4932.
