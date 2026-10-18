# The complete one-deletion spectrum of three-marker binary necklaces

## Finding

For each integer \(s\geq 0\), consider all cyclic binary words (necklaces, modulo rotation but **not** reversal) with exactly three \(1\)'s and exactly \(s\) \(0\)'s. A **one-deletion descendant** is the necklace formed by removing one symbol, with distinct output rotations identified. Let \(B(w)\) be the number of **distinct** one-deletion descendants of \(w\), not the number of deletion positions. Let \(C_{s,j}\) count source necklaces for which \(B(w)=j\).

For \(s=0\), there is one source necklace, and \(C_{0,1}=1\). For every \(s\geq1\), put
\[
 e_s=\mathbf 1_{\{3\mid s\}},\qquad h_s=\mathbf 1_{\{s\geq5,\ s\equiv2\pmod3\}},\qquad z_s=\mathbf 1_{\{s=2\}},\qquad f_s=\left\lfloor\frac{s-1}{2}\right\rfloor.
\]
Then the **complete one-deletion sphere-size distribution** is
\[
\begin{aligned}
 C_{s,2}&=1+e_s, & C_{s,3}&=z_s,\\
 C_{s,4}&=s-1-z_s+h_s, & C_{s,5}&=f_s-e_s-h_s,\\
 C_{s,6}&=\frac{\binom{s-1}{2}-3f_s+2e_s}{3}.
\end{aligned}
\]
All other \(C_{s,j}\) vanish. The convention is \(\binom{m}{2}=0\) for integers \(m<2\). The total number of source necklaces is
\[
N_s=\frac{\binom{s+2}{2}+2e_s}{3}\quad(s\geq1),
\]
which equals the sum of these five counts.

In particular, **six distinct descendants are possible exactly from length nine onward**, because \(B(w)=6\) if and only if its three cyclic zero gaps are positive and pairwise distinct. The only length admitting \(B(w)=3\) is length five; thereafter all attainable values lie in \(\{2,4,5,6\}\). For uniformly sampled source necklaces at a given length, the exact mean is
\[
\mathbb E[B]=6-\frac{2s+f_s+2+3e_s+z_s+h_s}{N_s}\quad(s\geq1),
\]
and hence \(\mathbb E[B]=6-15/s+O(s^{-2})\), while \(\Pr(B=6)=1-9/s+O(s^{-2})\) as \(s\to\infty\). These asymptotics refer to uniform **necklaces**, not uniform labeled words.

## Assumptions and scope

Represent the source necklace uniquely up to a cyclic rotation of a nonnegative integer triple \((a,b,c)\) through
\[
w=[1\,0^a\,1\,0^b\,1\,0^c],\qquad a+b+c=s.
\]
Cyclic rotations of \((a,b,c)\) encode exactly the rotations of \(w\), even when some gaps vanish. Reflections are **not** identified. An output from deleting a \(1\) has two \(1\)'s; an output from deleting a \(0\) has three \(1\)'s. These two sets are disjoint, including all boundary cases. The binary alphabet, exact single-symbol deletion, and cyclic observation are essential hypotheses.

The individual value \(B(w)\), for \(s\geq1\), has the following complete classification:

* If exactly one gap is positive, then \(B(w)=2\).
* If exactly two gaps are positive, then \(B(w)=3\) precisely for a rotation of \((0,1,1)\); otherwise \(B(w)=4\).
* If all three gaps are positive and equal, then \(B(w)=2\).
* If all three are positive and pairwise distinct, then \(B(w)=6\).
* If all are positive and exactly two are equal, say \((t,t,u)\) up to permutation with \(u\neq t\), then \(B(w)=4\) exactly when \(u=t-1\); otherwise \(B(w)=5\).

For \(s=0\), \(B([111])=1\).

## Proof

**Gap representation.** Each occurrence of \(1\) specifies the start of one zero gap; choosing another \(1\) as the start rotates the gap triple, without changing its orientation. Therefore necklaces of weight three correspond bijectively to rotation classes of nonnegative triples of total \(s\).

