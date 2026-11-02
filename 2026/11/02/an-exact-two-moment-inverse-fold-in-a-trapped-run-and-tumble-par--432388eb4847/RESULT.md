# An exact two-moment inverse fold in a trapped run-and-tumble particle

## Finding

A harmonic-trap run-and-tumble particle with an exponentially distributed, nonzero-duration rest (tumble) state has an exact stationary **independent beta-product representation**. This representation gives strict parameterwise stochastic ordering of stationary displacement magnitudes. More significantly, the map from its two dimensionless run/rest rates to the second and fourth stationary position moments has a **single sharp fold on every fixed-variance fiber**. Consequently, exactly two distinct pairs of strictly positive rates can generate the same second and fourth moments, and the entire region with two solutions is characterized below.

Let \(s=\mathbb E[Z^2]\in(0,1)\), \(t=\mathbb E[Z^4]/(3s)\), and define
\[
\rho=\sqrt{1+5s},\qquad
 t_{\min}(s)=\frac{(\rho-1)(3\rho+7)}{(2\rho+3)^2},\qquad
 t_{\mathrm{edge}}(s)=\frac{s}{1+2s}.
\]
The exact count of **finite, strictly positive** dimensionless rate pairs consistent with \((s,t)\) is
\[
\begin{array}{c|c}
\text{condition}&\text{number of rate pairs}\\\hline
 t<t_{\min}(s)\text{ or }t\geq 1/3&0\\
 t=t_{\min}(s)&1\\
 t_{\min}(s)<t<t_{\mathrm{edge}}(s)&2\\
 t_{\mathrm{edge}}(s)\leq t<1/3&1.
\end{array}
\]
Here \(0<t_{\min}(s)<t_{\mathrm{edge}}(s)<1/3\). A concrete two-to-one witness is
\[
 (a,c)=(7/5,28/5)\quad\text{and}\quad (a,c)=(3/2,15/2).
\]
Both have \(\mathbb E[Z^2]=1/3\) and \(\mathbb E[Z^4]=19/99\), but their sixth moments are respectively \(95/726\) and \(2185/16731\); hence the stationary laws really differ.

## Assumptions and scope

Fix trap relaxation rate \(b>0\), self-propulsion speed \(v>0\), run-to-tumble rate \(\alpha>0\), and tumble-to-run rate \(\beta>0\). The one-dimensional process follows
\[
\dot X_\tau=-b X_\tau+v\sigma_\tau,
\]
where \(\sigma_\tau\in\{-1,0,+1\}\). Each run state \(\pm1\) jumps to \(0\) at rate \(\alpha\); state \(0\) jumps to each of \(\pm1\) at rate \(\beta/2\). Direction after each tumble is an independent fair coin; there is no thermal diffusion. Define the dimensionless stationary coordinate \(Z=bX/v\) and dimensionless rates \(a=\alpha/b\), \(c=\beta/b\). The scale \(v/b\) is assumed known for the inverse-moment statement. Physical rates can be recovered by multiplying \((a,c)\) by \(b\) when \(b\) is known.

The Markov modulator has a unique stationary law. The stationary coordinate is the unique pullback solution
\[
Z_\tau=\int_{-\infty}^{\tau}b\,e^{-b(\tau-u)}\sigma_u\,du,
\]
so \(|Z|\leq1\), and compact support makes its moment sequence determinate. All assertions concern the stationary law, not a finite-time transient or estimation from noisy samples.

## Proof

**1. Generator recurrence and beta-product representation.** Rescale time by \(b\). Write \(p_n=\mathbb E[Z^n]\), \(q_n=\mathbb E[\sigma Z^n]\), \(h_n=\mathbb E[\sigma^2 Z^n]\). Stationarity of the three polynomial test functions, using the above transition rates, gives for every integer \(n\geq1\),
\[
p_n=q_{n-1},\qquad (n+a)q_n=nh_{n-1},
\]
and for every integer \(n\geq0\),
\[
(n+a+c)h_n=(n+c)p_n.
\]
Reflection symmetry implies \(p_{2m+1}=0\). Therefore, for every \(m\geq1\),
\[
\frac{p_{2m}}{p_{2m-2}}=
\frac{(2m-1)(2m-2+c)}{(2m-1+a)(2m-2+a+c)},\qquad p_0=1.
\]
Let \(U\sim\operatorname{Beta}(c/2,a/2)\), \(W\sim\operatorname{Beta}(1/2,a/2)\), and let \(\varepsilon\) be a fair random sign, all independent. The beta-moment identity \(\mathbb E[B^m]=(u)_m/(u+v)_m\) for \(B\sim\operatorname{Beta}(u,v)\) shows that \(\varepsilon\sqrt{UW}\) has this recurrence and vanishing odd moments. Both laws are supported on \([-1,1]\), so the Hausdorff moment theorem yields
\[
\boxed{Z\ \overset{d}{=}\ \varepsilon\sqrt{UW}.}
\]
The beta product is a representation of an already known hypergeometric stationary law, not an assertion that its density was previously unknown.

**2. Parameterwise stochastic order.** At fixed \(a\), the beta family \(\operatorname{Beta}(c/2,a/2)\) is strictly ordered upward by \(c\); its likelihood-density ratio is proportional to a positive power of \(u\). At fixed \(c\), both beta factors decrease strictly in first-order stochastic order as \(a\) increases; the corresponding density ratio is a positive power of \(1-u\) in the direction of decreasing \(a\). Independent quantile couplings preserve these strict inequalities after multiplication and square root. Thus for every \(r\in(0,1)\), \(\mathbb P(|Z|>r)\) increases strictly with \(c\) at fixed \(a\), and decreases strictly with \(a\) at fixed \(c\). The same ordering holds for every strictly increasing radial test function whose expectation exists.

