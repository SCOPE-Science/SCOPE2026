# A sharp periodic-mesosome dichotomy for near-permutation words

## Finding

A **mesosome** is a word \(xx'\) in which \(x'\) is a cyclic conjugate of \(x\) and \(x'\ne x\). Let \(q\ge2\), and let \(w\) have length \(n=q+1\) over \(q\) distinct letters, with exactly one letter \(a\) appearing twice and each of the other \(q-1\) letters appearing once. Write \(w^\omega\) for the right-infinite periodic word of period \(w\), and let \(g(w)\) be the length of a shortest mesosome factor of \(w^\omega\), setting \(g(w)=\infty\) when there is none.

**Theorem (complete one-repeat classification).** If the two occurrences of \(a\) are adjacent in the *cyclic* word \(w\), then \(g(w)=2q\). If the two occurrences are not cyclically adjacent, then \(g(w)=\infty\). In particular, for \(q\ge3\) there are nonconstant periodic mesosome-avoiding infinite words whose period contains a repeated symbol.

With the alphabet labels fixed, the numbers of distinct cyclic rotation classes are exactly
\[
N_{\mathrm{all}}(q)=\frac{q!}{2},\qquad
N_{\mathrm{forcing}}(q)=(q-1)!,\qquad
N_{\mathrm{avoiding}}(q)=\frac{(q-2)(q-1)!}{2}.
\]
The middle quantity counts periods with \(g(w)=2q\); the last counts periods with \(g(w)=\infty\). These equalities include the boundary \(q=2\), for which no such mesosome-free rotation class exists.

## Assumptions and scope

All letters are distinguished and the alphabet has exactly \(q\) symbols. The period has content \(\{a,a,b_1,\ldots,b_{q-1}\}\), with the \(b_i\) pairwise distinct and different from \(a\). The condition 'cyclically adjacent' includes the first and last positions. Mesosomes must have nonempty conjugate halves that are **different**; ordinary squares \(xx\) alone are not mesosomes. Factors may cross arbitrarily many period boundaries. Two finite periods are identified only under rotation, not reversal or relabeling. The repeated-letter period is necessarily primitive, since a proper-power period would repeat each singleton letter.

## Proof

Set \(n=q+1\) and index the positions of one copy of \(w\) by the cyclic group \(\mathbb Z/n\mathbb Z\). Suppose a mesosome \(xx'\) occurs in \(w^\omega\), beginning at cyclic position \(s\), and put \(h=|x|=|x'|\). Since conjugates have equal Parikh vectors (symbol multiplicity vectors), \(x\) and \(x'\) have the same number of every letter. Write \(h=tn+r\) with \(0\le r<n\).

If \(r=0\), the two adjacent length-\(h\) blocks are identical by period \(n\), contradicting \(x'\ne x\). Thus \(1\le r<n\). Each length-\(h\) block consists of \(t\) entire periods in symbol counts, followed by a cyclic arc of \(r\) positions. Let \(A\) be the arc of \(r\) positions starting at \(s\), and \(B\) the arc of \(r\) positions starting at \(s+r\) modulo \(n\). Equal Parikh vectors of the two blocks imply equal Parikh vectors of these arcs.

Each letter other than \(a\) occurs **once** per period. Consequently, a singleton's position belongs to \(A\) if and only if it belongs to \(B\). The symmetric difference \(A\triangle B\) can therefore contain only the two positions occupied by \(a\).

For consecutive cyclic arcs of length \(r\), a direct interval calculation yields
\[
|A\triangle B|=2\min(r,n-r).
\]
Indeed, when \(r\le n/2\) the arcs are disjoint; when \(r>n/2\) their complementary arcs, each of length \(n-r\), are disjoint. Because \(A\ne B\), the symmetric difference is nonempty. It fits inside the two \(a\)-positions only if \(\min(r,n-r)=1\). Hence \(r=1\) or \(r=n-1\). In either case the symmetric difference consists of two *cyclically adjacent* positions: for \(r=1\), these are the two singleton arcs; for \(r=n-1\), they are the two positions omitted by the arcs. They must be the two occurrences of \(a\). This proves that a nonadjacent repeated pair makes a mesosome factor impossible, at every half-length \(h\).

Now suppose the two occurrences of \(a\) are adjacent. Rotate the period so that
\[
w=a a c_1c_2\cdots c_{n-2},
\]
where all \(c_i\) are different from one another and from \(a\). The infinite periodic word contains the consecutive factor
\[
(c_1c_2\cdots c_{n-2}a)\,(a c_1c_2\cdots c_{n-2}).
\]
The two length-\(n-1\) halves are distinct one-position conjugates, so this is a mesosome of total length \(2(n-1)=2q\). The preceding necessary residue condition also proves minimality: any mesosome half-length \(h<n-1\) would have residue \(r=h\) strictly between \(1\) and \(n-1\), except for \(h=1\); but at \(h=1\) a conjugate cannot be different. Thus \(g(w)=2(n-1)\).

Finally, with fixed labels, there are \((q+1)!/2\) linear words of the specified content. Each has exactly \(q+1\) distinct rotations, because the singleton symbols prevent a proper period. Hence there are \(q!/2\) rotation classes. A cyclically adjacent pair \(aa\) can be fused into one block. This gives \(q\) mutually distinct cyclic objects (the block together with \(q-1\) singletons), with \((q-1)!\) circular arrangements. Subtracting gives \((q-2)(q-1)!/2\) avoiding classes. This proves all assertions. \(\square\)

## Verification

A standalone standard-library Python checker, `checker.py`, independently enumerates every cyclic period of content \(\{a,a,b_1,\ldots,b_{q-1}\}\) for \(2\le q\le7\). It directly tests all cyclic starts and all half-lengths \(2\le h\le2(q+1)\), checking actual distinct conjugacy, not merely equal symbol counts. It finds precisely the predicted first mesosome when the repeated positions are adjacent, and none in this tested finite window otherwise. The counts of all, forcing, and avoiding rotation classes are respectively \((1,1,0)\), \((3,2,1)\), \((12,6,6)\), \((60,24,36)\), \((360,120,240)\), and \((2520,720,1800)\) for \(q=2,3,4,5,6,7\). The proof, not this bounded computation, establishes infinite avoidance.

Reproduce with `python3 checker.py` (no external dependencies).

## Relationship to prior work

Cummings, Shallit, and Staadecker introduced mesosome avoidance and classified **binary** finite and infinite mesosome-avoiding words [1]. Their binary results include only the \(q=2\) boundary of the present alphabet-parametrized near-permutation problem; their stated scope is binary, rather than the circular \(q\)-ary one-repeat family considered here. Ng, Ochem, Rampersad, and Shallit [2] study *pseudosquares* where the second half results from a uniform permutation or transformation of the **alphabet**. That operation is different from a cyclic conjugation of positions in the first half; their results do not give the mesosome-girth criterion or these necklace counts. This theorem does not claim a classification of arbitrary periodic words with several duplicated letters.

## Limitations

The classification requires exactly one letter with multiplicity two and all remaining letters with multiplicity one. It does not classify arbitrary circular words, multiple repeated letters, generalized Abelian squares, or mesosomes over unrelated aperiodic words. Distinct repeated-letter positions are understood modulo the full period. The verification is exhaustive only for \(2\le q\le7\), and finite absence checks are not evidence for unlimited length without the proof. Literature comparisons cannot completely exclude an equivalent result in unindexed sources; no independent mathematical audit has been performed.

## References

[1] R. Cummings, J. Shallit, and P. Staadecker, *Mesosome Avoidance*, arXiv:2107.13813v1, publicly posted 2021-07-29. https://arxiv.org/abs/2107.13813

[2] T. Ng, P. Ochem, N. Rampersad, and J. Shallit, *New results on pseudosquare avoidance*, arXiv:1904.09157v1, publicly posted 2019-04-19. https://arxiv.org/abs/1904.09157
