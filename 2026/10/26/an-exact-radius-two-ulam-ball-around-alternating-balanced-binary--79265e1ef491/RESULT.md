# An exact radius-two Ulam ball around alternating balanced binary words

## Finding

Fix an integer \(m\ge1\), and set \(n=2m\) and \(w_m=(01)^m\). Let \(\operatorname{LCS}(x,y)\) denote the length of a longest common subsequence. Define the constant-composition Ulam ball
\[
B_m=\{v\in\{0,1\}^{2m}: |v|_0=|v|_1=m,\ \operatorname{LCS}(v,w_m)\ge 2m-2\}.
\]
Its cardinality is exactly
\[
\boxed{|B_m|=\frac{m^4-2m^3+5m^2+4}{4}}\quad(m\ge1).
\]
The mechanism is a stronger membership criterion. For every binary word \(v=v_1\cdots v_{2m}\), write \(e(v)=|\{i:1\le i<2m,\ v_i=v_{i+1}\}|\). Then
\[
\operatorname{LCS}(v,w_m)\ge2m-2\iff
(e(v)\le3)\ \lor\ (e(v)=4\text{ and }v_1=0).
\]
This criterion also covers words with unequal zero/one frequencies; only the displayed cardinality imposes equal frequencies.

## Assumptions and scope

Binary letters are the symbols \(0,1\); subsequences preserve order. For equal-length words with identical Parikh vectors, the Ulam distance is length minus longest-common-subsequence length. The radius is exactly *at most two*, not exactly two. The center alternates and begins with zero; swapping the names of zero and one gives the analogous theorem for the opposite phase. The result applies to all integer \(m\ge1\), including \(m=1\) where the threshold \(n-2\) is zero and \(|B_1|=2\).

## Proof

**1. Alternating-subsequence embedding cost.** Let \(u=u_1\cdots u_L\) be any nonempty binary word. Its earliest greedy embedding into the infinite alternating word \(010101\cdots\), with positions indexed from one, ends at position
\[
L+e(u)+\mathbf1_{\{u_1=1\}}.
\]
Indeed, the first symbol matches at position one for zero and position two for one; each subsequent unequal pair advances one position, whereas an equal pair advances two. Therefore \(u\) embeds in \(w_m\) if and only if its displayed cost is at most \(2m\). In particular, for \(|u|=2m-2\), the criterion is \(e(u)+\mathbf1_{\{u_1=1\}}\le2\). The empty word (possible for \(m=1\)) embeds trivially.

**2. Necessity.** Deleting any one letter from a binary word reduces its number of equal adjacent pairs by at most one. Thus every word \(u\) obtained by exactly two deletions from \(v\) has \(e(u)\ge e(v)-2\). If \(e(v)\ge5\), the required length-\(2m-2\) subsequence cannot embed, since it has at least three equal adjacencies. Suppose instead \(e(v)=4\) and \(v_1=1\). If the retained word begins with one, then \(e(u)\ge2\) and its embedding cost exceeds \(2m\). If it begins with zero, the initial run of ones in \(v\) must be deleted completely. Since only two deletions are allowed, this initial run has length one or two. Removing a one-letter initial run does not reduce \(e\), and removing a two-letter initial run decreases \(e\) by exactly one. After any remaining deletion, the resulting word consequently has \(e(u)\ge3\) when it begins with zero, again impossible. This establishes the necessary alternatives.

**3. Sufficiency.** If \(e(v)\ge2\), repeatedly delete the *last* letter of any constant run of length at least two. Each deletion decreases \(e\) by exactly one and preserves the first letter. After two such deletions, the retained length-\(2m-2\) word \(u\) has \(e(u)=e(v)-2\) and \(u_1=v_1\). The embedding criterion from Step 1 applies when \(v_1=0\) and \(e(v)\le4\), or \(v_1=1\) and \(e(v)\le3\). If \(e(v)=1\), deleting one nonfirst letter of its unique repeated run gives an alternating word of length \(2m-1\); it embeds in \(w_m\), whether its initial letter is zero (end position \(2m-1\)) or one (end position \(2m\)). If \(e(v)=0\), the word is alternating: it equals \(w_m\) when it begins with zero, while deleting its first one gives the first \(2m-1\) letters of \(w_m\) when it begins with one. This proves the full criterion, including the small-length cases.

