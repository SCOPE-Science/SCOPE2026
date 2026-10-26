# A noncrossing variance-optimal pairing theorem for heterogeneous two-stage disease screening

## Finding

**Theorem.** Fix any integer \(m\geq1\) and \(2m\) independent binary infection statuses with probabilities \(p_i\in(0,1)\). Every specimen must be assigned to exactly one pool of size two; each pool receives one perfect assay, and a positive pool causes exactly two perfect individual retests. Sort the individual *noninfection* probabilities as \(0<q_1\leq\cdots\leq q_{2m}<1\), where \(q_i=1-p_i\).

Among all pair partitions, at least one partition minimizing the **variance** of the total number of assays is noncrossing in this sorted order: no two pairs have indices \(i<j<k<\ell\) with pairs \(\{i,k\}\) and \(\{j,\ell\}\). In particular, the exact minimum is found by the interval recurrence

\[
V(i,j)=\min_{\substack{i<k\leq j\\ k-i\;\mathrm{odd}}}\left\{q_iq_k(1-q_iq_k)+V(i+1,k-1)+V(k+1,j)\right\},
\]

for even-length intervals \([i,j]\), with \(V(i,j)=0\) for empty intervals. The minimum assay-count variance is \(4V(1,2m)\). The recurrence takes \(O(m^3)\) arithmetic operations and \(O(m^2)\) storage; backtracking returns an optimal pairing.

The noncrossing property remains true for *mixed* noninfection risks, even if some probabilities lie below \(1/2\) and others above it. Already with six people, the optimal matching need not be either the consecutively adjacent pairing or the opposite-extreme pairing.

## Assumptions and scope

Each person's infection indicator is independent of every other person's. The test response is exactly positive if one or both members of the tested pair are infected, and a positive pool triggers both individual tests regardless of their eventual outcomes. Individual assay results have no errors, delays, dilution effects or cross-pool dependencies. Pair size two is mandatory, and no singleton pools are permitted. Only the variance of the *total assay count* is optimized; the expected assay count and diagnostic quality are different criteria. Sorted ties are resolved arbitrarily and need not yield a unique optimum.

The result is exact for every \(m\geq1\), every vector of probabilities in the stated open range, and every perfect matching on the individuals. It does not claim that two-person pooling is preferable to direct individual testing in all prevalence ranges.

## Proof

**Reduction to a matching weight.** For any pair \(\{i,j\}\), its pool is negative with probability \(q_iq_j\). Its test count is \(1+2B_{ij}\), where \(B_{ij}\) indicates a positive pool and hence has success probability \(1-q_iq_j\). Pool indicators are independent across disjoint pairs. If \(T_M\) denotes the total test count for matching \(M\), then

\[
T_M=m+2\sum_{\{i,j\}\in M}B_{ij},\qquad
\operatorname{Var}(T_M)=4\sum_{\{i,j\}\in M}f(q_iq_j),
\quad f(t)=t(1-t).
\]

It therefore suffices to minimize the sum of edge weights \(f(q_iq_j)\) over perfect matchings.

**Four-point uncrossing inequality.** Write four ordered risk values as \(a\geq b\geq c\geq d\). Their three matching costs are

\[
P_{\rm sep}=f(ab)+f(cd),\quad
P_{\rm cross}=f(ac)+f(bd),\quad
P_{\rm nest}=f(ad)+f(bc).
\]

Direct expansion gives

\[
P_{\rm sep}-P_{\rm cross}=(a-d)(b-c)\bigl[1-(a+d)(b+c)\bigr],
\]
\[
P_{\rm cross}-P_{\rm nest}=(a-b)(c-d)\bigl[1-(a+b)(c+d)\bigr],
\]

and

\[
(a+d)(b+c)-(a+b)(c+d)=(a-c)(b-d)\geq0.
\]

If \((a+d)(b+c)\geq1\), then \(P_{\rm sep}\leq P_{\rm cross}\). Otherwise \((a+b)(c+d)<1\), and \(P_{\rm nest}\leq P_{\rm cross}\). Thus a crossing pair can always be uncrossed without increasing total cost.

**Existence of a noncrossing optimum.** Choose a minimum-cost perfect matching with the least total index-span \(\sum_{\{i,j\}\in M}|i-j|\), and among these choose one with the largest squared-span sum \(\sum_{\{i,j\}\in M}(i-j)^2\). If it contained crossing pairs \(i<j<k<\ell\) connected as \(\{i,k\},\{j,\ell\}\), the four-point inequality would permit one of two cost-nonincreasing replacements. The separated replacement \(\{i,j\},\{k,\ell\}\) **strictly decreases** total span by \(2(k-j)\). The nested replacement \(\{i,\ell\},\{j,k\}\) preserves total span but **strictly increases** squared-span sum by \(2(j-i)(\ell-k)\). Either contradicts the tie-breaking choice if cost stays optimal; a strict cost improvement would contradict optimality immediately. Therefore the selected optimum is noncrossing.

**Dynamic programming.** In any noncrossing matching on an even-length interval \([i,j]\), if \(i\) is paired to \(k\), then \(i+1,\ldots,k-1\) are matched among themselves, as are \(k+1,\ldots,j\). Both subintervals must have even size, which is equivalent to \(k-i\) being odd. Minimizing over \(k\) proves the displayed recurrence. There are \(O(m^2)\) even-length intervals and at most \(O(m)\) candidate partners in each; this proves the stated time and memory bounds.

