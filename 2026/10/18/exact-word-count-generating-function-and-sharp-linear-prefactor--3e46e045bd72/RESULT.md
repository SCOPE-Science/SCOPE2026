# Exact word-count generating function and sharp linear prefactor for heterochaos baker codings

## Finding
For each integer \(M\ge2\), let \(A_{n,M}\) be the number of distinct length-\(n\) words in the canonical \(2M\)-cell symbolic coding of the generalized heterochaos baker maps of Takahasi–Yamamoto, with \(A_{0,M}=1\). Their coding theorem identifies this language with that of the \(M\)-type Dyck shift. Define the algebraic power series
\[
q_M(t)=\frac{1-\sqrt{1-4Mt^2}}{2Mt},\qquad q_M(0)=0.
\]
Then the **complete word-complexity generating function** is
\[
\boxed{\sum_{n\ge0}A_{n,M}t^n=\frac{1-q_M(t)}{[1-(M+1)t][1-Mq_M(t)]}.}
\]
For every fixed \(M\ge2\) and each \(\vartheta\) satisfying \(2\sqrt M/(M+1)<\vartheta<1\),
\[
\boxed{A_{n,M}=(M+1)^n\left[\frac{(M-1)^2}{M(M+1)}\,n+\frac{M+1}{M}+O_{M,\vartheta}(\vartheta^n)\right]}
\]
as \(n\to\infty\). The exponential remainder is in the **normalized** word count, not the unnormalized count. In particular, for \(M=2\),
\[
A_{n,2}=3^n\left(\frac{n+9}{6}+O_{\vartheta}(\vartheta^n)\right),\qquad \frac{2\sqrt2}{3}<\vartheta<1.
\]
Its first ten terms, for lengths \(0\) through \(9\), are \(1,4,14,48,160,528,1720,5568,17888,57216\). Consequently, the already-known entropy \(\log(M+1)\) has the sharper finite-word refinement
\[
\frac{\log A_{n,M}}n=\log(M+1)+\frac{\log n+\log\!\left(\frac{(M-1)^2}{M(M+1)}\right)}n+O_M(n^{-2}).
\]

## Assumptions and scope
The original two-dimensional family is the map \(f_a\) on \([0,1]^2\) for every \(0<a<1/M\), and the three-dimensional family is \(f_{a,b}\) on \([0,1]^3\) for every \(0<a,b<1/M\), with the \(2M\) specified cells and the associated **closed** one- or two-sided coding spaces of [1, Theorem A]. The parameter independence and identification with the Dyck shift are established in [1]; they are prerequisites, not newly proved or claimed here. We count words in the symbolic coding spaces, **not** distinguishable physical periodic orbits or physical trajectories, and do not assert that every infinite symbolic itinerary is realized by a unique point. The Dyck alphabet consists of \(M\) opening brackets \(\alpha_i\) and \(M\) closing brackets \(\beta_i\), for \(1\le i\le M\). Finite admissibility means that no internal matched pair has conflicting types, equivalently that its Dyck-monoid reduction is nonzero. This includes words with unmatched opening or unmatched closing brackets, which occur in bi-infinite admissible extensions. All parameters are strictly interior; \(M=1\) is excluded.

## Proof
**1. Coarse-word lifts.** Replace all \(\beta_i\) with a single closing symbol \(R\), keeping the \(M\) distinct \(\alpha_i\). For an arbitrary length-\(n\) coarse word \(w\), scan left-to-right, pushing the types of openers and popping the most recently unmatched opener whenever \(R\) is encountered with nonempty stack. If the stack is empty, an \(R\) is an unmatched closing bracket. Any close that pops an opener must have precisely the opener's type; an unmatched closing bracket can independently receive any one of the \(M\) closing types. Thus, for a fixed coarse word, its number of admissible typed lifts is \(M^{H(w)}\), where \(H(w)\) is its number of unmatched \(R\) steps.

Write \(S_j\) for the prefix count of \(R\) minus the count of all \(\alpha_i\), with \(S_0=0\). Each unmatched \(R\) increases the running record of \(S\) by one, so
\[
H(w)=\max_{0\le j\le n}S_j.
\]
There are \((M+1)^n\) equally weighted coarse words. Equivalently, with artificial independent walk increments \(+1\) of probability \(1/(M+1)\) and \(-1\) of probability \(M/(M+1)\), and \(H_n=\max_{0\le j\le n}S_j\),
\[
A_{n,M}=(M+1)^n\,\mathbb E[M^{H_n}]. \tag{1}
\]
This probability is a word-counting device, **not** a physical invariant distribution of the baker map.

