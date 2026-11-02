# Binary run-count likelihood-ratio balancing and the first three-color obstruction

## Finding

For fixed \(n\ge2\), draw uniformly from all binary words with \(k\) ones and \(n-k\) zeros, and let \(R_{n,k}\) count maximal nonempty constant-symbol runs. Define likelihood-ratio ordering for finite laws by \(P\le_{\mathrm{lr}}Q\) when \(P(r)Q(t)\ge P(t)Q(r)\) for every \(r<t\), including zero probabilities and endpoints.

**Theorem.** For every \(0\le k<\lfloor n/2\rfloor\),
\[
 R_{n,k}\le_{\mathrm{lr}}R_{n,k+1}.
\]
Thus all two-by-two minors in the ordered half-composition array are nonnegative. For \(1\le k<\lfloor n/2\rfloor\), stochastic dominance is strict, although adjacent run values can have equal likelihood ratios. The laws for the two central compositions at odd \(n\) coincide. For every exchangeable binary random vector \(X\) of length \(n\), without independence or infinite extendibility,
\[
 \Pr\{R(X)\ge t\}\le\Pr\{R_{n,\lfloor n/2\rfloor}\ge t\}
 \quad\text{for every integer }t.
\]
This upper envelope is attainable by the balanced fixed-composition law.

The likelihood-ratio conclusion does **not** extend to three positive symbol classes: at total length eight, moving counts \((3,1,4)\) to \((2,2,4)\) violates it. Eight is minimal for an elementary balancing move among three strictly positive classes (a finite exhaustive classification, not a statement about arbitrary alphabet sizes).

## Assumptions and scope

Words are linearly ordered; a run is a maximal consecutive group of equal symbols. All arrangements of any fixed composition have equal probability. In a three-color balancing step, one class count is decreased by one and another increased by one, with both old counts positive and their initial difference at least two; the third count is held fixed and all resulting counts remain positive. The result concerns likelihood-ratio order of the entire run-count distribution, which is stronger than an expectation comparison. The all-positive condition is essential for the asserted sharp cutoff eight; if zero-count colors are permitted, the first three-category counterexample occurs earlier.

## Proof

**Binary count.** Put \(m=n-k\), and write \(A_{n,k}(r)\) for the number of words with \(r\) runs. For \(1\le k\le n-1\), independent positive compositions of the one-runs and zero-runs give
\[
 A_{n,k}(2s)=2\binom{k-1}{s-1}\binom{m-1}{s-1},
\]
\[
 A_{n,k}(2s+1)=\binom{k-1}{s}\binom{m-1}{s-1}
 +\binom{k-1}{s-1}\binom{m-1}{s}
 =\frac{n-2s}{s}\binom{k-1}{s-1}\binom{m-1}{s-1}.
\]
Binomial coefficients outside their range are zero. If \(k=0\) or \(k=n\), the run count equals one. Normalization is \(\binom nk\).

**Adjacent likelihood ratio.** For \(1\le k<\lfloor n/2\rfloor\), on common positive support at run values \(2s\) and \(2s+1\), the ratio of *counts* in compositions \(k+1\) and \(k\) equals
\[
 h_s=\frac{k(n-k-s)}{(k-s+1)(n-k-1)}.
\]
For successive common-support pairs,
\[
 h_{s+1}-h_s=
 \frac{k(n-2k-1)}{(n-k-1)(k-s)(k-s+1)}>0.
\]
The two values within each pair share exactly the same ratio. At higher new-support run counts, the earlier count is zero and the later is nonnegative. Therefore every cross-product minor is nonnegative. At \(k=0\), the first distribution is concentrated at one run, so the order holds. Multiplying each row by its positive constant \(\binom nk^{-1}\) does not alter signs. Chaining adjacent likelihood-ratio orders gives the whole half-composition array. Symbol complementation sends \(k\) to \(n-k\), proving central symmetry. For the indicated strict steps, the probability of a sufficiently high number of runs increases strictly because the new composition permits additional alternations, so stochastic ordering is strict.

**Exchangeable envelope.** For an arbitrary finitely exchangeable binary law, conditioning on its number \(K\) of ones makes the word uniform over its \(\binom nK\) arrangements. Every conditional law of the runs is stochastically below the balanced law by the preceding order and complement symmetry. Average the conditional tail probabilities over \(K\); taking \(K\) balanced attains equality for all thresholds simultaneously.

