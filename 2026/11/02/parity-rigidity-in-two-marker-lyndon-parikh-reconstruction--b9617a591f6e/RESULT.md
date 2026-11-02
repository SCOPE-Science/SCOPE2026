# Parity rigidity in two-marker Lyndon–Parikh reconstruction

## Finding

Let \(\Sigma=\{0,1\}\) with \(0<1\). For a word \(w\), let \(P(w)\) be its ordinary binary Parikh matrix (recording counts of \(0\), of \(1\), and of the scattered subsequence \(01\)). Let \(L(w)\) be the lexicographically smallest cyclic rotation of \(w\). Consider the joint observation
\[
\mathcal O(w)=(P(w),P(L(w))).
\]
For each integer \(N\ge0\), restrict the input to the \(\binom{N+2}{2}\) words containing exactly \(N\) zeros and exactly two ones.

**Theorem (complete ambiguity classification).** Every fiber of \(\mathcal O\) on this fixed-composition input set has cardinality at most two. If \(N\) is odd, every fiber is a singleton. If \(N=2h\) is even, the entire collection of doubleton fibers is indexed without repetition by the integers \(0\le t<h\) and \(0\le j\le t\); the two words in the corresponding fiber are
\[
\begin{aligned}
 u_{h,t,j}&=0^j1\,0^{2h-t}1\,0^{t-j},\\
 v_{h,t,j}&=0^{j+h-t}1\,0^t1\,0^{h-j}.
\end{aligned}
\]
Consequently, when \(N=2h\), exactly \(h(h+1)/2\) observations have two preimages, exactly \((h+1)^2\) have one preimage, and exactly \((h+1)(3h+2)/2\) observations occur. For odd \(N\), all \(\binom{N+2}{2}\) observations are distinct. In particular, the maximum size of a zero-error code for this deterministic observation, within the fixed-composition input set, equals the number of occurring observations. The exact uniquely recoverable fraction is \(1\) for odd \(N\), and \((h+1)/(2h+1)\) when \(N=2h\).

## Assumptions and scope

The Parikh matrix uses scattered (not contiguous) occurrences of \(01\) and the fixed order \(0<1\). The canonical conjugate \(L(w)\) is a cyclic rotation of the *same word*, not the lexicographically smallest word in the entire original Parikh-matrix equivalence class (a different convention sometimes termed a Lyndon image). Both matrices are observed. Source words are linear, have exactly two labeled \(1\) symbols, and are not identified under rotation or reversal. Length is \(N+2\); the boundary case \(N=0\) is included. No noise channel or multiple-observation statistics are assumed.

## Proof

Every permitted word has a unique representation
\[
 w=0^a1\,0^b1\,0^c,\qquad a,b,c\in\mathbb Z_{\ge0},\quad a+b+c=N.
\]
The number of scattered \(01\) pairs is \(x(w)=2a+b\): the first \(1\) has \(a\) zeros preceding it and the second has \(a+b\). Since the single-letter counts are fixed, this determines \(P(w)\).

There are exactly two circular gaps of zeros between the two ones, of sizes \(b\) and \(a+c=N-b\). Among the cyclic rotations, a lexicographically least word begins with the longer zero run, followed by a one, then the shorter run, then the remaining one (the equal-gap case gives the same periodic representative). Thus
\[
 L(w)=0^{\max\{b,N-b\}}1\,0^{\min\{b,N-b\}}1,
\]
with the same formula when a gap is empty. Its scattered \(01\) count is
\[
 y(w)=N+\max\{b,N-b\}.
\]
Accordingly, the joint observation on this slice is equivalent to the integer pair
\[
 (x,y)=(2a+b,\ N+\max\{b,N-b\}). \tag{1}
\]

If the pair in (1) is given, the number \(\ell=y-N\) is the longer circular gap. The only possible values of \(b\) are \(\ell\) and \(N-\ell\). Each such value determines \(a=(x-b)/2\) and \(c=N-a-b\) uniquely. Hence every fiber has at most two words. When \(N\) is odd, the two candidate values for \(b\) have opposite parity, so only one can give integral \(a\); all fibers are singletons.

