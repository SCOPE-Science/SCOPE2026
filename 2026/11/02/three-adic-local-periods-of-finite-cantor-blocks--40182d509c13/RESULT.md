# Three-adic local periods of finite Cantor blocks

## Finding

For every integer \(r\geq 0\), let \(m=3^r\), let \(C_0=1\), and apply the binary morphism \(1\mapsto101\), \(0\mapsto000\) exactly \(r\) times to obtain \(C_r\). Put \(V_r=C_r0^m\), a word of length \(2m\). For every cyclic cut \(0\leq i<2m\), let \(L_r(i)\) be the length of the **shortest nonempty proper border** of the conjugate \(V_r[i:2m]V_r[0:i]\), with \(L_r(i)=2m\) if the conjugate is unbordered.

The complete local-period array is
\[
L_r(i)=\begin{cases}
2m,&i=0\text{ or }i=m,\\
1,&m<i<2m,\\
1,&0<i<m\text{ and }C_r[i-1]=C_r[i],\\
2\cdot3^{\nu_3(i)},&0<i<m\text{ and }C_r[i-1]\ne C_r[i].
\end{cases}
\]
Here \(\nu_3(i)\) is the exponent of the greatest power of three dividing the positive integer \(i\). In particular, for each \(0\leq j<r\), the value \(2\cdot3^j\) occurs at exactly \(2^{r-j}\) cyclic cuts; the value \(1\) occurs at exactly \(2\cdot3^r-2^{r+1}\) cuts; and the value \(2\cdot3^r\) occurs at exactly two cuts. These statements also hold for \(r=0\), when only the last case occurs.

Moreover, the maximum unbordered-factor length in \(C_{r+1}\) is \(2\cdot3^r\); its only two unbordered factors of that length are \(C_r0^{3^r}\) and \(0^{3^r}C_r\). The new central assertion is the complete position-by-position local-period law and its spectrum, not merely the existence of two unbordered conjugates.

## Assumptions and scope

Words are literal finite words on \(\{0,1\}\), and positions are numbered from zero. A **border** of a length-\(n\) word is a nonempty proper prefix that is also a suffix; an unbordered word has no such border. A **cyclic conjugate at cut** \(i\) is the suffix starting at \(i\) followed by the prefix of length \(i\). The term **local period** here follows the cyclic-word convention: it is the length of the shortest border of that conjugate, or its full length when no border exists. It is not the usual least period of the conjugate. No arbitrary-prefix or infinite-word claim is made.

## Proof

**1. Three structural properties.** Each \(C_s\) begins and ends in \(1\), is a palindrome, and has no adjacent pair of ones. All three statements follow inductively from the morphism; equivalently,
\[
C_{s+1}=C_s\,0^{3^s}\,C_s.
\]
In particular, \(C_s\) contains no block of \(3^s\) consecutive zeros.

**2. A useful unbordered pair.** Let \(P\) be a length-\(d\) word beginning and ending in \(1\). Then \(0^dP\) is unbordered. A putative border of length at most \(d\) would begin in zero and end in one. A border of length greater than \(d\) would require a second occurrence of the prefix \(0^d1\), yet this prefix occurs only at the start: \(P\) begins and ends in one, so no \(d\)-zero block lies inside \(P\). By reversal, \(P0^d\) is unbordered if \(P\) is palindromic. Consequently both \(0^{3^j}C_j\) and \(C_j0^{3^j}\) are unbordered for every \(j\geq0\).

**3. The two exceptional cuts.** At \(i=0\) and \(i=m\), the conjugates of \(V_r=C_r0^m\) are precisely \(C_r0^m\) and \(0^mC_r\), which are unbordered by Step 2. If \(m<i<2m\), the conjugate begins and ends in zero, so its shortest border has length \(1\). For \(0<i<m\), the first and last letters of the conjugate are \(C_r[i]\) and \(C_r[i-1]\). Equal letters therefore give shortest border \(1\).

**4. The remaining transitions and their shortest borders.** Fix \(0<i<m\) with \(C_r[i]\ne C_r[i-1]\). Let \(j=\nu_3(i)\), \(d=3^j\), and \(t=i/d\), so \(j<r\) and \(t\not\equiv0\pmod3\). View the cyclic word \(V_r\) in length-\(d\) blocks. Its block coding is the cyclic binary word \(T=C_{r-j}0^{3^{r-j}}\), under the substitutions \(1\mapsto C_j\) and \(0\mapsto0^d\). The cut \(i\) lies at a block boundary, and the unequal adjacent letters mean that the two blocks on either side have different types.

