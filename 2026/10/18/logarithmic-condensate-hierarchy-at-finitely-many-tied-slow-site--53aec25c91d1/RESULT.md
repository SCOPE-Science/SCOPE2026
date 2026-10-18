# Logarithmic condensate hierarchy at finitely many tied slow sites

## Finding
Consider a clockwise zero-range process on a periodic ring with a fixed number \(m\ge3\) of identical slow sites and a growing number of ordinary sites. At the marginal interaction exponent, a typical stationary configuration has one extensive slow-site condensate, while the other \(m-1\) slow sites occupy mutually independent logarithmic scales. A sharp, nonzero finite-size coefficient measures the rare failure of uniqueness.

Fix \(0<q<1\) and density \(\rho>\rho_c=q/(1-q)\). Let the number of lattice sites \(L\to\infty\), and let the integer total particle number \(N_L\) satisfy \(N_L/L\to\rho\). At each ordinary site an occupied site ejects one particle clockwise at rate \(1\). At each of the \(m\) distinguished sites with \(k\ge1\) particles, that total jump rate is \(q(1+1/k)\). Let \(\eta_{1,L},\ldots,\eta_{m,L}\) be slow-site occupations, let \(B_L\) be the total occupation of the ordinary sites, and let \(S_L=N_L-B_L\). Put \(d=\rho-\rho_c>0\).

**Critical hierarchy theorem.** The invariant distribution exists uniquely for each \(L>m\). It has the exact product weights stated below and satisfies:

1. \(S_L/L\to d\) in probability, while \((B_L-(L-m)\rho_c)/\sqrt L\) converges to a centered Gaussian of variance \(q/(1-q)^2\).
2. With probability tending to one, exactly one distinguished site has occupation \(S_L-o(S_L)\). The index \(J_L\) of the largest slow-site occupation (with the smallest-index tie convention) is asymptotically uniform on the \(m\) distinguished sites. Conditional on \(J_L=j\), the vector \(\bigl(\log(1+\eta_{i,L})/\log L\bigr)_{i\ne j}\) converges to \(m-1\) independent \(\operatorname{Uniform}(0,1)\) variables. This limiting index-and-exponent vector is independent of the limiting Gaussian ordinary-site fluctuation.
3. For every fixed \(0<\varepsilon<1/2\), writing \(E_{L,\varepsilon}\) for the event that **at least two distinct** slow sites each contain at least \(\varepsilon S_L\) particles, the probability has the sharp finite-size law
\[
\lim_{L\to\infty}(\log L)\,\Pr(E_{L,\varepsilon})
=(m-1)\log\!\left(\frac{1-\varepsilon}{\varepsilon}\right).
\]

For any integer \(s\ge0\), the normalizing polynomial for the slow-site occupations conditional on \(S_L=s\) has the exact Stirling form
\[
W_m(s)=\sum_{k_1+\cdots+k_m=s}\ \prod_{j=1}^{m}\frac1{k_j+1}
=\frac{m!\,{s+m\brack m}}{(s+m)!}
\sim\frac{m(\log s)^{m-1}}s,
\]
where \({n\brack m}\) denotes the unsigned Stirling number of the first kind and the asymptotic is for \(s\to\infty\).

## Assumptions and scope
All claims concern the unique stationary distribution of the *finite* continuous-time, totally asymmetric, irreducible zero-range chain on a ring. The number \(m\ge3\) is fixed independently of \(L\); \(q\in(0,1)\) and \(\rho>q/(1-q)\) are fixed, and \(N_L/L\to\rho\). The location of the distinguished sites does not matter to the product stationary weights. The threshold \(\varepsilon\) in the rare-sharing law is fixed in \((0,1/2)\). The event refers to the total slow-site mass, rather than the system's total mass. We use the convention \(\log(1+0)=0\).

The theorem does not apply when \(m\) grows with \(L\), at the critical total density, or in the nonstationary approach to equilibrium.

## Proof
**1. Exact stationary weights.** For an ordinary site define \(f_o(k)=1\). For each special site the recurrence \(f_s(k)/f_s(k-1)=1/[q(1+1/k)]\) gives \(f_s(k)=q^{-k}/(k+1)\). On the finite state space \(\sum_i\eta_i=N_L\), set
\[
\pi_{L,N_L}(\eta)=\frac1{Z_{L,N_L}}\prod_{i=1}^m\frac{q^{-\eta_i}}{\eta_i+1}.
\]
This obeys the master equation: at every configuration, the incoming weighted flux along an edge equals the weighted flux from the following site, so summing cyclically cancels incoming and outgoing terms. All allowed positive-rate moves connect the fixed-particle state space, hence this stationary distribution is unique.

