# The sharp parity-inequality cutoff for partitions into fourth powers

## Finding

Let \(E_4(n)\) and \(O_4(n)\) denote the numbers of unrestricted partitions of the nonnegative integer \(n\) into positive fourth powers with, respectively, an even or odd number of parts. The empty partition of zero has zero parts. Define
\[
A_4(n)=(-1)^n\bigl(E_4(n)-O_4(n)\bigr).
\]
For every integer \(n\geq0\), \(A_4(n)\geq0\), and equality holds **if and only if**
\[
 n\in\{16,17,\ldots,31\}\cup\{48,49,\ldots,63\}\cup\{80,112,144\}.
\]
In particular,
\[
\boxed{A_4(n)>0\quad\hbox{for all integers }n\geq145.}
\]
The cutoff 145 is sharp because \(A_4(144)=0\), while \(A_4(145)=1\). This completely determines the equality cases in the sign-refined partition inequality for the fourth-power case.

## Assumptions and scope

A partition may repeat fourth-power parts. An odd-part-count partition contributes one to \(O_4(n)\), even-part-count one to \(E_4(n)\). The coefficientwise generating functions are formal series over \(\mathbb Z[[q]]\); no analytic convergence is necessary. The result pertains to fourth powers only. All intervals and inequalities include their specified endpoints.

## Proof

**Step 1: a distinct-part model.** Write the signed generating series as
\[
F(q)=\sum_{n\geq0}A_4(n)q^n
 =\prod_{m\geq1}\frac{1}{1+(-q)^{m^4}}
 =\prod_{m\text{ odd}}\frac1{1-q^{m^4}}
  \prod_{m\text{ even}}\frac1{1+q^{m^4}}.
\]
Every positive integer \(m\) is uniquely \(m=2^j u\), with \(u\) odd and \(j\geq0\). The elementary formal identity
\[
\frac1{1-x}=\prod_{\ell\geq0}(1+x^{2^\ell})
\]
then cancels, for each odd \(u\), every factor indexed by \(\ell=4,8,12,\ldots\). Consequently
\[
F(q)=\prod_{\substack{u\geq1\\u\text{ odd}}}
 \prod_{\substack{\ell\geq0\\\ell=0\text{ or }4\nmid\ell}}
 (1+q^{2^\ell u^4}). \tag{1}
\]
The exponents \(2^\ell u^4\) in (1) are pairwise distinct by uniqueness of the odd-part/dyadic-valuation decomposition. Thus \(A_4(n)\) exactly counts subsets of
\[
\mathcal W=\{2^\ell u^4:u\geq1\text{ odd},\ \ell=0\text{ or }4\nmid\ell\}
\]
with sum \(n\). In particular it is nonnegative.

**Step 2: a finite interval certificate.** The ten allowed, distinct weights
\[
B=\{1,2,4,8,32,64,81,128,162,324\}\subseteq\mathcal W
\]
fall into three sets: the weights \(1,2,4,8\) realize every sum from 0 to 15, the weights \(32,64,128\) realize \(32j\) for every \(0\leq j\leq7\), and \(81,162,324\) realize \(81t\) for every \(0\leq t\leq7\). Hence **all** subset sums of \(B\) form the union of the 64 integer intervals
\[
I_{j,t}=[32j+81t,\ 32j+81t+15]\cap\mathbb Z,
\qquad 0\leq j,t\leq7. \tag{2}
\]
Sorting and merging these explicit intervals gives precisely the eleven components
\[
\begin{gathered}
[0,15],\ [32,47],\ [64,79],\ [81,111],\ [113,143],\\
[145,661],\ [663,693],\ [695,725],\ [727,742],\\
[759,774],\ [791,806]. \tag{3}
\end{gathered}
\]
In particular every integer in \([145,661]\) is a subset sum of \(B\). Below 145, only the eight weights \(1,2,4,8,32,64,81,128\) from \(\mathcal W\) are usable. From (2), or by merging the components below 145 in (3), the omitted nonnegative integers below 145 are exactly the 35 integers in the stated equality set. In particular 144 is omitted.

**Step 3: propagate coverage to infinity.** Additional allowed weights will be adjoined in increasing order. Take all \(2^h\) with \(h\geq9\) and \(4\nmid h\), and, for each integer \(r\geq3\), take the two bridging weights
\[
81\cdot2^{4r-7},\qquad81\cdot2^{4r-6}. \tag{4}
\]
These weights all belong to \(\mathcal W\), none belongs to \(B\), and their first element in sorted order is 512. The ordered weights have ratio at most 2 between consecutive terms. Indeed consecutive eligible pure powers have ratio 2 except where the power \(2^{4r}\) is omitted. Across such a gap, for \(r\geq3\), the ordered chain is
\[
2^{4r-1},\quad81\cdot2^{4r-7},\quad
81\cdot2^{4r-6},\quad2^{4r+1},
\]
with consecutive ratios \(81/64\), \(2\), and \(128/81\). The first extra weight 512 satisfies \(512\leq517\), the number of integers in \([145,661]\).

If a set of subset sums contains all integers in \([145,U]\), and a new distinct positive weight \(w\) satisfies \(w\leq U-145+1\), adjoining that weight makes the entire interval \([145,U+w]\) representable: it is the union of the old interval and its translate by \(w\), which overlap or are adjacent. Starting with interval length \(L=517\) and \(w=512\), the new length is \(L+w\geq2w\). The next weight \(w'\) is at most \(2w\), so the same argument applies inductively to all extra weights. Their sums tend to infinity, proving every integer \(n\geq145\) is representable by distinct allowed weights. Together with Step 2 and (1), this proves the theorem. \(\square\)

## Verification

The standalone Python 3 file `verify.py` is dependency-free and independently reproduces (2)--(3) by enumerating all \(2^{10}=1024\) subsets of \(B\). It checks the 35 equalities and the 517-integer initial interval, performs two algebraically independent coefficient recurrences through degree 2048, and samples the dyadic bridging ratios at 13 higher scales. Execute `python3 verify.py`. These finite checks do not replace the infinite induction in Step 3 or the formal-product identity in Step 1.

## Relationship to prior work

Ciolan, *Equidistribution and inequalities for partitions into powers* (first public arXiv version February 13, 2020), proves eventual strict parity inequalities for all fixed exponents and a combinatorial coefficientwise nonnegativity mechanism. Its Section 3 proves nonnegativity; the conclusion explicitly allows small equality cases. That article does not enumerate the fourth-power equality cases or state the exact threshold 145. The present result derives an exact finite boundary, rather than another asymptotic or general sign statement. Ciolan's earlier work on squares addresses the distinct exponent two; a known exact cutoff for squares does not imply the fourth-power cutoff.

## Limitations

The result neither calculates the numbers \(A_4(n)\) for every \(n\) nor determines sharp thresholds for other fixed exponents. Novelty is assessed relative to the inspected primary literature, targeted searches, and accessible comparison records; a differently indexed prior computation remains possible. No independent mathematical audit has been performed.

## References

1. A. Ciolan, *Equidistribution and inequalities for partitions into powers*, arXiv:2002.05682 (first version February 13, 2020), https://arxiv.org/abs/2002.05682 . In particular Theorems 2--3 and Sections 2--3 and 8; an open full text is https://archive.mpim-bonn.mpg.de/4196/1/mpim-preprint_2021-3.pdf .
2. A. Ciolan, *Asymptotics and inequalities for partitions into squares*, arXiv:1806.00708 (2018), https://arxiv.org/abs/1806.00708 .
