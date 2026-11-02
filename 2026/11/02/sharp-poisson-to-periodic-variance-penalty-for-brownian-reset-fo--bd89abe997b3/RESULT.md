# Sharp Poisson-to-periodic variance penalty for Brownian reset forcing in a harmonic trap

## Finding

A Brownian active force is reset to zero at independent renewal epochs but the harmonically confined particle it drives is **not** position-reset. The central result is a **sharp, strictly monotone, dimensionless variance cost** of Poisson rather than periodic force resetting at the same mean interval: this cost decreases from six to two as the product of trap relaxation and mean reset interval increases. A complementary exact renewal-clock formula quantifies the stationary variance for arbitrary iid reset durations.

Let the strictly positive independent reset intervals have law \(L\), mean \(m=\mathbb E L\in(0,\infty)\), and finite second moment. For Brownian diffusivity \(D>0\), the stationary reset force has covariance, for every \(s\in\mathbb R\),

\[
C_L(s)=\operatorname{Cov}(Y_0,Y_s)=\frac{D}{m}\,\mathbb E\left[(L-|s|)_+^2\right].
\]

Here \((a)_+=\max(a,0)\). If two clock distributions share their mean and satisfy \(L_1\le_{\mathrm{cx}}L_2\) in convex order, then \(C_{L_1}(s)\le C_{L_2}(s)\) at every lag. Consequently every nonnegative integrable causal linear filter has no larger stationary output variance under \(L_1\) than under \(L_2\).

In particular, for the harmonic response \(\dot X=-\mu X+Y\), \(\mu>0\), deterministic reset intervals \(L=m\) uniquely minimize the stationary position variance among *all* positive renewal clocks of fixed mean \(m\) and finite second moment. The variance has the exact clock functional

\[
V_L(\mu)=\frac{D}{\mu^2m}\,\mathbb E\left[L^2-\frac{2L}{\mu}+\frac{2(1-e^{-\mu L})}{\mu^2}\right].
\]

There is no finite upper variance bound under only the fixed-mean constraint. For periodic resetting and for Poisson resetting with the *same mean interval*, put \(z=\mu m\). Their stationary **random-time-sampled** variances obey

\[
V_{\mathrm{per}}=\frac{D}{\mu^3}\frac{z^2-2z+2(1-e^{-z})}{z},\qquad
V_{\mathrm{Pois}}=\frac{2D}{\mu^3}\frac{z^2}{1+z}.
\]

The exact inefficiency ratio

\[
R(z)=\frac{V_{\mathrm{Pois}}}{V_{\mathrm{per}}}=
\frac{2z^3}{(1+z)[z^2-2z+2(1-e^{-z})]}
\]

is strictly decreasing on \((0,\infty)\), with sharp limits \(R(0^+)=6\) and \(R(+\infty)=2\). Thus \(2<R(z)<6\) at every finite positive \(z\).

## Assumptions and scope

Construct a stationary two-sided renewal point process with independent interval lengths \(L>0\) almost surely, \(0<\mathbb E L=m<\infty\), and \(\mathbb E L^2<\infty\). In every interval, independently start Brownian motion from zero with covariance \(\mathbb E[B(u)B(v)]=2D\min(u,v)\), \(D>0\). Concatenating these excursions, with an instantaneous force reset to zero at each renewal, produces the stationary mean-zero process \(Y_t\). No continuity across reset epochs is assumed for \(Y\).

The particle position \(X\) is **not reset**; it is the stable causal convolution

\[
X_t=\int_0^\infty e^{-\mu u}Y_{t-u}\,du,\quad\mu>0.
\]

More generally, \(Z_k(t)=\int_0^\infty k(u)Y_{t-u}\,du\) for any measurable \(k\ge0\) in \(L^1([0,\infty))\). Each integral exists in mean square by the finite second moment of \(Y\). The convex order \(L_1\le_{\mathrm{cx}}L_2\) means that \(\mathbb E\phi(L_1)\le\mathbb E\phi(L_2)\) for every convex function for which both expectations exist. In the periodic case, stationarity means **uniform random phase**, not observation only at reset epochs.

