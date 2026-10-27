# The Golomb–Dickman covariance threshold for cycle counts and the largest permutation cycle

## Finding
Let \(\Pi_n\) be a uniformly random permutation of \(\{1,\ldots,n\}\), let \(C_{n,j}\) count cycles of length \(j\), and let \(M_n\) be the largest cycle length. Write \(\mu_n=\mathbb E M_n\). For every integer \(n\ge2\) and every \(1\le j\le n\),
\[
\operatorname{sgn}\operatorname{Cov}(C_{n,j},M_n)=\operatorname{sgn}(j-\mu_n).
\]
Thus a cycle count at length \(j\) is negatively correlated with the largest cycle below the exact finite-sample threshold \(\mu_n\), positively correlated above it, and has zero covariance precisely if \(j=\mu_n\). The first positive length is \(\lfloor\mu_n\rfloor+1\). More precisely,
\[
\operatorname{Cov}(C_{n,j},M_n)
 =\frac{\mathbb E\max\{j,M_{n-j}\}-\mu_n}{j},
\]
with \(M_0=0\). This yields two explicit regimes:
\[
\begin{aligned}
1\le j\le n/2&:\quad
\operatorname{Cov}(C_{n,j},M_n)
\le-\frac{n-2j+1}{2(n-j)}<0,\\
n/2<j\le n&:\quad
\operatorname{Cov}(C_{n,j},M_n)=\frac{j-\mu_n}{j}.
\end{aligned}
\]
The classical Shepp–Lloyd longest-cycle limit \(\mu_n/n\to\lambda\), where \(\lambda=0.62432997\ldots\) is the Golomb–Dickman constant, therefore locates the positive-covariance onset at a fraction tending to \(\lambda\) of the permutation size. For any \(j_n/n\to x>1/2\),
\[
\operatorname{Cov}(C_{n,j_n},M_n)\longrightarrow 1-\lambda/x.
\]

## Assumptions and scope
The permutation is uniformly distributed over the symmetric group. All \(n\) and \(j\) in the stated integer ranges are covered, including \(j=n\), and no limit theorem is used for the finite-sample sign assertion. The convention for the empty permutation is \(M_0=0\). The theorem concerns a count of cycles of **exactly** one length, not the total cycle count, an arbitrary Ewens parameter, or nonuniform permutations. The displayed weak inequality in the short-cycle regime implies a strict sign because its right-hand side is strictly negative.

## Proof
**1. Marked-cycle identity.** For any functional \(F\) of the unordered cycle lengths, summing over all possible marked \(j\)-cycles gives
\[
\mathbb E[C_{n,j}F(\Pi_n)]
=\frac1j\,\mathbb E[F(\text{one }j\text{-cycle together with an independent uniform permutation of }n-j\text{ labels})].
\]
Indeed the number of candidate marked cycles is \(\binom nj(j-1)!\), each appearing with probability \((n-j)!/n!\), and their product equals \(1/j\). Consequently \(\mathbb E C_{n,j}=1/j\), and setting \(F=M_n\) gives the covariance identity in the Finding section. No conditional-on-existence substitution is being made: the marked-cycle identity is a **size-biased** moment formula even when multiple \(j\)-cycles can occur.

**2. A lower bound for mean-longest-cycle growth.** For a uniform permutation of \(r\) labels, the length \(U_r\) of the cycle containing label 1 is uniform on \(\{1,\ldots,r\}\), hence \(\mathbb E M_r\ge\mathbb E U_r=(r+1)/2\). Insert label \(r+1\) into a uniform permutation on \(r\) labels by either starting a singleton cycle or inserting after one of the \(r\) existing labels, with all \(r+1\) choices equally likely. The resulting permutation is uniform. Conditional on the old permutation, the largest cycle grows by at least one whenever the insertion follows any label in a chosen longest cycle, an event of probability at least \(M_r/(r+1)\). The largest cycle never shrinks under insertion. Therefore
\[
\mu_{r+1}-\mu_r\ge\frac{\mu_r}{r+1}\ge\frac12\qquad(r\ge1).
\]
By telescoping, for all nonnegative integers \(m\ge1\) and \(j\ge1\), \(\mu_{m+j}-\mu_m\ge j/2\).

**3. Every short-cycle covariance is strictly negative.** Assume \(1\le j\le n/2\) and write \(m=n-j\ge j\). As \(M_m\ge U_m\),
\[
\mathbb E\max(j,M_m)
=\mu_m+\mathbb E(j-M_m)_+
\le\mu_m+\mathbb E(j-U_m)_+
=\mu_m+\frac{j(j-1)}{2m}.
\]
The final equality sums \((j-u)/m\) for \(1\le u<j\). Combining with Step 2,
\[
\mathbb E\max(j,M_m)-\mu_n
\le\frac{j(j-1)}{2m}-\frac j2
=-\frac{j(n-2j+1)}{2(n-j)}<0.
\]
Division by \(j\) proves the stated quantitative bound.