**Three-color failure.** Let \(B_c(r)\) be the number of linear words with three-color counts \(c\) and \(r\) runs. For old counts \((3,1,4)\), the consecutive values at runs \(3,4,5,6,7,8\) are
\[
 (6,30,80,90,60,14),
\]
whereas after balancing to \((2,2,4)\) they are
\[
 (6,30,90,150,120,24).
\]
All other counts vanish. The total number of words is respectively \(280\) and \(420\). The likelihood-ratio minor at seven and eight runs, before normalization, is
\[
 60\cdot24-14\cdot120=-240<0.
\]
Thus balancing does not preserve likelihood-ratio ordering for a three-symbol alphabet.

**Sharp minimum in the all-positive three-color class.** A self-contained exhaustive recurrence is available for each composition \(c\) and the previous symbol \(j\). Let \(F(c,j;z)\) encode the number of future runs in the unplaced suffix, including a new run if the next symbol differs from \(j\). With \(F(0,j;z)=1\),
\[
 F(c,j;z)=\sum_{i:c_i>0}z^{\mathbf1\{i\ne j\}}F(c-e_i,i;z),
\]
where the initial previous symbol is a sentinel different from all three colors. This recurrence enumerates every word exactly once. The included exact-integer checker evaluates every positive three-color composition of each length \(3\le n\le7\), every possible elementary balancing move, and every run-pair minor. No negative minor occurs. The displayed eight-letter example therefore certifies the exact minimal length. The finite claim is exhaustive over its stated finite domain; the all-length binary theorem rests on the preceding algebra, not on finite experiments.

## Verification

Run `python verify_binary_runs_mlr.py` in the directory containing that file. The standalone checker independently enumerates all binary words up to length eleven, verifies the exact binary mass formula and likelihood-ratio minors through length forty, computes three-color word-count polynomials by a suffix recurrence, exhaustively tests every all-positive three-color balancing move through length seven, and checks the explicit length-eight obstruction. It reports `EXACT_ASSERTIONS=161557`. All arithmetic is exact integer arithmetic. This does not certify claims beyond the algebraically proved binary range or the stated exhaustive finite cutoff.

## Relationship to prior work

The classical fixed-composition run-count formula itself is **not** claimed as new: Mood's distribution theory, Schuster's exchangeable representation, and subsequent enumerative treatments predate the present comparison. Makri, Philippou, and Psillakis derive exact conditional run-statistic distributions useful for permutation tests. Balado and Silvestre's 2026 enumeration includes Hamming-weight constrained binary run counts; its exact formulas are also prior coverage of the enumerative layer. The present claim concerns cross-composition likelihood-ratio minors, the sharp finite-exchangeability upper-tail envelope, and the first all-positive three-color counterexample. Schuster and Gu's 1997 multisymbol run-distribution recurrences are a particularly relevant computational predecessor; the displayed three-color example can be checked independently of their formulation. Prior works on individual transition covariances and other conditional run statistics do not logically imply the all-threshold statements without additional arguments.

## Limitations

The counterexample excludes monotone likelihood-ratio ordering, not ordinary stochastic dominance, in three or more colors. No multicolor stochastic-order conjecture is proved or refuted here. The minimality cutoff applies exactly to three positive categories and one-unit balancing, and is supported by exhaustive exact recurrence rather than a symbolic classification. Historical-priority uncertainty remains around older conditional-run distribution texts that are not fully accessible; the 1991 Schuster article and 1997 Schuster--Gu paper are specifically relevant. Earlier publication of the 2007 issue precedes the precise publication day available in the selected date source, so the day field records verified day-specific evidence without asserting that no earlier undated public appearance existed. No independent audit has been performed.

## References

1. A. M. Mood (1940), *The distribution theory of runs*, Annals of Mathematical Statistics 11, 367--392.
2. E. F. Schuster (1991), *Distribution theory of runs via exchangeable random variables*, Statistics & Probability Letters 11, 379--386.
3. E. F. Schuster and X. Gu (1997), *On the conditional and unconditional distributions of the number of runs in a sample from a multisymbol alphabet*, Communications in Statistics--Simulation and Computation 26, 423--442. DOI: `10.1080/03610919708813389`.
4. F. S. Makri, A. N. Philippou and Z. M. Psillakis (2007), *Success run statistics defined on an urn model*, Advances in Applied Probability 39, 991--1019. DOI: `10.1239/aap/1198177236`. Primary MSC 60C05.
5. F. Balado and G. C. M. Silvestre (2026), *Systematic Enumeration of Fundamental Quantities Involving Runs in Binary Strings*, arXiv:2602.10005, especially Sections 4 and 7. This work is cited only for earlier enumeration and is not used as an archive-date anchor.
6. The source catalogue entry for reference 4 gives the day-specific public publication date 2008-02-20: `https://portal.mardi4nfdi.de/wiki/Success_run_statistics_defined_on_an_urn_model`. The original journal issue is dated December 2007, so priority should not be inferred from the catalogue day alone.
