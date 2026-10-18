# Geometric long-window \(b\)-symbol weight enumerators of cyclic binary Hamming codes

## Finding
Let \(m\ge 3\), \(n=2^m-1\), and let \(\alpha\) be a primitive element of \(\mathbb F_{2^m}\). Define the cyclic binary Hamming code
\[
C_m=\{(c_0,\ldots,c_{n-1})\in\mathbb F_2^n:\sum_{i=0}^{n-1}c_i\alpha^i=0\}.
\]
For an integer \(n/2<b\le n\), let \(w_b(c)\) count the cyclic starting positions at which the \(b\) consecutive coordinates of \(c\) are not all zero, and set \(W_{m,b}(z)=\sum_{c\in C_m}z^{w_b(c)}\). Put \(t=n-b-m\). The complete enumerator is
\[
W_{m,b}(z)=
\begin{cases}
1+(2^{n-m}-1)z^n,&t\le0,\\
1+n\displaystyle\sum_{j=1}^{t}a_jz^{b+m+j-1}+(2^{n-m}-1-n2^{t-1})z^n,&t\ge1,
\end{cases}
\]
where \(a_1=1\) and \(a_j=2^{j-2}\) for \(j\ge2\). Thus when \(t\ge1\), the positive weights below \(n\) are exactly \(b+m,\ldots,n-1\); in total precisely \(n2^{t-1}\) nonzero words have nonfull \(b\)-symbol weight. In particular, \(m=4\), \(n=15\), \(b=8\) gives
\[
W_{4,8}(z)=1+15z^{12}+15z^{13}+30z^{14}+1987z^{15}.
\]

## Assumptions and scope
The field is binary; the coordinate order is the **cyclic exponent order** \(1,\alpha,\alpha^2,\ldots\), not an arbitrary permutation of the parity-check columns. A circular length-\(b\) window may cross the boundary between coordinates \(n-1\) and \(0\). The assertion applies to each integer \(m\ge3\) and \(b\in\{\lfloor n/2\rfloor+1,\ldots,n\}\). The zero word has weight zero. No claim is made about shorter windows or Hamming codes under other coordinate orderings.

## Proof
**Consecutive-column rank.** For any cyclic interval of \(\ell\) columns with \(1\le\ell\le m\), these columns are linearly independent over \(\mathbb F_2\): a dependence becomes \(\alpha^i p(\alpha)=0\) for a binary polynomial \(p\) of degree less than \(m\), forcing \(p=0\) by the minimal-polynomial degree of \(\alpha\). Any consecutive interval of length \(\ell\ge m\) therefore has parity-check rank \(m\). As a result, the subcode supported inside one fixed interval of \(\ell\) positions contains \(2^{\ell-m}\) codewords when \(\ell\ge m\), and only the zero codeword for \(\ell\le m\). In particular, \(\dim C_m=n-m\).

**Unique short supporting arc.** Fix \(0\ne c\in C_m\) with \(w_b(c)<n\). Some cyclic run of at least \(b\) consecutive zero coordinates occurs. Since \(b>n/2\), at most one maximal cyclic zero run can have that length. Its complement is the unique shortest cyclic supporting arc of \(c\), with nonzero endpoints and length \(\ell\le n-b\). The rank statement forces \(\ell\ge m+1\). Conversely, every nonzero codeword supported on a cyclic arc of length \(m+1\le\ell\le n-b\), with both endpoints nonzero, has such a unique maximal zero run of length \(n-\ell\), hence exactly \(n-\ell-b+1\) zero windows and
\[
w_b(c)=n-(n-\ell-b+1)=b+\ell-1.
\]
No double-counting is possible: the long zero run, and hence the supporting arc and its initial coordinate, is unique.

**Endpoint inclusion-exclusion.** For one fixed arc of \(\ell=m+j\) positions, with \(j\ge1\), the number with first and last coordinates equal to one is obtained by removing words with a zero at either endpoint:
\[
a_j=2^j-2\cdot2^{j-1}+2^{\max(j-2,0)}.
\]
For \(j=1\), the interior subarc is of length \(m-1\) and only supports zero, giving \(a_1=1\); for \(j\ge2\), this simplifies to \(a_j=2^{j-2}\). There are exactly \(n\) cyclic starting coordinates. Distinct starting coordinates or different \(\ell\) cannot represent the same nonfull-weight codeword, by uniqueness of the maximal zero run. With \(t=n-b-m\), allowed lengths are \(\ell=m+j\) for \(1\le j\le t\), giving the displayed sum. Its total nonfull multiplicity is \(n\sum_{j=1}^{t}a_j=n2^{t-1}\).

