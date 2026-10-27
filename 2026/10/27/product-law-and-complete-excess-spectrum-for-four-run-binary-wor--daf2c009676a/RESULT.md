# Product law and complete excess spectrum for four-run binary words

## Finding

For a finite word \(w\), let \(\mathcal C(w)\) be its set of **distinct closed contiguous factors**, including the empty factor. A word of length at most one is closed; a longer word is closed exactly when it has a nonempty proper border occurring only as its prefix and suffix. For any integers \(a,b,c,d\geq1\), put
\[
 w=0^a1^b0^c1^d,\quad n=a+b+c+d,\quad p=\min(a,c),\quad q=\min(b,d).
\]
Then the exact set \(\mathcal C(w)\) is the **disjoint union** of
\[
\begin{aligned}
&\{\varepsilon\}\cup\{0^i:1\leq i\leq\max(a,c)\}
       \cup\{1^j:1\leq j\leq\max(b,d)\},\\
&\{0^i1^b0^i:1\leq i\leq p\},\\
&\{1^j0^c1^j:1\leq j\leq q\},\\
&\{0^i1^b0^c1^j:1\leq i\leq p,\ 1\leq j\leq q\}.
\end{aligned}
\]
Consequently,
\[
\boxed{|\mathcal C(w)|=n+1+\min(a,c)\min(b,d).}
\]
For each integer \(n\geq4\), the **complete attainable closed-factor excess spectrum** among binary words of length \(n\) with exactly three symbol changes is
\[
\boxed{\bigl\{|\mathcal C(w)|-(n+1)\bigr\}
=\{pq:p,q\in\mathbb Z_{\geq1},\ 2(p+q)\leq n\}.}
\]
Its minimum is \(1\), and its maximum is
\[
\boxed{\left\lfloor\frac{\lfloor n/2\rfloor^2}{4}\right\rfloor.}
\]
The formula and spectrum are invariant under exchanging the two letters, so they cover every binary word with exactly three symbol changes, not only those beginning in \(0\).

## Assumptions and scope

A *run* is a maximal nonempty block of identical letters. Thus \(w=0^a1^b0^c1^d\) has exactly four runs and three changes. Factors are linear contiguous substrings, not circular factors or scattered subsequences; equal substrings at different positions are counted once. The empty word contributes one to \(|\mathcal C(w)|\). A nonempty proper border \(u\) is simultaneously a prefix and a suffix, with \(|u|<|w|\), and the two prescribed occurrences may overlap. Closedness requires that no third occurrence of \(u\) appear.

## Proof

**Classification by number of runs.** Every nonempty factor of \(w\) has one, two, three, or four runs.

A one-run factor is a power of one letter, and every such factor is closed. The distinct powers have lengths from \(1\) to \(\max(a,c)\) for \(0\), and \(1\) to \(\max(b,d)\) for \(1\). Every two-run factor starts and ends in different letters and therefore has no nonempty border; none is closed.

A three-run factor is either \(0^i1^b0^j\), with \(1\leq i\leq a\) and \(1\leq j\leq c\), or \(1^i0^c1^j\), with \(1\leq i\leq b\) and \(1\leq j\leq d\). The outer runs have the same letter. Hence every nonempty border must be a power of that letter and has length at most the shorter outer run. When the outer lengths differ, any candidate border has an internal occurrence inside the longer outer run and is not a closing border. When they agree, the whole outer run is a border occurring exactly at the two ends, since the middle run uses the other letter. Thus precisely \(0^i1^b0^i\) for \(1\leq i\leq p\) and \(1^j0^c1^j\) for \(1\leq j\leq q\) are closed.

Any four-run factor must cross all three changes, so it is of the form \(v=0^i1^b0^c1^j\), with \(1\leq i\leq a\) and \(1\leq j\leq d\). Every nonempty border of \(v\) starts in \(0\) and ends in \(1\) and must contain the transition \(01\). A proper suffix equal to a prefix cannot start inside the first \(0\)-run: it would have fewer initial zeroes before its first \(1\) than the full prefix of \(v\). Thus the suffix border must start inside the third run. It necessarily equals \(0^i1^j\), requiring \(i\leq c\); the matching prefix exists only if \(j\leq b\). Conversely, when both inequalities hold, \(0^i1^j\) occurs exactly twice in \(v\), at its two \(01\) transitions, so \(v\) is closed. Therefore the closed four-run factors are exactly those in the final displayed family, indexed independently by \(1\leq i\leq p\) and \(1\leq j\leq q\).

