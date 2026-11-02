# Gaussian-projection rigidity for linear systems driven by Poisson-reset Brownian baths

## Finding

**Theorem (covariance-blind fourth-moment obstruction).** Consider a stationary, exponentially stable finite-dimensional real linear system driven by finitely many mutually independent Brownian processes that are individually reset to zero at independent positive-rate Poisson times, plus any independent centered Gaussian forcing. Every real linear stationary readout is a centered **Gaussian variance mixture**. Such a readout is Gaussian (possibly degenerate) **if and only if** its deterministic impulse response to every positive-diffusivity resetting bath vanishes identically. Otherwise its fourth cumulant is strictly positive, its characteristic function is positive and completely monotone as a function of squared frequency, its density is symmetric and strictly decreasing away from zero, and *every* normalized even moment of order at least four strictly exceeds that of the covariance-matched Gaussian readout.

In particular, replacing the resetting baths by stationary Ornstein--Uhlenbeck baths of exactly the same two-time covariances preserves **all** stationary second-order correlations of the linear system, but strictly underestimates every even one-point readout moment of order at least four whenever that readout sees a resetting bath. For the finite fixed-end nearest-neighbor harmonic chain with positive spring, mass, and boundary damping parameters, every individual oscillator velocity sees either positive-diffusivity boundary bath and therefore has strictly positive stationary excess kurtosis at every finite chain size, including when additional independent Langevin thermal reservoirs are present.

## Assumptions and scope

Let \(d,J\geq1\), \(A\in\mathbb R^{d\times d}\) be Hurwitz, \(b_j,c\in\mathbb R^d\), and \(B\) be a real \(d\times m\) matrix (\(m\geq0\)). On the whole time line consider the stationary solution of
\[
 dZ_t=AZ_t\,dt+\sum_{j=1}^J b_jX_j(t)\,dt+B\,dW_0(t),\qquad Y_t=c^\top Z_t.
\]
Here \(W_0\) is a standard multivariate Brownian motion independent of the other sources. For each \(j\), the real process \(X_j\) follows \(dX_j=\sqrt{2D_j}\,dW_j\) between independent rate-\(r_j\) Poisson resets \(X_j\mapsto0\), with \(r_j,D_j>0\). All Brownian motions and Poisson clocks are mutually independent, and the processes are in their stationary two-sided versions. A nonzero constant mean can be subtracted; the claim concerns centered readouts.

Put \(h_j(s)=c^\top e^{As}b_j\) for \(s\geq0\), and \(\sigma_0^2=\int_0^\infty\|c^\top e^{As}B\|^2\,ds\). Each \(h_j\) is real analytic, exponentially decaying and integrable. The stationary readout variance is
\[
 \sigma^2=\sigma_0^2+\sum_{j=1}^J\frac{2D_j}{r_j}
 \int_0^\infty\!\int_0^\infty h_j(s)h_j(t)e^{-r_j|s-t|}\,ds\,dt.
\]
The Gaussian comparison bath is \(dU_j=-r_jU_j\,dt+\sqrt{4D_j}\,d\widetilde W_j\) in stationarity, independent between \(j\). Its covariance equals that of \(X_j\), namely \(2D_jr_j^{-1}e^{-r_j|t-s|}\). The comparison output \(Y_t^{\rm OU}\) is centered Gaussian with variance \(\sigma^2\), and has the same full two-time covariance as \(Y_t\).

For every reset clock, partition \(( -\infty,0]\) into consecutive intervals \(I=(a_I,b_I]\), with \(b_I\) the next reset or time zero. Define its clock-dependent conditional-variance functional
\[
 \mathcal V_j=2D_j\sum_{I}\int_{a_I}^{b_I}
 \left(\int_u^{b_I}h_j(-t)\,dt\right)^2\,du,
 \qquad \mathcal V=\sigma_0^2+\sum_j\mathcal V_j.
\]
All sums and moments in the assertions converge. Explicitly, for every integer \(q\geq1\),
\[
 \mathbb E[Y_0^{2q}]=(2q-1)!!\,\mathbb E[\mathcal V^q],\qquad
 \mathbb E[Y_0^{2q+1}]=0,
\]
\[
 \boxed{\ \operatorname{cum}_4(Y_0)
 =3\operatorname{Var}(\mathcal V)=3\sum_{j=1}^J\operatorname{Var}(\mathcal V_j).\ }
\]
Each \(\operatorname{Var}(\mathcal V_j)\) is strictly positive exactly when \(h_j\not\equiv0\). Consequently, if any response is nonzero, for every integer \(q\geq2\),
\[
 \boxed{\ \mathbb E[Y_0^{2q}]>(2q-1)!!\,\sigma^{2q}
 =\mathbb E[(Y_0^{\rm OU})^{2q}].\ }
\]
If all responses vanish, equality holds at all orders and \(Y_0\) is Gaussian. The strict Gaussianity classification applies only to linear instantaneous readouts of this stable system, not to nonlinear current or energy observables.

