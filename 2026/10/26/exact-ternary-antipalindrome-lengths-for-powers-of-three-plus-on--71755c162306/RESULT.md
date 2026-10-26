# Exact ternary-antipalindrome lengths for powers of three plus one

## Finding
A positive integer is a ternary antipalindrome if its usual base-three expansion has digits \(a_0,\ldots,a_{\ell-1}\) with \(a_j+a_{\ell-1-j}=2\) and the leading digit nonzero. Write \(H(N)\) for the smallest number of positive ternary antipalindromes summing to \(N\). For every integer \(n\ge1\),
\[
H(3^n+1)=\begin{cases}1,&n=1;\\2,&n=2\text{ or }n\ge6\text{ even};\\3,&n\ge3\text{ odd, or }n=4.\end{cases}
\]
For \(n=2\), the only unordered two-term expression is \(10=4+6\). For every even \(n\ge6\), the **only** unordered two-term expression is \(3^n+1=A_n+B_n\), where
\[
B_n=3^{n-3}+1+2\sum_{j=1}^{n/2-2}3^{2j},\qquad A_n=3^n+1-B_n.
\]
Both summands are ternary antipalindromes. For all \(n\ge3\), an explicit three-term expression is \(3^n+1=1+U_n+V_n\), with \(U_n=(5\cdot3^{n-2}-3)/2\), \(V_n=3^n-U_n\).

## Assumptions and scope
All sums use positive summands, standard base-three representations without leading zeros, and no restrictions on lengths beyond the size of their sum. The index \(n\) is an arbitrary integer at least one. An unordered expression identifies the two possible summand orders. The result does not classify representations of integers outside the specified infinite sequence.

## Proof
**Digit-sum carry budget.** Every antipalindrome of length \(\ell\) has ternary digit sum exactly \(\ell\). Consider a two-term expression \(X+Y=N=3^n+1\) for \(n\ge2\). The number \(N\) has ternary digits \(10^{n-1}1\) and digit sum two, and is not itself an antipalindrome. Any antipalindrome of length \(n+1\) is at least \(3^n+1\), so both summands have length at most \(n\); at least one has length \(n\). Since \(N\equiv1\pmod3\), the last summand digits must be \(0,1\) in some order; their leading digits therefore are \(2,1\). The summand of leading digit two must have length \(n\): otherwise a length-\(n\) summand starting with one and a shorter summand starting with two would sum to less than \(3^n\). Call the length-\(n\) summand \(X\), and the other \(Y\), of length \(m\). Parity of ternary digit sums gives \(m\equiv n\pmod2\). Write \(m=n-2h\), where \(h\) is a nonnegative integer.

Write \(x_j,y_j\in\{0,1,2\}\) for low-to-high ternary digits of the summands, padding with zeros outside their lengths, and \(c_j\in\{0,1\}\) for the carry entering column \(j\). We have \(c_0=c_1=0\) because \(x_0=0,y_0=1\). In every column \(1\le j\le n-1\), the required output digit is zero, hence \(x_j+y_j+c_j=3c_{j+1}\). A carry of one cannot revert to zero. The carry leaving column \(n-1\) is one, since the leading digit of \(N\) is one. Summing the digit balances, the total number of carried units is \((n+m-2)/2=n-h-1\). There are \(n-h-1\) carry positions, namely those after columns \(h+1,h+2,\ldots,n-1\). It follows that
\[
 x_j+y_j=0\ (1\le j\le h),\quad x_{h+1}+y_{h+1}=3,\quad x_j+y_j=2\ (h+2\le j\le n-1).
\]

**Eliminating length gaps.** If \(h\ge2\) and \(m\le h+1\), the transition column has \(y_{h+1}=0\), an impossibility. If instead \(m\ge h+2\), then \(m\ge4\), and column \(j=n-h-2=m+h-2\) is above the length of \(Y\) and in the stable-carry range. Thus \(x_j=2\). Antipalindromicity gives \(x_{h+1}=2-x_j=0\), contradicting the transition-column sum three. Hence \(h\le1\).

If \(h=0\) and \(n\ge3\), the leading column \(n-1\), with incoming carry one, would require \(x_{n-1}+y_{n-1}=2\), while the leading digits are two and one. This is impossible. For \(n=2\), direct column equations uniquely give \((X,Y)=(6,4)\).

