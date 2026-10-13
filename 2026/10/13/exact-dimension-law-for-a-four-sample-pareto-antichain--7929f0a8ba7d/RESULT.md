# Exact dimension law for a four-sample Pareto antichain

## Finding
For any integer \(d\ge1\), let \(Z_1,\ldots,Z_4\) be independent and identically distributed random vectors in \(\mathbb R^d\). Assume that their coordinate components are mutually independent and that every marginal distribution is atomless. Write \(x\preceq y\) if each coordinate of \(x\) is at most the corresponding coordinate of \(y\). Two distinct vectors are *comparable* if one precedes the other; otherwise they are *incomparable*. Denote by \(A_d\) the event that all six unordered sample pairs are incomparable. Equivalently, all four sample observations are Pareto maximal.

Then the exact dimension law is
\[
\boxed{\mathbb P(A_d)=1-12\,2^{-d}+24\,3^{-d}+4\,4^{-d}-24(5/24)^d+6\,6^{-d}.}
\]
The law is strictly increasing as a function of the positive integer dimension. In particular,
\[
\mathbb P(A_2)=\frac1{24},\quad
\mathbb P(A_3)=\frac{151}{576},\quad
\mathbb P(A_4)=\frac{7207}{13824}>\frac12.
\]
Thus dimension four is exactly the first dimension in which a four-point random sample is more likely than not to be a Pareto antichain. Moreover,
\[
\mathbb P(A_d^{\mathrm c})=12\,2^{-d}-24\,3^{-d}+O(4^{-d})
\qquad(d\to\infty).
\]

## Assumptions and scope
The four vectors are i.i.d.; coordinate marginals can differ between coordinates, need not be uniform, and can be singular continuous. Atomlessness excludes ties with probability one. Independence between different coordinate components is essential. The number of observations is exactly four, while dimension is an arbitrary positive integer. No claim is made for dependent coordinates or a variable number of points. All probabilities and comparisons are with respect to the product order on real vectors.

## Proof
**Distribution-free rank reduction.** In each fixed coordinate, the four labels have one of the \(4!=24\) strict orders, each equally likely. Independence of coordinate components and of sampled vectors implies independence of these uniform orders across coordinates. Permuting labels lets us fix the first coordinate's ordering as \(1<2<3<4\) without affecting the desired probability.

There are six ordered pairs \((i,j)\) with \(1\le i<j\le4\). Since the first coordinate has \(Z_i<Z_j\) for each, the pair is incomparable in the full product order exactly when at least one of the other \(d-1\) coordinate orders puts \(j\) before \(i\). Let \(E_{ij}\) be the event that **none** of the remaining coordinate orders reverses that pair. Consequently
\[
A_d=\bigcap_{1\le i<j\le4}E_{ij}^{\mathrm c}.
\]

**Exact inclusion-exclusion.** For every subset \(S\) of the six pairs, let \(e(S)\) be the number of permutations of four labels in which \(i\) precedes \(j\) whenever \((i,j)\in S\); equivalently \(e(S)\) is the number of linear extensions of the induced acyclic poset. Every further independent coordinate has probability \(e(S)/24\) of satisfying all the corresponding pairwise constraints. Therefore
\[
\mathbb P(A_d)=\sum_{S\subseteq\{(i,j):1\le i<j\le4\}}
 (-1)^{|S|}\left(\frac{e(S)}{24}\right)^{d-1}.\tag{1}
\]
This is exact for all dimensions, including \(d=1\), when the empty product is one.

It remains to calculate a **finite and exhaustive** \(64\)-subset table. The columns below give each possible extension count, the number of subsets with that count, and the signed sum over them:

| \(e(S)\) | Number of subsets | \(\sum_{S:e(S)=e}(-1)^{|S|}\) |
|---:|---:|---:|
| 1 | 8 | 0 |
| 2 | 10 | 0 |
| 3 | 12 | 0 |
| 4 | 9 | 1 |
| 5 | 5 | -5 |
| 6 | 5 | 1 |
| 8 | 8 | 8 |
| 12 | 6 | -6 |
| 24 | 1 | 1 |

