# Circular mesosome avoidance: a parity classification and exact binary necklace counts

## Finding

A **mesosome** is a nonempty even-length word \(xy\) in which \(y\) is a cyclic conjugate of \(x\) but \(y\neq x\). For an integer \(n\geq 1\), a binary circular word of circumference \(n\) is **one-turn mesosome-free** when none of its circular contiguous factors of lengths at most \(n\) is a mesosome. The restriction to one turn matters: it does not assert avoidance in the infinite periodic repetition.

**Theorem.** For \(n\geq 3\), precisely the following binary necklaces of length \(n\) are one-turn mesosome-free, where necklaces identify circular rotations but **not** symbol complements:

1. The two constant necklaces \(0^n\) and \(1^n\).
2. The two-run necklaces represented by \(0^a1^{n-a}\) with \(1\leq a<n\), provided either \(\min(a,n-a)=1\), or both \(a\) and \(n-a\) are odd.
3. If \(n\) is even, the alternating necklace represented by \((01)^{n/2}\).

The third family is disjoint from the second for \(n\geq 4\). Consequently, the exact number \(N_n\) of such necklaces is
\[
N_1=2,\qquad N_2=3,\qquad
N_n=\begin{cases}4,&n\geq3\text{ odd},\\n/2+3,&n\geq4\text{ even}.\end{cases}
\]
The corresponding number \(L_n\) of distinct labeled linear presentations of these circular words (not modulo rotation) is
\[
L_1=2,\qquad L_2=4,\qquad
L_n=\begin{cases}2+2n,&n\geq3\text{ odd},\\n^2/2+4,&n\geq4\text{ even}.\end{cases}
\]
In particular, odd circumferences at least three have exactly four qualifying necklaces, while even circumferences have linearly many. The enumeration is an all-length classification, not a claim about infinite periodic mesosome avoidance.

## Assumptions and scope

Words use the fixed alphabet \(\{0,1\}\); \(n\) is any positive integer. A circular factor of length \(k\leq n\) begins at one of the \(n\) cyclic positions, uses exactly \(k\) successive letters, and may cross the chosen linear boundary. Length-zero factors are ignored. Every mesosome has half-length at least two because half-length one would make \(x=y\). A rotation class with two cyclic runs has one maximal \(0\)-run and one maximal \(1\)-run. Counting \(L_n\) includes all different linear starting positions but does not count identical periodic rotations more than once.

The argument invokes the published and independently inspectable binary *linear* mesosome-free run lemmas in Cummings–Shallit–Staadecker (2021). Its additional assertion is simultaneous avoidance under **every** rotation, with the resulting cyclic structure and counts; these do not appear as counts in that source.

## Proof

**Reduction to rotations.** Every circular factor of length at most \(n\) is a factor of some length-\(n\) rotation, and every factor of such a rotation is a circular factor. Hence one-turn avoidance is equivalent to the statement that **each** rotation is a linearly mesosome-free word. A nonconstant binary circle has an even number \(r\geq2\) of cyclic maximal runs. We analyze all possible \(r\).

**Two runs.** Write the circle as \(0^a1^b\), with \(a,b\geq1\) and \(a+b=n\). A rotation can either start at a run boundary, leaving at most two linear runs, or split one cyclic run into two edge-runs. If it splits the zero-run (which requires \(a\geq2\)), it has the form \(0^i1^b0^{a-i}\) for \(1\leq i<a\), and Lemma 1 of Cummings–Shallit–Staadecker states that such a three-run word is mesosome-free exactly when its middle-run length \(b\) is odd. Similarly, when \(b\geq2\), splitting the one-run forces \(a\) odd. Thus the necessary and sufficient conditions are \((a=1\text{ or }b\text{ odd})\) and \((b=1\text{ or }a\text{ odd})\). These are exactly \(\min(a,b)=1\) or both \(a,b\) odd. The same cited lemma and the elementary two-run case establish sufficiency for every rotation, not just necessity.

**Four runs.** Suppose the cyclic run lengths in order are \((a,b,c,d)\), all positive. A rotation beginning at a run boundary produces a four-run *linear* word. Lemma 2 of Cummings–Shallit–Staadecker states the precise criterion for the linear word \(0^a1^b0^c1^d\): either \(b=c=1\), or \(a<c\), \(b>d\), and \(b,c\) odd. Write this criterion as \(F(a,b,c,d)\); the criterion is invariant under swapping the names of zeros and ones, so it applies to each cyclic permutation of the run-length quadruple. If both \(F(a,b,c,d)\) and \(F(c,d,a,b)\) used their second alternative, the first would require \(a<c\) while the second would require \(c<a\). Thus some boundary rotation, after cyclic relabeling, must have \(b=c=1\). Next \(F(b,c,d,a)=F(1,1,d,a)\) cannot use its second alternative, since its first run has length \(1\) and its third run length \(d\), while its second run has length \(1\) and fourth length \(a\geq1\), violating strict inequality \(1>a\); hence its first alternative gives \(d=1\). The following rotation \(F(c,d,a,b)=F(1,1,a,1)\) also cannot use the second alternative (it would require \(1>1\)), so \(a=1\). All four runs are singleton, making the circle alternating.