**2. First-passage generating function.** Define \(T_k=\inf\{j\ge0:S_j=k\}\) for \(k\ge1\). Set
\[
\phi_M(z)=\mathbb E[z^{T_1};T_1<\infty].
\]
The first step is either an immediate upward passage or a downward step followed by two independent upcrossings. Therefore
\[
\phi_M(z)=\frac{z}{M+1}\bigl(1+M\phi_M(z)^2\bigr),\quad
\phi_M(z)=\frac{(M+1)-\sqrt{(M+1)^2-4Mz^2}}{2Mz}.
\]
The branch is the one vanishing at zero. The strong Markov property yields \(\mathbb E[z^{T_k};T_k<\infty]=\phi_M(z)^k\). By the exact identity
\[
M^{H_n}=1+\sum_{k\ge1}(M^k-M^{k-1})\mathbf1_{\{T_k\le n\}},
\]
nonnegative summation for \(0\le z<1\) gives
\[
\sum_{n\ge0}\mathbb E[M^{H_n}]z^n=
\frac1{1-z}\left(1+\sum_{k\ge1}(M^k-M^{k-1})\phi_M(z)^k\right)
=\frac{1-\phi_M(z)}{(1-z)(1-M\phi_M(z))}.
\]
Initially this holds for sufficiently small \(z\); its formal power series equality then follows coefficientwise. With \(z=(M+1)t\), (1) proves the boxed generating function.

**3. Singularity and sharp asymptotics.** The function \(\phi_M\) is holomorphic for \(|z|<R_M=(M+1)/(2\sqrt M)>1\). Its only possible denominator zero in this disk solves \(M\phi_M(z)=1\), which substituted into the quadratic first-passage equation forces \(z=1\). At \(z=1\),
\[
\phi_M(1)=\frac1M,\qquad
\phi_M'(1)=\frac{M+1}{M(M-1)},\qquad
\phi_M''(1)=\frac{2(M+1)(3M-1)}{M(M-1)^3}.
\]
The first-passage generating function therefore has a double pole at \(z=1\), with Laurent principal part
\[
\frac{1-\phi_M(z)}{(1-z)(1-M\phi_M(z))}
=\frac{(M-1)^2}{M(M+1)}\frac1{(1-z)^2}
+\frac4{M+1}\frac1{1-z}+\text{holomorphic remainder}.
\]
Subtracting both displayed pole terms leaves a function holomorphic on \(|z|<R_M\). For each \(1<r<R_M\), Cauchy's estimate bounds its Taylor coefficients by \(O_{M,r}(r^{-n})\). Extract coefficients and use \([z^n](1-z)^{-2}=n+1\) and
\[
\frac{(M-1)^2}{M(M+1)}+\frac4{M+1}=\frac{M+1}{M}
\]
to obtain the sharp formula, choosing \(r=1/\vartheta\). The logarithmic entropy refinement follows by taking \(\log\) and expanding \(\log(n+c)\).

## Verification
The companion standalone `verify.py` implements three independent finite checks using exact integers: direct enumeration of Dyck-admissible \(2M\)-letter words; dynamic programming for the coarse-walk maximum weight in (1); and formal-power-series extraction from the boxed generating function. It checks all \(n\le9\) for \(M=2\), all \(n\le7\) for \(M=3\), and all \(n\le5\) for \(M=4\), plus generating coefficients through \(n=18\) for each of these three choices. These computations support algebraic consistency but do not replace the infinite first-passage and analytic proof.

## Relationship to prior work
Takahasi and Yamamoto [1] prove the exact coding of the generalized heterochaos baker maps by the Dyck system, independent of the allowed map parameters, and discuss the two maximal-entropy measures of the symbolic system. The coding and the known value \(\log(M+1)\) of topological entropy are not new here. Saiki, Takahasi, and Yorke [2] introduced the original heterochaos baker maps. Takahasi's subsequent periodic-point study [3] counts periodic orbits and their distribution, rather than all finite admissible symbolic words. Inoue and Krieger [4] obtain Dyck-system zeta functions and entropy but do not state the present all-length word-count generating function or its sharp linear prefactor in the relevant inspected text. These prior results motivate the distinction between periodic-word growth, exponential entropy growth, and exact unrestricted finite-word complexity. The combinatorial maximum-walk technique is elementary in origin but its weighted all-length evaluation for these maps, including its two-term pole asymptotics, is the specific contribution.

## Limitations
Novelty has only been assessed against identified and inspected accessible literature; a combinatorially equivalent word-count formula may exist in an unindexed earlier source. Results concern symbolic word multiplicities, not the number of geometrically distinct points, the physical distribution of cells along Lebesgue-typical trajectories, or finite-precision implementations. The estimate is for fixed \(M\); uniformity when \(M\to\infty\) is unproved. The original known entropy and coding are hypotheses used, not independently reproved. The analytical proof does not assert that the all-length count determines periodic-point zeta functions.

## References
[1] H. Takahasi and K. Yamamoto, *Heterochaos baker maps and the Dyck system: maximal entropy measures and a mechanism for the breakdown of entropy approachability*, arXiv:2209.04905v1 (first posted 2022-09-11), Theorem A and Sections 1.2 and 2.

[2] Y. Saiki, H. Takahasi, and J. A. Yorke, *Piecewise Linear Maps with Heterogeneous Chaos*, arXiv:1811.01009 (2018).

[3] H. Takahasi, *Distributions of periodic points for the Dyck shift and the heterochaos baker maps*, arXiv:2409.01261 (2024).

[4] K. Inoue and W. Krieger, *Subshifts from sofic shifts and Dyck shifts, zeta functions and topological entropy*, arXiv:1001.1839 (2010).
