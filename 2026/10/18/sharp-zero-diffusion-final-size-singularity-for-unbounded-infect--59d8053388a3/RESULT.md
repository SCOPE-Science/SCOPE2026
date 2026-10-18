# Sharp zero-diffusion final-size singularity for unbounded infectivity evolution

## Finding

The unrestricted continuous-infectivity mutation model of Lamata-Otín, Arenas, Gómez-Gardeñes and Soriano-Paños [1] has a sharp and singular final-size boundary. Let a closed population of unit size contain initially \(s_0>0\) susceptible individuals, \(i_0>0\) infectious individuals and \(r_0\geq0\) removed individuals, with \(s_0+i_0+r_0=1\). Let the initial infected infectivity-trait measure be any nonzero finite measure supported on \([0,L_0]\) and of mass \(i_0\). For arbitrary \(k,\mu>0\), the full-line trait-diffusion coefficient \(D>0\) implies
\[
\lim_{t\to\infty}(s(t),i(t),r(t))=(0,0,1),
\qquad \lim_{t\to\infty}m(t)=+\infty,
\]
where \(m(t)\) is the infected population's conditional mean infectivity. With precisely \(D=0\), however,
\[
s_\infty\geq s_0\exp\!\left[-\frac{kL_0(1-r_0)}{\mu}\right]>0.
\]
Thus \(\lim_{D\downarrow0}r_\infty(D)=1>r_\infty(0)\). Even if mutation is allowed at any rate, imposing a genuine nonnegative hard cap \(0\leq\lambda\leq L\) gives the universal bound \(s_\infty\geq s_0\exp[-kL(1-r_0)/\mu]>0\). The discontinuity is a property of *unbounded-trait deterministic dynamics*, not an assertion about real viruses.

## Assumptions and scope

For \(t\geq0\), \(\rho(t,d\lambda)\) is the nonnegative infected-trait measure on the **entire real line**; after any positive time with \(D>0\) it admits a density. The system is
\[
\partial_t\rho=(k\lambda s(t)-\mu)\rho+\frac D2\partial_{\lambda\lambda}\rho,
\quad i(t)=\int_{\mathbb R}\rho(t,d\lambda),
\quad s'(t)=-k s(t)\int_{\mathbb R}\lambda\rho(t,d\lambda),
\quad r'(t)=\mu i(t).
\]
The normalization \(s+i+r=1\) is imposed initially and follows from the equations. Initial \(\rho_0\) is any finite positive measure with compact support \([0,L_0]\), not necessarily Gaussian or absolutely continuous; it can be a point mass. Set \(m(t)=\int\lambda\rho/i\). For a separately considered **capped model**, the mutation dynamics can be any conservative mechanism preserving a nonnegative infected distribution supported on \([0,L]\), with the same macroscopic infection and recovery balances; the capped statement does not assert the same full-line PDE or any particular reflecting boundary scheme.

## Proof

