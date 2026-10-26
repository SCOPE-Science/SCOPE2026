# Constant health information makes vaccination-memory oscillations lower mean infection

## Finding
In the public-information extension of the delayed vaccination imitation model of Kyrychko and Blyuss [1], let \(S(t)\) and \(I(t)\) be susceptible and infected fractions and \(p(t)\) vaccination uptake. Assume the parameters and domain below, and let \((S_*,I_*,p_*)\) be the unique positive endemic equilibrium. For **every positive nonconstant periodic solution** of any period \(T>0\), put
\[
\bar p=\frac1T\int_0^T p(t)\,dt,\quad
\bar I=\frac1T\int_0^T I(t)\,dt,\quad
\mathcal V=\frac1T\int_0^T\frac{dt}{p(t)}-\frac1{\bar p}.
\]
Then \(\mathcal V>0\) and the **exact finite-amplitude prevalence discount** is
\[
\boxed{I_*-\bar I=\frac{\mu}{\delta}\,
\frac{\eta\mathcal V}{\alpha+\mu/\delta+\eta/(p_*\bar p)}},\qquad \delta=\mu+\nu.
\]
In particular, when \(\eta>0\), every such oscillation strictly **lowers** mean infection below the positive endemic-equilibrium level, whereas for \(\eta=0\) its mean infection equals that level exactly. No small-amplitude expansion or restriction on the normalized memory law is necessary. More generally, the same statements hold for any compactly interior invariant probability distribution on complete trajectories: time averages are replaced with expectations, and strictness holds exactly when vaccination is nonconstant under that distribution.

## Assumptions and scope
The precise model is
\[
\begin{aligned}
\dot S&=\mu(1-p)-\beta SI-\mu S,\\
\dot I&=I(\beta S-\delta),\\
\dot p&=k(1-p)\left[p\left(I-\alpha \int_{[0,\infty)}p(t-s)\,G(ds)\right)+\eta\right],
\end{aligned}
\]
with \(\mu,\nu,\beta,\alpha,k>0\), \(\delta=\mu+\nu\), \(\eta\ge0\), and \(G\) any Borel probability measure on nonnegative delays. The physical region is \(S\ge0\), \(I\ge0\), \(S+I\le1\), \(0\le p\le1\). We require \(\beta>\delta\), put \(q=1-\delta/\beta>0\), and restrict \(0\le\eta<\alpha q^2\). These ensure a unique endemic equilibrium with \(S_*,I_*>0\) and \(0<p_*<q<1\). Explicitly,
\[
S_*=\delta/\beta,\qquad
p_*=\frac{\mu q+\sqrt{\mu^2 q^2+4\delta\eta(\mu+\delta\alpha)}}{2(\mu+\delta\alpha)},\qquad
I_*=\frac\mu\delta(q-p_*).
\]
For a periodic orbit, all three state variables must remain strictly interior: \(S(t),I(t)>0\) and \(0<p(t)<1\) for every time. For the invariant-measure extension, assume a stationary distribution on bounded complete solution histories supported in a compact set uniformly separated from \(I=0\), \(p=0\), and \(p=1\); the physical region and well-defined memory convolution are retained. Such assumptions ensure logarithms and reciprocal observables are bounded and differentiable as used below. **Neither the existence of a periodic orbit for every parameter choice nor an attracting cycle is claimed.**

## Proof
Write \(M(t)=\int_{[0,\infty)}p(t-s)\,G(ds)\). For a period-average \(\langle\cdot\rangle\) over \(T\), periodicity and Tonelli's theorem imply \(\langle M\rangle=\langle p\rangle=\bar p\), irrespective of the delay distribution. Positive infection allows the logarithmic derivative
\[
\frac d{dt}\log I=\beta S-\delta,
\]
which gives \(\bar S=\delta/\beta=S_*\). Averaging the infected equation yields \(\beta\langle SI\rangle=\delta\bar I\), hence also \(\operatorname{Cov}(S,I)=0\). Averaging the susceptible equation gives
\[
\mu q=\mu\bar p+\delta\bar I,\qquad \bar I=\frac\mu\delta(q-\bar p).\tag{1}
\]
Since \(p\in(0,1)\), the imitation equation has the exact logarithmic identity
\[
\frac d{dt}\log\frac{p}{1-p}=k\left[I-\alpha M+\frac\eta p\right].
\]
Its period average is zero, so
\[
\bar I=\alpha\bar p-\eta\left\langle\frac1p\right\rangle.\tag{2}
\]
A positive equilibrium obeys the corresponding identities
\[
I_*=\frac\mu\delta(q-p_*)=\alpha p_*-\frac\eta{p_*};\tag{3}
\]
together they give \((\mu+\delta\alpha)p_*^2-\mu q p_*-\delta\eta=0\), the advertised unique positive root. At \(p_*=q\), the polynomial is \(\delta(\alpha q^2-\eta)>0\) and is negative at zero, so \(0<p_*<q\) for the assumed range.

