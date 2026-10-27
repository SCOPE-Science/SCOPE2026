# Joint critical-field diffusion and passage-time laws for nonlinear voter dynamics with zealots

## Finding
Fix an integer \(q\geq2\). For populations of size \(N\) in the complete-graph nonlinear \(q\)-voter process, let \(S_N\) be the number of susceptible voters and \(Z_{+,N},Z_{-,N}\) the counts of permanently fixed positive and negative zealots. Suppose
\[
S_N+Z_{+,N}+Z_{-,N}=N,\quad
\frac{S_N-N/q}{\sqrt N}\longrightarrow\theta\in\mathbb R,\qquad
\frac{Z_{+,N}-Z_{-,N}}{N^{1/4}}\longrightarrow\eta\in\mathbb R.
\]
Both zealot types must have positive counts for all sufficiently large \(N\). Let \(K_N(t)\) count positive susceptible voters and set
\[
X_N(t)=\frac{K_N(\sqrt N\,t)-S_N/2}{N^{3/4}}.
\]
If \(X_N(0)\) converges in distribution to a finite random variable \(X_0\), the processes \(X_N\) converge on every bounded time interval (in Skorokhod space) to the unique nonexplosive diffusion
\[
dX_t=b_{q,\theta,\eta}(X_t)\,dt+\sqrt{2^{-q}/q}\,dW_t,
\quad b_{q,\theta,\eta}(x)=2^{1-q}q\theta x+2^{-q}\eta-\frac{2^{3-q}(q^2-1)}3x^3.
\]
The finite-chain stationary laws, rescaled as above, converge with all polynomial moments to the diffusion's unique invariant density
\[
f_{q,\theta,\eta}(x)=\frac{1}{\mathcal Z}\exp\left(2q^2\theta x^2+2q\eta x-\frac{4q(q^2-1)}3x^4\right),\quad x\in\mathbb R,
\]
where \(\mathcal Z\) is its integral over the real line. The convergence also holds for stationary processes.

For any \(a<b\), start at lattice states whose scaled positions tend to \(a\) or \(b\), respectively; write \(H_N^+\) for the first time to reach the smallest lattice state at or above scaled level \(b\) when starting near \(a\), and \(H_N^-\) for the analogous first time to reach the largest state at or below \(a\) from near \(b\). These hitting times are measured in the original time units, before the \(\sqrt N\) acceleration. With \(\sigma_q^2=2^{-q}/q\) and \(F(x)=\int_{-\infty}^x f_{q,\theta,\eta}(u)\,du\),
\[
\frac{\mathbb E H_N^+}{\sqrt N}\longrightarrow
\frac{2}{\sigma_q^2}\int_a^b\frac{F(x)}{f_{q,\theta,\eta}(x)}\,dx,
\qquad
\frac{\mathbb E H_N^-}{\sqrt N}\longrightarrow
\frac{2}{\sigma_q^2}\int_a^b\frac{1-F(x)}{f_{q,\theta,\eta}(x)}\,dx.
\]
Thus the critical density perturbation acts on the quadratic potential at scale \(\sqrt N\), the *absolute* zealot-count imbalance acts on its linear tilt at scale \(N^{1/4}\), and finite-threshold switching occurs on the \(\sqrt N\) time scale. These are two distinct simultaneous finite-size response windows.

## Assumptions and scope
A susceptible positive voter becomes negative only after \(q\) independently sampled other voters all express the negative opinion; conversely, a susceptible negative voter becomes positive after \(q\) sampled other voters all express the positive opinion. Sampling is with replacement, but excludes the updating voter. Each susceptible attempts an update at rate one. Hence the exact transition rates of \(K_N\), for \(0\le k\le S_N\), are
\[
B_N(k)=(S_N-k)\left(\frac{k+Z_{+,N}}{N-1}\right)^q,\qquad
D_N(k)=k\left(\frac{S_N-k+Z_{-,N}}{N-1}\right)^q.
\]
The first formula vanishes at \(k=S_N\); the second vanishes at \(k=0\). The positivity of both zealot types makes the finite chain irreducible and ensures its unique stationary law \(\pi_N\). No assumption of independence of voters in the stationary state is made. The transition rates are exact, not mean-field replacements.

The macroscopic parameter restrictions are fixed \(q\ge2\) and fixed finite real \(\theta,\eta\); \(N\) ranges over integers for which the displayed count constraints hold. The initial law for process convergence may be deterministic or random and is assumed only to converge after centering and scaling. Thresholds \(a,b\) are fixed finite real numbers with \(a<b\).

