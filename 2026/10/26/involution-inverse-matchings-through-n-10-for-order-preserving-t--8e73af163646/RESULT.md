# Involution inverse matchings through \(n=10\) for order-preserving transformation monoids

## Finding
For each integer \(1\le n\le10\), let \(O_n\) be the monoid of all order-preserving maps \(f:\{1,\ldots,n\}\to\{1,\ldots,n\}\). There exists a bijection \(I_n:O_n\to O_n\) such that
\[
I_n^2=\operatorname{id},\qquad fI_n(f)f=f,\qquad I_n(f)fI_n(f)=I_n(f)
\]
for every \(f\in O_n\). Thus each \(O_n\) through degree ten has an **involution matching** by mutual semigroup inverses, a stronger property than merely admitting an arbitrary permutation matching.

A finite, explicit certificate consists of the 62,704 two-cycles in `INVOLUTION_MATCHINGS.tsv`; all unlisted maps are fixed, and every such map is idempotent. The complete number of elements at each size is \(\binom{2n-1}{n}\), reaching \(92{,}378\) at \(n=10\). The certificate is self-contained and independently checkable by the supplied standard-library-only program.

## Assumptions and scope
Integers \(n\) are restricted to \(1\le n\le10\). Composition uses ordinary function composition, and \(g\) is an inverse of \(f\) in the semigroup sense precisely when \(fgf=f\) and \(gfg=g\). No claims are made for \(n\ge11\) or for the full transformation monoid.

For rank \(r\), a map \(f\in O_n\) is uniquely determined by its ordered contiguous kernel blocks
\[
A_i=\{c_{i-1}+1,\ldots,c_i\},\quad 0=c_0<c_1<\cdots<c_{r-1}<c_r=n,
\]
and its increasing list of distinct image values \(b_1<\cdots<b_r\): the map is constant with value \(b_i\) on \(A_i\). The number of rank-\(r\) maps is \(\binom{n-1}{r-1}\binom nr\). For every fixed \((n,r)\) the certificate orders kernel cut sets \((c_1,\ldots,c_{r-1})\) and image sets \((b_1,\ldots,b_r)\) lexicographically, obtaining lists \(P\) and \(Q\). The integer \(u=a|Q|+b\) encodes the map with zero-based kernel index \(a\) and image index \(b\).

## Proof
**Inverse-edge lemma.** Suppose \(f,g\in O_n\) have the same rank \(r\), with kernel intervals \(A_1,\ldots,A_r\), \(C_1,\ldots,C_r\) and increasing image lists \((b_i)\), \((d_i)\), respectively. Then \(f\) and \(g\) are mutual semigroup inverses if and only if
\[
 b_i\in C_i\quad\text{and}\quad d_i\in A_i\qquad(1\le i\le r).
\]
To prove sufficiency, \(f(A_i)=b_i\), \(g(b_i)=d_i\in A_i\), and hence \(fgf=f\); reversing the roles gives \(gfg=g\). Conversely, the identities imply both maps have the same rank, and the restrictions of \(g\) to \(\operatorname{im}f\) and of \(f\) to \(\operatorname{im}g\) are bijections. Monotonicity forces those restrictions to preserve the respective increasing indices, so \(g(b_i)=d_i\) and \(f(d_i)=b_i\), giving the displayed conditions. A map \(f\) is idempotent exactly when \(b_i\in A_i\) for each \(i\).

**Finite certificate theorem.** For each \(n\in\{3,\ldots,10\}\) and \(2\le r<n\), the text file `INVOLUTION_MATCHINGS.tsv` lists disjoint pairs \((u,v)\) in the rank-\(r\) block. The supplied verifier checks for *every* row that \(0\le u<v<|P||Q|\), that no encoded map appears twice, and that the inverse-edge lemma holds at each paired vertex. It then enumerates **every** unused rank-\(r\) vertex and checks the idempotency criterion; it does not assume unmatched vertices are idempotent. For ranks \(1\) and \(n\), all elements are idempotent (respectively constant maps and the identity), so fixing them is valid. The case \(n=1\) is immediate. Therefore declaring the endpoints of each listed pair to be exchanged, and all unused vertices to be fixed, defines a globally well-defined involution on each \(O_n\). Paired elements are mutual inverses by the lemma, and fixed elements are inverses of themselves. This proves the stated finite-range theorem.

Every certificate condition is a finite exact integer membership/equality assertion checked exhaustively over the explicitly enumerated domain. This is a finite certificate proof, **not** an extrapolation of experiments to arbitrary \(n\).

## Verification
Run `python verify_involutions.py INVOLUTION_MATCHINGS.tsv` in the directory containing both files using Python 3.8 or later without optimization flags. The checker uses only `itertools`, `math`, `pathlib`, `collections`, and `sys`. It reconstructs all \(\sum_{n=1}^{10}\binom{2n-1}{n}\) maps by rank, confirms the correctness of every pair and every fixed point, and independently tests the full equations \(fgf=f\) and \(gfg=g\) by composing the actual maps for \(n\le5\). The general inverse-edge lemma covers the remaining sizes. An ordinary run reports 62,704 valid two-cycles and no uncovered nonidempotent maps. The certificate itself—not the algorithm that originally located the pairs—is the evidence.

## Relationship to prior work
Higgins's 2018 preprint (published in 2019) developed involution matchings in finite regular semigroups and established them for orientation-preserving or reversing transformation monoids on cycles, while explicitly observing that the order-preserving chain monoid had not then been shown to admit even a permutation matching. His 2024 paper recorded the latter question and noted a computer check for arbitrary permutation matchings through \(n=4\), as well as the unresolved general difference between permutation and involution matchings. The October 1, 2026 preprint establishes permutation matchings of \(O_n\) for every \(n\), using balanced weightings. A permutation matching may have cycles longer than two, so that theorem alone does not supply an involution matching. The present finite certificate proves the stronger inverse-involution property only through \(n=10\). It does not claim a general resolution.

## Limitations
The result has a finite cutoff and does not establish an involution matching for \(n\ge11\), a canonical construction, optimality, or asymptotic behavior. The certificate's size grows rapidly; its correctness depends on replaying the exact included data under the stated indexing convention. Existing permutation matchings for arbitrary degree and involution matchings for the larger orientation-preserving/reversing monoid are prior work. Searching cannot establish priority exhaustively, so an unknown earlier finite-case involution certificate is a residual originality risk.

## References
1. P. M. Higgins, *Involution matchings, the semigroup of orientation-preserving and orientation-reversing mappings, and inverse covers of the full transformation semigroup*, arXiv:1811.04472 (first submitted 11 November 2018), *Semigroup Forum* 98 (2019), 669–689.
2. P. M. Higgins, *Finite regular semigroups with permutations that map elements to inverses*, *Semigroup Forum* 109 (2024), 141–147, DOI: 10.1007/s00233-024-10430-0 (online 22 April 2024).
3. P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912v1, submitted 1 October 2026.