**2. Ordinary-site fluid.** Put \(F=L-m\). If the ordinary sites contain \(b\) particles, there are \({b+F-1\choose F-1}\) nonnegative occupation vectors. Multiplying the stationary weight by the harmless constant \(q^{N_L}\), the law of \(B_L=b\) is proportional to
\[
 {b+F-1\choose F-1}\,q^b\,W_m(N_L-b),\qquad0\le b\le N_L.
\]
Without the last factor, this is the negative-binomial distribution with shape \(F\) and success probability \(1-q\): it is the law of a sum of \(F\) independent geometric variables of mean \(\rho_c\) and variance \(\sigma^2=q/(1-q)^2\). The factor \(W_m(s)\) is bounded above by a fixed polynomial in \(1+s\) and below by \(1/(1+s)\), since the all-but-one-empty slow-site term is present. Therefore the exponentially small large-deviation tails of the negative-binomial variable remain negligible under this polynomial tilt, and the lower normalizer on the typical region is polynomially large. It follows that \(B_L/L\to\rho_c\) and \(S_L/L\to d\).

More precisely, the asymptotic for \(W_m(s)\) proved below implies that the tilt \(W_m(N_L-b)\) has a ratio tending uniformly to one relative to its value at \(s=N_L-\lfloor F\rho_c\rfloor\) whenever \(|b-F\rho_c|=O(\sqrt L)\), because this changes \(s\asymp L\) by a relative \(o(1)\) amount. Truncating at a sufficiently wide central window and controlling tails by a geometric moment-generating function transfers the ordinary negative-binomial central limit theorem unchanged. The same local uniformity later yields independence from the slow-site logarithmic exponents.

**3. Exact slow partition and asymptotics.** For each fixed \(m\),
\[
\sum_{s\ge0}W_m(s)z^s=
\left(\sum_{k\ge0}\frac{z^k}{k+1}\right)^m
=\left(\frac{-\log(1-z)}z\right)^m.
\]
The classical exponential generating series of unsigned Stirling numbers gives the displayed exact coefficient identity. Singularity coefficient extraction at \(z=1\), equivalently the fixed-column Stirling asymptotic \({n\brack m}\sim(n-1)!(\log n)^{m-1}/(m-1)!\), yields \(W_m(s)\sim m(\log s)^{m-1}/s\).

**4. Independent logarithmic subordinate scales.** Fix a distinguished index \(j\) and any \(0<t_i<1\) for \(i\ne j\). In the conditional law given \(S_L=s\), restrict the other sites to \(0\le k_i\le s^{t_i}\) and set \(k_j=s-\sum_{i\ne j}k_i\). Since the sum of the restricted subordinate occupations is \(o(s)\), uniformly over the restricted box,
\[
\frac1{k_j+1}=\frac{1+o(1)}s.
\]
The box weight is consequently
\[
\frac{1+o(1)}s\prod_{i\ne j}
\sum_{k\le s^{t_i}}\frac1{k+1}
=\frac{(\log s)^{m-1}}s\biggl(\prod_{i\ne j}t_i\biggr)(1+o(1)).
\]
Dividing by \(W_m(s)\) shows that the probability of this event tends to \(m^{-1}\prod_{i\ne j}t_i\). Letting all \(t_i\uparrow1\) shows that the disjoint events defining a unique asymptotically extensive site exhaust probability one and that its index is uniform. These joint distribution functions give independent uniform subordinate log-exponents. Since \(S_L/L\to d\), \(\log S_L/\log L\to1\), and the argument is uniform for \(S_L\) in compact multiples of \(L\), the same limits hold without conditioning on \(S_L\). The uniformity on the central \(B_L\) fluctuation window established in Step 2 proves the asserted joint independence from the Gaussian fluid.

**5. Sharp probability of two macroscopic slow sites.** Work first conditionally on \(S_L=s\). Select an unordered pair of distinguished sites. On the leading contribution with that pair at occupations \(k\) and \(s-k-o(s)\), the sum over their split with both at least \(\varepsilon s\) is the Riemann sum
\[
\sum_{k=\lceil\varepsilon s\rceil}^{\lfloor(1-\varepsilon)s\rfloor}
\frac1{(k+1)(s-k+1)}
\sim\frac{1}s\int_{\varepsilon}^{1-\varepsilon}
\frac{dx}{x(1-x)}
=\frac2s\log\!\left(\frac{1-\varepsilon}{\varepsilon}\right).
\]
The other \(m-2\) sites have a total harmonic weight \((\log s)^{m-2}(1+o(1))\) when each is \(o(s)\); this follows by first restricting each to a fixed small fraction of \(s\), evaluating its harmonic sum, then sending that fraction to zero. Contributions in which three or more sites have at least a fixed positive fraction of \(s\) are \(O((\log s)^{m-3}/s)\), hence negligible at this order after dividing by \(W_m(s)\). The leading numerator for the event of at least two large sites is therefore
\[
{m\choose2}\frac{2(\log s)^{m-2}}s
\log\!\left(\frac{1-\varepsilon}{\varepsilon}\right)(1+o(1)).
\]
Dividing by \(W_m(s)\sim m(\log s)^{m-1}/s\) proves the coefficient \((m-1)\log((1-\varepsilon)/\varepsilon)\). Concentration of \(S_L\) on \(s\asymp L\), plus the same uniform slow-coefficient estimates on compact relative intervals, replaces \(\log s\) by \(\log L\) and finishes the proof.

