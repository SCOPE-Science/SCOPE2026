# Exact maximum size of binary weight-three non-overlapping codes

## Finding
For every integer \(n\ge 3\), let \(A_3(n)\) be the maximum cardinality of a family \(C\subseteq\{0,1\}^n\) in which every word has exactly three occurrences of \(1\), and no nonempty proper suffix of any word equals a prefix of the same length of any word in \(C\), including itself. Then
\[
A_3(n)=\left\lfloor\frac{(n-1)(n-2)}{6}\right\rfloor.
\]
For \(n\ge4\), put \(m=\lfloor(n+2)/3\rfloor\) and \(B=n-m+1\). An optimal code consists precisely of the words whose three \(1\)-positions, numbered from one, are
\[
(1,a,b),\qquad 2\le a\le m,\qquad a+1\le b\le B.
\]
For \(n=3\), the optimal code is empty. In fact, this construction includes exactly one representative from each primitive cyclic-rotation class of binary length-\(n\) words of weight three.

## Assumptions and scope
A word is a finite binary string of the stated length; weight means the number of \(1\) symbols. A proper prefix or suffix here has length between \(1\) and \(n-1\). The non-overlap requirement applies to ordered pairs of words whether or not they are distinct; thus every codeword must be unbordered. A cyclic-rotation class is the orbit of a word under all cyclic shifts. A word is *primitive* if it is not a proper integer power of a shorter word. Only exact zero-overlap synchronization is asserted, not correction of symbol errors or deletions.

## Proof
**1. An upper bound from cyclic rotations.** If a non-overlapping code contains \(u\), then \(u\) cannot be a proper power: a proper power has the same nonempty proper prefix and suffix of length equal to its shortest repeated block. Thus every codeword is primitive. If two different codewords \(u,v\) were cyclic rotations of one another, write \(v=u_{d+1}\cdots u_n u_1\cdots u_d\) for some \(1\le d<n\). The suffix \(u_{d+1}\cdots u_n\) of \(u\) is also the prefix of \(v\), contradicting non-overlap. Consequently a code selects at most one word from each primitive rotation class.

There are \(\binom n3\) binary words of weight three. A nonprimitive such word must be a triple repetition, since its repetition multiplicity divides its total number of \(1\) symbols. This is possible precisely when \(3\mid n\). In that case its repeated block has length \(n/3\) and exactly one \(1\), giving exactly \(n/3\) nonprimitive words. All remaining words have full rotation orbit size \(n\). Therefore the number of primitive weight-three rotation classes is
\[
N_3(n)=\frac{1}{n}\left(\binom n3-\mathbf 1_{3\mid n}\frac n3\right)
=\frac{(n-1)(n-2)}6-\frac{\mathbf1_{3\mid n}}3
=\left\lfloor\frac{(n-1)(n-2)}6\right\rfloor.
\]
The final equality follows by considering \(n\) modulo three. Hence \(A_3(n)\le N_3(n)\).

**2. A compatible family of the required size.** Assume \(n\ge4\). Let \(C_n\) consist of all words with \(1\) in exactly the positions \(1,a,b\), where \(2\le a\le m\) and \(a+1\le b\le B\). These inequalities are consistent for \(n\ge4\), and \(B\le n-1\). Every word in \(C_n\) therefore has weight three, starts with \(1\), and ends with \(0\).

Choose any \(u,v\in C_n\) and a proper suffix of \(u\) of length \(L\), with \(1\le L<n\). If it begins with \(0\), it differs immediately from the prefix of \(v\). If it begins with \(1\), its initial position in \(u\) is either the second \(1\)-position \(a\) or the third \(1\)-position \(b\), because a proper suffix cannot start at position one.

If it starts at \(b\), then \(L=n-b+1\ge n-B+1=m\). This suffix contains precisely one \(1\), whereas the length-\(L\) prefix of \(v\) contains at least two \(1\)s: its first two \(1\)-positions are at most \(m\).

