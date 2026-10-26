# Rescaling-invariant time-share distortion in successful fractional resetting excursions

## Finding
For a finite one-dimensional nearest-neighbor continuous-time random walk with two absorbing endpoints, complete Poisson resetting, and Mittag-Leffler holding times, the fractions of the *last successful excursion* spent in its successive holding intervals have a sharp non-Markovian correction. Conditional on absorption at either specified endpoint whose shortest route contains \(m\geq2\) jumps, the jump-count/time-share law converges in total variation to a shortest path marked by a symmetric \(m\)-coordinate Dirichlet law. For fractional exponent \(0<\beta<1\), the leading error is strictly positive and of order \((r\tau)^{-\beta}\), with an exact coefficient below. For the exponential endpoint \(\beta=1\), the intrinsic time-share error vanishes *exactly* and only rare two-jump detours survive, producing order \((r\tau)^{-2}\). This distinguishes a scale-invariant observable of anomalous trapping from the Markovian clock at high reset rates.

Specifically, let \(a=(r\tau)^{-\beta}\) and \(V=(W_1,\ldots,W_K)/(W_1+\cdots+W_K)\). Define
\[
A_{m,\beta}=\frac{\Gamma(\beta)\Gamma((m+1)\beta)}{\Gamma(2\beta)\Gamma(m\beta)},\qquad
C_{m,\beta}=\frac12\mathbb E_{U\sim\operatorname{Dirichlet}_m(\beta)}\left|m-A_{m,\beta}\sum_{j=1}^{m}U_j^\beta\right|.
\]
For every fixed \(0<\beta<1\), \(C_{m,\beta}>0\) and
\[
d_{\mathrm{TV}}\!\left(\mathcal L(K,V\mid S=z),\,\delta_m\otimes\operatorname{Dirichlet}_m(\beta)\right)=C_{m,\beta}a+O(a^2).
\]
More precisely the joint probability measure on the \(K=m\) stratum has the following signed expansion in total variation:
\[
\Pr(K=m,V\in dv\mid S=z)
=\operatorname{Dirichlet}_m(\beta)(dv)
\left[1+a\left(m-A_{m,\beta}\sum_{j=1}^m v_j^\beta\right)\right]+O_{\mathrm{TV}}(a^2).
\]
At \(\beta=1\), conditional on \(K=m\) the time-share law is exactly \(\operatorname{Dirichlet}_m(1)\) for every rate, and
\[
d_{\mathrm{TV}}\!\left(\mathcal L(K,V\mid S=z),\delta_m\otimes\operatorname{Dirichlet}_m(1)\right)
=\frac{c_{N,i,z}}4(r\tau)^{-2}+O((r\tau)^{-3}),
\]
where \(c_{N,i,0}=i-\mathbf1_{\{i=N-1\}}\) and \(c_{N,i,N}=N-i-\mathbf1_{\{i=1\}}\).

## Assumptions and scope
Fix integers \(N\ge3\), \(i\in\{1,\dots,N-1\}\), an absorbing endpoint \(z\in\{0,N\}\), \(\tau>0\), and \(\beta\in(0,1]\). A walker starts at \(i\), waits an independent strictly positive random time \(W\) with Laplace transform \(\mathbb E e^{-sW}=[1+(\tau s)^\beta]^{-1}\), jumps left or right with independent equal probability, and repeats until first reaching \(0\) or \(N\). Independent Poisson events with rate \(r>0\) completely reset position to \(i\) and renew the waiting clock; they do not terminate the experiment. Denote by \(S\) the absorbing endpoint eventually attained; both endpoints have strictly positive chance. The **last successful excursion** is the interval since the final reset (or initiation when no reset occurs) until absorption. Let \(K\) count its jumps, and \(W_1,\ldots,W_K\) be precisely its successive holding durations. The marked state space is the disjoint union \(\coprod_{k\ge1}\{k\}\times\Delta_{k-1}\), where \(\Delta_{k-1}=\{v_j>0,\sum_jv_j=1\}\); total-variation distance uses the standard supremum-over-events convention. Require shortest jump distance \(m=i\) for \(z=0\) and \(m=N-i\) for \(z=N\) to satisfy \(m\ge2\). All asymptotics take \(r\to\infty\) with \(N,i,z,\tau,\beta\) fixed; the constants in the remainders can depend on these fixed parameters.

