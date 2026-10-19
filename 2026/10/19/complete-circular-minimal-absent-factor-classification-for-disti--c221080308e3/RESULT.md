# Complete circular minimal-absent-factor classification for distinct binary gaps

## Finding

Let \(r\ge 2\) and let \(g_1,\ldots,g_r\) be pairwise distinct positive integers. In the periodic binary word with circular period
\[
W=0\,1^{g_1}0\,1^{g_2}\cdots0\,1^{g_r},
\]
**every minimal absent factor has at most three zeros**, and the following six explicit, pairwise-disjoint families comprise every minimal absent factor.

Put \(S=\{g_1,\ldots,g_r\}\), \(M=\max S\), and \(E=\{(g_i,g_{i+1}):i\in\mathbb Z/r\mathbb Z\}\). Define \(D(u,v)\) to mean that some \((x,y)\in E\) has \(x\ge u\) and \(y\ge v\). Define \(s(g_i)=g_{i+1}\) and \(p(g_i)=g_{i-1}\), with circular indices.

\[
\begin{aligned}
\mathcal G_0={}&\{1^{M+1}\},\\
\mathcal G_1={}&\{1^u0\,1^v:1\le u,v\le M,\ \neg D(u,v),\ D(u-1,v),\ D(u,v-1)\},\\
\mathcal G_{2a}={}&\{00\}\cup\{0\,1^j0:1\le j<M,\ j\notin S\},\\
\mathcal G_{2b}={}&\{0\,1^j0\,1^{s(j)+1}:j\in S,\ D(j,s(j)+1)\},\\
\mathcal G_{2c}={}&\{1^{p(j)+1}0\,1^j0:j\in S,\ D(p(j)+1,j)\},\\
\mathcal G_3={}&\{0\,1^x0\,1^y0:x,y\in S,\ y\le s(x),\ x\le p(y),\ y\ne s(x)\}.
\end{aligned}
\]

The complete circular minimal-absent-factor set is the disjoint union of these six families. In particular its cardinality is exactly
\[
M-r+2+|\mathcal G_1|+|\mathcal G_{2b}|+|\mathcal G_{2c}|+|\mathcal G_3|.
\]
This formula depends only on the gap lengths and their cyclic successor permutation, not on an expanded binary string. In contrast to the three-gap case, cyclic order matters with four gaps: the profiles \((1,2,3,4)\) and \((1,3,2,4)\) have respectively \(10\) and \(11\) minimal absent factors, despite the same multiset of gaps.

## Assumptions and scope

A factor means a contiguous factor of any power of the finite circular period \(W\), equivalently a factor of its bi-infinite periodic extension. Over the **fixed alphabet \(\{0,1\}\)**, a nonoccurring word is minimally absent exactly when its prefix and suffix of length one less both occur. The positive gaps must be pairwise distinct. No assumption is made about their magnitude or ordering, and \(r\) is unbounded. The two symbols both occur. For \(r=2\) this statement is also valid.

## Proof

**Phase-uniqueness lemma.** Each factor of the form \(0\,1^j0\) for \(j\in S\) has exactly one starting position modulo the circular period, since every gap length appears once. Consequently, if two occurring words differ by deleting opposite ends of a candidate word, and both retain the *same full gap* \(0\,1^j0\), their occurrences are anchored at the same cyclic phase. They agree on every shared position and jointly force the whole candidate to occur. Thus such a candidate cannot be minimally absent.

**No four zeros.** For a candidate with at least four zeros, its one-letter-shorter prefix and suffix both contain the complete gap between its second and third zeros. Both therefore share a unique full-gap anchor. By the lemma, an absent candidate with at least four zeros cannot have both immediate proper factors occurring.

**Three zeros.** A candidate with exactly three zeros and occurring immediate proper factors cannot contain \(00\), so it is \(1^u0\,1^x0\,1^y0\,1^v\) with \(u,v\ge0\) and \(x,y\ge1\). If \(u>0\), the immediate prefix and suffix share the complete first gap \(x\). If \(v>0\), they share the complete second gap \(y\). The phase-uniqueness lemma forces \(u=v=0\). Occurrence of the proper prefix \(0\,1^x0\,1^y\) requires \(x\in S\) and \(y\le s(x)\). Occurrence of the proper suffix \(1^x0\,1^y0\) requires \(y\in S\) and \(x\le p(y)\). Under these two conditions the entire word occurs if and only if \(y=s(x)\). This proves precisely \(\mathcal G_3\).

