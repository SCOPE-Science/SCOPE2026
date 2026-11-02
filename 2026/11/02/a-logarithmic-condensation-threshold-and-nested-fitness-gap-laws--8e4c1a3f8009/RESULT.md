# A logarithmic condensation threshold and nested fitness-gap laws under local resetting

## Finding

In a locally reset non-conserving zero-range process, logarithmic factors multiplying a linearly vanishing high-fitness reset rate create a sharp **second condensation threshold**. Suppose that, as \(u\downarrow0\), the resetting rate satisfies
\[
r(1-u)\sim c\,u[\log(1/u)]^\theta,\qquad c>0,\quad\theta\in\mathbb R.
\]
As the excess combined death-and-hopping rate \(\zeta=\beta+\delta-1\downarrow0\), the stationary mean particle density diverges exactly when \(\theta\le1\); for \(\theta>1\) it has a finite limit. Thus the exponent of the algebraic factor \(u\) alone does **not** determine condensation at the marginal boundary.

More precisely, define
\[
H_\zeta(l)=\zeta+1-l+r(l),\quad
I_\zeta=\int_0^1\frac{l\,dl}{H_\zeta(l)},\quad
J_\zeta=\int_0^1\frac{q(l)\,dl}{H_\zeta(l)},\quad
J_0=\int_0^1\frac{q(l)\,dl}{1-l+r(l)}.
\]
Writing \(L=\log(1/\zeta)\), the exact leading asymptotics are
\[
I_\zeta\sim
\begin{cases}
L,&\theta<0,\\
L/(1+c),&\theta=0,\\
L^{1-\theta}/[c(1-\theta)],&0<\theta<1,\\
(\log L)/c,&\theta=1.
\end{cases}
\]
For \(\theta>1\), \(I_\zeta\to I_0<\infty\). In every case the stationary mean density is exactly \(\rho_\zeta=I_\zeta/(1-\beta J_\zeta)\), and \(J_\zeta\to J_0<\infty\).

The limit for the **normalized stationary particle-fitness distribution** \(\mu_\zeta\) is, when \(\theta\le1\),
\[
\mu_\zeta\Rightarrow (1-\beta J_0)\delta_1+
\frac{\beta q(l)}{1-l+r(l)}\,dl.
\]
For \(\theta>1\) there is no endpoint atom: the limiting law is the absolutely continuous probability measure with density
\[
\frac{1-\beta J_0}{I_0}\frac{l}{1-l+r(l)}
+\frac{\beta q(l)}{1-l+r(l)}.
\]

There are also **universal multiscale descriptions of the condensate**, invisible in the weak convergence on fitness space. Let \(X_\zeta\) have law \(\mu_\zeta\) and set
\[
U_\zeta=\frac{\log[1/(1-X_\zeta)]}{\log(1/\zeta)}.
\]
For \(\theta<1\),
\[
U_\zeta\Rightarrow \beta J_0\delta_0+(1-\beta J_0)\mathsf B_\theta,
\]
where \(\mathsf B_\theta\) is uniform on \([0,1]\) for \(\theta\le0\), and has cumulative distribution \(t^{1-\theta}\) for \(0\le t\le1\) when \(0<\theta<1\) (a beta law with shape parameters \((1-\theta,1)\)).

At the doubly marginal point \(\theta=1\), \(U_\zeta\) instead converges to \(\delta_0\). A second logarithm restores a nondegenerate universal law. Put
\[
V_\zeta=\frac{\log\bigl[1+\log(1/(1-X_\zeta))\bigr]}
{\log[1+\log(1/\zeta)]}.
\]
Then
\[
V_\zeta\Rightarrow \beta J_0\delta_0+(1-\beta J_0)\mathrm{Uniform}[0,1].
\]
The assertions hold for every profile and rate satisfying the assumptions below, not just for a specially chosen explicit example.

## Assumptions and scope

The underlying process is the continuum-fitness mean-field limit of the fully connected, locally reset, non-conserving zero-range model with extensive creation, annihilation, and hopping rates considered in the cited 2023 source. Fitness is \(l\in[0,1]\); particles are created by fitness-dependent rates, die at rate \(\delta>0\), hop at rate \(\beta>0\), and sites at fitness \(l\) reset independently to zero occupancy at rate \(r(l)\). The density \(q\) of fitness levels is nonnegative with \(\int_0^1q(l)dl=1\) and \(q(1-u)=O(u^\alpha)\) for some \(\alpha>0\).

