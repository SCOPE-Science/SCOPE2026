# Exact power-of-base differences of nonbinary palindromes

## Finding

Let \(b\ge3\) and \(k\ge1\) be integers. A positive integer is a base-\(b\) palindrome if its canonical base-\(b\) expansion, with nonzero leading digit, reads identically in both directions. Let \(\mathcal P_b\) be the set of all such integers and define

\[
R_b(k)=\{(n,m)\in\mathcal P_b\times\mathcal P_b:m-n=b^k\}.
\]

Write \(\tau(k)\) for the number of positive divisors of \(k\). Then

\[
\boxed{\lvert R_b(k)\rvert=(b-1)^2b^{k-1}+\tau(k).}
\]

More precisely, \(R_b(k)\) is the disjoint union of two explicitly classified families.

**Divisor-spaced family.** For each positive divisor \(a\mid k\), one pair is

\[
n=\sum_{j=0}^{k/a-1}b^{ja}=\frac{b^k-1}{b^a-1},\qquad m=n+b^k.
\]

**Central-digit family.** Let \(n\) be an arbitrary base-\(b\) palindrome with exactly \(2k+1\) digits and central digit in \(\{0,1,\ldots,b-2\}\). Then \(m=n+b^k\) is also a base-\(b\) palindrome. Every pair with that length has this form.

The first family has \(\tau(k)\) pairs; the second has \((b-1)^2b^{k-1}\). These are all the pairs.

## Assumptions and scope

All palindromes are **positive integers** in an integer base \(b\ge3\), and their leading digits are nonzero. The gap is precisely \(b^k\) for a positive integer \(k\), not a general difference. Pairs are ordered as \((n,m)\) with \(n<m\). No primality assumption is made on \(b\). The statement includes \(k=1\) and every composite base.

For an integer \(n\), let \(L\) denote its number of base-\(b\) digits, indexed \(0,1,\ldots,L-1\) from least to most significant. Distinct digit positions refer to canonical expansions, never to expansions padded with leading zeroes.

## Proof

**Case 1: \(L\le k\).** Write the digit polynomial of \(n\) as \(D(X)=\sum_{i=0}^{L-1}d_iX^i\). It satisfies \(D(X)=X^{L-1}D(X^{-1})\) since \(n\) is palindromic. Adding \(b^k\) creates a new top digit \(1\) without any carry, so the digit polynomial of \(m\) is \(X^k+D(X)\), of length \(k+1\). Palindromicity of \(m\), as a polynomial identity in \(X\), gives

\[
X^k+D(X)=X^k(X^{-k}+D(X^{-1}))=1+X^{k-L+1}D(X).
\]

Put \(a=k-L+1\), so \(1\le a\le k\). Rearranging,

\[
(X^a-1)D(X)=X^k-1.
\]

Dividing \(X^k-1\) by \(X^a-1\) leaves the remainder \(X^{k\bmod a}-1\). As \(0\le k\bmod a<a\), this remainder vanishes precisely when \(a\mid k\). Therefore \(D(X)=1+X^a+\cdots+X^{k-a}\), determining exactly one pair for each divisor \(a\) of \(k\). These polynomials have legitimate base-\(b\) digits, so every listed pair exists.

**Case 2: \(L\ge k+1\) and \(m\) has \(L\) digits.** Addition of \(b^k\) changes a consecutive interval of digit positions \(\{k,k+1,\ldots,t\}\), where \(t\le L-1\) is the first position at which the old digit is smaller than \(b-1\). For \(k\le i<t\), the old digit is \(b-1\) and changes to \(0\); the digit at \(t\) increases by \(1\). Every position in this interval changes, and no other digit changes. Since both \(n\) and \(m\) are palindromes of equal length, the set of changed positions must be invariant under reflection \(i\mapsto L-1-i\). For the interval this forces \(t=L-1-k\).

