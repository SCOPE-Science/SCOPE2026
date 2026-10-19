# Critical finite-population quartic diffusion for ratio-dependent contrarian triplets

## Finding

Consider a finite population of \(N\in6\mathbb N\) binary-opinion agents, freshly and uniformly partitioned into unordered three-agent groups at every discrete time step. Each group updates simultaneously by majority; independently for each of its three members, the majority output is reversed with probability \(a\) for an originally unanimous group, or \(b\) for an originally two-to-one group. Let \(P_m^{(N)}\) be the proportion holding opinion A after step \(m\).

**Critical stability boundary.** Fix \(0<a\le1/3\), set \(b=1/3-a\), and assume deterministic initial configurations satisfying \(N^{1/4}(P_0^{(N)}-1/2)\to z_0\in\mathbb R\). For each finite \(T>0\), in the Skorokhod space \(D([0,T])\),
\[
\left(N^{1/4}\big(P_{\lfloor \sqrt N t\rfloor}^{(N)}-1/2\big)\right)_{0\le t\le T}
\Longrightarrow (Z_t)_{0\le t\le T},
\qquad dZ_t=-8aZ_t^3\,dt+\sqrt{\tfrac16+2a^2}\,dB_t,
\quad Z_0=z_0.
\]
The diffusion is nonexplosive and has the unique invariant probability density
\[
\pi_a(z)=\frac{\exp(-4az^4/\sigma_a^2)}{\int_{\mathbb R}\exp(-4au^4/\sigma_a^2)\,du},
\qquad \sigma_a^2=\tfrac16+2a^2.
\]
Thus the natural critical fluctuation window is \(N^{-1/4}\), the round-count timescale is \(N^{1/2}\), and the limiting density is quartic, not Gaussian.

**Critical flip boundary.** Fix \(2/3\le a<1\) and \(b=5/3-a\). For \(Y_m^{(N)}=(-1)^m(P_m^{(N)}-1/2)\) and deterministic \(N^{1/4}Y_0^{(N)}\to z_0\), the same limit holds with \(a\) replaced throughout by \(1-a\):
\[
N^{1/4}Y_{\lfloor\sqrt N t\rfloor}^{(N)}\Longrightarrow\widetilde Z_t,
\quad d\widetilde Z_t=-8(1-a)\widetilde Z_t^3\,dt+
\sqrt{\tfrac16+2(1-a)^2}\,dB_t.
\]
The finite-population parity-corrected transition kernel is **exactly**, for every allowed \(N\), the lower-boundary kernel at complementary parameters \((1-a,1-b)\), not just asymptotically. The quartic densities here are invariant laws of the **limiting diffusions**; convergence of stationary distributions of the finite chains is not asserted.

## Assumptions and scope

Opinion A is coded \(1\) and B is coded \(0\); after observing an input triplet with \(k\in\{0,1,2,3\}\) A agents, the three updated outputs are conditionally independent Bernoulli variables of A-probability
\[
q_k=(a,b,1-b,1-a)_k.
\]
The random repartition is uniform over partitions into \(N/3\) unordered disjoint triples, independently at every step, and fresh Bernoulli choices are independent among agents and steps. Parameters \(a,b\in[0,1]\) are fixed, not \(N\)-dependent. The statement concerns finite-time weak convergence from the critical \(N^{-1/4}\) initial window, **not** arbitrarily distant initial conditions, joint \(N\)-dependent parameter perturbations, or first-passage times.

The primary model belongs to mathematical social dynamics (MSC2020 91D30). The comparison source's deterministic map is used as a premise; all finite-population variance and limiting-diffusion statements are separate assertions.

## Proof

**1. Exact one-step combinatorics.** Set \(J_m=NP_m\), condition on \(J_m=j\), let \((x)_r=x(x-1)\cdots(x-r+1)\), and put \(M=N/3\). The number \(K\) of A opinions in a uniformly sampled initial triplet satisfies
\[
\mathbb P(K=k\mid J_m=j)
=\frac{\binom3k(j)_k(N-j)_{3-k}}{(N)_3},
\quad k=0,1,2,3.
\]
For any two distinct groups, their initial A-counts \(K_1,K_2\) have the exact joint law
\[
\mathbb P(K_1=k,K_2=\ell\mid J_m=j)=
\frac{\binom3k\binom3\ell(j)_{k+\ell}(N-j)_{6-k-\ell}}{(N)_6}.
\]
The outgoing A count of one group, conditional on \(K=k\), is \(\operatorname{Bin}(3,q_k)\). Write \(\overline q_N=\mathbb E[q_K]\). Conditional independence of the Bernoulli outputs and exchangeability of groups give the *exact* relations
\[
\mathbb E[P_{m+1}\mid j]=\overline q_N,
\]
\[
\operatorname{Var}(J_{m+1}\mid j)=
3M\mathbb E[q_K(1-q_K)]
+9M\operatorname{Var}(q_K)
+9M(M-1)\operatorname{Cov}(q_{K_1},q_{K_2}).
\]
The negative inter-group covariance term is essential; treating group compositions as independent gives an incorrect diffusion coefficient.

