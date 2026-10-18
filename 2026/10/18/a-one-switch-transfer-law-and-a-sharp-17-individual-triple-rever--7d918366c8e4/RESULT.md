# A one-switch transfer law and a sharp 17-individual triple reversal for rarefaction singletons

## Finding

Let a finite ecological census contain \(N\ge 2\) labeled individuals belonging to \(s\ge2\) species of strictly positive integer abundances \(\mathbf a=(a_1,\ldots,a_s)\), with \(\sum_i a_i=N\). Draw a uniformly random subset of \(m\) individuals without replacement. Write \(F_1(m)\) for the number of species represented **exactly once** in that sample. The expected singleton curve is \(S_{\mathbf a}(m)=\mathbb E[F_1(m)]\).

**Local one-switch theorem.** For any integer abundance transfer from \(a\) to \(b\) with \(a\ge b+2\), replacing those two species counts by \(a-1,b+1\) while retaining every other count, define \(\Delta_m=S_{\mathrm{after}}(m)-S_{\mathrm{before}}(m)\). Among the nonzero terms of \((\Delta_m)_{m=1}^{N}\), their signs change **exactly once**, from positive to negative. In particular, \(\Delta_2>0\), \(\Delta_{N-b+1}<0\), and there is never a second reversal. Zero differences are ignored in counting strict sign reversals.

**Sharp global failure of the one-switch property.** For two distinct, positive-integer abundance profiles of the same census size and **the same species count**, with the first strictly majorizing the second, the corresponding singleton-curve difference can have at least two strict sign reversals for the first time at \(N=17\). For \(N\le16\) there are no such comparable pairs. At \(N=17\) there is exactly **one** such pair up to permutation of species (the comparison direction is fixed by strict majorization):

\[
\mathbf a=(9,4,3,1)\succ\mathbf b=(7,6,2,2).
\]

For this pair, the complete exact numerator vector \(\bigl(\binom{17}{m}[S_{\mathbf b}(m)-S_{\mathbf a}(m)]\bigr)_{m=1}^{17}\) is

\[
(0,14,108,350,597,522,129,-112,9,114,-70,-306,-325,-186,-63,-12,-1).
\]

It has **three** strict sign reversals: between sample sizes \(7\) and \(8\), \(8\) and \(9\), and \(10\) and \(11\). The listed minimum and uniqueness are exact finite classification statements within the specified class, not claims about all pairs of distributions or infinite censuses.

## Assumptions and scope

The census is fixed; individuals are labeled, species identities are discrete, and every size-\(m\) subset of the \(N\) individuals has equal probability. The number of species remains the same in each comparison, and all abundances are positive. A strictly balancing transfer requires integers \(a\ge b+2\). For profiles sorted in nonincreasing order, \(\mathbf a\succ\mathbf b\) means their totals agree, their first \(j\) partial sums satisfy \(\sum_{i\le j}a_i\ge\sum_{i\le j}b_i\) for every \(j<s\), and at least one inequality is strict. Majorization permits multiple balancing transfers. Throughout, \(\binom uv=0\) when \(v<0\), \(v>u\), or \(u<0\).

The statistic \(F_1(m)\) is the **frequency-of-frequencies singleton count**, not total observed species richness, the number of truly singleton species in the underlying census, or an empirical estimator derived from independent sampling with replacement.

## Proof

**1. Exact hypergeometric identity.** A given species of abundance \(a_i\) is represented exactly once if the sample chooses one of its \(a_i\) individuals and chooses the other \(m-1\) individuals from the \(N-a_i\) outside the species. Therefore

\[
S_{\mathbf a}(m)=\frac{1}{\binom Nm}\sum_{i=1}^s a_i\binom{N-a_i}{m-1},\qquad 1\le m\le N.
\]

This is an established hypergeometric sample-abundance expectation and is not asserted as new.