**Remaining coefficient and boundaries.** The code contains exactly \(2^{n-m}\) words. Subtract the zero word and all nonfull-weight words to obtain the coefficient \(2^{n-m}-1-n2^{t-1}\) at \(z^n\). When \(t\le0\), no admissible nonzero word fits in an arc of length at most \(n-b\), so every nonzero word has full \(b\)-symbol weight. This includes \(b=n\) and the dimension-three case. The field argument depends only on primitivity and is independent of the choice of primitive element. \(\square\)

## Verification
Run `python3 verify.py` using Python 3 and its standard library. `verify.py` constructs the finite-field parity-check columns and independently computes cyclic window weights by direct inspection (not from the run-length formula). It exhaustively enumerates all codewords for \(m=3,4\) and all long windows. It also enumerates anchored short-support codewords for \(m=4,5\), verifies every span count, checks applicable weights directly, and checks uniqueness of all cyclic rotations when \(m=5\). The program ends with `VERIFY_OK cyclic_hamming_long_window` if every assertion succeeds. Its finite tests are corroboration; the proof for unbounded \(m\) is above.

## Relationship to prior work
Liu and Pan (arXiv:2103.16299, first public March 30, 2021) calculated **generalized minimum** \(b\)-symbol weight matrices of two small binary Hamming codes; their Section 4 does not enumerate all weights and multiplicities for the cyclic exponent ordering. Shi, Özbudak and Solé (HAL:hal-03189478, April 3, 2021) established bounds and stability of cyclic \(b\)-symbol weight enumerators once \(b\) reaches the code dimension; their irreducible-code formulas do not determine this Hamming spectrum in the nontrivial range \(b<n-m\). Zhu and Shi (arXiv:2203.11567), Vega (arXiv:2206.03459), and related work concern **irreducible cyclic** codes, whereas \(C_m\) has dimension \(n-m\) and is not the dimension-\(m\) irreducible simplex code. Zhu and collaborators (arXiv:2404.02471) bound the **cardinality** of the \(b\)-symbol weight spectrum of cyclic codes rather than the coefficients in this enumerator. The classical upper-bound and saturation statements alone do not imply the geometric multiplicities proved here.

## Limitations
The result addresses only \(b>n/2\) and the cyclic exponent ordering. It neither asserts optimality in a coding-performance criterion nor extends the formula to arbitrary column permutations, nonbinary Hamming codes, or short windows. Prior coverage cannot be categorically excluded from unindexed sources, and no independent external review is claimed. The exhaustive checks stop at the indicated small dimensions; they are not substituted for the general proof.

## References
1. H. Liu and X. Pan, *Generalized b-symbol weights of Linear Codes and b-symbol MDS Codes*, arXiv:2103.16299, https://arxiv.org/abs/2103.16299 (first posted 2021-03-30).
2. M. Shi, F. Özbudak and P. Solé, *Geometric Approach to b-Symbol Hamming Weights of Cyclic Codes*, HAL:hal-03189478, https://hal.science/hal-03189478 (submitted 2021-04-03).
3. H. Zhu and M. Shi, *The b-symbol weight distribution of irreducible cyclic codes and related consequences*, arXiv:2203.11567, https://arxiv.org/abs/2203.11567 (first posted 2022-03-22).
4. G. Vega, *The b-symbol weight distributions of all semiprimitive irreducible cyclic codes*, arXiv:2206.03459, https://arxiv.org/abs/2206.03459 (first posted 2022-06-07).
5. H. Zhu, S. Li, M. Shi, S.-T. Xia and P. Solé, *Some bounds on the cardinality of the b-symbol weight spectrum of codes*, arXiv:2404.02471, https://arxiv.org/abs/2404.02471 (first posted 2024-04-03).
