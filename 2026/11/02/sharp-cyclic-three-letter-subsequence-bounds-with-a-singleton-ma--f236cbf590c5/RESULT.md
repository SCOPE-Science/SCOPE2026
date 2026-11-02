# Sharp cyclic three-letter subsequence bounds with a singleton marker

## Finding

For positive integers \(a,b\), let \(n=a+b+1\) and let \(W\) be a circular word over \(\{\mathtt a<\mathtt b<\mathtt c\}\), containing \(a\) copies of \(\mathtt a\), \(b\) copies of \(\mathtt b\), and exactly one copy of \(\mathtt c\). Let \(E(u)\) be the number of increasing triples of positions of a linear word \(u\) spelling \(\mathtt{abc}\), and define the rotation-sum invariant
\[
T(W)=\sum_{u\in\operatorname{Rot}(W)} E(u),
\]
where each distinct rotation appears once. The unique occurrence of \(\mathtt c\) guarantees that all \(n\) rotations are distinct. Accordingly, \(T(W)/n\) is precisely the upper-right entry of the averaged ternary circular Parikh matrix of \(W\).

Every such necklace has exactly one linear representative \(\mathtt c v\), with \(v\) binary and of content \((a,b)\). If the positions of \(\mathtt a\) in \(v\), in one-based indexing, are \(p_1<\cdots<p_a\), and \(t_r\) is the number of \(\mathtt b\)'s preceding its \(r\)-th \(\mathtt a\), then
\[
T(W)=\sum_{r=1}^{a}p_r(b-t_r)=\sum_{r=1}^{a}(r+t_r)(b-t_r).
\]
The sequence \(0\le t_1\le\cdots\le t_a\le b\) uniquely specifies \(v\).

The **exact maximum** and all its attaining necklaces are
\[
M_{a,b}=\max_W T(W)=\frac a2\max_{0\le t\le b\atop t\in\mathbb Z}(b-t)(2t+a+1),
\]
\[
T(W)=M_{a,b}\ \Longleftrightarrow\ W=[\mathtt c\,\mathtt b^{t}\mathtt a^{a}\mathtt b^{b-t}]
\quad\text{for an integer maximizing the displayed quadratic.}
\]
The maximizing integers are precisely the integer points of \([0,b]\) nearest to \((2b-a-1)/4\), after clipping to this interval. In particular the optimizer may split the \(\mathtt b\)'s into two blocks, despite all \(\mathtt a\)'s being consecutive.

There is also a **sharp positive spectral gap**:
\[
T(W)=0\quad\text{or}\quad T(W)\ge b.
\]
The zero value occurs only at \([\mathtt c\mathtt b^b\mathtt a^a]\). The smallest strictly positive value is exactly \(b\), and its entire attaining set consists of
\[
[\mathtt c\mathtt a\mathtt b^b\mathtt a^{a-1}],\qquad
[\mathtt c\mathtt b^{b-1}\mathtt a\mathtt b\mathtt a^{a-1}],
\]
which coincide when \(b=1\). Thus no value among \(1,\ldots,b-1\) occurs. No claim is made that all larger integers up to \(M_{a,b}\) occur.

## Assumptions and scope

Here the alphabet is labeled and ordered, the positive integers \(a,b\) are arbitrary, the marker \(\mathtt c\) appears **exactly once**, and the observations are position-distinct *scattered subsequences* of \(\mathtt{abc}\), not contiguous factors. A necklace means an orbit under cyclic rotation, not reversal. The invariant is the sum over rotations (integer-valued); the associated averaged circular Parikh-matrix coefficient divides it by \(n\). All powers such as \(\mathtt a^a\) denote repeated concatenation of letters. The upper/lower extrema concern necklaces with this exact composition.

## Proof

**Rotation reduction.** Put \(W=[\mathtt c v]\), and index the positions of \(v\) from one. A rotation beginning with \(\mathtt c\) has no \(\mathtt{abc}\) subsequence. A rotation beginning at position \(s\) of \(v\) has form \(v[s:]\mathtt c v[:s-1]\). Since its single \(\mathtt c\) must be the last selected letter, its \(\mathtt{abc}\) triples are precisely the \(\mathtt{ab}\) subsequences in the suffix \(v[s:]\). Summing over \(s\), each ordered \(\mathtt{ab}\) pair with its \(\mathtt a\) at position \(p\) contributes to exactly \(p\) suffixes. The \(r\)-th \(\mathtt a\) occurs at \(p_r=r+t_r\), and has \(b-t_r\) following \(\mathtt b\)'s. This establishes the formula for \(T(W)\).

