# Sharp census thresholds for Shannon–Simpson evenness rankings

## Finding

Fix any integer number of present species \(s\ge3\). Compare two abundance vectors of \(s\) **positive integers**, each with the same total census \(N\ge s\), without distinguishing permutations of species labels. Let \({}^1E\) and \({}^2E\) be Hill evenness of orders one (exponentiated Shannon entropy divided by richness) and two (inverse Simpson concentration divided by richness).

There are two sharp, distinct thresholds:

1. If \(0\le N-s\le5\), the two indices give **identical weak rankings** of every pair of abundance multisets: neither index can break a tie of the other, and a strict preference has the same direction for both.
2. At \(N=s+6\), strict reversals remain impossible, but the rankings first cease to be identical: \({}^2E\) can tie two multisets that \({}^1E\) distinguishes. For \(s=3\) there is exactly one such unordered pair, up to relabeling; for every \(s\ge4\) there are exactly two. The universally available pair has counts \((2,2,5)\) versus \((1,4,4)\), padded on each side by \(s-3\) additional singleton species. The other pair, available when \(s\ge4\), has counts \((2,2,2,4)\) versus \((1,3,3,3)\), padded by \(s-4\) singletons.
3. The first **strict ranking reversal** occurs at \(N=s+7\). For every \(s\ge3\), it has exactly one unordered abundance-multiset pair (up to swapping the two communities):
   \[
   A=(\underbrace{1,\ldots,1}_{s-3},2,2,6),\qquad
   B=(\underbrace{1,\ldots,1}_{s-3},1,4,5).
   \]
   The directions are \({}^1E(A)>{}^1E(B)\) but \({}^2E(A)<{}^2E(B)\). Indeed, the exact comparison invariants are
   \[
   \sum_i A_i^2=s+41>s+39=\sum_i B_i^2,
   \qquad
   \prod_i A_i^{A_i}=746496<800000=\prod_i B_i^{B_i}.
   \]

For \(s=1\) or \(s=2\), a strict reversal is impossible at every census size. In particular, the **globally smallest positive-integer example** has three present species and ten individuals, and it is unique up to permutation and exchange of communities.

## Assumptions and scope

A community is a multiset \(a=(a_1,\ldots,a_s)\) of positive integer abundances with \(\sum_i a_i=N\), each species present. Define \(p_i=a_i/N\), entropy \(H(a)=-\sum_i p_i\log p_i\), and Hill evenness
\[
{}^1E(a)=\frac{e^{H(a)}}s,\qquad {}^2E(a)=\frac{1}{s\sum_i p_i^2}.
\]
Rankings are compared **only between communities with identical \(s\) and \(N\)**. The use of \(\sum p_i^2\) is the usual with-replacement Simpson concentration, not the finite-population without-replacement unbiased estimator. Two abundance multisets are considered the same if one is a permutation of the other. A *strict reversal* means that one index strictly favors one community and the other index strictly favors the other. A *tie disagreement* means exactly one index is tied.

## Proof

**Reduction to two exact integer invariants.** Set \(e_i=a_i-1\ge0\), let \(k=N-s=\sum_i e_i\), and discard zero increments. The remaining positive increments form an ordinary integer partition \(\pi\) of \(k\), with at most \(s\) parts. Conversely, every such partition gives one abundance multiset after padding by zero increments. Define
\[
S(\pi)=\sum_{e\in\pi}e(e+2),\qquad
T(\pi)=\prod_{e\in\pi}(e+1)^{e+1}.
\]
Direct substitution, including the zero increments, gives
\[
\sum_i a_i^2=s+S(\pi),\qquad
H(a)=\log N-\frac{\log T(\pi)}N,
\]
so both evenness indices decrease strictly in their respective invariants: order one in \(T\), order two in \(S\). Thus two distinct partitions have opposite strict rankings exactly when
\[
\bigl(S(\pi)-S(\rho)\bigr)\bigl(T(\pi)-T(\rho)\bigr)<0.
\]
A one-index tie disagreement occurs when exactly one of the two factors vanishes.

**Finite exhaustive classification, uniform in species richness.** Each positive integer partition of \(k\) is either empty for \(k=0\), or has a first positive part \(e\) and a nondecreasing remaining partition of \(k-e\), with all later parts at least \(e\). This gives an exhaustive, nonduplicating recursive enumeration. Below are all exact \((S,T)\) pairs, in nondecreasing \(S\) order, for \(0\le k\le7\). Equal \(S\) values represent different abundance multisets and are retained separately. The total numbers of entries, \(1,1,2,3,5,7,11,15\), independently agree with the ordinary partition counts at these arguments.

| Excess \(k\) | Complete ordered list of \((S,T)\) |
| --- | --- |
| 0 | \((0,1)\) |
| 1 | \((3,4)\) |
| 2 | \((6,16),(8,27)\) |
| 3 | \((9,64),(11,108),(15,256)\) |
| 4 | \((12,256),(14,432),(16,729),(18,1024),(24,3125)\) |
| 5 | \((15,1024),(17,1728),(19,2916),(21,4096),(23,6912),(27,12500),(35,46656)\) |
| 6 | \((18,4096),(20,6912),(22,11664),(24,16384),(24,19683),(26,27648),(30,50000),(30,65536),(32,84375),(38,186624),(48,823543)\) |
| 7 | \((21,16384),(23,27648),(25,46656),(27,65536),(27,78732),(29,110592),(31,186624),(33,200000),(33,262144),(35,337500),(39,800000),(41,746496),(43,1259712),(51,3294172),(63,16777216)\) |