**Six-person mixed-risk boundary.** Let the sorted noninfection probabilities be

\[
(q_1,q_2,q_3,q_4,q_5,q_6)=\frac17(1,2,3,4,5,6).
\]

The unique variance-minimizing pairing is \(\{1,4\},\{2,3\},\{5,6\}\), with edge-weight sum \(144/343=1008/2401\). The adjacent matching has sum \(1108/2401\), and the opposite-extreme matching has sum \(156/343=1092/2401\). For a complete certificate, the edge-weight numerators on denominator \(2401\) for all fifteen matchings, ordered by their three paired index strings, are:

| Paired indices | Numerator | Paired indices | Numerator | Paired indices | Numerator |
|---|---:|---|---:|---|---:|
| 12 34 56 | 1108 | 12 35 46 | 1204 | 12 36 45 | 1232 |
| 13 24 56 | 1036 | 13 25 46 | 1128 | 13 26 45 | 1162 |
| 14 23 56 | **1008** | 14 25 36 | 1128 | 14 26 35 | 1134 |
| 15 23 46 | 1078 | 15 24 36 | 1106 | 15 26 34 | 1108 |
| 16 23 45 | 1096 | 16 24 35 | 1096 | 16 25 34 | 1092 |

All rows are obtained by direct substitution into \(f(q_iq_j)\); the finite table is exhaustive because there are \(5\cdot3\cdot1=15\) perfect matchings. For four people, the four-point inequality ensures that one of just the adjacent and opposite-extreme matchings is optimal. Six is thus the smallest *even number of individuals* admitting a uniquely optimal pairing of neither of those two canonical forms.

## Verification

Run `python verify.py` in a directory containing `verify.py` and `verification_certificate.json`. The program uses only Python's standard library and exact `fractions.Fraction` arithmetic. It prints a single JSON object that must match `verification_certificate.json` byte-for-byte, apart from an optional final newline. It checks the four-point identities over 126 strictly ordered rational quadruples, computes exact optimal pairings over 219 complete risk profiles on four, six and eight people, enumerates all \(2^6\) infection outcomes for each of 1260 size-six matching/profile cases, and compares the dynamic program with all 945 pairings for each of fifteen size-ten profiles. The full fifteen-matching example above is checked separately.

These calculations verify stated finite certificates and implementation details. The global claim for every population size and every risk vector follows from the exact uncrossing and interval arguments in the proof, not from finite enumeration.

## Relationship to prior work

Dorfman's 1943 two-stage assay design introduces the initial-pool-then-retest mechanism. McMahan, Tebbs and Bilder (first published 15 July 2011) develop risk-ordered informative Dorfman screening, with objectives built around the **expected** number of tests, assay errors and pooling sizes. Bilder and Tebbs (first published 13 March 2012) examine heterogeneous screening procedures. Warasi and Das (first published 2 September 2024) study pooling designs and an estimator's variance, distinguishing this from expected assay resource use. None of the inspected material supplies the present particular mixed-risk variance-minimization noncrossing criterion and complete interval recurrence. The high-risk and low-risk homogeneous-side rearrangement regimes alone do not determine the mixed-risk optimum, as the displayed six-person example demonstrates.

General minimum-weight perfect matching is a classical polynomial-time optimization problem. The new structural point here is the application-specific four-point inequality: *without requiring a one-sided global Monge sign*, it guarantees an optimum that is noncrossing in the order of individual infection risks. General matching algorithms remain available, and no superior asymptotic complexity over all such algorithms is claimed.

## Limitations

This result is not a claim of global priority over all matching-theory formulations. An unlocated equivalent result under ordered matching, anti-Monge quadrangle inequalities, or variance-focused group testing may exist. The 2011 article's direct full-text access was obstructed, although its indexed substantive method sections and publication information were available; undetected additional material there remains a residual comparison risk. The procedure assumes independent statuses and exact assay outcomes, mandatory two-person pools, and fixed pairings. With unrestricted individual testing, the variance objective can be trivially zero, so the forced-pooling constraint is essential. The variance optimum need not minimize mean assay use, and neither a variance optimum nor a small expected test count alone certifies practical safety or sensitivity.

## References

1. R. Dorfman, "The Detection of Defective Members of Large Populations," *Annals of Mathematical Statistics* 14 (1943), 436–440.
2. C. S. McMahan, J. M. Tebbs and C. R. Bilder, "Informative Dorfman Screening," *Biometrics* 68 (2012), 287–296; first published 15 July 2011. DOI: `10.1111/j.1541-0420.2011.01644.x`.
3. C. R. Bilder and J. M. Tebbs, "Pooled-Testing Procedures for Screening High Volume Clinical Specimens in Heterogeneous Populations," *Statistics in Medicine* 31 (2012), 3261–3268; first published 13 March 2012. DOI: `10.1002/sim.5334`.
4. M. S. Warasi and K. P. Das, "Optimizing Disease Surveillance Through Pooled Testing with Application to Infectious Diseases," *Journal of Agricultural, Biological and Environmental Statistics* (first published 2 September 2024). DOI: `10.1007/s13253-024-00646-6`.
5. W. Cook and A. Rohe, "Computing Minimum-Weight Perfect Matchings," *INFORMS Journal on Computing* 11 (1999), 138–148. DOI: `10.1287/ijoc.11.2.138`.
