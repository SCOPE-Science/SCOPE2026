# Exact worst-case inverse degree for length-two reverse-complement duplication
## Finding
Let \(q\ge 2\) be even and let \(\Sigma_q\) have a fixed-point-free complement involution \(a\mapsto\bar a\). For \(n\ge 2\), a length-two reverse-complement duplication applied to a source factor \(ab\) inserts \(\bar b\bar a\) immediately after it, so locally \(ab\mapsto ab\bar b\bar a\).

For a received word \(y\in\Sigma_q^{{n+2}}\), write \(P_n(y)\) for the set of distinct words in \(\Sigma_q^n\) that produce \(y\) by exactly one length-two reverse-complement duplication. Then
\[
\max_{{y\in\Sigma_q^{{n+2}}}} |P_n(y)|=\left\lfloor\frac n2\right\rfloor.
\]
The bound is sharp for every even \(q\) and every \(n\ge 2\).

## Assumptions and scope
Positions are indexed from zero. A complement is an involution with no fixed points, so \(\overline{\bar a}=a\) and \(\bar a\ne a\) for every symbol. The finding concerns exactly one reverse-complement duplication of fixed length \(2\). It does not claim an analogous formula for other duplication lengths, multiple duplications, palindromic duplication, or complement maps with fixed points.

A position \(i\in\{{0,1,\ldots,n-2}}\) is a valid deduplication start in \(y\) exactly when
\[
y_{{i+2}}=\overline{{y_{{i+1}}}},\qquad y_{{i+3}}=\overline{{y_i}}.
\]
Deleting positions \(i+2\) and \(i+3\) then gives a parent in \(P_n(y)\).

## Proof
Suppose both \(i\) and \(i+1\) are valid starts. The two validity conditions give
\[
y_{{i+2}}=\overline{{y_{{i+1}}}},\quad y_{{i+3}}=\overline{{y_i}},\quad y_{{i+3}}=\overline{{y_{{i+2}}}},\quad y_{{i+4}}=\overline{{y_{{i+1}}}}.
\]
Using involutivity, these imply
\[
y_{{i+2}}=y_i,\qquad y_{{i+3}}=y_{{i+1}},\qquad y_{{i+4}}=y_i.
\]
The parent obtained at start \(i\) is \(y_0\cdots y_{{i+1}}y_{{i+4}}y_{{i+5}}\cdots\), whereas the parent obtained at start \(i+1\) is \(y_0\cdots y_{{i+1}}y_{{i+2}}y_{{i+5}}\cdots\). The displayed identities show that these parents are equal.

Choose one valid start for each distinct parent. Two chosen starts cannot be adjacent, because adjacent valid starts yield the same parent. Thus the chosen starts form an independent set in the path on the \(n-1\) possible starts. Its maximum independent-set size is
\[
\left\lceil\frac{{n-1}}2\right\rceil=\left\lfloor\frac n2\right\rfloor,
\]
which proves the upper bound.

For sharpness, fix a symbol \(a\), put \(b=\bar a\), and let \(y\) be the length-\(n+2\) prefix of the period-four word
\[
aabb\,aabb\,aabb\cdots.
\]
Every even start has local block \(aabb\) or \(bbaa\), hence is valid; every odd start has local block \(abba\) or \(baab\), hence is invalid because \(a\ne b\). The valid starts are therefore exactly \(0,2,4,\ldots\) up to \(n-2\), giving \(\lfloor n/2\rfloor\) starts. If \(i<j\) are two such starts, then at coordinate \(i+2\) the parent deduplicated at \(i\) has symbol \(y_{{i+4}}=y_i\), while the parent deduplicated later at \(j\) still has \(y_{{i+2}}=\bar y_i\). Since the complement has no fixed points, the two parents are distinct. Hence all \(\lfloor n/2\rfloor\) valid starts give distinct parents.

## Verification
The accompanying `verify.py` implements the channel forward from every source and, independently, reconstructs candidate parents from received-word local constraints. It checks equality of the two parent sets exhaustively for \(q=2\) and \(2\le n\le 8\), for \(q=4\) and \(2\le n\le 4\), and for \(q=6\) and \(2\le n\le 3\). It also checks the claimed maximum and the period-four construction in all of those cases, and checks the construction for \(q\in\{{2,4,6,8,10}}\) through \(n=100\). A successful replay prints `VERIFY_OK exhaustive_cases=12 construction_q<=10_n<=100`.

These computations are corroboration, not the proof of the universal statement; the proof above supplies the all-parameter argument.

## Relationship to prior work
Ben-Tolila and Schwartz introduced and analyzed the reverse-complement string-duplication system and, for odd duplication length, proved uniqueness of the duplication location once the parent is fixed (Lemma 16 of the 2022 journal version). Their argument explicitly uses odd parity and does not cover even duplication length. The present statement instead counts how many *distinct parents* a received word can have when the duplication length is exactly \(2\), and proves the sharp worst-case value.

Yohananov and Schwartz later determined coding capacity for arbitrary numbers of reverse-complement and palindromic duplications. Their open-access treatment notes that a single duplication has coding capacity one, but does not give a received-word inverse-degree formula. Sun and Ge study one arbitrary-length duplication and multiple length-one duplications through redundancy bounds and constructions rather than this inverse-degree invariant. A 2026 preprint by Zabokritskiy gives an even-length correspondence between reverse-complement and palindromic duplication and studies multiple-error redundancy and the maximum number of two-error descendants from one source. Its abstract does not state the one-error inverse-degree result here; the full text was not available through the bounded open retrieval attempted, so possible overlap inside that text remains a residual risk.

The related palindromic-duplication literature for length \(2\) studies irreducible roots and correcting codes. Uniqueness of an irreducible root is not an upper bound on the number of immediate one-step parents of a received word and therefore does not imply the present formula.

## Limitations
The theorem depends on a fixed-point-free complement involution and fixed duplication length \(2\). It does not classify every maximizing received word. The literature comparison cannot rule out an unindexed result or a result phrased only through the even-length palindromic correspondence. In particular, the inaccessible full text of the September 2026 multiple-duplication preprint is a concrete residual originality risk. No independence or external validation is claimed.

## References
1. E. Ben-Tolila and M. Schwartz, “On the Reverse-Complement String-Duplication System,” arXiv:2112.11811, first public version 2021-12-22; IEEE Transactions on Information Theory 68(11), 2022.
2. L. Yohananov and M. Schwartz, “On the Coding Capacity of Reverse-Complement and Palindromic Duplication-Correcting Codes,” arXiv:2312.00394; Designs, Codes and Cryptography 93, 2025, DOI 10.1007/s10623-025-01627-7.
3. Y. Sun and G. Ge, “On the Palindromic/Reverse-Complement Duplication Correcting Codes,” arXiv:2602.01151, 2026.
4. A. L. Zabokritskiy, “Coding for Multiple Reverse-Complement and Palindromic Duplications,” arXiv:2609.00779, 2026.
5. M. Zeraatpisheh, M. Esmaeili, and T. A. Gulliver, “Construction of Duplication Correcting Codes,” IEEE Access 8, 2020, DOI 10.1109/ACCESS.2020.2995812.
