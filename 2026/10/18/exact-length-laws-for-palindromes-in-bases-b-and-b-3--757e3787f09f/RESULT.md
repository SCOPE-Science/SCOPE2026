# Exact length laws for palindromes in bases \(b\) and \(b^3\)

## Finding
For each integer base \(b\ge2\), let \(P_b(L)\) count positive integers with exactly \(L\) digits in base \(b\) whose *standard* expansions are palindromes both in base \(b\) and in base \(b^3\). The complete count, valid for all lengths, is
\[
P_b(3q)=(b-1)b^{2\lceil q/2\rceil-1}\quad(q\ge1),
\]
\[
P_b(3q+1)=P_b(3q+2)=(b-1)b^{\lfloor q/2\rfloor}\quad(q\ge0).
\]
More strongly, every such expansion has one of three explicit forms, with free digit letters chosen from \(\{0,\ldots,b-1\}\) and its first letter nonzero:

1. At length \(3q\), a palindromic list of \(q\) three-digit blocks, each block itself palindromic. The first block has shape \((a,c,a)\) with \(a\ne0\).
2. At length \(3q+1\), a palindromic list of \(q+1\) letters, successive letters separated by exactly two zero digits: \(a_0,0,0,a_1,0,0,\ldots,0,0,a_q\).
3. At length \(3q+2\), a palindromic list of \(q+1\) letters, each letter doubled and successive pairs separated by exactly one zero digit: \(a_0,a_0,0,a_1,a_1,0,\ldots,0,a_q,a_q\).

The ordinary generating function is the rational function
\[
\sum_{L\ge1}P_b(L)z^L=(b-1)\left(\frac{(z+z^2)(1+z^3)}{1-bz^6}+\frac{b(z^3+z^6)}{1-b^2z^6}\right).
\]
Consequently, for fixed \(b\), the number of integers at most \(X\) that are palindromic in both bases is \(\Theta_b(X^{1/3})\). The length layers have two distinct growth regimes: the multiples-of-three layers have order \(b^{L/3}\) and the other layers have order \(b^{L/6}\), up to constants depending on \(b\).

## Assumptions and scope
All numbers are positive integers with no leading zero in either standard positional expansion. Digits of a base-\(b^3\) number are grouped from the *right* into three base-\(b\) digits, so only its first block can have fewer than three digits. A short leading block is compared by *numeric value*, thus leading zeros in its corresponding rightmost three-digit block are required. No primality, coprimality, or unproved hypothesis is assumed.

## Proof
Write the base-\(b\) digits of a candidate as \(x_0,x_1,\ldots,x_{L-1}\) from most to least significant, with \(x_0\ne0\) and \(x_i=x_{L-1-i}\) by the first palindrome condition. The second condition says that the consecutive right-aligned three-digit blocks, viewed as base-\(b^3\) digits, are palindromic.

**Case \(L=3q\).** There are \(q\) full three-digit blocks. The base-\(b^3\) palindrome equates block \(j\) to block \(q-1-j\), while the base-\(b\) palindrome equates block \(j\) to the digitwise reversal of block \(q-1-j\). Thus every block equals its reversal, and the list of blocks itself is palindromic. Conversely these conditions clearly imply both palindromes. There are \(\lceil q/2\rceil\) independent block orbits, each specified by two digits, with the first of these \(2\lceil q/2\rceil\) digits nonzero. Hence the claimed count for this case.

**Case \(L=3q+1\).** For \(q=0\) there is only one nonzero digit. For \(q\ge1\), the leading base-\(b^3\) digit is \(x_0\). Its equal rightmost base-\(b^3\) digit is therefore the full triple \((0,0,x_0)\). Because the entire base-\(b\) string is also palindromic, \(x_1=x_2=0\). For each pair of nonterminal full blocks indexed by \(0\le j\le q-2\), first equate the blocks using the base-\(b^3\) palindrome, then reverse the partnered block using the base-\(b\) palindrome. Comparing the three digits gives
\[
x_{3j+1}=x_{3j+5},\qquad x_{3j+2}=x_{3j+4}.
\]
Starting from \(x_1=x_2=0\) and applying these equalities in increasing \(j\), all digits with indices congruent to \(1\) or \(2\) modulo \(3\) vanish. The surviving letters \(x_0,x_3,\ldots,x_{3q}\) form a palindrome by the original base-\(b\) reversal. Conversely a string with this displayed pattern is a base-\(b\) palindrome, and its base-\(b^3\) expansion is precisely the palindromic letter list \((a_0,a_1,\ldots,a_q)\). The number of free letters is \(\lceil(q+1)/2\rceil=\lfloor q/2\rfloor+1\), the first nonzero, proving the count.

