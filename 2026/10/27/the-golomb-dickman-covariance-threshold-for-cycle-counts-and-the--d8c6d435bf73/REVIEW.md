# Scientific review: cycle-count/maximum dependence

## Correctness — PASS
The claim is for a uniform random permutation, every \(n\ge2\), and each \(1\le j\le n\). Marking a particular \(j\)-cycle proves exactly that \(\mathbb E[C_{n,j}M_n]=j^{-1}\mathbb E\max(j,M_{n-j})\); it is not conditioning on there being a unique cycle. Growth by insertion supplies \(\mu_{r+1}-\mu_r\ge1/2\) from the uniform tagged-cycle law. The upper bound on \(\mathbb E(j-M_m)_+\) uses the same tagged-cycle law; with \(m=n-j\ge j\), the difference is strictly negative. For \(j>n/2\) the complementary maximum is bounded by \(n-j<j\), giving the exact identity \((j-\mu_n)/j\). Exhaustive enumeration through eight labels and 1,829 further exact-rational comparisons of all cases through sixty labels agree; the analytical proof, not these finite experiments, covers all cases. Shepp–Lloyd supplies the asymptotic constant, not a new finite-size lemma.

## Originality — PASS, with residual priority uncertainty
Full material inspected: Shepp–Lloyd on the cycle-class law and mean longest-cycle growth, Granville on cycle-length spectra and conditioned counts, Lugo on factorial moments of macroscopic cycle counts, and Betz–Schäfer on counts under prohibited long cycles. Shepp–Lloyd's Section 6 explicitly supplies an increment identity closely related to Step 2 of the proof, and Lugo's Proposition 1 supplies the classical joint factorial-moment kernel. These **do not themselves state** a finite all-length covariance sign boundary determined by the unconditional mean maximum. Neither an equivalent law under longest-component terminology nor a stronger joint theorem yielding the sign condition was located. This is a best-knowledge originality assessment, not an independence or exhaustive-historical-priority certificate. Full-text gaps in more distant earlier sources and differing terminology remain risks.

## Mathematical value — PASS
Cycle counts of a specific size and the size of the longest cycle are fundamental observables in random-permutation statistics and in random combinatorial structures. The sign is not fixed: short cycles suppress the maximum but sufficiently long cycles force it upward. The theorem completely locates their finite-sample reversal at the natural, independently studied mean maximum, with a uniform strict quantitative bound throughout the lower half of lengths and a clean exact expression throughout the upper half. The Golomb–Dickman constant becomes the sharp asymptotic switch point. It is more than a marginal distribution identity or an arbitrary finite parameter evaluation.

## Closest literature and limitations
- Shepp and Lloyd (1966): marginal longest-cycle distribution, growth bound, and cycle-class law; no stated \(C_{n,j}\)–\(M_n\) sign threshold.
- Granville (2006): cycle spectra; not the particular covariance classification.
- Lugo (2009): factorial moments for fixed and macroscopic cycle counts; does not include the largest-cycle covariance threshold.
- Betz and Schäfer (2016): cycle-count limit under long-cycle conditioning, not individual-count/maximum dependence.

The strongest priority risk is an older joint-cycle identity that implicitly subsumes the marked-cycle covariance. The result is deliberately limited to uniform permutations. No independent audit was performed.

Self-review: passed. Independent audit: not yet performed.
