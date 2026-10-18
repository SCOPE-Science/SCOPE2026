# Directional first-detour law and sharp successful-excursion localization under lattice resetting

## Finding

For a continuous-time symmetric nearest-neighbor walk on \(\mathbb Z^d\), resetting at rate \(r>0\) to a non-target starting site \(m=(m_1,\ldots,m_d)\), the entire **last successful excursion**, rather than the total arrival time, has an explicit first correction to shortest-path localization. Let \(N\) be its hop count; put \(L=\sum_i |m_i|\ge1\), \(K=L!/\prod_i|m_i|!\), and \(q=(r+2d)^{-1}\). For a successful excursion with \(N=L+2\), let \(J\) be the unique coordinate in which the walk made one extra opposite-direction step pair relative to a shortest path. Define

\[
 c_j=\frac{(L+1)(L+2)}{|m_j|+1}-2,\qquad C=\sum_{j=1}^d c_j.
\]

For **fixed** \(d\) and \(m\), as \(r\to\infty\),

\[
 \begin{aligned}
 \mathbb P(N=L)&=1-Cq^2+O_{d,m}(q^4),\\
 \mathbb P(N=L+2,J=j)&=c_jq^2+O_{d,m}(q^4),\\
 \mathbb P(N\ge L+4)&=O_{d,m}(q^4),\\
 \mathbb E[N]&=L+2Cq^2+O_{d,m}(q^4).
 \end{aligned}
\]

In particular, \(\mathbb P(N>L)=Cq^2+O_{d,m}(q^4)\), and every \(c_j>0\). Conditioned on \(N=L\), all \(K\) shortest routes have exactly equal probability for every reset rate.

Let \(H\) be the duration of the successful excursion, including its final jump but excluding all preceding failed excursions. Given \(N=n\), the scaled duration \((r+2d)H\) has the Gamma distribution of integer shape \(n\) and unit rate. Consequently, with \(\Gamma_L\) denoting that law at shape \(L\),

\[
 d_{\mathrm{TV}}\bigl(\mathcal L((r+2d)H),\Gamma_L\bigr)
 =C\,\delta_Lq^2+O_{d,m}(q^4),
\]

where

\[
 \delta_L= e^{-\sqrt{L(L+1)}}\left[
 \frac{(L(L+1))^{L/2}}{L!}
 +\frac{(L(L+1))^{(L+1)/2}}{(L+1)!}
 \right]>0.
\]

A second statement quantifies the large-dimensional observation in the motivating paper. Let \(m=(2,0,\ldots,0)\), \(r=\alpha d\), and hold \(\alpha>0\) fixed while \(d\to\infty\). Then

\[
 \begin{aligned}
 \mathbb P(N>2)&=\frac{10}{(\alpha+2)^2d}+O_\alpha(d^{-2}),\\
 \mathbb E[N]&=2+\frac{20}{(\alpha+2)^2d}+O_\alpha(d^{-2}),\\
 d_{\mathrm{TV}}\bigl(\mathcal L((r+2d)H),\Gamma_2\bigr)
 &=\frac{10\delta_2}{(\alpha+2)^2d}+O_\alpha(d^{-2}).
 \end{aligned}
\]

At the rate \(r=2d\), suggested as a large-dimensional optimum in the source's approximate finite-state model, these become \(\mathbb P(N>2)=5/(8d)+O(d^{-2})\) and \(\mathbb E[N]=2+5/(4d)+O(d^{-2})\). Among the \(N=4\) successes, a transverse coordinate accounts for \(10(d-1)\) of \(10d-8\) admissible paths, whereas the longitudinal coordinate accounts for only two. These conclusions concern exactly the stated family and do not assume that \(2d\) is the exact finite-dimensional optimal reset rate.

## Assumptions and scope

The target is the absorbing origin of the infinite lattice \(\mathbb Z^d\). Every one of the \(2d\) oriented nearest-neighbor jumps has independent exponential rate one, so the total jump intensity is \(2d\). Resetting to the fixed starting site \(m\ne0\) occurs at independent exponential rate \(r>0\), restarts the search from scratch, and leaves no residual memory. A successful excursion is the final excursion from the initial placement or the last reset to first absorption, with no intervening reset. Because a particular shortest path has positive probability on every trial, a successful excursion eventually occurs almost surely. No finite-volume boundary or spatially heterogeneous hopping is imposed. \(d,m\) are fixed in the first limit; in the second, \(d\) varies, \(m=(2,0,\ldots,0)\), and \(r/d=\alpha>0\) is fixed.

## Proof

**1. Exact renewal path weights.** Superpose the \(2d\) independent jump clocks and the reset clock. The waiting times between successive events are independent \(\operatorname{Exp}(r+2d)\), and the probability of any prescribed oriented jump as the next event is \(q\). Let \(F_n\) be the number of oriented nearest-neighbor paths that start at \(m\), avoid the target before their final step, and first hit it exactly on step \(n\). The probability of a successful excursion of length \(n\) in one trial is therefore exactly \(F_n q^n\). Since all restart trials are identically distributed and independent, the final successful trial has the single-trial law conditional on success, namely