**2. Exact local polynomial identity.** Fix two counts \(a\ge b+2\). The other species cancel from the difference. Put \(d=a-b-1\ge1\), \(M=N-a\ge0\), and let \(H_k=\binom N{k+1}\Delta_{k+1}\) for \(0\le k\le N-1\). Expanding the four affected species-count contributions gives

\[
\begin{aligned}
\sum_{k=0}^{N-1}H_kz^k
&=(a-1)(1+z)^{N-a+1}+(b+1)(1+z)^{N-b-1}\\
&\quad-a(1+z)^{N-a}-b(1+z)^{N-b}\\
&=(1+z)^M Q(z),\\
Q(z)&=(1+z)^d(1-bz)+(a-1)z-1.
\end{aligned}
\]

Write \(Q(z)=\sum_{j=0}^{d+1}q_jz^j\). Its coefficients satisfy

\[
q_0=0,\quad q_1=2d>0,\quad
q_j=\binom dj-b\binom d{j-1}\ \ (2\le j\le d+1).
\]

For \(1\le j\le d\), the ratio \(\binom dj/\binom d{j-1}=(d-j+1)/j\) strictly decreases with \(j\). Thus \((q_1,\ldots,q_{d+1})\) has a positive initial section, possibly a zero, then a negative final section; the last coefficient is \(q_{d+1}=-b<0\). In particular, it has exactly one positive-to-negative sign change after omitting zeros.

Multiplication of a polynomial by \(1+z\) transforms the coefficient sequence \((c_j)\) into the adjacent sums \((c_j+c_{j-1})\), taking absent boundary values as zero. If a coefficient sequence has all its positive entries before all its negative entries, this operation cannot introduce a second sign change: away from the unique boundary the sums retain the existing sign, and at that boundary only one sum mixes opposite signs. Induction on \(M\) shows that the coefficients of \((1+z)^M Q(z)\) have at most one sign change. Finally \(H_1=q_1=2d>0\) and the coefficient of \(z^{N-b}\) is \(-b<0\), since \(\deg((1+z)^M Q)=M+d+1=N-b\). Therefore there must be exactly one positive-to-negative sign change. Since \(\binom Nm>0\) for every \(1\le m\le N\), this proves the local theorem, including its boundary cases.

**3. An exhaustive and independently constructed finite classification.** Every positive-integer abundance profile of size \(N\) is uniquely represented up to relabeling by an integer partition of \(N\), sorted decreasingly. To compare profiles with the same number of species, group all partitions by length, and for each ordered distinct pair test the partial-sum inequalities defining strict majorization. For every passing pair, calculate the \(N\) exact integer numerators

\[
H_m(\mathbf a,\mathbf b)=\sum_i b_i\binom{N-b_i}{m-1}-\sum_i a_i\binom{N-a_i}{m-1}
\]

and count sign transitions after discarding zero entries. All operations are integer arithmetic.

The reproducible enumeration in `verify_singletons.py` covers **all** positive integer partitions for each \(2\le N\le17\), all same-length ordered strictly comparable profile pairs, and all sample sizes \(1\le m\le N\). Its counts of strictly majorization-comparable pairs for \(N=2,\ldots,17\), in order, are

\[
(0,0,1,2,7,13,30,55,106,182,336,551,947,1543,2549,4032).
\]

For \(2\le N\le16\) no pair has more than one strict sign reversal; at \(N=17\) exactly one pair has more than one, with exactly three, and it is the displayed \((9,4,3,1)\succ(7,6,2,2)\). Completeness follows because the partition-generation recurrence branches over every permissible next positive part no larger than its predecessor, and the two nested pair loops examine every ordered pair of equal-length partitions. The independent `verify_independent.py` enumerates all ordered compositions via all breakpoints before sorting to partitions, then independently repeats the comparison. Both methods agree on the complete classification.

For the 17-individual witness, `verify_singletons.py` additionally enumerates every one of the \(2^{17}\) labeled subsets **separately in each community**, tallies actual exactly-once species counts by sample size, and reproduces the same complete numerator vector. This gives a direct combinatorial check independent of the closed hypergeometric formula.

