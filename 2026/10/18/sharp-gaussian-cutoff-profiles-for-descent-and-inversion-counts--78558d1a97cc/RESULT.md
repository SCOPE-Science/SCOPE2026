# Sharp Gaussian cutoff profiles for descent and inversion counts in random-to-top shuffling

## Finding

Consider an initially ordered deck of \(n\) distinct cards. A random-to-top step selects one card uniformly from all \(n\) cards and moves it to the first position, including the possibility of selecting the current top card. Let \(D_{n,r}\) be the number of adjacent descents and \(I_{n,r}\) the number of inversions after \(r\) independent steps. Define the mean number of cards never selected by time \(r\) as
\[
 u_{n,r}=n(1-1/n)^r.
\]
**Theorem (sharp statistic-level Gaussian profile).** Let \(r=r_n\) be any sequence of nonnegative integers satisfying \(r_n/n\to\infty\). Set
\[
 Z_{D,n}=\frac{D_{n,r_n}-(n-1)/2}{\sqrt n},\quad
 Z_{I,n}=\frac{I_{n,r_n}-n(n-1)/4}{n^{3/2}}.
\]
If \(u_{n,r_n}/\sqrt n\to a\in[0,\infty)\), then
\[
 Z_{D,n}\Longrightarrow N(-a/2,1/12).
\]
If \(u_{n,r_n}/n^{3/4}\to b\in[0,\infty)\), then
\[
 Z_{I,n}\Longrightarrow N(-b^2/4,1/36).
\]
In the respective cases where the occupancy ratio tends to \(+\infty\), the corresponding centered statistic converges to \(-\infty\) in probability. Consequently, convergence to the stationary, centered Gaussian limit holds **if and only if** \(u_{n,r_n}=o(\sqrt n)\) for descents or \(u_{n,r_n}=o(n^{3/4})\) for inversions.

For each fixed real \(c\), write
\[
 r_{D,n}(c)=\left\lfloor\tfrac12n\log n+cn\right\rfloor,\qquad
 r_{I,n}(c)=\left\lfloor\tfrac14n\log n+cn\right\rfloor.
\]
At these respective windows the limits are \(N(-e^{-c}/2,1/12)\) and \(N(-e^{-2c}/4,1/36)\). If \(D_n^{\mathrm{stat}}\) and \(I_n^{\mathrm{stat}}\) count the same statistics under a uniformly random permutation, then the Kolmogorov distances of the *appropriately centered and scaled statistics* (equivalently, of the unscaled counts) have the exact limits
\[
\begin{aligned}
 d_K(D_{n,r_{D,n}(c)},D_n^{\mathrm{stat}})&\longrightarrow 2\Phi\bigl((\sqrt3/2)e^{-c}\bigr)-1,\\
 d_K(I_{n,r_{I,n}(c)},I_n^{\mathrm{stat}})&\longrightarrow 2\Phi\bigl((3/4)e^{-2c}\bigr)-1,
\end{aligned}
\]
where \(\Phi\) is the standard normal distribution function and \(d_K\) is the supremum distance between cumulative distribution functions. These are nontrivial strictly decreasing functions of \(c\), approaching one as \(c\to-\infty\) and zero as \(c\to+\infty\). The last two limits are limits of the **profile functions** after taking \(n\to\infty\) for fixed \(c\); no interchange of the two limits is asserted.

## Assumptions and scope

The deck starts in identity order, each card is equally likely to be selected at each discrete-time step, and all selections are independent. The asymptotic statement applies to every integer sequence \(r_n\) for which \(r_n/n\to\infty\). It concerns scalar descent or inversion counts, not convergence in total variation of the complete permutation to uniformity and not the whole descent-set process. The primary classification is MSC2020 60C05.

## Proof

**1. Occupancy concentration.** Let \(U=U_{n,r}\) be the number of cards never selected and \(K=n-U\). Let \(p_0=(1-1/n)^r\). Writing \(U\) as the sum of never-selected indicators gives
\[
 \mathbb E U=u=np_0,\qquad
 \operatorname{Var}(U)=np_0(1-p_0)+n(n-1)\bigl((1-2/n)^r-p_0^2\bigr)\le u,
\]
because \(1-2/n\le(1-1/n)^2\). The hypothesis \(r/n\to\infty\) implies \(u/n\to0\), and hence \(U/n\to0\) in probability by Markov's inequality. If \(u\to\infty\), then \(U/u\to1\) in probability since \(\operatorname{Var}(U)/u^2\le1/u\). If \(u/s_n\to a<\infty\) with \(s_n\ge\sqrt n\), then \((U-u)/s_n\to0\) in probability by Chebyshev's inequality, since \(u=o(n)\).

