# Exact Lie complexity of higher-radix sparse-marker fixed points

## Finding

For every integer \(r\ge3\), consider the length-\(r\) binary substitution
\[
\sigma_r(0)=0^{r-1}1,\qquad \sigma_r(1)=0^r,
\]
and its one-sided fixed point \(p_r=\lim_{j\to\infty}\sigma_r^j(0)\). Let \(L_r(n)\) count cyclic-equivalence classes of words \(w\in\{0,1\}^n\) for which **every** cyclic rotation of \(w\) occurs as a contiguous factor of \(p_r\). Define the reduced part \(s_r(n)=n/r^{v_r(n)}\), where \(v_r(n)\) is the largest nonnegative integer \(k\) satisfying \(r^k\mid n\) (this definition works even when \(r\) is composite). Then, for every integer \(n\ge1\),
\[
\boxed{L_r(n)=\begin{cases}
2,&1\le s_r(n)\le2r-1,\\
0,&s_r(n)\ge2r.
\end{cases}}
\]
The first branch automatically has \(r\nmid s_r(n)\). In particular, for fixed \(r\ge3\), the exact number of supported lengths not exceeding \(X\ge1\) is
\[
T_r(X)=\sum_{\substack{1\le s\le2r-1\\r\nmid s}}\max\{0,\,1+\lfloor\log_r(X/s)\rfloor\},
\]
where a summand is understood as zero when \(s>X\); consequently \(T_r(X)=2(r-1)\log_r X+O_r(1)\). These are consequences of the single exact Lie-complexity classification, not separate novelty claims.

## Assumptions and scope

Indices in \(p_r\) are zero-based. A factor is a finite consecutive block, and cyclic equivalence identifies words differing by a rotation, not by reversal or letter exchange. Every rotation must occur somewhere in the same right-infinite fixed point, possibly at different positions. The substitution is prolongable on zero, so the limit exists; it begins in zero. All claims concern the binary alphabet \(\{0,1\}\), arbitrary integers \(r\ge3\) and all lengths \(n\ge1\). We separately acknowledge the classical binary length-two substitution case \(r=2\) as already recorded in prior research; novelty is not asserted for that special case.

## Proof

**(1) Marker and zero-run constraints.** Each substituted letter contributes \(r-1\) initial zeros; an image contains a one exactly when its input is zero, then at its final position. Thus all ones of \(p_r\) lie at indices congruent to \(r-1\pmod r\), and the word has no adjacent ones. A zero-run spans at most one entire \(\sigma_r(1)=0^r\) block between two output ones, because the input \(p_r\) itself has no factor \(11\). Therefore no factor \(0^{2r}\) occurs. The factor \(10\) occurs in \(p_r\), and its image begins with the run \(0^{2r-1}\); hence \(0^{2r-1}\) does occur. Both input factors \(10\) and \(01\) occur: one sees \(10\) across a block boundary after \(\sigma_r(0)\), and \(01\) immediately before such a terminal one.

**(2) Short complete circular factors.** Fix \(1\le n<2r\). The constant necklace \([0^n]\) is complete by the zero-run result. All rotations of \(0^{n-1}1\) also occur. Indeed a rotated one-marker word is \(0^a1 0^b\) with \(a+b=n-1\le2r-2\), so either \(a\le r-1\) or \(b\le r-1\). If \(b\le r-1\), use an occurrence of the input factor \(10\): its image \(\sigma_r(10)=0^{2r-1}1\), followed by the next image block's initial \(r-1\) zeros, contains \(0^a1 0^b\). If \(a\le r-1\), an occurrence of input \(01\) gives \(\sigma_r(01)=0^{r-1}1 0^r\) followed by the next block's initial \(r-1\) zeros, also containing the requested factor. No other complete necklace exists. To see this, take two ones in a representative; their forward distance \(d\) is divisible by \(r\), since the representative occurs in \(p_r\). A cyclic rotation interchanging their order also occurs, forcing \(n-d\) to be divisible by \(r\). Hence \(r\mid n\), and then \(n=r\), but no length-\(r\) factor contains two ones. Thus \(L_r(n)=2\) throughout this base range.

**(3) Lengths not divisible by the substitution length.** The same two-one argument implies that a complete necklace of length \(n\) with \(r\nmid n\) has at most one one. When \(n\ge2r\) and \(r\nmid n\), necessarily \(n\ge2r+1\). A constant zero word cannot occur and a one-marker necklace has a rotation containing \(0^{n-1}\), which includes forbidden \(0^{2r}\). Therefore \(L_r(n)=0\) for \(n\ge2r\) not divisible by \(r\).

