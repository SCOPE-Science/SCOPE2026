# Exact shell census and density oscillation in the binary–quaternary palindrome race

## Finding

For each base \(b\ge2\), let \(A_b(n)\) be the number of **positive** palindromic integers in base \(b\) up to and including \(n\), and write \(D(n)=A_2(n)-A_4(n)\). Fix any integer \(h\ge1\) and abbreviate \(B=4^h\), \(q=2^h\), \(X=16^h=B^2\).

Count integers \(X\le n<16X\) for which \(D(n)\) is positive, negative or zero, denoting the counts by \(P_h,N_h,Z_h\), respectively. Then

\[
P_h=\frac{39B^2}{56}+1-\frac{q}{14},\qquad
N_h=\frac{375B^2}{56}-3B-1-\frac{q}{14},\qquad
Z_h=\frac{213B^2}{28}+3B+\frac q7.
\]

More precisely, the sign census on each of four consecutive intervals is:

| Interval for \(n\) | \(D(n)>0\) | \(D(n)<0\) | \(D(n)=0\) |
|:--|--:|--:|--:|
| \([X,2X)\) | \((B^2-4B)/8\) | \((B^2+4B)/8\) | \(3B^2/4\) |
| \([2X,4X)\) | \(1\) | \(2B^2-B-2\) | \(B+1\) |
| \([4X,8X)\) | \(0\) | \(4B^2-2B+1\) | \(2B-1\) |
| \([8X,16X)\) | \((8B^2+7B-q)/14\) | \((8B^2-7B-q)/14\) | \((48B^2+q)/7\) |