**Deletion of a marker.** If one of the three \(1\)'s is deleted, the two neighboring zero gaps concatenate. The remaining two \(1\)'s have two zero gaps whose unordered lengths are \(\{a,s-a\}\), \(\{b,s-b\}\), or \(\{c,s-c\}\). Rotation interchanges the two gaps. Consequently the number of distinct marker-deletion descendants is exactly
\[
O(a,b,c)=\#\{\min(x,s-x):x\in\{a,b,c\}\}.
\]
The braces here denote the image set of the three indexed gap values, so repeated values are counted once. If all three gaps are positive, their marker-deletion outputs coincide exactly for equal gaps: two different positive gaps cannot sum to \(s\) because the third gap is positive. If exactly two gaps are positive, their marker deletions coincide (complementary gaps), whereas the zero gap produces the distinct unordered pair \(\{0,s\}\). If exactly one gap is positive, all three marker deletions coincide.

**Deletion of a zero.** Deleting a zero inside gap \(i\) decreases that gap by one; all zero deletions within a given positive gap give the same necklace. Thus the number of distinct zero-deletion descendants equals the number of cyclic rotation classes among
\[
(a-1,b,c)\ (a>0),\quad(a,b-1,c)\ (b>0),\quad(a,b,c-1)\ (c>0).
\]
The only nontrivial point is when distinct positive gaps give the same class. Relabel cyclically so that those gaps are the first and second. Write their reduced triples as \(u=(a-1,b,c)\) and \(v=(a,b-1,c)\). They cannot be equal without rotation. Equality after one cyclic shift of \(v\), namely \((b-1,c,a)\), forces \(a=b=c\). Equality after two shifts, namely \((c,a,b-1)\), forces \(a=b\) and \(c=a-1\). Conversely each condition makes the corresponding reductions rotationally equal, provided the deleted gaps are positive. Therefore **all** zero-deletion coincidences are accounted for by the all-equal case and the exceptional gap pattern \((t,t,t-1)\), with deletion in either of the two gaps of length \(t\). This also covers the boundary \((1,1,0)\). No appeal to finite enumeration is needed.

**Individual classification.** Add the two disjoint descendant counts. For one positive gap these counts are \((O,Z)=(1,1)\). For two positive gaps they are \((2,2)\), except for \((1,1,0)\), where \((O,Z)=(2,1)\). For three positive equal gaps they are \((1,1)\); for three positive distinct gaps they are \((3,3)\); and for three positive gaps with exactly two equal they are \((2,2)\) in the exceptional \((t,t,t-1)\) case and \((2,3)\) otherwise. This proves the complete five-way classification including the stated boundaries.

**Counting necklaces of each size.** One-positive-gap triples give one necklace for every \(s\geq1\). All-equal positive triples contribute one more size-two necklace exactly when \(3\mid s\). There are exactly \(s-1\) necklaces with one zero gap and two positive gaps: anchor at the unique zero gap, then the two ordered positive entries sum to \(s\). At \(s=2\), precisely one of these has pattern \((1,1,0)\) and size three. The exceptional all-positive class \((t,t,t-1)\) exists exactly when \(s=3t-1\) with \(t\geq2\), giving \(h_s\) additional size-four necklaces.

Among all-positive triples with exactly two equal gaps, let their repeated value be \(t\). The third value is \(s-2t\), so \(1\le t\le\lfloor(s-1)/2\rfloor\). For each such \(t\) there is exactly one cyclic necklace. Remove the all-equal option when \(s=3t\), and the exceptional size-four option when \(s=3t-1\). This gives \(C_{s,5}=f_s-e_s-h_s\).