## Verification

Use Python 3 with the standard library only:

```
python3 verify_singletons.py
python3 verify_independent.py
```

The first program reports all partition and comparison counts for \(N=2,\ldots,17\), verifies the unique triple-reversal witness, checks the full set of \(2\cdot2^{17}\) labeled subsets for the witness, and confirms the local polynomial coefficients and one-switch pattern on 1378 allowable numerical transfer instances through \(N=27\). The second program independently reconstructs the complete partition census from binary composition breakpoints and finds the same unique anomalous comparison. Both programs were actually executed against these exact embedded source files before submission. Their finite enumeration is a proof of the stated **finite** minimum only because it covers the entire explicitly specified domain; it is not used to establish the unrestricted local theorem.

## Relationship to prior work

Classical rarefaction (Heck, van Belle and Simberloff, 1975) established formulas for expected observed richness and its sampling variance. Chao and Jost (2012) explain the role of singleton species in sample-coverage estimation. Sibuya (2003) reviews singleton categories in sampled populations. Shimadzu and Darnell (2015, Section 5.1) explicitly develop the hypergeometric abundance-spectrum expectation, which includes the displayed formula for sample singletons. These establish the base statistic and context; none of the inspected applicable materials establishes the local positive-to-negative one-switch theorem or the exact global minimal comparable-pair triple reversal under finite-census abundance majorization.

Zoroa and coauthors (2016) study majorization and species discovery in an urn model with **independent replacement draws**, with objectives concerning distinct categories rather than the finite-population singleton curve. Its results do not imply this classification. Neither the known monotone expectation of *total* rarefied richness under abundance balancing nor stochastic order of the species-accumulation process orders the expected number of categories seen **exactly once**. The three reversals therefore do not contradict monotonicity of expected total richness.

## Limitations

The sharp 17-individual statement is restricted to strictly positive integer abundance vectors with equal total size, equal number of species, and comparability by majorization. It is not a classification of every conceivable abundance pair, of different-richness comparisons, or of arbitrary noninteger probability laws. The local one-switch theorem concerns a single unit transfer, not every majorization comparison; the 17-individual witness itself requires multiple transfers. The statistic is an expectation, not the distribution or variance of singleton counts. Nothing here establishes inference performance or ecological outcomes in an observed ecosystem. The exact census supplies no asymptotic theorem on the maximum possible number of sign changes at unrestricted \(N\). Literature equivalences under other terminology remain possible; no independent bibliographic or scientific audit has been performed.

## References

1. Heck, K. L., van Belle, G., and Simberloff, D. (1975). *Explicit Calculation of the Rarefaction Diversity Measurement and the Determination of Sufficient Sample Size.* Ecology 56, 1459–1461. DOI: 10.2307/1934716. First published 1 October 1975. The accessible abstract describes expected richness and its variance, not the new singleton reversal statement.
2. Sibuya, M. (2003). *Number of Categories with a Singleton in Sample and Population.* Proceedings of the Institute of Statistical Mathematics 51(2), 261–295. https://www.ism.ac.jp/editsec/toukei/pdf/51-2-261.pdf. Japanese review with English synopsis on p. 295.
3. Chao, A., and Jost, L. (2012). *Coverage-based rarefaction and extrapolation: standardizing samples by completeness rather than size.* Ecology 93, 2533–2547. DOI: 10.1890/11-1952.1.
4. Shimadzu, H., and Darnell, R. (2015). *Attenuation of species abundance distributions by sampling.* Royal Society Open Science 2, 140219. DOI: 10.1098/rsos.140219. See §5.1 on hypergeometric sample-abundance spectra.
5. Zoroa, N., et al. (2016). *The coupon collector urn model with unequal probabilities in ecology and evolution.* arXiv:1608.00155. The paper's majorization comparisons concern sampling with replacement.
