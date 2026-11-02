# Parity threshold and complete ambiguity spectrum for pooled one-marker longest reads

## Finding

Consider a multiset of \(k\) binary words of length \(n\ge2\), each of Hamming weight exactly one. Its observed \((n-1)\)-profile is the unlabeled multiset of both length-\((n-1)\) contiguous substrings of every source word, with multiplicities retained. Two source multisets are indistinguishable exactly when they have the same observed profile.

**Theorem (exact fibers and zero-error capacity).** Let \(k\ge0\) and set \(B_n(t)=\binom{t+n-1}{n-1}\) for integer \(t\ge0\), with \(B_n(t)=0\) for \(t<0\). There are \(B_n(k)\) possible source multisets.

* For **odd** \(n\), every source multiset is uniquely determined by the profile. There are \(B_n(k)\) profiles, all of fiber size one.
* For **even** \(n=2m\), the number \(H_{n,k}(s)\) of distinct profiles having **exactly \(s\)** source multisets is, for every integer \(s\ge1\),

\[
H_{n,k}(s)=B_n\bigl(k-m(s-1)\bigr)-2B_n(k-ms)+B_n\bigl(k-m(s+1)\bigr).
\]

In particular, the exact number of profiles is

\[
R_{n,k}=B_n(k)-B_n(k-m),
\]

and the largest ambiguity fiber has size \(1+\lfloor k/m\rfloor\). Thus the entire source space is uniquely reconstructible for \(k<m\), whereas ambiguity first appears at \(k=m\), where **exactly one** profile has two sources and all others are singletons. For fixed even \(n\) and \(k\to\infty\),

\[
R_{n,k}\sim\frac{m\,k^{n-2}}{(n-2)!},\qquad
\frac{R_{n,k}}{B_n(k)}\sim\frac{m(n-1)}{k}.
\]

For example, with \(n=4\) and \(k=4\), there are 35 possible source multisets but only 25 observed profiles: 16 have a single source, eight have two sources, and one has three.

The number \(R_{n,k}\) (or \(B_n(k)\) for odd \(n\)) is also the **maximum cardinality of a zero-error one-profile reconstruction code** chosen among all these source multisets, since one may choose exactly one representative of each fiber.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). The strand length \(n\ge2\) and multiset size \(k\ge0\) are known. Strands may repeat. Reads retain their literal left-to-right symbol order, but neither the originating strand nor whether a read was a prefix or suffix is revealed. All reads are present without errors; the profile is a multiset (not merely a set). The read length is exactly \(n-1\), the longest proper substring length. Source multisets are **not** identified under reversal. No claims are made for arbitrary strand weights, shorter reads, unordered read compositions, or missing or noisy reads.

## Proof

**1. Exact observation map.** For \(i\in\{1,\ldots,n\}\), let \(x_i\) denote the number of source strands whose unique one lies in position \(i\). Then \(x_i\in\mathbb Z_{\ge0}\) and \(\sum_{i=1}^{n}x_i=k\). The \(n\) possible strand types correspond bijectively to these vectors. Each weight-one read of length \(n-1\), with its one in position \(j\in\{1,\ldots,n-1\}\), occurs with multiplicity

\[
y_j=x_j+x_{j+1}.
\]

Indeed, this read arises from the prefix of a source with its one at \(j\), or from the suffix of a source with its one at \(j+1\). The remaining reads are the all-zero word, with multiplicity \(2k-\sum_{j=1}^{n-1}y_j\). Therefore, with \(k\) fixed, the entire observed profile is equivalent to the vector \((y_1,\ldots,y_{n-1})\).

**2. Every collision and its parity.** If two vectors \(x\) and \(x'\) have the same profile, their difference \(z_i=x'_i-x_i\) satisfies \(z_i+z_{i+1}=0\). Thus for some integer \(t\),

\[
z_i=(-1)^{i-1}t\qquad(1\le i\le n).
\]

For odd \(n\), equality of strand counts forces \(0=\sum_i z_i=t\), so no collision is possible. Equivalently, when \(n\) is odd, \(x_n=k-\sum_{j\ \mathrm{odd}}y_j\), and then every preceding coordinate is uniquely recovered backwards from the adjacent-sum equations.

For even \(n=2m\), the alternating vector sums to zero, and every integer \(t\) preserving nonnegativity gives another source multiset with the same profile. Its precise admissible range is

\[
-\min_{i\ \mathrm{odd}}x_i\ \le t\ \le\min_{i\ \mathrm{even}}x_i.
\]

Consequently the fiber of \(x\) has exactly \(1+\min_{i\ \mathrm{odd}}x_i+\min_{i\ \mathrm{even}}x_i\) members, independently of the chosen member \(x\).

**3. Canonical representatives and all fiber counts.** Every even-length fiber has a unique representative \(x\) with \(\min_{i\ \mathrm{odd}}x_i=0\): subtract that minimum from all odd coordinates and add it to all even coordinates. This is the unique alternating translate with minimum odd coordinate zero. For this representative, the fiber size is \(1+\min_{i\ \mathrm{even}}x_i\).

