# Sharp alphabet-support threshold for simultaneous shuffle and reverse-shuffle squares

## Finding

For every integer \(n\ge1\), consider words \(w\) of length \(2n\) which are simultaneously shuffle squares and reverse shuffle squares. Their greatest possible number of distinct letters is exactly

\[
\max_{w\in\mathrm{SS}_{2n}\cap\mathrm{RSS}_{2n}}|\operatorname{alph}(w)|=\left\lfloor\frac n2\right\rfloor+1.
\]

In particular, for every \(q\ge2\), a word in this intersection using all \(q\) letters exists at length \(2n\) if and only if \(n\ge2(q-1)\). The shortest joint word with full \(q\)-letter support has length \(4q-4\). If \(J_n(Q)\) counts joint words of length \(2n\) over a labeled \(Q\)-letter alphabet, then for fixed \(n\),

\[
J_n(Q)=\Theta_n\!\left(Q^{\lfloor n/2\rfloor+1}\right)\qquad(Q\to\infty).
\]

This is a statement about **simultaneous** satisfaction: the two subsequence partitions need not coincide.

## Assumptions and scope

A **shuffle square** is a word whose positions can be partitioned into two disjoint increasing subsequences spelling the same word of length \(n\). A **reverse shuffle square** is a word whose positions can be partitioned into two disjoint increasing subsequences spelling a word of length \(n\) and its reversal, respectively. The alphabet is finite, letters are uninterpreted symbols, repeated letters are permitted, and a word's support counts distinct symbols that actually occur. The results concern ordinary scattered subsequences, not contiguous squares or cyclic cuts. The support equality includes \(n=1\); the shortest-length statement is phrased for \(q\ge2\).

## Proof

**Matching from an ordinary shuffle.** Fix a shuffle-square witness, with equal subsequences indexed in their common reading order. Pair the positions of their first letters, their second letters, and so forth, obtaining a perfect matching \(M\) on positions \(\{1,\ldots,2n\}\). If these paired positions are \((a_i,b_i)\) with both \(a_i\) and \(b_i\) strictly increasing in \(i\), then both \(\min(a_i,b_i)\) and \(\max(a_i,b_i)\) strictly increase. Thus the matching has no nested pair of edges \((i,\ell),(j,k)\) with \(i<j<k<\ell\). Each matched edge joins equal letters.

**Matching from a reversed shuffle.** Fix a reverse-shuffle witness with positions \(a_1<\cdots<a_n\) in its first subsequence and \(b_1<\cdots<b_n\) in the other. Pair \(a_i\) with \(b_{n+1-i}\), producing a perfect matching \(N\) of equal letters. Every edge has one endpoint among positions \(1,\ldots,n\) and the other among \(n+1,\ldots,2n\). Indeed, if both paired endpoints lay in the first half, the \(i\) positions \(a_1,\ldots,a_i\) and the \(n+1-i\) positions \(b_1,\ldots,b_{n+1-i}\) would give \(n+1\) positions in that half. If both endpoints lay in the second half, counting suffixes instead gives \(n+1\) positions in the second half. Therefore write the edges as \((i,n+\pi(i))\), where \(\pi\) is a permutation of \(\{1,\ldots,n\}\). Within the left endpoints belonging to the same one of the two witness subsequences, \(\pi\) is strictly decreasing, since matched partners have reversed subsequence ranks. Hence the sequence \(\pi(1),\ldots,\pi(n)\) is the union of two decreasing subsequences and has no increasing subsequence of length three.

**Interaction bound.** Let \(h=|M\cap N|\). Any shared edges must cross the midpoint. If three shared edges had left endpoints \(i<j<k\), their right endpoints could not be increasing: three increasing images would contradict the preceding length-three prohibition on \(\pi\). But two shared edges with right endpoints in decreasing order would form nested edges of \(M\). Consequently \(h\le2\).

View \(M\cup N\) as a multigraph, retaining one edge of each matching even where the pairs coincide. Its components are alternating cycles: a shared edge forms a two-vertex component; every other component has at least four vertices. If it has \(c\) components, then

\[
2n\ge2h+4(c-h)=4c-2h,
\qquad
c\le\left\lfloor\frac{n+h}{2}\right\rfloor
\le\left\lfloor\frac n2\right\rfloor+1.
\]

