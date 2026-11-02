# Extremal distinct-deletion collisions for permutation words through length eight

## Finding
For a permutation \(\pi\in S_n\), let \(\operatorname{std}(w)\) denote the unique permutation with the same strict comparison relations as the distinct-letter word \(w\). Define the **distinct one-deletion shadow**
\[
\mathcal D(\pi)=\bigl\{\operatorname{std}(\pi_1\cdots\pi_{i-1}\pi_{i+1}\cdots\pi_n):1\le i\le n\bigr\}.
\]
For \(n\ge3\), let \(M_n=\max_{\pi\ne\sigma}|\mathcal D(\pi)\cap\mathcal D(\sigma)|\), with unordered distinct pairs \(\{\pi,\sigma\}\) counted once. The exact profile is

| \(n\) | \(3\) | \(4\) | \(5\) | \(6\) | \(7\) | \(8\) |
|---|---:|---:|---:|---:|---:|---:|
| \(M_n\) | 2 | 4 | 4 | 4 | 4 | 4 |
| Number of pairs attaining \(M_n\) | 6 | 1 | 4 | 18 | 96 | 600 |

Moreover, for every \(4\le n\le8\), **all** pairs attaining \(M_n=4\) are exactly the following pairs. Choose four consecutive values \(\{a,a+1,a+2,a+3\}\), place them into four consecutive positions, and keep the remaining \(n-4\) values in an arbitrary fixed order outside that block. In one permutation, the block has relative pattern \(2413\); in the other, it has relative pattern \(3142\). In absolute values the two blocks are \((a+1,a+3,a,a+2)\) and \((a+2,a,a+3,a+1)\). The number of such unordered pairs is exactly
\[
(n-3)(n-3)! \quad (4\le n\le8).
\]
This local replacement always produces **at least four** common distinct children for every \(n\ge4\), without asserting that four is the global maximum beyond \(n=8\).

## Assumptions and scope
Permutations consist of each symbol of \(\{1,\ldots,n\}\) exactly once; a received word is formed by deleting exactly one symbol and restandardizing the survivors, as in the permutation-invariant deletion channel. Children are counted *as distinct permutations*, irrespective of how many deletion positions produce the same child. No claims about multisets, multiple deletions, or \(n>8\) are implied by the finite classification.

## Proof
**Construction and counting.** The four deletions of \(2413\) yield the distinct patterns \(312,213,132,231\); the deletions of \(3142\) yield the same four patterns. If the block occupies consecutive positions and uses consecutive values, any deletion within the block leaves all outside symbols in the same relative order, and each outside symbol lies below or above all four block values. Therefore the four matching local deletion patterns extend to four *distinct* common global children. A block is specified by its starting value \(a\) in \(\{1,\ldots,n-3\}\). Treating that block as one atom, the order of its atom and the remaining \(n-4\) individually labeled values gives \((n-3)!\) choices. The changed four-position interval and changed four-value interval are recoverable from each unordered pair, so these \((n-3)(n-3)!\) pairs are distinct.

**Exhaustive upper bound and rigidity.** For a child \(\tau\in S_{n-1}\), construct all parents by choosing a missing value \(v\in\{1,\ldots,n\}\), raising each entry of \(\tau\) at least \(v\) by one, and inserting \(v\) in any of the \(n\) positions. Deduplicate parents. This yields exactly all parents of \(\tau\): deleting the inserted value recovers \(\tau\), and every parent supplies its omitted value and position. For every unordered pair of distinct parents, increment its counter exactly once for each child in which the pair occurs. The resulting counter is exactly \(|\mathcal D(\pi)\cap\mathcal D(\sigma)|\). Pairs with zero common children never occur in a bucket and cannot maximize a positive counter.

The complete finite computation performs this procedure for every child in \(S_{n-1}\) for each \(3\le n\le8\). Its checked results give maximum and equality-pair counts as tabulated above. For \(4\le n\le8\), it independently generates every pair from the proposed consecutive-value four-block construction and verifies equality of the **entire set** of maximum-counter pairs, not merely equality of cardinalities. This is exhaustive because the parent construction covers every possible common child and every parent pair of that child. The attached `verify.py` additionally reconstructs the same incidence relation directly by deleting each position in every parent, independently of inverse insertion; the two computations agree for every tested length.

This proof is finite for the stated interval. It uses exhaustive enumeration of complete finite spaces, not an extrapolation from sample values or an assumed eventual pattern.

## Verification
Run `python3 verify.py` with Python 3. The supplied `check_output.txt` records full positive-intersection histograms and the passing equality checks. The \(n=8\) histogram for intersections of size \(1,2,3,4\) is respectively \((5521776,324432,320,600)\); no larger intersection occurs. The two algorithms compare their entire histograms and their entire sets of extremal pairs at every length. The verifier requires no third-party packages or data and constructs all witnesses itself. Its reference replay completed successfully; runtime and memory are environment-dependent.

## Relationship to prior work
Wu, Bui, Niu, Vu, and Wang (2026) define permutation-invariant deletion and establish a coarse bound on the number of parents of a received permutation; their coding theorems concern asymptotic redundancy and systematic constructions, rather than this finite classification of distinct-child intersection extremizers. Smith (2006) proves unique reconstruction of full distinct deletion decks for permutations of length at least five; full-deck injectivity does not determine the largest *partial* overlap or its extremizers. Gouveia and Lehtonen (2021) count intersections of **multiset** decks, with multiplicities retained, and enumerate their multiset-extremal pairs through length eight. Their length-eight maximum of five multiset cards concerns a different statistic. The present enumeration resolves the distinct-child optimum and the complete \(600\)-pair equality structure for length eight; it does not claim the earlier full-deck reconstructibility or multiset extrema as new.

## Limitations
The upper bound and complete maximizer classification are proved only for \(3\le n\le8\). The all-length local construction is only a lower bound outside that range. The question whether an intersection larger than four is possible for any longer permutation is not settled. The independent review of this certificate and complete external publication-priority confirmation are not available; the result is reproducibly checked but not independently certified.

## References
1. B. Wu, Q. D. Bui, K. Niu, V. K. Vu, S. Wang, *Order-Optimal Systematic Permutation Codes for Correcting t Deletions*, arXiv:2609.37578, first submitted 2026-09-29, https://arxiv.org/abs/2609.37578 .
2. R. Smith, *Permutation Reconstruction*, Electronic Journal of Combinatorics 13 (2006), #N11, DOI:10.37236/1149, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v13i1n11/pdf .
3. M. J. Gouveia and E. Lehtonen, *Permutation Reconstruction From a Few Large Patterns*, Electronic Journal of Combinatorics 28(3) (2021), #P3.41, DOI:10.37236/10403, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v28i3p41/pdf/ .