**4. Exact run enumeration.** Write \(k=e(v)\). A word of length \(2m\) with exactly \(k\) equal boundaries has exactly \(2m-k\) nonempty constant runs. For a balanced binary word with an even number of runs, the two symbols have equal numbers of runs; compositions of \(m\) into a fixed positive number of parts count these words. For odd run count, the starting symbol has one extra run. These compositions yield the following respective numbers of balanced words with \(k=0,1,2,3\):
\[
2,\quad 2(m-1),\quad 2(m-1)^2,\quad (m-1)^2(m-2).
\]
For \(k=4\), only the words starting with zero qualify, and there are exactly \(\binom{m-1}{2}^{\!2}\) such balanced words. As usual a binomial coefficient vanishes when its lower index is not between zero and the upper index. The sum is
\[
2+2(m-1)+2(m-1)^2+(m-1)^2(m-2)+\binom{m-1}{2}^2
=\frac{m^4-2m^3+5m^2+4}{4},
\]
valid also for \(m=1,2\), completing the proof.

## Verification

The included standard-library program `verify_alternating_jumble.py` computes longest-common-subsequence lengths by a separate dynamic program, exhaustively compares the run criterion for *all* \(2^{2m}\) binary words for \(1\le m\le6\), and confirms the balanced counts \(2,6,19,53,126,262\). It additionally checks the closed formula against the run-composition sum for \(1\le m<500\). This finite verification is supplementary; the unrestricted parameter theorem follows from the preceding proof and not from extrapolating the finite checks. Reproduce using `python3 verify_alternating_jumble.py`.

## Relationship to prior work

Fleischmann et al. (2026, arXiv:2610.17910v1), Definition 6, use the longest-common-subsequence condition to define jumbled neighborhoods and Lemma 8 gives a general upper bound. Their full text does not supply this alternating-center membership classification or exact balanced two-jumble count. Kong and Hagiwara (2017, arXiv:1701.03896v1) and Kong (2017/2019, arXiv:1712.03639v2) study multipermutation Ulam spheres. They compute sphere sizes for arbitrary centers at radius one and for sorted centers at arbitrary radius; the present center is alternating and the radius is two, so those formulas do not directly imply this result. The same-symbol relabeling of an alternating center cannot turn it into a sorted center except at the trivial size.

## Limitations

The theorem does not classify all possible centers, establish whether the alternating center is globally extremal, or give a general radius beyond two. The full jumbled neighborhood without fixed Parikh content is larger than the counted ball, although the membership criterion characterizes that full neighborhood. A literature search cannot rule out all unindexed equivalent observations; independent scrutiny has not been performed.

## References

1. P. Fleischmann, A. Huch, S. Kim, T. Koß and E. Wiards, *Jumbled Simon's Equivalence and Embeddings*, arXiv:2610.17910v1 (first public: 2026-10-13), Definition 6 and Lemma 8. https://arxiv.org/abs/2610.17910
2. J. Kong and M. Hagiwara, *Multipermutation Ulam Sphere Analysis Toward Characterizing Maximal Code Size*, arXiv:1701.03896v1 (2017), Sections IV–VII. https://arxiv.org/abs/1701.03896
3. J. Kong, *Ulam Sphere Size Analysis for Permutation and Multipermutation Codes Correcting Translocation Errors*, arXiv:1712.03639v2 (originally 2017; revision 2019), Sections III, V–VII and Table III. https://arxiv.org/abs/1712.03639