\[
 \mathbb P(N=n)=\frac{F_nq^n}{p(q)},\qquad p(q)=\sum_{n\ge L}F_nq^n>0.
\]

The same argument proves that the time intervals, conditional on any prescribed successful jump path of length \(n\), remain independent \(\operatorname{Exp}(r+2d)\). This gives the exact Gamma mixture for \(H\).

**2. Minimal and next-to-minimal paths.** A shortest route has exactly \(|m_j|\) directed moves toward zero in each coordinate. Its number is \(F_L=K\). Every route of length \(L+2\) to zero has exactly one additional opposite-direction pair, in a uniquely determined coordinate \(j\). Ignoring premature target visits, the number of such routes is

\[
 A_j=\frac{(L+2)!}{(|m_j|+1)!\prod_{i\ne j}|m_i|!}
 =K\frac{(L+2)(L+1)}{|m_j|+1}.
\]

A route of this length can have visited zero before its final step only at step \(L\), by shortest-path length and bipartite parity. Such a route consists of a shortest route followed by one of the two opposite two-step loops along \(j\), giving exactly \(2K\) premature-hit routes. Subtracting yields

\[
 F_{L+2}^{(j)}=Kc_j,
 \qquad F_{L+2}=KC.
\]

The positive coefficient \(c_j\) follows because \(|m_j|\le L\), so \((L+1)(L+2)/(|m_j|+1)\ge L+2\), whence \(c_j\ge L>0\).

**3. Controlling all longer paths for fixed dimension.** Lattice parity forbids first hits at lengths \(L+1,L+3,\ldots\). Every \(F_n\le(2d)^n\). For \(q<1/(2d)\), the tail beginning at \(L+4\) is bounded by a convergent geometric series:

\[
 0\le\sum_{n\ge L+4}F_nq^n
 \le\frac{(2dq)^{L+4}}{1-2dq}=O_{d,m}(q^{L+4}).
\]

Its \(n\)-weighted version is also \(O_{d,m}(q^{L+4})\) as \(q\downarrow0\). Therefore

\[
 p(q)=Kq^L\left[1+Cq^2+O_{d,m}(q^4)\right],
\]

and division proves every claimed fixed-dimensional hop-count and expectation expansion. All shortest paths have the same weight \(q^L\), proving their exact uniformity.

**4. Sharp duration total-variation correction.** Write \(G_n\) for the Gamma distribution of integer shape \(n\), unit rate. The exact successful-duration law is the nonnegative mixture \(\sum_n\mathbb P(N=n)G_n\). The preceding estimates give, as an identity of finite signed measures with remainder bounded in total variation norm,

\[
 \mathcal L((r+2d)H)-G_L
 =Cq^2(G_{L+2}-G_L)+O_{\mathrm{TV},d,m}(q^4).
\]

For \(t>0\), the two densities obey \(g_{L+2}(t)/g_L(t)=t^2/[L(L+1)]\). They cross exactly once at \(t_*=\sqrt{L(L+1)}\). Consequently

\[
 d_{\mathrm{TV}}(G_{L+2},G_L)
 =\mathbb P(G_L\le t_*)-\mathbb P(G_{L+2}\le t_*)
 =e^{-t_*}\left(\frac{t_*^L}{L!}+\frac{t_*^{L+1}}{(L+1)!}\right)=\delta_L.
\]

The reverse triangle inequality transfers the \(O(q^4)\) signed-measure remainder into the asserted sharp scalar total-variation expansion.

**5. Joint large-dimensional limit.** For \(m=(2,0,\ldots,0)\), let \(A_n(v)\) count unrestricted oriented \(n\)-step lattice routes from \(v\) to zero. Define their ordinary generating functions \(G_v(q)=\sum_{n\ge0}A_n(v)q^n\). The first-hit renewal factorization gives \(p(q)=G_{2e_1}(q)/G_0(q)\). The Bessel generating identity and \(\int_0^\infty e^{-s}s^n\,ds=n!\) show

\[
 \begin{aligned}
 G_0(q)&=\int_0^\infty e^{-s}I_0(2qs)^d\,ds,\\
 G_{2e_1}(q)&=\int_0^\infty e^{-s}I_2(2qs)I_0(2qs)^{d-1}\,ds.
 \end{aligned}
\]

Put \(q=c/d\) where \(c=1/(\alpha+2)<1/2\). For \(x\ge0\), the absolutely convergent nonnegative Bessel series give

\[
 I_0(2x)=1+x^2+O(x^4e^{2x}),\qquad
 I_2(2x)=x^2/2+x^4/6+O(x^6e^{2x}),
\]

and, uniformly in \(d\ge1\),

\[
 I_0(2x)^d=1+dx^2+O(d^2x^4e^{2dx}),
\]

\[
 I_2(2x)I_0(2x)^{d-1}
 =x^2/2+\left((d-1)/2+1/6\right)x^4
 +O(d^2x^6e^{2dx}).
\]

The remainders are integrable after setting \(x=qs\), since \(e^{-s}e^{2dqs}=e^{-(1-2c)s}\) and \(c<1/2\). Integration, using \(\int e^{-s}s^n ds=n!\), yields

