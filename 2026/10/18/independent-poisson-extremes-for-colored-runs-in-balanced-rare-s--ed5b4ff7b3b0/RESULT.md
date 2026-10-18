# Independent Poisson extremes for colored runs in balanced rare-switch walks

## Finding

Let \(N\) range through the even positive integers. Choose a fair initial sign, and at each subsequent site repeat the previous sign with probability \(p_N=1-q_N\) or change it with probability \(q_N\). Condition on the **balanced endpoint** event \(C_N\) that exactly \(N/2\) signs are positive. Assume
\[
T_N=Nq_N\longrightarrow\infty,\qquad \frac{T_N^2}{N}\longrightarrow0.
\]
For every maximal constant-sign run \(R\), let \(\ell(R)\) be its length and \(\varepsilon(R)\in\{+,-\}\) its sign. Define the two random point measures
\[
\Xi_N^{\pm}=\sum_{R:\,\varepsilon(R)=\pm}
\delta_{(T_N/N)\ell(R)-\log T_N}.
\]
**Theorem.** Under the conditional law given \(C_N\), the pair \((\Xi_N^+,\Xi_N^-)\) converges jointly in distribution, in the vague topology of locally finite point measures on \(\mathbb R\), to **independent** Poisson point processes, each with intensity
\[
\frac12 e^{-x}\,dx.
\]
In particular, if \(M_N\) is the longest run of either sign, then for every real \(z\),
\[
\lim_{N\to\infty\atop N\ \mathrm{even}}
\mathbb P\!\left(\left.\frac{T_N}{N}M_N-\log T_N\le z\ \right|\ C_N\right)
=\exp(-e^{-z}).
\]
Moreover, the counts of positive and negative runs exceeding \((N/T_N)(\log T_N+z)\) converge jointly to independent Poisson variables of mean \(e^{-z}/2\) each. The joint point-process conclusion is stronger than the largest-run marginal.

At the unique center-versus-endpoint crossing of the persistent random walk, the known estimate \(q_N\sim (\log N)/N\) satisfies these hypotheses; thus the theorem applies at this physically motivated coexistence point. The crossing and this estimate are earlier results, not part of the new claim.

## Assumptions and scope

A sign word is \((\sigma_1,\ldots,\sigma_N)\in\{+,-\}^N\). Its number of switches is
\[
K_N=\sum_{j=1}^{N-1}\mathbf 1\{\sigma_j\ne\sigma_{j+1}\}.
\]
A run is a maximal nonempty consecutive block of identical signs, including possible boundary runs. The initial sign is fair, and all repeat/flip decisions are independent. The conditioning event \(C_N\) has positive probability for each even \(N\) and every \(0<q_N<1\). The hypotheses imply \(q_N\to0\). Statements concern the conditional finite-word law, not an unconditioned walk and not a fixed positive flip probability.

A locally finite point process may have infinitely many points toward \(-\infty\), but finite point count in each compact interval. Poisson point processes are specified by their Laplace functionals and have no atoms at fixed thresholds almost surely.

## Proof

### 1. Conditional switch count concentrates

