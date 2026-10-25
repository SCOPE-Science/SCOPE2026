# Exact completion-time tail for an endogenous-aging threshold cascade on a cycle

## Finding
For every integer \(m\ge1\), a seeded \((m+2)\)-cycle under the explicitly defined endogenous-aging, randomly sampled threshold process below has an almost surely finite full-adoption time \(T_m\), but \(\mathbb E T_m=\infty\). Its exact survival law is a finite matrix product, and its sharp tail is
\[
\lim_{t\to\infty}t\,\Pr(T_m>t)=\frac{2^{m-1}}{\Gamma(2-1/(m+2))^{m+2}}.
\]
For every real \(q>0\), \(\mathbb E[T_m^q]<\infty\) exactly when \(q<1\). The leading amplitude, including the factor \(2^{m-1}\), is not inferred from a mean-field density approximation.

## Assumptions and scope
Let \(N=m+2\ge3\), take the simple cycle \(C_N\), and initially designate exactly two adjacent vertices as irreversible adopters, with the other \(m\) vertices nonadopters. All nonadopters have age zero initially, and the strict fractional neighborhood threshold satisfies \(0<\theta<1/2\). Thus a nonadopter becomes eligible as soon as at least one of its two neighbors adopts. A sweep indexed by \(s=0,1,\ldots\) comprises exactly \(N\) sequential, independently and uniformly sampled vertices (sampling with replacement). At each selected vertex, if it is a currently eligible nonadopter, it becomes an adopter with independently sampled probability \(p_s=1/(s+2)\); otherwise nothing changes. Updates act immediately within a sweep. A remaining nonadopter's age increases by one at the end of each sweep; adopters never revert. Consequently all remaining nonadopters use the common activation probability \(p_s\) during sweep \(s\). The completion time \(T_m\) is the number of sweeps to first reach all-adopter state; hence \(\Pr(T_m>0)=1\).

Write \(Q\) for the \((m+1)\)-by-\((m+1)\) matrix indexed by the remaining arc length \(k=0,1,\ldots,m\), with \(Q_{0,0}=0\), \(Q_{1,1}=-1\), \(Q_{1,0}=1\), and for \(2\le k\le m\), \(Q_{k,k}=-2\) and \(Q_{k,k-1}=2\); all other entries vanish. Let \(e_m\) be the unit column vector at index \(m\), and \(u=(0,1,\ldots,1)^\mathsf T\). Define for every integer \(t\ge0\)
\[
F_t(z)=\prod_{s=0}^{t-1}\left(1+\frac{z}{N(s+2)}\right)^N,
\qquad F_0(z)=1.
\]

## Proof
The currently nonadopting vertices always form a contiguous (possibly empty) arc. When its length \(k\ge2\), exactly the two endpoints are eligible; when \(k=1\), its single vertex is eligible. One vertex draw in sweep \(s\) therefore changes the row distribution on arc lengths by multiplication with the stochastic matrix \(I+Q/[N(s+2)]\). Since there are \(N\) independent conditional draws per sweep, the transition matrix after \(t\) complete sweeps is the polynomial matrix \(F_t(Q)\). Consequently, for every \(m\ge1\) and integer \(t\ge0\),
\[
\Pr(T_m>t)=e_m^\mathsf T F_t(Q)u.
\]
This is an exact finite-time formula, not an asymptotic approximation.

Restrict \(Q\) to transient indices \(1,\ldots,m\). It is lower bidiagonal, with diagonal entries \(-1,-2,\ldots,-2\). The eigenvalue \(-1\) is simple; a right eigenvector is \(v_k=2^{k-1}\) for \(1\le k\le m\), and a left eigenvector is \(e_1^\mathsf T\), normalized so \(e_1^\mathsf T v=1\). The spectral projection on this eigenvalue is therefore \(P=ve_1^\mathsf T\), so \(e_m^\mathsf T P\mathbf1=2^{m-1}\).

