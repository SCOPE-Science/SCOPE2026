# Exact three-nonzero-digit reversal-product palindromes

## Finding
For every integer \(d\ge2\), every \(1\le j<d\), and all decimal digits \(a,b,c\in\{1,\ldots,9\}\), put
\[
A=a10^d+b10^j+c,\qquad A^{\mathrm{rev}}=c10^d+b10^{d-j}+a.
\]
Then the decimal integer \(AA^{\mathrm{rev}}\) is a palindrome **if and only if**
\[
a^2+b^2+c^2\le9.\]
Equivalently the ordered digits are exactly \((1,1,1)\), the three permutations of \((1,1,2)\), or the three permutations of \((1,2,2)\), irrespective of the interior position or number of intervening zeros. This is a classification in the three-nonzero-digit family only.

## Assumptions and scope
A decimal palindrome is an integer whose ordinary decimal digit string, without leading zeros, equals its reversal. The endpoints \(a,c\) and interior digit \(b\) are all nonzero. Reversing \(A\) exchanges \(a,c\) and replaces \(j\) by \(d-j\), without changing the product; hence it is enough to consider \(j=g\le d/2\), writing \(d=2g+h\) with integers \(g\ge1\), \(h\ge0\).

## Proof
**1. Symmetric uncarried product.** Formal multiplication gives coefficients at exponents
\[
(0,ac),\ (g,ab),\ (g+h,bc),\ (2g+h,S),\ (3g+h,bc),\ (3g+2h,ab),\ (4g+2h,ac),
\]
where \(S=a^2+b^2+c^2\); coefficients at coincident exponents are added. Thus the uncarried coefficient vector \((q_0,\ldots,q_{2d})\) is symmetric. Every coefficient is an inner product of two sublists of \((a,b,c)\) and its reversal. By Cauchy–Schwarz, \(0\le q_i\le S\), with equality \(q_d=S\). Consequently \(S\le9\) implies that no base-ten carries occur and the product is a palindrome with exactly \(2d+1\) digits.

**2. Any palindrome of length \(2d+1\) has no carries.** Let \(t_i\) be the nonnegative carry entering column \(i\), so \(t_0=0\), and let
\[
p_i=q_i+t_i-10t_{i+1}\quad(0\le i\le 2d)
\]
be the actual decimal digits. A product having \(2d+1\) digits has \(t_{2d+1}=0\). When it is palindromic, \(p_i=p_{2d-i}\). Induct from the two ends: assuming \(t_i=t_{2d+1-i}=0\), equality of the symmetric pair of digits and of \(q_i=q_{2d-i}\) yields \(-10t_{i+1}=t_{2d-i}\), so both carries are zero. Starting at \(i=0\) forces all carries to vanish. In particular \(S=q_d\le9\). Therefore an exception could only be a palindrome of the longer possible length \(2d+2\).

**3. Long palindromes with an interior gap of at least three.** At most \(27\) is carried into any position, because \(q_i\le S\le243\) and \(\lfloor(243+27)/10\rfloor=27\). Suppose \(g\ge3\). The coefficient immediately below the leading coefficient \(q_{2d}=ac\) occurs at distance at least three. Even when two terms coincide, their total is at most \(162\). The carry after this coefficient is at most \(18\), followed by two zero columns, giving carries at most \(1\) and then \(0\). Hence the leading two decimal digits of any \(2d+2\)-digit product are the two digits of \(ac\); the trailing two are likewise those of \(ac\), since the next positive coefficient above \(q_0=ac\) is at exponent at least three. Palindromicity would force the two-digit number \(ac\) to read identically backwards. Every positive two-digit decimal palindrome is divisible by \(11\), but no product of two digits from \(1\) through \(9\) is divisible by the prime \(11\). Contradiction.

**4. Long palindromes with \(g=2\) and \(h\ge1\).** The term at exponent \(2d-2\) has coefficient \(ab\le81\); the preceding column has coefficient at most \(bc\le81\). Whatever arrives from lower positions is at most \(27\), so the carry into \(2d-2\) is at most \(10\), the carry into \(2d-1\) is at most \(9\), and the carry into \(2d\) is zero. The bottom two digits still come from \(ac\) alone. The same impossible two-digit-palindrome obstruction excludes a longer palindrome.