**Maximum and equality.** Write \(c_0=(a+1)/2\). Expanding gives
\[
T(W)=bc_0a+\sum_{r=1}^{a}\bigl((b-r)t_r-t_r^2\bigr).
\]
Because both \((r)\) and \((t_r)\) are nondecreasing,
\[
a\sum_{r=1}^a rt_r-\Big(\sum_{r=1}^a r\Big)\Big(\sum_{r=1}^a t_r\Big)
=\sum_{1\le r<s\le a}(s-r)(t_s-t_r)\ge0.
\]
Consequently,
\[
T(W)\le abc_0+\sum_{r=1}^{a}\bigl((b-c_0)t_r-t_r^2\bigr)
\le abc_0+a\max_{0\le t\le b\atop t\in\mathbb Z}\bigl((b-c_0)t-t^2\bigr).
\]
The last expression is exactly \(M_{a,b}\). Equality in the first inequality forces all \(t_r\) to be equal when \(a\ge2\), because every summand in the displayed covariance identity is nonnegative, and the case \(a=1\) is automatic. Equality in the second requires that common integer \(t\) to maximize the quadratic. Conversely \(t_r=t\) is realized by \(v=\mathtt b^t\mathtt a^a\mathtt b^{b-t}\), and substituting it in the rotation formula attains the bound. Completing the square yields the nearest-integer description of the optimizers.

**Zero, least positive value, and equality.** The sum of the nonnegative \(\mathtt{ab}\)-pair contributions is zero exactly when \(v\) has no \(\mathtt{ab}\) pair, namely \(v=\mathtt b^b\mathtt a^a\). Otherwise let \(t\le b-1\) be the number of initial \(\mathtt b\)'s before the first \(\mathtt a\). That first \(\mathtt a\) contributes
\[
(t+1)(b-t)=b+t(b-t-1)\ge b.
\]
All later \(\mathtt a\)'s contribute nonnegatively, so \(T(W)\ge b\). Equality requires \(t=0\) or \(t=b-1\), and all later \(\mathtt a\)'s to occur after the last \(\mathtt b\). These conditions give precisely the two displayed necklaces; direct substitution verifies both have \(T=b\). This also handles \(a=1\), \(b=1\), and their shared boundary.

## Verification

A standalone pure-Python verifier, `verify.py`, independently counts the number of position-distinct \(\mathtt{abc}\) occurrences in each rotation, compares against the positional formula, and enumerates all compositions for \(1\le a,b\le7\). For each of the \(49\) parameter pairs it checks the maximum, the complete maximizing set, the unique zero, the least positive value, the exact least-positive attaining set, and the forbidden initial interval. The executed result was:

`VERIFY_OK profiles=49 circular_classes=12854 literal_rotations=170100 maxima_and_all_extremizers=True positive_gap=True`

Run with `python verify.py`. This is finite corroboration, not the proof of the universally quantified result; the preceding algebraic argument supplies that proof.

## Relationship to prior work

Poovanandran, Simpson and Teh (2021) introduce and analyze averaged circular Parikh matrices. Their Definition 4.1 and Theorem 4.2 directly ground the interpretation of \(T(W)/n\) as a matrix coefficient, and their Theorem 4.11 shows the very different binary setting in which the corresponding two-letter entry depends only on composition. Their sections on ternary equivalence provide rewriting rules, not the fixed-composition singleton-marker sharp extrema and positive gap proved here. The present statement is a specialized theorem about the first nonbinary case, not a claim to have introduced Parikh matrices or rotation-averaged subsequence counts. Searches of published research records and related literature did not reveal a statement implying these specific equality classifications; non-discovery is not a proof of novelty.

## Limitations

The result requires exactly one \(\mathtt c\), and no result is asserted for multiple copies of the marker, higher-order alphabets, or the full set of intermediate attainable positive values. A previously unnoticed formulation of the same extremal combinatorics could exist; independent scientific comparison remains outstanding. The exhaustive checks establish only the stated finite test range. Inferences about practical identification or coding capacity beyond this exact restricted observable are not made.

## References

- G. Poovanandran, J. Simpson and W. C. Teh, *Counting Subwords in Circular Words and Their Parikh Matrices*, arXiv:2110.14858, first publicly submitted 2021-10-28, https://arxiv.org/abs/2110.14858 . The publicly readable manuscript has Definition 4.1, Theorems 4.2 and 4.11, and Section 5 on ternary matrix equivalence.
- G. Poovanandran, J. Simpson and W. C. Teh, publicly readable author-uploaded manuscript (2021), https://www.researchgate.net/publication/355721154_Counting_Subwords_in_Circular_Words_and_Their_Parikh_Matrices_Accepted_by_Theoretical_Computer_Science_on_12_Dec_2023 .