## Proof
**Step 1: successful-excursion reduction.** In one independent attempt, every prescribed absorbing path of \(k\) nearest-neighbor steps has likelihood \(2^{-k}\prod_{j=1}^k\psi(w_j)e^{-rw_j}\,dw_j\), since the Poisson clock must not ring before the endpoint is reached. Failed attempts are independent and identically distributed after each complete reset, so conditioning on the eventual endpoint simply conditions the *final successful attempt* on hitting that endpoint before reset. Write
\[
h=\widehat\psi(r)=\frac{1}{1+(r\tau)^\beta}=\frac a{1+a}.
\]
A given successful \(k\)-step path receives weight \((h/2)^k\). Its \(k\) rescaled waits \(U_j=rW_j\), conditional on that path, are independent with probability density \(q_a\) and Laplace transform
\[
\widehat q_a(s)=\frac{\widehat\psi(r(1+s))}{\widehat\psi(r)}=\frac{1+a}{(1+s)^\beta+a}.
\]
The ordinary first-passage resolvent obtained by summing these weights is known; this proof instead retains the *individual waiting-time marks* absent from an aggregated first-passage transform.

**Step 2: uniform suppression of detours.** The unique shortest path from \(i\) to \(z\) has \(m\) steps. Every other allowable first-absorption path has at least \(m+2\) steps by parity. Its total absolute path weight is at most \(\sum_{k\ge m+2}2^k(h/2)^k=O(h^{m+2})\); the shortest weight is \((h/2)^m\), so
\[
\Pr(K\ne m\mid S=z)=O(h^2)=O(a^2).
\]
This simple bound is uniform for fixed \(N,i,z\) and all sufficiently small \(a\).

**Step 3: an exact signed Gamma mixture.** For \(0<a<1\), the geometric-series identity and uniqueness of Laplace transforms yield an absolutely convergent expansion of finite signed measures
\[
q_a(u)\,du=(1+a)\sum_{j=1}^\infty(-a)^{j-1}\,\operatorname{Gamma}(j\beta,1)(du).
\]
Absolute convergence in total variation follows from summing the absolute weights; in particular
\[
q_a= g_\beta+a(g_\beta-g_{2\beta})+O_{L^1}(a^2),
\qquad g_t(u)=\frac{u^{t-1}e^{-u}}{\Gamma(t)}.
\]
For any fixed \(m\), taking the product of the \(m\) densities yields
\[
q_a^{\otimes m}=g_\beta^{\otimes m}
+a\sum_{j=1}^m\left(g_\beta^{\otimes m}-g_\beta^{\otimes(j-1)}\otimes g_{2\beta}\otimes g_\beta^{\otimes(m-j)}\right)+O_{L^1}(a^2).
\]
The map from positive waits to their normalized time shares is measurable and contracts total variation. Equal-rate independent Gamma variables have a Dirichlet law of their normalized proportions. For the term with a single \(2\beta\) shape, the Dirichlet density relative to the all-\(\beta\) base is \(A_{m,\beta}v_j^\beta\) with the displayed constant. Combining this with Step 2 gives the stated signed expansion; taking total variation of a zero-mass first-order signed density yields exactly \(C_{m,\beta}a+O(a^2)\). The \(O(a^2)\) is a norm bound rather than a pointwise claim near simplex faces.

**Step 4: positivity and the Markovian transition.** Standard Dirichlet moments give \(\mathbb E[U_j^\beta]=\Gamma(2\beta)\Gamma(m\beta)/[\Gamma(\beta)\Gamma((m+1)\beta)]=1/A_{m,\beta}\), so the signed correction integrates to zero. For \(m\ge2\) and \(0<\beta<1\), the function \(\sum v_j^\beta\) is not constant in the interior of the simplex: it has a different value near a vertex than at the barycenter. Thus \(C_{m,\beta}>0\).