**2. Uniform moment asymptotics.** Put \(p=j/N\). The hypergeometric one-group law differs from \(K\sim\operatorname{Bin}(3,p)\) by \(O(N^{-1})\) uniformly in \(0\le j\le N\). Therefore
\[
\mathbb E[P_{m+1}\mid j]=F(p)+O(N^{-1}),
\qquad F(p)=\sum_{k=0}^3\binom3k p^k(1-p)^{3-k}q_k.
\]
On every fixed compact interior subinterval \(p\in[\varepsilon,1-\varepsilon]\), expansion of the two-group falling factorial law yields
\[
\operatorname{Cov}(q_{K_1},q_{K_2})
=-\frac{\operatorname{Cov}(q_K,K)^2}{Np(1-p)}+O(N^{-2}),
\]
where expectations on the right use \(K\sim\operatorname{Bin}(3,p)\). One way to check the expansion is to divide the joint group law by the product of binomial laws: the first-order correction is
\[
\frac1N\left(15-\frac{k(k-1)+(\ell)(\ell-1)+2k\ell}{2p}
-\frac{(6-k-\ell)(5-k-\ell)}{2(1-p)}\right)+O(N^{-2});
\]
after centering against the one-group marginals, the only surviving cross-term is the stated negative covariance. Equivalently the joint-to-product-of-hypergeometric-marginals ratio has correction \(-[(k-3p)(\ell-3p)]/[Np(1-p)]\).
Thus
\[
N\operatorname{Var}(P_{m+1}\mid j)\longrightarrow
v(p)=\mathbb E[q_K(1-q_K)]
+3\operatorname{Var}(q_K)
-\frac{\operatorname{Cov}(q_K,K)^2}{p(1-p)}.
\]
In addition, a permutation-exposure bounded-differences argument yields, uniformly over all \(j\),
\[
\mathbb E\big[|J_{m+1}-\mathbb E(J_{m+1}\mid j)|^4\mid j\big]\le C N^2,
\qquad \operatorname{Var}(J_{m+1}\mid j)\le CN.
\]
Indeed, swapping two input labels in the permutation affects at most two groups (six output bits), and changing one independent update uniform affects one bit. Sequential exposure of these bounded perturbations gives sub-Gaussian concentration at variance scale \(N\), hence the displayed bounds.

**3. Critical cubic drift and exact noise.** Algebra gives, on the lower boundary \(b=1/3-a\),
\[
F(1/2+y)-1/2=y-8ay^3,
\qquad v(1/2)=\tfrac16+2a^2.
\]
For comparison, the upper critical boundary satisfies \(F(1/2+y)-1/2=-y+8(1-a)y^3\). Both identities and the two variance coefficients are checked symbolically in `check.py`.

Write \(h_N=N^{-1/2}\), \(Z_m^{(N)}=N^{1/4}(P_m-1/2)\), and \(\Delta Z=Z_{m+1}^{(N)}-Z_m^{(N)}\). On every compact set of rescaled states \(z\), the preceding estimates imply
\[
\frac{\mathbb E[\Delta Z\mid z]}{h_N}\to-8az^3,
\qquad
\frac{\mathbb E[(\Delta Z)^2\mid z]}{h_N}\to \sigma_a^2,
\qquad
\frac{\mathbb E[|\Delta Z|^4\mid z]}{h_N}\to0.
\]
The last estimate follows from the uniform fourth centered moment \(O(N^2)\) and the critical drift bound. Consequently the discrete generators converge uniformly on compact sets for smooth compactly supported test functions to
\[
\mathcal Lf(z)=-8az^3f'(z)+(\sigma_a^2/2)f''(z).
\]

