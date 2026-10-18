# Exact shortest-extension profile of the Černý automata

## Finding

For each integer \(n\ge3\), let \(C_n\) be the complete two-letter deterministic automaton on \(Q=\{0,1,\ldots,n-1\}\), with \(a:i\mapsto i+1\pmod n\) and \(b:0\mapsto1\), while \(b\) fixes all other states. For a nonempty proper subset \(S\subset Q\), write \(s_i=\mathbf1_{i\in S}\) and
\[
 r(S)=\min\{0\le r<n:s_r=0,\ s_{(r+1)\bmod n}=1\}.
\]
Define \(\operatorname{minext}(S)\) as the minimum length of a word \(w\) with \(|\{q\in Q:q\cdot w\in S\}|>|S|\).

**Theorem.** For every such \(n\) and \(S\),
\[
 \operatorname{minext}(S)=r(S)+1,
\]
and the **unique** shortest extending word is \(ba^{r(S)}\). For \(1\le d<n\), exactly \(d\,2^{n-d-1}\) nonempty proper subsets have \(\operatorname{minext}(S)=d\); exactly \(n-1\) have extension length \(n\). More precisely, among subsets of size \(k\) with \(1\le k<n\), the count at length \(d<n\) is
\[
 \sum_{h=0}^{d-1}\binom{n-d-1}{k-1-h},
\]
where an out-of-range binomial coefficient is zero; at length \(n\), there is exactly one subset of each size \(k\), namely \(\{0,1,\ldots,k-1\}\).

The mean minimum extension length over all \(2^n-2\) nonempty proper subsets is
\[
 \frac{3(2^n-n-1)}{2^n-2},
\]
which tends to \(3\), even though the worst case is exactly \(n\).

## Assumptions and scope

A word acts from left to right: \(q\cdot xy=(q\cdot x)\cdot y\). The preimage \(Sw^{-1}\) consists of states mapped by \(w\) into \(S\). The alphabet is precisely \(\{a,b\}\), and empty and full subsets are excluded. The theorem concerns **a strict increase by at least one** in preimage cardinality, not total extension, avoidance, the reset threshold, or an arbitrary synchronizing automaton. The cyclic indicator indexing and the normalization \(b:0\mapsto1\) are part of the statement.

## Proof

Let \(P_x\) be the \(n\)-by-\(n\) zero-one transition matrix of a letter \(x\), indexed by source state in rows, and let \(e_i\) be the row coordinate vectors. Write \(\mathbf1\) for the all-ones row vector. Since \(a\) is a permutation and \(b\) maps two states to \(1\) and none to \(0\),
\[
 \mathbf1P_a-\mathbf1=0,\qquad
 \mathbf1P_b-\mathbf1=e_1-e_0.
\]
For any word \(w=x_1x_2\cdots x_L\), telescoping from the left gives
\[
 \mathbf1P_w-\mathbf1
 =\sum_{j=1}^L(\mathbf1P_{x_j}-\mathbf1)
                   P_{x_{j+1}\cdots x_L}.
 \tag{1}
\]
When dotted with the indicator column of \(S\), the left side is \(|Sw^{-1}|-|S|\).

**Short-suffix lemma.** For any word \(v\) of length at most \(n-1\), the states \(0\cdot v\) and \(1\cdot v\) either coincide or equal \(h\) and \((h+1)\bmod n\), respectively, where \(h\) is the number of letters \(a\) in \(v\). In particular \(0\le h\le|v|\). Indeed, until the pair has first undergone \(n-1\) cyclic shifts, its coordinates, if still distinct, are \(h,h+1\) with \(0\le h\le n-2\). In this range a letter \(b\) merges the pair only at \(h=0\) and acts trivially on both when \(h\ge1\). A merged pair remains merged. If \(h=n-1\) within a word of length at most \(n-1\), then \(v=a^{n-1}\), and the pair is \(n-1,0\). This establishes the assertion including the wraparound case.

Each nonzero contribution on the right of (1), for a \(b\) whose remaining suffix is \(v\), is therefore
\[
 s_{(h+1)\bmod n}-s_h,
 \qquad 0\le h\le |v|,
 \tag{2}
\]
for the \(h\) in the short-suffix lemma. If the two image states coincide, that contribution is zero.

