# Exact digit classification and counting of palindromes in every dependent base pair

## Finding
Fix integers \(b\ge2\) and \(k\ge2\). Let \(P_{b,k}(L)\) be the number of positive integers with exactly \(L\) digits in base \(b\) whose canonical base-\(b\) and base-\(b^k\) expansions are both palindromes. Define \(K=\lceil k/2\rceil\). For every \(q\ge1\),
\[
P_{b,k}(kq)=(b-1)b^{K\lceil q/2\rceil-1}.
\]
For every \(q\ge0\) and \(1\le r<k\), setting \(R_r=\lceil r/2\rceil\),
\[
P_{b,k}(kq+r)=(b-1)b^{R_r\lceil(q+1)/2\rceil-1}.
\]
In particular, for fixed \(b,k\), the exact ordinary generating function is
\[
\sum_{L\ge1}P_{b,k}(L)z^L
=(b-1)\left[\frac{b^{K-1}(z^k+z^{2k})}{1-b^Kz^{2k}}
+(1+z^k)\sum_{r=1}^{k-1}\frac{b^{R_r-1}z^r}{1-b^{R_r}z^{2k}}\right].
\]
Writing \(N_{b,k}(X)\) for the number of such positive integers not exceeding \(X\),
\[
N_{b,k}(X)=\Theta_{b,k}\bigl(X^{\lceil k/2\rceil/(2k)}\bigr)
\qquad(X\longrightarrow\infty).
\]
The power is exactly \(1/4\) for even \(k\) and \((k+1)/(4k)\) for odd \(k\).

## Assumptions and scope
All expansions are canonical, with no leading zero, except for internal fixed-width blocks, which may start with zero. For a digit word \(W\), write \(W^{\mathrm{rev}}\) for its digitwise reversal. A \(d\)-digit word is a palindrome precisely when \(W=W^{\mathrm{rev}}\). The symbol \(0^t\) denotes a word of \(t\) zero digits, including the empty word when \(t=0\). The count is for positive integers; the integer zero is not included.

Here is the complete constructive characterization of the counted integers. If \(L=kq\) with \(q\ge1\), split the base-\(b\) word into \(q\) consecutive blocks of width \(k\). The integer is counted if and only if every block is a palindrome and the ordered sequence of blocks is itself palindromic (with the leading digit nonzero). If \(L=kq+r\) with \(1\le r<k\), the word is counted if and only if it has the form
\[
A_0\,0^{k-r}A_1\,0^{k-r}A_2\,\cdots\,0^{k-r}A_q,
\]
where every \(A_i\) is a palindrome of width \(r\), the ordered list \((A_0,\ldots,A_q)\) is palindromic, and the first digit of \(A_0\) is nonzero. No restriction is imposed on the first digit of \(A_i\) for \(i>0\). For \(q=0\), this form consists solely of \(A_0\).

## Proof
**Full blocks.** Suppose \(L=kq\). The canonical base-\(b^k\) expansion is exactly the list \(B_1,\ldots,B_q\) of fixed-width \(k\)-digit blocks regarded as digit values. Being palindromic in base \(b^k\) means \(B_i=B_{q+1-i}\). Reversing the full base-\(b\) word both reverses the block order and reverses the digits inside each block; with the first condition, base-\(b\) palindromicity is equivalent to \(B_i=B_i^{\mathrm{rev}}\) for every \(i\). There are \(\lceil q/2\rceil\) independent palindromic blocks, each having \(K=\lceil k/2\rceil\) freely chosen digit positions. The first position is nonzero, so there are exactly \((b-1)b^{K\lceil q/2\rceil-1}\) words.

**Partial leading block.** Suppose \(L=kq+r\), with \(1\le r<k\). Write the word as a first block \(A_0\) of width \(r\) followed by \(q\) blocks \(B_1,\ldots,B_q\) of width \(k\). For \(q=0\), the base-\(b^k\) expansion has one digit, so the simultaneous-palindrome condition says exactly that \(A_0\) is a palindrome. Its count is \((b-1)b^{R_r-1}\), as required.

Take \(q\ge1\). Palindromicity of the base-\(b^k\) digit sequence means (as **values**) that \(B_q=0^{k-r}A_0\) and \(B_i=B_{q-i}\) for \(1\le i<q\). The suffix of length \(k\) is therefore \(0^{k-r}A_0\), whereas the prefix of length \(k\) is \(A_0C\), where \(C\) denotes the first \(k-r\) digits of \(B_1\). Equality of the prefix and reversed suffix in the base-\(b\) palindrome yields \(A_0=A_0^{\mathrm{rev}}\) and \(C=0^{k-r}\); hence \(B_1=0^{k-r}A_1\) for some width-\(r\) word \(A_1\). For \(q=1\) this already gives \(A_1=A_0\).

