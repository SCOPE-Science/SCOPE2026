# Rational enumeration and entropy of locally irreducible reverse-complement length-two words

## Finding

Fix any even alphabet size \(q\ge2\) and a fixed-point-free involution \(a\mapsto\bar a\) of its symbols. Let \(I_q(n)\) count length-\(n\) words admitting **no inverse** of a reverse-complement duplication of a block of length two. In particular, these are precisely the words avoiding every contiguous factor \(ab\bar b\bar a\).

For all such \(q\), including the four-letter DNA alphabet,
\[
\boxed{\sum_{n\ge0}I_q(n)z^n =
\frac{1+z+2z^2+(q+1)z^3+qz^4+qz^5}
{1-(q-1)z-(q-2)z^2-(q-1)z^3}.}
\]
Thus \(I_q(0)=1\), \(I_q(1)=q\), \(I_q(2)=q^2\), \(I_q(3)=q^3\), \(I_q(4)=q^4-q^2\), and \(I_q(5)=q^5-2q^3+q\), while for every \(n\ge6\),
\[
I_q(n)=(q-1)I_q(n-1)+(q-2)I_q(n-2)+(q-1)I_q(n-3).
\]
Let \(\lambda_q\) be the unique positive root of
\[
\lambda_q^3-(q-1)\lambda_q^2-(q-2)\lambda_q-(q-1)=0.
\]
Then \(q-1<\lambda_q<q\), \(I_q(n)=\Theta_q(\lambda_q^n)\), and the language has exponential growth rate \(\log_q\lambda_q\) in base \(q\). For \(q=4\), its first values at lengths \(0\) to \(12\) are
\[
1,4,16,64,240,900,3372,12636,47352,177444,664944,2491776,9337548.
\]
Here \(\lambda_4=3.74734654030721\ldots\), giving growth rate \(0.95293469938397\ldots\).

## Assumptions and scope

The alphabet is a labeled finite set \(\Sigma\) of even cardinality \(q\); complementation has no fixed points and satisfies \(\overline{\bar a}=a\). A reverse-complement length-two duplication replaces a factor \(ab\) by \(ab\bar b\bar a\), leaving other positions unchanged. The phrase **locally irreducible** means that the resulting word admits no single inverse deletion, i.e. no factor of exactly this form, not that it belongs to an error-correcting code or is a unique representative of an arbitrary duplication-descendant class. The empty word is counted at length zero. No assumption on the particular pairing of alphabet symbols is necessary.

## Proof

**Local characterization.** An inverse move removes the final two symbols of a contiguous factor \(ab\bar b\bar a\), and no other inverse of the stipulated channel is possible. Thus admissible words are exactly the words avoiding the finite forbidden set
\[
\mathcal F=\{ab\bar b\bar a:a,b\in\Sigma\},\qquad |\mathcal F|=q^2.
\]
All forbidden words have length four and none contains another as a proper factor.

**Marked clusters.** Apply formal inclusion-exclusion to the occurrences of words in \(\mathcal F\). A cluster is a nonempty chain of marked forbidden occurrences whose consecutive occurrence intervals overlap and whose union is one interval. Each marked occurrence receives weight \(-1\). A chain begins with a forbidden four-letter word, then each successive marked occurrence begins either one, two, or three positions later. Partition a forbidden pattern \(ab\bar b\bar a\) into type \(A\) if \(b=\bar a\), and type \(B\) otherwise. There are \(q\) and \(q(q-1)\) starting patterns respectively.

A shift by one permits a continuation only from type \(A\), and it has exactly one type-\(A\) successor. A shift by two permits exactly one continuation of the same type. A shift by three permits \(q\) successors, exactly one of type \(A\) and \(q-1\) of type \(B\), from either starting type. These statements follow by equating the overlapping suffix of \(ab\bar b\bar a\) to the prefix of \(cd\bar d\bar c\), for overlaps of lengths three, two, and one, respectively. This enumerates all possible overlapping marked words; no longer jumps are clusters.

Let \(A(z)\) and \(B(z)\) be the signed generating functions for successive continuations after an already fixed marked type-\(A\) or type-\(B\) word, with an empty continuation having weight one. Overlap lengths give the equations
\[
\begin{aligned}
A(z)&=1-zA(z)-z^2A(z)-z^3[A(z)+(q-1)B(z)],\\
B(z)&=1-z^2B(z)-z^3[A(z)+(q-1)B(z)].
\end{aligned}
\]
Writing \(J(z)=1+z+2z^2+(q+1)z^3+qz^4+qz^5\), elementary elimination gives
\[
A(z)=\frac{1+z^2}{J(z)},\qquad
B(z)=\frac{1+z+z^2}{J(z)}.
\]
The entire signed cluster series, including the first marked word and its four letters, is therefore
\[
C(z)=-qz^4\bigl[A(z)+(q-1)B(z)\bigr]
=-\frac{qz^4[q+(q-1)z+qz^2]}{J(z)}.
\]