## Proof

**1. Stationary covariance.** Let \(A\) and \(B\) be the stationary age and residual lifetime of the renewal interval containing time zero. The equilibrium renewal-reward identity is

\[
\mathbb E[h(A,B)]=\frac1m\mathbb E\left[\int_0^L h(a,L-a)\,da\right]
\]

for every nonnegative measurable test function \(h\). Conditional on \(A=a\) and \(B=b\), the force at zero is Brownian at excursion age \(a\). If no reset occurs in \((0,s)\), its covariance with the force at \(s\) is \(2Da\); after a reset it is zero because subsequent Brownian excursions are independent and mean zero. Hence, for \(s\ge0\),

\[
C_L(s)=\frac{2D}{m}\mathbb E\int_0^{(L-s)_+}a\,da
=\frac Dm\mathbb E[(L-s)_+^2].
\]

Stationarity gives the even extension in \(s\). The finite second moment implies bounded, continuous covariance.

**2. Convex-order comparison.** For each \(s\ge0\), the function \(\ell\mapsto(\ell-s)_+^2\) is convex, so the covariance formula immediately yields pointwise ordering. For \(k\in L^1\), \(k\ge0\),

\[
\operatorname{Var}(Z_k)=\int_0^\infty\!\int_0^\infty k(u)k(v)C_L(u-v)\,du\,dv,
\]

which preserves that ordering. Every fixed-mean positive interval law dominates \(\delta_m\) in convex order by Jensen. For a nondegenerate law, \(\mathbb E L^2>m^2\), so the force-covariance comparison is strict at zero and, by continuity, on a neighborhood of zero. The harmonic kernel is strictly positive, making its variance ordering strict. This proves uniqueness of periodic resetting at fixed mean.

**3. Exact harmonic variance.** Symmetry of the covariance, Fubini's theorem, and a change of variables give

\[
\operatorname{Var}(X)=\int_0^\infty\!\int_0^\infty e^{-\mu(u+v)}C_L(u-v)\,du\,dv
=\frac1\mu\int_0^\infty e^{-\mu s}C_L(s)\,ds.
\]

Inserting the renewal covariance and integrating the elementary integral

\[
\int_0^L e^{-\mu s}(L-s)^2\,ds
=\frac{L^2}{\mu}-\frac{2L}{\mu^2}+\frac{2(1-e^{-\mu L})}{\mu^3}
\]

proves the clock functional. Its integrand after multiplication by \(\mu\) has second derivative \(2(1-e^{-\mu\ell})>0\) for \(\ell>0\), an independent strict-convexity proof. With fixed \(m\), take two-point intervals equal to \(m/2\) and \(M>m\), assigning the large value probability \(m/[2M-m]\); as \(M\to\infty\), their second moments and output variances diverge. Thus no finite upper bound exists.

**4. Sharp Poisson penalty.** Deterministic \(L=m\) immediately gives the periodic formula. For exponential \(L\) of mean \(m\), the covariance formula reduces to \(C_L(s)=2Dm e^{-|s|/m}\), and integration gives the Poisson formula. Let

\[
f(z)=z^2-2z+2(1-e^{-z})=\int_0^z e^{-u}(z-u)^2\,du>0.
\]

Set \(H(z)=(1+z)f(z)/z^3=2/R(z)\). Direct differentiation yields

\[
H'(z)=\frac{e^{-z}}{z^4}\left[(z^2-6)e^z+2z^2+6z+6\right]
=\frac{e^{-z}}{z^4}\sum_{n=4}^\infty\frac{(n-3)(n+2)}{n!}z^n>0.
\]