The families are pairwise disjoint because they have different run counts, except that the two three-run families have distinct starting letters. Parameters within each family give distinct words. The count is therefore
\[
1+\max(a,c)+\max(b,d)+p+q+pq
=1+a+b+c+d+pq=n+1+pq,
\]
proving the set classification and cardinality formula.

**Complete spectrum.** Given a four-run word, \(p+q\leq(a+c+b+d)/2=n/2\). Conversely, for any integers \(p,q\geq1\) with \(2(p+q)\leq n\), choose
\[
(a,b,c,d)=(p+n-2(p+q),\ q,\ p,\ q).
\]
All four run lengths are positive, their sum is \(n\), and their two minima are exactly \(p,q\); every displayed product is attained. For \(m=\lfloor n/2\rfloor\), the maximum of \(pq\) under \(p,q\geq1\) and \(p+q\leq m\) occurs at the most balanced split of \(m\), giving \(\lfloor m^2/4\rfloor\). The minimum \(1\) is attained by \(p=q=1\). Exchanging \(0\) and \(1\) covers the other four-run orientation.

## Verification

The standalone standard-library script `verify.py` does not assume the run-factor classification. It enumerates all distinct factors of each four-run word and tests closedness by checking every nonempty proper border and explicitly listing all occurrence positions. It compares the resulting exact factor set—not just its cardinality—to the displayed families for all \(6^4=1296\) parameter quadruples \(1\leq a,b,c,d\leq6\), reaching total word length \(24\). It separately enumerates every positive four-part composition of lengths \(4\) through \(18\), confirming the exact attainable excess set and its extremum at each length. The checks return:

`CHECK_OK families=1296 run_lengths=1..6 max_length=24 exact_sets=matched`

`CHECK_OK exact_excess_spectra=lengths_4_through_18 maxima=matched`

To replay, run `python3 verify.py` with Python 3 and no third-party dependencies. These finite tests are diagnostics; the preceding classification proof establishes the unbounded integer parameter ranges.

## Relationship to prior work

Badkobeh, Fici, and Lipták (arXiv:1305.6395, first submitted 28 May 2013) proved that every length-\(n\) word has at least \(n+1\) distinct closed factors and characterized binary words meeting this minimum as bitonic words, namely cyclic rotations of words with only one run of each symbol. Hence a binary word with three changes is the first run class beyond this lower-bound equality. Their paper also exhibits four-run constructions with quadratically many closed factors but does not give the complete factor set, the all-parameter excess formula, or the fixed-length product spectrum above. The present classification quantifies exactly the first deviation from closed-factor minimality, which can already have quadratic size.

Parshina and Puzynina (arXiv:2111.00863) study the unrestricted **maximum** of closed-factor counts and its asymptotic \(n^2/6\). Their analysis contains examples built from repeated runs but not the exact four-run classification. Mieno, Takahashi, Seto, and Horiyama (arXiv:2409.19576) provide general algorithms for computing closed-factor counts from an input string, not an all-parameter four-run formula. A separate published computation titled *Exact binary closed-rich maxima at lengths 25–27* determines unrestricted maxima at three lengths, not the constrained run-class spectrum. These are distinctions between mathematical statements, not merely between titles.

## Limitations

The finding concerns words with exactly three changes (four nonempty runs) and does not determine closed-factor counts for arbitrary binary words, arbitrary numbers of runs, or alphabets of larger size. The fixed-length product spectrum is not generally an interval: for example, the excess \(7\) is unattainable at length \(12\). Priority assessment is based on the specified full-text literature and targeted source searches; an unindexed or unpublished equivalent four-run formula remains a residual possibility. No claim of a complete literature census is made.

## References

1. G. Badkobeh, G. Fici, and Z. Lipták, *On the Number of Closed Factors in a Word*, arXiv:1305.6395 (first public preprint 2013-05-28); published in LATA 2015, DOI 10.1007/978-3-319-15579-1_29. https://arxiv.org/abs/1305.6395
2. O. Parshina and S. Puzynina, *Finite and infinite closed-rich words*, arXiv:2111.00863 (2021); *Theoretical Computer Science* 984 (2024), 114315. https://arxiv.org/html/2111.00863v3
3. T. Mieno, S. Takahashi, K. Seto, and T. Horiyama, *Online and Offline Algorithms for Counting Distinct Closed Factors via Sliding Suffix Trees*, arXiv:2409.19576 (2024). https://arxiv.org/abs/2409.19576
4. *Exact binary closed-rich maxima at lengths 25–27*, published mathematical research record (2026). https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-binary-closed-rich-maxima-at-lengths-25-27--86328d0d91d6
