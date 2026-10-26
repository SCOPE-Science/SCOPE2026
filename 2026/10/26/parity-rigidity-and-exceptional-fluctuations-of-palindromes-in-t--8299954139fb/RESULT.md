# Parity rigidity and exceptional fluctuations of palindromes in two-marker circular words

## Finding
A circular word of length \(n\) is a word considered modulo rotation. Its palindromic-factor count \(P(w)\) is the number of **distinct nonempty** palindromic strings occurring as cyclic factors of lengths between \(1\) and \(n\), inclusive. For integers \(a,b\geq0\), consider the binary circular word represented by \(w=1\,0^a1\,0^b\), of length \(n=a+b+2\). Then
\[
P(w)=\max(a,b)+\min(a,b)+1+
\begin{cases}
\lfloor a/2\rfloor+\lfloor b/2\rfloor+2,&a\ne b,\\
\lfloor a/2\rfloor+1,&a=b.
\end{cases}
\]
In particular, **every** binary circular word with precisely two ones and odd length \(n\) has the *same* count \(P(w)=(3n-1)/2\), regardless of the positions of the ones.

For even length \(n=2m\), with \(m\geq1\), define \(H=3m\), \(D=\lfloor m/2\rfloor+1\), \(A=\lfloor m/2\rfloor\), and \(B=\lceil m/2\rceil-1\). The complete distribution among the \(m\) binary circular words of weight two (one representative per rotation orbit) is:

| Palindromic-factor count | Number of circular words |
| --- | ---: |
| \(H\) | \(A\) |
| \(H-1\) | \(B\) |
| \(H-D\) | \(1\) |

Zero-frequency rows are omitted, and any coinciding values are combined. The exceptional class \(H-D\) has its two ones exactly opposite one another and its representative is \(1\,0^{m-1}1\,0^{m-1}\). For \(n\geq4\), the sharp maximum over weight-two circular words is \(3n/2\), attained precisely by unequal, **even** zero gaps. For odd \(n\), every such word maximizes within this fixed-weight family.

Choose a length-\(n\) binary word uniformly from all \(\binom n2\) words containing exactly two ones, and let \(X_n\) be its circular palindromic-factor count. For odd \(n\), \(\operatorname{Var}(X_n)=0\). For even \(n=2m\), the probabilities of the three rows above are respectively \(2A/(2m-1)\), \(2B/(2m-1)\), and \(1/(2m-1)\). In consequence,
\[
\mathbb E X_{2m}=H-\frac{2B+D}{2m-1},\qquad
\operatorname{Var}(X_{2m})=
\frac{2B+D^2}{2m-1}-\left(\frac{2B+D}{2m-1}\right)^2.
\]
Along even lengths, \(\mathbb E X_n=3n/2-3/4+O(1/n)\) and \(\operatorname{Var}(X_n)=n/16+O(1)\). Thus the variance is identically zero along odd lengths but grows linearly along even lengths, driven by the single antipodal necklace orbit of probability \(1/(n-1)\) and deficit \(\Theta(n)\).

## Assumptions and scope
The alphabet is \(\{0,1\}\), exactly two entries are one, and \(n\geq2\). Cyclic factors have lengths no greater than the circumference \(n\): factors containing more than two ones by traversing multiple turns are **not** counted. Distinct means distinct as strings, not occurrences or rotational classes of factors. For a uniformly random linear word, the circular statistic is computed from all its rotations. The case \(n=2\) is included in the distribution formulas (only the antipodal class, with count \(2\)); the displayed sharp maximum \(3n/2\) is asserted only for \(n\geq4\).

## Proof
Fix \(a,b\geq0\), and write \(n=a+b+2\). Every cyclic factor of length at most \(n\) contains at most two ones, so partition its distinct palindromic factors by the number of ones.

**No ones.** Exactly the strings \(0^j\), \(1\leq j\leq\max(a,b)\), occur, giving \(\max(a,b)\) strings. This family is empty when \(a=b=0\).

**Exactly one one.** Every such palindrome has the form \(0^i1\,0^i\). Around either one the two adjacent zero gaps have lengths \(a\) and \(b\); the factor occurs exactly when \(0\leq i\leq\min(a,b)\). Thus there are \(\min(a,b)+1\) such strings. In particular, the case \(i=0\) counts the one-letter factor \(1\) once.

**Exactly two ones.** Symmetry forces the form \(0^i1\,0^g1\,0^i\), in which the internal zero gap \(g\) is one of \(a,b\). If \(g=a\), the remaining circular gap \(b\) must accommodate \(i\) zeros outside each end, and a factor of permitted length exists precisely when \(2i\leq b\). Therefore this family contains exactly \(\lfloor b/2\rfloor+1\) strings. Similarly \(g=b\) contributes \(\lfloor a/2\rfloor+1\). When \(a\ne b\), these families are disjoint because their internal gaps differ. When \(a=b\), they coincide identically and contribute only \(\lfloor a/2\rfloor+1\) strings. The classification also holds at \(a=b=0\), where the factors are \(1\) and \(11\). Adding the three disjoint marked-symbol families proves the first formula.