## Proof
**1. Exact reduction and the critical point.** The number of positive susceptibles is a birth-and-death chain with the displayed rates. Detailed balance gives the exact probability ratios
\[
\frac{\pi_N(k+1)}{\pi_N(k)}=
\frac{S_N-k}{k+1}\left(\frac{k+Z_{+,N}}{S_N-k-1+Z_{-,N}}\right)^q.
\]
Write \(s=S_N/N\), \(h=(Z_{+,N}-Z_{-,N})/(2N)\), \(y=(k-S_N/2)/N\). The continuum logarithmic ratio is
\[
\ell_{s,h}(y)=\log\frac{s/2-y}{s/2+y}
+q\log\frac{1/2+y+h}{1/2-y-h}.
\]
On any fixed neighborhood of zero, the difference between the exact log ratio and \(\ell_{s,h}(y)\) is \(O(N^{-1})\), uniformly for the stated sequences. For \(h=0\), its linear coefficient is \(4(q-1/s)\), so the critical susceptibility fraction is \(s_c=1/q\).

**2. Local potential and its global control.** Around the critical point, Taylor expansion yields
\[
\ell_{s,h}(y)=4(q-1/s)y+4qh-\frac{16q(q^2-1)}3y^3
+O\bigl(|y|^5+|s-s_c|\,|y|^3+|h|\,y^2+h^2\bigr).
\]
With \(y=xN^{-1/4}\), \(s=s_c+\theta N^{-1/2}+o(N^{-1/2})\), and \(h=\eta/(2N^{3/4})+o(N^{-3/4})\), summing log ratios from the central state to \(k\) gives, uniformly for \(x\) in compact sets,
\[
\log\frac{\pi_N(k)}{\pi_N(k_0)}
=2q^2\theta x^2+2q\eta x-\frac{4q(q^2-1)}3x^4+o(1),
\]
where \(k_0\) is the nearest integer to \(S_N/2\).

This local expansion cannot alone establish convergence of stationary laws. To control tails, at the unperturbed critical point use the identity
\[
\ell_{1/q,0}(y)=-2\operatorname{atanh}(2qy)+2q\operatorname{atanh}(2y).
\]
For \(0<y<1/(2q)\), strict convexity of \(\operatorname{atanh}\) on positive arguments implies \(\operatorname{atanh}(2qy)>q\operatorname{atanh}(2y)\); hence the logarithmic ratio has a strict restoring sign for every nonzero interior \(y\). Near zero its restoring term is cubic. Uniform perturbation bounds and summation of the exact log ratios consequently give a central-region estimate of the form
\[
\frac{\pi_N(k)}{\pi_N(k_0)}\le C\exp(-c|x|^4+C|x|^2+C|x|)
\]
with \(c,C>0\) independent of large \(N\); outside a small fixed neighborhood of the center the ratios decay exponentially in \(N\), and the boundary factors only reinforce the restoring direction. These bounds give tightness, Riemann-sum normalization, convergence to the stated invariant density, and uniform integrability of every polynomial moment.

**3. Critical generator and the path limit.** For \(f\in C_c^3(\mathbb R)\), the time-rescaled generator, with \(x=(k-S_N/2)/N^{3/4}\), is
\[
\mathcal L_N f(x)=\sqrt N\{B_N(k)[f(x+N^{-3/4})-f(x)]+D_N(k)[f(x-N^{-3/4})-f(x)]\}.
\]
Expanding the exact rates near their critical point yields uniformly on compact sets
\[
N^{-1/4}(B_N-D_N)\longrightarrow b_{q,\theta,\eta}(x),
\qquad N^{-1}(B_N+D_N)\longrightarrow\sigma_q^2.
\]
For example, the cubic coefficient in the rate difference is exactly \(-2^{3-q}(q^2-1)/3\), from the binomial expansion at \(s_c\). Therefore
\[
\mathcal L_N f\longrightarrow b_{q,\theta,\eta}f'+\tfrac12\sigma_q^2f''.
\]
The same global restoring-sign estimates imply a uniform bound \(\mathcal L_N(x^2)\le C\) for large \(N\); the positive variance term is bounded, and outside a bounded critical region the drift contribution is nonpositive up to a fixed additive constant. Stopping at \(|X_N|\ge R\) gives compact containment on finite time intervals. The vanishing jump sizes and local generator convergence establish tightness and identification of every limit as the martingale problem for the displayed diffusion. Its coefficients are locally Lipschitz and its cubic drift has a negative leading coefficient, so the martingale problem is well posed and nonexplosive. This gives process convergence for all convergent initial laws. Starting from the finite stationary laws and using the previous paragraph gives stationary process convergence. The limiting diffusion is irreducible, has constant positive noise, and its explicitly integrable speed density is proportional to the displayed quartic exponential; hence that invariant law is unique.