**From clusters to avoiding words.** In the standard first-atom decomposition of a word with any set of marked forbidden occurrences, the first atom is either a free letter (weight \(qz\)) or one complete marked cluster (weight \(C(z)\)). Thus the signed generating function for marked words is \(1/(1-qz-C(z))\). Summing each word over all subsets of occurrences gives \((1-1)^k\), equal to one exactly when the word has zero forbidden occurrences and zero otherwise. Hence
\[
\sum_{n\ge0}I_q(n)z^n=\frac1{1-qz-C(z)}
=\frac{J(z)}{1-(q-1)z-(q-2)z^2-(q-1)z^3}.
\]
Coefficient extraction proves the stated initial values and homogeneous recurrence from \(n\ge6\). The calculation takes place in formal power series, so no analytic convergence is assumed during the enumeration.

**Asymptotic growth.** The recurrence has companion matrix
\[
M_q=\begin{pmatrix}q-1&q-2&q-1\\1&0&0\\0&1&0\end{pmatrix}.
\]
For every even \(q\ge2\), this matrix is nonnegative, irreducible, and primitive: its directed graph is strongly connected and has a self-loop (including at \(q=2\)). Its Perron eigenvalue is a simple positive root of the characteristic cubic and strictly exceeds the magnitudes of its other roots. Evaluating this cubic at \(q-1\) and \(q\) gives respectively \(-(q-1)^2\) and \(q+1\), so \(q-1<\lambda_q<q\). The positive initial recurrence vector has a positive Perron projection, proving \(I_q(n)=\Theta_q(\lambda_q^n)\) and the claimed entropy.

## Verification

The standalone `VERIFY.py` implements three independent finite checks: (i) the displayed rational-function coefficient recurrence; (ii) a direct length-three-state dynamic program that admits an appended letter precisely when no forbidden four-letter factor appears; and (iii) literal enumeration of every word for bounded parameters. It compares methods for alphabets of sizes \(2,4,6,8\), direct enumeration through lengths \(16,8,6,5\) respectively, and the state dynamic program through length \(35\). It additionally checks that complementing alternating positions maps forbidden reverse-complement four-factors bijectively to ordinary palindromic four-factors.

The proof is valid for **all even** \(q\) and **all** \(n\ge0\). The finite computations corroborate the algebra and are not substituted for the proof.

## Relationship to prior work

Ben-Tolila and Schwartz, *On the Reverse-Complement String-Duplication System*, arXiv:2112.11811 (public 22 December 2021), define the underlying mutation channel and analyze expressiveness and the binary length-two special case. This result counts all locally irreducible words for **every even alphabet size**, including the four-letter DNA case, and gives their rational generating function and exact entropy.

Yohananov and Schwartz, arXiv:2312.00394 (public 1 December 2023), prove **zero capacity for codes correcting arbitrarily many** reverse-complement duplications of length at least two. This theorem is not contradicted: a set of locally irreducible words is not, in general, an unbounded-error-correcting code. The separate problem of enumerating irreducible roots can have a positive language growth rate despite zero duplication-correction coding capacity.

There is an elementary alias: complementing the symbols in every other position turns the excluded factors \(ab\bar b\bar a\) into ordinary palindromes of length four. Equivalence to the **four-palindrome-avoiding word count** was included in overlap searches. The recent 2026 arXiv:2609.00779 abstract reports an even-block reverse-complement/palindromic coding-channel conjugacy, not this exact counting formula; its full paper was not inspected, and it is recorded as a residual originality risk.

## Limitations

This is a local forbidden-factor enumeration, not a classification of global descendant cones, a uniqueness-of-reduction theorem, or a duplication-error-correcting code construction. No result about higher duplication lengths, insertion mixtures, or alphabets with fixed points of complementation is asserted. Full-text coverage of arXiv:2609.00779 and potential unindexed palindrome-avoidance enumeration remain originality risks; absence of a database match is not a proof of novelty. The result has not undergone independent expert review.

## References

1. E. Ben-Tolila and M. Schwartz, *On the Reverse-Complement String-Duplication System*, arXiv:2112.11811v1 (22 December 2021), https://arxiv.org/abs/2112.11811.
2. L. Yohananov and M. Schwartz, *On the Coding Capacity of Reverse-Complement and Palindromic Duplication-Correcting Codes*, arXiv:2312.00394v1 (1 December 2023), https://arxiv.org/abs/2312.00394.
3. A. L. Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779 (1 September 2026), https://arxiv.org/abs/2609.00779; abstract comparison only.
