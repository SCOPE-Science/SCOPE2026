# Euler–Mahonian factorization for nonnesting canon permutations of higher multiplicity

## Finding

Let \(n\ge1\) and \(k\ge3\). A **\(k\)-canon permutation** on \([n]\) is a word containing each of \(1,\ldots,n\) exactly \(k\) times, such that the subsequence of first occurrences of the distinct letters, the subsequence of second occurrences, and so forth, all give the same permutation \(\sigma\in S_n\). Let \(\mathcal N_{n,k}\) be the canon permutations avoiding the patterns \(1221\) and \(2112\): equivalently, there are no four increasing positions with respective letters \(a,b,b,a\), where \(a\neq b\).

Define the strict descent number and major index by
\[
\operatorname{Des}(w)=\{i:1\le i<|w|,\ w_i>w_{i+1}\},\quad
\operatorname{des}(w)=|\operatorname{Des}(w)|,\quad
\operatorname{maj}(w)=\sum_{i\in\operatorname{Des}(w)}i.
\]
Let \(A_n(u,Q)=\sum_{\sigma\in S_n}u^{\operatorname{des}(\sigma)}Q^{\operatorname{maj}(\sigma)}\) be the usual Euler–Mahonian polynomial.

**Theorem.** For every \(n\ge1\), \(k\ge3\), the complete bivariate enumerator is
\[
\boxed{
\sum_{w\in\mathcal N_{n,k}}u^{\operatorname{des}(w)}q^{\operatorname{maj}(w)}
=A_n(u,q^k)\prod_{i=1}^{n-1}(1+uq^{ki}).
}
\]
More precisely, every such word is obtained *uniquely* by choosing an underlying permutation \(\sigma\) and a subset \(B\subseteq[n-1]\), starting from the consecutive blocks
\[
\sigma_1^k\sigma_2^k\cdots\sigma_n^k
\]
and swapping the two adjacent letters at each block boundary indexed by \(B\). The statistics of the resulting word satisfy
\[
\boxed{
\operatorname{des}(w)=\operatorname{des}(\sigma)+|B|,\qquad
\operatorname{maj}(w)=k\operatorname{maj}(\sigma)+k\sum_{i\in B}i.
}
\]

Setting \(u=1\) and using the classical major-index identity gives
\[
\boxed{
\sum_{w\in\mathcal N_{n,k}}q^{\operatorname{maj}(w)}
=[n]_{q^k}!\prod_{i=1}^{n-1}(1+q^{ki}),
}
\]
where \([n]_Q!=\prod_{r=1}^{n}(1+Q+\cdots+Q^{r-1})\). It follows that every major index is divisible by \(k\), **all** values
\[
0,k,2k,\ldots,kn(n-1)
\]
actually occur, and the major-index distribution is palindromic of degree \(kn(n-1)\). At \(q=1\), the descent polynomial is \(A_n(u,1)(1+u)^{n-1}\); at \(u=q=1\), the class cardinality is \(n!2^{n-1}\). These latter specializations are not claimed as new results.

## Assumptions and scope

All word positions are numbered from \(1\). An occurrence of a four-letter pattern is a not necessarily contiguous subsequence of four positions; the avoidance pair covers nested outer letters in both possible orders of distinct letter values. The requirement \(k\ge3\) is essential to the block-boundary separation argument. For \(k=2\), the general nonnesting class has a different Catalan-related structure, so this formula is not asserted. Empty products are \(1\), making \(n=1\) valid.

## Proof

Fix the underlying occurrence order \(\sigma=(a_1,\ldots,a_n)\). Write \(p_{a,j}\) for the position of the \(j\)-th occurrence of letter \(a\). By the canon condition, if \(a=a_i\) precedes \(b=a_j\) in \(\sigma\), then \(p_{a,r}<p_{b,r}\) for every \(1\le r\le k\).

**Step 1: exact pairwise nonnesting inequalities.** Consider \(a\) before \(b\) in \(\sigma\). The word has a forbidden \(b,a,a,b\) subsequence precisely when at least two copies of \(a\) lie between the first and last copies of \(b\). Since \(p_{a,k}<p_{b,k}\), this occurs precisely when \(p_{a,k-1}>p_{b,1}\). Thus avoiding this orientation is equivalent to
\[
p_{a,k-1}<p_{b,1}.
\]
Similarly, the forbidden \(a,b,b,a\) orientation occurs precisely when \(p_{b,2}<p_{a,k}\), because \(p_{a,1}<p_{b,1}\). Its avoidance is equivalent to
\[
p_{a,k}<p_{b,2}.
\]
The two inequalities for every pair are therefore necessary and sufficient to avoid both nested patterns.

**Step 2: reduce to adjacent blocks.** Since all occurrence orders agree with \(\sigma\), it is enough to impose both inequalities for consecutive letters \(a_i,a_{i+1}\). For any nonconsecutive \(a_i,a_j\), the first-occurrence ordering and the adjacent inequalities chain to the required inequality with the first occurrence of \(a_j\), and analogously for the second occurrences. More strongly, for \(k\ge3\), two adjacent constraints give
\[
p_{a_i,k}<p_{a_{i+1},2}
\le p_{a_{i+1},k-1}<p_{a_{i+2},1}.
\]
Thus every occurrence of \(a_i\) precedes every occurrence of \(a_{i+2}\); nonadjacent letter blocks never interleave. Consecutive letters \(a,b\) may interleave only between their last and first occurrences, respectively: the pair inequalities imply that the only possible orders are
\[
a^kb^k\quad\text{or}\quad a^{k-1}bab^{k-1}.
\]
Equivalently, one may independently swap the last copy of \(a\) with the first copy of \(b\) at any boundary between adjacent blocks of \(\sigma\). The swaps are at pairwise disjoint positions. The resulting word still has \(\sigma\) as the order of every occurrence-rank, because \(k\ge3\). Conversely, the inequalities show that every avoiding word arises this way. Both \(\sigma\) and the chosen boundary subset \(B\) are recoverable, proving the claimed bijection.