## Proof

**1. Stationary responses and covariance matching.** Since \(A\) is Hurwitz, variation of constants gives
\[
 Y_0=\int_{-\infty}^0 c^\top e^{-At}B\,dW_0(t)
 +\sum_j\int_{-\infty}^0h_j(-t)X_j(t)\,dt.
\]
The first term is an independent centered Gaussian of variance \(\sigma_0^2\). The resetting Brownian bath has stationary variance \(2D_j/r_j\). For a lag \(\tau\), only the event of no reset between the two observation times contributes a nonzero covariance; hence
\[
 \mathbb E[X_j(t)X_j(t+\tau)]=\frac{2D_j}{r_j}e^{-r_j|\tau|}.
\]
The stated stationary OU replacement has exactly this covariance. Linear filtering therefore yields the asserted equality of readout variances and of all two-time covariance functions, with the displayed double integral.

**2. Conditional variance as a positive reset-interval sum.** Condition on all reset times. On each interval \(I=(a_I,b_I]\), the source has the representation \(X_j(t)=\sqrt{2D_j}(W_j(t)-W_j(a_I))\). Stochastic Fubini, first for finitely truncated intervals and then in \(L^2\), gives
\[
 \int_{a_I}^{b_I}h_j(-t)X_j(t)\,dt
 =\sqrt{2D_j}\int_{a_I}^{b_I}
 \left(\int_u^{b_I}h_j(-t)\,dt\right)dW_j(u).
\]
These integrals are independent centered Gaussians conditional on the clock, with variances given by the interval terms in \(\mathcal V_j\). The independent Gaussian thermal term contributes its fixed variance. Therefore \(Y_0\mid\{\text{reset clocks}\}\sim N(0,\mathcal V)\). Its conditional characteristic function is \(e^{-k^2\mathcal V/2}\), which proves both the moment identities and the unconditional formula \(\varphi_Y(k)=\mathbb E[e^{-k^2\mathcal V/2}]>0\). The latter is a Laplace transform in \(k^2/2\), hence completely monotone there.

All positive moments are finite: at a stationary time, each \(X_j\) is a centered Laplace variable with all absolute moments, and the exponentially decaying impulse responses permit Minkowski's inequality in every finite \(L^p\). Gaussian conditional moments and independence of the clocks now yield the exact fourth-cumulant decomposition, including the case of nonzero Gaussian thermal forcing.

**3. Nondegeneracy of the conditional variance.** It remains to verify the strict assertion, which does not follow from covariance matching alone. If \(h_j\equiv0\), then \(\mathcal V_j=0\). Conversely let \(h_j\not\equiv0\). By analyticity and continuity, choose \(a<c<b<0\) in a short interval on which \(f(t)=h_j(-t)\) has one strict sign. Suppose a reset interval has endpoints \(a,b\). Insert one additional reset at \(c\), keeping the exterior clock and endpoints fixed. The difference of the *unscaled* conditional variance contributions (no inserted reset minus inserted reset) equals
\[
 \int_a^c\left[Q^2+2Q\int_u^c f(t)\,dt\right]du,
 \qquad Q=\int_c^b f(t)\,dt.
\]
Since \(f\) has a fixed nonzero sign on \([a,b]\), this expression is strictly positive. Poisson configurations with endpoint resets in sufficiently small neighborhoods of \(a,b\) and either no interior reset or exactly one near \(c\) each have positive probability. Conditioning on the exterior points gives a strictly different conditional variance between these two events. Therefore \(\mathcal V_j\) is not almost surely constant and \(\operatorname{Var}(\mathcal V_j)>0\). The \(\mathcal V_j\) are independent because the clocks are independent, so their variances add without cancellation.

When any response is nonzero, the positive conditional-variance sum is almost surely nonzero. The density is a mixture of centered Gaussian densities with strictly positive variances. Every Gaussian component decreases strictly on the positive half-line, so their mixture is symmetric and strictly decreasing there. Strict Jensen inequality for \(x\mapsto x^q\), \(q\geq2\), establishes the complete even-moment hierarchy. If every response vanishes, only the Gaussian thermal term remains; this proves both directions of the Gaussianity criterion.

