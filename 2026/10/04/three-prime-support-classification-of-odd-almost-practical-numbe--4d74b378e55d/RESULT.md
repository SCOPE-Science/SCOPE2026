# Three-prime-support classification of odd almost practical numbers
## Finding
Call a positive integer \(n\) almost practical when every integer \(j\) with \(2<j<\sigma(n)-2\) is a sum of distinct positive divisors of \(n\). An odd integer with exactly three distinct prime factors is almost practical if and only if
\[
n=3^a5^b7^c,
\qquad a,b,c\ge 1,
\qquad a\ge 2,
\qquad a+b+c\ge 5.
\]
Equivalently, for positive \(a,b,c\), the number \(3^a5^b7^c\) is almost practical exactly when \(a\ge2\) and \((a,b,c)\ne(2,1,1)\).

## Assumptions and scope
The divisor-sum function is \(\sigma(n)=\sum_{d\mid n}d\). All sums of divisors use each positive divisor at most once. The theorem concerns odd integers with exactly three distinct prime factors; no assertion is made about even almost practical numbers or about odd almost practical numbers with four or more distinct prime factors.

The proof uses Stewart's criterion for odd almost practical numbers and Stewart's closure result: if an odd almost practical number \(m\ne3\) is multiplied by a prime already dividing \(m\), the product remains almost practical. A later full-text restatement of these results appears as Proposition 3.6 and Proposition 3.10 in F. Jokar, *On k-layered numbers*, arXiv:2207.09053.

## Proof
Let \(1=d_1<d_2<\cdots<d_k=n\) be the positive divisors of an odd integer \(n\), and write \(s_i=d_1+\cdots+d_i\). Stewart's criterion states that, for \(n\ne3\), almost practicality is equivalent to \(d_2=3\), \(d_3=5\), and for every \(i\ge3\) either
\[
d_{i+1}\le s_i-2\quad\hbox{and}\quad d_{i+1}\ne s_i-4,
\]
or
\[
d_{i+1}=s_i-4\quad\hbox{and}\quad d_{i+2}=s_i-2.
\]
The same source records the consequence that if an odd almost practical integer has at least three distinct prime factors, then its third smallest prime factor is \(7\). Thus an odd almost practical integer with exactly three distinct prime factors must have the form \(3^a5^b7^c\) with \(a,b,c\ge1\).

We now determine the exponent triples.

First suppose \(a=1\). The first five divisors are then \(1,3,5,7,15\): the divisor \(9\) is absent, and every other new product is at least \(15\). At \(i=4\), one has \(s_4=16\) and \(d_5=15\). The first branch of Stewart's criterion would require \(15\le14\), and the second would require \(15=12\). Both fail. Hence no triple with \(a=1\) is almost practical.

Next take \((a,b,c)=(2,1,1)\), so \(n=315\). Its divisors are
\[
1,3,5,7,9,15,21,35,45,63,105,315.
\]
The first eleven sum to \(309\). At the final transition Stewart's criterion would require either \(315\le307\) or \(315=305\); both are false. Therefore \(315\) is not almost practical.

It remains to prove all other triples with \(a\ge2\). Three base integers suffice:
\[
945=3^3\cdot5\cdot7,
\qquad
1575=3^2\cdot5^2\cdot7,
\qquad
2205=3^2\cdot5\cdot7^2.
\]
For \(945\), the ordered divisors are
\[
1,3,5,7,9,15,21,27,35,45,63,105,135,189,315,945.
\]
For indices \(i=3,\ldots,15\), the values of \(s_i-2-d_{i+1}\) are
\[
0,5,8,17,32,51,76,103,124,199,280,343,28.
\]
All are nonnegative and none equals \(2\), so the first branch of Stewart's criterion holds at every step.

For \(1575\), the ordered divisors are
\[
1,3,5,7,9,15,21,25,35,45,63,75,105,175,225,315,525,1575,
\]
and the corresponding values of \(s_i-2-d_{i+1}\), for \(i=3,\ldots,17\), are
\[
0,5,8,17,34,49,74,101,152,197,232,357,492,597,72.
\]
Again all are nonnegative and none equals \(2\).

For \(2205\), the ordered divisors are
\[
1,3,5,7,9,15,21,35,45,49,63,105,147,245,315,441,735,2205,
\]
and the corresponding values are
\[
0,5,8,17,24,49,90,125,146,209,258,433,622,769,34.
\]
Thus all three bases are almost practical.

Stewart's closure result says that multiplying an odd almost practical integer by a prime already dividing it preserves almost practicality. Hence every triple with \(a\ge3\) follows from \(945\). If \(a=2\) and \(b\ge2\), every such triple follows from \(1575\). If \(a=2\), \(b=1\), and \(c\ge2\), every such triple follows from \(2205\). These three cases are exactly \(a\ge2\) with \((a,b,c)\ne(2,1,1)\), equivalently \(a\ge2\) and \(a+b+c\ge5\). This proves the classification.

## Verification
The accompanying `verify.py` independently generates divisors, implements Stewart's odd criterion, checks the three positive bases and the two obstruction patterns, verifies by subset-sum dynamic programming that the three positive bases miss exactly \(2\) and \(\sigma(n)-2\), and checks every exponent triple \(1\le a,b,c\le6\) against the stated classification. The finite grid is corroborative only; the infinite theorem follows from the proof above and Stewart's closure theorem.

## Relationship to prior work
B. M. Stewart's 1954 paper *Sums of Distinct Divisors* gives the odd almost-practical criterion and the multiplication closure used here. The 2022 full-text restatement by Jokar records that an odd almost practical number with at least three distinct prime factors has third prime \(7\), and explicitly gives the sufficient family \(3^a5^b7^c\) for \(a\ge3\). The present classification closes the missing \(a=1\) and \(a=2\) boundary: \(a=1\) never works, while for \(a=2\) exactly \(315\) fails and every larger exponent triple works.

OEIS A174535 lists odd almost practical numbers and begins \(945,1575,2205,2835,\ldots\), consistent with the theorem. Focused searches for the exact three-prime-support classification, the exponent form \(3^a5^b7^c\), and the boundary values \(315,1575,2205\) did not locate a prior statement of this complete classification. The inaccessible original 1954 full text remains a residual literature risk; the specific Stewart criterion and closure theorem used here were checked in a later full-text source that attributes them precisely to Stewart.

## Limitations
This result is a classification inside the natural minimal three-prime-support stratum of odd almost practical numbers. It does not classify odd almost practical numbers with more prime factors. The originality comparison is limited by lack of direct full-text access to Stewart's 1954 article; issue metadata and later precise restatements were inspected, but an equivalent corollary could conceivably appear in the original text under different notation.

## References
1. B. M. Stewart, *Sums of Distinct Divisors*, American Journal of Mathematics 76 (1954), 779–785, DOI 10.2307/2372651.
2. F. Jokar, *On k-layered numbers*, arXiv:2207.09053 (2022), especially Section 3, Proposition 3.6, Theorem 3.8, Proposition 3.10, and Example 3.11.
3. OEIS A174533, *Almost practical numbers*.
4. OEIS A174535, *Odd almost practical numbers*.
