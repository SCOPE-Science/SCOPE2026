# Exact coupon-collector diamond mixing for product-state quantum refresh channels

## Finding
Let \(n\geq1\), let \(\mathcal H_i\) be finite-dimensional complex Hilbert spaces of dimensions at least two, and choose unit vectors \(|\phi_i\rangle\in\mathcal H_i\). With positive weights \(w_i\) summing to one, define the local pure-state replacement channel \(\mathcal E_i\), the randomly refreshed channel \(\mathcal T_w\), and the full preparation channel \(\mathcal R\) precisely below. For every integer \(m\geq0\),
\[
\boxed{\frac12\|\mathcal T_w^m-\mathcal R\|_\diamond
=\sup_\rho\frac12\|\mathcal T_w^m(\rho)-|\Phi\rangle\langle\Phi|\|_1
=\Pr\{\tau_w>m\}.}
\]
Here \(\tau_w\) is the time needed for independent draws with site probabilities \(w_i\) to select every site, \(|\Phi\rangle=\bigotimes_i|\phi_i\rangle\), and the supremum is over all system density matrices without reference ancillas. In particular, ancillary entanglement does not increase the optimal distinguishing advantage. The equality has the exact finite-time inclusion–exclusion form
\[
\Pr\{\tau_w>m\}=
\sum_{\varnothing\ne A\subseteq\{1,\ldots,n\}}
(-1)^{|A|+1}\Bigl(1-\sum_{i\in A}w_i\Bigr)^m,
\]
with \(0^0=1\) when \(m=0\).

For uniform selection \(w_i=1/n\), put \(d_n(m)=\frac12\|\mathcal T_w^m-\mathcal R\|_\diamond\). For every fixed real \(c\),
\[
\boxed{\lim_{n\to\infty}d_n(\lfloor n\log n+cn\rfloor)
=1-\exp(-e^{-c}).}
\]
Hence, for each fixed \(0<\varepsilon<1\), the smallest integer \(m\) with \(d_n(m)\le\varepsilon\) is
\[
\boxed{t_{\diamond,n}(\varepsilon)=n\log n
-n\log[-\log(1-\varepsilon)]+o(n).}
\]
For the corresponding *classical* uniformly refreshed bit-string walk, the worst-start total-variation mixing time is \((\frac12+o(1))n\log n\). Thus the ratio of these two specified mixing times tends to two. This comparison is between different operational distances, not a claim that the classical cutoff is new.

## Assumptions and scope
For an operator \(X\) on \(\mathcal H=\bigotimes_{i=1}^n\mathcal H_i\), let
\[
\mathcal E_i(X)=|\phi_i\rangle\langle\phi_i|_i\otimes\operatorname{tr}_i(X),\quad
\mathcal T_w=\sum_{i=1}^n w_i\mathcal E_i,\quad
\mathcal R(X)=\operatorname{tr}(X)|\Phi\rangle\langle\Phi|.
\]
The tensor factors in the partial-trace expression are placed back in their original labeled positions. The norm \(\|\cdot\|_\diamond\) is the completely bounded trace norm of a difference of channels, and \(\|\cdot\|_1\) is the ordinary trace norm. Each \(\mathcal E_i\) is CPTP, idempotent, and independent of the values of other sites. Every \(w_i>0\), so the target is the unique fixed density matrix. The finite-time formula remains true when some weights vanish, but then convergence to the full preparation channel need not occur.

This includes the quantized grand-coupling construction for *product* classical stationary measures. If site \(i\) has a strictly positive distribution \(\pi_i(b)\), choose \(|\phi_i\rangle=\sum_b\sqrt{\pi_i(b)}|b\rangle\) and update classical site \(i\) to an independent sample \(b\) with probability \(w_i\pi_i(b)\). The grand-coupling Kraus formula of Temme and Wocjan [1, journal Eq. (55); arXiv v1 Eq. (56)] then reduces algebraically to
\[
K_{i,b}=\sqrt{w_i}\,(|\phi_i\rangle\langle b|)_i\otimes I_{-i},
\]
whose sum over \(b\) is exactly \(w_i\mathcal E_i\). The general theorem is stated directly for physical replacement channels, regardless of whether a classical grand coupling was used to realize them.

