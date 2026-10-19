# Sharp three-symbol, one-deletion, two-list codes from Kirkman triple systems

## Finding

For a finite alphabet \(\Sigma\) with \(q=|\Sigma|\), let \(D_1(x)\) be the **set** (not multiset) of distinct words obtained from \(x\in\Sigma^3\) by deleting one coordinate. Define \(A_q(3,1;2)\) to be the maximum cardinality of a set \(C\subseteq\Sigma^3\) for which every \(y\in\Sigma^2\) belongs to \(D_1(x)\) for at most two distinct \(x\in C\).

For every integer \(q\ge2\),
\[
A_q(3,1;2)\le q+\left\lfloor\frac{2q^2}{3}\right\rfloor.
\]
For **every** integer \(q\ge3\) such that \(q\equiv3\pmod6\), equality holds:
\[
\boxed{A_q(3,1;2)=q+\frac{2q^2}{3}.}
\]
There is a construction from any resolvable Steiner triple system on \(q\) letters that uses each of the \(q^2\) two-letter deletion outputs **exactly twice**. In this congruence class, every optimal code contains all \(q\) constant words and, for each letter, exactly one nonconstant word with two adjacent copies of that letter; no optimal code contains a nonconstant word with its repeated letters separated.

## Assumptions and scope

A code is a **set of distinct ordered words**, with one deletion allowed at any of the three positions. A repeated deletion output from the same transmitted word counts once. The list-size condition is at most two distinct candidate codewords per output. Alphabets are arbitrary sets of size \(q\); no field structure is required. The asserted capacity equality applies only when \(q\equiv3\pmod6\), although the upper bound applies to every \(q\ge2\). No capacity formula is asserted for other congruence classes.

## Proof

**Upper bound.** Partition the codewords into three types: \(p\) constant words, \(r\) nonconstant words using exactly two different letters, and \(d\) words using three distinct letters. There are exactly \(q\) diagonal outputs \(aa\), each with capacity two. Every constant word produces exactly one diagonal output, as does every two-letter word, while a three-letter word produces none. Thus
\[
p+r\le2q,\qquad p\le q.
\]
There are \(q(q-1)\) off-diagonal outputs \(ab\) with \(a\ne b\), each of capacity two. A two-letter nonconstant word produces at least one distinct off-diagonal output; a three-letter word produces exactly three. Consequently
\[
r+3d\le2q(q-1).
\]
Combining the two resource bounds gives
\[
\begin{aligned}
3|C|&=3p+3r+3d\\
&\le3p+2r+2q(q-1)\\
&\le p+4q+2q(q-1)\\
&\le2q^2+3q.
\end{aligned}
\]
Taking integer parts proves the bound.

**Local construction.** A Steiner triple system is a family of three-element blocks in which every unordered pair of different letters occurs in exactly one block. A parallel class is a set of disjoint blocks partitioning the alphabet. For each block \(\{a,b,c\}\), fix any ordering \((a,b,c)\). On a block *outside* one selected parallel class, insert the four ordered words
\[
acb,\quad bac,\quad bca,\quad cab.
\]
On a block *inside* the selected parallel class, instead insert the six words
\[
aac,\quad bba,\quad ccb,\quad abc,\quad bca,\quad cab.
\]
In either case each of the six different-letter ordered outputs \(ab,ba,ac,ca,bc,cb\) occurs as a distinct one-deletion output of exactly two of the inserted words. For a selected block, each of \(aa,bb,cc\) additionally occurs once. Finally insert every constant word \(aaa\) for \(a\in\Sigma\).

Since distinct blocks contain each unordered pair exactly once, no different-letter output is produced by words attached to different blocks. Since the selected parallel class partitions the alphabet, every diagonal output occurs exactly once from a repeated-letter nonconstant word, and once from its constant word. Thus every one of the \(q^2\) outputs is covered exactly twice. The construction contains no duplicate codewords: three-distinct-letter words are attached to a unique block; words with a repeated letter are attached to a unique member of the selected parallel class; constant words are separate.

