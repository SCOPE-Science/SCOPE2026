# Total occurrences of the subword \(1122\) in non-crossing partitions

## Finding

Let \(NC_n\) be the set of non-crossing partitions of \([n]=\{1,\ldots,n\}\), represented in canonical sequential form \(\pi=\pi_1\cdots\pi_n\): blocks are ordered by increasing minimum element and each entry records its block label. Define \(\operatorname{occ}_{1122}(\pi)\) to be the number of indices \(i\in\{1,\ldots,n-3\}\) such that

\[
\pi_i=\pi_{i+1}<\pi_{i+2}=\pi_{i+3}.
\]

For every integer \(n\ge4\), the total number of such contiguous, order-isomorphic occurrences across all non-crossing partitions is

\[
\sum_{\pi\in NC_n}\operatorname{occ}_{1122}(\pi)=\binom{2n-5}{n-4}.
\]

For \(n<4\), the total is zero. Since \(|NC_n|=\frac{1}{n+1}\binom{2n}{n}\), the mean number of occurrences in a uniformly random member of \(NC_n\) is

\[
\frac{n(n+1)(n-3)}{8(2n-1)(2n-3)}\sim\frac{n}{32}.
\]

## Assumptions and scope

A subword occurrence uses four consecutive entries, and its letters must be order-isomorphic to \(1122\); it is not a classical, nonconsecutive subsequence. The labels are those of the canonical sequential form. The result gives the first moment (the sum of occurrence counts), not the full distribution, variance, or a limit law.

## Proof

Let \(C(x)=\sum_{n\ge0}|NC_n|x^n\) be the Catalan generating function, so \(C=1+xC^2\). Call a non-crossing partition indecomposable if it cannot be split at a cut into a nonempty initial interval and a nonempty final interval with no block meeting both intervals. Every non-crossing partition is uniquely a sequence of indecomposable components. Their generating function is

\[
I(x)=\sum_{k\ge1}x^kC(x)^{k-1}=\frac{x}{1-xC(x)}=xC(x),
\]

and therefore the generating function for arbitrary component sequences is \(1/(1-I)=C\).

Write \(S_I(x)\) and \(E_I(x)\) for the generating functions of indecomposable components whose first two, respectively last two, entries are equal. In an indecomposable component, the block containing the first entry also contains the last entry. If that block has \(k\) entries, the \(k-1\) gaps between consecutive entries are arbitrary non-crossing partitions, possibly empty. Equality of the first two entries means the first gap is empty; equality of the last two means the last gap is empty. Hence

\[
S_I(x)=E_I(x)=\sum_{k\ge2}x^kC(x)^{k-2}=x^2C(x).
\]

For arbitrary non-crossing partitions, the first (or last) two entries are equal exactly when the first (or last) indecomposable component has that property. Thus both corresponding generating functions are

\[
S(x)=E(x)=C(x)S_I(x)=x^2C(x)^2.
\]

Let \(T(x)\) be the generating function whose coefficient of \(x^n\) is the total number of occurrences of \(1122\) over \(NC_n\), and let \(T_I(x)\) be the analogous total restricted to indecomposable components. In the gap decomposition of an indecomposable component with first block of size \(k\), an occurrence is either wholly inside one gap, or it uses two consecutive entries of the first block followed immediately by the first two equal entries of the next gap. The latter case requires a preceding empty gap. These are the only cross-gap occurrences with the required increasing block-label order: a first pair from a gap followed by a pair from the first block has the reverse order, and a pair straddling a block/gap boundary cannot have equal entries. Summing the two cases over \(k\) gives

\[
T_I(x)=\sum_{k\ge2}(k-1)x^kC^{k-2}T+\sum_{k\ge3}(k-2)x^kC^{k-3}S
=x^2C^2T+x^3C^2S
=x^2C^2T+x^5C^4.
\]

In a sequence of indecomposable components, an occurrence is internal to one component or straddles a component boundary. A boundary occurrence exists exactly when the left component ends with an equal pair and the right component begins with an equal pair. The arbitrary component sequences before and after the marked component(s) each contribute \(C\). Consequently,

\[
T=C^2T_I+C^2E_IS_I=x^2C^4T+x^5C^6+x^4C^4.
\]

Solving and cancelling the factor \(1+xC^2\) yields

\[
T(x)=\frac{x^4C(x)^4(1+xC(x)^2)}{1-x^2C(x)^4}
=\frac{x^4C(x)^4}{1-xC(x)^2}.
\]

For \(n\ge4\), put \(m=n-4\). The generalized Catalan coefficient formula \([x^r]C(x)^s=\frac{s}{2r+s}\binom{2r+s}{r}\) gives

\[
[x^m]\frac{C(x)^4}{1-xC(x)^2}
=\frac{1}{m+2}\sum_{r=0}^{m}(m-r+2)\binom{2m+4}{r}.
\]

To evaluate the sum, set \(A=\sum_{r=0}^{m}\binom{2m+3}{r}\) and \(B=\sum_{r=0}^{m-1}\binom{2m+3}{r}\), with \(B=0\) if \(m=0\). Pascal's identity gives \(\sum_{r=0}^{m}\binom{2m+4}{r}=A+B\), while \(\sum_{r=0}^{m}r\binom{2m+4}{r}=(2m+4)B\). The numerator of the preceding expression is therefore \((m+2)(A+B)-(2m+4)B=(m+2)(A-B)=(m+2)\binom{2m+3}{m}\). Dividing by \(m+2\) proves that the coefficient is \(\binom{2m+3}{m}=\binom{2n-5}{n-4}\). Finally, division by the Catalan number gives the stated mean.

## Verification

The generating-function argument proves the identity for every \(n\ge4\); the zero case for \(n<4\) follows because a four-entry subword cannot occur. The included standard-library script independently enumerates canonical non-crossing restricted-growth words through \(n=10\), checks the Catalan totals, and confirms the occurrence totals for those finite sizes. That enumeration is a sanity check, not the infinite proof.

## Relationship to prior work

Shattuck's study of repeated-letter subwords in non-crossing partitions gives generating functions for several infinite families and for every repeated-letter pattern of length three. Mansour and Shattuck treat several other families and all length-three patterns with distinct letters. The inspected family lists and tables do not include the length-four pattern \(1122\). The numerical sequence here is the known binomial sequence OEIS A002054 shifted by three; its appearance as a sequence is not claimed as new. The result established here is the occurrence-count interpretation for canonical non-crossing partitions and its exact mean.

## Limitations

No full generating function for the distribution of \(\operatorname{occ}_{1122}\), variance, asymptotic distribution, or explicit bijection to another Catalan statistic is proved. The coefficient sequence is known in other contexts, so novelty is limited to this statistic's exact interpretation under the literature checked; an unindexed prior treatment cannot be ruled out absolutely.

## References

1. M. Shattuck, “Enumeration of non-crossing partitions according to subwords with repeated letters,” arXiv:2303.06300v1 (first public 2023-03-11); published in *Applicable Analysis and Discrete Mathematics* 19 (2025), 1–20, DOI 10.2298/AADM211221017S.
2. T. Mansour and M. Shattuck, “Counting occurrences of subword patterns in non-crossing partitions,” *Art of Discrete and Applied Mathematics* 6(3) (2023), P3.03, DOI 10.26493/2590-9770.1552.b43.
3. OEIS Foundation Inc., OEIS A002054, “Binomial coefficient \(\binom{2n+1}{n-1}\),” consulted for the numerical sequence identity only.