Finally, the number of **ordered** triples of pairwise distinct positive integers summing to \(s\) is, by inclusion-exclusion,
\[
\binom{s-1}{2}-3\left\lfloor\frac{s-1}{2}\right\rfloor+2\mathbf 1_{\{3\mid s\}}.
\]
Such triples have three-element cyclic orbits, giving the asserted formula for \(C_{s,6}\). The size-six classification proves the sharp threshold \(s=6\): \((1,2,s-3)\) works for every \(s\geq6\), while three distinct positive gaps cannot sum below six.

Burnside's lemma gives the total number of source necklaces as \((\binom{s+2}{2}+2\mathbf1_{\{3\mid s\}})/3\), consistent with the sum above. Weighting the five classes by their deletion-ball sizes gives the exact mean; expanding its numerator and denominator gives the stated asymptotic formulas. This completes the proof for **all** nonnegative \(s\).

## Verification

The standalone standard-library program `verify.py` takes each cyclic gap triple of total \(s\) for all \(0\le s\le36\), directly constructs its binary circle, deletes every symbol, canonicalizes each resulting **binary** word under all rotations, and counts the distinct outputs. It compares this independent word-based count against both the gap formula and the five-way classification. It also groups all source necklaces at each length and compares the resulting histogram with the closed formulas and Burnside totals. Larger random gap triples with \(s\in\{45,61,90,128,256\}\) give supplementary checks. Successful local output was:

`PASS circular one-deletion three-marker profile: complete_zero_totals=0..36 necklaces=3055 random_larger_cases=450`

These finite checks are corroboration only: the proof of the unrestricted theorem is the gap-collision case analysis and inclusion-exclusion above.

## Relationship to prior work

Narayanan and Ren (2020) introduce circular deletion-channel trace reconstruction and use three-marker circular words in a lower-bound construction (Theorem 1.6, Section 5). Their concern is the sample complexity of distinguishing random trace distributions, not the degree distribution of the exact-one-deletion **rotation-quotiented** channel over all three-marker necklaces. Their conditional single-marker-deletion observation in Section 5 is compatible with the two-gap representation above, but does not give the zero-deletion collision classification or the counting formulas.

Bar-Lev, Etzion and Yaakobi (2021/2022) analyze ball sizes for *linear*, equal-length fixed-length Levenshtein distance, which combines deletions and insertions. Their run-statistic formulas cannot be substituted for rotation-identified exact single-deletion descendants. Ota and Manada (first public prepublication in 2023, final journal 2024) study unique reconstruction of circular words from **contiguous substring frequencies** and minimal absent factors, which is a different observation channel.

This theorem does not assert novelty for Burnside enumeration of necklaces, the elementary merging of two circular zero gaps after deleting a marker, or the already-known circular trace-reconstruction model. The asserted contribution is the **complete single-deletion descendant-size distribution** for the infinite weight-three family, including all exceptional collision types and exact finite-length sphere statistics.

## Limitations

The results concern binary necklaces with precisely three \(1\)'s, one deletion, and equality only under **rotation**. They do not describe full circular trace probabilities, distinguish source necklaces from a single received output, classify two-deletion spheres, or extend the formulas to more than three markers. The exact mean averages uniformly over source necklaces; weighting each necklace by its number of labeled rotations gives a different distribution. No independent audit or external replication has been performed. An equivalent enumeration could exist in older or unindexed combinatorial-word literature.

## References

1. S. Narayanan and M. Ren, *Circular Trace Reconstruction*, arXiv:2009.01346, first posted 2020-09-02. Relevant sections: Introduction, Theorem 1.6, and Section 5. https://arxiv.org/abs/2009.01346
2. D. Bar-Lev, T. Etzion, and E. Yaakobi, *On Levenshtein Balls with Radius One*, arXiv:2103.01681, first posted 2021-03-02. Relevant sections: I–III and ball-size results. https://arxiv.org/abs/2103.01681
3. T. Ota and A. Manada, *A Reconstruction of Circular Binary String Using Substrings and Minimal Absent Words*, DOI:10.1587/transfun.2023TAP0015, advance publication 2023-09-05; final version 2024. Relevant sections: 2–4. https://doi.org/10.1587/transfun.2023TAP0015