Suppose \(N=2h\). A doubleton requires distinct gap sizes, and thus a uniquely determined smaller gap \(t=\min\{b,2h-b\}\) satisfying \(0\le t<h\). The word whose middle gap is the larger \(2h-t\) has exterior zero counts summing to \(t\), so write them \(j\) and \(t-j\), with \(0\le j\le t\). Its scattered-pair count is \(x=2j+2h-t\). For the word with middle gap \(t\) to have the same count, its first exterior run is forced to be \(j+h-t\), and its last run is forced to be \(h-j\), both nonnegative. This proves that the two words displayed in the theorem form one fiber. Conversely, all doubletons arise in this way, and uniqueness of \(t,j\) follows from the larger-middle-gap member.

Therefore there are exactly
\[
 \sum_{t=0}^{h-1}(t+1)=\frac{h(h+1)}2
\]
doubleton fibers. The number of input words is \(\binom{2h+2}{2}=(2h+1)(h+1)\), so subtracting two words per doubleton gives \((h+1)^2\) singleton fibers. Adding the two fiber counts gives \((h+1)(3h+2)/2\) distinct observations. The formula remains valid when \(h=0\). A maximal zero-error code consists of exactly one representative per fiber, proving the coding statement. The uniquely recoverable proportion is the singleton-word count divided by total word count.

## Verification

The independent Python program `VERIFY.py` computes both Parikh matrices from literal words and lexicographically minimal explicit rotations (not using the proof's formula to obtain those observations). It enumerates every weight-two binary word for zero counts \(0\) through \(60\), groups observations, and checks the claimed histogram and every explicit collision pair. It separately checks the formula (1) for each source word. Running `python VERIFY.py` produces `VERIFY_OK zero_counts=0..60 words=39711 direct_rotations=yes explicit_pairs=yes`. These finite checks support but do not replace the all-parameter proof above.

## Relationship to prior work

Dick, Hutchinson, Mercaş and Reidenbach introduced and analyzed combining a word's Parikh matrix with that of its Lyndon conjugate. Their LATA 2020 paper characterizes certain non-distinguishable ordinary Parikh-matrix classes; the displayed statements do not give the full two-marker joint-fiber partition or these exact parity-dependent counts. The associated 2021 journal article concerns the same ambiguity-reduction approach, but its full text was not available for complete comparison here. The 2022 toolkit paper documents implementation of Parikh-matrix variants and is not in itself an exact two-marker counting theorem. Ordinary Parikh-matrix unambiguity and substring-composition or contiguous-pair reconstruction use different observations, so results for those channels do not imply (1) or the claimed fiber spectrum without an additional reduction.

## Limitations

The result concerns only binary inputs with exactly two ones, and only the specified pair of observations. It does not characterize all binary Lyndon–Parikh fibers at arbitrary composition, establish optimal noisy-channel codes, or assert that the parity law is unknown under every possible alternative terminology. A 2021 full-text article from the same authors and specialized earlier work may contain related cases not recovered here. Independent expert validation has not been performed.

## References

1. J. Dick, L. K. Hutchinson, R. Mercaş, and D. Reidenbach, *Reducing the Ambiguity of Parikh Matrices*, LATA 2020, Lecture Notes in Computer Science 12038, 397–411. DOI: `10.1007/978-3-030-40608-0_28`; open text indexed at `https://pmc.ncbi.nlm.nih.gov/articles/PMC7206623/`.
2. J. Dick, L. K. Hutchinson, R. Mercaş, and D. Reidenbach, *Reducing the ambiguity of Parikh matrices*, Theoretical Computer Science 860 (2021), 23–40. DOI: `10.1016/j.tcs.2021.01.025`.
3. L. K. Hutchinson, R. Mercaş, and D. Reidenbach, *A Toolkit for Parikh Matrices*, CIAA 2022, Lecture Notes in Computer Science 13266, 116–127. DOI: `10.1007/978-3-031-07469-1_9`.
