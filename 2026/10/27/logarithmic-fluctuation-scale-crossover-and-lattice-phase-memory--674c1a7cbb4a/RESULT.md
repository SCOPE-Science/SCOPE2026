# Logarithmic fluctuation-scale crossover and lattice-phase memory in the Kac ring

## Finding

Consider the classical Kac ring on \(N\) sites. Initially each spin is \(+1\); between adjacent sites lie independent, static scatterers that flip a passing spin with probability \(p\in(0,1/2)\). Define \(\mu=1-2p\in(0,1)\), \(\kappa=-\log\mu\), and normalized magnetization \(M_N(t)\) at integer time \(t\geq0\).

**Theorem (logarithmic-time Gaussian crossover).** Let \(t_N\to\infty\) be integers satisfying \(t_N=O(\log N)\). For any fixed integer offsets \(h_1,\ldots,h_d\), as \(N\to\infty\),
\[
\sqrt N\bigl(M_N(t_N+h_i)-\mu^{t_N+h_i}\bigr)_{i=1}^d
\ \Longrightarrow\ \mathcal N_d(0,C),
\qquad C_{ij}=\mu^{|h_i-h_j|}\left(|h_i-h_j|+\frac{1+\mu^2}{1-\mu^2}\right).
\]
All offset times are nonnegative for large \(N\). Write \(\tau_N=\log N/(2\kappa)\). Along any subsequence for which \(t_N-\tau_N\to a\in\mathbb R\), the uncentered vector \(\sqrt N(M_N(t_N+h_i))_i\) converges to a Gaussian with covariance \(C\) and mean \((e^{-\kappa(a+h_i)})_i\). In particular, with \(\sigma^2=(1+\mu^2)/(1-\mu^2)\),
\[
\Pr\bigl(M_N(t_N)>0\bigr)\longrightarrow\Phi\left(\frac{e^{-\kappa a}}{\sigma}\right).
\]
When \(t_N-\tau_N\to-\infty\) the probability tends to one; when \(t_N-\tau_N\to+\infty\), with \(t_N=O(\log N)\), it tends to one-half. This is a signal-to-noise crossover, not a mixing theorem for the microscopic deterministic dynamics. The integer-time offset \(t_N-\tau_N\) retains a lattice phase: \(t_N=\lfloor\tau_N+s\rfloor\) generally has several subsequential Gaussian shifts rather than a single full-sequence limit.

## Assumptions and scope

Set \(\xi_j=-1\) when the edge immediately preceding site \(j\) carries a scatterer, and \(+1\) otherwise. These are independent with \(\Pr(\xi_j=-1)=p\), periodic with period \(N\). A spin traverses one edge per time step and reverses on a scatterer. Thus for each integer \(t\in[0,N]\),
\[
Y_j(t)=\prod_{r=0}^{t-1}\xi_{j-r\pmod N},\qquad M_N(t)=\frac1N\sum_{j=1}^N Y_j(t),\qquad \mathbb EY_j(t)=\mu^t.
\]
The probability law is over the static independent scatterers, with all initial spins fixed positive. It is the **annealed scatterer law**, not a quenched law conditioning on one arrangement. \(\Phi\) denotes the standard normal distribution function. The proof is uniform over each specified finite set of offsets, with \(p\) fixed in the open interval stated; it does not treat near-degenerate scatterer densities changing with \(N\).

## Proof

**Step 1: exact finite-\(N\) covariance.** Fix positive integers \(u\leq v\) with \(u+v<N\). A product of \(u\) consecutive scatterer signs and one of \(v\) consecutive signs share either all \(u\) signs (at \(v-u+1\) shifts) or all but \(r\in\{1,\ldots,u-1\}\) signs (at exactly two shifts for each \(r\)). Their product then has expectation \(\mu^{v-u}\) or \(\mu^{v-u+2r}\), respectively. At disjoint shifts its covariance is zero. Summing the covariances of all pairs around the ring yields
\[
N\operatorname{Cov}(M_N(u),M_N(v))
=(v-u+1)\mu^{v-u}+2\sum_{r=1}^{u-1}\mu^{v-u+2r}-(u+v-1)\mu^{u+v}.\tag{1}
\]
For \(u=t_N+h_i\), \(v=t_N+h_j\) and offsets reordered as needed, the last term vanishes as \(N\to\infty\), while the finite geometric sum tends to \(2\mu^{|h_i-h_j|+2}/(1-\mu^2)\). This gives the stated \(C\), including the positive diagonal variance \(\sigma^2\).

