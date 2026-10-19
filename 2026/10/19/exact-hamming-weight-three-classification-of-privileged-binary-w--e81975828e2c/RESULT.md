# Exact Hamming-weight-three classification of privileged binary words

## Finding

Let \(P_3(n)\) be the number of length-\(n\) binary words with exactly three occurrences of \(1\) that are **privileged**, meaning that words of length at most one are privileged and every longer privileged word is a complete return to a shorter privileged word. A *complete return* begins and ends with the shorter word and has exactly two occurrences of it, including overlapping occurrences.

**Classification.** For every \(n\geq 0\), the privileged words of Hamming weight three are exactly the disjoint union of the following two families:

1. The palindromes
   \[
   0^a1\,0^b1\,0^b1\,0^a,\qquad a,b\in\mathbb Z_{\geq0}.
   \]
2. The nonpalindromes
   \[
   0^a1\,0^b1\,0^c1\,0^a,\qquad a\in\mathbb Z_{\geq1},\quad 0\leq b,c<a,\quad b\neq c.
   \]

For the respective counting sequences \(P_3^{\mathrm{pal}}(n)\) and \(P_3^{\mathrm{nonpal}}(n)\), their generating functions are
\[
\begin{aligned}
\sum_{n\geq0}P_3^{\mathrm{pal}}(n)z^n&=\frac{z^3}{(1-z^2)^2},\\
\sum_{n\geq0}P_3^{\mathrm{nonpal}}(n)z^n&=\frac{2z^8}{(1-z^2)(1-z^3)(1-z^4)},\\
\sum_{n\geq0}P_3(n)z^n&=\frac{z^3(1+z^2-z^3+z^5)}{(1-z^2)(1-z^3)(1-z^4)}.
\end{aligned}
\]
In particular, \(P_3(n)\) is a quasipolynomial in \(n\) of **minimal period twelve**, and
\[
P_3(n)=\frac{n^2}{24}+O(n),\qquad
P_3^{\mathrm{nonpal}}(n)=\frac{n^2}{24}+O(n).
\]
Consequently, as \(n\to\infty\), a uniformly chosen privileged binary word of length \(n\) with exactly three ones is nonpalindromic with probability tending to \(1\). All privileged binary words with at most two ones are palindromes. This identifies weight three as the first nonpalindromic sparse stratum and determines its complete length distribution.

## Assumptions and scope

The alphabet is exactly the labeled binary alphabet \(\{0,1\}\), and Hamming weight always counts ones. The empty word is privileged; words of length one are privileged. A border is nonempty and proper. Overlapping occurrences count separately at their starting positions. A word in a displayed family is counted once; the two families are disjoint. The formulas hold for **all** nonnegative integer lengths, with zero count below length three. They count distinct words, not equivalence classes under reversal or complementation.

## Proof

First observe that a proper common prefix-suffix border of a word containing exactly \(k>0\) ones cannot contain all \(k\) ones: if it did, the first one of the word would have identical relative position in both the initial and final occurrences, forcing those occurrences to begin at the same position. Thus a privileged proper border has strictly fewer ones.

We need two elementary sparse-border facts. Among words with exactly one one, the privileged words are \(1\) and \(0^t1\,0^t\), where \(t\geq1\). Indeed, a longer privileged word must begin and end with zeros, and its privileged border must be a run of zeros; that run occurs exactly twice only when the two outer zero runs are equal in length. Conversely, that common run does give a complete return.

Among words with exactly two ones, every privileged word is a palindrome, and the precise forms are \(1\,0^s1\) for \(s\geq0\), and \(0^t1\,0^s1\,0^t\) for \(t\geq1,s\geq0\). For a word beginning and ending in zero, a possible privileged border has zero or one one. A zero-only complete-return border forces equal outer zero-run lengths; a one-one privileged border has the form \(0^r1\,0^r\) and again forces equal outer zero-run lengths. Conversely, if the outer runs have common length \(t\), then the word is closed by \(0^t\) when \(s<t\), or by \(0^t1\,0^t\) when \(s\geq t\). For a word beginning and ending in one, the only possible two-one form is \(1\,0^s1\), closed by \(1\). This proves the two-one fact.

Now let a privileged word have exactly three ones. If it begins and ends with \(1\), it has form \(1\,0^b1\,0^c1\). A privileged border cannot have three ones, and the border \(1\) has three occurrences. Thus the border must contain exactly two ones. It is simultaneously the first-two-one prefix and the last-two-one suffix, which requires \(b=c\). Conversely, \(1\,0^b1\,0^b1\) is closed by the privileged border \(1\,0^b1\).

Otherwise a privileged word starts and ends with zero and has the unique gap form
\[
w=0^a1\,0^b1\,0^c1\,0^d,\qquad a,d\geq1,\quad b,c\geq0.
\]
Its privileged complete-return border contains zero, one, or two ones. If it contains no ones, the border is a zero run \(0^r\). Its occurrence count is two only if \(a=d=r\) and \(b,c<a\); otherwise one of the outer runs contains extra occurrences or an internal run contains an occurrence. This gives the second displayed family when \(b\neq c\), as well as the portion of the first family when \(b=c<a\).

