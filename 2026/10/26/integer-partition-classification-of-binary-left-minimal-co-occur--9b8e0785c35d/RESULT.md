# Integer-partition classification of binary left-minimal co-occurrence profiles

## Finding

Fix the binary alphabet \(\{0,1\}\) and the required itemset \(Q=\{0,1\}\). For a length-\(n\) binary word \(w\), let \(L_w(h)\) be the number of intervals of length \(h\) containing both symbols for which deletion of the *leftmost* position destroys that property. Such intervals are called **left-minimal co-occurrences**. We use the full query-answer profile \((L_w(1),\ldots,L_w(n))\), not the ordinary all-window co-occurrence profile.

Write \(p(t)\) for the number of integer partitions of \(t\), with \(p(0)=1\). For every \(n\ge1\), the number of distinct left-minimal co-occurrence profiles of length-\(n\) binary words is exactly

\[
A_n=\sum_{t=0}^{n-1}p(t).
\]

Equivalently,

\[
\sum_{n\ge1}A_n z^n=\frac{z}{1-z}\prod_{j\ge1}\frac{1}{1-z^j}.
\]

More precisely, profiles are canonically indexed by all integer partitions \(\lambda\) of all integers \(0\le t\le n-1\). For a partition other than the empty partition and, when \(n\ge2\), the singleton partition \((n-1)\), write \(m_j\) for its multiplicity of the part \(j\), and \(k=\sum_jm_j\). Set \(\Delta_w(2)=L_w(2)-L_w(1)\) and \(\Delta_w(h)=L_w(h)-L_w(h-1)\) for \(3\le h\le n\). Its associated profile is characterized by

\[
\Delta_w(2)=k,\qquad \Delta_w(j+2)=-m_j\quad(1\le j\le n-2).
\]

The empty partition gives the zero profile; the exceptional partition \((n-1)\) gives \(\Delta_w(2)=1\) and every later difference zero. The full vector \(L_w\) is recovered by cumulative summation from \(L_w(1)=0\).

Every ordinary nonempty partition \(\lambda\) has exactly

\[
\frac{2k!}{\prod_{j\ge1}m_j!}
\]

binary words in its profile fiber. The empty and exceptional partitions have exactly two words each (the exceptional case exists only when \(n\ge2\)). Thus the theorem gives every ambiguity-class size, not merely the number of profiles.