If \(t>k\), the old digit at \(k\) is \(b-1\). By palindrome symmetry the old digit at \(t=L-1-k\) is also \(b-1\), contradicting the choice of \(t\). Hence \(t=k\), and reflection invariance gives \(L=2k+1\). The central digit is at most \(b-2\), so adding \(b^k\) increments exactly that central digit. Conversely any palindrome with the stated central digit has precisely this behavior, proving the second family.

**Case 3: \(L\ge k+1\) and addition increases the digit length.** All old digits at positions \(k,\ldots,L-1\), including the leading digit, must equal \(b-1\). Thus the trailing digit of the palindrome \(n\) also equals \(b-1\). The positive carry creates a leading digit \(1\) in \(m\), while the trailing digit remains \(b-1\) because \(k\ge1\). Since \(b\ge3\), those two digits differ, so \(m\) cannot be palindromic. No pairs arise here.

These three cases cover every positive palindrome \(n\). The families are disjoint: in Case 1, \(n\) has at most \(k\) digits, whereas in Case 2 it has \(2k+1\). The divisor-spaced family has \(\tau(k)\) elements. A length-\(2k+1\) palindrome is determined by its first \(k\) digits (\(b-1\) possibilities for the leading digit, then \(b\) at each of the next \(k-1\) positions) and its middle digit (\(b-1\) allowed values). Hence the central-digit family has \((b-1)^2b^{k-1}\) elements. Summing gives the formula for all admissible \(b,k\). \(\square\)

## Verification

The supplied standalone `verify.py` constructs all positive base-\(b\) palindromes of lengths at most \(2k+1\), independently tests whether adding \(b^k\) gives a palindrome, and compares the resulting pair set with the explicit two-family construction. It also counts the pairs and checks the claimed expression using integer arithmetic. The tested grid comprises all \(3\le b\le6\), \(1\le k\le4\), plus \((b,k)=(3,5),(3,6),(7,1),(7,2),(7,3)\), totaling 21 instances and 13,287 matching pairs. Selected additional longer lengths were searched for forbidden pairs; none appeared. The output file `verification_output.txt` reproduces the observed counts and ends in `VERIFY_OK`.

These finite computations are not the proof for unbounded bases or exponents. The unrestricted proof is the three-case digit argument above, including the reason no larger lengths are possible.

## Relationship to prior work

Pongsriiam and Saito, *Palindromes and Antipalindromes in Short Intervals* (2023), Theorem 12, characterize which fixed gaps have infinitely many base-\(b\) palindromic representations. Their Theorem 12(ii) shows that gaps \(b^k\), for \(b\ge3\), have only finitely many representations; it does **not** give their number. Their Question 26 asks for bounds on finite representation counts. The present result evaluates the exact count and provides every pair for an infinite family of gaps in every nonbinary base.

Phunphayap and Pongsriiam, *A Complete Comparison for the Number of Palindromes in Different Bases* (2023), compare cumulative palindrome-counting functions across bases rather than counting ordered pairs separated by a prescribed difference; their main theorems do not imply this exact gap classification.

The binary case is deliberately not asserted: in base \(2\), length-increasing carries can yield extra families. The sharp base restriction is part of the theorem, not an incidental convention.

## Limitations

The formula concerns only gaps that are positive powers of the same base, not general finite gaps or the asymptotic aggregate posed in Question 26. It does not address the binary case. Matching finite computations do not constitute a proof for all parameters. A survey of indexed and inspected literature cannot exclude unpublished or unindexed equivalent results. No independent external audit has been performed.

## References

1. P. Pongsriiam and K. Saito, *Palindromes and Antipalindromes in Short Intervals*, Journal of Integer Sequences **26** (2023), Article 23.9.5, Theorem 12, Question 26, published December 11, 2023. https://cs.uwaterloo.ca/journals/JIS/VOL26/Saito/saito1.pdf
2. P. N. Phunphayap and P. Pongsriiam, *A Complete Comparison for the Number of Palindromes in Different Bases*, AIMS Mathematics **8** (2023), 9924–9932, DOI: 10.3934/math.2023502, published February 23, 2023. https://www.aimspress.com/aimspress-data/math/2023/4/PDF/math-08-04-502.pdf