For \(k\le5\), both invariants are injective on the partition list, and \(T\) strictly increases with \(S\). Hence the weak rankings are identical, irrespective of which partition lengths are allowed by \(s\). For \(k=6\), \(T\) remains strictly increasing across distinct \(S\) values. Its only \(S\)-ties are the partition pairs
\[
(1,1,1,3)\ \text{versus}\ (2,2,2),\qquad
(1,1,4)\ \text{versus}\ (3,3).
\]
Their \(T\) values are, respectively, \(16384\ne19683\) and \(50000\ne65536\). The first pair requires at least four species, while the second requires at least three. Thus the tie-disagreement classification and absence of strict reversals are exact.

For \(k=7\), the ordered list shows **precisely one decrease of \(T\) as \(S\) strictly increases**, from \((39,800000)\) to \((41,746496)\), and these two entries form the only pair of partitions exhibiting opposite strict orders (all other intervening comparisons are monotone). The corresponding positive increment partitions are \((3,4)\) and \((1,1,5)\). Both are allowed whenever \(s\ge3\); translating back to abundance counts produces exactly the stated pair \(A,B\). Their direction follows from the displayed exact invariants. This proves the sharp thresholds and uniqueness for every \(s\ge3\), with **no bound on \(s\)**.

For \(s=1\) the only positive-abundance multiset at each \(N\) is \((N)\). For \(s=2\), at fixed \(N\) both order-one and order-two Hill evenness strictly decrease as \(\lvert a_1-a_2\rvert\) increases: this follows by differentiating \(-p\log p-(1-p)\log(1-p)\) and \(1/(p^2+(1-p)^2)\) on \(p\in(0,1/2]\). Hence neither can reverse the other. QED.

## Verification

The separately embedded, dependency-free `verify.py` enumerates each partition of \(0,1,\ldots,7\), computes \(S\) and \(T\) with arbitrary-precision integers, and checks *every unordered pair* for strict reversals and single-index tie disagreements. It verifies the two \(k=6\) tie classes, uniqueness of the \(k=7\) strict reversal, the partition counts, and both witness invariants for richness \(3\le s\le60\). The code's finite checks reproduce an **analytical proof by exhaustive partition classification** because the combinatorial reduction gives exactly all possible inputs for every species richness \(s\). No finite test is used to infer an unbounded census conclusion without this reduction. Run `python3 verify.py` from the extracted package.

## Relationship to prior work

Hill's 1973 diversity formulation, Roswell and colleagues' 2021 conceptual guide, and Chisholm's 2026 perspective establish Hill indices and the relevance of comparing evenness measures. Chisholm explains that crossing Lorenz curves permit different Lorenz-consistent indices to rank communities differently, without a sharp **integer-census** cutoff. Nagendra (2002) reports empirical opposite responses of Shannon and Simpson indices for landscape assemblages, so existence of rank reversals itself is not new. Gates (2026) proves the more general qualitative fact that second-order collision information need not determine Shannon entropy; the present \(k=6\) tie examples are finite-count refinements, not a newly discovered non-identifiability phenomenon. The claimed contribution is **only** the complete sharp finite-positive-integer threshold and uniqueness classification under equal richness and equal total count, including the earlier tie-versus-reversal separation. Those earlier qualitative results do not supply the specific integer bounds or classify all extremizers. Relevant public mathematical database searches did not yield a statement with the same integer cutoff or a stronger implication; the residual risk of unindexed equivalent mathematics remains.

## Limitations

The result is combinatorial and applies to deterministic, fully observed abundance-count multisets, not estimated ecological population parameters, sampling uncertainty, different richness or census totals, or count vectors with absent species. It does not assert that rank reversals are common in nature or that either index is scientifically preferable. Normalizations other than Hill diversity divided by richness are not covered unless they are strictly monotone for the fixed richness. The characterization of \(k=7\) concerns the **first** reversal layer, not all larger census sizes. Nagendra's 2002 article was accessible through its abstract but not full text; an equivalent unindexed cutoff in other literature cannot be ruled out merely by searches. Independent scientific validation has not been performed.

## References

- Chisholm, R. A. (2026). *The Usefulness of Evenness*. Ecology Letters, 29, e70446. First published 16 August 2026. DOI: `10.1111/ele.70446`.
- Roswell, M., Dushoff, J., and Winfree, R. (2021). *A conceptual guide to measuring species diversity*. Oikos. DOI: `10.1111/oik.07202`.
- Alroy, J. (2025). *Does Evenness Even Exist?* Ecology Letters. DOI: `10.1111/ele.70181`.
- Gates, A. J. (2026). *Finite-Resolution Information from Collision Statistics*. Entropy, 28, 882. DOI: `10.3390/e28080882`.
- Nagendra, H. (2002). *Opposite trends in response for the Shannon and Simpson indices of landscape diversity*. Applied Geography, 22, 175–186. DOI: `10.1016/S0143-6228(02)00002-4`.
- Hill, M. O. (1973). *Diversity and Evenness: A Unifying Notation and Its Consequences*. Ecology, 54, 427–432. DOI: `10.2307/1934352`.
