# Joint spatial Poisson and Gaussian limits for long monotone runs and descents

## Finding

Let \(\pi_n\) be uniform on the permutations of \(\{1,\ldots,n\}\). For an integer \(2\le r\le n\), set
\[
 A_{i,+}=\mathbf 1\{\pi_n(i)<\cdots<\pi_n(i+r-1)\},\qquad
 A_{i,-}=\mathbf 1\{\pi_n(i)>\cdots>\pi_n(i+r-1)\},
\]
for \(1\le i\le n-r+1\). Their location-and-sign point process, a finite measure on \([0,1]\times\{+,-\}\), is
\[
 \Xi_{n,r}=\sum_{i=1}^{n-r+1}\bigl(A_{i,+}\delta_{(i/n,+)}+A_{i,-}\delta_{(i/n,-)}\bigr).
\]
Define the total number of descents and its fluctuation by
\[
 D_n=\sum_{i=1}^{n-1}\mathbf 1\{\pi_n(i)>\pi_n(i+1)\},\qquad
 Z_n=\frac{D_n-(n-1)/2}{\sqrt n}.
\]

**Theorem.** Along every sequence of pairs \((n,r)\) satisfying \(n\to\infty\), \(r\to\infty\), and \(n/r!\to\lambda\in(0,\infty)\),
\[
 (\Xi_{n,r},Z_n)\ \xrightarrow{\mathrm d}\
 (\Pi_+\otimes\delta_+ +\Pi_-\otimes\delta_-,\,G),
\]
where the processes \(\Pi_+\) and \(\Pi_-\) are independent homogeneous Poisson point processes on \([0,1]\), each with intensity \(\lambda\,dt\), and \(G\) is independent of both and normal with mean zero and variance \(1/12\). In particular, for every real \(x\),
\[
 \lim\Pr\{\Xi_{n,r}=0,\ Z_n\le x\}=e^{-2\lambda}\Phi(\sqrt{12}\,x).
\]
The location-and-mark assertion is stronger than marginal laws for the longest monotone run or for the descent count alone.

## Assumptions and scope

The permutation is uniform, and a *run window* means \(r\) **consecutive positions**, not an arbitrary increasing subsequence. The sign classes are separate even if their numerical mark notation is suppressed. Equivalently, take \(U_1,\ldots,U_n\) to be independent observations from any common atomless distribution and replace \(\pi_n\) by their relative ranks. Then the same events and joint law arise. The factorial-window regime is naturally observed on subsequences, e.g., by taking integers \(n\) nearest to \(\lambda r!\). Convergence of point measures means weak convergence on the compact marked space. No assertion is made for fixed \(r\), discrete distributions with ties, or a regime lacking a limit for \(n/r!\).

## Proof

**1. Local probabilities and dependence.** Work with independent atomless \(U_i\), so relative orderings of disjoint position sets are independent. Each signed window has probability \(1/r!\). For two length-\(r\) windows whose start positions differ by \(d\), \(1\le d<r\), two events of the same orientation occur together exactly when all \(r+d\) involved observations are ordered that way, with probability \(1/(r+d)!\). Opposite-orientation events cannot overlap on two or more positions, since at least one adjacent inequality conflicts. At distance \(d=r-1\), the windows share one observation; the shared point must be the unique maximum (up then down) or minimum (down then up), and the remaining two arms have prescribed orders. The probability is exactly
\[
 \frac1{(2r-1)((r-1)!)^2}.
\]
At equal start the two signs are exclusive. At distance at least \(r\), the windows are independent. Hence the expected number of ordered pairs of *distinct overlapping* positive window events anywhere in the sample is at most a universal constant times
\[
 n\sum_{d=1}^{r-1}\frac1{(r+d)!}
 + \frac{n}{(2r-1)((r-1)!)^2}
 =O\!\left(\frac{n}{r!\,r}+\frac{nr}{(r!)^2}\right)=o(1).
\]
Every step uses the full overlap classification, not a heuristic independence approximation.