Assume \(r:[0,1]\to[0,\infty)\) is measurable and bounded, with the stated marginal logarithmic asymptotics for some fixed real \(\theta\) and \(c>0\). Take fixed
\[
0<\beta<\min\{1,J_0^{-1}\},\qquad
\delta=1+\zeta-\beta>0,
\]
and let \(\zeta\downarrow0\). The integral \(J_0\) is finite and strictly positive under the assumptions. All limits refer to stationary mean profiles in the continuum mean-field model, not finite-network limits or random realizations of the condensate population.

## Proof

**1. Stationary decomposition.** The established stationary mean-occupation formula is
\[
n_\zeta(l)=\frac{l+\beta\rho_\zeta q(l)}{H_\zeta(l)},
\qquad \rho_\zeta=\int_0^1 n_\zeta(l)\,dl.
\]
Integrating gives \(\rho_\zeta=I_\zeta+\beta\rho_\zeta J_\zeta\), so \(\rho_\zeta=I_\zeta/(1-\beta J_\zeta)\). Since \(0\le J_\zeta\le J_0\) and \(\beta J_0<1\), the stationary normalization is positive for every \(\zeta>0\). The particle-fitness law decomposes **exactly** as
\[
\mu_\zeta=(1-\beta J_\zeta)\nu_\zeta
+\frac{\beta q(l)}{H_\zeta(l)}dl,
\qquad
\nu_\zeta(dl)=\frac{l}{I_\zeta H_\zeta(l)}dl.
\]
The second component has mass \(\beta J_\zeta\). Since \(H_\zeta(l)\ge1-l\), the integrand \(q(l)/H_\zeta(l)\le q(l)/(1-l)\) is integrable by the endpoint assumption, proving \(J_\zeta\to J_0\) by dominated convergence.

**2. A logarithmic integral comparison.** Set \(u=1-l\), \(s=\log(1/u)\), and \(L=\log(1/\zeta)\). The exact integral becomes
\[
I_\zeta=\int_0^\infty
\frac{1-e^{-s}}{1+R(s)+e^{s-L}}\,ds,
\qquad R(s)=e^s r(1-e^{-s})\sim c s^\theta.
\]
For \(\theta\le1\), the divergent part comes from \(1\ll s\ll L\). To justify replacing its integrand by \([1+c s^\theta]^{-1}\), fix \(\varepsilon\in(0,1)\), split at \(s=S\), \((1-\varepsilon)L\), and \((1+\varepsilon)L\), and then let \(S\to\infty\), \(L\to\infty\), and \(\varepsilon\downarrow0\) in that order. Uniformity of \(R(s)/(c s^\theta)\to1\) holds on \([S,\infty)\); the factor \(e^{s-L}\) is uniformly negligible below \((1-\varepsilon)L\). The interval around \(L\) contributes at most a fraction tending to zero as \(\varepsilon\downarrow0\) for each exponent \(\theta<1\); when \(\theta=1\), its contribution is bounded while the leading \(\log L\) diverges. The tail above \((1+\varepsilon)L\) is bounded by \(\int_{(1+\varepsilon)L}^\infty e^{L-s}ds\). This gives the same leading integral as \(\int_1^L[1+c s^\theta]^{-1}ds\), and ordinary integral comparison yields all four stated asymptotics. For \(\theta>1\), \([1+R(s)]^{-1}\) is integrable at infinity, and the displayed exact formula yields a finite limit by dominated convergence.

**3. Macroscopic fitness limit.** When \(I_\zeta\to\infty\), for each fixed \(l_0<1\), the numerator \(\int_0^{l_0} l/H_\zeta(l)dl\) stays bounded. Hence \(\nu_\zeta\Rightarrow\delta_1\). The exact decomposition and convergence of the background component prove the claimed condensate law, with mass \(1-\beta J_0>0\). For \(\theta>1\), dominated convergence gives \(\nu_\zeta\) the density \(l/[I_0(1-l+r(l))]\), and adding the background gives the claimed absolutely continuous law.