Therefore \(R'(z)<0\). The expansion \(f(z)\sim z^3/3\) at zero and \(f(z)\sim z^2\) at infinity give the two sharp endpoints.

## Verification

The standalone file `verify.py` checks the renewal covariance expression against independent numerical Laplace integration for discrete and exponential interval laws; checks the harmonic variance against a separate **uniform-phase average** based on the original paper's exact variance measured at reset epochs; verifies the Poisson result again through the stationary Markov moment equations; tests fixed-mean two-point spreads; and evaluates the strict ratio ordering over several scales. Run `python verify.py` from the extracted package. The code uses only the Python standard library.

As an exact algebraic independent check, integrate the within-cycle variance \(e^{-2\mu a}V_{\mathrm{epoch}}+D\mu^{-3}[2\mu a-3+4e^{-\mu a}-e^{-2\mu a}]\) over uniformly distributed phase \(0\le a<m\), where \(V_{\mathrm{epoch}}=D\mu^{-3}[2z-3+4e^{-z}-e^{-2z}]/(1-e^{-2z})\). Its result is exactly \(V_{\mathrm{per}}\), not the reset-epoch variance. The analytic proof, rather than finite numerical tests, establishes the infinite-domain statements.

## Relationship to prior work

Guéneau, Majumdar, and Schehr (2023) introduce the resetting-noise harmonic model, its Kesten recursion, the *reset-epoch* Gaussian variance for periodic driving (their equation 11), and time-stationary statistics for Poisson driving (their section 4). Their periodic result is not a uniform-phase stationary-time variance, and their two fixed reset protocols do not establish optimization over all renewal laws. Prior stationary-renewal Brownian autocovariance formulas, including an earlier result on the unique minimum of **finite-window time averages** under deterministic resetting, already cover the renewal covariance and its elementary convexity mechanism. Taźbierski, Metzler, and Magdziarz (2025) separately establish a general two-time covariance framework for completely renewal-reset processes. Neither such general formula nor the finite-window averaging optimum is asserted as new here. The assessed additional conclusion is the *unreset harmonic response* clock functional and, decisively, the explicit sharp Poisson-to-periodic variance penalty with strict monotonicity and endpoint factors \(6\) and \(2\), a different infinite-horizon exponential-response observable not stated in the checked sources.

The 2025 renewal-resetting framework derives general autocorrelation identities for reset Brownian processes, but its fully available article discusses resets of the stochastic process and first-passage optimization rather than the persistent harmonic response or the strict monotone \(2\)-to-\(6\) variance ratio. The convex-order optimality here is a consequence of the already-known renewal covariance and is presented as supporting context, not an independently original structural principle. General renewal-resetting surveys describe equilibrium age and arbitrary reset-time laws but do not supply this model-specific ordering or ratio. The distinction from alternating-renewal telegraph forcing is also material: Brownian excursions have increasing variance with their age and no deterministic sign alternation; no telegraph covariance formula directly implies the Brownian-excursion identity. Prior renewal formulas and convex-order tools are acknowledged ingredients rather than claimed innovations.

## Limitations

The comparison concerns stationary **second moments** and nonnegative linear-response kernels; it does not assert stochastic ordering of full position distributions, arbitrary signed filters, finite-time optimality, or optimality when reset intervals are dependent. Brownian excursions are independent across resets and have constant diffusivity. Fixed mean is the constraint; there is no reset-energy budget or finite-duration reset operation. The lack of a finite upper variance bound is for the unrestricted interval laws specified above. The covariance and periodic-clock minimization ingredients are not claimed as novel. The ratio theorem may be implicit in general prior formulae, and its publication priority remains a residual risk despite the inspected comparisons.

## References

1. M. Guéneau, S. N. Majumdar, and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453v1 (first public 2023-06-15), J. Phys. A: Math. Theor. 56, 475002 (2023). https://arxiv.org/abs/2306.09453 ; full text https://arxiv.org/html/2306.09453v2 .
2. K. Taźbierski, R. Metzler, and M. Magdziarz, *Series representation approach to stochastic processes with complete and incomplete renewal resetting*, New J. Phys. 27, 074603 (2025). https://doi.org/10.1088/1367-2630/adee40 ; freely readable text https://www.researchgate.net/publication/393582214_Series_representation_approach_to_stochastic_processes_with_complete_and_incomplete_renewal_resetting .
3. M. R. Evans, S. N. Majumdar, and G. Schehr, *Stochastic Resetting and Applications*, J. Phys. A: Math. Theor. 53, 193001 (2020), arXiv:1910.07993. https://arxiv.org/abs/1910.07993 .
