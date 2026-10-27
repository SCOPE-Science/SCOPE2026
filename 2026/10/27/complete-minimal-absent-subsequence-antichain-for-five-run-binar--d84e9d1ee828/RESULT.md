# Complete minimal-absent-subsequence antichain for five-run binary words

## Finding

For every five-tuple of positive integers \(a,b,c,d,e\), let \(w=0^a1^b0^c1^d0^e\). A **minimal absent subsequence** is a binary word \(u\) that is not a scattered subsequence of \(w\), although all proper scattered subsequences of \(u\) are. In particular, **scattered** and **contiguous** occurrences are not interchangeable.

The entire minimal-absent-subsequence antichain consists of the following seven words, together with the six conditional words in the next display:
\[
\begin{aligned}
 &0^{a+c+e+1},\quad 1^{b+d+1},\\
 &0^{a+c+1}1,\quad 0^{a+1}1^{d+1},\\
 &1\,0^{c+e+1},\quad 1^{b+1}0^{e+1},\\
 &1\,0^{c+1}1.
\end{aligned}
\]
The additional words are:
\[
\begin{array}{c|l}
\text{word}&\text{necessary and sufficient condition}\\\hline
1\,0\,1^{d+1}&b\ge2\\
1^{b+1}0\,1&d\ge2\\
0^{a+1}1\,0^{e+1}&c\ge2\\
0^{a+1}1\,0\,1&c\ge2,\ d\ge2\\
1\,0\,1\,0^{e+1}&b\ge2,\ c\ge2\\
1\,0\,1\,0\,1&b\ge2,\ c\ge2,\ d\ge2.
\end{array}
\]
All listed words are pairwise distinct. With \(B=\mathbf 1_{b\ge2}\), \(C=\mathbf 1_{c\ge2}\), and \(D=\mathbf 1_{d\ge2}\), the exact antichain cardinality is
\[
K(w)=7+B+C+D+BC+CD+BCD\in\{7,8,9,10,13\}.
\]
The maximum is \(13\), attained precisely if all three interior run lengths are at least two. For fixed total length \(n\ge5\), the exact bivariate generating function is
\[
\sum_{a,b,c,d,e\ge1}z^{a+b+c+d+e}y^{K(w)}
=\frac{z^5}{(1-z)^2}\left(y^7+\frac{3z}{1-z}y^8+\frac{z^2}{(1-z)^2}(y^9+2y^{10})+\frac{z^3}{(1-z)^3}y^{13}\right).
\]
In particular, for a uniformly selected positive five-part composition of \(n\), the probabilities of cardinalities \(7,8,9,10,13\) are respectively
\[
\frac{\binom{n-4}{1}}{\binom{n-1}{4}},\quad
\frac{3\binom{n-4}{2}}{\binom{n-1}{4}},\quad
\frac{\binom{n-4}{3}}{\binom{n-1}{4}},\quad
\frac{2\binom{n-4}{3}}{\binom{n-1}{4}},\quad
\frac{\binom{n-4}{4}}{\binom{n-1}{4}},
\]
where an out-of-range binomial coefficient means zero. Thus \(\Pr(K(w)=13)\to1\) and \(\mathbb E[K(w)]=13-40/n+O(n^{-2})\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\); all five runs are nonempty; subsequences permit gaps and retain order; minimality concerns deleting any nonempty selection of letters. Checking that each **single-letter deletion** embeds suffices, because the subsequence relation is transitive. The result treats all positive run parameters simultaneously, not merely a finite computational window. The parameter distribution samples all positive five-part compositions uniformly, rather than weighting binary words from all run counts.

## Proof

Write \(u\preceq w\) for scattered-subsequence containment. A word with \(k\) runs requires at least \(k\) alternating run occurrences. The word \(w\) begins and ends with zero and has just two one-runs. Consequently \(10101\not\preceq w\). Any word of at least six alternating runs contains \(10101\) as a **proper** subsequence, hence cannot be minimally absent. This reduces completeness to at most five runs.

**One run.** Total symbol capacities are \(a+c+e\) zeros and \(b+d\) ones; the two monochromatic minimal absent words are exactly the first two in the display.

**Two runs beginning in zero.** For positive \(p,q\), the word \(0^p1^q\) occurs if and only if
\[
(p\le a\ \land\ q\le b+d)\ \lor\ (p\le a+c\ \land\ q\le d).
\]
After excluding words whose proper one-run subsequence is absent, the only minimal outside corners of this union of rectangles are \(0^{a+c+1}1\) and \(0^{a+1}1^{d+1}\). Similarly \(1^p0^q\) occurs iff
\[
(p\le b\ \land\ q\le c+e)\ \lor\ (p\le b+d\ \land\ q\le e),
\]
and its minimal outside corners are \(1\,0^{c+e+1}\) and \(1^{b+1}0^{e+1}\). These are precisely the four two-run entries.

**Three runs beginning in zero.** Suppose \(0^p1^q0^r\) is minimally absent. Its proper subsequence \(1^q0^r\) embeds. If \(p\le a\), those first-run zeros can always be prepended, contradicting absence. By the dual argument, embeddability of \(0^p1^q\) implies \(r>e\). Minimality under deletion of any letter from the first or last block forces \(p=a+1\) and \(r=e+1\); deletion from the middle block forces \(q=1\). The sole possible word is \(0^{a+1}1\,0^{e+1}\). Its one-letter deletions in the zero blocks embed by using the intermediate zero-run; deleting its sole one gives \(0^{a+e+2}\), which embeds iff \(c\ge2\).

