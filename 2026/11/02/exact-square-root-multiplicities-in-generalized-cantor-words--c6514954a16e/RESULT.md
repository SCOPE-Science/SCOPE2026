# Exact square-root multiplicities in generalized Cantor words

## Finding

For each integer \(b\ge 3\), let \(\sigma_b\) be the binary uniform morphism
\[
\sigma_b(1)=1\,0^{b-2}1,\qquad \sigma_b(0)=0^b,
\]
and let \(c_b=\lim_{j\to\infty}\sigma_b^j(1)\) be its one-sided fixed point. For every integer \(k\ge0\), write
\[
m=b^k,\quad g=(b-2)m,\quad p=(b-1)m,\quad S_k=\sigma_b^k(1).
\]
A *square root of length \(p\)* is a word \(u\in\{0,1\}^p\) such that the concatenation \(uu\) occurs contiguously in \(c_b\). The complete set of square roots that contain a \(1\) is
\[
\boxed{\mathcal R_{b,k}=\{0^aS_k0^{g-a}:0\le a\le g\}.}
\]
In particular, \(\lvert\mathcal R_{b,k}\rvert=(b-2)b^k+1\). Every such root is primitive, and all are rotations of \(S_k0^g\), whose full rotation class has \(p\) members. Hence exactly \(g+1\) of those \(p\) rotations have their squares appearing, a fraction \((g+1)/p\) tending to \((b-2)/(b-1)\) for each fixed \(b\). The zero root \(0^p\) is also present, but is excluded from \(\mathcal R_{b,k}\).

For the classical Cantor word \(b=3\), the nonzero counts at periods \(2,6,18,54,162\) are respectively \(2,4,10,28,82\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), with zero-based indices, factors being contiguous (not scattered), and equality of roots being literal rather than modulo rotation. The parameters range over all integers \(b\ge3\), \(k\ge0\); no claim is made here about root counts at other periods, cubes, or general powers. A square is counted as a distinct *root*, not as a position or an occurrence in the infinite word.

## Proof

**1. The level-\(k\) island decomposition.** For every \(n\ge0\), the \(n\)-th letter of \(c_b\) equals \(1\) exactly when every base-\(b\) digit of \(n\) belongs to \(\{0,b-1\}\). Index these one-positions by \(A_0<A_1<\cdots\), where \(A_j\) is obtained by replacing every binary digit \(1\) of \(j\) by base-\(b\) digit \(b-1\). For \(j\ge1\), a binary carry at the \(2\)-adic valuation \(r=\nu_2(j)\) gives
\[
A_j-A_{j-1}=(b-1)\left(b^r-\sum_{i=0}^{r-1}b^i\right)=(b-2)b^r+1.
\]
At block scale \(m=b^k\), the fixed point is tiled by the \(m\)-letter blocks \(\sigma_b^k(c_b(n))\), namely either \(S_k\) or \(0^m\). Call the nonzero \(S_k\)-blocks *islands*. Two consecutive islands are separated by a zero run of length
\[
g\,b^{\nu_2(j)}=(b-2)m\,b^{\nu_2(j)}.
\]
Since consecutive positive integers cannot both be odd, two consecutive inter-island gaps cannot both have the minimum length \(g\). Every island starts and ends in \(1\).

**2. Any length-\(2p\) window hits at most two islands.** If three successive islands were met, their first-to-third start distance would be at least \(2m+g+bg\), since one of the two intervening gaps has length at least \(bg\). The distance from the last letter of the first island to the first letter of the third would be at least
\[
m+g+bg+1=\bigl(b^2-b-1\bigr)m+1>2(b-1)m=2p.
\]
The strict inequality holds for all \(b\ge3\). A factor spanning only \(2p\) positions therefore cannot meet three islands.

**3. Localization of a square.** Suppose \(uu\) is a length-\(2p\) factor containing a \(1\), with \(|u|=p\). There is a position \(y\) carrying \(1\) in the first half and a corresponding \(1\) at \(y+p\) in the second. As an island has length \(m<p\), these two positions belong to different islands. They must be the two islands met by the factor, and their gap cannot be larger than \(g\): a gap of length at least \(bg\) makes the distance between any letters in different islands at least \(bg+1>p\). Thus the gap is exactly \(g\), and the two islands begin exactly \(p=m+g\) positions apart.