**3. Exact fixed-second-moment inverse curve.** From the recurrence,
\[
s=\frac{c}{(a+c)(a+1)},\qquad
 t=\frac{c+2}{(a+c+2)(a+3)}.
\]
Fix any \(s\in(0,1)\). Solving the first identity gives a unique positive \(c\) for each
\[
0<a<\frac{1-s}{s},\qquad c=\frac{s a(a+1)}{1-s(a+1)}.
\]
Substituting in the second identity produces the rational inverse curve
\[
T_s(a)=\frac{a^2s-as-2s+2}{(a+3)(a-2as-2s+2)}.
\]
Its derivative has the exact factorization
\[
T_s'(a)=-\frac{2P_s(a)}{(a+3)^2(2as-a+2s-2)^2},
\]
\[
P_s(a)=s(5s-3)a^2+2(5s-1)(s-1)a+5(s-1)^2.
\]
Put \(y=sa/(1-s)\in(0,1)\). Then
\[
\frac{sP_s(a)}{(1-s)^2}
=(5s-3)y^2-2(5s-1)y+5s=:Q_s(y).
\]
Since \(Q_s(0)=5s>0\) while \(Q_s(1)=-1<0\), this quadratic has **exactly one simple root** in \((0,1)\): two roots there would force the endpoint signs to agree, and a double root would not change sign. Consequently \(T_s\) first decreases strictly and then increases strictly.

Solving the quadratic and selecting its sole admissible root gives
\[
a_*(s)=\frac{5(1-s)}{5s-1+\sqrt{1+5s}}.
\]
Direct substitution gives \(T_s(a_*)=t_{\min}(s)\). The endpoint limits, with endpoints excluded, are
\[
\lim_{a\downarrow0}T_s(a)=\frac13,
\qquad
\lim_{a\uparrow(1-s)/s}T_s(a)=\frac{s}{1+2s}=t_{\mathrm{edge}}(s).
\]
Because the unique minimum is strictly interior, \(t_{\min}<t_{\mathrm{edge}}\); since \(s<1\), \(t_{\mathrm{edge}}<1/3\). Counting intersections with the decreasing and increasing branches yields every case in the finding table. In particular the right endpoint \(a=(1-s)/s\), corresponding to \(c\to+\infty\), is **not** an admissible finite-rate solution, which explains the one-solution count at equality \(t=t_{\mathrm{edge}}\).

**4. Exact distinct-law witness.** For the two pairs in the finding, exact substitution yields identical \(s=1/3\), identical fourth moment \(19/99\), but distinct sixth moments. The sixth-moment formula following from the same recurrence is
\[
\mathbb E[Z^6]=
\frac{15c(c+2)(c+4)}{(a+c)(a+c+2)(a+c+4)(a+1)(a+3)(a+5)}.
\]
Their sixth-moment difference is exactly \(95/368082>0\), proving that the two parameter pairs are not merely an equivalent reparameterization of one stationary distribution.

## Verification

The accompanying standalone `verify.py` runs exact symbolic equalities in SymPy. It verifies seven general even-moment recurrences against the beta-product Pochhammer formula; the fixed-variance rational substitution, full derivative factorization and endpoint limits; the explicit fold minimum; the rational witness at orders two, four, and six; and 48 exact rational parameter evaluations along distinct fixed-variance fibers. The proof of uniqueness and the complete parameter-domain count are analytic; finite symbolic tests are supplementary rather than an exhaustive parameter sweep. Run with `python verify.py` after installing SymPy.

## Relationship to prior work

Sun, Ye, and Podgornik (2024 preprint; revised 2025) give the full one-dimensional stationary distribution, characteristic function, and even-moment machinery for this same model. Those results directly determine the forward law, and are not claimed here. The new question is **global inverse identifiability from only the stationary variance and fourth moment**: its unique interior fold, exact two-solution region and a pair of demonstrably distinct stationary laws are not stated in the inspected versions of that work. The independent beta-product representation makes the stochastic parameter order transparent, but the inverse fold—not the existence of a stationary law—is the main contribution.

Basu and collaborators (2019) provide an earlier exact harmonic-trap three-state solution with equal run/tumble time scales, which covers a one-parameter subfamily but not the two-rate fold. Guéneau, Majumdar, and Schehr (2026) study generalized velocity-redraw dynamics under Poisson events and Dirichlet-type representations; their transition mechanism differs from alternating finite-duration rest and running states. Thus general stick-breaking analogies do not by themselves supply this two-rate inverse classification.

## Limitations

The inverse theorem requires known deterministic trap and speed scales, positive exponential run and tumble durations, a symmetric choice of running direction, stationarity, no thermal noise and the one-dimensional trap. It classifies exact population moments, not sampling variance or statistical estimation accuracy. Higher moments can disambiguate the explicit witness, but no theorem here asserts that the sixth moment resolves **every** two-solution pair. The beta-product identity reformulates an established forward distribution; publication priority for the inverse classification remains subject to wider independent literature verification.

## References

1. A. Sun, F. Ye, and R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578v1 (first publicly available 2024-09-01), https://arxiv.org/html/2409.00578v1 ; revised arXiv:2409.00578v2, https://arxiv.org/html/2409.00578v2 .
2. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, and G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083 (2019), https://arxiv.org/abs/1910.10083 .
3. M. Guéneau, S. N. Majumdar, and G. Schehr, *Exact Stationary State of a \(d\)-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436 (2026), https://arxiv.org/abs/2602.08436 .