**Step 3: local descents.** At boundary \(i\), let \(a=a_i\), \(b=a_{i+1}\), and let \(t=ki\) be its original one-indexed position. With no swap, there is a strict descent at \(t\) if and only if \(a>b\). After the swap, the local string is
\[
\cdots a\,b\,a\,b\cdots.
\]
If \(a<b\), the swap introduces one descent, at position \(t\). If \(a>b\), it replaces the former single descent at \(t\) with two descents at positions \(t-1\) and \(t+1\). In the first case both the descent count and major-index sum increase by \(1\) and \(t\); in the second case they increase by \(1\) and
\[
(t-1)+(t+1)-t=t,
\]
respectively. The relevant neighborhoods for different boundaries are disjoint when \(k\ge3\). Therefore all increments add, giving
\[
\operatorname{des}(w)=\operatorname{des}(\sigma)+|B|,\quad
\operatorname{maj}(w)=k\operatorname{maj}(\sigma)+k\sum_{i\in B}i.
\]
Summation over \(\sigma\) and all subsets \(B\) proves the two-variable factorization.

**Step 4: support and symmetry.** MacMahon's classical identity states
\[
\sum_{\sigma\in S_n}Q^{\operatorname{maj}(\sigma)}=[n]_Q!.
\]
After substituting \(Q=q^k\), each factor in the major-index product is palindromic and has nonnegative coefficients. The factorial part has positive coefficients in every degree from \(0\) to \(n(n-1)/2\), and the subset-sum factor has positive coefficients in every degree from \(0\) to \(n(n-1)/2\), since the available weights are \(1,2,\ldots,n-1\). Their product thus supports all degrees from \(0\) to \(n(n-1)\) in the variable \(Q\), and no other powers of \(q\) occur. The total degree is \(kn(n-1)\), establishing the support and palindromicity conclusions.

## Verification

Run `python3 artifacts/verify.py` with Python 3 and no external packages. The program independently generates all \(k\)-canon permutations via rectangular lattice words; directly checks nested-pattern avoidance by occurrence positions; cross-checks a literal four-index pattern test in the smallest cases; constructs the unique boundary-swap model; computes the joint \((\operatorname{des},\operatorname{maj})\) histogram by direct traversal; and compares that histogram against the bivariate product without using the structural generator. Tested cases are all \(1\le n\le4\) with \(k\in\{3,4\}\), plus \((n,k)=(5,3),(2,5),(3,5)\).

The actual replay finishes with:

`ALL CHECKS PASSED; cases=11; canons_tested=1347568; literal_four_index_checks=263; admissible_words=2390; all cases exhaustive`

This is a finite test of the indicated parameter cases only. The theorem for arbitrary \(n,k\) rests on the preceding exact positional proof, not the enumeration.

## Relationship to prior work

Laudone (2026), *Pattern avoidance in canon permutations*, introduces the unrestricted-alphabet avoidance framework for \(k\)-canon words and gives the unrefined size \(n!2^{n-1}\) of the class avoiding \(1221,2112\) for \(k\ge3\) (the displayed result of Proposition 5.3). Both that scalar enumeration and the associated existence of a structural decomposition are prior work. We do not claim either is new.

The present statement refines the same class by the *joint* descent number and major index. Unlike an ordinary count or descent-only polynomial, it determines the precise positions of descents through their sum. The explicit boundary-weight formula provides an exact \(q\)-factorization, arithmetic support, and palindromicity; no prior statement located in the inspected primary material or corresponding searches gives this joint refinement. Some later portions of the relevant first paper could not be read from the available routes, so an unnoticed equivalent result there remains a specific originality risk.

Elizalde (2024) studies canon permutations and descent statistics over the full class, including the relation to standard Young tableaux. Deligeorgaki–Menon (2026) examines descent polynomials and bouncing for other canon families, including multiplicity two. Shankar (2026) studies patterns involving three *distinct* letters and descent refinements, distinct from the two-letter nesting patterns here. None of these identified results states the present joint \((\operatorname{des},\operatorname{maj})\) formula for the indicated avoidance class.

## Limitations

The formula requires \(k\ge3\), exact canon occurrence order, and simultaneous avoidance of both specified nesting patterns. It does not enumerate all canon permutations, arbitrary other pattern sets, or \(k=2\) nonnesting permutations. The scalar cardinality and descent-only specialization follow from earlier work and are excluded from the originality claim. The status is a self-review, not an independent audit; alternate terminology and unread later portions of the initial 2026 paper contribute residual indexing risk.

## References

1. R. Laudone, *Pattern avoidance in canon permutations*, arXiv:2608.21351v1, first public 2026-08-21, MSC2020 05A05. See the definition, results table, and Proposition 5.3 for the prior unrefined class count.
2. S. Elizalde, *Canon permutations and generalized descents of standard Young tableaux*, arXiv:2403.14914v1, first public 2024-03-22.
3. D. Deligeorgaki and K. Menon, *How to bounce your canon permutation*, arXiv:2603.22565v1.
4. U. Shankar, *Avoiding patterns with three distinct letters in Canon permutations*, arXiv:2608.30002v1.
5. P. A. MacMahon, classical major-index equidistribution theorem \(\sum_{\sigma\in S_n}q^{\operatorname{maj}(\sigma)}=[n]_q!\).