**(4) Exact desubstitution at divisible lengths.** Write \(n=rm\) with \(m\ge2\). Any complete necklace at length \(rm\) contains a one, since \(0^{rm}\) is forbidden. In a factor containing a one, the residue class of the ones identifies precisely the substitution-block boundaries. Hence one can rotate such a necklace to \(\sigma_r(u)\) for a unique \(r\)-block-aligned length-\(m\) word \(u\), up to cyclic block rotation, and \(u\) contains a zero. If \(\sigma_r(u)\) occurs in the infinite fixed point, its occurrence must begin at a global block boundary because of the residue of a one. It follows that \(u\) occurs in the input fixed point.

Suppose \([\sigma_r(u)]\) is complete. Every block-rotation \(\sigma_r(\operatorname{rot}_j u)\) occurs; the preceding alignment argument implies every \(\operatorname{rot}_j u\) occurs, so \([u]\) is complete. Conversely, if \([u]\) is complete, every aligned \(\sigma_r(\operatorname{rot}_j u)\) occurs. For each of these occurrences, shifting the window forward by \(t\in\{0,\ldots,r-1\}\) symbols and extending into the next substitution block yields exactly the cyclic shift by \(t\) of \(\sigma_r(\operatorname{rot}_j u)\): both the omitted first \(t\) letters and the new final \(t\) letters are zeros. Thus all rotations occur. Finally, two images \(\sigma_r(u)\) and \(\sigma_r(v)\) that are cyclic rotations of each other and contain a one differ by a multiple of \(r\) positions, because their ones have the same block-end residue. Their preimages differ by a block rotation. This proves a bijection on complete cyclic classes and therefore
\[
L_r(rm)=L_r(m)\qquad(m\ge2).
\]

**(5) Finish.** Repeatedly remove factors of \(r\) from the length. The recursion stops at the unique \(s_r(n)\) not divisible by \(r\). At lengths below \(2r\), step (2) gives two classes, while at larger lengths step (3) gives none. This establishes the boxed formula for every \(r\ge3\) and \(n\ge1\). Exactly \(2r-2\) integers in \(\{1,\ldots,2r-1\}\) are not divisible by \(r\); each generates a disjoint geometric progression of supported lengths. Counting those progressions proves the final exact and asymptotic expressions.

## Verification

The standalone `verify_lie.py` independently constructs prefixes of the actual substitution fixed points and enumerates both factor sets and full-rotation classes from them. It compares the resulting counts with the formula for radices \(2\) through \(7\) (the radix-two cases are control tests only), over \(332\) radix/length pairs and two prefix sizes of \(16000\) and \(32000\). It reports `GENERALIZED_LIE_FINITE_PASS` when those checks agree. Such finite checks do not establish the all-length theorem; the five proof steps above establish it without a computation assumption.

## Relationship to prior work

Bell and Shallit introduced and developed Lie complexity and proved broad automaticity properties for automatic infinite words. Those general properties are consistent with, but do not give as stated, the explicit complete spectrum for this higher-radix substitution family. Cassaigne, Fici, Sciortino and Zamboni studied *cyclic complexity*, a distinct statistic counting a necklace when at least one of its rotations occurs; the present condition requires **every** rotation to occur. De Luca and Fici considered Lie complexity for Sturmian words, rather than the fixed points defined above; Li provided broader bounds and methods. A separately established radix-two specialization is acknowledged rather than presented as new. The contribution here is the explicit exact formula, its phase-desubstitution proof, and the classification across every integer radix at least three.

## Limitations

The result concerns this particular two-letter uniform substitution family and does not classify arbitrary constant-length morphic words. It does not assert a new statement for the radix-two specialization. The comparison with inspected prior work and available research records is not a proof of worldwide uniqueness; an equivalent treatment of higher-radix generalized period doubling under another name may exist. Finite prefix experiments are corroboration, not a substitute for the argument.

## References

1. J. P. Bell and J. Shallit, *Lie Complexity of Words*, arXiv:2102.03821v1 (first posted 2021-02-07), https://arxiv.org/abs/2102.03821.
2. J. Cassaigne, G. Fici, M. Sciortino, and L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843, https://arxiv.org/abs/1402.5843.
3. A. De Luca and G. Fici, *On Lie Complexity of Sturmian Words*, arXiv:2206.00995v1, https://arxiv.org/abs/2206.00995.
4. S. Li, *A Note on the Lie Complexity and Beyond*, arXiv:2207.05859v1, https://arxiv.org/abs/2207.05859.
