# Fibonacci law for parity-balanced short signed-binary representations

## Finding

A *short binary signed-digit representation* of a positive integer \(n\) is an expression
\[
n=\sum_{j=0}^{L-1}\epsilon_j2^j,\quad \epsilon_j\in\{-1,0,1\},\quad\epsilon_{L-1}=1,
\]
whose leading two digits (if \(L\ge2\)) are not \((1,-1)\). Equivalently, the second-leading digit is \(0\) or \(1\). This is the shortness convention of Anders--Dawsey--Gupta--Vandehey [1]. Representations are counted as digit strings without leading zeroes. Let \(E(n)\) and \(O(n)\) count those containing, respectively, an even and an odd number of negative digits.

**Theorem.** For every \(n\ge1\), \(E(n)=O(n)\) precisely when the conventional binary expansion of \(n\) lies in the regular language
\[
\boxed{\quad 1(01^{*}0)^{*}10^{*}\quad}.
\]
Here \(^{*}\) means arbitrary finite repetition, including zero repetitions. For every \(r\ge2\), among the integers having exactly \(r\) binary digits there are precisely \(F_{r-1}\) with equal even and odd representation counts, where \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). Consequently, for every \(r\ge1\),
\[
\boxed{\#\{1\le n<2^r:E(n)=O(n)\}=F_{r+1}-1.}
\]
In particular, the parity-balanced integers have natural density zero. Their dyadic counting exponent is \(\log_2\bigl((1+\sqrt5)/2\bigr)\).

## Assumptions and scope

All integers and representations are finite. For \(n>0\), the leading digit must be \(1\): if it were \(-1\), even replacing every lower digit by \(1\) would give a negative total. The convention forbids the adjacent leading pair \((1,-1)\), not arbitrary occurrences of adjacent opposite nonzero digits below the leading position. The counts \(E(n)\), \(O(n)\) are finite under this convention. The empty set of repeated blocks in the displayed language is permitted.

## Proof

Put \(g(n)=E(n)-O(n)\). Direct enumeration yields \(g(1)=g(2)=1\). For \(m\ge1\), a representation of \(2m\) must end in digit \(0\); removing that digit is a sign-preserving bijection with short representations of \(m\). Thus
\[
g(2m)=g(m).
\]
For \(m\ge1\), a representation of \(2m+1\) ends in digit \(1\) or \(-1\). Removing it gives respectively a short representation of \(m\) or of \(m+1\); the latter case changes the parity of the negative-digit count. This gives
\[
g(2m+1)=g(m)-g(m+1).
\]
The only potentially forbidden concatenation to a one-digit representation is \(1,-1\), which would represent \(1\); it does not arise for \(2m+1\ge3\). These bijections are exhaustive and unique.

Define \(v(n)=(g(n),g(n+1))=(a,b)\). Combining the two recurrences gives
\[
v(2n)=(a,a-b),\qquad v(2n+1)=(a-b,b).
\]
Both transformations have determinant \(\pm1\), and \(v(1)=(1,1)\). In particular \(\gcd(|a|,|b|)=1\) for all \(n\ge1\). Track \(v(n)\) by its projective ratio \(a/b\), writing \(\infty\) if \(b=0\). Only four types can occur:
\[
P: a=b\ne0,\quad I:b=0,\quad Z:a=0,\quad X:ab<0\text{ or }(ab>0\text{ and }|a|<|b|).
\]
For \(X\), the ratio belongs to \((-\infty,0)\cup(0,1)\). Starting in state \(P\) at the initial leading binary digit \(1\), the above two transformations, applied in order to the remaining binary digits, give exactly this transition table:

| State | Append binary \(0\) | Append binary \(1\) |
| --- | --- | --- |
| \(P\) | \(I\) | \(Z\) |
| \(I\) | \(P\) | \(I\) |
| \(Z\) | \(Z\) | \(X\) |
| \(X\) | \(X\) | \(X\) |

Indeed, in state \(X\), the map \(a/b\mapsto (a/b)/((a/b)-1)\) sends negative ratios to \((0,1)\) and ratios in \((0,1)\) to negative ratios; the map \(a/b\mapsto (a/b)-1\) sends both classes to negative ratios. Hence \(X\) is absorbing. Since \(g(n)=0\) exactly in state \(Z\), a successful word starts at \(P\), makes any number of excursions \(P\xrightarrow{0}I\xrightarrow{1^{*}}I\xrightarrow{0}P\), next takes \(P\xrightarrow{1}Z\), and finally reads zero or more zeroes in \(Z\). This proves the regular-language characterization.

Let \(p_r,i_r,z_r\) count the ordinary binary words of exactly \(r\) digits ending in states \(P,I,Z\), respectively. Each word starts with a \(1\); hence \((p_1,i_1,z_1)=(1,0,0)\). The transition table implies
\[
p_{r+1}=i_r,\qquad i_{r+1}=p_r+i_r,\qquad z_{r+1}=p_r+z_r.
\]
Induction from \(r=2\) shows \(p_r=F_{r-2}\), \(i_r=F_{r-1}\), and \(z_r=F_{r-1}\) for \(r\ge2\). This gives exactly \(F_{r-1}\) balanced integers of binary length \(r\). Summing over lengths \(2,\ldots,r\), using \(\sum_{j=1}^{r-1}F_j=F_{r+1}-1\), proves the cumulative formula. Finally \(F_r=O(\varphi^r)\) with \(\varphi=(1+\sqrt5)/2<2\), so the balanced integers have density zero, and \(F_{r+1}=\Theta(\varphi^r)\) gives the stated exponent.

## Verification

The standalone standard-library script `verify.py` independently constructs every short signed-digit representation of each \(1\le n\le1024\) (29,525 such representations). Completeness holds because a short representation of length \(L\ge2\) has value at least \(2^{L-2}+1\), so length \(12\) cannot represent a positive integer at most \(1024\). The script classifies sign parity, and compares the resulting counts against the proven recurrences and the unweighted Stern recurrence. It also checks the binary-language criterion for every \(1\le n<2^{17}\), the exact Fibonacci counts for lengths \(1\le r\le17\), and the four-state transition classification across the same range. The unrestricted theorem is proved above; these finite checks are corroboration, not an infinite certificate. Run `python3 verify.py` from the package directory.

## Relationship to prior work

Anders, Dawsey, Gupta, and Vandehey [1] prove that the total number \(E(n)+O(n)\) of short signed-digit representations equals the Stern diatomic sequence and give bijective and generating-function proofs. Their result does not distinguish the parity of negative digits. The present theorem classifies exact cancellations between the two parity classes; it is neither a statement about the total count nor its direct numerical consequence. Monroe [2] studies fixed-length signed-digit representations and Stern-polynomial distributions by different statistics, primarily the number of zero digits. Classical twisted Stern recurrences [3] use different signs in the even and odd recursion and do not give this zero-language classification. The prime object is the specifically restricted short representation family, not all signed-digit expansions.

## Limitations

The exact formula applies to the shortness convention above and to the parity of the number of negative digits, not to unrestricted signed-digit expansions, non-adjacent forms, or fixed-length counts. Related unindexed sources may contain an equivalent formulation; no absolute novelty guarantee is claimed. The original 2023 preprint and 2024 journal article have the same motivating definition, but the latter's publication date is not used as the first public date.

## References

[1] K. Anders, M. L. Dawsey, R. Gupta, J. Vandehey, *Non-standard binary representations and the Stern sequence*, first public arXiv:2308.07448 (2023-08-14); *Electronic Journal of Combinatorics* 31 (2024), P4.39, DOI 10.37236/12312. https://arxiv.org/abs/2308.07448

[2] L. Monroe, *Binary Signed-Digit Integers and the Stern Polynomial*, arXiv:2108.12417 (2021). https://arxiv.org/abs/2108.12417

[3] J.-P. Allouche, *On the Stern sequence and its twisted version*, arXiv:1202.4171 (2012); recurrence also indexed as OEIS A213369. https://oeis.org/A213369