Let \(m=N/2\), \(u_N=q_N/(1-q_N)\), and let \(W(N,m,k)\) count balanced sign words with exactly \(k\) switches. Since each such word has probability \(p_N^{N-1-k}q_N^k/2\), its conditional switch-count probability generating function is
\[
\mathbb E[s^{K_N}\mid C_N]
=\frac{S_N(su_N)}{S_N(u_N)},\qquad
S_N(u)=\sum_{k=1}^{N-1}W(N,m,k)u^k.
\]
The classical run-composition enumeration yields
\[
W(N,m,2j-1)=2\binom{m-1}{j-1}^2,\qquad
W(N,m,2j)=2\binom{m-1}{j}\binom{m-1}{j-1}.
\]
Write \(x_N=mu_N\) and \(F(x)=2x\bigl(I_0(2x)+I_1(2x)\bigr)\), with \(I_0,I_1\) the modified Bessel functions. The uniform clipped-product bound in Pemmasani's Theorem 3.3 states, for each \(x>0\),
\[
0\le 1-\frac{mS_N(x/m)}{F(x)}\le\frac{x(x+1)}{m}.
\]
It can also be read directly from the displayed binomial series using
\[
0\le 1-\frac{j!}{m^j}\binom{m-1}{j}\le\frac{j(j+1)}{2m},
\]
then summing nonnegative Bessel-series coefficients. Because \(x_N\sim T_N/2\to\infty\) and \(x_N^2/m=O(T_N^2/N)\to0\), this bound is uniform when \(x_N\) is multiplied by any factor in a fixed compact subset of \((0,\infty)\). The large-argument asymptotic
\[
F(x)=2\sqrt{x/\pi}\,e^{2x}(1+O(x^{-1}))
\]
therefore gives, uniformly for \(s\) in such a compact set,
\[
\log\mathbb E[s^{K_N}\mid C_N]
=2x_N(s-1)+\tfrac12\log s+o(1).
\]
Here \(2x_N=Nu_N=T_N+O(T_N^2/N)=T_N+o(1)\). Apply the exponential Markov inequality with \(s=\exp(\pm c\delta_N)\), where \(\delta_N=(\log T_N)^{-2}\) and \(0<c<1\) is fixed. Taylor expansion of the displayed logarithmic generating function then yields
\[
\mathbb P\bigl(|K_N-T_N|>T_N\delta_N\mid C_N\bigr)
\le 2\exp\bigl(-c_0T_N\delta_N^2+o(T_N\delta_N^2)\bigr)\longrightarrow0
\]
for a suitable constant \(c_0>0\) (choose \(c<1\) small). In particular, \(K_N/T_N\to1\) in conditional probability and \(|K_N/T_N-1|\log T_N\to0\).

### 2. Exact factorization at a fixed switch count

Fix \(K_N=k\ge1\) and the initial sign, under \(C_N\). There are \(k+1\) alternating runs. If \(r_+\) and \(r_-\) are their respective numbers, then \(r_++r_-=k+1\) and \(|r_+-r_-|\le1\). Their lengths are **independent uniform positive compositions** of \(m=N/2\) into \(r_+\) and \(r_-\) parts. Indeed, for fixed \(k\) every balanced word has the same Markov weight, and specifying two compositions uniquely reconstructs the word.

For \(r-1\) independent uniform cuts of \([0,1]\), their \(r\) spacings have the joint law
\[
(E_1,\ldots,E_r)/(E_1+\cdots+E_r),
\]
where the \(E_j\) are independent rate-one exponentials. Discretize each uniform cut onto the \(m-1\) interior integer cut locations. Conditional on no two cuts landing on the same location, the resulting positive composition is exactly uniform. The probability of a collision is \(O(r^2/m)\), and on the no-collision event every discrete part differs from \(m\) times the corresponding continuous spacing by at most \(2\).

On the high-probability switch-count event from Step 1, \(r_\pm=T_N/2+o(T_N)\), so \(r_\pm^2/m=O(T_N^2/N)\to0\). Furthermore, since the exponential sample mean is \(1+O_{\mathbb P}(r^{-1/2})\) and its largest observation is \(O_{\mathbb P}(\log r)\), the maximum difference between the rescaled discrete parts and the corresponding exponentials, over all parts, is \(o_{\mathbb P}(1)\). The coefficient is \(k/N\), and \(k/(2r_\pm)=1+O(1/k)\).

### 3. Colored Poisson limits

For \(r\) independent rate-one exponentials, the point process \(\sum_{j=1}^r\delta_{E_j-\log r}\) converges to a Poisson point process of intensity \(e^{-x}dx\). For example, for any nonnegative compactly supported continuous \(f\), its Laplace functional equals
\[
\left(1-\frac{1}{r}\int_{-\log r}^{\infty}
(1-e^{-f(x)})e^{-x}\,dx\right)^r
\longrightarrow
\exp\left(-\int_{\mathbb R}(1-e^{-f(x)})e^{-x}\,dx\right).
\]
For either run color, \(\log r_\pm-\log k\to-\log2\). Shifting the preceding Poisson limit by \(-\log2\) changes its intensity from \(e^{-x}dx\) to \(\tfrac12 e^{-x}dx\). The plus and minus composition arrays are independent conditional on \(k\) and the initial sign, so the two limiting point processes are independent. The conditional convergence is uniform over switch counts satisfying the high-probability concentration event: otherwise a deterministic subsequence of admissible switch counts would violate the just-established exponential-spacing argument.