**At least six runs.** Choose any five consecutive complete cyclic runs. Since at least one further nonempty run lies outside them, these five runs form a linear circular factor of length strictly less than \(n\). Lemma 3 of Cummings–Shallit–Staadecker says a mesosome-free linear word with exactly five runs must be \(01010\) or its complement, forcing each of these five run lengths to equal one. Moving the five-run window cyclically proves *every* run singleton. Thus again the circle is alternating, of even circumference.

**Sufficiency of alternating circles.** Every factor of an alternating circle is alternating. For a potential mesosome \(xy\), if the half-length is even then \(x=y\); if the half-length is odd, the two halves have opposite starting bits and therefore different zero/one counts, so they cannot be conjugate. Constants avoid mesosomes trivially. The two-run case was settled above. This completes the classification for \(n\geq3\); the two binary circles of length one and the three necklaces \(00,01,11\) of length two can be checked directly.

**Necklace counts and presentations.** Distinct two-run necklaces are determined by the positive ordered pair \((a,n-a)\), because the number of zeros is rotation-invariant. For odd \(n\geq3\), two odd positive lengths cannot sum to \(n\), leaving exactly \(a=1\) or \(a=n-1\), so there are two two-run necklaces and two constants. Every such two-run necklace has exact period \(n\) and hence \(n\) distinct rotations. Thus \(N_n=4\), \(L_n=2+2n\). For even \(n\geq4\), the allowed pairs are precisely the \(n/2\) positive odd pairs \((a,n-a)\). There are also two constants and one alternating necklace (having only two distinct rotations), giving \(N_n=n/2+3\) and \(L_n=(n/2)n+2+2=n^2/2+4\). The exceptional length-two alternating circle is simultaneously a two-run necklace, so is counted only once.

## Verification

Run `python3 check.py` from the directory containing the enclosed checker. This program independently tests each binary word at every length \(1\leq n\leq15\) for circular mesosomes by exhaustive scanning of all starts and all even lengths at most the circumference, and compares that result with the classified run-count condition. It separately canonicalizes necklaces under rotation and verifies the exact formulas for their numbers and the numbers of linear presentations. The finite test covers \(65{,}534\) words and prints `CIRCULAR_MESOSOME_PASS tested_words=65534 n_range=1..15`. The mathematical all-length proof is the preceding argument relying on the published linear run lemmas; finite testing is a cross-check, not an infinite certificate.

## Relationship to prior work

Cummings, Shallit, and Staadecker, *Mesosome Avoidance*, arXiv:2107.13813v1 (29 July 2021), establishes a **complete linear** binary classification (their Theorem 1), its counts (Theorem 2), and infinite one-sided avoidance (Theorem 3). Their Lemmas 1, 2, and 3 are explicitly reused here. None of those statements directly enumerates necklaces satisfying all length-\(n\) cyclic rotation tests: this result derives the intersection of those tests and its parity-sensitive cyclic counts. The OEIS sequence A341277 records the linear counts and is not the necklace count derived here. For instance, at length six the published linear count is 32, while this work finds six one-turn-avoiding necklaces and 22 distinct qualified linear presentations.

The one-turn condition is **not** equivalent to infinite periodic avoidance. A circle such as \(0^31^3\) (circumference six) qualifies for one turn, although its infinite repetition need not avoid mesosomes. The difference in quantified factor length is essential to the claim.

## Limitations

The contribution is a consequence of the cited linear run lemmas plus new cyclic compatibility analysis, not a new proof of those lemmas. Any prior treatment of all rotations of the linear classification might imply this result; a targeted literature search did not identify one, but indexing is incomplete and independent audit has not been performed. The scope is binary only; the circular factor length is bounded by \(n\), and no extension to unbounded periodic factors is claimed.

## References

1. Robert Cummings, Jeffrey Shallit, and Paul Staadecker, *Mesosome Avoidance*, arXiv:2107.13813v1, posted 2021-07-29. Accessible full preprint: https://arxiv.org/pdf/2107.13813 . See Lemmas 1–3 and Theorems 1–3.
2. OEIS Foundation, *A341277 — Number of length-n binary mesosome-avoiding strings*, https://oeis.org/A341277 (linear words, not circular necklaces).
