# Exact chronological interval-overlap waiting laws and a two-Gumbel limit

## Finding
Let \(m\ge2\), and let \((Y_t)_{t\ge1}\) be independent identically distributed labels in \([m]\), with \(\Pr(Y_t=i)=p_i>0\) and \(\sum_{i=1}^m p_i=1\). For each prefix of length \(n\), form the empirical interval of label \(i\) from its first to last observed index (empty if unseen). Define \(T_m\) as the smallest \(n\) at which all \(m\) intervals have nonempty common intersection. Let \(\tau\) denote the first time all labels have appeared and \(L=Y_\tau\) the last discovered label. Then, almost surely,
\[
T_m=\tau+\inf\{s\ge0:\text{each label in }[m]\setminus\{L\}\text{ appears in }Y_{\tau+1},\ldots,Y_{\tau+s}\}.
\]
The suffix is independent of the past after \(\tau\). This gives the exact finite-sample law for arbitrary strictly positive \(p_i\): for every integer \(n\ge0\),
\[
\Pr(T_m\le n)=\sum_{t=1}^{n}\sum_{\ell=1}^m p_\ell A_\ell(t-1)B_\ell(n-t),
\]
where, writing \(p(S)=\sum_{i\in S}p_i\),
\[
A_\ell(u)=\sum_{S\subseteq[m]\setminus\{\ell\}}(-1)^{|S|}(1-p_\ell-p(S))^u,\qquad
B_\ell(v)=\sum_{S\subseteq[m]\setminus\{\ell\}}(-1)^{|S|}(1-p(S))^v.
\]
Here all integer exponents are nonnegative and \(0^0=1\) denotes the probability of avoiding any positive-probability event in an empty word.

In the uniform case \(p_i=1/m\), the law is a sum of **independent geometric waiting times**:
\[
T_m\ \stackrel{d}=\ \sum_{j=1}^{m}G_j+\sum_{j=1}^{m-1}G'_j,
\qquad G_j,G'_j\sim\operatorname{Geom}(j/m)
\]
with mutually independent variables and \(\Pr(\operatorname{Geom}(q)=k)=(1-q)^{k-1}q\) for integers \(k\ge1\). Consequently, for \(|z|\le1\),
\[
\mathbb E[z^{T_m}]=\prod_{j=1}^{m}\frac{jz}{m-(m-j)z}\prod_{j=1}^{m-1}\frac{jz}{m-(m-j)z},
\]
\[
\mathbb ET_m=2mH_m-1,\qquad
\operatorname{Var}(T_m)=2m^2H_m^{(2)}-2mH_m,
\]
where \(H_m=\sum_{j=1}^{m}j^{-1}\) and \(H_m^{(2)}=\sum_{j=1}^{m}j^{-2}\). The earliest possible completion time is \(2m-1\), attained with probability \(m!(m-1)!/m^{2m-1}\). Finally, as \(m\to\infty\),
\[
\frac{T_m-2m\log m}{m}\ \Longrightarrow\ G^{(1)}+G^{(2)},
\]
where \(G^{(1)},G^{(2)}\) are independent standard Gumbel random variables, each with CDF \(\Pr(G\le x)=\exp(-e^{-x})\).

## Assumptions and scope
Labels are iid, stationary and mutually exclusive at each observation index. All \(m\) probabilities are strictly positive. Singleton empirical intervals are allowed, and intervals are closed. The stopping time is measured in observations, not physical waiting time. The Gumbel limit is for the uniform law as \(m\to\infty\), and the exact finite-\(n\) formula holds for arbitrary positive probabilities.

## Proof
**Pathwise decomposition.** For each observed color, let \(a_i(n)\) and \(b_i(n)\) denote its first and last appearance indices through \(n\). Since these are closed real intervals, they share a common point if and only if all colors occur and \(\max_i a_i(n)\le\min_i b_i(n)\). Before \(\tau\), at least one color is absent. At and after \(\tau\), the greatest first appearance is exactly \(\tau\), because the final newly discovered color \(L\) occurs first at time \(\tau\). The last appearance of \(L\) is automatically at least \(\tau\). Every other label has its last appearance at least \(\tau\) if and only if it occurs at least once strictly after \(\tau\). This establishes the asserted identity simultaneously on every realization. The strong Markov property of the iid observations yields an independent fresh suffix after \(\tau\), conditional on \(L\).

**Nonuniform CDF.** The event \(\{\tau=t,L=\ell\}\) is the conjunction of (i) no \(\ell\) in the first \(t-1\) draws, (ii) every other color already seen, and (iii) \(Y_t=\ell\). Inclusion-exclusion gives probability \(p_\ell A_\ell(t-1)\). Independently, by inclusion-exclusion on the fresh suffix, the chance that all colors other than \(\ell\) occur at least once in its next \(v\) draws is \(B_\ell(v)\). Summing the mutually exclusive possibilities \((\tau,L)=(t,\ell)\) for \(t\le n\) proves the exact formula. In particular, \(\Pr(T_m\le n)=0\) for \(n<2m-1\), as all but the last newly appearing color must each appear once on each side of \(\tau\).

