# The palindromic-defect law and exact spectrum for binary words with three ones

## Finding

For a finite binary word \(w\), let \(\operatorname{Pal}^{+}(w)\) be its set of **distinct nonempty contiguous palindromic factors** and define its *palindromic defect* as \(D(w)=|w|-|\operatorname{Pal}^{+}(w)|\). A word is *rich* precisely when \(D(w)=0\). For every quadruple \(a,b,c,d\in\mathbb Z_{\ge0}\), write
\[
w=0^a1\,0^b1\,0^c1\,0^d.
\]
Then the exact defect is
\[
D(w)=\begin{cases}
0,&b=c,\\
\max\{0,\min(a,d)-\max(b,c)\},&b\ne c.
\end{cases}
\]
In particular, a three-one binary word fails richness exactly when its two interior zero gaps differ and both exterior zero runs are longer than either interior gap.

The complete joint length-and-defect generating function, with \(z\) marking length and \(u\) marking defect, is
\[
F(z,u)=\sum_{n\ge0}\sum_{\substack{w\in\{0,1\}^n\\|w|_1=3}}z^nu^{D(w)}
=\frac{z^3}{(1-z)^4}+\frac{2z^8(u-1)}{(1-z)^2(1-z^3)(1-z^4)(1-uz^2)}.
\]
Equivalently, for every integer \(r\ge1\), the length generating function for exactly defect \(r\) is
\[
H_r(z)=\frac{2z^{2r+6}(1+z)}{(1-z)(1-z^3)(1-z^4)},
\]
and the rich, defect-zero, length generating function is
\[
H_0(z)=\frac{z^3}{(1-z)^4}-\frac{2z^8}{(1-z)^2(1-z^3)(1-z^4)}.
\]
Thus, among uniformly sampled length-\(n\) binary words with three ones, the limiting rich proportion equals \(5/6\). Every binary word with at most two ones is rich, so the three-one layer is the first layer exhibiting positive palindromic defect.

## Assumptions and scope

The alphabet is \(\{0,1\}\); symbols are distinguished. Words are finite, linear, and indexed: **neither cyclic factors nor subsequences** are considered. All four zero-run lengths may equal zero, so consecutive ones and leading/trailing ones are included. A palindrome is allowed to contain zero, one, two, or three ones; palindromes are counted as *distinct strings*, not by their number of occurrences. In \(F(z,u)\), coefficients are interpreted in the formal power-series ring \(\mathbb Z[u][[z]]\); the count is zero at lengths below three.

## Proof

**Classification of palindromes.** Put \(M=\max(a,b,c,d)\) and \(P=\max\{\min(a,b),\min(b,c),\min(c,d)\}\). There are exactly \(M\) nonempty all-zero palindromes and exactly \(1+P\) palindromes with one one, the latter being \(0^t1\,0^t\) with \(0\le t\le P\).

If \(b\ne c\), the two families of palindromes containing exactly two ones have distinct middle gaps and hence are disjoint. They are \(0^t1\,0^b1\,0^t\) for \(0\le t\le\min(a,c)\), and \(0^t1\,0^c1\,0^t\) for \(0\le t\le\min(b,d)\). There is no palindrome with all three ones, since this would require \(b=c\). Consequently,
\[
|\operatorname{Pal}^{+}(w)|=M+P+\min(a,c)+\min(b,d)+3.
\]
It suffices, by reversing the word, to handle \(b>c\), when \(P=\max\{\min(a,b),c\}\). If \(a<b\), then \(P+\min(a,c)=a+c\) and \(M+\min(b,d)=b+d\), proving zero defect. If \(a\ge b\) and \(d\le b\), then \(M=a\), \(P=b\), \(\min(a,c)=c\), and \(\min(b,d)=d\), again proving zero defect. In the remaining case \(a\ge b\) and \(d>b\), we have \(M=\max(a,d)\), \(P=b\), \(\min(a,c)=c\), and \(\min(b,d)=b\); subtraction from \(|w|=a+b+c+d+3\) yields \(D(w)=\min(a,d)-b\), which is nonnegative. Reversal gives the analogous formula when \(c>b\), completing this case.

If \(b=c=t\), write \(x=\max(a,d)\) and \(y=\min(a,d)\). Then the numbers of palindromes with zero, one, two and three ones are respectively \(\max(x,t)\), \(t+1\), \(1+\min(x,t)\), and \(1+y\). These four families are disjoint. Their total is \(x+2t+y+3=|w|\), using \(\max(x,t)+\min(x,t)=x+t\). Hence \(D(w)=0\) also in this case.

