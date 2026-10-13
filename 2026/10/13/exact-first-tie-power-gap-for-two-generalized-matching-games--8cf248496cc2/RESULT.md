# Exact first-tie power gap for two generalized matching games

## Finding
For two independent matching games, each with \(n\ge4\) objects and a common skill probability \(0<\theta<1\), let \(K_1,K_2\) be their numbers of correct matches. Under no skill, write \(a=\Pr_0(K=0)\), \(b=\Pr_0(K=1)\), \(c=\Pr_0(K=2)\), \(A=b^2\), \(B=2ac\), and \(\beta=\Pr_0(K_1+K_2\ge3)\). All of \(a,b,c,A,B\) are positive.

For **every** significance level \(\alpha\in[\beta,\beta+A+B]\), a uniformly most powerful level-\(\alpha\) test of no skill versus any positive skill rejects whenever \(K_1+K_2\ge3\). Within the tied total \(K_1+K_2=2\), it first rejects the balanced outcome \((1,1)\) and only then, if necessary, the equally informative outcomes \((0,2)\), \((2,0)\); it can randomize at the cutoff. Outcomes with total at most one are never rejected in this level band.

The **most powerful test restricted to the total** \(K_1+K_2\) rejects totals at least three and randomizes uniformly at total two with rejection probability \((\alpha-\beta)/(A+B)\). The exact improvement in power of the full-data test over this total-only test is
\[
\Delta_{n,\theta}(\alpha)=\frac{AB}{A+B}\,n\theta^2(1-\theta)^{2n-2}
\min\!\left\{\frac{\alpha-\beta}{A},\frac{\beta+A+B-\alpha}{B}\right\}.
\]
It is strictly positive at all interior significance levels and zero at the endpoints. At its peak \(\alpha_*=\beta+A\), if \(\theta=\lambda/n\) for fixed \(\lambda>0\), then
\[
\lim_{n\to\infty}n\Delta_{n,\lambda/n}(\alpha_*)
=\frac{\lambda^2}{2}e^{-2(1+\lambda)},\qquad
\lim_{n\to\infty}\alpha_*=1-4e^{-2}.
\]

## Assumptions and scope
For each independent game, first independently label every object as known with probability \(\theta\); retain known objects in their correct positions, and uniformly permute the remaining objects. Let \(F_j\) count the fixed points of a uniform random permutation of \(j\) objects, with \(F_0=0\). If \(L\sim\operatorname{Bin}(n,\theta)\), the observed total is \(K=L+F_{n-L}\). Two games use independent labels and permutations. All tests considered are possibly randomized measurable functions of the two observed match counts. A level-\(\alpha\) test has rejection probability at most \(\alpha\) under \(\theta=0\). The uniformly most powerful assertion is within the entire composite alternative \(0<\theta<1\), for each fixed \(n\) and \(\alpha\) in the specified interval.

## Proof
For integer \(0\le k\le n\), the uniform-permutation fixed-point mass is
\[
p_0(k)=\frac1{k!}\sum_{j=0}^{n-k}\frac{(-1)^j}{j!}.
\]
This follows by choosing the \(k\) fixed points and deranging the remainder; it is zero at \(k=n-1\), and strictly positive at \(k=0,1,2\) for \(n\ge4\). Direct conditioning on \(L\), followed by rearranging the binomial coefficients, gives, on the positive-probability support,
\[
R_k(\theta):=\frac{p_\theta(k)}{p_0(k)}
=(1-\theta)^n Q_k(r),\quad r=\frac\theta{1-\theta},\quad
Q_k(r)=\sum_{j=0}^k\binom{k}{j}(n)_j r^j,
\]
where \((n)_j=n(n-1)\cdots(n-j+1)\) and \((n)_0=1\). The identity can equally be verified directly from \(p_\theta(k)=\sum_{\ell=0}^k\binom n\ell\theta^\ell(1-\theta)^{n-\ell}p_0^{(n-\ell)}(k-\ell)\). For \(r>0\), \(Q_k\) strictly increases with \(k\) on the support, because its binomial-coefficient expansion has positive coefficients, including a strictly increasing linear term.