If the border contains one one, the preceding one-one classification makes it \(0^r1\,0^r\). The prefix and suffix occurrences force \(a=d=r\), \(b\geq r\), and \(c\geq r\). But then the middle one also supplies an occurrence, contradicting the complete-return property. Thus this case is impossible.

If the border contains two ones, the preceding two-one classification forces it to be \(0^r1\,0^s1\,0^r\). Prefix-suffix equality then forces \(a=d=r\) and \(b=c=s\geq r\). Conversely, with \(a=d\geq1\) and \(b=c\geq a\), the two-one word \(0^a1\,0^b1\,0^a\) is privileged and occurs exactly twice in \(w\), once on each consecutive pair of ones. Combining this case with the zero-only case and the words beginning and ending in one gives precisely all the palindromes \(0^a1\,0^b1\,0^b1\,0^a\) for \(a,b\geq0\), plus precisely the stated nonpalindromic family. This also proves that no other words qualify.

The palindrome of parameters \((a,b)\) has length \(2a+2b+3\). Summing its weights gives \(z^3/(1-z^2)^2\). For the nonpalindromic family, reversal pairs \(b<c\) with \(b>c\). In the first orientation, uniquely write
\[
b=j,\qquad c=j+h+1,\qquad a=j+h+v+2,
\quad j,h,v\geq0.
\]
The word length becomes \(8+4j+3h+2v\), so the two orientations give
\[
\frac{2z^8}{(1-z^4)(1-z^3)(1-z^2)}.
\]
Adding the two fractions and simplifying yields the complete generating function.

Its denominator factors into \((1-z^2)(1-z^3)(1-z^4)\), so its coefficients are quasipolynomial in \(n\) with period dividing twelve. The numerator is nonzero at primitive third and primitive fourth roots of unity (substitution gives nonzero values), so its **minimal eventual period** is divisible by three and four and hence is twelve. The only pole of order three occurs at \(z=1\), and the leading singular term there is \(\frac{1}{12}(1-z)^{-3}\). Therefore the coefficients are \(n^2/24+O(n)\). The nonpalindromic fraction has that same principal term, whereas the palindromic coefficient is \((n-1)/2\) at odd \(n\geq3\) and zero at even \(n\). The claimed limiting fraction follows.

## Verification

The accompanying standalone Python 3 script `verify_sparse_privileged.py` computes the privileged predicate directly by its recursive complete-return definition; it independently identifies the two families from the locations of the three ones, checks every binary word with exactly three ones at each length \(3\leq n\leq37\), and checks rational-function coefficients through \(n=256\). It uses only the standard library and can be run with `python3 verify_sparse_privileged.py`. The expected output contains three `PASS` lines. Those finite checks are corroboration; the proof above establishes the statements for all \(n\).

## Relationship to prior work

Gabrić's study of closed and privileged words (arXiv:2206.14273, first public posting June 28, 2022) derives bounds for their unconditioned counts over finite alphabets. Schaeffer and Shallit (DOI:10.37236/5752, especially Theorem 8) give a first-order logical characterization of privileged words and study their occurrences within automatic infinite words. That general characterization is stronger than the decision question for an individual word and is acknowledged as such; it does not furnish the explicit weight-three disjoint gap classification, three simple generating functions, or nonpalindromic-density law stated here. OEIS A231208 tabulates total binary privileged-word counts and A235609 lists examples, including the familiar first nonpalindromic example. Their examples and generic enumeration procedures are not claimed as new. The contribution here is the exact sparse-stratum structure and its consequences, not privileged-word decidability or general rationality consequences of Presburger logic.

## Limitations

This is a theorem only for words containing exactly three ones. It does not enumerate all privileged words of a given length, nor provide analogous formulas for arbitrary Hamming weight. General techniques might computationally recover the formulas, so priority over all possible unpublished or unindexed analyses is not independently established. No empirical finite check constitutes proof of an infinite assertion; the infinite proof is given above. No independent audit has been performed.

## References

- Daniel Gabrić, *Asymptotic bounds for the number of closed and privileged words*, arXiv:2206.14273 (first posted 2022-06-28), and *Electronic Journal of Combinatorics* 31(2), P2.45 (2024).
- Luke Schaeffer and Jeffrey Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences*, *Electronic Journal of Combinatorics* 23(1), P1.25 (2016), DOI:10.37236/5752.
- Michael Forsyth, Amlesh Jayakumar, Jarkko Peltomäki, and Jeffrey Shallit, *Remarks on Privileged Words*, *International Journal of Foundations of Computer Science* 27(4), 431–442 (2016), DOI:10.1142/S0129054116500088.
- OEIS A231208, *Number of binary privileged words of length n*, and OEIS A235609, *List of privileged words over a two-letter alphabet*.