If \(a\ne b\), the first formula simplifies to
\[
P(w)=n+1+\lfloor a/2\rfloor+\lfloor b/2\rfloor.
\]
If \(n\) is odd, then \(a+b=n-2\) is odd, so \(a\ne b\) and the floors sum to \((n-3)/2\). Hence \(P(w)=(3n-1)/2\). If \(n=2m\), then \(a+b=2m-2\) is even. Unequal gaps are either both even, giving \(P=3m\), or both odd, giving \(P=3m-1\). Equal gaps necessarily satisfy \(a=b=m-1\), and give
\[
P=2m+\lfloor(m-1)/2\rfloor=3m-\lfloor m/2\rfloor-1=H-D.
\]
For odd \(n=2m+1\), the unordered gap pairs \(\{a,b\}\) number \(m\), all unequal. For even \(n=2m\), exactly one unordered gap pair is equal. Of the unequal pairs, precisely \(A=\lfloor m/2\rfloor\) have both gaps even, and \(B=\lceil m/2\rceil-1\) have both gaps odd: enumerate the smaller gap \(a\) in \(0\leq a<m-1\), and use \(b=2m-2-a\). This proves the necklace distribution and all stated maximizers.

Each unequal gap pair has a rotation orbit of size \(n\). The equal pair, which exists only for even \(n\), has rotation orbit size \(n/2\), because rotating by half the circumference fixes it. Thus, under uniform sampling of the \(\binom n2\) labeled words, an unequal necklace has probability \(n/\binom n2=2/(n-1)\), whereas the equal necklace has probability \((n/2)/\binom n2=1/(n-1)\). This yields the exact probability masses. For even \(n=2m\), define the deficit \(Y=H-X_n\); it takes values \(0,1,D\) with multiplicities proportional to \(2A,2B,1\). Computing \(\mathbb EY\) and \(\mathbb EY^2\) proves the exact mean and variance. Since \(B=m/2+O(1)\) and \(D=m/2+O(1)\), their asymptotics are \(\mathbb EY=3/4+O(1/m)\) and \(\operatorname{Var}(Y)=m/8+O(1)=n/16+O(1)\). At odd lengths all values coincide, so the variance is exactly zero. This completes the proof.

## Verification
Run `python3 checker.py` with Python 3 and the standard library. The checker directly generates the distinct cyclic palindromes and compares them to the formula for every ordered gap pair with \(2\leq n\leq55\) (1,485 cases), and for 25 additional large-size boundary samples. It independently enumerates all unordered gap classes and labeled weight-two words for \(2\leq n\leq45\), checking the complete spectrum, exact mean, and exact variance by rational arithmetic. Observed output is recorded in `VERIFICATION.md`. These finite checks corroborate, but do not replace, the all-length counting argument above.

## Relationship to prior work
J. Simpson's 2014 article initiated the sharp general study of distinct palindromes in circular words and gives a general upper bound of \(5n/3\). OEIS A247000 records finite global maxima of the binary circular-palindrome statistic and examples, some of which are two-marker circles. Neither the general upper bound nor the listed global maxima logically determines a fixed-weight-two gap-by-gap classification or the distribution and variance derived here. The 2017 paper by Amit and Gawrychowski treats **squares**, not palindromes, in circular words; its introduction cites Simpson's palindrome bound. These works motivate the circular statistic and provide useful comparisons, but are not claimed to establish the present classification.

## Limitations
The theorem only concerns binary circular words containing exactly two ones. It does not determine maximum palindromic complexity over all binary circular words or higher-weight families. Self-review is not an independent mathematical audit. The full body of Simpson's 2014 article was not accessible despite open-access and institutional attempts, leaving a genuine historical-priority risk for an equivalent special case in that paper or other earlier literature. Finite tests cannot rule out an unindexed prior theorem; the mathematical argument itself proves the stated all-length identities under the definitions above.

## References
1. J. Simpson, *Palindromes in circular words*, Theoretical Computer Science **550** (2014), 66–78; available online 2014-07-22. DOI: 10.1016/j.tcs.2014.07.012. Library abstract: https://researchportal.murdoch.edu.au/esploro/outputs/journalArticle/Palindromes-in-circular-words/991005543823107891
2. OEIS A247000, *Maximal number of palindromes in a circular binary word of length n*: https://oeis.org/A247000
3. M. Amit and P. Gawrychowski, *Distinct Squares in Circular Words*, arXiv:1708.00639 (2017): https://arxiv.org/html/1708.00639v1
