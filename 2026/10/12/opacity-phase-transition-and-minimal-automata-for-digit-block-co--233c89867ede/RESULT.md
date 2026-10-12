# Opacity phase transition and minimal automata for digit-block counting sequences
## Finding
Let \(q\ge2\) be any integer (not necessarily prime), let \(\Sigma_q=\{0,1,\ldots,q-1\}\), and fix any nonempty pattern \(w=w_0\cdots w_{k-1}\in\Sigma_q^k\). The digit-block sequence \(a_{q,w}(n)\) counts, modulo \(q\), overlapping copies of \(w\) in the *standard, unpadded* base-\(q\) expansion of \(n\). The standard expansion of zero is the one-digit word \(0\). Denote by \(\varpi_q(a_{q,w})\) the normalized prefix-metric opacity defined by Allouche and Yao [2], namely their intrinsic-automaton opacity divided by \(M_q=1/2\).

**Theorem.** The minimal base-\(q\) deterministic finite automaton with output (DFAO) for this sequence has exactly
\[
\boxed{qk+\mathbf1_{\{w_0=0\}}}
\]
accessible, pairwise distinguishable states. Its normalized opacity is
\[
\boxed{
\varpi_q(a_{q,w})=
\begin{cases}
0,&q=2,\ k\ge2,\\
\tfrac12,&q=2,\ w=0,\\
1,&q=2,\ w=1,\\
1,&q\ge3\quad(\text{every nonempty }w).
\end{cases}}
\]
In particular, the complete family of binary block-counting sequences with block length at least two is transparent, while the same construction over every larger base is maximally opaque. The state-size assertion also holds for composite bases.

## Assumptions and scope
Digits are read most-significant first, including the leading-zero-insensitive extension of the DFAO (a zero transition at its initial state). A match may overlap another match. The final output of the DFAO is the match count modulo \(q\), not the last digit read. For the one-letter pattern \(w=0\), \(a_{q,0}(0)=1\), because the unpadded expansion of zero is \(0\); this exceptional value is retained in the construction. These conventions agree with the block-counting object studied by Abram, Hu, and Li [1].

A transition path is *inhomogeneous* if it enters some state twice along that path using two different input digits. We use [2, Theorems 1 and 2]: the opacity is determined by the minimal DFAO's graph; it is zero if all its input paths are homogeneous, and otherwise the shortest inhomogeneous path length \(\ell\ge2\) gives normalized opacity \(2^{2-\ell}\).

## Proof
**1. Explicit prefix automaton.** Let \(a=w_0\), and write \(w[:j]\) for the first \(j\) symbols of \(w\), with \(w[:0]\) empty. Introduce the states \((j,c)\) for \(0\le j<k\) and \(c\in\mathbb Z/q\mathbb Z\). The state means that \(c\) complete matches have been seen, modulo \(q\), while the longest suffix that is a proper prefix of \(w\) has length \(j\). On reading a digit \(d\), form the word \(z=w[:j]d\); increment the residue by one precisely when \(z=w\), and replace \(j\) by the largest \(h<k\) such that \(w[:h]\) is a suffix of \(z\). This is the standard overlapping-match prefix (failure-function) automaton. Its output at \((j,c)\) is \(c\).

If \(a\ne0\), use \((0,0)\) as initial state; reading digit \(0\) there is a self-loop, so arbitrarily many leading zeros are ignored. If \(a=0\), add one initial state \(I\) with a zero self-loop and with every nonzero input digit moving to \((0,0)\). Set its output to \(0\) when \(k\ge2\), and to \(1\) when \(k=1\) (the expansion of zero). These transitions and outputs produce exactly \(a_{q,w}(n)\) for all \(n\ge0\). Their total number of states is the asserted \(qk+\mathbf1_{\{a=0\}}\).

**2. Every state is reachable.** Choose any digit \(b\ne a\). The word \(wb^k\) has exactly one copy of \(w\), at its first position, and it ends in prefix-matching state \(j=0\). For if a second copy started a shift \(1\le t<k\) inside the first one and continued into \(b^k\), then \(w\) would have period \(t\) and its last \(t\) digits would all equal \(b\). One of those final \(t\) positions is a multiple of \(t\) and hence would equal \(w_0=a\), a contradiction. No occurrence can begin within a run of \(b\)'s, because \(w\) begins with \(a\ne b\). Thus each block \(wb^k\) contributes exactly one new match, also in arbitrary repetitions separated by the runs of \(b\)'s.

Consequently \((wb^k)^c w[:j]\) reaches \((j,c)\) for every \(0\le c<q\) and \(0\le j<k\), starting from \((0,0)\). When \(a=0\), prepend the nonzero digit \(b\), which leaves \(I\) and enters \((0,0)\) without creating a match. Hence all listed states are reachable; \(I\) itself is the initial state when present.