**2. The conditional ordered-suffix coupling.** Conditional on \(K=k\), the \(k\) moved cards form a uniformly random ordered \(k\)-tuple and the untouched cards remain in increasing initial order. Thus one can sample a uniform permutation \(\pi\), independently of \(K\), and transform it into \(\pi'\) by preserving the first \(K\) entries of \(\pi\) and sorting the remaining \(U\) entries increasingly. This exactly produces the law after \(r\) shuffles, for every finite \(n,r\). This established decomposition is used as the starting point, rather than being claimed as new.

**3. Descent perturbation.** Let \(A_i=\mathbf1\{\pi(i)>\pi(i+1)\}\) and \(D^*=\sum_{i=1}^{n-1}A_i\). The transformed deck has the first \(\max(K-1,0)\) descents from this same sequence, no descents within its sorted suffix, and at most one additional descent at the interface. Therefore, with \(B\in\{0,1\}\) and the natural convention at \(K=0,n\),
\[
 D_{n,r}=D^*-\sum_{i=\max(K,1)}^{n-1}A_i+B.
\]
The indicators \(A_i\) have mean \(1/2\), variance \(1/4\), covariance \(-1/12\) for neighbors, and zero covariance at distance at least two. They are independent of \(K\). Consequently, if the difference of the sum in the preceding display from \(U/2\) is absorbed with the bounded interface term into \(E_D\), then
\[
 D_{n,r}=D^*-U/2+E_D,\qquad
 \mathbb E E_D^2\le C(1+u)
\]
for an absolute constant \(C\). Indeed, conditional on \(K\), the centered tail has at most \(U\) summands and variance at most \(U/4\); for \(K=0\), the discrepancy between the tail length and \(U\) is exactly one. Because \(u=o(n)\), \(E_D/\sqrt n\to0\) in \(L^2\). The classical one-dependent central limit theorem gives
\[
 \frac{D^*-(n-1)/2}{\sqrt n}\Longrightarrow N(0,1/12).
\]
The asserted finite-shift law follows from step 1 and Slutsky's theorem. When \(u/\sqrt n\to\infty\), step 1 ensures \(U/u\to1\), while the Gaussian term remains tight and the remainder negligible; therefore the centered statistic tends to \(-\infty\) in probability.

**4. Inversion perturbation.** Under a uniform permutation the Lehmer contributions \(R_i=\#\{j>i:\pi(i)>\pi(j)\}\), for \(1\le i\le n\), are independent and uniformly distributed on \(\{0,\ldots,n-i\}\). Sorting the last \(U\) entries removes precisely their within-suffix inversion contributions, so
\[
 I_{n,r}=I^*-\sum_{i=K+1}^{n}R_i,
 \qquad I^*=\sum_{i=1}^{n}R_i.
\]
The last \(U\) summands, conditional on \(U\), have mean \(U(U-1)/4\) and variance
\[
 \sum_{j=0}^{U-1}\frac{j(j+2)}{12}
 =\frac{U(U-1)(2U+5)}{72}.
\]
Since \(0\le U/n\le1\) and \(U/n\to0\) in probability, bounded convergence gives \(\mathbb E[U^3]/n^3\to0\). Therefore the centered tail sum divided by \(n^{3/2}\) tends to zero in \(L^2\), and replacing \(U(U-1)\) with \(U^2\) creates a deterministic error bounded by \(1/(4\sqrt n)\). Thus
\[
 \frac{I_{n,r}-n(n-1)/4}{n^{3/2}}
 =\frac{I^*-n(n-1)/4}{n^{3/2}}-\frac{U^2}{4n^{3/2}}+o_{\mathbb P}(1).
\]
The independent-summand central limit theorem gives
\[
 \frac{I^*-n(n-1)/4}{n^{3/2}}\Longrightarrow N(0,1/36).
\]
Step 1 shows \(U/n^{3/4}\to b\) if \(u/n^{3/4}\to b<\infty\), and shows \(U/n^{3/4}\to\infty\) if the latter ratio diverges. This proves the inversion assertions.

**5. Sharp necessity and window profiles.** Suppose one occupancy ratio does not converge to zero. It has a subsequence converging in the compactified half-line to a strictly positive finite value or to \(+\infty\). Along that subsequence, steps 3–4 produce a shifted normal law or divergence to \(-\infty\), respectively, so convergence to the unshifted stationary Gaussian law is impossible. Hence the little-oh criteria are necessary as well as sufficient.

For fixed \(c\) and \(\alpha\in\{1/2,1/4\}\), setting \(r=\lfloor\alpha n\log n+cn\rfloor\) gives
\[
 u_{n,r}=n^{1-\alpha}e^{-c}(1+o(1)).
\]
Substituting the corresponding \(\alpha\) gives the two critical Gaussian shifts. Weak convergence to a continuous normal CDF is uniform in the CDF argument. Apply this elementary fact to both the shuffled statistic and its stationary comparator. For two normal CDFs with common variance \(\sigma^2\) and means separated by \(h\), the maximum absolute difference is \(2\Phi(|h|/(2\sigma))-1\), attained at the midpoint of the means. With \((h,\sigma)=(e^{-c}/2,1/\sqrt{12})\) and \((e^{-2c}/4,1/6)\), respectively, the displayed Kolmogorov profiles follow. This completes the proof.

## Verification

The standalone `verify.py` requires only the Python standard library. Run `python verify.py`. It enumerates the complete finite Markov chain for deck sizes \(3,4,5,6\), compares exact state probabilities after each step against an *independently computed* occupancy-mixture permutation law, checks exact inversion means, verifies all occupancy and Lehmer-tail moment formulas across further finite values, and checks the finite-size occupancy ratios in the Gaussian windows. All checks passed on the packaged version. These are independent finite consistency checks, not numerical proofs of asymptotic convergence; the proof above handles all \(n\) and the limiting statements.

## Relationship to prior work

Clay (2026, arXiv:2603.09008, version 2, Theorems 1.2–1.3 and 4.2–4.3) establishes the ordered-suffix representation, Gaussian limit laws in the \(r=cn\) regime, and sufficient conditions for an unshifted Gaussian law above the \(\tfrac12n\log n\) and \(\tfrac14n\log n\) scales, with diverging \(n\)-scale offsets. The present contribution is *not* a new proof of those decompositions: it treats the moving Gaussian-window regime, proves exact mean-shift profiles, sharp necessity in terms of occupancy means, and obtains statistic-level Kolmogorov cutoff curves. Clay's general fixed-density statements (Theorems 6.1 and 7.1) assume that the fraction of touched cards tends to a value strictly inside \((0,1)\), whereas the present results concern the boundary where this fraction tends to one. The paper explicitly leaves the intermediate \(n\ll r\ll n\log n\) ranges as directions for investigation.

Athanasiadis and Diaconis (2009/2010, arXiv:0912.1686, Proposition 5.9) provide stationary laws and convergence estimates for the **full descent-set** process of an associated walk. A full descent-set upper bound need not furnish a scalar count's lower bound or its exact Gaussian window profile; neither the inversion result nor either scalar profile follows from their displayed estimates. Feng (2026, arXiv:2604.09933) proves whole-deck probability-metric profiles for colored top-to-random shuffles at the later coupon-collector \(n\log n\) window. Its objective and scaling differ from the earlier scalar-statistic windows here.

## Limitations

The result does not claim total-variation mixing of the entire deck, a local limit theorem for individual statistic point masses, quantitative Berry–Esseen rates, or joint Gaussian limits of the two statistics. Independent literature-priority assessment remains to be done; a more general previously published functional-statistic theorem might subsume some of these asymptotics. The proof depends on a known exact ordered-suffix decomposition, so originality attaches to the complete sharp Gaussian-window and occupancy-boundary classification, not to that underlying coupling.

## References

1. A. Clay, *On the statistics of random-to-top shuffles*, arXiv:2603.09008, first publicly posted 9 March 2026, version 2 (8 April 2026), especially Theorems 1.2–1.3, 4.2–4.3, 6.1, 7.1 and Section 8. https://arxiv.org/pdf/2603.09008
2. C. A. Athanasiadis and P. Diaconis, *Functions of random walks on hyperplane arrangements*, arXiv:0912.1686 (2009), *Advances in Applied Mathematics* 45 (2010), 410–437, especially Proposition 5.9. https://arxiv.org/pdf/0912.1686
3. I. Z. Feng, *Explicit cutoff profiles for colored top-\(m\)-to-random shuffles*, arXiv:2604.09933 (2026), main results and introduction. https://arxiv.org/pdf/2604.09933