**4. Critical passage times.** For lattice states \(i<j\), the exact birth-and-death first-passage identity is
\[
\mathbb E_i H_j=\sum_{v=i}^{j-1}\frac{\sum_{u=0}^{v}\pi_N(u)}{B_N(v)\pi_N(v)},
\qquad
\mathbb E_j H_i=\sum_{v=i+1}^{j}\frac{\sum_{u=v}^{S_N}\pi_N(u)}{D_N(v)\pi_N(v)}.
\]
These follow by taking differences in the backward hitting-time equation and solving the resulting telescoping recurrence with the natural reflecting endpoint. Uniformly on compact critical positions, \(N^{3/4}\pi_N(k)\to f(x)\), the cumulative stationary probabilities converge to \(F(x)\), and \(B_N(k)/N,D_N(k)/N\to\sigma_q^2/2\). Dividing the exact identities by \(\sqrt N\) converts their sums into the two stated integrals. All summed indices between the fixed scaled thresholds remain in a compact critical window, so the local uniform limits suffice. This proves both mean passage-time limits without assuming convergence of expectations from weak process convergence.

## Verification
The standalone program `verify_critical_qvoter.py` computes the full finite-chain stationary probabilities from exact detailed-balance ratios and independently evaluates the original transition rates. It passed 368 individual finite-chain detailed-balance identities, 60 rescaled generator coefficient comparisons, 12 finite-distribution moment comparisons against the quartic density, and 18 finite-chain mean passage-time comparisons against the limiting quadrature, for 458 passed checks. The program also checks normalization and compares both passage directions. The checks use finite \(N\) and numerical quadrature; the proof of convergence and of uniqueness is analytical, not inferred from the tests.

To reproduce: install the packages in `requirements.txt`, then run `python verify_critical_qvoter.py` with Python 3. The code's tests use several \(q\)-values, population sizes, and perturbations of both signs. The finite-size comparison errors need not decrease monotonically because counts are rounded to integers.

## Relationship to prior work
Mobilia's 2015 analysis introduced the complete-graph nonlinear voter model with fixed zealots, derived its exact birth-death stationary product, and characterized the qualitative phase change and metastable switching (arXiv:1506.04911, especially Sections II–V). Those exact rates and product formulas are used and credited here; they are not new. Mellor, Mobilia, and Zia's later heterogeneous two-class analysis (arXiv:1610.06092, especially Section IV.E and the discussion) predicts the quartic Landau variance exponent at symmetric criticality and specifically describes the full finite-size critical scaling and unequal-zealot effects as outstanding. The symmetric \(N^{-1/2}\) variance exponent is therefore **prior art**, not a claimed discovery.

The assessed joint theorem instead gives explicitly the two different finite-population tuning scales, the exact coefficients of the *asymmetrically tilted* non-Gaussian limiting density for every fixed \(q\ge2\), a path-level cubic diffusion under its critical time rescaling, and the two directional mean switching-time quadratures. The 2015 exact stationary product makes the equilibrium part approachable, but extracting the joint limit requires quartic saddle-point analysis; it does not contain the dynamic weak-convergence or critical passage-time statements. The heterogeneous 2017 Landau analogy gives neither the field tilt coefficients nor the finite-chain critical diffusion and its passage limits. General near-critical birth-and-death diffusion approximation theorems are a potential conceptual reduction and remain a residual originality qualification.

## Limitations
The result is for the homogeneous complete-graph \(q\)-voter process with a fixed integer \(q\), two positive zealot populations, symmetric susceptibility within each opinion, and sampling with replacement excluding the focal voter. It does not settle universality for heterogeneous \(q\) types or sparse graphs, spectral-gap asymptotics, quantitative convergence rates in the weak-limit theorem, or barrier transitions at critical thresholds diverging with \(N\). Numerical finite-size checks cannot establish any of these omitted statements. A broad general theorem for density-dependent critical birth-and-death chains might imply parts of this calculation, so historical priority is not asserted conclusively.

## References
1. M. Mobilia, *Nonlinear q-voter model with inflexible zealots*, Physical Review E **92**, 012803 (2015), arXiv:1506.04911, first submitted June 16, 2015, https://arxiv.org/abs/1506.04911.
2. A. Mellor, M. Mobilia, and R. K. P. Zia, *A Heterogeneous Out-of-Equilibrium Nonlinear q-Voter Model with Zealotry*, Physical Review E **95**, 012104 (2017), arXiv:1610.06092, https://arxiv.org/abs/1610.06092.
3. T. G. Kurtz, *Solutions of ordinary differential equations as limits of pure jump Markov processes*, Journal of Applied Probability **7**, 49–58 (1970). Cited for the general generator-convergence context, not for the evaluated critical-field theorem.