## Proof
**1. Channel normalization and commutation.** In any local orthonormal basis \(\{|b\rangle\}\), the Kraus family \(\{\sqrt{w_i}(|\phi_i\rangle\langle b|)_i\otimes I_{-i}\}_{i,b}\) satisfies \(\sum_{i,b}K_{i,b}^\dagger K_{i,b}=I\). Every replacement discards the previous state at the selected site and prepares \(|\phi_i\rangle\), whence \(\mathcal E_i^2=\mathcal E_i\) and \(\mathcal E_i\mathcal E_j=\mathcal E_j\mathcal E_i\) for all \(i,j\). If \(V\) is the set of distinct sites visited in \(m\) independent draws, the channel conditional on this update history is exactly \(\mathcal E_V=\prod_{i\in V}\mathcal E_i\). For the full set, \(\mathcal E_{\{1,\ldots,n\}}=\mathcal R\).

**2. Sharp completely bounded upper bound.** Let \(p_m=\Pr\{\tau_w>m\}\). Conditioning on complete coverage gives the decomposition \(\mathcal T_w^m=(1-p_m)\mathcal R+p_m\mathcal N_m\), where for \(p_m>0\) the channel \(\mathcal N_m\) is the convex mixture of \(\mathcal E_V\) conditional on incomplete coverage. Since the diamond distance between CPTP maps is at most two,
\[
\tfrac12\|\mathcal T_w^m-\mathcal R\|_\diamond
=p_m\tfrac12\|\mathcal N_m-\mathcal R\|_\diamond\le p_m.
\]
If \(p_m=0\), equality is immediate.

**3. A product-state witness attaining the bound.** For each site select a unit \(|\psi_i\rangle\perp|\phi_i\rangle\), possible because \(\dim\mathcal H_i\ge2\), and input \(\rho_-=\bigotimes_i|\psi_i\rangle\langle\psi_i|\). When \(V\) is not the full set, \(\mathcal E_V(\rho_-)\) is supported orthogonally to \(|\Phi\rangle\): at least one unvisited site still has state \(|\psi_i\rangle\). Consequently
\[
\mathcal T_w^m(\rho_-)=(1-p_m)|\Phi\rangle\langle\Phi|+p_m\sigma_m,
\quad \sigma_m|\Phi\rangle=0.
\]
Thus \(\frac12\|\mathcal T_w^m(\rho_-)-|\Phi\rangle\langle\Phi|\|_1=p_m\). This establishes equality in both preceding upper bounds; no reference system is needed.

**4. Weighted exact formula.** Write \(A_i\) for the event that site \(i\) has not been drawn. For nonempty \(A\), independence of the draws yields \(\Pr(\bigcap_{i\in A}A_i)=(1-\sum_{i\in A}w_i)^m\). Inclusion–exclusion for \(\bigcup_i A_i\) gives the stated identity, including the empty-update case using \(0^0=1\).

**5. Uniform cutoff and its exact profile.** In the uniform case the probability of complete coverage is
\[
1-d_n(m)=\sum_{k=0}^n(-1)^k\binom nk(1-k/n)^m.
\]
For \(m=\lfloor n\log n+cn\rfloor\) and each fixed \(k\), \(\binom nk(1-k/n)^m\to e^{-ck}/k!\). For all \(k\le n\), its absolute value is at most \((n e^{-m/n})^k/k!\), a uniformly summable envelope for fixed \(c\). Dominated convergence therefore yields \(1-d_n(m)\to\sum_{k\ge0}(-1)^ke^{-ck}/k!=\exp(-e^{-c})\). Since the limiting profile is continuous and strictly decreasing in \(c\), monotonicity of \(d_n\) gives the stated threshold expansion.