For the sparse-difference parameter \(d_w=\#\{h:2\le h\le n,\Delta_w(h)\ne0\}\), its exact maximum is

\[
\max_{w\in\{0,1\}^n}d_w=
\begin{cases}
0,&n=1,\\
1,&n=2,\\
1+\left\lfloor\dfrac{\sqrt{8n-7}-1}{2}\right\rfloor,&n\ge3.
\end{cases}
\]

For every \(k\ge2\), the shortest words attaining \(d_w=k+1\) have length \(1+k(k+1)/2\), and precisely \(2k!\) words of that shortest length attain it.

## Assumptions and scope

All words have a prescribed positive length \(n\), with alphabet *exactly* \(\{0,1\}\). A co-occurrence interval is contiguous and nonempty. The deletion test removes only the left endpoint; it does not require right-minimality. A profile records the counts for every integer window length \(1\le h\le n\). The empty integer partition is permitted, and the single part \((n-1)\) is exceptional only for \(n\ge2\). The statement does **not** assert the same enumeration for ordinary co-occurrence counts, an alphabet containing symbols outside \(Q\), or itemsets of size greater than two.

## Proof

**Run decomposition.** Let \(w\) have \(m\) maximal constant runs, with positive lengths \(a_1,\ldots,a_m\) summing to \(n\). If \(m=1\), no interval contains both letters, so the profile is zero. If \(m\ge2\), any left-minimal mixed interval must start at the last letter of a run: otherwise removing its first letter would leave the same symbol elsewhere in the interval, so the interval would remain mixed. It must end in the immediately following run: after reaching the next run transition, removing its first letter would again leave both symbols. Conversely, every interval starting at the last letter of run \(i\) and ending anywhere in run \(i+1\) is left-minimal. Hence, for every \(1\le h\le n\),

\[
L_w(h)=\sum_{i=2}^m \mathbf 1_{\{2\le h\le a_i+1\}}.
\]

Therefore \(\Delta_w(2)=m-1\) and, for every \(3\le h\le n\),

\[
\Delta_w(h)=-\#\{i:2\le i\le m,\ a_i=h-2\}.
\]

These identities remain valid when the indicated sets are empty. Notice the endpoint convention: a noninitial run of length \(n-1\) creates a negative difference only at \(n+1\), *outside* the observed range. It can occur only for \(m=2\) and \(a_1=1\).

**Partition bijection.** The multiset of the noninitial run lengths \(a_2,\ldots,a_m\) is an integer partition \(\lambda\) of \(t=n-a_1\le n-1\); a constant word corresponds to the empty partition. Conversely, every partition \(\lambda\) of some \(0\le t\le n-1\) is realizable: choose the first run to have length \(n-t\), and append runs whose lengths are the parts of \(\lambda\) in any order, alternating the binary symbol. For all nonempty partitions except \((n-1)\), no part exceeds \(n-2\), and the displayed difference formula determines each part multiplicity from its negative entries. It determines the number of parts from the difference at width two. For \((n-1)\), the difference at width two is one and there are no negative differences in the observed range, separating it both from ordinary nonempty partitions and from the empty partition. Thus two distinct partitions yield distinct profiles, while every binary word induces one partition. The asserted bijection and count follow.

**Fibers.** With \(\lambda\) fixed, the initial run length is forced to be \(n-t\), its letter has two choices, and the \(k\) subsequent run lengths may occur in precisely \(k!/\prod_j m_j!\) different orders. This gives the stated fiber size. For \(\lambda=\varnothing\), there are the two constant words; for \(\lambda=(n-1)\), the two words have one initial letter followed by \(n-1\) copies of the other letter. Summing the class sizes recovers all \(2^n\) binary words.

**Sharp sparse support.** If a nonexceptional word has \(k\) distinct noninitial run lengths, its nonzero difference indices are width two and the \(k\) indices obtained by adding two to those lengths. The smallest possible sum of \(k\) distinct positive run lengths is \(k(k+1)/2\), and at least one position is needed for the initial run, so \(1+k(k+1)/2\le n\). For \(n\ge3\), the largest such \(k\) satisfies the displayed square-root formula and is attained by noninitial runs of lengths \(1,\ldots,k\) and a first run using all leftover positions. The empty and exceptional partitions have respectively zero and one nonzero differences, yielding the two small-length boundary cases. When \(k\ge2\) and \(n=1+k(k+1)/2\), equality forces the first run to have length one and the other run lengths to be exactly \(1,\ldots,k\); there are exactly \(2k!\) such words.

## Verification

A dependency-free verifier, `verify_profiles.py`, independently constructs left-minimal windows directly from their definition, comparing them with the run formula. It enumerates all binary words for \(1\le n\le15\), checks the cumulative partition count, checks the entire fiber-size multiset (not just the number of classes), and checks the sharp maximum of the sparse-difference parameter. The finished verifier reports `VERIFY_OK` after checking \(65{,}534\) words. These finite tests are corroboration; the proof above establishes the statement for all positive lengths.

The first fifteen profile counts are \(1,2,4,7,12,19,30,45,67,97,139,195,272,373,508\), agreeing with the known cumulative integer-partition sequence.

## Relationship to prior work

Bille, Gørtz and Stordalen introduced the sparse difference parameter for left-minimal co-occurrences and proved general data-structure bounds of order \(O(d)\) and \(O(\sqrt{nq})\). Their Lemma 1 describes general intervals arising from minimal co-occurrences; specialized to a binary alphabet with \(Q=\{0,1\}\), it is compatible with the run identity above, but their theorem does not count attainable query-answer profiles, enumerate their fibers, or establish the exact finite-length extremum. Sobel and collaborators established all-window-length co-occurrence algorithms using gap histograms and obtained a triangular-number estimate for storage complexity; the exact left-minimal profile partition classification is a different statement. The numerical sequence itself is already tabulated as OEIS A000070, so the mathematical claim is the new interpretation, bijection and fiber classification, **not** discovery of the sequence or of integer partitions.

## Limitations

The classification is for left-minimal mixed-window counts over exactly two symbols. It does not classify the ordinary number of mixed windows of each length, does not establish a novel algorithm for the general co-occurrence problem, and does not assert that the count sequence is new. The originality comparison is not an independent bibliographic audit; equivalent unindexed enumerations remain a residual literature risk. No external formal proof verification was performed.

## References

1. P. Bille, I. L. Gørtz and T. Stordalen, *The Complexity of the Co-Occurrence Problem*, arXiv:2206.10383, first publicly posted 2022-06-21; especially Theorem 1 and Lemma 1. https://arxiv.org/abs/2206.10383
2. J. Sobel, N. Bertram, C. Ding, F. Nargesian and D. Gildea, *AWLCO: All-Window Length Co-Occurrence*, arXiv:2011.14460, first publicly posted 2020-11-29; CPM 2021, DOI 10.4230/LIPIcs.CPM.2021.24. https://arxiv.org/abs/2011.14460
3. OEIS Foundation, *A000070: partial sums of partition numbers*, https://oeis.org/A000070 (numerical sequence identity, not a prior statement about co-occurrence profiles).
