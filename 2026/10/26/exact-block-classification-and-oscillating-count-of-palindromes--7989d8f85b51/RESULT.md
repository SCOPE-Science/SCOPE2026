# Exact block classification and oscillating count of palindromes in a base and its power

## Finding

Fix integers \(b\ge2\) and \(k\ge2\). A positive integer is a base-\(b\) palindrome if its ordinary positional expansion, without leading zeros, reads identically in both directions. Put \(B=b^k\). For arbitrary \(m\ge1\) and \(1\le s\le k\), define \(L=k(m-1)+s\), so \(m\) is the base-\(B\) digit length and \(L\) the base-\(b\) digit length.

**Exact classification.** An \(L\)-digit integer is palindromic in both bases \(b\) and \(B\) if and only if its \(m\) successive base-\(B\) digits form a palindrome, each of those digits is below \(b^s\), and the ordinary \(s\)-digit base-\(b\) expansion of each digit (with zero padding permitted) is itself a palindrome. The outermost block has nonzero leading digit. Thus the simultaneous palindromes are precisely palindromes of short palindromic blocks, with a forced zero suffix of length \(k-s\) in every padded block.

Their exact count with this base-\(b\) length is
\[
F_{b,k}(m,s)=(b-1)b^{\lfloor(s-1)/2\rfloor+\lceil s/2\rceil(\lceil m/2\rceil-1)}.
\]
Writing \(A_s=(b-1)b^{\lfloor(s-1)/2\rfloor}\), \(a_s=\lceil s/2\rceil\), their complete block-length generating function is the rational function
\[
\sum_{m\ge1}\left(\sum_{s=1}^k F_{b,k}(m,s)\right)z^m
=\sum_{s=1}^k A_s\frac{z+z^2}{1-b^{a_s}z^2}.
\]

Let \(N_{b,k}(X)\) count positive integers \(n<X\) palindromic in both bases. For any \(M\ge1\),
\[
N_{b,k}(b^{kM})=\sum_{m=1}^M\sum_{s=1}^kF_{b,k}(m,s).
\]
For \(R\ge1\), the even and odd cutoffs have the *exact* formulas
\[
N_{b,k}(b^{2kR})=2\sum_{s=1}^k A_s\frac{b^{a_sR}-1}{b^{a_s}-1},
\]
\[
N_{b,k}(b^{k(2R+1)})=2\sum_{s=1}^k A_s\frac{b^{a_sR}-1}{b^{a_s}-1}+\sum_{s=1}^k A_sb^{a_sR}.
\]
The odd formula also holds for \(R=0\), interpreting its first sum as zero.

Put \(c=\lceil k/2\rceil\), \(\alpha=c/(2k)\), and \(W=\sum_{1\le s\le k:\,a_s=c}A_s\). Then
\[
N_{b,k}(X)=\Theta_{b,k}(X^{\alpha}),\qquad
\lim_{X\to\infty}\frac{\log N_{b,k}(X)}{\log X}=\alpha,
\]
with \(\alpha=1/4\) for even \(k\) and \(\alpha=(k+1)/(4k)\) for odd \(k\). Moreover
\[
\lim_{R\to\infty}\frac{N_{b,k}(b^{2kR})}{(b^{2kR})^\alpha}=\frac{2W}{b^c-1},
\qquad
\lim_{R\to\infty}\frac{N_{b,k}(b^{k(2R+1)})}{(b^{k(2R+1)})^\alpha}=\frac{W(b^c+1)}{(b^c-1)b^{c/2}}.
\]
Because the second constant is strictly larger, \(N_{b,k}(X)\) admits **no** asymptotic of the form \(C X^\alpha\) with fixed positive \(C\).

## Assumptions and scope

Both bases are fixed integral powers \(b\) and \(b^k\); \(b\ge2\), \(k\ge2\), with no relative primality or digit-length conditions beyond those stated. All integers are positive, and standard positional expansions have no leading zeros. The cutoff function uses \(n<X\), hence a value at an integral power counts all shorter base-\(B\) lengths. Every displayed count is exact for every permitted integer parameter. The \(\Theta\) constants may depend on fixed \(b,k\). The statements do not concern multiplicatively independent bases.

## Proof

**1. Digit-coordinate lemma.** Write the unique padded base-\(b\) array as \(d_{j,c}\) with \(0\le j<m\) indicating the base-\(B\) block from the least significant end and \(0\le c<k\) the base-\(b\) digit within that block, also from the least significant end. The base-\(b\) digit at exponent \(jk+c\) is \(d_{j,c}\). As the true base-\(b\) length is \(L=k(m-1)+s\), the top block has \(d_{m-1,c}=0\) for \(s\le c<k\), and \(d_{m-1,s-1}\ne0\). Base-\(B\) palindromicity means
\[
d_{j,c}=d_{m-1-j,c}\qquad(0\le j<m,\ 0\le c<k).
\]
In particular, \(d_{0,c}=0\) for all \(c\ge s\).