As a consequence, \(\{n\ge1:D(n)>0\}\) has **no natural density**. Specifically, writing \(H(Y)=\#\{1\le n\le Y:D(n)>0\}\),
\[
\lim_{h\to\infty}\frac{H(16^h)}{16^h}=\frac{13}{280},\quad
\lim_{h\to\infty}\frac{H(2\cdot16^h)}{2\cdot16^h}=\frac3{35},\quad
\lim_{h\to\infty}\frac{H(8\cdot16^h)}{8\cdot16^h}=\frac3{140}.
\]

## Assumptions and scope

All counts exclude \(0\) as a palindrome, although including it in both bases leaves \(D(n)\) unchanged. Each interval is half-open and counts **integer** values of \(n\), not distinct palindrome events. Define \(\operatorname{rev}_{b,m}(t)\) as reversal of the length-\(m\) base-\(b\) numeral of \(t\), padding leading zeros before reversing. We use no unproved hypothesis on primes. The explicit formulas concern \(h\ge1\). The density conclusion is specifically for the positive-race set; no global limsup or liminf is asserted.

## Proof

**Block principle.** If a block of \(L\) consecutive integers starts with \(D=0\), contains one binary and one quaternary palindrome at offsets \(u_2,u_4\in[0,L)\), and ends with \(D=0\), then exactly \((u_4-u_2)_+\) locations have \(D>0\), \((u_2-u_4)_+\) have \(D<0\), and all others are ties. Similarly the initial value of \(D\), together with the ordered palindrome positions, determines its entire sign profile in blocks containing unequal numbers of palindrome events.

**Boundary counts.** The standard count of positive palindromes with fewer than \(k+1\) digits in base \(b\) is \(b^{\lceil k/2\rceil}+b^{\lfloor k/2\rfloor}-2\). Substituting the relevant digit lengths gives \(D(X)=0\), \(D(2X)=0\), \(D(4X)=-B\), \(D(8X)=0\), \(D(16X)=0\). The same equalities hold immediately before each boundary when the boundary itself is not palindromic; this is the case at these powers for \(h\ge1\).

**First interval.** Partition \([X,2X)\) into length-\(B\) blocks \([aB,(a+1)B)\), where \(a=B+t\) and \(0\le t<B\). Each contains one binary and one quaternary palindrome, with offsets
\[
u_2=\operatorname{rev}_{2,2h}(\lfloor a/2\rfloor),\quad
u_4=\operatorname{rev}_{4,h}(\lfloor a/4\rfloor).
\]
Writing \(t=\sum_{j=0}^{h-1}d_j4^j\) and \(e_j=\lfloor d_j/2\rfloor\), elementary paired-bit reversal gives
\[
u_2-u_4=\frac B2e_0-6\sum_{j=1}^{h-1}4^{h-j-1}e_j.\]
The tail has size at most \((B-4)/12\) before multiplication by \(6\); hence the sign is positive exactly when \(e_0=1\), zero only when all \(e_j=0\), and otherwise negative. Each vector of \(h\) bits \((e_j)\) comes from exactly \(2^h\) digit strings \((d_j)\). Summing the positive and negative parts of the identity over the bits yields \(\sum(u_4-u_2)_+=(B^2-4B)/8\) and \(\sum(u_2-u_4)_+=(B^2+4B)/8\). The remaining \(3B^2/4\) positions are ties.

**Second interval.** Split \([2X,4X)\) into blocks \([2aB,2(a+1)B)\), \(B\le a<2B\). Each contains one even-length binary palindrome and two odd-length base-four palindromes; the starting values of \(D\) are \(0,-1,\ldots,-(B-1)\). In the first block, the binary palindrome is at offset \(1\), before the two quaternary palindromes at offsets \(2\) and \(B+2\); hence it contributes one positive position and \(B+1\) ties. In the second block, the quaternary event precedes the binary event, so there is no tie. All remaining blocks start at most \(-2\), making ties impossible. This proves the second row of the table.

**Third interval.** Partition \([4X,8X)\) into blocks \([4aB,4(a+1)B)\), \(B\le a<2B\). There are two odd-length binary palindromes and one even-length quaternary palindrome per block, so starting values rise through \(-B,-B+1,\ldots,-1\). None can become positive. Blocks before the last two start at most \(-3\). In the penultimate block the quaternary palindrome (offset \(3B-3\)) precedes the second binary palindrome (offset \(3B-1\)), preventing a tie. In the final block the first binary palindrome is at offset \(2B-1\), the base-four palindrome at \(4B-3\), and the last binary palindrome at \(4B-1\). Exactly \(2B-1\) values are tied: the \(2B-2\) positions from the first binary event through just before the base-four event, and the last position. This proves the third row.

**Fourth interval.** Split \([8X,16X)\) into \(2B\) blocks \([4aB,4(a+1)B)\), \(2B\le a<4B\). Each contains one even-length binary and one even-length quaternary palindrome, with respective offsets \(u_2=\operatorname{rev}_{2,2h+2}(a)\), \(u_4=\operatorname{rev}_{4,h+1}(a)\). In base four the binary reversal is base-four reversal followed by swapping the two bits within every digit. Let \(\rho\) be the involution \(\rho(0)=0,\rho(1)=2,\rho(2)=1,\rho(3)=3\). Writing \(a=\sum_{j=0}^h d_j4^j\), with \(d_h\in\{2,3\}\), we obtain
\[
\Delta(a):=u_2-u_4=\sum_{j=0}^h\bigl(\rho(d_j)-d_j\bigr)4^{h-j}.
\]
For lower digits the coefficient is \(0,1,-1,0\) as \(d_j\) runs through \(0,1,2,3\), while the leading digit contributes \(-1\) or \(0\). Thus \(\sum_a\Delta(a)=-B\). Set
\[
T_h=\sum_{d_0,\ldots,d_{h-1}}\left|\sum_{j=0}^{h-1}(\rho(d_j)-d_j)4^{h-1-j}\right|.
\]
The first nonzero signed base-four digit dominates the remaining tail. Therefore \(T_0=0\) and \(T_h=2\cdot16^{h-1}+2T_{h-1}\), giving \(T_h=(16^h-2^h)/7=(B^2-q)/7\). Combining the two possible leading digits, symmetry under swapping digits \(1\leftrightarrow2\), and the \(2^h\) choices where every signed lower digit vanishes, gives \(\sum_a|\Delta(a)|=8T_h+q=(8B^2-q)/7\). The block principle now yields
\[
P=\frac{\sum_a|\Delta(a)|-\sum_a\Delta(a)}2=\frac{8B^2+7B-q}{14},\quad
N=\frac{\sum_a|\Delta(a)|+\sum_a\Delta(a)}2=\frac{8B^2-7B-q}{14}.
\]
The remaining \(8B^2-P-N=(48B^2+q)/7\) positions are ties, proving row four.

Summing the four rows proves the displayed shell formulas. To prove the density statement, the number of positive signs below \(X=16^h\) equals a fixed finite initial contribution plus \(\sum_{j=1}^{h-1}P_j\); the leading term is \((39/56)\sum_{j<h}16^j\sim(13/280)16^h\), while all lower-order terms are \(o(16^h)\). Adding the first row of the current shell contributes \(X/8+o(X)\) at \(2X\), and the subsequent second and third rows contribute only \(O(1)\) positive signs before \(8X\). Dividing by \(X,2X,8X\), respectively, gives the three stated, unequal limits. Therefore a natural density cannot exist. \(\square\)

## Verification

The standalone Python 3 script `verify.py` scans each integer in all four shells for \(h=1,2,3,4\), detects palindromes directly by digit reversal in bases \(2\) and \(4\), and independently compares each subinterval to the formulas. Shell triples \((P,N,Z)\) are \((12,94,134)\), \((179,1665,1996)\), \((2853,27235,31352)\), and \((45641,438087,499312)\). Run `python3 verify.py`; it prints `ALL_EXACT_CHECKS_PASS`. This finite test does **not** establish the infinite theorem, which depends on the block and signed-digit arguments above.

## Relationship to prior work

Phunphayap and Pongsriiam (2021 publication, 2022 volume) initiated the general race question and proved infinitely many sign changes when bases differ. Their 2023 follow-up establishes sharp **pointwise** comparison for the paired bases, including \(A_4(n)-A_2(n)\ge-1\), and gives the asymptotic picture of differences. The earlier pointwise formulas of Pongsriiam and Subwattanachai (2019) calculate \(A_b(n)\) from digits. These are compatible but do not provide the four exact sign-frequency formulas or the density-nonexistence conclusion above. The essential added step is a complete arithmetic averaging of signed palindrome-order offsets over each aligned block, not evaluation at one \(n\).

## Limitations

The theorem treats bases \(2\) and \(4\), not arbitrary base pairs. It proves three distinct subsequential densities but does not identify global limsup or liminf. Published, indexed, and accessible sources were inspected; an independent mathematical audit has not been performed and unindexed equivalent work remains possible.

## References

1. P. Phunphayap and P. Pongsriiam, *Extremal orders and races between palindromes in different bases*, AIMS Mathematics **7** (2022), 2237–2254; first public publication 10 November 2021. https://doi.org/10.3934/math.2022127.
2. P. N. Phunphayap and P. Pongsriiam, *A complete comparison for the number of palindromes in different bases*, AIMS Mathematics **8** (2023), 9924–9932. https://doi.org/10.3934/math.2023502.
3. P. Pongsriiam and K. Subwattanachai, *Exact formulas for the number of palindromes up to a given positive integer*, International Journal of Mathematics and Computer Science **14** (2019), 27–46. https://future-in-tech.net/14.1/R-Pongsriiam.pdf.