If \(t\equiv1\pmod3\), this boundary is the \(1|0\) boundary inside the three-block image \(101\) of a one; the preceding block is zero because the corresponding parent one has no adjacent one, including the cyclic zero-padding boundary. Thus the four consecutive blocks indexed \(t-2,t-1,t,t+1\), cyclically, have binary types \(0101\). If \(t\equiv2\pmod3\), they instead have types \(1010\). In either case, the two blocks immediately before the cut equal the two immediately after it, block by block. Therefore the conjugate of \(V_r\) at cut \(i\) has a border of length \(2d\).

This common prefix/suffix of length \(2d\) is exactly \(0^dC_j\) or \(C_j0^d\); both are unbordered by Step 2. A shorter border of the full conjugate would also be a border of this common unbordered word, which is impossible. Hence the shortest border length is exactly \(2d=2\cdot3^{\nu_3(i)}\). This proves the entire pointwise array.

**5. Multiplicities.** Fix \(0\leq j<r\). At scale \(d=3^j\), precisely the boundaries of type \(1|0\) or \(0|1\) within a \(101\) triple give \(j=\nu_3(i)\) and unequal neighbors. These two boundaries arise for each one in \(C_{r-j-1}\). Since this word has \(2^{r-j-1}\) ones, the count is \(2^{r-j}\). Summing over \(j\) gives \(2^{r+1}-2\) nontrivial transitional cuts. Subtracting them and the two exceptional cuts from the total \(2m\) yields \(2m-2^{r+1}\) cuts with shortest border one. The listed possibilities are disjoint.

**6. Maximal unbordered factors.** The identity \(C_{r+1}=C_r0^mC_r\) shows that \(2m\) is a period of \(C_{r+1}\). Any factor of length \(\ell>2m\) therefore has a nonempty border of length \(\ell-2m\), using the equality between letters a distance \(2m\) apart. The \(m+1\) factors of length \(2m\) are the conjugates of \(V_r\) at cuts \(0\leq i\leq m\), and Steps 3–4 show that exactly the two endpoint factors are unbordered. The maximum and the uniqueness assertion follow. \(\square\)

## Verification

Run `python3 checker.py` with Python 3 and no external dependencies. The checker independently constructs the words from base-three digit conditions and from substitution, builds every cyclic conjugate, computes its shortest border by a prefix-function algorithm, and verifies every predicted value and histogram for \(0\leq r\leq6\). It separately checks the longer-factor border obstruction. The output ends in `VERIFY_OK`. The finite computation checks examples; the proof above supplies the unbounded quantifier.

## Relationship to prior work

Holub and Müller, *Fully bordered words* (first public version 2015), define cyclic local periods via shortest borders and characterize binary words with exactly two unbordered conjugates. Their results motivate the invariant and may address the qualitative two-conjugate part; the three-adic pointwise array and its exact multiplicity law are not stated in the inspected full text. Goč, Mousavi and Shallit, *On the Number of Unbordered Factors* (first public version 2012), give enumerative theorems for the Thue–Morse, Rudin–Shapiro, and period-doubling sequences, including a two-unbordered-factor law for the last family. This theorem instead concerns cyclic Cantor blocks and assigns a shortest border to **every cut**, not a lengthwise count of unbordered factors in those other infinite words. General decisions or automata for border properties do not directly supply the closed triadic array without the specialized argument in Step 4.

## Limitations

The result is about finite complete morphic iterates and one cyclic block \(C_r0^{3^r}\) at each rank; it does not give the local-period array of all factors, all prefixes, or all words. The shortest-border length and ordinary least period of a word are different quantities. This is a mathematical proof with finite computational cross-checking, not an independently audited or machine-formalized theorem. Historical priority is assessed from identified accessible sources, not exhaustively certified.

## References

1. D. Goč, H. Mousavi, and J. Shallit, *On the Number of Unbordered Factors*, arXiv:1211.1301, first public 2012-11-06, https://arxiv.org/abs/1211.1301 (especially Sections 1 and 5).
2. Š. Holub and M. Müller, *Fully bordered words*, arXiv:1504.02222, first public 2015-04-09, https://arxiv.org/abs/1504.02222 (especially definition of local period and Theorems 1–3).
3. D. Henshall and J. Shallit, *Automatic Theorem-Proving in Combinatorics on Words*, arXiv:1203.3758, first public 2012-03-16, https://arxiv.org/abs/1203.3758 (algorithmic background on borders and automatic words).