**5. Long palindromes with \(g=1\), \(h\ge3\).** Now \(d=h+2\ge5\), and grouping disjoint blocks gives
\[
AA^{\mathrm{rev}}=U10^{2d-1}+W10^{d-1}+V,
\]
\[
U=a(10c+b),\qquad V=a(10b+c),\qquad W=101bc+10S.
\]
Here \(U,V\le891\) and \(W\le10611\); the blocks do not overlap in decimal positions. For a product to have \(2d+2\) digits requires \(U\ge100\). Its three leading digits are \(U\); its three trailing digits are \(V\) padded to width three. Thus a palindrome requires \(U\) to equal that padded string reversed. Exhausting \(a,b,c\in\{1,\ldots,9\}\) gives precisely \((a,b,c,U,V)=(7,8,8,616,616)\) and \((8,7,7,616,616)\). Their respective middle blocks are \(W=8234\) and \(W=6569\), whose middle two digits are unequal (respectively \(3\ne2\) and \(6\ne5\)); those two digits occupy the central positions of the full product. Neither product is palindromic.

**6. Remaining finite gaps.** The only unhandled parameter pairs are
\[
(g,h)\in\{(1,0),(1,1),(1,2),(2,0)\}.
\]
The attached standalone `check.py` exhausts every one of the \(4\cdot9^3=2916\) digit triples in these four cases by constructing \(A\) and its reversal as exact integers, multiplying, and testing whether a \(2d+2\)-digit result equals its decimal reversal. The count of such palindromes is zero in every case. The same script separately checks the complete \(9^3\)-entry three-digit boundary census in Step 5. These are exhaustive finite computations with explicit complete iteration ranges, not extrapolation from sample tests. Thus no palindrome has \(2d+2\) digits. Combining with Steps 1–2 proves the claimed equivalence for every \(d,j,a,b,c\). \(\square\)

## Verification
Run `python3 check.py` using only the Python standard library. The essential proof certificates are `SHORT_GAP_PROOF_CASES 2916`, `BOUNDARY_CENSUS_CASES 729`, and `PASS`. Independently, the script cross-checks multiplication against the full symmetric coefficient array for all \(40{,}824\) instances with \(1\le g\le7\), \(0\le h\le7\); all \(56\) gap cells have exactly seven successful digit triples. A further \(4{,}374\) wide-gap evaluations are diagnostic checks only. Neither finite grid is used to prove the infinite theorem; the six proof steps supply that reduction.

## Relationship to prior work
OEIS A062936 records palindrome-producing reversal products and identifies the low digit-square-sum construction. Ezerman, Meyer and Solé, *On Polynomial Pairs of Integers* (initial arXiv version October 29, 2012; Journal of Integer Sequences 18 (2015), Article 15.3.5), prove the carry-free construction and that a reversal-product palindrome of the expected \(2d+1\)-digit length must be carry free (their Proposition 14). They pose a more general converse problem (Conjecture 11). The remaining logically distinct obstruction in this three-sparse family is a palindrome of length \(2d+2\); Steps 3–6 exclude it uniformly. The present theorem neither claims to resolve their conjecture for four or more nonzero digits nor claims that the already known \(2d+1\)-digit argument is new.

## Limitations
Only ordinary base ten and exactly three nonzero digits are classified; there is no general claim for other bases, additional nonzero digits, or arbitrary palindromic factor pairs. The finite census is an exact standard-library executable argument but has not been independently audited. An unindexed equivalent formulation or subsequent strengthening in the literature is a residual priority risk.

## References
1. OEIS Foundation, A062936, decimal reverse-product palindromes, https://oeis.org/A062936 (early public sequence record, 2001).
2. M. F. Ezerman, B. Meyer and P. Solé, *On Polynomial Pairs of Integers*, arXiv:1210.7593 (first posted 2012-10-29), https://arxiv.org/abs/1210.7593 .
3. M. F. Ezerman, B. Meyer and P. Solé, *On Polynomial Pairs of Integers*, Journal of Integer Sequences 18 (2015), Article 15.3.5, especially Proposition 10, Conjecture 11, Proposition 14, https://cs.uwaterloo.ca/journals/JIS/VOL18/Ezerman/eze3.pdf .
