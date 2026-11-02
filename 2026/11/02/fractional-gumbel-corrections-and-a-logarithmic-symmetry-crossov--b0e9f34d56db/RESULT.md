# Fractional Gumbel corrections and a logarithmic symmetry crossover in alternating-rate dimer coverage

## Finding

Let \(n\ge4\) be even. On the cycle with \(n\) vertices, independently attempt placement of a dimer on every even edge at Poisson rate \(a>0\) and on every odd edge at rate \(b>0\). Accept an attempted placement when at least one endpoint was uncovered, and stop at the first complete coverage time \(T_n\). Set \(c=a+b\), \(\alpha=a/c\), \(\beta=b/c\), and \(\delta=\min(\alpha,\beta)\). Write \(G(x)=\exp(-e^{-x})\) and \(F_n(x)=\Pr\{cT_n-\log n\le x\}\).

**Exact finite-cycle law.** For \(t\ge0\), let \(q_a=e^{-at}\), \(q_b=e^{-bt}\), \(u=q_aq_b\), and \(s=q_a+q_b\). Define
\[
\Lambda_{\pm}=\frac{1-u\pm\sqrt{(1-u)^2-4u(1-q_a)(1-q_b)}}2.
\]
Then
\[
\Pr\{T_n\le t\}=\Lambda_+^{n/2}+\Lambda_-^{n/2}.
\]

**Fractional correction and sharp Kolmogorov constant.** For fixed \(a,b>0\) and every \(x\in\mathbb R\),
\[
F_n(x)=G(x)\exp\left\{\frac{e^{-x}}2\left[n^{-\alpha}e^{-\alpha x}+n^{-\beta}e^{-\beta x}\right]+O_x(n^{-1})\right\}.
\]
If \(a\ne b\), then the following convergence is uniform over \(x\in\mathbb R\):
\[
 n^{\delta}(F_n(x)-G(x))\longrightarrow \tfrac12G(x)e^{-(1+\delta)x}.
\]
Consequently, the Kolmogorov distance has an exact first-order constant:
\[
\lim_{n\to\infty} n^{\delta}\sup_{x\in\mathbb R}|F_n(x)-G(x)|
 =\frac{(1+\delta)^{1+\delta}e^{-(1+\delta)}}2.
\]
For \(a=b\), replace the limiting profile by \(G(x)e^{-3x/2}\) at scale \(n^{1/2}\), and the distance constant by \((3/2)^{3/2}e^{-3/2}\). Thus the unequal-rate convergence exponent varies continuously with the smaller edge-rate fraction and is strictly below \(1/2\).

**First correction to the expectation.** With Euler's constant \(\gamma\) and Gamma function \(\Gamma\),
\[
\mathbb E T_n=\frac{\log n+\gamma}{c}-\begin{cases}
\frac{\Gamma(1+\delta)}{2c}n^{-\delta}+o(n^{-\delta}),&a\ne b,\\
\frac{\Gamma(3/2)}{c}n^{-1/2}+o(n^{-1/2}),&a=b.
\end{cases}
\]

**Logarithmic near-symmetry crossover.** For each even \(n\), instead take \(a_n=1+\varepsilon_n\), \(b_n=1-\varepsilon_n\), with \(|\varepsilon_n|<1\), \(\varepsilon_n\to0\), and \(\varepsilon_n\log n\to\kappa\in\mathbb R\). With \(F_n(x)=\Pr\{2T_n-\log n\le x\}\), uniformly in \(x\),
\[
\sqrt n\,[F_n(x)-G(x)]\longrightarrow G(x)e^{-3x/2}\cosh(\kappa/2),
\]
and
\[
\mathbb ET_n=\frac{\log n+\gamma}{2}-\frac{\Gamma(3/2)}2\cosh(\kappa/2)n^{-1/2}+o(n^{-1/2}).
\]
The convergence of scaled distribution differences also holds in \(L^1(\mathbb R,dx)\), which justifies both mean expansions.

## Assumptions and scope

The cycle has a fixed alternating pattern of two positive edge-attempt rates. Each edge has its own independent Poisson process; failed attempts do not remove an earlier accepted dimer or uncover a site. Time is physical continuous time, not the count of accepted dimers. Vertex coverage is irreversible and a placement succeeds precisely if it covers at least one new site. All fixed-rate limits keep \(a,b\) constant as even \(n\to\infty\), except the explicitly specified near-symmetry family. No claim is made for cycles of odd order, for different acceptance rules, or for rates vanishing so fast that their normalized fractions leave the stated regimes.