Every edge connects identical letters, so every component is monochromatic. Different components may share a letter, but not conversely; hence \(|\operatorname{alph}(w)|\le c\), proving the upper bound.

**Sharp construction.** Choose an additional letter \(a\) and a palindrome \(P\) of length \(n-1\), containing exactly \(\lceil(n-1)/2\rceil\) distinct letters, none equal to \(a\). For \(n=1\), \(P\) is empty. Define \(w=aPaP\). The two consecutive halves both spell \(aP\), so \(w\) is a shuffle square. A reverse-shuffle witness takes the initial \(a\) together with the final \(P\) for one subsequence, spelling \(aP\); the remaining initial \(P\) followed by the second \(a\) spells \(Pa\), the reversal of \(aP\). The support of \(w\) is \(1+\lceil(n-1)/2\rceil=\lfloor n/2\rfloor+1\). A surjective relabeling can reduce this support to any prescribed number from one up to that maximum without destroying either witness. The shortest-length assertion follows by solving \(q\le\lfloor n/2\rfloor+1\) for integer \(n\).

**Alphabet-growth consequence.** Put \(r=\lfloor n/2\rfloor+1\). The upper bound shows that any joint word over a \(Q\)-letter alphabet uses at most \(r\) letters; for fixed \(n\), this gives \(J_n(Q)=O_n(Q^r)\). Assigning \(r\) distinct alphabet letters injectively to the letters in the sharp construction gives \((Q)_r\) different words (for \(Q\ge r\)); hence \(J_n(Q)=\Omega_n(Q^r)\). Together these prove the stated \(\Theta_n\) estimate.

## Verification

The standalone standard-library program `verify_joint_shuffle_support.py` separately generates all non-nesting perfect matchings and all permutations avoiding increasing triples for \(1\le n\le8\), then calculates the connected components of each union. This checks exactly \(2{,}248{,}355\) matching pairs, attaining the claimed sharp bound at every tested half-length. It also checks the construction directly via all subsequence bipartitions at \(1\le n\le7\), and exhaustively compares the joint property with support limits for binary and ternary words at \(1\le n\le4\). The finite tests validate the encoding and small cases; the proof above establishes the result for all \(n\).

Run: `python verify_joint_shuffle_support.py`.

## Relationship to prior work

He, Huang, Nam, and Thaper's *Shuffle Squares and Reverse Shuffle Squares* (2021), arXiv:2109.12455, develops the separate matching characterizations and alphabet-growth counts of the two families. Its non-nesting and increasing-subsequence-avoidance descriptions are acknowledged as prior foundations here. The new comparison is an **intersection** theorem: a non-nesting matching and a reversed-shuffle matching on the same positions can share at most two edges, enforcing a sharp upper bound on the number of *joint* monochromatic components. The separate enumerations by themselves do not give this common-support threshold.

Grytczuk, Pawlik, and Pleszczyński's *Variations on shuffle squares* (2023), arXiv:2308.13882, studies related permutation and variant-shuffle configurations; it does not state this simultaneous ordinary/reverse support boundary. Subsequent work on ordered nest-free graphs, arXiv:2503.22043 (2025), develops broader graph connections and notes reverse shuffles but does not provide this joint threshold. The present result claims neither the individual matching characterizations nor the separate-family Catalan leading coefficients.

## Limitations

The theorem establishes an exact maximum support, a shortest full-support length, and the **exponent** of large-alphabet growth, not exact coefficients for the number of joint words. It does not count distinct witness partitions, classify every extremal word, or address a cyclic shuffle variant. The literature comparisons do not rule out an equivalent result under another terminology; independent expert review remains outstanding. Finite computations are not used as a substitute for the all-length proof.

## References

1. X. He, E. Huang, I. Nam, R. Thaper, *Shuffle Squares and Reverse Shuffle Squares*, arXiv:2109.12455 (first public version 2021-09-25), https://arxiv.org/abs/2109.12455.
2. J. Grytczuk, B. Pawlik, M. Pleszczyński, *Variations on shuffle squares*, arXiv:2308.13882 (2023-08-26), https://arxiv.org/abs/2308.13882.
3. *Shuffle squares and ordered nest-free graphs*, arXiv:2503.22043 (2025), https://arxiv.org/abs/2503.22043.