Let \(T_s\) be the number of fibers of size at least \(s\). A canonical representative counted by \(T_s\) has every even coordinate at least \(s-1\), while at least one odd coordinate is zero. Subtracting \(s-1\) from the \(m\) even coordinates gives \(B_n(k-m(s-1))\) nonnegative vectors. Among them, exactly \(B_n(k-ms)\) have every odd coordinate positive. Thus

\[
T_s=B_n\bigl(k-m(s-1)\bigr)-B_n(k-ms).
\]

The required exact-fiber count is \(H_{n,k}(s)=T_s-T_{s+1}\). Taking \(s=1\) yields the total number \(R_{n,k}=T_1\) of fibers. These formulas include \(k=0\) and \(n=2\), using the stated zero convention.

**4. Sharp largest fiber, first ambiguity, and code size.** A fiber of size at least \(s\) has a canonical representative with at least \(s-1\) ones in each of its \(m\) even coordinates; hence \(k\ge m(s-1)\). Conversely, whenever \(k\ge m(s-1)\), take a canonical vector whose odd coordinates are zero and whose even coordinates are all at least \(s-1\), distributing any remaining units arbitrarily. Its fiber has size at least \(s\). Therefore the maximum fiber size is \(1+\lfloor k/m\rfloor\). At \(k=m\) exactly one canonical representative has all even coordinates one and all odd coordinates zero while having fiber size two; all other profiles remain singletons. Because two source multisets in a common fiber are confusable and different fibers are distinguishable, selecting one representative of each fiber yields the largest zero-error code, proving the capacity statement.

**5. Asymptotics.** The binomial polynomial \(B_n(k)\) has degree \(n-1\) with leading coefficient \(1/(n-1)!\). Its finite difference with step \(m\) therefore has degree \(n-2\) and leading coefficient \(m/(n-2)!\), giving both displayed asymptotic formulas.

## Verification

The included standalone `verify.py` constructs literal binary strands, forms all actual length-\((n-1)\) prefix and suffix strings, pools them with multiplicity, and independently groups source multisets by equal observation. It checks the complete predicted histogram, the exact number of sources, and maximum fiber size, for every \(2\le n\le10\) and \(0\le k\le6\). This comprises 63 parameter pairs and 19,440 source multisets. Run `python3 verify.py`; the observed success output is:

```
VERIFY_OK parameter_pairs=63 source_multisets=19440 distinct_profiles_accumulated=19209 method=literal_nminus1_factor_multisets
```

This finite test confirms the formulas within its exhaustively checked ranges. The proof above, not finite enumeration, establishes the result for arbitrary \(n\) and \(k\).

## Relationship to prior work

Yehezkeally, Marcovich and Yaakobi introduced reconstruction from pooled substring multispectra for multiple strands, and derived general rate bounds and repeat-free constructions [1]. The present result takes their observation model at the longest proper read length and obtains a complete **constant-weight-one**, finite-parameter collision and code-capacity census. Their general asymptotic results neither give this explicit fiber distribution nor imply the sharp parity threshold by a stated specialization. The generalized multi-strand trace study [2] and the random-source reconstruction study [3] concern distinct rate/noise/read-length regimes. Work on prefix-suffix **compositions** [4,5] discards read order and typically uses many read lengths; its reconstruction equivalence, including reversal, differs from the literal fixed-length read multispectrum here. Gabrys and Milenkovic [6] focus on single-strand coded reconstruction. A direct equivalent earlier result could exist under graph-incidence or integer-fiber terminology and remains a literature risk.

## Limitations

This is a noiseless, multiplicity-preserving, fixed-length read result for source strands with exactly one nonzero marker. The general multi-strand problem and length-\((n-2)\) or shorter reads are not solved. The zero-error code capacity counts source **multisets**, not labeled source tuples. Reversal is **not** an equivalence; if read orientations were erased, the formulas would need new analysis. Computational checks are finite; the infinite claims rely on the proof.

## References

1. Y. Yehezkeally, S. Marcovich, E. Yaakobi, *Multi-strand Reconstruction from Substrings*, arXiv:2108.11725, first public August 26, 2021. https://arxiv.org/abs/2108.11725
2. Y. Yehezkeally, D. Bar-Lev, S. Marcovich, E. Yaakobi, *Generalized Unique Reconstruction from Substrings*, arXiv:2210.04471, first public October 10, 2022. https://arxiv.org/abs/2210.04471
3. K. Levick, I. Shomorony, *Fundamental Limits of Multiple Sequence Reconstruction from Substrings*, arXiv:2305.05820, first public May 10, 2023. https://arxiv.org/abs/2305.05820
4. R. Gabrys, S. Pattabiraman, O. Milenkovic, *Reconstruction of Sets of Strings from Prefix/Suffix Compositions*, arXiv:2110.02352, first public October 5, 2021. https://arxiv.org/abs/2110.02352
5. Y. Yang, Z. Chen, *Reconstruction of Multiple Strings of Constant Weight from Prefix–Suffix Compositions*, arXiv:2411.03776, first public November 6, 2024. https://arxiv.org/abs/2411.03776
6. R. Gabrys, O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548, first public April 12, 2018. https://arxiv.org/abs/1804.04548