There are \(q(q-1)/6\) blocks and \(q/3\) blocks in the parallel class. Hence the number of codewords is
\[
q+4\left(\frac{q(q-1)}6-\frac q3\right)+6\frac q3
=q+\frac{2q^2}{3}.
\]
The classical Ray-Chaudhuri--Wilson existence theorem supplies a resolvable Steiner triple system for every \(q\equiv3\pmod6\), \(q\ge3\), so the upper bound is attained for all such \(q\).

**Equality constraints.** In this congruence class the displayed cardinality is integral. For an optimal code every inequality in the upper-bound chain must be an equality. Therefore \(p=q\), \(r=q\), both the diagonal and off-diagonal capacity constraints are saturated, and each nonconstant two-letter word produces exactly one off-diagonal output. Such a word must have its equal symbols adjacent (the separated form \(aba\) has both \(ab\) and \(ba\) as off-diagonal outputs). Each diagonal output is already used once by its constant word, so exactly one additional repeated-letter word is doubled at each letter. This proves the stated necessary structural conditions. Together with exact capacity saturation of the off-diagonal pairs, these conditions are also sufficient for optimality.

## Verification

The accompanying `verify.py` checks the elementary local templates, all pair-incidence requirements, codeword uniqueness and exact output multiplicities for the order-three design and for an order-nine Kirkman system realized by the twelve lines of the affine plane over \(\mathbb F_3\). Running `python3 verify.py` prints `VERIFY_OK q=3:9 q=9:63; each ordered two-symbol descendant occurs exactly twice`. These finite checks test implementation and boundary cases. The general theorem follows from the local counting proof and the classical design-existence theorem, not by extrapolation from the tests.

## Relationship to prior work

Kiah, Wei and Zeng (2026) study constant-list insertion/deletion coding with explicit numerical list size, prove general rate bounds and a finite-length Levenshtein-type list converse (Theorem 23), and explicitly motivate small fixed list sizes. For \(n=3\), one deletion and list size two, optimizing their Theorem 23 over its permitted run thresholds yields the upper bound \(q^2+q\), whereas the present sharp congruence-class value is \(2q^2/3+q\). Their results do not provide this short-block construction. Kong, Tamo and Wei (2024/2025) treat unique-decoding insdel codes and large-alphabet bounds, not this two-list quantity. Classical Kirkman triple systems and directed triple designs supply background combinatorial structure but do not alone state the exact deletion-code cardinality or its equality conditions.

## Limitations

The exact value outside \(q\equiv3\pmod6\) is not established here. The necessary equality conditions do not enumerate all nonisomorphic optimal codes. The local construction uses the established existence theorem for Kirkman triple systems rather than a new proof of that theorem. Searches and source inspection cannot exclude all unpublished or unindexed earlier statements; in particular, equivalences under directed-design language merit additional expert review. No external independent scientific audit has been performed.

## References

1. H. M. Kiah, H. Wei and R. Zeng, *Constant-List Insertion--Deletion Codes: New Bounds and an Improvement of Levenshtein's Lower Bound*, arXiv:2609.21395v1, first posted 2026-09-18; especially §1.2, Theorem 23 and §9. https://arxiv.org/abs/2609.21395
2. D. K. Ray-Chaudhuri and R. M. Wilson, *Solution of Kirkman's Schoolgirl Problem*, Proc. Sympos. Pure Math. 19 (1971), 187--203. See also E. W. Weisstein, *Kirkman Triple System*, MathWorld. https://mathworld.wolfram.com/KirkmanTripleSystem.html
3. X. Kong, I. Tamo and H. Wei, *Combinatorial alphabet-dependent bounds for insdel codes*, arXiv:2408.10961v1 (2024); IEEE Trans. Inf. Theory (2025). https://arxiv.org/abs/2408.10961
4. D. L. Kreher, D. R. Stinson and S. Veitch, *Block-avoiding point sequencings of directed triple systems*, arXiv:1907.11186 (2019), for the terminology of ordered transitive triple decompositions. https://arxiv.org/abs/1907.11186