**Two zeros.** A minimally absent candidate containing two zeros is \(1^u0\,1^j0\,1^v\). If \(j=0\), the only possibility is \(00\). If \(j>M\), neither immediate proper factor can contain a feasible run, so it is impossible. For \(1\le j\le M\) with \(j\notin S\), the shortest absent pattern \(0\,1^j0\) is minimal, and every longer word containing that pattern is not minimal. For \(j\in S\), the center gap uniquely anchors all occurrences. If \(u,v\ge1\), the immediate prefix and suffix share that gap and hence force occurrence. If \(u=0\) and \(v\ge1\), the whole candidate is absent precisely when \(v>s(j)\), while its immediate prefix occurs precisely when \(v-1\le s(j)\); hence \(v=s(j)+1\). The remaining immediate suffix \(1^j0\,1^v\) occurs exactly when \(D(j,v)\). This is \(\mathcal G_{2b}\). Symmetrically, the candidates with \(u\ge1,v=0\) are precisely \(\mathcal G_{2c}\). This exhausts the two-zero cases.

**One zero.** A candidate \(1^u0\,1^v\) occurs exactly when \(D(u,v)\). When \(u=0\) or \(v=0\), its absence already forces one of its immediate proper factors to be absent. If both are positive, the two immediate factors occur exactly when \(D(u-1,v)\) and \(D(u,v-1)\). These conditions imply \(u,v\le M\), giving \(\mathcal G_1\).

**No zeros.** All lengths up to \(M\) of the symbol \(1\) occur, whereas \(1^{M+1}\) does not. This gives \(\mathcal G_0\).

The families are disjoint: they have different zero counts except the two-zero families, which respectively start/end in \(0\), start in \(0\) and end in \(1\), or start in \(1\) and end in \(0\). The baseline two-zero family has \(1+(M-r)\) members, because all \(r\) distinct gaps lie in \([1,M]\). Summing gives the stated cardinality. Direct substitution, or the independent checker below, yields the two four-gap counts. \(\square\)

## Verification

The standalone `check_unique_gaps.py` implements the six explicit formula families, and independently constructs the periodic factor language and checks every binary candidate with immediate occurring prefix and suffix. Exhaustive comparisons passed for all \(152\) circular ordered gap tuples arising as permutations of \(\{1,\ldots,r\}\) for \(2\le r\le5\). Six additional tuples with nonconsecutive gap lengths also passed. The code confirms the four-gap counts and, for permutations of \(\{1,2,3,4,5\}\), the attained cardinalities \(13,14,15,16\). The proof above, rather than finite experimentation, establishes the assertion for unrestricted gaps and run counts.

## Relationship to prior work

Fici, Restivo, and Rizzo introduced and studied the factor language of a circular word, its minimal forbidden factors and associated automaton, and gave special results for circular Fibonacci words (arXiv:1707.04450, first public 2017-07-14). Akagi and collaborators developed a run-length-encoded representation and enumeration framework for minimal absent words of finite **linear** strings (arXiv:2202.13591, first public 2022-02-28). These general algorithms can enumerate factors for a supplied instance but do not state the present parameter-uniform six-family formula or three-zero cutoff for arbitrary distinct circular gaps. The three-gap formula \(M+4\) is a special case and is not asserted as novel. The result here covers all \(r\ge2\) and demonstrates genuine cyclic-order dependence beginning with four gaps. A hidden special-family theorem in other literature is a residual originality risk.

## Limitations

The pairwise-distinct-gap assumption is essential for the phase-uniqueness argument; repeated gap lengths are not treated. The theorem enumerates factors of the bi-infinite periodic word, not minimal absent scattered subsequences. The example demonstrates order dependence but does not determine the maximum/minimum cardinality over all permutations for general \(r\).

## References

1. G. Fici, A. Restivo, L. Rizzo, *Minimal Forbidden Factors of Circular Words*, arXiv:1707.04450 (first public 2017-07-14); Theoretical Computer Science 792 (2019), 144–153.
2. T. Akagi, K. Okabe, T. Mieno, Y. Nakashima, S. Inenaga, *Minimal Absent Words on Run-Length Encoded Strings*, arXiv:2202.13591 (first public 2022-02-28); CPM 2022, LIPIcs 223, article 27.