Put \(x=\bar p\) and \(\mathcal V=\langle1/p\rangle-1/x\). Subtract (3) from the common value in (1)–(2). Elementary rearrangement yields
\[
\left(\alpha+\frac\mu\delta+\frac\eta{xp_*}\right)(x-p_*)=\eta\mathcal V.\tag{4}
\]
Indeed, \(1/p_*-1/x=(x-p_*)/(xp_*)\). Equation (1) gives \(I_*-\bar I=(\mu/\delta)(x-p_*)\); substituting (4) proves the boxed formula.

The quantity \(\mathcal V\) admits the manifestly nonnegative variance representation
\[
\mathcal V=\frac1{x^2}\left\langle\frac{(p-x)^2}{p}\right\rangle\ge0.\tag{5}
\]
It vanishes exactly if \(p\) is constant. If \(p\) is constant and interior, then \(M=p\) and the vaccination equation forces \(I=\alpha p-\eta/p\) to be constant; positive constant infection forces \(S=\delta/\beta\), so the whole trajectory is an equilibrium. Thus each nonconstant periodic orbit has \(\mathcal V>0\). When \(\eta>0\), the denominator in (4) is strictly positive and the prevalence discount is strictly positive. When \(\eta=0\), (4) forces \(x=p_*\) and \(\bar I=I_*\), even for varying vaccination.

For a compactly interior invariant probability law on complete histories, replace every period average by the law's expectation. Stationarity gives zero expectation of the time derivative of each bounded smooth observable used above. Fubini's theorem and time-translation invariance still yield \(\mathbb E M=\mathbb E p\). Therefore (1)–(5) remain exact, and the same strictness criterion follows. This proves the invariant-law extension. Convex mixtures of invariant laws do not invalidate the identities; \(p\)-variance is computed for the combined stationary law.

## Verification
A standalone file `verify.py` symbolically checks the elimination identity and numerically exercises an Erlang-2 (strong Gamma) kernel through its two-stage linear chain. Requirements are in `requirements.txt`. Execute `python verify.py`. For \(\mu=(70\cdot365)^{-1}\), \(\nu=1/7\), \(\beta=10(\mu+\nu)\), \(\alpha=0.002\), \(\eta=10^{-6}\), \(k=400\), and Erlang-2 mean memory 150 days, the diagnostic on ten late apparent oscillation periods gives \(I_*\approx0.000215742844374\), \(\bar I\approx0.000210639238491\), observed discount \(5.1036058829\times10^{-6}\), and formula prediction \(5.10361729153\times10^{-6}\). The relative discrepancy is about \(2.24\times10^{-6}\), explained by numerical integration and endpoint sampling. This experiment is neither a rigorous existence proof for the cycle nor a substitute for the analytical argument, which is exact for every eligible orbit.

## Relationship to prior work
Kyrychko and Blyuss [1], Section IV, introduce the precise constant-information delayed vaccination model, calculate endemic equilibria, and study stability and numerical oscillations for multiple delay kernels. Their reported results do not provide the finite-amplitude campaign-dependent mean-prevalence formula. The equilibria, delay models, and numerical evidence for oscillatory regimes belong to [1], not to this finding. Bauch [2] observed that oscillations in an earlier imitation vaccination model do not change mean vaccine uptake or disease prevalence; the campaign-free neutrality here is a consistency boundary, not claimed as a new principle. d'Onofrio, Manfredi, and Poletti [3] investigated the interplay of public information and private vaccination, including delays and sustained oscillations; their accessible article emphasizes steady-state thresholds, control, and stability, not the exact inverse-vaccination Jensen discount shown here. A corresponding theorem may exist in related epidemiological or stationary-process literature and would affect priority.

## Limitations
The theorem is conditional on compact interior persistence, and says nothing about the prevalence of boundary attractors, extinction, basin sizes, global convergence, transient-time averages, or stochastic epidemics. The sign does not compare two separately perturbed models with different campaign strengths; it compares the same model's stationary orbit and endemic equilibrium. The mean-vaccination increase and mean-infection decrease are strict only for \(\eta>0\) and nonconstant vaccination. No claim of an independently audited result or exhaustive literature priority is made. Numerical recurrence is not mathematical proof of an exact periodic orbit.

## References
[1] Y. N. Kyrychko and K. B. Blyuss, “Vaccination games and imitation dynamics with memory,” *Chaos* **33**, 033134 (published online 20 March 2023), doi:10.1063/5.0143184; accessible manuscript: https://users.sussex.ac.uk/~kb275/Papers/cha23a.pdf.

[2] C. T. Bauch, “Imitation dynamics predict vaccinating behaviour,” *Proceedings of the Royal Society B* **272**, 1669–1675 (2005), doi:10.1098/rspb.2005.3153; https://pmc.ncbi.nlm.nih.gov/articles/PMC1560180/.

[3] A. d'Onofrio, P. Manfredi and P. Poletti, “The interplay of public intervention and private choices in determining the outcome of vaccination programmes,” *PLOS ONE* **7**, e45653 (2012), doi:10.1371/journal.pone.0045653; https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0045653.