**Three runs beginning in one.** The word \(1^p0^q1^r\) occurs exactly when \(p\le b,q\le c,r\le d\), since its two one-blocks must lie on opposite sides of the middle zero-run. A minimally absent word must exceed exactly one of these three capacities by one and use one in the other two coordinates. The three candidates are \(1^{b+1}0\,1\), \(1\,0^{c+1}1\), and \(1\,0\,1^{d+1}\). For the first candidate, deleting its zero produces \(1^{b+2}\), which embeds iff \(d\ge2\); for the third, the same test requires \(b\ge2\). For the middle candidate, deleting any one letter permits a shifted embedding, because \(a,e\ge1\), and its middle zero-block is exactly one too long. All conditions in the display follow.

**Four runs beginning in zero.** A word \(0^p1^q0^r1^s\) embeds if and only if \(p\le a,q\le b,r\le c,s\le d\): each run must occupy its corresponding run of \(w\). Its proper three-run suffix \(1^q0^r1^s\) can occur only within capacities \(b,c,d\), forcing the latter three inequalities. Thus any minimally absent four-run word must have \(p>a\), and single-letter deletion minimality forces exactly \(0^{a+1}101\). Deleting either of its middle one-letter runs gives a subsequence precisely when, respectively, \(c\ge2\) and \(d\ge2\); the other two deletion types always embed. This yields the \(c,d\ge2\) condition.

**Four runs beginning in one.** Dually \(1^p0^q1^r0^s\) embeds iff \(p\le b,q\le c,r\le d,s\le e\); its three-run prefix forces the first three capacities. The unique possible minimally absent form is \(101\,0^{e+1}\). Deleting the internal zero or the second one gives embeddings iff \(b\ge2\) and \(c\ge2\), respectively; the remaining deletion types automatically embed.

**Five runs beginning in zero.** A five-run word \(0^p1^q0^r1^s0^t\) embeds iff each of its run lengths is at most the matching run length of \(w\). If it is minimally absent, its proper four-run prefix and suffix both embed, jointly forcing all five inequalities, a contradiction.

**Five runs beginning in one.** Such a word never embeds, since \(w\) contains just two one-runs. If any run contains at least two letters, deleting one leaves a five-run word beginning in one, still absent; hence the only candidate is \(10101\). Deleting each one-letter position confirms that all proper subsequences embed exactly when \(b,c,d\ge2\); its first and last deletions embed automatically. This completes the antichain classification.

**Enumeration.** Increasing the three interior run lengths from one to two costs one additional symbol for each threshold satisfied, while the outer lengths remain arbitrary positive integers. The five threshold patterns with possible cardinalities \(7,8,9,10,13\) have multiplicities \(1,3,1,2,1\), respectively, indexed by zero, one, the nonadjacent pair, the two adjacent pairs, and all three satisfied thresholds. Their free positive compositions give the displayed rational generating function. Coefficient extraction yields the binomial formulas. The mass at \(13\) tends to one, and subtracting the deficits gives
\[
13-\mathbb E[K(w)]=\frac{6\binom{n-4}{1}+15\binom{n-4}{2}+10\binom{n-4}{3}}{\binom{n-1}{4}}
=\frac{40}{n}+O(n^{-2}).
\]

## Verification

The accompanying standalone `verify.py` constructs the complete scattered-subsequence set, independently enumerates all absent one-letter extensions whose single-letter deletions occur, and compares the resulting exact sets against all conditional templates for each of the \(5^5=3125\) parameter tuples with all run lengths from one through five. It additionally tests 79 larger selected parameter tuples and all fixed-length composition histograms for \(5\le n\le30\). These finite computations are corroboration of, **not substitutes for**, the preceding proof for arbitrary run lengths. Running `python verify.py` requires only Python's standard library.

## Relationship to prior work

Kosche, Koß, Manea and Siemer give general structural characterizations and algorithms for absent and minimal absent subsequences, including broad bounds and general examples [1]. The present specialized result supplies the explicit nonredundant five-run antichain, its threshold law and bivariate distribution; the general algorithm may enumerate the same words on a given input, but the inspected sections do not state the parameter-uniform closed classification or length distribution. Adamson and coauthors [2] study counts of absent subsequences of a prescribed length, a different statistic from the minimal-antichain cardinality here. Manea and coauthors [3] give more efficient general MAS/SAS enumeration algorithms but not the five-run symbolic closed form in the inspected sections. The four-run case may be separately classified; these formulas concern a distinct five-run family, not a mere recoloring or pure-parameter substitution.

## Limitations

The theorem only concerns binary words with exactly five positive alternating runs and counts minimal absent **scattered subsequences**. It does not give a general formula for arbitrarily many runs, all absent subsequences, or minimal absent contiguous factors. Search and comparison cover accessible versions and inspected relevant sections, not every unindexed publication or possible equivalent specialization. Any mathematical priority claim beyond these comparisons requires further external verification; independent audit has not been performed.

## References

[1] D. Kosche, F. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, first submitted 2021-08-31. https://arxiv.org/abs/2108.13968

[2] A. Adamson et al., *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599, first submitted 2024-07-26. https://arxiv.org/abs/2407.18599

[3] F. Manea et al., *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471, first submitted 2025-04-30. https://arxiv.org/abs/2504.21471