The only other transient eigenvalue, \(-2\), has an algebraic Jordan block of size at most \(m-1\). For each fixed \(m\), functional calculus gives
\[
e_m^\mathsf T F_t(Q)u=2^{m-1}F_t(-1)+\sum_{j=0}^{m-2}c_{m,j}F_t^{(j)}(-2),
\]
where the finite coefficients \(c_{m,j}\) are independent of \(t\). The sum is empty for \(m=1\). For complex \(z\) in a neighborhood of either relevant eigenvalue, the product identity and gamma ratio show
\[
F_t(z)=\left[\frac{\Gamma(t+2+z/N)}{\Gamma(2+z/N)\Gamma(t+2)}\right]^N
=\Gamma(2+z/N)^{-N}t^z(1+O_m(t^{-1})),
\]
with locally uniform analytic remainder. Differentiating \(j\) times at \(z=-2\) gives \(F_t^{(j)}(-2)=O_m(t^{-2}(1+\log t)^j)\). At \(z=-1\),
\[
F_t(-1)\sim\Gamma(2-1/N)^{-N}t^{-1}.
\]
Thus \(\Pr(T_m>t)=2^{m-1}\Gamma(2-1/N)^{-N}t^{-1}+O_m(t^{-2}(1+\log t)^{m-2})\) for \(m\ge2\); for \(m=1\) the error is \(O(t^{-2})\). This proves the asserted positive tail constant. Survival tends to zero, proving almost-sure completion. The discrete tail-sum/integration identity for nonnegative integer-valued random variables proves the moment criterion: a strictly positive \(t^{-1}\) survival tail has finite \(q\)-moment for \(0<q<1\) and infinite \(q\)-moment for \(q\ge1\).

## Verification
The independent-of-proof, exact-rational finite-chain checker `verify.py` computes row-state transitions without spectral decomposition and checks all \(m=1,\ldots,7\), \(t=0,\ldots,8\). It checks the matrix-derived explicit formulas for arc lengths \(m=1,2,3\) and strict decreasing survival after successive sweeps. The checker verifies \(63\) exact rational state distributions; finite checks do not prove the asymptotic result, which follows analytically above. For \(m=2\),
\[
\Pr(T_2>t)=2F_t(-1)-F_t(-2),\quad \Pr(T_2>1)=1753/2048.
\]
For \(m=3\), \(\Pr(T_3>t)=4F_t(-1)-3F_t(-2)-2F_t'(-2)\), and \(\Pr(T_3>1)=24233/25000\). Execute `python3 verify.py` using the Python standard library only.

## Relationship to prior work
Abella, San Miguel, and Ramasco (2022 preprint; 2023 journal) define the endogenous-aging threshold mechanism and its Monte Carlo update rule, study dynamics numerically and approximately on random networks and two-dimensional lattices, and observe a near-full-adoption nonadopter density decay proportional to reciprocal time. Their Appendix A gives the per-sweep single-vertex nonactivation product. Their Fig. 4 instead measures the time to more than 90% adoption, not the finite-system random time to 100% adoption. The present cycle calculation uses their mechanism but supplies a different exact finite-system observable: the whole distribution through the polynomial generator, the leading network-size-dependent amplitude, and a strict all-moments boundary. Classical spectral decompositions for absorbing finite-state Markov chains underlie the method and are not claimed as novel. Richter, Henkel, and Böttcher (2020) address aging and equilibration in bistable contagion dynamics, not this exact irreversible cycle completion law.

## Limitations
The graph is a cycle, the two seeds are adjacent, the strict threshold is below one half, and the age clock is synchronized by complete Monte Carlo sweeps. The result does not extend automatically to higher thresholds, nonsynchronized node-specific ages, exogenous resets, noncycle networks, finite-time practical cutoff measures, or all asynchronous implementations. The known reciprocal-time decay in mean nonadopter density is not claimed as new. Independent external audit and exhaustive publication-priority verification have not been performed.

## References
1. D. Abella, M. San Miguel, and J. J. Ramasco, *Aging in binary-state models: The Threshold model for complex contagion*, arXiv:2209.05990, first posted 13 September 2022; *Physical Review E* **107**, 024101 (2023), DOI:10.1103/PhysRevE.107.024101, especially Secs. II–III and Appendix A.
2. P. Richter, M. Henkel, and L. Böttcher, *Aging and equilibration in bistable contagion dynamics*, *Physical Review E* **102**, 042308 (2020), DOI:10.1103/PhysRevE.102.042308.