For reproducibility, enumerate the six bit positions in lexicographic pair order. For each of the \(2^6=64\) masks, test each of the \(24\) possible permutations against precisely the edges specified by the mask; increment the table's count and its parity sign. This is a *complete finite computation*, not a numerical experiment; the supplied standalone `verify.py` performs it and checks the stated table. In particular the middle column totals exactly \(64\), while all other extension counts are absent. Substitution into (1) yields
\[
\mathbb P(A_d)=1-6(1/2)^{d-1}+8(1/3)^{d-1}
 +(1/4)^{d-1}-5(5/24)^{d-1}+(1/6)^{d-1}.
\]
Reindexing powers gives the boxed formula.

**Strict increase and the dimension threshold.** Couple all dimensions using the first \(d\) coordinates of a single infinite sequence of independent coordinate-order permutations. Once any pair is incomparable it stays so when a coordinate is appended. Hence \(A_d\subseteq A_{d+1}\). The inclusion is strict with positive probability: if all first \(d\) coordinate orders agree and the next one reverses their common order, then the initial event fails but the extended event holds. Thus the probability strictly increases at every positive dimension. Direct exact substitution gives \(\mathbb P(A_3)=151/576<1/2\) and \(\mathbb P(A_4)=7207/13824>1/2\); consequently the first majority-antichain dimension is exactly four.

**Asymptotics.** Subtract the six-term formula from one. The two largest remaining bases are \(1/2\) and \(1/3\); all other bases are at most \(1/4\). This proves the stated two-term rare-comparability asymptotic and the convergence \(\mathbb P(A_d)\to1\).

## Verification
Run `python3 verify.py` with Python 3 standard library. The script independently enumerates all \(64\) subsets and all \(24\) permutation orders, verifies the signed extension-count table, compares the resulting identity against a separate inversion-mask dynamic program through dimension 12, and directly enumerates ordered permutation tuples through dimension 5. All arithmetic is exact rational/integer arithmetic. Passing these finite tests checks the finite enumeration; the rank coupling and probability argument establish all positive integer dimensions.

## Relationship to prior work
Răducan, Rădulescu, Rădulescu, and Zbăganu (2022), whose primary MSC includes 60E15, explicitly ask for the probability that a sample of independent uniform points in a higher-dimensional cube contains at least one comparable pair, noting the simple \(d=2\) answer and that they do not know the general \(d\ge3\) answer. Their full text develops different leader/anti-leader probabilities and properties and does not display the four-observation dimension law here. The complement of our formula answers that comparable-pair question **only for four observations**.

The known three-coordinate four-observation value \(151/576\) corresponds, after reversal of one permutation, to the \(n=4\) entry of OEIS A007767 on comparable pairs in the weak order of permutations. It is not claimed as a new count. Hammett and Pittel (2008) treat comparability in weak and strong permutation orders; this is related to the three-coordinate specialization, not an explicit arbitrary-coordinate dimension law in the material accessible for this comparison. The contribution claimed here is the finite six-term expression **valid for every dimension**, its distribution-free coordinate extension, and its exact first-majority dimension; there is no claim that every specialization is new.

## Limitations
No complete general-sample-size solution is established. Independence of coordinates cannot be removed by rank invariance. The finite exhaustive certificate is a deterministic calculation, not a formal proof assistant or external validation. Older literature about the full distribution of random Pareto-frontier sizes, including Barndorff-Nielsen and Sobel (1966), might contain an equivalent formula not located in this comparison. The full text of that older article and of Hammett and Pittel (2008) was not inspected here; originality should therefore be treated as a same-document-supported assessment with residual bibliographic risk, not independently certified priority.

## References
1. A. M. Răducan, C. Z. Rădulescu, M. Rădulescu, and G. Zbăganu, *On the Probability of Finding Extremes in a Random Set*, Mathematics **10** (2022), 1623. DOI: 10.3390/math10101623. First verified public date: 2022-05-10. Primary MSC: 60E15.
2. OEIS, *A007767: Number of pairs of permutations of degree n that avoid (12,21)*, https://oeis.org/A007767 (known integer \(151\) at four labels, equivalent under reversal).
3. A. Hammett and B. Pittel, *How often are two permutations comparable?*, Trans. Amer. Math. Soc. **360** (2008), 4541–4568. DOI: 10.1090/S0002-9947-08-04478-4; accessible 2006 manuscript abstract: arXiv:math/0605490.
4. O. Barndorff-Nielsen and M. Sobel, *On the distribution of the number of admissible points in a vector random sample*, Theory Probab. Appl. **11** (1966), 249–269 (historical related work; full text not inspected).