For \(q\ge2\), the base-\(b^k\) condition also gives \(B_{q-1}=B_1=0^{k-r}A_1\). Strip \(k\) base-\(b\) digit positions from each end of the complete base-\(b\) palindrome. The remaining word is \(A_1B_2\cdots B_{q-1}\), and it is palindromic as a word. Further, its fixed-width value list \((A_1,B_2,\ldots,B_{q-1})\) is palindromic, since it is obtained from the original palindromic value list by deleting its endpoints, then replacing the first padded width-\(k\) block \(0^{k-r}A_1\) by its width-\(r\) value representation. Therefore the same reasoning applies recursively with \(q\) replaced by \(q-2\). This recursion is on digit words with fixed-width blocks; intermediate payloads may start with zero and do not need to be canonical whole-number expansions. Induction proves that all \(B_i\) are \(0^{k-r}A_i\), each \(A_i\) is a palindrome, and \((A_0,\ldots,A_q)\) is a palindrome. Conversely, the displayed structure clearly is a base-\(b\) palindrome and its base-\(b^k\) values \((A_0,\ldots,A_q)\) form a palindrome. This proves necessity and sufficiency, including the zero-padding boundary.

There are \(\lceil(q+1)/2\rceil\) independent payloads, each with \(R_r\) independent digits. The leading payload is nonzero in its first digit, whereas every other free digit is arbitrary. This gives the stated formula \((b-1)b^{R_r\lceil(q+1)/2\rceil-1}\).

**Generating function.** In the full-block case, lengths \(k(2m+1)\) and \(k(2m+2)\) have the same count \((b-1)b^{K(m+1)-1}\), for \(m\ge0\). In the partial-block case at fixed \(r\), lengths \(2km+r\) and \(k(2m+1)+r\) have the same count \((b-1)b^{R_r(m+1)-1}\). Summing these geometric pairs over \(m\ge0\) gives the rational expression.

**Cumulative exponent.** For each \(1\le r<k\), \(R_r\le K\). Hence every length-\(L\) count is at most \(C_{b,k}b^{KL/(2k)}\), uniformly over residue classes of \(L\). The sum over \(L\le\lfloor\log_b X\rfloor+1\) is therefore \(O_{b,k}(X^{K/(2k)})\). Conversely, for sufficiently large \(X\), choose the largest multiple-of-\(2k\) digit length \(L\le\lfloor\log_b X\rfloor\); every counted integer of that length lies below \(X\), and the full-block formula yields at least \(c_{b,k}X^{K/(2k)}\) of them. This proves the claimed two-sided order of growth, without asserting an asymptotic constant.

## Verification
The accompanying standalone checker `verify_palindromes.py` calculates base expansions arithmetically and independently compares simultaneous numeral palindromicity with the structural characterization and length formulas. Its finite enumeration covers bases \(2\) and \(3\), exponents \(2\) through \(7\), and digit lengths through \(14\) or \(9\), respectively. A separate equality-constraint union/find calculation checks the predicted independent digit dimension for exponents \(2\) through \(17\) and all lengths through \(14k\). Run `python3 verify_palindromes.py`. Expected output: `VERIFY_OK numeric_profiles=138 tested_integers=216390 accepted=632 symbolic_profiles=2128`. These checks support the proof but are not a substitute for it.

## Relationship to prior work
Bérczes and Ziegler, *On Simultaneous Palindromes* (first public preprint 4 March 2014), study integers palindromic in two bases and explicitly set aside pairs where one base is a perfect power of the other because infinite elementary families already exist. Their full text does not provide the complete digit-word classification, exact length-by-length count, or generating function for all power-related pairs given here. The present statement quantifies this separate infinite regime rather than extending their multiplicatively independent-base finiteness theorems. Work on integers palindromic in many bases and lists of special simultaneous palindromes involves distinct quantifiers or restricted integer subclasses. The cubic-power specialization is subsumed by the general \(k\)-parameter statement and is not asserted to be a separately new case. Bašić's Theorem 1 gives a constructive zero-padding family for several varying bases, but neither a fixed-pair characterization nor exact enumeration; the present theorem captures every allowable padded-block pattern.

## Limitations
This theorem treats exactly the integer-power pairs \((b,b^k)\), not arbitrary multiplicatively dependent powers such as \((b^u,b^v)\) with neither exponent dividing the other, and it does not treat multiplicatively independent bases. The count concerns all positive integers, not prime or other restricted subclasses. The cumulative result establishes \(\Theta\)-order only, not the existence of one normalized leading constant. Database and bibliographic searches cannot exclude every earlier, unindexed or folklore statement of this elementary characterization.

## References
1. A. Bérczes and V. Ziegler, *On Simultaneous Palindromes*, arXiv:1403.0787v1 (first submitted 4 March 2014); *Journal of Combinatorics and Number Theory* **6** (2014), 37–49. https://arxiv.org/abs/1403.0787 .
2. B. Bašić, *On very palindromic sequences*, *Journal of the Korean Mathematical Society* **52** (2015), 765–780, doi:10.4134/JKMS.2015.52.4.765 (related many-base question; original full text consulted; its theorems concern existence of many-base representations).
3. OEIS A056145, primes that are palindromic in bases \(2\) and \(8\), https://oeis.org/A056145 (a restricted integer family, not a general length classification).