**All defect strata.** Fix \(r\ge1\). For each word of defect \(r\), one interior gap is strictly larger than the other. Orient so that \(b=m>c=j\), where \(m\ge1\) and \(0\le j<m\). The defect law is equivalent to writing \(a=m+r+s\) and \(d=m+r+t\) for nonnegative \(s,t\) with \(\min(s,t)=0\). The reverse orientation contributes an equal and disjoint family. Since \(|w|=3+2r+3m+j+s+t\), the exact length enumerator is
\[
H_r(z)=2z^{3+2r}\left(\sum_{m\ge1}\sum_{j=0}^{m-1}z^{3m+j}\right)
\left(\sum_{\substack{s,t\ge0\\\min(s,t)=0}}z^{s+t}\right).
\]
The first parenthesis equals \(z^3/((1-z^3)(1-z^4))\), while the second equals \((1+z)/(1-z)\). This proves the claimed formula for \(H_r(z)\). Summing over \(r\ge1\) gives
\[
\sum_{r\ge1}H_r(z)=\frac{2z^8}{(1-z)^2(1-z^3)(1-z^4)}.
\]
There are exactly \(\binom n3\) binary length-\(n\) words with three ones, with ordinary generating function \(z^3/(1-z)^4\). Subtracting the positive-defect strata proves the formula for \(H_0(z)\). Weighting them by \(u^r\) and summing a geometric series proves the stated \(F(z,u)\).

**Density.** As \(z\to1^-\), the positive-defect enumerator is asymptotic to \(\tfrac16(1-z)^{-4}\), while the enumerator for all three-one words is \(z^3(1-z)^{-4}\). Their length-\(n\) coefficients therefore have leading terms \(n^3/36\) and \(n^3/6\), respectively. The ratio of rich to all three-one words tends to \(1-1/6=5/6\).

Finally, every word with zero or one one is easily counted by its zero palindromes and its unique-centred one palindromes. For two ones, writing \(w=0^a1\,0^b1\,0^c\) and setting \(x=\max(a,c)\), the number of nonempty palindromes is \(\max(x,b)+(1+\min(x,b))+(1+\min(a,c))=a+b+c+2=|w|\). Thus these lower-weight layers are entirely rich.

## Verification

Run `python3 verify.py` with Python 3 and the standard library. It constructs palindromic-factor sets by **independent centre expansion** and exhaustively compares the defect law over all binary three-one words of lengths \(3\) through \(34\). It separately compares defect-stratum coefficients with the rational generating functions in that range, and compares two independent positive-defect counting sums for lengths through \(500\). Its success marker is `ALL_CHECKS_PASS`. Finite checks are corroboration, not the proof for arbitrary length; the case analysis and formal generating-function identities above establish the unrestricted statements.

For illustration, the positive-defect counts at lengths \(8,9,10,11,12,13,14,15,16\) are respectively \(2,4,6,10,16,22,30,40,52\). At length \(20\), the defect counts for \(r=0,1,\ldots,7\) are respectively \(1018,40,30,22,14,10,4,2\), summing to \(\binom{20}3=1140\).

## Relationship to prior work

Glen–Justin–Widmer–Zamboni's foundational theory defines rich words, palindromic defect, and structural characterizations. Guo–Shallit–Shur study the **total** binary rich-word growth function and give an infinite run-length sufficient family; those statements do not enumerate fixed-three-one defect strata. Rukavicka establishes subexponential bounds for the unrestricted alphabet-size growth function. Pelantová–Starosta's binary forbidden-factor criterion determines **whether** a word is rich, but does not give the exact positive defect of each three-one word or the bivariate defect-enumerator formula here. Fici identifies the shortest non-rich binary example of length eight, which lies in the three-one layer, but does not state the all-length joint defect law or generating function. These results are compatible: the example and general zero-defect criterion can be recovered from the formula as special qualitative observations. A prior equivalent enumeration has not been ruled out absolutely.

## Limitations

The result concerns exactly three occurrences of one; it does not claim an exact defect distribution for four or more ones or an unrestricted binary rich-word census. It distinguishes zero from one and therefore does not double-count the complementary three-zero layer. The proof requires no computational conjectures. Bibliographic comparisons are not an independent priority audit, and a previously unpublished or unindexed equivalent formula remains possible.

## References

1. A. Glen, J. Justin, S. Widmer, L. Q. Zamboni, *Palindromic Richness*, arXiv:0801.1656 (first public version 2008-01-10), https://arxiv.org/abs/0801.1656 .
2. C. Guo, J. Shallit, A. M. Shur, *On the Combinatorics of Palindromes and Antipalindromes*, arXiv:1503.09112 (2015), https://arxiv.org/abs/1503.09112 .
3. J. Rukavicka, *On Number of Rich Words*, arXiv:1701.07778 (2017), https://arxiv.org/abs/1701.07778 .
4. E. Pelantová, Š. Starosta, *On Words with the Zero Palindromic Defect*, arXiv:1708.06911 (2017), https://arxiv.org/abs/1708.06911 .
5. G. Fici, *The Shortest Interesting Binary Words*, arXiv:2412.21145 (2024), https://arxiv.org/abs/2412.21145 .
6. OEIS A216264, *Number of rich binary words of length n* (unrestricted weight), https://oeis.org/A216264 .