**Uniform geometric phases.** In the first phase, when \(m-j\) distinct labels have been collected, a fresh label arrives with chance \(j/m\). Successive waiting durations are independent geometric variables of parameters \(m/m,(m-1)/m,\ldots,1/m\). In the second phase there are \(m-1\) specified labels to collect; after \(m-1-j\) have appeared, the chance to see a still-needed specified label is \(j/m\), with \(j=m-1,\ldots,1\). These durations are likewise independent geometrics. The second-phase conditional distribution does not depend on which label was discovered last and, by the fresh-suffix property, its duration is independent of the entire first phase. This proves the law, PGF, exact mean and variance by multiplication and addition. Requiring each geometric variable to equal one gives the stated earliest-time probability.

**Gumbel limit.** Write \(C_m=\sum_{j=1}^m G_j\) and \(R_m=\sum_{j=1}^{m-1}G'_j\). Inclusion-exclusion for classical coupon collection gives, with \(r_m(x)=\lfloor m\log m+mx\rfloor\),
\[
\Pr(C_m\le r_m(x))=\sum_{k=0}^{m}(-1)^k\binom mk(1-k/m)^{r_m(x)}\longrightarrow\exp(-e^{-x}).
\]
For each fixed \(k\), the \(k\)-th term tends to \((-1)^ke^{-kx}/k!\); truncating the inclusion-exclusion formula at even and odd orders gives bounding Bonferroni partial sums, and then letting the truncation grow proves the limit without exchanging an uncontrolled infinite sum. Identically,
\[
\Pr(R_m\le r_m(x))=\sum_{k=0}^{m-1}(-1)^k\binom{m-1}k(1-k/m)^{r_m(x)}\longrightarrow\exp(-e^{-x}).
\]
The two phases are independent for every \(m\), so their joint centered-and-scaled law tends to that of independent standard Gumbels. The continuous mapping theorem applied to their sum completes the proof.

A corresponding exact expectation for general positive \(p_i\) follows from \(\mathbb ET_m=\mathbb E\tau+\sum_\ell\Pr(L=\ell)\mathbb ER_\ell\), with \(R_\ell\) the time to collect the other \(m-1\) labels. Its components have finite inclusion-exclusion formulas:
\[
\mathbb E\tau=\sum_{\varnothing\ne S\subseteq[m]}\frac{(-1)^{|S|+1}}{p(S)},\quad
\Pr(L=\ell)=p_\ell\sum_{S\subseteq[m]\setminus\{\ell\}}\frac{(-1)^{|S|}}{p_\ell+p(S)},\quad
\mathbb ER_\ell=\sum_{\varnothing\ne S\subseteq[m]\setminus\{\ell\}}\frac{(-1)^{|S|+1}}{p(S)}.
\]
All denominators are strictly positive by assumption. These follow by summing tail probabilities or from the independent-exponential poissonized coupon-collection identities (and can also be derived directly by geometric series).

## Verification
The independently written standard-library script `CHECK.py` constructs the direct empirical intervals, tests the pathwise criterion on every word in its stated finite ranges, independently enumerates exact rational nonuniform probabilities, and compares against inclusion-exclusion as well as the geometric moment formulas. Its run from the packaged bytes reports `PASS: 117928 independent exact finite assertions`. The finite checks are not the infinite proof; the displayed arguments establish the all-size identities and the limit.

For uniform labels, an alternative exact finite CDF uses Stirling numbers of the second kind \(S(q,r)\):
\[
\Pr(T_m\le n)=\frac1{m^n}\sum_{t=m}^{n}m!S(t-1,m-1)
\sum_{k=0}^{m-1}(-1)^k\binom{m-1}{k}(m-k)^{n-t}.
\]
The first factor counts surjective prefixes ending in the last new label, while the second counts suffixes including all the other labels. This independently matches the primary CDF formula.

## Relationship to prior work
De Loera, Jaramillo-Rodriguez, Oliveros and Torres introduce this empirical-interval sampling model. Their Theorem 12 supplies a lower bound for the probability of a complete simplex at a fixed sample size; their Theorem 13 supplies the bound \(\mathbb ET_m\le2\mathbb E\tau\), which is \(2mH_m\) in the uniform case. The exact pathwise identification, full arbitrary-probability CDF, independent-geometric distribution, sharp moments and two-Gumbel limit above refine those bounds. Standard coupon-collector calculations are used as known ingredients; the statement concerns the distinct *intersection-of-empirical-intervals* stopping event, not ordinary complete collection or the double-Dixie-cup stopping time. An accessible 2023 thesis on the same model repeats the expectation bound in its Section 4.4; it was not treated as a source of these exact formulas.

## Limitations
Only the stationary iid label model is treated. Physical time gaps, dependent sightings, changing sampling probabilities, and multidimensional observations are outside scope. A full historical-priority audit across all unpublished notes is not claimed. The limit is distributional, and no uniform finite-\(m\) Gumbel error bound is asserted.

## References
1. J. A. De Loera, E. Jaramillo-Rodriguez, D. Oliveros, and A. J. Torres, *A Model for Birdwatching and other Chronological Sampling Activities*, arXiv:2205.05743 (first posted 2022-05-11), *American Mathematical Monthly* 130 (2023), 541–558, https://arxiv.org/abs/2205.05743 , https://doi.org/10.1080/00029890.2023.2188036 . Relevant material: model definition in Section 1; Theorems 12 and 13 and Appendix in Section 3.
2. E. Jaramillo Rodriguez, *Combinatorial Analysis of Barcodes and Interval Graphs for Applications in Data Science*, doctoral dissertation, University of California, Davis, 2023, Section 4.4, https://escholarship.org/uc/item/0v78993q .
