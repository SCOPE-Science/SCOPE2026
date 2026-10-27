# Four-run exclusion from the binary palindrome-pair extremal bound

## Finding

For a finite binary word \(w\), let \(P(w)\) be the number of **distinct** contiguous factors (including the empty factor) that are each concatenations of at most two palindromes. For every choice of positive integers \(a,b,c,d\), write \(w=0^a1^b0^c1^d\) and \(n=a+b+c+d\). Then

\[
\begin{aligned}
P(w)={}&1+\max(a,c)+\max(b,d)+ab+bc+cd+ac+bd\\
&-\min(a,c)\min(b,d)+d\mathbf1_{c\le a}+a\mathbf1_{b\le d}-\mathbf1_{c\le a,\,b\le d}.
\end{aligned}
\]

**More importantly, every binary word with exactly four nonempty runs satisfies**

\[
P(w)<L(n):=\left\lceil\frac{n^2+2n+3}{3}\right\rceil\quad(n\ge4).
\]

For every \(n\ge4\), an explicit binary word with three runs has exactly \(L(n)\) such factors. Consequently, no exactly-four-run binary word maximizes the number of distinct palindrome-pair factors among all binary words of its length. The claim does **not** assert that \(L(n)\) is the unrestricted maximum.

## Assumptions and scope

A palindrome equals its reversal; the empty word is a palindrome. A palindrome pair is a concatenation of two palindromes, allowing an empty component. Each distinct factor is counted once even if it occurs several times or admits several decompositions. A run is a maximal nonempty block of equal letters. Complementation allows us to write any exactly-four-run binary word in the displayed form. All parameters \(a,b,c,d\) are positive integers; the result does not cover words with five or more runs.

## Proof

**Exact factor inventory.** The empty factor contributes one. One-run factors contribute \(\max(a,c)+\max(b,d)\). The \(01\) factors lie in two rectangles of run-length pairs, with sizes \(ab\) and \(cd\) and intersection \(\min(a,c)\min(b,d)\). The \(10\) factors contribute \(bc\). Three-run factors have shapes \(0^i1^b0^j\) or \(1^i0^c1^j\), contributing \(ac+bd\) distinct words. All factors with at most three runs are palindrome pairs: a three-run word splits into a palindrome comprising the middle run and equally many symbols from the two outside runs, plus any residual constant run.

Every four-run factor is uniquely of the form \(0^i1^b0^c1^j\), with \(1\le i\le a\) and \(1\le j\le d\). Such a factor is a palindrome pair **if and only if** \(i=c\) or \(j=b\). For necessity, the first palindromic component begins with zero and therefore ends with zero unless it is contained in the initial zero run; in the latter case it must be the entire initial run, and the remainder \(1^b0^c1^j\) is palindromic only for \(b=j\). In the former case the first component must end in the third run with matching outer zero-run lengths \(i\), and the remaining suffix can be palindromic only when the third run is exhausted, giving \(i=c\). Sufficiency follows from the decompositions \((0^c1^b0^c)(1^j)\) and \((0^i)(1^b0^c1^b)\), respectively. Hence four-run palindrome pairs number \(d\mathbf1_{c\le a}+a\mathbf1_{b\le d}-\mathbf1_{c\le a,\,b\le d}\), proving the formula.

**Universal four-run exclusion.** Write \(X(n)=(n^2+2n)/3\). Because \(L(n)=\lceil X(n)\rceil+1\), it suffices to prove \(P(w)\le X(n)\). There are four regions of the parameter space:

1. If \(c\le a\) and \(b\le d\), direct simplification gives \(P(w)=(a+d)(b+c+2)\le(n+2)^2/4\le X(n)\) for \(n\ge6\).

2. If \(c>a\) and \(b>d\), put \(s=b+c\), \(t=a+d\), so \(s+t=n\). The factor formula becomes \(P(w)=1+s+st+bc-ad\). Since \(bc\le s^2/4\) and \(ad\ge t-1\), completion of the square gives
\[
P(w)\le2-n+(n+2)s-\tfrac34s^2\le \frac{n^2+n+10}{3}\le X(n)\qquad(n\ge10).
\]