## Proof

**1. Exact reduction to independent Bernoulli edge states.** The first attempt on edge \(i\) occurs at an independent exponential time of rate \(a\) or \(b\). Any later attempts on that edge cannot add coverage because the first attempt has already covered both endpoints, unless both were already covered; in either case the edge's first attempt determines its eventual contribution to coverage. At time \(t\), edge \(i\) remains unattempted with probability \(q_i=e^{-r_it}\), independently. A vertex remains uncovered if and only if both incident edges are unattempted. Thus complete coverage is equivalent to the absence of adjacent unattempted edges in the cyclic length-\(n\) binary sequence.

Index binary states \(0\) (attempted) and \(1\) (unattempted). The allowed transitions are encoded by \(M(q)=\left(\begin{smallmatrix}1-q&q\\1-q&0\end{smallmatrix}\right)\). The cyclic probability is
\[
\operatorname{tr}\{[M(q_a)M(q_b)]^{n/2}\}.
\]
The two-by-two product has trace \(1-u\) and determinant \(u(1-q_a)(1-q_b)\). Its eigenvalues are the displayed \(\Lambda_\pm\), proving the exact formula (including the boundaries \(t=0\) and \(t\to\infty\)).

**2. Local spectral expansion.** Let \(v=e^{-x}\), \(t=(\log n+x)/c\), \(u=v/n\), and \(s=n^{-\alpha}e^{-\alpha x}+n^{-\beta}e^{-\beta x}\). For \(x\) in any fixed compact set, \(u,s\to0\). The characteristic equation gives
\[
\Lambda_+=1-2u+us+O(u^2),\qquad
\log\Lambda_+=-2u+us+O(u^2),\qquad
|\Lambda_-|\le C u.
\]
The error is uniform when \(0\le u\le u_0\) and \(s\le s_0\), for sufficiently small absolute \(u_0,s_0\). Multiplying the logarithm by \(n/2\) yields
\[
\frac n2\log\Lambda_+=-v+\frac v2s+O(v^2/n).
\]
The small-eigenvalue contribution is superpolynomially negligible. This proves the pointwise exponential expansion and its fixed-rate asymptotic profiles. In the equal-rate case, the two terms of \(s\) contribute equally; otherwise only the term corresponding to the smaller exponent survives after scaling by \(n^\delta\).

**3. Uniform and integrable control.** For \(x\ge-\tfrac12\log n\), \(v\le\sqrt n\), so \(u\le n^{-1/2}\) and \(s\le2n^{-\delta/2}\). For large \(n\), spectral expansion and a mean-value estimate yield
\[
|F_n(x)-G(x)|\le C e^{-v/2}\left[v(q_a+q_b)+\frac{v^2}{n}\right]+O((C v/n)^{n/2}).
\]
On multiplying by \(n^\delta\), this has a uniformly bounded, integrable majorant in \(dx=-dv/v\), since \(q_a=(v/n)^\alpha\) and \(q_b=(v/n)^\beta\). For the near-symmetry sequence, both exponents eventually belong to \([1/4,3/4]\) and \(n^{1/2-\alpha_n},n^{1/2-\beta_n}\) stay bounded, giving the same domination after multiplying by \(\sqrt n\).

For \(-\log n\le x<-\tfrac12\log n\), observing only the \(n/2\) vertices of one bipartition supplies independent necessary coverage conditions: their two incident edge pairs are disjoint, with probability \(1-u\) per vertex. Hence \(0\le F_n(x)\le(1-u)^{n/2}\le e^{-v/2}\). For \(x<-\log n\), the physical-time CDF is zero; also \(G(x)\le e^{-n}\). These left-tail estimates are negligible under the claimed scalings in both supremum norm and \(L^1(dx)\). Dominated convergence therefore upgrades pointwise limits to uniform and \(L^1\) limits.