At \(\beta=1\), the original waiting time is exponential with mean \(\tau\). Conditioning any prescribed path to survive resetting simply makes all its independent waits exponential with common rate \(r+1/\tau\), so their normalized proportions have **exactly** the uniform Dirichlet law for every \(r\). The probability of any nonshortest path is precisely the marked-law total-variation error. A first detour of two extra hops consists of one opposite-direction step paired with its return, and the number of such admissible first-absorption paths is \(c_{N,i,z}\): there are \(m\) candidate locations for this detour, except that the outward detour from the reset site is inadmissible if that site is immediately adjacent to the opposite absorbing endpoint. Hence, with \(h=(1+r\tau)^{-1}\),
\[
\Pr(K\ne m\mid S=z)=\frac{c_{N,i,z}}4 h^2+O(h^4)
=\frac{c_{N,i,z}}4(r\tau)^{-2}+O((r\tau)^{-3}).
\]
These coefficients are strictly positive under the standing \(m\ge2\) assumption. This completes both cases.

## Verification
The accompanying standalone file `verify_fractional_ctrw.py` uses Python 3, NumPy and SciPy, and runs with `python verify_fractional_ctrw.py`. It tests finite-interval absorbing resolvents against independent matrix inversions, counts first detour paths by brute-force enumeration, checks signed-Gamma mixture Laplace transforms, independently integrates first-order total-variation coefficients for two-hop time shares, verifies zero-mass and nonconstancy of the Dirichlet correction, and probes the memoryless detour asymptotics. The executed program reported **2804 deterministic comparisons passed**. These finite computations test critical normalizations and boundaries but do not prove infinite-parameter asymptotics; those follow from Steps 1–4.

## Relationship to prior work
Pal, Das and Pal (arXiv:2604.01986) derive the competing-exit reset renewal flux, first-passage transforms, conditional mean times and fluctuation criteria for anomalous CTRWs with Mittag-Leffler waiting times; the model and those results are prior work. Kuśmierz and Gudowska-Nowak (arXiv:1812.08489) analyze complete versus incomplete CTRW resetting, propagators, and hitting-time statistics. Chen, Li and Huang (arXiv:2111.01330) obtain finite absorbing Markov-chain resetting formulas, which already cover general **endpoint splitting resolvents**. Linn and Lawley (arXiv:2302.05409) establish frequent-reset **total first-passage time** asymptotics. None of the material inspected in these sources states this *path-resolved, normalized holding-time share* expansion or the positive fractional-versus-Markovian error exponent transition. Dirichlet-from-Gamma normalization is classical, not claimed new. The new claim is the path-conditioned sharp total-variation comparison and its explicit nonzero correction. Formula-level implication from more general published marked-renewal identities remains a possible source of prior coverage; no uniqueness assertion is made.

## Limitations
This is a theorem for the fixed finite interval, a symmetric nearest-neighbor walk, fresh-clock complete resetting, and the **exact** Mittag-Leffler transform. It does not concern partial/clock-preserving resetting, random reset sites, continuum scaling, the number/durations of prior failed excursions, total first-passage time, or uniform asymptotics when \(\beta\to1\) or \(N\to\infty\). The \(m=1\) case is excluded because its fraction vector is deterministic. The constant \(C_{m,\beta}\) is a finite-dimensional Dirichlet expectation rather than generally an elementary expression. Novelty still requires independent comparison with all potentially broader marked-path renewal literature.

## References
1. S. Pal, R. Das and A. Pal, *Resetting optimized competitive first-passage outcomes in non-Markovian systems*, arXiv:2604.01986v1 (public April 2, 2026), https://arxiv.org/abs/2604.01986.
2. Ł. Kuśmierz and E. Gudowska-Nowak, *On subdiffusive continuous time random walks with stochastic resetting*, arXiv:1812.08489 (2018), https://arxiv.org/abs/1812.08489.
3. Y. Chen, X. Li and Y. Huang, *First passage in discrete-time absorbing Markov chains under stochastic resetting*, arXiv:2111.01330 (2021), https://arxiv.org/abs/2111.01330.
4. S. Linn and S. D. Lawley, *First passage times under frequent stochastic resetting*, arXiv:2302.05409 (2023), https://arxiv.org/abs/2302.05409.
5. F. Colantoni and G. Pagnini, *Master equations for continuous-time random walks with stochastic resetting*, arXiv:2507.07590 (2025), https://arxiv.org/abs/2507.07590.