**4. Long cycles and the exact transition.** For \(j>n/2\), the complementary permutation has at most \(n-j<j\) labels, hence \(\max(j,M_{n-j})=j\) identically. The marked-cycle identity gives \(\operatorname{Cov}(C_{n,j},M_n)=(j-\mu_n)/j\). Moreover \(\mu_n\ge(n+1)/2>n/2\), so every \(j\le n/2\) lies below \(\mu_n\). Steps 3 and 4 together prove the stated sign identity for every length, including the possibility of zero exactly when integer \(j\) equals \(\mu_n\). The positive lengths are exactly the integers strictly greater than \(\mu_n\), so the first is \(\lfloor\mu_n\rfloor+1\).

**5. Asymptotic placement.** Shepp and Lloyd prove that the mean largest cycle satisfies \(\mu_n/n\to\lambda\) for the Golomb–Dickman constant. Taking the integer part in the preceding exact threshold proves \((\lfloor\mu_n\rfloor+1)/n\to\lambda\). When \(j_n/n\to x>1/2\), the long-cycle exact formula applies eventually, and \((j_n-\mu_n)/j_n\to1-\lambda/x\).

## Verification
`check_cycle_max.py` is a standalone Python 3 standard-library verifier. It independently enumerates all permutations for \(n=1,\ldots,8\), computes the covariance directly from cycle decompositions, and matches the marked-cycle formula exactly using rational arithmetic. It also computes \(\Pr(M_n\le k)\) by the recurrence
\[
p_{0,k}=1,\qquad p_{n,k}=\frac1n\sum_{r=1}^{\min(k,n)}p_{n-r,k}\quad(n\ge1,k\ge1),
\]
which follows by conditioning on the uniform length of the cycle containing label 1. Summing the tails gives \(\mu_n=n-\sum_{k=1}^{n-1}p_{n,k}\). The verifier uses this exact recurrence to check the sign formula, the quantitative bound, and the long-cycle formula across all \(2\le n\le60\). `check_results.txt` records the executed tests: 36 exhaustive covariance comparisons and 1,829 exact-rational parameter comparisons. These tests support reproducibility but are not the proof for unbounded \(n\); Steps 1–5 supply that proof.

## Relationship to prior work
Shepp and Lloyd (1966) develop the cycle-class distribution and the asymptotic expected longest cycle and analyze single-step longest-cycle growth; their Sections 2, 4 and 6 contain important ingredients but not the above covariance-sign classification by **marked cycle length**. Granville (2006) studies Poisson-like distributions of cycle lengths and conditioned counts; Lugo (2009) derives joint factorial moments for counts of specified lengths, including macroscopic lengths; Betz and Schäfer (2016) prove a central limit theorem for the total number of cycles under long-cycle restrictions. These works concern related marginal laws and aggregate cycle counts. The present classification links an *individual* length-specific cycle count to the *maximum* and proves a finite sharp sign boundary equal to the mean maximum. The marked-cycle moment law and the mean-growth inequality are classical ingredients; the all-length covariance sign classification is the additional statement.

## Limitations
The finite-sample sign theorem is restricted to the uniform permutation law (Ewens parameter exactly one). An arbitrary Ewens parameter can alter the distribution of cycle lengths, so no extension is asserted. The constant \(\lambda\) and the marginal longest-cycle limit are classical; the new claim is the complete finite-sample covariance-sign connection and its consequent threshold. The proof does not determine whether \(\mu_n\) is ever an integer beyond the exact zero criterion, nor does it claim a distributional order conditional on \(C_{n,j}\). Literature priority remains subject to the possibility of older equivalent joint-dependence statements not identified by the searches.

## References
1. L. A. Shepp and S. P. Lloyd, *Ordered cycle lengths in a random permutation*, Transactions of the American Mathematical Society **121** (1966), 340–357. https://doi.org/10.1090/S0002-9947-1966-0195117-8 ; lawful text: https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Ordered-cycle-lengths-in-a-random-permutation.pdf.
2. Andrew Granville, *Cycle lengths in a permutation are typically Poisson*, Electronic Journal of Combinatorics **13** (2006), R107, published 2006-11-17. https://doi.org/10.37236/1133.
3. Michael Lugo, *The number of cycles of specified normalized length in permutations*, arXiv:0909.2909 (first version 2009-09-16). https://arxiv.org/abs/0909.2909.
4. Volker Betz and Helge Schäfer, *The number of cycles in random permutations without long cycles is asymptotically Gaussian*, arXiv:1605.08383 (first version 2016-05-26). https://arxiv.org/abs/1605.08383.