Suppose base-\(b\) palindromicity also holds. For \(0\le j\le m-2\) and \(s\le c<k\), the reflected position of \(jk+c\) among the \(L\) significant digits is
\[
L-1-(jk+c)=(m-2-j)k+(k+s-1-c).
\]
The reflected column \(c'=k+s-1-c\) again lies in \([s,k-1]\). Using base-\(B\) block reversal to send block \(m-2-j\) to block \(j+1\) gives
\[
d_{j,c}=d_{j+1,c'}.
\]
The high columns in block zero vanish, so induction on \(j\) proves \(d_{j,c}=0\) for all blocks and all \(c\ge s\). This induction is empty when \(m=1\), for which the same conclusion follows from the padding of the only block.

For \(0\le c<s\) and any \(0\le j<m\), reflection instead takes exponent \(jk+c\) to \((m-1-j)k+(s-1-c)\). Again applying block reversal yields
\[
d_{j,c}=d_{j,s-1-c},
\]
so each short \(s\)-digit block is individually palindromic. Conversely, if all high columns vanish, the short blocks are palindromes and the blocks occur in palindromic order, then both digit-reversal equalities hold at each significant position, proving the classification, including the leading-zero boundary.

**2. Exact enumeration.** There are exactly \((b-1)b^{\lfloor(s-1)/2\rfloor}=A_s\) palindromic \(s\)-digit strings with nonzero leading digit, and \(b^{\lceil s/2\rceil}=b^{a_s}\) palindromic \(s\)-digit strings when leading zeros are allowed. Block reversal leaves \(\lceil m/2\rceil\) independently chosen blocks; one outer independent block must be nonzero. Multiplying choices gives the asserted \(F_{b,k}(m,s)\). As \(\lceil m/2\rceil-1\) takes each nonnegative value twice, the geometric-series generating function follows. Summing over the unique length pairs \((m,s)\) proves the two finite-cutoff formulas.

**3. Growth and oscillation.** Let \(c=\max_s a_s\). Only \(s\) with \(a_s=c\) contribute to the leading exponential order of the exact even/odd cutoff formulas. Divide each of the two formulas by \(b^{cR}\), and note that all terms having \(a_s<c\) vanish as \(R\to\infty\). Taking account of the extra factor \(b^{c/2}\) in the normalization of odd cutoffs gives the two displayed constants. Their ratio is
\[
\frac{b^c+1}{2b^{c/2}}>1,
\]
by strict arithmetic-geometric mean since \(b^c>1\). This proves failure of a single normalized leading constant. The exact cutoff counts have order \(b^{cM/2}\). For any real large \(X\), choose \(M\) with \(b^{kM}\le X<b^{k(M+1)}\); monotonicity of \(N_{b,k}\) sandwiches it between adjacent cutoff counts. Since those endpoints differ by a bounded fixed factor, \(N_{b,k}(X)=\Theta_{b,k}(X^{c/(2k)})\), proving the logarithmic exponent. Finally, \(\lceil k/2\rceil/(2k)\) simplifies to the stated parity-dependent values.

## Verification

The included standalone standard-library program `verify.py` directly computes base expansions and digit reversals rather than using the theorem as its oracle. For each affordable combination among \(b\in\{2,3,4\}\), \(2\le k\le5\), \(1\le m\le5\), and \(1\le s\le k\), it enumerates every integer in the corresponding exact base-\(b\) digit-length bin, checks the structural equivalence and the explicit count, and where affordable cross-checks the cumulative power-of-base cutoff. Its successful replay produced `VERIFY_OK: 134 exact length bins and 1148558 direct integer tests`. These checks do not replace the proof for unbounded lengths or bases.

For example, at \((b,k)=(2,2)\), the exact formulas simplify to
\[
N_{2,2}(2^{4R})=4(2^R-1),\qquad
N_{2,2}(2^{4R+2})=6\cdot2^R-4.
\]
The corresponding normalized limits are \(4\) and \(3\sqrt2\), respectively.

## Relationship to prior work

Bérczes and Ziegler [1] study simultaneous palindromes in distinct bases. In their introduction, page 2, they explicitly note that when one base is a power of the other, simultaneous palindromes exist infinitely often, giving elementary examples. Their main theorems impose multiplicative independence and do not derive the complete dependent-base block classification, exact digit-length counts, rational generating function, or oscillating asymptotic cutoff constants proved here. Thus infinitude is previously known and is not claimed as a new result.

Bašić [2], especially its abstract, introduction and Section 2, constructs integers palindromic in arbitrarily many selectable bases and studies prescribed digit patterns; those quantifiers do not yield an exact count for one *fixed* pair \((b,b^k)\). Phunphayap and Pongsriiam [3] compare two marginal base-palindrome counting functions; subtracting marginal totals does not determine the cardinality of their intersection. These are different statement-level implications, rather than merely different titles.

## Limitations

The fixed-base, fixed-power characterization does not decide simultaneous palindromicity for multiplicatively independent bases or non-integral relations between bases. The error term beyond the two explicit subsequential limits, the detailed oscillation profile at arbitrary real cutoffs, and any distributional arithmetic restrictions on the simultaneously palindromic numbers are not determined. A mathematically equivalent formula in further digit-combinatorics literature could have escaped the targeted searches; independent review has not been conducted.

## References

[1] A. Bérczes and V. Ziegler, *On Simultaneous Palindromes*, arXiv:1403.0787 (first public version March 4, 2014), https://arxiv.org/abs/1403.0787 ; full text https://arxiv.org/pdf/1403.0787 .

[2] B. Bašić, *On “very palindromic” sequences*, Journal of the Korean Mathematical Society 52 (2015), 765–780, DOI:10.4134/JKMS.2015.52.4.765 ; author manuscript https://people.dmi.uns.ac.rs/~bojan.basic/papers/multpal.pdf .

[3] P. N. Phunphayap and P. Pongsriiam, *A complete comparison for the number of palindromes in different bases*, AIMS Mathematics 8 (2023), 9924–9932, DOI:10.3934/math.2023502, https://www.aimspress.com/article/doi/10.3934/math.2023502 .