\[
 G_0(q)=1+2dq^2+O_\alpha(d^2q^4),
 \quad G_{2e_1}(q)=q^2+(12d-8)q^4+O_\alpha(d^2q^6).
\]

Hence

\[
 p(q)=q^2+(10d-8)q^4+O_\alpha(d^2q^6).
\]

As \(F_2=1\) and \(F_4=10d-8\), nonnegativity of the remaining first-hit coefficients implies \(\sum_{n\ge6}F_nq^n=O_\alpha(d^2q^6)\). It follows by division that \(\mathbb P(N>2)=(10d-8)q^2+O_\alpha(d^2q^4)\). Differentiating the same dominated Bessel-integral expansions with respect to \(q\) (a factor of \(s\) remains integrable) gives \(\mathbb E[N]=q p'(q)/p(q)=2+2(10d-8)q^2+O_\alpha(d^2q^4)\). The TV expansion from Step 4 applies with an \(O_\alpha(d^{-2})\) mixture remainder. Substituting \(q=1/((\alpha+2)d)\) proves the displayed sharp \(d^{-1}\) laws.

## Verification

The companion standalone \`verify.py\` uses Python's standard library and tests the combinatorial identities by two independent mechanisms: dynamic enumeration of first-target-hit routes with their full coordinate-step counts, and exact rational Bessel-series/renewal coefficient extraction. It checks all nonzero sites in specified small boxes, eight separate lattice dimensions in the Green-series calculation, the long-dimension coefficient against independent truncated generating functions, and the Gamma crossing constant. It reports **360 successful finite checks**. The infinite-lattice tail bound, all large-parameter limits, and the nonnegative-mixture total-variation expansion are analytical, not established by finite tests.

## Relationship to prior work

Hartmann and Majumdar (2025), arXiv:2505.19903v1, provide the model, exact mean-first-passage and lattice Green-function structure. In Section V.3 and Figure 5 they *numerically observe* that the final successful excursion tends toward the minimal hop count as either dimension or reset rate increases; their short-route finite-state approximation suggests \(r\simeq2d\) for the example starting two sites away. Those results are prior, not claimed here. The finding here instead **counts and labels the first surviving nonminimal routes**, determines their coordinate bias, proves a sharp total-variation correction for the successful-excursion duration, and supplies the \(5/(8d)\) and \(5/(4d)\) coefficients for the source's dimension-dependent observation. An unmarked total correction can also be recovered by expanding the previously known exact lattice Green function; it is not being represented as an independent new stochastic-renewal mechanism.

Linn and Lawley (2023), arXiv:2302.05409v1, give a general frequent-resetting theorem for the **total arrival time**, including discrete-network geodesic domination and the geometric number of unsuccessful trials. Lawley (2020), arXiv:2008.04496v1, gives related fastest-searcher geodesic dominance for network first passage. Neither total-arrival-time limit, shortest-path existence, nor renewal structure is claimed as novel. The present claim is specifically a **marked path-level and successful-segment duration law** on the homogeneous lattice, including first detour and sharp finite correction. Sunil, Blythe, Evans and Majumdar (2025), arXiv:2503.03697v1, treat jump/reset costs in a different discrete-time continuous-space walk, not this lattice coordinate-resolved successful-segment law.

## Limitations

The fixed-dimensional expansion is not uniform in growing dimension; a separate argument establishes the stated \(m=2e_1\), \(r=\alpha d\) case. Bounds are asymptotic with parameter-dependent implicit constants, not finite-rate certified inequalities. The model assumes an infinite homogeneous hypercubic lattice with fixed resetting site and memoryless resetting. No claim is made for weighted graphs, partial resets, random reset positions, other target sets, or optimality of \(r=2d\) at a finite \(d\). The source's unmarked first-passage Green function already contains the aggregate path information implicitly, and the calculations use elementary power-series and path-counting methods; the new scope is the directional marked excursion classification and the quantitative duration/front coefficients. Independent originality evaluation has not occurred.

## References

1. A. K. Hartmann and S. N. Majumdar, *Diffusion with stochastic resetting on a lattice*, arXiv:2505.19903v1 (first posted 2025-05-26), Physical Review E **112**, 034102 (2025), DOI: 10.1103/1xkk-7q63. Primary model and Figure 5.
2. S. Linn and S. D. Lawley, *First-passage times under frequent stochastic resetting*, arXiv:2302.05409v1 (2023), Physical Review E **108**, 024114 (2023), DOI: 10.1103/PhysRevE.108.024114.
3. S. D. Lawley, *Extreme first-passage times for random walks on networks*, arXiv:2008.04496v1 (2020), Physical Review E **102**, 062118 (2020), DOI: 10.1103/PhysRevE.102.062118.
4. J. C. Sunil, R. A. Blythe, M. R. Evans and S. N. Majumdar, *The cost of resetting discrete-time random walks*, arXiv:2503.03697v1 (2025), Journal of Statistical Mechanics 083204 (2025), DOI: 10.1088/1742-5468/adf297.