If it starts at \(a\), then \(L=n-a+1\ge n-m+1=B\). This suffix contains precisely two \(1\)s, whereas the length-\(L\) prefix of \(v\) contains all three \(1\)s, because the third \(1\)-position of \(v\) is at most \(B\). Thus no suffix can coincide with a corresponding prefix, for any ordered pair including \(u=v\). The family is non-overlapping.

The number of words in this family is
\[
|C_n|=\sum_{a=2}^{m}(B-a)=\frac{(m-1)(2n-3m)}2.
\]
For \(n=3k,3k+1,3k+2\), this is respectively \(3k(k-1)/2\), \(k(3k-1)/2\), and \(k(3k+1)/2\), exactly \(N_3(n)\). For \(n=3\), the only weight-three word is \(111\), which is bordered, so the empty code is optimal. Combining the lower and upper bounds proves the formula.

**3. Rotation-class transversal.** As proved above, the constructed code has no two distinct cyclic rotations of the same primitive word and contains no nonprimitive word. Since its cardinality equals the total number of primitive weight-three rotation classes, it meets each such class exactly once. \(\square\)

## Verification
The self-contained `check.py` builds \(C_n\) directly from the displayed position inequalities and checks its size and every ordered prefix–suffix comparison for each \(3\le n\le30\). Independently, it enumerates every weight-three word at each such length, groups all cyclic rotations, removes nonprimitive classes, and verifies that the code's rotation classes equal this complete set. All checks pass. These finite checks are supplementary to, and not a substitute for, the preceding all-length proof. Run `python3 check.py` using the Python standard library.

## Relationship to prior work
Non-overlapping codes also appear as cross-bifix-free and strongly regular codes. Bilotta, Pergola and Pinzani (2011) gave binary constructions based on Dyck paths and investigated non-expandability. Chee, Kiah, Purkayastha and Wang (2012) studied nearly optimal general cross-bifix-free constructions. Blackburn (2013) proved unconstrained alphabet/length bounds and constructions. Subsequent work by Bernini, Bilotta, Pinzani and Vajnovszki (2014), Qin, Chen and Luo (2023), and Stanovnik, Moškon and Mraz (2024, 2025), analyzed non-expandability, unrestricted maxima, and balance/run-length constraints. Their inspected statements do not determine an exact all-length maximum **restricted to binary Hamming weight three**, or give the explicit primitive-necklace transversal above. The cyclic-orbit obstruction by itself is only an upper bound; the attaining construction supplies the missing implication.

## Limitations
The result covers the fixed weight-three binary constraint and exact prefix–suffix disjointness, not arbitrary weights, mixed weights, or noisy synchronization. It does not classify every optimal code, nor establish uniqueness. Published and indexed-literature comparisons support distinctness from the specifically inspected results, but cannot rule out all unindexed or differently formulated prior work. Independent mathematical audit has not been performed.

## References
- S. Bilotta, E. Pergola and R. Pinzani, *A new approach to cross-bifix-free sets*, arXiv:1112.3168v1 (14 December 2011), https://arxiv.org/abs/1112.3168.
- Y. M. Chee, H. M. Kiah, P. Purkayastha and C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236 (first posted 3 September 2012), https://arxiv.org/abs/1209.0236.
- S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026 (first posted 5 March 2013), https://arxiv.org/abs/1303.1026.
- A. Bernini, S. Bilotta, R. Pinzani and V. Vajnovszki, *A Gray Code for cross-bifix-free sets*, arXiv:1401.4650 (first posted 19 January 2014), https://arxiv.org/abs/1401.4650.
- C. Qin, B. Chen and G. Luo, *On non-expandable cross-bifix-free codes*, arXiv:2309.08915 (2023), https://arxiv.org/abs/2309.08915.
- L. Stanovnik, M. Moškon and M. Mraz, *In search of maximum non-overlapping codes*, *Designs, Codes and Cryptography* 92 (2024), 1299–1326, doi:10.1007/s10623-023-01344-z.
- L. Stanovnik, M. Moškon and M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, arXiv:2410.18458 (2024), https://arxiv.org/abs/2410.18458.