**4. Finite-chain corollary.** For a uniform fixed-end chain of \(N\geq2\) oscillators, take positive mass \(m\), spring constant \(k\), and boundary damping \(\gamma\). Its displacements obey
\[
 m\ddot x+\gamma(e_1e_1^\top+e_Ne_N^\top)\dot x
 +kL_N x=k(e_1X_1+e_NX_N)+\xi,
\]
where \(L_N\) has diagonal \(2\), adjacent off-diagonal \(-1\), and all other entries zero. The independent centered Langevin forcing \(\xi\) may have any finite nonnegative covariance matrix. The fixed-end stiffness is positive definite; boundary damping and connectivity give exponential stability, since no nontrivial undamped normal mode can have a zero first component. For velocity at site \(\ell\), its left-wall transfer function at Laplace frequency \(s>0\) is
\[
 H_{\ell 1}(s)=ks\,e_\ell^\top
 [ms^2I+\gamma s(e_1e_1^\top+e_Ne_N^\top)+kL_N]^{-1}e_1.
\]
The matrix in brackets is an irreducible nonsingular \(M\)-matrix for every \(s>0\), so its inverse has strictly positive entries and \(H_{\ell1}(s)>0\). Thus the left-wall impulse response is not identically zero for any site; likewise for the right wall. The theorem gives \(\operatorname{cum}_4(v_\ell)>0\) whenever either wall has \(D_j>0\), for every finite \(N\), every site, every pair of positive reset rates and arbitrary additional independent thermal noises. The same result holds for \(N=1\) with the evident single-oscillator equation.

## Verification

The accompanying `verify.py` constructs stationary polynomial-generator equations for the single-pole test system \(dY=(-aY+X)dt\), where \(X\) is rate-\(r\), diffusivity-\(D\) resetting Brownian noise. It independently gives
\[
 \mathbb E[Y^2]=\frac{2D}{ar(a+r)},\qquad
 \operatorname{cum}_4(Y)=\frac{24D^2(3a+7r)}{ar^2(a+r)^2(2a+r)(3a+r)},
\]
which is positive for \(a,r,D>0\) and agrees with the general conditional-variance identity. For \(a=r=D=1\), it verifies \(\mathbb E[Y^2]=1\), \(\mathbb E[Y^4]=8\), and fourth cumulant \(5\). It also checks exact positivity of the finite-chain transfer resolvent for several nontrivial chain sizes and rational positive parameters. These computations are checks, not a substitute for the all-parameter proof above.

Run `python verify.py` with Python 3 and SymPy installed. The script has no data files or network dependencies.

## Relationship to prior work

Sarkar and Roy's *Stationary state of harmonic chains driven by boundary resetting* (arXiv:2307.06127v1, first public date 2023-07-12) introduces the boundary-reset Brownian harmonic-chain model, analyzes its two-point correlations, and reports numerical non-Gaussianity and positive velocity kurtosis for specific finite chains, including an observed \(N^{-1}\) bulk scaling. Those physical observations and model definitions are not new here. The present result is a uniform exact **Gaussian-projection criterion for arbitrary stable finite linear networks**, an all-even-moment strict inequality against covariance-matched Gaussian baths, and strict shape/characteristic-function constraints that do not follow merely from a plotted kurtosis profile.

Sarkar, Santra and Basu's *Stationary states of activity-driven harmonic chains* (arXiv:2210.09035) gives the linear Green-function response framework and discusses Gaussian Ornstein--Uhlenbeck versus bounded non-Gaussian active baths. Guéneau, Majumdar and Schehr's *Active particle in a harmonic trap driven by a resetting noise* (arXiv:2306.09453) derives single-particle resetting-noise distributions and conditional Gaussian recursion. Single-filter moments and the covariance-matching observation are established background, not claimed as original. None of these works, in the relevant full-text passages checked, states the all-projection if-and-only-if criterion, strict reset-clock variance formula for finite networks, or complete even-moment and unimodality consequences. The general Gaussian scale-mixture and Jensen ingredients themselves are standard; the contribution claimed here is their rigorous combination with the strict Poisson-clock condition and the resulting universal network-level comparison.

## Limitations

The result concerns finite-dimensional exponentially stable **linear** systems, independent Poisson reset clocks, Brownian excursions reset to zero, and linear instantaneous readouts. It does not imply that nonlinear energy-current observables are Gaussian mixtures, prove the numerical \(N^{-1}\) rate conjecture, establish any uniform positive lower bound on excess kurtosis as the network size grows, or describe non-Poisson resetting without further proof. The strictness conclusion can fail when a readout has zero transfer from every resetting bath; the comparison also fails if thermostat noise depends on reset clocks. The numerical checker tests special instances and is not an infinite proof. Definitive publication priority has not been independently certified.

## References

1. R. Sarkar and P. Roy, *Stationary state of harmonic chains driven by boundary resetting*, arXiv:2307.06127v1 (2023), https://arxiv.org/abs/2307.06127 ; full text https://arxiv.org/html/2307.06127v3 .
2. R. Sarkar, I. Santra and U. Basu, *Stationary states of activity-driven harmonic chains*, arXiv:2210.09035 (2022), https://arxiv.org/html/2210.09035v3 .
3. M. Guéneau, S. N. Majumdar and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453 (2023), https://arxiv.org/html/2306.09453v2 .