**1. Exact transform.** Write \(A(t)=k\int_0^t s(u)\,du\) and \(M_0(z)=\int e^{z\lambda}\rho_0(d\lambda)>0\) for real \(z\). Let \(K_0(z)=\log M_0(z)\). For \(M(z,t)=\int e^{z\lambda}\rho(t,d\lambda)\), integration by parts on the full line gives
\[
\partial_tM=k s(t)\partial_zM-\mu M+\frac D2 z^2 M.
\]
The characteristics yield the **exact identity for every finite \(t\)**
\[
M(z,t)=M_0\bigl(z+A(t)\bigr)
 \exp\!\left[-\mu t+\frac D2\int_0^t
 \bigl(z+A(t)-A(u)\bigr)^2\,du\right]. \tag{1}
\]
All exponential moments are finite at finite time: compact initial support makes \(M_0\) entire and the time integral in (1) finite. The formula is also a constructive positive Gaussian-kernel representation. In particular, for the exponentially tilted probability \(\rho_0^a(d\lambda)=e^{a\lambda}\rho_0(d\lambda)/M_0(a)\), differentiating \(\log M(z,t)\) at \(z=0\) gives
\[
 m(t)=K_0'(A(t))+D\int_0^t[A(t)-A(u)]\,du,
\qquad V(t)=K_0''(A(t))+Dt. \tag{2}
\]
Here \(K_0''(a)=\operatorname{Var}_{\rho_0^a}(\lambda)\geq0\), so **\(V(t)\geq Dt\) without any Gaussian hypothesis**, and
\[
 m'(t)=k s(t)V(t)\geq kD s(t)t. \tag{3}
\]
The initial support in \([0,L_0]\) also implies \(0\leq K_0'(A(t))\leq L_0\) and \(0\leq K_0''(A(t))\leq L_0^2/4\).

**2. Global positive solution.** The full-line evolution with prescribed continuous \(s\) is positive by its Gaussian propagator. Equation (2) implies \(m(t)\geq0\) whenever \(s\geq0\). Then \(s(t)=s_0\exp[-k\int_0^t i(u)m(u)\,du]>0\) and \(s\) is nonincreasing. Likewise \(r'\geq0\), \(i'=i(ksm-\mu)\), \(i(t)>0\) at every finite time, and \(s+i+r=1\). Since \(0\leq s\leq s_0\), equation (2) supplies the finite-time bound \(m(t)\leq L_0+(Dks_0/2)t^2\). The nonnegative, bounded compartments and this trait-moment estimate prevent finite-time blowup and extend the local solution uniquely to all \(t\geq0\).

**3. Positive full-line diffusion consumes all susceptibles.** Since \(r\) increases and is at most one,
\[
 \int_0^\infty i(t)\,dt=\frac{r_\infty-r_0}{\mu}\leq\frac{1-r_0}{\mu}<\infty. \tag{4}
\]
The monotonicity of \(s\) and \(r\) gives limits of both, hence of \(i=1-s-r\); an integrable nonnegative function with a limit has limit zero. Assume \(D>0\) and, for contradiction, \(s_\infty=\delta>0\). Inequality (3) then gives \(m(t)\geq m(0)+kD\delta t^2/2\). But
\[
 \frac{d}{dt}\log i(t)=k s(t)m(t)-\mu
 \geq k\delta\bigl[m(0)+kD\delta t^2/2\bigr]-\mu
 \longrightarrow+\infty,
\]
which would force \(i(t)\to+\infty\), contradicting \(i(t)\leq1\). Therefore \(s_\infty=0\), and equation (4) plus mass conservation forces \(r_\infty=1\). If \(m\) had a finite limit, then \(s_\infty=s_0\exp[-k\int_0^\infty im]>0\) by (4), again impossible. Since (3) makes \(m\) nondecreasing, \(m(t)\to+\infty\).

**4. Zero diffusion and hard caps.** With \(D=0\) the support of \(\rho\) remains in \([0,L_0]\); therefore \(0\leq m(t)\leq L_0\). More generally, for any nonnegative **conservative** mutation scheme retaining the infected-trait support inside \([0,L]\), one has \(0\leq m(t)\leq L\). In either case,
\[
 \log\frac{s_0}{s_\infty}
 =k\int_0^\infty m(t)i(t)\,dt
 \leq k L\frac{1-r_0}{\mu},
\]
with \(L=L_0\) for \(D=0\). This proves the displayed positive survivor lower bounds and the singular final-size contrast.

**Exact witness.** Let \(s_0=9/10\), \(i_0=1/10\), \(r_0=0\), \(k=\mu=1\), and \(\rho_0=(1/10)\delta_0\). For \(D=0\), infection generates no new cases and \(s_\infty=9/10\), \(r_\infty=1/10\). For every full-line \(D>0\), the proved limits are \(s_\infty=0\), \(r_\infty=1\). Every capped version with \(\lambda\in[0,1]\) retains at least \((9/10)e^{-1}\) susceptibles.

## Verification

The included `verify.py` checks the exact transform's characteristic differential identity with rational polynomial coefficients, the mean/variance identity on a two-point non-Gaussian initial trait law, positivity of the variance floor, and the exact no-mutation witness and hard-cap bound. The general all-time statement follows from the inequalities above, **not** from finite trajectory simulations. Run `python3 verify.py` using the standard Python library. The proof checks the arbitrary-initial-measure quantifier analytically; the checker illustrates critical identities but cannot certify infinite time.

## Relationship to prior work

Equation (1) of Lamata-Otín et al. [1] is exactly the underlying continuous infectivity-diffusion system. Its Supplementary Notes 2–3 approximate the trait variance by \(Dt\) for a sharply concentrated early-time profile, find a no-cutoff active regime even at vanishing initial reproduction number, and Supplementary Note 5 plots finite-horizon final sizes. Those statements neither assert nor prove the universal **infinite-time** attack rate for all compactly supported initial trait measures. The present claim isolates this mathematical consequence of the **unbounded, nonnegative-mean full-line approximation** and its hard-cap contrast; it does not claim the original paper's model, early-time cubic growth, or basic replicator-mutator transform as new.

Berestycki et al. [2, Proposition 4] already show complete eventual infection and divergent mean risk in a **different, susceptibility-structured social-diffusion model** with an unbounded risk trait and a special zero-restoring-drift limit. That establishes the general warning about unbounded traits; the present result does not claim that principle for the first time. Its infected-trait diffusion, nonlinear recovery-coupled moment transform, and all-compact-initial-data variance inequality are not obtained by that proposition's hypotheses or proof. Almeida et al. [3] prove final-size theorems for heterogeneous epidemic systems including diffusion under bounded contact-kernel assumptions; their bounded-kernel coverage does not directly include linear, unbounded infectivity on the whole real line. Classical replicator-mutator Gaussian methods, including Alfaro and Veruete [4], are background rather than claimed inventions.

## Limitations

The unrestricted heat equation instantaneously generates negative trait values and traits larger than one, although the motivating interpretation calls \(\lambda\) a probability of transmission. Thus this finding is a **mathematical boundary/normalization warning**, not a prediction that all real people become infected under arbitrarily weak biological mutation. Finite trait grids, truncations, hard probability caps, absorbing extinction cutoffs, discrete finite populations, and noise can radically change the terminal behavior. The two nested limits (long time and vanishing diffusion) cannot be exchanged. The theorem gives no uniform-in-\(D\) forecast horizon, quantitative extinction times, or control-policy optimum. Nonnegative initial compact support is essential here; no assertion is made for initially unbounded distributions or negative initial mean. Originality remains subject to possible unindexed specialized results.

## References

1. S. Lamata-Otín, A. Arenas, J. Gómez-Gardeñes and D. Soriano-Paños, *Interplay between evolutionary and epidemic time scales challenges the outcome of control policies*, arXiv:2603.18801, submitted 19 March 2026; revised 3 October 2026. https://arxiv.org/abs/2603.18801 ; full-text equations and supplementary notes: https://arxiv.t3mt.com/html/2603.18801v2 .
2. H. Berestycki, B. Desjardins, J. S. Weitz and J.-M. Oury, *Epidemic modeling with heterogeneity and social diffusion*, Journal of Mathematical Biology 86, article 60 (2023), Proposition 4. https://pmc.ncbi.nlm.nih.gov/articles/PMC10039364/ ; doi:10.1007/s00285-022-01861-w.
3. L. Almeida, P.-A. Bliman, G. Nadin, B. Perthame and N. Vauchelet, *Final size and convergence rate for an epidemic in heterogeneous population*, arXiv:2010.15410, later Mathematical Models and Methods in Applied Sciences 31 (2021), 1021–1051. https://arxiv.org/abs/2010.15410 .
4. M. Alfaro and M. Veruete, *Density-dependent replicator-mutator models in directed evolution*, arXiv:1901.07848. https://arxiv.org/abs/1901.07848 .