Translate coordinates so that the first island occupies \([0,m-1]\) and the second \([p,p+m-1]\), with the square starting at integer position \(x\). The gap immediately before the first island and the gap immediately after the second have length at least \(bg\), since the central gap is minimal. If \(x>0\), the first half of the square includes the \(1\) at position \(p\), but its required mate at \(2p\) is zero; contradiction. If \(x<-g\), the second half includes the \(1\) at position \(m-1\), but its required mate at \(m-1-p=-g-1\) is zero; contradiction. (The fact that the two paired islands are met also ensures \(-p<x\le m-1\), so these comparisons are inside the square.) Therefore \(-g\le x\le0\). The first half is exactly
\[
u=0^{-x}S_k0^{g+x}.
\]
Writing \(a=-x\) proves the claimed necessary form.

**4. All forms occur.** Choose a pair of consecutive islands separated by the minimal gap \(g\) that is not the first pair, so that both outer gaps exist and have length at least \(bg\). For each \(0\le a\le g\), the length-\(2p\) factor beginning \(a\) zeros before the first island is
\[
\bigl(0^aS_k0^{g-a}\bigr)^2.
\]
This proves sufficiency. Distinct \(a\)'s give distinct roots because their first \(1\) occurs at different positions. Thus the cardinality is \(g+1\).

**5. Primitivity and conjugacy.** Each \(S_k\) starts and ends with \(1\), and its longest internal zero run is strictly shorter than \(g\) (for \(k\ge1\), its longest possible inter-one gap of zeros is \((b-2)b^{k-1}\)). Hence \(S_k0^g\), viewed circularly, has a unique longest zero run, of length \(g\). A proper power would repeat its cyclic runs, which is impossible. The root is primitive, so its \(p\) rotations are distinct; the above \(g+1\) explicitly listed roots are rotations of it.

## Verification

Run `python3 check_square_roots.py` using Python 3 without external packages. Its direct finite-prefix enumerations compare literal square roots against the stated family for \(23\) parameter pairs covering bases \(3\) through \(7\) and levels up to \(4\), subject to a prefix-length cap. It independently compares morphic prefixes against their base-\(b\) digit characterization. The reproducible checker returned `VERIFY_OK` and `CASES 23`. These finite checks are supplementary: the argument above proves the result for all allowed parameters.

## Relationship to prior work

Bell and Shallit, *Lie Complexity of Words* (arXiv:2102.03821, Example 7.3), explicitly determine the **number of full cyclic-rotation classes** for the classical \(b=3\) Cantor word, including an exceptional class at lengths \(2\cdot3^k\). That is not a count of roots whose squares occur. Even one complete rotation class does not imply that every rotation yields a square, and it does not determine the subset \(\mathcal R_{3,k}\). The present theorem supplies that subset, its size, and a uniform extension to all bases \(b\ge3\).

Chen, Lü and Wu, *On the \(k\)-Abelian Complexity of the Cantor Sequence* (arXiv:1703.04063), treat the same classical word but count equivalence classes of factors under Parikh-based relations rather than square roots. Bulgakova, Frid and Scanvic, *Prefix Palindromic Length of the Sierpinski Word* (arXiv:2201.09556), consider the same substitution and explicitly mention its extension to \(1\mapsto1 0^{b-2}1\) in their discussion; their invariant concerns palindromic partitions, not squares. No statement in those inspected portions gives the present root classification. This is a best-knowledge comparison, not a claim that all literature has been exhaustively indexed.

## Limitations

The theorem only counts distinct nonzero roots of squares at the natural periods \((b-1)b^k\). It neither enumerates occurrences nor asserts that these are the only periods supporting nonzero squares. An independent scientific assessment has not been performed. Unindexed or inaccessible literature could contain an equivalent result; the most relevant comparison risk is prior repetition-specific work not captured by the targeted searches.

## References

- J. Chen, X. Lü, W. Wu, *On the \(k\)-Abelian Complexity of the Cantor Sequence*, arXiv:1703.04063, first posted 2017-03-12. https://arxiv.org/abs/1703.04063
- J. P. Bell, J. Shallit, *Lie Complexity of Words*, arXiv:2102.03821, first posted 2021-02-07, especially Example 7.3. https://arxiv.org/abs/2102.03821
- D. V. Bulgakova, A. E. Frid, J. Scanvic, *Prefix Palindromic Length of the Sierpinski Word*, arXiv:2201.09556, first posted 2022-01-24. https://arxiv.org/abs/2201.09556