**Case \(L=3q+2\).** For \(q=0\), a two-digit base-\(b\) palindrome is \((a,a)\), and it is automatically one base-\(b^3\) digit. For \(q\ge1\), the leading base-\(b^3\) digit has value \(bx_0+x_1\), so the equal rightmost three-digit block must be \((0,x_0,x_1)\). The whole-word reversal yields \(x_0=x_1\) and \(x_2=0\). As in the previous case, compare each of the \(q-1\) pairs of nonterminal full blocks with its reversed counterpart. For \(0\le j\le q-2\), the resulting equalities are
\[
x_{3j+2}=x_{3j+5},\qquad x_{3j+3}=x_{3j+4}.
\]
Induction gives \(x_{3j+2}=0\) for \(0\le j\le q-1\), and \(x_{3j}=x_{3j+1}\) for \(0\le j\le q\), with the final doubled pair supplied also by whole-word reversal. These \(q+1\) pair digits form a palindrome. Conversely any such string is palindromic in base \(b\); the base-\(b^3\) digits have equal mirror values because the initial pair \((a_0,a_0)\) and final triple \((0,a_q,a_q)\) have equal numeric value, and all intermediate triples take form \((0,a_j,a_j)\). Again \(\lfloor q/2\rfloor+1\) letters are free and the first nonzero.

The rational generating function follows by separating the even and odd values of \(q\) in the three formulas. Finally, if \(b^{M-1}\le X<b^M\), summing the formulas through \(L=M\) gives \(O_b(b^{M/3})\). For the converse, choose the largest multiple of three \(L\le M-1\); then every \(L\)-digit candidate is at most \(X\), and its layer has \(\gg_b b^{L/3}\) elements. Since \(L=M-O(1)\), both bounds are constant multiples of \(X^{1/3}\). This proves the growth statement.

## Verification
The separate, standard-library Python program `CHECK.py` independently enumerates all base-\(b\) palindromes of chosen lengths, converts each integer to base \(b^3\), checks reversal directly, and compares the result *as a set* to the three structural constructions above. It additionally checks all exact cardinality formulas. The verified profiles are \(1\le L\le20\) for \(b=2\), \(1\le L\le14\) for \(b=3\), \(1\le L\le11\) for \(b=4\), and \(1\le L\le9\) for \(b=5\): 54 base-length profiles in total. Run `python3 CHECK.py`. The finite test is corroboration, not the basis of the unrestricted proof.

## Relationship to prior work
Bérczes and Ziegler, *On Simultaneous Palindromes* (arXiv:1403.0787, first submitted March 4, 2014), study integers palindromic in two bases; their Introduction explicitly sets aside pairs with one base a perfect power of the other, noting elementary infinite families, while their theorems use multiplicative independence. The present exact digit-length classification treats the particular dependent pair \((b,b^3)\) quantitatively, a statement not supplied by their theorems. OEIS A056145 tabulates *primes* palindromic in bases two and eight, not all simultaneous palindromes or their length counts. Phunphayap and Pongsriiam, *A complete comparison for the number of palindromes in different bases* (2023), investigate differences between the *separate* palindrome counting functions; that comparison does not by itself determine their intersection.

## Limitations
The theorem applies exactly to base pairs \((b,b^3)\) and does not classify general multiplicatively dependent pairs \((b,b^k)\), independent bases, or primes inside the simultaneous-palindrome family. The exact enumeration is proved by elementary positional constraints; no claim of difficulty comparable to the multiplicatively independent case is made. A logically equivalent formula in less-indexed literature has not been ruled out.

## References
1. A. Bérczes and V. Ziegler, *On Simultaneous Palindromes*, arXiv:1403.0787 (first posted 2014-03-04), https://arxiv.org/abs/1403.0787 and https://arxiv.org/html/1403.0787v2.
2. OEIS A056145, *Palindromic primes in bases 2 and 8*, https://oeis.org/A056145 (accessed 2026-10-14).
3. P. N. Phunphayap and P. Pongsriiam, *A complete comparison for the number of palindromes in different bases*, AIMS Mathematics 8 (2023), 9924–9932, https://doi.org/10.3934/math.2023502 (abstract and bibliographic record consulted).