**4. Compact containment and diffusion convergence.** For all physically admissible \(|y|\le1/2\), the lower-front deterministic map obeys \(|y-8ay^3|\le|y|\), because \(0<a\le1/3\). Combining that inequality with the uniform \(O(N^{-1})\) conditional-mean error and \(O(N^{-1})\) conditional proportion variance shows
\[
\mathbb E[(Z_{m+1}^{(N)})^2\mid Z_m^{(N)}=z]\le z^2+Ch_N
\]
with a constant independent of \(N,m,z\). Stopping when \(|Z|\ge R\) and applying the nonnegative supermartingale maximal bound gives
\[
\mathbb P\{\max_{m\le T\sqrt N}|Z_m^{(N)}|\ge R\}
\le\frac{\sup_N|Z_0^{(N)}|^2+C(T+1)}{R^2}.
\]
This establishes compact containment. The cubic-drift SDE has pathwise uniqueness and no explosion, since its drift is locally Lipschitz and \(z(-8az^3)\le0\). The standard martingale-problem diffusion approximation, using the preceding generator, jump, and tightness estimates, yields the claimed process convergence. Its strictly positive constant diffusion coefficient and dissipative confining drift give the unique invariant density by integrating the stationary zero-current equation, yielding the displayed quartic expression.

**5. Exact conjugacy across the flip boundary.** For upper parameters \((a,b)\) put lower parameters \((\widehat a,\widehat b)=(1-a,1-b)\). The four probabilities obey \(q_k^{\mathrm{upper}}=1-q_k^{\mathrm{lower}}\). Hence the entire one-step upper output law at any fixed input state is the spin-complement of the lower one-step output law, while simultaneous complementation of input and output leaves the lower kernel invariant. Thus the parity-adjusted deviations \((-1)^m(P_m-1/2)\) evolve *exactly* under the lower kernel, with \(\widehat a=1-a\in(0,1/3]\) and \(\widehat b=1/3-\widehat a\). Applying steps 1–4 proves the flip-boundary assertion.

## Verification

`check.py` requires Python 3 with SymPy and can be executed using `python check.py`. It checks the precise cubic mean map, the symbolic critical variances, exact six-agent grouping enumeration, exact finite-population moment formulas at six sizes for four parameter sets, and the entire seven-by-seven six-agent parity-conjugacy transition kernel. All assertions passed in a fresh execution. The finite computations check necessary identities and examples; the uniform asymptotic expansions, moment bounds, tightness argument and weak-convergence proof are mathematical arguments, not claims based on extrapolated numerics.

## Relationship to prior work

Galam (2026, DOI `10.3390/e28040443`, publicly available 2026-04-14) introduces these two contrarian probabilities and analyzes the deterministic cubic map and its fixed-point phases. The critical slope conditions and cubic map are **already implicit in that paper**. Galam's 2026 follow-up `arXiv:2607.02358` analyzes the microscopic stochastic interpretation and nonreversibility for the uniform-contrarian setting; it does not state this critical two-parameter diffusion limit. Noonan and Lambiotte (`arXiv:2101.03632`) derive Fokker–Planck approximations for majority-rule hypergraphs with **one interacting triplet per event**, no ratio-dependent contrarian activation and no simultaneous random partition into disjoint triplets.

The asserted incremental contribution is the exact \(N^{-1/4}\) and \(N^{1/2}\) finite-population critical limit **for the specified whole-population repartition model**, including the partition-corrected amplitude \(\sigma_a^2=1/6+2a^2\) and an exact parity conjugacy of both critical lines. General diffusion approximations, quartic critical potential mechanisms, and earlier deterministic phase boundaries are not asserted to be novel.

## Limitations

The finite-population implementation is an explicitly specified stochastic realization of Galam's group-update rules, rather than a claim that every alternative microscopic interpretation yields the same noise. The diffusion limit is for fixed parameters precisely on the two critical curves, and for initial fractions inside the critical window. No conclusion is drawn for microscopic detailed balance, finite-chain invariant measures, finite-\(N\) equilibrium-to-diffusion stationarity, voter exit probabilities, or off-critical parameters. The earliest verified public availability of the motivating 2026 source is its 2026-04-14 online publication, not the later arXiv upload. Prior specialized stochastic mean-field literature may contain an equivalent treatment under a different name; priority has not been independently audited.

## References

1. Serge Galam, *Ratio-Dependent Contrarian Activation in Opinion Dynamics*, Entropy 28(4), 443 (2026), published online 2026-04-14; DOI: `10.3390/e28040443`; https://www.mdpi.com/1099-4300/28/4/443; lawful preprint https://arxiv.org/abs/2604.27226.
2. Serge Galam, *Contrarian Majority Dynamics: Violation of Detailed Balance and Nonequilibrium Steady States* (2026), `arXiv:2607.02358`; https://arxiv.org/abs/2607.02358.
3. James Noonan and Renaud Lambiotte, *Dynamics of Majority Rule on Hypergraphs* (2021), `arXiv:2101.03632`; https://arxiv.org/abs/2101.03632.
4. S. N. Ethier and T. G. Kurtz, *Markov Processes: Characterization and Convergence* (1986), standard martingale-problem diffusion approximation framework.