**2. Separate rare events into independent blocks.** Put \(b=\lfloor n^{1/3}\rfloor\). Since \(n/r!\) has a positive finite limit, factorial growth implies \(r=o(b)\); also \(b=o(\sqrt n)\). Partition the first \(b\lfloor n/b\rfloor\) observations into independent blocks of length \(b\). Discard all marked windows not contained within a block. The expected discarded number is \(O(r/b+b/r!+r/r!)=o(1)\): at most \(O(nr/b+b+r)\) omitted starts, each with probability \(2/r!\). By Step 1, overlapping pairs within all blocks contribute \(o(1)\). Disjoint pairs within the same block contribute at most \(O(nb/(r!)^2)=o(1)\). Thus with probability tending to one, each block contains at most one retained signed window.

**3. Spatial marked Poisson limit.** Retained marked events from disjoint blocks are independent. A single block contains a plus event with probability \((b-r+1)/r!+o(b/n)\), and likewise for a minus event, because the expected number of multiple events across all blocks vanishes. The maximum block event probability is \(O(b/r!)=O(b/n)=o(1)\), and the sum of per-block plus and minus probabilities over blocks covering a fixed interval \((s,t]\subseteq[0,1]\) tends to \(\lambda(t-s)\) for each color. The characteristic or Laplace functional of these independent rare categorical blocks therefore converges to that of two independent, independently scattered Poisson processes with respective intensity \(\lambda\,dt\). Replacing each event position by the midpoint of its block changes its location by at most \(b/n\to0\); discarding the exceptional multi-event blocks changes the process with probability \(o(1)\). This proves the marked spatial limit.

**4. Gaussian descents from the same blocks.** Let \(T_j\) be the descent count among the \(b\) observations within complete block \(j\). The variables \(T_j\) are independent. The descent indicators are 1-dependent: each has variance \(1/4\), adjacent indicators have covariance \(-1/12\), and more distant indicators are independent. Therefore
\[
 \operatorname{Var}(D_n)=\frac{n+1}{12},\qquad
 \operatorname{Var}(T_j)=\frac{b+1}{12}.
\]
The missing boundary comparisons are mutually independent for \(b\ge3\), so their centered sum divided by \(\sqrt n\) has variance \(O(1/b)\); the incomplete terminal block changes the centered statistic by at most \(O(b/\sqrt n)=o(1)\). With \(|T_j-\mathbb ET_j|\le b=o(\sqrt n)\), the Lindeberg central limit theorem for independent blocks yields
\[
 \frac{\sum_j(T_j-\mathbb ET_j)}{\sqrt n}\Rightarrow N(0,1/12),\qquad
 Z_n\Rightarrow N(0,1/12).
\]

**5. Joint independence rather than marginal convergence.** Let \(F_j\) denote any bounded-by-one complex Laplace-factor determined by signed marked events in block \(j\), equal to \(1\) whenever the block contains no such event. Let \(p_j\) be the probability that block \(j\) contains at least one event. Because \(|T_j-\mathbb ET_j|\le b\), for each fixed real \(t\),
\[
 \bigl|\operatorname{Cov}(F_j,e^{it(T_j-\mathbb ET_j)/\sqrt n})\bigr|
 \le \frac{4|t|b}{\sqrt n}\,p_j.
\]
This follows by subtracting \(1\) from \(F_j\), centering the characteristic factor at \(1\), and using \(|e^{iu}-1|\le|u|\). Summing the bound over independent blocks costs at most
\[
 \frac{4|t|b}{\sqrt n}\sum_jp_j=O(b/\sqrt n)=o(1),
\]
since \(\sum_jp_j\le2(n-r+1)/r!=O(1)\). Thus the joint characteristic/Laplace functionals factor into the Gaussian part and both Poisson factors in the limit. Tightness follows from the established marginal limits. This proves the stated joint convergence and independence.