## Verification
Run the accompanying \(\texttt{verify_critical_hierarchy.py}\) with Python 3 and NumPy. It checks the product invariant distribution by direct rational master-equation flux balance for 60 finite parameter instances, covering 1,904 state-balance identities. Independently it verifies 70 exact Stirling/coefficient identities and reports finite-size comparisons against the joint logarithmic profile and the two-macroscopic-site coefficient. For \(m=3\) and \(s=500,2000,8000\), the observed rare-event coefficients after multiplication by \(\log s\) were approximately \(2.12445,2.21917,2.28986\), respectively, against the analytic limit \(2\log4\approx2.77259\); slow logarithmic convergence is expected. The infinite-limit conclusions are established by the proof, not by these finite checks.

## Relationship to prior work
Angel, Evans and Mukamel (2004) treated a zero-range ring with a single defect rate of the form \(q(1+b/k)\) and established the relevant product weights and condensation mechanism; this theorem analyzes a different, fixed-multiplicity degeneracy exactly at \(b=1\). Godrèche and Luck (2012), Appendix A, derived and discussed the exact canonical two-site weight \(p_kp_{N-k}\), and its noncritical \(b<1\) and \(b>1\) limits. That does not assert the present joint \(m-1\)-coordinate critical log-law, the independent Gaussian bulk, or the coefficient for rare two-condensate coexistence at \(m\ge3\). Schwarzkopf, Evans and Mukamel (2008) studied multiple condensates created by nonmonotone hopping rates, a different mechanism. Mailler, Mörters and Ueltschi (2015) studied condensation under weak random continuous site disorder, not finitely many tied rates.

There is an **exact combinatorial equivalence**: setting \(\ell_i=k_i+1\), the conditional slow-site law coincides with the ordered cycle-length law of a uniform random permutation of \(s+m\) elements **conditioned to have exactly \(m\) cycles**, with those cycles uniformly labeled. The corresponding Stirling-number formula is classical (see Tao 2011 for the underlying Cauchy cycle-weight identity). This equivalence is part of the novelty comparison, not a claim that the finite cycle law is newly discovered. The new assertion is the joint two-scale stationary limit and the sharp rare-sharing coefficient in the critical tied-slow-site setting. No inspected primary source provided those conclusions together, although prior combinatorial treatments of fixed-cycle permutations remain a residual source of uncertainty.

## Limitations
This is a stationary finite-ring theorem under fixed \(m\) and supercritical density, not a statement about mixing, coarsening, dynamical switching, or growing defect multiplicity. The finite-size rare-sharing law gives a first logarithmic order but no second-order expansion. The exact permutation equivalence creates a substantive possibility of equivalent earlier conditional-cycle asymptotics that cannot be excluded through bibliographic searches alone. No claim of independent review is made.

## References
- A. G. Angel, M. R. Evans, D. Mukamel, *Condensation Transitions in a One-Dimensional Zero-Range Process with a Single Defect Site*, preprint arXiv:cond-mat/0401262v1 (15 January 2004), https://arxiv.org/html/cond-mat/0401262v1.
- C. Godrèche, J. M. Luck, *Condensation in the inhomogeneous zero-range process: an interplay between interaction and diffusion disorder*, arXiv:1209.4749 (21 September 2012), especially Appendix A, https://arxiv.org/abs/1209.4749.
- Y. Schwarzkopf, M. R. Evans, D. Mukamel, *Zero-Range Processes with Multiple Condensates*, arXiv:0801.4501 (2008), https://arxiv.org/abs/0801.4501.
- C. Mailler, P. Mörters, D. Ueltschi, *Condensation and symmetry-breaking in the zero-range process with weak site disorder*, arXiv:1509.07672 (25 September 2015), https://arxiv.org/abs/1509.07672.
- T. Tao, *The number of cycles in a random permutation*, 23 November 2011, https://terrytao.wordpress.com/2011/11/23/the-number-of-cycles-in-a-random-permutation/.