**3. Every state is distinguishable.** Distinct residues \(c\) have distinct current outputs. For equal residues but different prefix lengths \(i<j\), append \(w[j:]\). Starting with prefix-memory \(j\), exactly one occurrence is completed at the end; starting with prefix-memory \(i\), no occurrence is possible within only \(k-j<k-i\) input digits. Hence the resulting outputs differ modulo \(q\). If \(I\) exists and \(k\ge2\), distinguish it from \((j,0)\) for \(j>0\) by \(w[j:]\), and from \((0,0)\) by \(w\): the first leading zero is ignored from \(I\), so the complete pattern cannot yet have occurred, whereas the relevant active state completes a match. States of nonzero residue are already output-distinguished from \(I\). For \(w=0\), the output at \(I\) equals \(1\); the only active state of equal output is \((0,1)\), and an input \(0\) separates them (\(I\) remains at output \(1\), whereas the other output increments to \(2\bmod q\)). Thus the DFAO is minimal, with precisely the stated number of states. This prefix-state separation is consonant with the distinguishability argument of [1, Lemma 12], whose earlier observation is credited here.

**4. Binary patterns of length at least two are transparent.** In the minimal DFAO over the alphabet \(\{0,1\}\), consider a state \((j,c)\) with \(j>0\). Every transition entering this state has input label \(w_{j-1}\), since the target retains the last \(j\) digits as the prefix \(w[:j]\). Any transition entering \((0,c)\) must instead carry the digit distinct from \(w_0\); if the last digit were \(w_0\), a prefix of length at least one would remain, since \(k\ge2\). The extra initial state \(I\), when present, receives only zero-labeled transitions. Each state therefore has incoming transitions of a single label. Every path is homogeneous, and [2, Theorem 2] yields \(\varpi_2=0\).

**5. Larger bases are maximally opaque.** Suppose \(q\ge3\). If \(a\ne0\), choose two distinct digits \(x,y\ne a\); reading \(xy\) from \((0,0)\) uses two differently labeled self-loops, an inhomogeneous path of length two. If \(a=0\), choose distinct nonzero \(x,y\); the transitions \(I\xrightarrow{x}(0,0)\xrightarrow{y}(0,0)\) give two different incoming labels at the same state. This holds for every \(k\ge1\), including \(w=0\), and yields \(\ell=2\), so \(\varpi_q=1\).

**6. One-symbol binary boundary.** For \(w=1\), the two-state residue automaton has an inhomogeneous path of length two (inputs \(10\) revisit the same state with opposite labels), giving opacity \(1\), as also calculated for Thue--Morse in [2]. For \(w=0\), the minimal DFAO consists of \(I\) and the two active residue states. No length-two path has conflicting labels at one state, whereas inputs \(100\) give such a conflict at the active residue-zero state. Therefore \(\ell=3\) and \(\varpi_2=2^{2-3}=1/2\). The cases exhaust all \(q,w\). \(\square\)

## Verification
The standalone pure-Python program `verify.py` constructs the prefix DFAO, minimizes it using output-aware partition refinement, checks accessibility, evaluates short input paths for conflicts, and independently compares its outputs against literal base-\(q\) expansions (including \(n=0\)). Execute `python3 verify.py` from the same directory.

A completed run returned `VERIFY_OK patterns=1368 direct_cases=846900 binary_transparent=508 nonbinary_opaque=all intrinsic_size=q*length+leading_zero singleton_zero_opacity=1/2 singleton_one_opacity=1`. Every pattern was tested for \(q=2\), \(1\le k\le8\); \(q=3\), \(1\le k\le5\); \(q=4\), \(1\le k\le4\); and \(q=5\), \(1\le k\le3\). Each was checked at hundreds of indices against the direct definition. The unbounded result is proved in the preceding symbolic steps, not inferred from the finite computations.

## Relationship to prior work
Abram, Hu, and Li [1] develop the digit-block count family, provide recurrences and an algorithm, prove non-pure morphicity (in prime bases, with specified exceptions), and give an earlier state-distinguishability observation in Lemma 12. They do not evaluate the opacity of this family. Allouche and Yao [2] define the normalized opacity, establish the general intrinsic-automaton and shortest-inhomogeneous-path criteria used here, and calculate selected classical examples, including the Thue--Morse and Rudin--Shapiro cases that this theorem subsumes. The present result contributes the uniform all-pattern, all-base classification and exact minimal-state size, including the binary-to-nonbinary phase change and composite bases. It does not claim the earlier general opacity criterion or known individual examples as new.

## Limitations
Opacity here is the specific prefix-distance notion of [2], **not** quadratic-distance opacity, state-observation security opacity, factor complexity, or morphic complexity. The theorem covers one fixed nonempty block per sequence, counted modulo the numeral base, and uses standard unpadded numeral expansions. It does not assert the corresponding classification for sums of distinct pattern-counting sequences, other moduli, or alternative metrics. Independent mathematical validation has not been performed. The finite checker is a consistency check only.

## References
[1] A. Abram, Y. Hu, and S. Li, *Block-counting sequences are not purely morphic*, arXiv:2304.14595v1 (first public 2023-04-28), https://arxiv.org/html/2304.14595v1. In particular, §§1–4 and Lemma 12.

[2] J.-P. Allouche and J.-Y. Yao, *Opacity complexity of automatic sequences: The general case*, arXiv:2404.13601v1 (first public 2024-04-21), https://arxiv.org/html/2404.13601v1. In particular, Theorems 1–2, Corollaries 1–2, and Examples 5 and 7.