**4. First logarithmic magnification.** For \(\theta<1\), the push-forward of \(\nu_\zeta\) by \(s\mapsto s/L\) has interval probabilities obtained from the ratio of the previous logarithmic integral restricted to \(s\in[aL,bL]\) to the full \(I_\zeta\). For each \(0<a<b<1\), the limiting ratio is \(b-a\) when \(\theta\le0\), and \(b^{1-\theta}-a^{1-\theta}\) when \(0<\theta<1\). Tightness at the endpoints follows from the same comparison and the exponentially small tail above \((1+\varepsilon)L\). The background law has a finite limiting measure on \([0,1)\), so its logarithmic coordinate converges to zero. Combining the exact component weights proves the mixture law.

**5. Double-logarithmic magnification at the second threshold.** When \(\theta=1\), the restricted origin contribution on \(s\in[(1+L)^a-1,(1+L)^b-1]\), for \(0<a<b<1\), is asymptotic to \((b-a)\log L/c\). Division by \(I_\zeta\sim\log L/c\) gives the uniform law in the \(V_\zeta\) coordinate. On the first coordinate, any fixed interval \(s\in[aL,L]\), \(a>0\), has only bounded mass against the diverging \(\log L\), proving \(U_\zeta\Rightarrow\delta_0\). The background again collapses to zero. These arguments cover all parameters and establish the limits, rather than extrapolating from numerical samples.

## Verification

The accompanying `verification.py` numerically reconstructs the stationary integrals for the explicit, admissible example \(q(l)=2(1-l)\), \(\beta=0.1\), \(c=0.4\), and \(r(1-u)=0.4u[1+\log(1/u)]^\theta\). It checks the exact elementary formulas for \(\theta=0\), exact mass conservation in the stationary mixture, divergence classes, the beta-limit cumulative distributions, the double-logarithmic limit, and convergence in the noncondensing regime. The 46 deterministic checks passed when run with Python 3 and SciPy. They provide numerical corroboration only; the proof above supplies the infinite-parameter result.

## Relationship to prior work

Grange's 2023 work [1] derives the general stationary profiles and treats the three **pure power-law** high-fitness reset cases \(r(1-u)\sim c u^\nu\), including the strictly linear case \(\nu=1\). The present finding **does not claim** those formulas or the standard logarithmic divergence for strictly linear reset rates. It studies the marginal class with a nonconstant slowly varying logarithmic factor, where the pure-power case split no longer distinguishes condensation from finite density, and resolves the full first-logarithm and second-logarithm fitness-gap distributions. Grange's earlier nonresetting [2] and globally resetting [3] models have different resetting mechanisms and do not state the corresponding local logarithmic-edge classification. Yuan's random-mutation Kingman models [4] treat random mutation probabilities, not fitness-local resetting with this boundary-layer law.

## Limitations

This is a theorem about the stationary continuum mean profile, and it does not establish a finite-site condensate law, empirical convergence rates, arbitrary subpolynomial rate fluctuations without the asserted asymptotic equivalence, or fluctuations of the occupation numbers. The logarithmic-gap distributions describe particle fractions sampled from the normalized stationary *mean* density. As with other results derived from explicit mean profiles, the existence of an applicable general renewal or regular-variation theorem may reduce its publication novelty; no universal publication-priority guarantee is claimed.

## References

[1] P. Grange, *Local resetting in non-conserving zero-range processes with extensive rates*, arXiv:2311.12414 (first public 21 November 2023), https://arxiv.org/abs/2311.12414 . Stationary equations (41), (42), (44); Section 5.2 pure-power classification.

[2] P. Grange, *Steady states in a non-conserving zero-range process with extensive rates as a model for the balance of selection and mutation*, arXiv:1904.05604 (2019), https://arxiv.org/abs/1904.05604 .

[3] P. Grange, *Non-conserving zero-range processes with extensive rates under resetting*, arXiv:1910.05991 (2019), https://arxiv.org/abs/1910.05991 .

[4] L. Yuan, *Kingman's model with random mutation probabilities: convergence and condensation I*, arXiv:2001.07033 (2020), https://arxiv.org/abs/2001.07033 .