By definition of \(r=r(S)\), \(s_{(h+1)\bmod n}-s_h\le0\) for every integer \(0\le h<r\); because \(S\) is nonempty and proper, at least one cyclic upward boundary exists and \(r\) is well-defined. A word of length \(L\le r\) has, after each letter \(b\), a suffix of length at most \(L-1<r\). Every summand in (1) is nonpositive on \(S\), so this word cannot extend \(S\). On the other hand the word \(ba^r\) has difference \(s_{(r+1)\bmod n}-s_r=1\) and extends \(S\). Hence \(\operatorname{minext}(S)=r+1\).

For uniqueness, consider a length-\(r+1\) word. Every contribution from a \(b\) in position \(j\ge2\) has suffix length less than \(r\) and is nonpositive. The contribution from a \(b\) in first position is positive only if its remaining suffix has \(r\) occurrences of \(a\), because the first positive cyclic difference occurs at \(h=r\). The suffix has exactly \(r\) positions, hence must be \(a^r\). Thus any extending word of minimum length is exactly \(ba^r\), and this word works.

It remains to count subsets. For \(d=r+1<n\), the binary prefix \(s_0\cdots s_{d-1}\) contains no adjacent \(01\), with \(s_{d-1}=0\). It consequently has the unique form \(1^h0^{d-h}\) for some \(0\le h<d\). The bit \(s_d\) is \(1\), and the remaining \(n-d-1\) bits are free. This gives \(d\,2^{n-d-1}\) sets and, on fixing size \(k\), the displayed binomial count. For \(d=n\), the linear word of all \(n\) bits must be \(1^k0^{n-k}\), with \(1\le k<n\); its only cyclic upward transition is at \(n-1\). That gives one set at each size. Finally, summing the histogram gives
\[
 \sum_{d=1}^{n-1}d^2 2^{n-d-1}+n(n-1)
 =3(2^n-n-1),
\]
by the finite geometric-series derivative identity, and division by \(2^n-2\) yields the mean.

## Verification

A standalone dependency-free checker, `checker.py`, computes shortest extension lengths by breadth-first search on the reverse-preimage subset automaton for every nonempty proper subset when \(3\le n\le11\). It checks both the unconditional and cardinality-refined histograms, all exceptional length-\(n\) subsets, and the first moment. For \(3\le n\le9\), it also enumerates every binary word of the alleged minimum length for every subset and verifies that the only extending word is \(ba^{r(S)}\). Reproduce with `python3 checker.py`. The file `check_output.txt` records the resulting literal output. These finite experiments are consistency checks; the preceding proof establishes all \(n\ge3\).

## Relationship to prior work

The subset-preimage extension problem and its role in synchronization are treated by Berlinkov, Ferens and Szykuła [2]; their paper gives general complexity classifications and a four-state Černý example of a short extending word, not the all-subset exact distribution or uniqueness result here. Miccinesi [1] studies certificates ensuring \(\operatorname{minext}(S)\le n-1\) on arbitrary automata and uses the Černý family to show that some subsets fail that bound, but does not classify which subsets fail or their exact minimum words. Here exactly \(n-1\) subsets fail that bound and they are explicitly identified, with full cardinality-refined lengths. Published results about low-rank image compression and complete avoidance in Černý automata concern different quantifiers and stronger/different target preimages, and do not imply this local first-extension profile. This is a best-knowledge comparison, not a guarantee of historical priority.

## Limitations

The formula relies on the indicated Černý labeling; relabeling requires transporting the boundary definition. It establishes no improvement to general reset-word bounds, no exact total-extension time, and no result for non-Černý automata. An equivalent all-subsets profile in unindexed older work remains possible. Computational checks cover only finite sizes and independent mathematical validation has not been performed.

## References

1. M. Miccinesi, *Certificates for short extending words in a finite automaton*, arXiv:2609.21603v1 (first posted 2026-09-18), https://arxiv.org/html/2609.21603v1 . See Introduction and Section 8.1.
2. M. V. Berlinkov, R. Ferens, and M. Szykuła, *Preimage problems for deterministic finite automata*, arXiv:1704.08233v4, https://arxiv.org/html/1704.08233v4 . See Introduction and Sections 2–4.