The first four polynomials are
\[
Q_0=1,\quad Q_1=1+nr,\quad Q_2=1+2nr+n(n-1)r^2,\quad
Q_3=1+3nr+3n(n-1)r^2+n(n-1)(n-2)r^3.
\]
Two exact comparisons are
\[
Q_1^2-Q_0Q_2=nr^2>0,
\quad Q_0Q_3-Q_1^2=nr+n(2n-3)r^2+n(n-1)(n-2)r^3>0.
\]
The first says that among outcomes with total two, \((1,1)\) has a larger likelihood ratio than \((0,2)\) or \((2,0)\). The second, together with \(Q_2>Q_1\) and coordinatewise monotonicity, says that **every** supported outcome with total at least three has larger likelihood ratio than \((1,1)\). Indeed, either one coordinate is at least three (compare to \((3,0)\)), or both coordinates are positive and one is at least two (compare to \((2,1)\)). For \(n=4\), the count three is not supported, so the first alternative does not arise with that count; all supported outcomes of total at least three are still covered by monotonicity. Every supported outcome of total at most one has smaller likelihood ratio than the two unbalanced total-two outcomes. These strict comparisons hold for every \(0<\theta<1\). The Neyman–Pearson lemma therefore proves the alternative-independent ordering and uniform optimality throughout the specified level band. Averaging likelihood ratios conditional on the total preserves the strict separation between totals at least three, total two, and totals at most one; hence the same upper-tail/randomized-boundary rule is most powerful even within the smaller class of total-measurable tests.

Write \(A=\Pr_0(1,1)=b^2\) and \(B=\Pr_0(0,2)+\Pr_0(2,0)=2ac\). For a level \(\alpha\le\beta+A\), the optimal test additionally rejects \((1,1)\) with probability \((\alpha-\beta)/A\); for \(\alpha\ge\beta+A\), it rejects \((1,1)\) surely and the two unbalanced outcomes with a common probability \((\alpha-\beta-A)/B\). Subtracting the power of the total-only randomized test yields a triangular power difference with maximum
\[
\frac{AB}{A+B}(R_1^2-R_0R_2).
\]
The polynomial identity above gives exactly \(R_1^2-R_0R_2=n\theta^2(1-\theta)^{2n-2}\), proving the claimed complete formula and strictness.

Finally, for every fixed nonnegative integer \(k\), the derangement formula gives \(\Pr(F_n=k)\to e^{-1}/k!\). Hence \(A\to e^{-2}\), \(B\to e^{-2}\), and \(AB/(A+B)\to e^{-2}/2\). With \(\theta=\lambda/n\), \(n^2\theta^2=\lambda^2\) and \((1-\theta)^{2n-2}\to e^{-2\lambda}\), proving the sharp local coefficient. The limiting null significance follows from \(\beta+A=1-a^2-2ab-2ac\).

## Verification
The standalone `verification.py` uses Python's exact `Fraction` arithmetic to reconstruct the finite-permutation masses, both independent-mixture mass formulas, the likelihood identities, and the entire triangular power profile at 32 rational parameter pairs and additional sparse-intensity cases. Execute `python3 verification.py` from the directory containing this result. The verifier does not serve as proof for the continuum in \(\theta\), the all-size statement, or the asymptotic limit; those follow from the explicit identities in the preceding section.

## Relationship to prior work
O'Neill's generalized matching distribution (first public preprint 2021; journal 2023) supplies the underlying two-stage model, its single-game likelihood ratios, and total-match testing proposals. Its discussion also suggests a likelihood-ratio test, so the mere possibility of improving a total-based test is already recognized. The present statement is a *specific exact refinement*: it identifies the first nontrivial two-game likelihood tie, establishes an alternative-independent UMP ordering over its full significance band, and computes the exact finite-parameter power gain and sparse-skill coefficient. Standard Neyman–Pearson optimality by itself does not supply that ordering or the gain; Poisson–binomial approximation concerns a different, asymptotic reduction.

## Limitations
The theorem concerns independent identical matching games and two trials, with \(n\ge4\). The significance interval is approximately between \(0.323\) and \(0.594\) for large \(n\); it does **not** settle optimal rules at conventional levels such as \(0.05\), nor describe longer trial sequences or heterogeneous skill probabilities. The optimum is among tests based on observed match counts, not full permutations or knowledge labels. No claim of independent verification or exhaustive priority search is made. The exact power advantage vanishes as \(\theta\to0\) or \(\theta\to1\) at fixed \(n\).

## References
1. B. O'Neill, *A generalised matching distribution for the problem of coincidences*, arXiv:2112.12442 (first posted 2021-12-23); *Methodology and Computing in Applied Probability* 25, article 93 (2023), DOI 10.1007/s11009-023-10067-6.
2. N. Papadatos, *On corrected Poisson approximations for sums of independent indicators*, arXiv:2304.10314 (2023). This comparison concerns approximation of independent Bernoulli sums, not the exact finite-size matching-test likelihood ordering.
