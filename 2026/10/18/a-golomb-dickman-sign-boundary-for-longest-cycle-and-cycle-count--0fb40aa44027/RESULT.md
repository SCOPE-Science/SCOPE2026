# A Golomb–Dickman sign boundary for longest-cycle and cycle-count dependence

## Finding

Let a permutation of \(\{1,\ldots,n\}\) be uniform. Write \(M_n\) for the length of its longest cycle, \(C_{n,r}\) for the number of cycles of length \(r\), and \(a_n=\mathbb E[M_n]\). Set \(M_0=0\) and \(a_0=0\).

For every integer \(n\ge2\) and every \(1\le r\le n\),

\[
\operatorname{Cov}(M_n,C_{n,r})
=\frac{\mathbb E[\max\{r,M_{n-r}\}]-a_n}{r},
\qquad
\operatorname{sgn}\operatorname{Cov}(M_n,C_{n,r})
=\operatorname{sgn}(r-a_n).
\]

Thus small-cycle counts are negatively correlated with longest-cycle length, and large-cycle counts are positively correlated, with the **single exact sign boundary at the expected longest-cycle length**. Equality is characterized by \(r=a_n\); no assertion about existence of an integer equality case is necessary. More specifically, the covariance is strictly negative throughout \(1\le r\le n/2\), whereas for \(r>n/2\) it equals \((r-a_n)/r\).

Let \(\delta=\lim_{n\to\infty} a_n/n=0.6243299885\ldots\), the classical Golomb–Dickman constant. If \(r_n/n\to u\in(0,1]\) with \(u\ne\delta\), the covariance eventually has the sign of \(u-\delta\). If \(r_n/n\to u>1/2\), then

\[
\lim_{n\to\infty}\operatorname{Cov}(M_n,C_{n,r_n})
=1-\frac{\delta}{u}.
\]

## Assumptions and scope

Permutations are uniformly distributed on the finite symmetric group. The cycle count \(C_{n,r}\) counts disjoint permutation cycles, not consecutive patterns or cycles of a graph. The largest cycle is measured in number of labels. The entire finite statement holds for every integer \(n\ge2\) and every integer \(r\) from \(1\) through \(n\), including \(r=n\). The case \(n=1\) has deterministic statistics and zero covariance and is deliberately excluded from the strict-sign assertion.

The asymptotic statement only requires the classical existence and value of \(\delta\). In the regime \(r_n/n\to\delta\), the exact finite sign formula still applies, but a universal eventual strict sign is not claimed.

## Proof

**1. Marked-cycle identity.** Mark one cycle of length \(r\). The number of choices of its labeled support, internal cyclic ordering, and permutation of the remaining labels is

\[
\binom nr(r-1)!(n-r)!=\frac{n!}{r}.
\]

Consequently \(\mathbb E[C_{n,r}]=1/r\). Under the probability distribution induced by marking such a cycle, the permutation on the remaining \(n-r\) labels is uniform, and the longest cycle has length \(\max\{r,M_{n-r}\}\). Hence

\[
\mathbb E[M_nC_{n,r}]=\frac1r\,\mathbb E[\max\{r,M_{n-r}\}],
\]

which gives the first identity after subtracting \(a_n/r\).

**2. A uniform half-unit growth lower bound.** Coupling uniform permutations of \(k\) and \(k+1\) labels by the usual insertion rule, a new label either becomes a singleton cycle or is inserted immediately after one of the \(k\) old labels; each of the \(k+1\) choices has equal probability. Conditional on an existing permutation with longest-cycle size \(\ell\), insertion into any one selected longest cycle has probability \(\ell/(k+1)\), and on that event the longest length increases by one. It never decreases. Thus

\[
a_{k+1}-a_k\ge\frac{a_k}{k+1}.
\]

The cycle containing a specified label of a uniform permutation of \(k\) labels is uniform in length on \(\{1,\ldots,k\}\), as follows by counting cycles. Since \(M_k\) is at least the length of that cycle, \(a_k\ge(k+1)/2\); therefore

\[
a_{k+1}-a_k\ge\tfrac12\qquad(k\ge1).
\]

**3. Strict negativity for short marked cycles.** For \(r\le n/2\), put \(m=n-r\), so \(m\ge r\ge1\). For each integer \(1\le x\le m\), elementary comparison on the regions \(x\le r\) and \(x\ge r\) gives

\[
(r-x)_+\le r\left(1-\frac{x}{m}\right).
\]

Apply this inequality to \(M_m\) and use \(a_m\ge(m+1)/2\):

\[
\mathbb E[\max\{r,M_m\}]-a_m
=\mathbb E[(r-M_m)_+]
\le r\left(1-\frac{a_m}{m}\right)
\le\frac{r(m-1)}{2m}<\frac r2.
\]