3. If \(c\le a\) and \(b>d\), set \(t=a+c\), \(s=b+d\), so \(s+t=n\). Substitution yields
\[
P(w)=1+n+st+c(t-1-c)+d(s-t-d).
\]
If \(s\le t\), the bounds \(c(t-1-c)\le(t-1)^2/4\) and \(d(s-t-d)\le s-t-1\) (since \(d\ge1\)) give
\[
P(w)\le2n+\tfrac14+(n-\tfrac52)t-\tfrac34t^2\le \frac{n^2+n+7}{3}\le X(n)\qquad(n\ge7).
\]
If \(s>t\), the bounds \(c(t-1-c)\le(t-1)^2/4\) and \(d(s-t-d)\le(s-t)^2/4\), with \(t<n/2\), give
\[
P(w)\le1+n+\frac{n^2+(t-1)^2}{4}\le\frac{5n^2}{16}+\frac{3n}{4}+\frac54\le X(n)\qquad(n\ge10).
\]

4. The remaining region \(c>a,\ b\le d\) is transformed into region 3 by reversing the word and complementing its bits, which preserve \(P\) and the length.

Thus the strict inequality holds for all \(n\ge10\). For \(4\le n\le9\), the four-run formula is exhausted over all positive quadruples of sum \(n\); the maxima are respectively \(8,12,16,21,27,33\), whereas \(L(n)\) is respectively \(9,13,17,22,28,34\). All \(\binom{n-1}{3}\) quadruples are covered at each length, independently corroborated by directly constructing and testing all factors. The embedded checker implements both counts.

**Three-run witnesses.** If \(n=3k\), take \(0^k1^k0^k\); if \(n=3k+1\), take \(0^k1^{k+1}0^k\); if \(n=3k+2\), take \(0^{k+1}1^{k+1}0^k\). Here \(k\ge1\) whenever \(n\ge4\). Every factor is a palindrome pair, and direct enumeration of distinct factors of \(0^x1^y0^z\) gives \(1+\max(x,z)+y+xy+yz+xz\). Substitution yields \(L(n)\) in each congruence class. Therefore the three-run witness strictly exceeds every four-run word of the same length.

## Verification

Run `python3 checker.py` with Python 3. The checker independently creates each word, enumerates all of its distinct factors, and tests palindrome-pair status by every split. It confirms the exact formula and strict inequality for all \(715\) positive quadruples of total length \(4\) through \(13\), including the \(126\) cases used for the finite portion of the proof; it also tests the three-run witnesses through length \(13\). The all-length inequalities above are algebraic proofs and do not rely on finite experiments.

## Relationship to prior work

Borchert and Rampersad, *Words with many palindrome pair factors* (2015), Section 4, proposed \(L(n)\) as the unrestricted binary maximum and exhibited computationally suggested three-run extremizers. Their Lemma 13 states that every word with at most three runs is a palindrome pair, but their article does not establish the four-run factor inventory or the strict four-run exclusion. Guo, Shallit and Shur, *On the Combinatorics of Palindromes and Antipalindromes* (2015), Proposition 5, give the useful equivalent characterization of a palindrome pair as a word conjugate to its reversal; their results concern individual words and language enumeration, rather than the present distinct-factor extremal comparison. The present theorem is a rigorously proved restricted-case step toward the former open extremal question, not its full resolution.

## Limitations

The proof excludes exactly-four-run maximizers and supplies the stated exact count only in that class. It does not exclude five-or-more-run candidates or settle the global conjecture. The originality comparison covers the identified primary papers and searchable related records; unindexed or differently named specialized classifications remain a priority risk. The checker tests finite instances only, independently of the supplied all-length proof.

## References

1. A. Borchert and N. Rampersad, *Words with many palindrome pair factors*, arXiv:1509.05396 (first public preprint 2015-09-17), *Electronic Journal of Combinatorics* 22(4), P4.23 (2015). https://arxiv.org/abs/1509.05396 ; https://doi.org/10.37236/5583 .
2. C. Guo, J. Shallit and A. M. Shur, *On the Combinatorics of Palindromes and Antipalindromes*, arXiv:1503.09112 (first public preprint 2015-03-31), Section 3. https://arxiv.org/abs/1503.09112 .