**6. Classical counterpart (included for an explicit comparison).** For the classical random walk, a uniformly selected site is replaced by a fair bit at each step. Starting from the all-zero word, every Walsh character indexed by \(A\subseteq\{1,\ldots,n\}\) has mean \((1-|A|/n)^m\). Its chi-square distance from uniform obeys
\[
\chi^2(m)=\sum_{k=1}^n\binom nk(1-k/n)^{2m}
\le(1+e^{-2m/n})^n-1.
\]
At \(m=(\frac12+\delta)n\log n\) this tends to zero for any fixed \(\delta>0\), so total variation vanishes. For the converse let \(Y\) be the sum of the \(n\) bit-signs. At time \(m\), \(\mathbb E Y=n(1-1/n)^m\) and \(\operatorname{Var}(Y)\le n\), since pair covariances equal \((1-2/n)^m-(1-1/n)^{2m}\le0\). At equilibrium \(\mathbb E Y=0\) and \(\operatorname{Var}(Y)=n\). At \(m=(\frac12-\delta)n\log n\), the nonequilibrium mean is much larger than \(\sqrt n\); Chebyshev's inequality separates the laws in total variation with probability tending to one. Translation symmetry makes the all-zero start worst-case up to relabeling. This proves the stated classical cutoff location, in the conventional half-lazy normalization. Its factor-two comparison with the quantum cutoff follows.

## Verification
The standalone `verify.py` implements Kraus updates and subset-conditioned mixtures independently. It checks complete positivity and trace preservation, the weighted inclusion–exclusion identity, the product witness for exact trace distance, the ancilla-independent upper bound on random joint pure-state tests, a biased two-site qubit–qutrit product preparation, and finite-size approximations to the Gumbel profile. Running `python verify.py` with the version constraint in `requirements.txt` returned `VERIFY_OK 122 independent Kraus, reference, masks, inclusion-exclusion and Gumbel tests`. The proofs above cover all finite dimensions, all positive weights, all integer times, and the infinite-size limit; finite numerical checks are corroboration rather than proof.

## Relationship to prior work
Temme and Wocjan [1] construct quantized grand-coupling CPTP maps, including a hypercube random-refresh example. Their general Kraus expression [1, journal Eq. (55); arXiv v1 Eq. (56)] is an essential prior input. Section 5.2 identifies the classical coupon-collection time and provides its tail upper estimate; Section 6 explicitly raises whether a stationary-weight prefactor in the general quantum convergence bound can be removed. The present claim concerns the exact *diamond* distance for product-state refresh maps, sharpness via a no-ancilla input, arbitrary local pure states and site weights, and the full uniform Gumbel profile. It does **not** resolve the general prefactor question for interacting models or general grand couplings.

The classical coupon-collector distribution and cutoff are established probability theory [2], and classical hypercube total-variation mixing is established independently [3]. Neither classical result alone gives an exact quantum-channel diamond distance. The comparison with classical mixing is made in the same site-refresh normalization; it is not a priority claim for the classical cutoff.

## Limitations
The equality requires exactly commuting **pure-state replacement** maps. It is not asserted for partial thermalizations, coherent interactions, noncommuting refresh maps, mixed local targets, interacting Gibbs measures, or arbitrary quantized couplings. The channel diamond norm quantifies distinguishability with access to an arbitrary reference system; it is not a physical gate-count or implementation-complexity estimate. Nonuniform weights have the displayed exact finite formula but need not share the uniform Gumbel scaling. The possible presence of an unindexed earlier derivation of the exact channel norm cannot be excluded without an independent literature audit.

## References
[1] Kristan Temme and Pawel Wocjan, *Quantized Markov Chain Couplings that Prepare Qsamples*, arXiv:2504.02651v1 (first publicly posted 2025-04-03), later *Quantum* **9**, 1951 (2025), DOI: 10.22331/q-2025-12-18-1951. Relevant locations: arXiv version 1 Sections 3, 4, 5.2 and 6; journal Eq. (55), Section 5.2 and Section 6; arXiv v1 Kraus Eq. (56).

[2] David A. Levin and Yuval Peres, *Markov Chains and Mixing Times*, 2nd ed., AMS (2017), sections on coupling, coupon collection, and random walks on the hypercube.

[3] Persi Diaconis, Ronald L. Graham, and John A. Morrison, *Asymptotic analysis of a random walk on a hypercube with many dimensions*, *Random Structures & Algorithms* **1** (1990), 51–72, DOI: 10.1002/rsa.3240010105. The walk in [3] uses a different step normalization; the half-lazy normalization is derived explicitly here.