By the preceding growth bound, \(a_n-a_m\ge r/2\). Therefore \(\mathbb E[\max\{r,M_m\}]<a_n\), and the marked-cycle identity yields \(\operatorname{Cov}(M_n,C_{n,r})<0\).

**4. Sharp sign boundary for long marked cycles.** If \(r>n/2\), then \(M_{n-r}\le n-r<r\) deterministically, and so

\[
\operatorname{Cov}(M_n,C_{n,r})=\frac{r-a_n}{r}.
\]

Because \(a_n\ge(n+1)/2\), every integer \(r\le n/2\) also satisfies \(r<a_n\). Combining the short and long regimes proves the sign classification, including the zero case if \(r=a_n\).

**5. Scaling boundary.** The classical longest-cycle mean limit gives \(a_n/n\to\delta\). Comparison of \(r_n/n\) and \(a_n/n\) gives the eventual sign whenever \(u\ne\delta\). If \(u>1/2\), then \(r_n>n/2\) for all sufficiently large \(n\), so the exact long-cycle covariance equals \(1-a_n/r_n\) and tends to \(1-\delta/u\).

## Verification

The included Python program `check.py` uses exact rational arithmetic and independent exhaustive permutation enumeration to test the marked-cycle identity and sign classification. It exhausts all permutations for \(2\le n\le8\). A separate longest-cycle cumulative-distribution recurrence checks all \(1\le r\le n\) for \(2\le n\le35\). The recurrence starts from \(F_{0,k}=1\), where \(F_{n,k}=\Pr(M_n\le k)\), and for \(n\ge1\) uses

\[
F_{n,k}=\frac1n\sum_{j=1}^{\min(n,k)}F_{n-j,k},\qquad
a_n=\sum_{k=0}^{n-1}(1-F_{n,k}).
\]

To reproduce, run `python3 check.py` using only the Python standard library. The program prints `PASS: exact recurrence n<=35; exhaustive permutation enumeration n<=8.` on success. These finite tests corroborate the formulas; the proof above establishes them for all allowed integers.

## Relationship to prior work

Shepp and Lloyd (1966) establish classical ordered-cycle laws, the cycle-type distribution, and the asymptotic mean longest-cycle constant. Their insertion construction is the basis for the growth comparison used here. The present result addresses a different mixed statistic: the covariance of the **largest cycle length** with the **count of cycles of a prescribed size**, including its all-size sign boundary. Their general cycle-type distribution can be used to reconstruct such a mixed moment in principle but does not itself state the sign classification.

Arratia, Barbour, and Tavaré (1999) establish Poisson–Dirichlet limits for longest components; those limits do not determine this exact finite-sample covariance. Shi (2014) studies joint correlations among *ordered longest-cycle lengths*, not the count of cycles of one fixed length. Results on covariance between total block counts and fixed-size block counts in uniform **set partitions** describe a distinct distribution and a distinct first statistic. Direct comparisons by mathematical implication did not identify an earlier statement covering the present all-parameter sign classification. Because exact cycle-index formulas predate this result, prior implicit derivability and uninspected general joint transforms remain genuine originality risks.

## Limitations

The theorem is restricted to **uniform** permutations; no claim is made for general Ewens parameters, biased permutations, or nonuniform cycle weights. The proof classifies signs and supplies an exact one-dimensional reduction, not a new explicit elementary closed formula for \(a_n\). It does not assert a fixed positive limit of covariance when \(r\) is fixed, or a universal eventual sign for sequences approaching the critical ratio \(\delta\). Finite numerical checks are not substitutes for the proof, and equivalent earlier formulas may remain outside the inspected literature.

## References

1. L. A. Shepp and S. P. Lloyd, “Ordered Cycle Lengths in a Random Permutation,” *Transactions of the American Mathematical Society* **121** (1966), 340–357. Open full text: https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Ordered-cycle-lengths-in-a-random-permutation.pdf . The printed paper records public presentation to the Society on 1965-09-02.
2. R. Arratia, A. D. Barbour, and S. Tavaré, “On Poisson–Dirichlet Limits for Random Decomposable Combinatorial Structures,” *Combinatorics, Probability and Computing* **8** (1999), 193–208. Author-accessible full text: https://www.columbia.edu/cu/simontavare/STpapers-pdf/ABT99b.pdf .
3. T. Shi, “Cycle Lengths of \(\theta\)-Biased Random Permutations,” Harvey Mudd College thesis (2014). Repository description: https://scholarship.claremont.edu/hmc_theses/65/ ; readable text: https://studylib.net/doc/7963369/biased-random-permutations .
4. V. Betz and H. Schäfer, “The number of cycles in random permutations without long cycles is asymptotically Gaussian,” arXiv:1605.08383 (2016). https://arxiv.org/abs/1605.08383 .