**6. Exact finite dependence check.** For \(W_{n,r}^{\pm}=\sum_iA_{i,\pm}\), conditioning on an increasing window makes its \(r-1\) internal descents vanish, while at each existing boundary the conditional descent probability becomes \(r/(r+1)\). Consequently, for every \(2\le r\le n\),
\[
 \operatorname{Cov}(D_n,W_{n,r}^{+})
 =-\frac{r-1}{2r!}\left((n-r+1)-\frac{2(n-r)}{r+1}\right),\qquad
 \operatorname{Cov}(D_n,W_{n,r}^{-})=-\operatorname{Cov}(D_n,W_{n,r}^{+}).
\]
These auxiliary exact identities illustrate that the finite signs are not independent of descents; the theorem proves independence only at their different limiting scales.

## Verification

Running `python3 verify.py` with Python 3.9 or later and no third-party packages returns `VERIFY_OK`. It exhaustively enumerates every permutation of orders 2 through 8 (46,232 permutations in total), performs 140 exact-rational mean/covariance assertions across all possible window lengths in those orders, and tests 20 overlap-probability identities through window length five using 414,990 ordered configurations. The verification code is supplied as a complete standalone artifact. These calculations test finite statements and proof components; they are not an exhaustive or computer-certified verification of the infinite limit. That limit rests on Steps 1–5.

## Relationship to prior work

The longstanding literature on monotone blocks and scan statistics analyzes maximum run lengths and one-color counts. Csáki and Földes (1996), Chryssaphinou and Vaggelatou (2001), and Amárioarei (2015) address overlapping-run or maximal-run questions. Novak's 1992 approximation, as discussed by Amárioarei, controls the scalar probability of no long increasing run; it does not itself assert three-way joint independence of two spatial point processes and the normalized global descent count. Johnson and Fu (2014) treat run and pattern-count distributional approximations. Janson, Nakamura, and Zeilberger (2013) address joint Gaussian behavior of *fixed-length classical* permutation patterns, a different regime from increasing consecutive lengths tending to infinity. The elementary univariate descent CLT is classical and is not a new component of the claim.

The asserted addition is the *joint marked spatial and global* limit, including both signs and independence from the global Gaussian statistic. Literature comparisons were made at the level of mathematical implications, not keyword matches. Full text of the especially relevant Chryssaphinou--Vaggelatou paper was unavailable, so its possible implicit coverage is an unresolved priority risk; no claim of definitive exhaustive novelty is made.

## Limitations

The theorem concerns uniform permutations (or the relative ranks of atomless i.i.d. observations) in the rare factorial-window regime. It does not establish rates for joint normal--Poisson convergence, does not cover nonuniform permutations or ties, and does not infer independence for finite \(n\). Exact boundary probabilities are asymptotic along admissible sequences of lengths, not uniform in arbitrary \(r\). Historical coverage by broad scan-statistic theorems or unavailable complete papers remains a risk. The cited 2013 source has a verified date of initial public preprint; older cited journal papers have not been assigned invented day-level public dates. No independent audit has been performed.

## References

1. E. Csáki and A. Földes, “On the length of the longest monotone block,” *Studia Scientiarum Mathematicarum Hungarica* **31** (1996), 35–46. Full-volume PDF: https://real-j.mtak.hu/5474/1/StudScientMath_31.pdf.
2. O. Chryssaphinou and E. Vaggelatou, “Compound Poisson approximation for long increasing sequences,” *Journal of Applied Probability* **38** (2001), 449–463. DOI: 10.1239/jap/996986755.
3. S. Janson, B. Nakamura, and D. Zeilberger, “On the asymptotic statistics of the number of occurrences of multiple permutation patterns,” preprint arXiv:1312.3955v1, initially submitted 2013-12-13, https://arxiv.org/abs/1312.3955.
4. B. C. Johnson and J. C. Fu, “Approximating the distributions of runs and patterns,” *Journal of Statistical Distributions and Applications* **1** (2014), article 5. DOI: 10.1186/2195-5832-1-5.
5. A. Amárioarei, “Approximations for the length of the longest monotone run in a sequence of i.i.d. random variables,” conference presentation, 2015-05-08. https://alexamarioarei.github.io/Research/docs/SPSR2015.pdf.