**Step 2: growing-window central limit theorem.** Fix any linear combination of the centered components and write its summands as \(Z_j=\sum_i a_i(Y_j(t_N+h_i)-\mu^{t_N+h_i})\). Each is bounded in absolute value by \(2\sum_i|a_i|\). It depends only on a consecutive interval of at most \(L_N=t_N+\max_i h_i=O(\log N)\) independent scatterer signs. From the overlap argument above, and \(0<\mu<1\), for each fixed pair of offsets,
\[
\sup_N\sum_{k=0}^{N-1}\bigl|\operatorname{Cov}(Y_0(t_N+h_i),Y_k(t_N+h_j))\bigr|<\infty.
\]
Hence the same uniform absolute covariance-sum bound holds for the \(Z_j\). Partition the ring into disjoint blocks of \(b_N=\lfloor N^{1/3}\rfloor\) consecutive retained terms, separated by gaps of at least \(L_N\); leave a final wraparound gap as well. The retained block sums depend on disjoint sets of scatterer signs and are independent. The total number of discarded terms is \(O(NL_N/b_N+b_N+L_N)=o(N)\). The covariance-sum bound gives variance \(o(N)\) for their sum, so discarding changes the normalized sum by \(o_{L^2}(1)\). Each retained centered block is bounded by a constant times \(b_N=o(\sqrt N)\), so the Lindeberg condition holds for the independent block array. Its total variance divided by \(N\) converges, by (1), to \(a^\top Ca\). The Lindeberg–Feller theorem and then Cramér–Wold prove the claimed joint normal law, including degenerate linear combinations by Chebyshev's inequality.

**Step 3: crossover and lattice phase.** Exactly \(\mathbb EM_N(t_N+h)=\mu^{t_N+h}\), and
\[
\sqrt N\,\mu^{t_N+h}=\exp[-\kappa(t_N-\tau_N+h)].
\]
Slutsky's theorem gives the shifted normal limit in every convergent phase subsequence. The centered normal has continuous positive one-point variance, yielding the limiting positivity probabilities. If the phase tends to \(-\infty\), the deterministic positive shift diverges while the centered sequence remains tight; if it tends to \(+\infty\), the shift vanishes. Finally, integer times make \(\lfloor\tau_N+s\rfloor-\tau_N=s-\{\tau_N+s\}\), which need not converge: the correct general statement is the family of phase-subsequential limits, not a false universal continuous-time shift.

## Verification

The self-contained `verify_kac.py` enumerates complete independent-scatterer configurations for \(6\leq N\leq11\), several time pairs with \(u+v<N\), and two nontrivial probabilities \(p\); it compares the exact empirical magnetization means and covariances with (1). It also checks positivity of the five-time limiting covariance matrix and rapid convergence of the finite-time covariance formula for several growing times. The script completes without external dependencies beyond NumPy. These finite checks are corroboration only; the block proof establishes the limit for arbitrary growing \(N\).

## Relationship to prior work

The classical Kac ring and its relaxation mechanism are standard. De Roeck, Jacobs, Maes, and Netočný (2003) studied a quantum extension and first the thermodynamic limit, then the long-time limit; their scatterer ensemble fixes the total number of scatterers, unlike the present independent ensemble. Hiura (2021), especially Section 3.3 and Eq. (3.16), derived the annealed covariance for fixed observation times and analyzed dynamical fluctuations, chiefly under a quenched setup. Its exact covariance agrees with the fixed-time specialization of (1). Importantly, a fixed-time covariance identity or fixed-horizon central limit theorem alone does **not** yield a triangular-array central limit theorem at a diverging observation time: that is the additional step proved here. A 2004 thesis by Cardoen analyzes small fluctuations in the classical Kac ring; relevant indexed text was consulted, but its full text was not accessed during this review. It is an explicit residual priority risk, not claimed to have been ruled out.

## Limitations

The result applies to a ring with all initially positive spins, independent fixed Bernoulli scatterers of density strictly between zero and one-half, integer observation times diverging at most logarithmically, and finitely many fixed offsets. It does not characterize the microscopic stationary distribution, quenched sample-to-sample behavior, nonlinear observation times near recurrence, scatterers sampled at a fixed exact count, or independent historical priority. No claim of mixing is made: each microscopic orbit has a period dividing \(2N\).

## References

1. W. De Roeck, T. Jacobs, C. Maes, and K. Netočný, *An extension of the Kac ring model*, arXiv:cond-mat/0307460, first posted 18 July 2003, https://arxiv.org/abs/cond-mat/0307460.
2. K. Hiura, *Macroscopic dynamical fluctuations in Kac ring model*, arXiv:2109.06434, first posted 14 September 2021; Section 3.3, Eq. (3.16), https://arxiv.org/abs/2109.06434.
3. D. Cardoen, *The Gibbs hypothesis for macroscopic fluctuations: study of the Kac ring model*, master's thesis dated 27 July 2004, DOI 10.13140/RG.2.1.2887.4323; full-text comparison remains incomplete.