Now assume \(h=1\). Then \(m=n-2\), the transition is at column two, and \(x_1=y_1=0\). If \(n\le4\), the shorter number has no column-two digit, contradicting the transition sum three. If \(n=5\), the middle digit of the length-five antipalindrome \(X\) is one, and the top digit of the length-three antipalindrome \(Y\) is one; again their column-two sum is not three. Hence \(n\ge6\).

Since \(x_{n-1}=x_{n-2}=2\), \(y_{n-3}=1\), and the column \(n-3\) is in the stable-carry range, \(x_{n-3}=1\); complement symmetry gives \(x_2=1\), and the transition forces \(y_2=2\). If \(n\ge7\), the digit \(y_{n-4}=2-y_1=2\) forces \(x_{n-4}=0\), hence \(x_3=2\). If \(n\ge8\), similarly \(y_{n-5}=2-y_2=0\) forces \(x_{n-5}=2\), hence \(x_4=0\). For each \(3\le j\le n-6\), applying stable-carry column sums at \(j\) and \(n-3-j\), and then the complementary-digit identities for both summands, yields \(x_{j+2}=x_j\). Thus all intermediate digits \(x_3,\ldots,x_{n-4}\) alternate \(2,0,2,0,\ldots\), and all remaining digits of \(X,Y\) are uniquely determined. If \(n\ge7\) is odd, the central digit \(x_{(n-1)/2}\) lies in this alternating block, hence is either zero or two; but it must be one. This contradiction eliminates every odd \(n\ge7\). (For \(n=7\), the same forced equation \(x_3=2\) directly contradicts the central digit.) Therefore two summands are possible only for \(n=2\) and even \(n\ge6\).

**Construction and uniqueness.** For even \(n\ge6\), define the shorter number \(B_n\) by the formula in the finding. Its low-to-high digits are \(1,0,2,0,2,0,\ldots,2,1\), hence they sum in opposite positions to two; its length is \(n-2\). Define \(A_n=3^n+1-B_n\). The base-three subtraction, or equivalently the column equations above, gives the length-\(n\) antipalindrome with low digits \(0,0,1,2,0,2,\ldots,0,1,2,2\) (for \(n=6\), its digits are \((221100)_3\)). Since the carry analysis determines all digits uniquely, this unordered representation is the only one.

**Three summands and sharpness.** For \(n\ge3\), the number \(U_n\) has ternary expansion \((2\underbrace{11\cdots1}_{n-3}0)_3\). The number \(V_n\) is \((210)_3\) for \(n=3\), and \((20\underbrace{11\cdots1}_{n-4}20)_3\) for \(n\ge4\). These are both antipalindromes, as is the one-digit number \(1\); their sum is \(3^n+1\). Together with the two-term obstruction this proves the claimed minimum three for odd \(n\ge3\) and \(n=4\). Finally, \(3^1+1=(11)_3\) is itself an antipalindrome. This completes the classification.

## Verification
Run `python3 verify.py` from this package. It generates antipalindromes independently by digit-complement recursion, exhaustively counts unordered representations for \(1\le n\le14\), checks the exceptional pair and every explicit even-index pair, and checks all three-summand constructions. This is an auxiliary finite consistency test; the proof above establishes the claim for every \(n\ge1\).

## Relationship to prior work
Dvořáková, Kruml, and Ryzák introduced systematic arithmetic study of antipalindromic numbers and conjectured that every positive integer outside a short exceptional list is a sum of at most three ternary antipalindromes, reporting computation through five million. Their definition, parity and divisibility properties, and the open three-summand problem motivate the exact infinite-family analysis. Their Sections 2–6 do not give a minimal-summand classification for \(3^n+1\) or uniqueness of its two-term representations. The present claim is narrower than their unrestricted conjecture and does not imply it.

## Limitations
No universal three-summand theorem for arbitrary integers is claimed. Finite exhaustive checks stop at \(n=14\); they are not a substitute for the symbolic carry proof. The originality search cannot exclude unpublished or unindexed equivalent results. Independent assessment has not been performed.

## References
Dvořáková, Ľ., Kruml, S., and Ryzák, D., *Antipalindromic numbers*, arXiv:2008.06864 (first public version 2020-08-16); *Acta Polytechnica* 61 (2021), 428–440, DOI 10.14311/AP.2021.61.0428.