**4. Sharp constants and the symmetry window.** The function \(G(x)e^{-(1+\delta)x}\) achieves its maximum where \(e^{-x}=1+\delta\), yielding the asserted Kolmogorov constant. In the moving-rate family, \(\alpha_n=(1+\varepsilon_n)/2\) and \(\beta_n=(1-\varepsilon_n)/2\). Thus
\[
\sqrt n\,s= n^{-\varepsilon_n/2}e^{-\alpha_nx}+n^{\varepsilon_n/2}e^{-\beta_nx}\longrightarrow2e^{-x/2}\cosh(\kappa/2),
\]
which proves the logarithmic crossover.

**5. Mean correction.** The centered variable \(cT_n-\log n\) has an integrable distribution, with negative part bounded by \(\log n\) and positive part exponentially controlled by the union bound \(\Pr(T_n>t)\le n e^{-ct}\). The standard Gumbel variable has mean \(\gamma\). The identity
\[
\mathbb E(cT_n-\log n)-\gamma=-\int_{-\infty}^{\infty}(F_n(x)-G(x))\,dx
\]
and the \(L^1\) limits above give the stated coefficients because
\[
\int_{-\infty}^{\infty}G(x)e^{-(1+\delta)x}\,dx=\Gamma(1+\delta).
\]
No finite enumeration is used to justify an infinite limit.

## Verification

Execute the included standalone `checker.py` using Python 3. It independently enumerates cyclic binary edge states, compares with the two-by-two transfer formula in exact rational arithmetic, and compares two algebraically distinct exact expectation calculations (polynomial integration and vertex-event inclusion-exclusion). It also checks the predicted asymmetric and near-symmetric correction profiles numerically at growing even cycle sizes. The delivered checker passed 77 assertions. These finite and numerical checks are diagnostics; the above analytic proof establishes all quantified asymptotic statements.

## Relationship to prior work

Krapivsky's 2022 *Random Sequential Covering* defines the deposition rule and solves finite-interval deposited-dimer statistics, finite-ring accepted-dimer counts, and infinite-line occupancy evolution. This finding concerns instead the time of complete coverage on *finite even rings with unequal alternating edge rates*, including precise first finite-size corrections and their logarithmic crossover. Exact finite circular-run distributions are not themselves new: Inoue and Aki (2005) derive circular Bernoulli-run distributions for identically distributed trials; Koutras, Papadopoulos and Papastavridis (1995) treat nonidentical Bernoulli trials and first-order Poisson limits, with full-text comparison still outstanding. The present claim is restricted to the explicit asymmetric fractional correction, its sharp Kolmogorov and mean coefficients, and near-symmetry window, not a claim to discover transfer matrices or the Gumbel law in general. General Poisson bounds and iid second-order approximations do not by themselves supply these coefficients for the moving alternating array. Historical priority is not certified.

## Limitations

The checker covers only finite cycles and finite samples of asymptotic profiles. The primary risk is an earlier specialized treatment of the same periodic nonidentical two-run problem not found in accessible full text. The 1995 *Runs on a circle* paper was available only as an abstract in this review; its exact finite law and Poisson convergence are treated as prior, while its possible higher-order implications remain a residual literature risk. The results apply to alternating rates on even cycles only; there is no general nonperiodic environment or higher-dimensional analogue established here.

## References

- P. L. Krapivsky, *Random Sequential Covering*, arXiv:2209.03992 (first public version September 8, 2022), https://arxiv.org/abs/2209.03992.
- M. V. Koutras, G. K. Papadopoulos and S. G. Papastavridis, *Runs on a circle*, Journal of Applied Probability 32 (1995), 396–404, https://doi.org/10.2307/3215295.
- K. Inoue and S. Aki, *Joint distributions of numbers of success runs of specified lengths in linear and circular sequences*, Annals of the Institute of Statistical Mathematics 57 (2005), 353–368, https://doi.org/10.1007/BF02507029. Open version: https://www.ism.ac.jp/editsec/aism/pdf/057_2_0353.pdf.
- J. Petrauskienė and V. Čekanavičius, *On lower bounds for Poisson approximation to 2-runs statistic*, Lietuvos Matematikos Rinkinys 51 (2010), 470–474, https://www.journals.vu.lt/LMR/en/article/download/17874/17049/30075.
- A. P. Godbole, S. G. Papastavridis and D. R. Weishaar, *Formulae and recursions for the joint distribution of success runs of several lengths*, Annals of the Institute of Statistical Mathematics 49 (1997), 141–154, https://www.ism.ac.jp/editsec/aism/pdf/049_1_0141.pdf.