Finally, replacing the normalization \((k/N)\ell-\log k\) by the asserted \((T_N/N)\ell-\log T_N\) changes the points in every bounded upper-tail window by \(o_{\mathbb P}(1)\). Indeed, the largest \((k/N)\ell\) is \(\log k+O_{\mathbb P}(1)\), so the absolute change is at most
\[
|T_N/k-1|\bigl(\log k+O_{\mathbb P}(1)\bigr)
+|\log(T_N/k)|=o_{\mathbb P}(1).
\]
The probability of inadmissible switch counts tends to zero by Step 1. This proves joint vague convergence of the colored processes.

### 4. Longest run and threshold counts

The superposition of the two limiting independent Poisson processes has intensity \(e^{-x}dx\). Its number of points above \(z\) is Poisson with mean \(\int_z^\infty e^{-x}dx=e^{-z}\), so the probability of no such point is \(\exp(-e^{-z})\). Each color contributes an independent Poisson count of mean \(e^{-z}/2\). Tightness of the maximum follows from the same exponential-spacing bound used in Step 2, allowing passage from vague convergence to the largest-run event. This completes the proof.

## Verification

The accompanying standalone script `verify.py` enumerates balanced binary words and separately computes capped run-composition counts for even lengths through fourteen. It verifies the finite conditional word enumeration exactly at every tested switch count and cap, and repeats the weighted comparison with exact rational odds. It also checks the nonasymptotic Bessel comparison at three larger even sizes using a direct positive-series evaluation. The executed script passed **285 assertions**. None of these finite computations is used as a substitute for the analytical Poisson-convergence proof.

## Relationship to prior work

Pemmasani (2026), arXiv:2610.06935v1, studies the central/endpoint tie, proves the classical switch-count formula and a finite uniform Bessel bound, and shows \(Nq_N\sim\log N\) at the tie. The present result uses those facts to determine the **joint, sign-resolved extreme-run process conditional on the balanced endpoint**, not the marginal bin crossing. The source paper's main theorem does not assert this extremal point-process law.

Fu, Wang and Lou (2003) derive exact longest-run distributions for two-state Markov trials and fixed-threshold large-deviation approximations. Their inspected Theorems 4.2–4.3 take the word length to infinity with a fixed run threshold and do not establish the balanced-endpoint rare-switch triangular-array law. Lou (1996) gives general finite-sample conditional longest-success-run calculations; its complete text was unavailable, so this is a priority risk rather than proof of absence. The normalized exponential-spacing representation and its extreme-value limit are classical ingredients; the claim of originality concerns their joint application with the balanced rare-switch conditional law and independent color splitting, not those ingredients separately.

## Limitations

The theorem assumes even word length, exact half-positive conditioning, symmetric switching, and \(T_N\to\infty\) with \(T_N^2/N\to0\). It makes no claim for fixed positive switching probability, bounded expected switches, unequal sign transition probabilities, or general endpoint conditioning. The sign-specific Poisson limits are weak convergence statements, not finite-sample distributional equalities. Independent assessment of priority and proof has not been conducted; prior exact conditional run work may contain stronger general asymptotics not identified in the accessible sources.

## References

1. Arjun Pemmasani, *Uniform Bessel bounds for endpoint crossings in the persistent random walk*, arXiv:2610.06935v1 (first submitted 2026-10-03), https://arxiv.org/html/2610.06935v1 .
2. James C. Fu, Liqun Wang, W. Y. Wendy Lou, *On exact and large deviation approximation for the distribution of the longest run in a sequence of two-state Markov dependent trials*, Journal of Applied Probability **40** (2003), 346–360, https://doi.org/10.1239/jap/1053003548 . Author-uploaded readable full text: https://www.researchgate.net/publication/305973350_On_exact_and_large_deviation_approximation_for_the_distribution_of_the_longest_run_in_a_sequence_of_two-state_Markov_dependent_trials .
3. W. Y. Wendy Lou, *On Runs and Longest Run Tests: A Method of Finite Markov Chain Imbedding*, Journal of the American Statistical Association **91** (1996), 1595–1601, https://doi.org/10.1080/01621459.1996.10476727 .
4. D. A. Darling, *On a class of problems related to the random division of an interval*, Annals of Mathematical Statistics **24** (1953), 239–253, https://doi.org/10.1214/aoms/1177729030 .
