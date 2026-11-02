# Exact run-length frequencies for binary semigroups with \(a=dt+1\) and \(b=a+d\)

## Finding
For any integers \(d,t\ge 2\), set \(a=dt+1\), \(b=a+d\), and \(S=\langle a,b\rangle=\{ua+vb:u,v\in\mathbb Z_{\ge0}\}\). For each integer \(\ell\ge1\), let \(B_\ell(S)\) be the number of **maximal intervals of length \(\ell\)** consisting entirely of positive integers outside \(S\). Then the complete run-length distribution is
\[
\boxed{\sum_{\ell\ge1}B_\ell(S)z^\ell
=t(t+1)\sum_{\ell=1}^{d-1}z^\ell+\sum_{j=1}^{t}z^{dj}.}
\]
Thus each length from \(1\) through \(d-1\) occurs exactly \(t(t+1)\) times, each of \(d,2d,\ldots,td\) occurs exactly once, and no other length occurs.

Consider the binary inclusion-exclusion (semigroup) polynomial
\[
Q_{a,b}(x)=\frac{(1-x^{ab})(1-x)}{(1-x^a)(1-x^b)}.
\]
List the exponents of its nonzero coefficients as \(0=e_0<e_1<\cdots<e_M=(a-1)(b-1)\), and put \(N_\ell=\#\{i:e_{i+1}-e_i=\ell\}\). Then **every exponent-spacing frequency** is
\[
\boxed{\sum_{\ell\ge1}N_\ell z^\ell
=2t(t+1)\sum_{\ell=1}^{d-1}z^\ell+2\sum_{j=1}^{t}z^{dj}.}
\]
In particular, the polynomial has exactly \(1+2[(d-1)t(t+1)+t]\) nonzero coefficients. Its exponent-spacing support has cardinality \(d+t-1\). For example, \(d=4\), \(t=3\) gives the prime pair \(a=13\), \(b=17\) and hence the binary cyclotomic polynomial \(\Phi_{221}\): spacings \(1,2,3\) occur \(24\) times each, whereas spacings \(4,8,12\) occur twice each.

## Assumptions and scope
The parameters are arbitrary integers \(d,t\ge2\); primality of either generator is **not** assumed. Since \(\gcd(a,b)=\gcd(dt+1,d)=1\), the complement of \(S\) is finite. Its Frobenius number and conductor are
\[
F=ab-a-b=(a-1)(b-1)-1,
\qquad c=F+1=(a-1)(b-1)=d^2t(t+1).
\]
Maximal missing-integer intervals are counted in the full nonnegative integer line; they all lie in \([1,F]\). The polynomial spacing statistic includes spacing \(1\) between adjacent nonzero terms. The parameter condition ensures \(b\bmod a=d\), where \(2\le d\le a-2\): these are not the previously analyzed \(\pm1\) residue cases.

## Proof
**1. Exact Apéry thresholds.** For a residue \(0\le r<a\), choose the unique \(k_r\in\{0,1,\ldots,a-1\}\) satisfying \(dk_r\equiv r\pmod a\). Since \(b\equiv d\pmod a\), the least element of \(S\) in residue \(r\) is \(k_rb\). Indeed, every representation \(ua+vb\) can be transformed to one with \(0\le v<a\) by replacing \(ab\) with \(ba\). Write \(k_rb=h_ra+r\). Then
\[
ma+r\in S\quad\Longleftrightarrow\quad m\ge h_r
\qquad(m\ge0,\ 0\le r<a).
\]
For \(r=dj\), \(0\le j\le t\), one has \(k_r=j\) and \(h_r=j\). Every other residue has the unique form \(r=dj+s\), with \(0\le j\le t-1\) and \(1\le s\le d-1\). Using \(dt=a-1\), one calculates
\[
k_r=t(d-s)+1+j,\qquad
h_{dj+s}=(t+1)(d-s)+1+j.\tag{1}
\]
Indeed \(dk_r=(d-s)a+dj+s\), from which the claimed least residue and quotient follow. The largest Apéry representative is \((a-1)b\), attained at \(k_r=a-1\), so the largest gap is \((a-1)b-a=ab-a-b=F\), justifying the conductor used above.

**2. Isolated long gaps.** Partition the integers into rows \(ma,ma+1,\ldots,ma+a-1\), for \(m\ge0\). At each row \(0\le m<t\), the represented residues are precisely \(0,d,\ldots,md\), by (1). Its missing residues therefore consist of \(m\) bounded intervals of length \(d-1\), between consecutive represented multiples of \(d\), and a final suffix of length \(d(t-m)\). The next row begins with a represented integer, so each suffix is a maximal gap block. As \(m\) ranges from \(0\) through \(t-1\), these contribute exactly one gap block of each length \(d,2d,\ldots,td\), and no other long blocks.

**3. Short gaps, including the boundary rows.** At row \(m=t\), each residue \(0,d,\ldots,td=a-1\) is represented. The same is true in every later row. Hence no missing block crosses a row boundary for \(m\ge t\), and the only possibly missing entries in later rows occur in the \(t\) interior intervals \(dj+1,\ldots,d(j+1)-1\), with \(0\le j<t\). Within interval \(j\), the residue \(dj+s\) first becomes represented in row
\[
H_{j,s}=(t+1)(d-s)+1+j.
\]
The entries become represented from right to left. Thus the remaining missing entries are always a single initial block, of some length between zero and \(d-1\).

Fix \(\ell\in\{1,\ldots,d-2\}\). In interval \(j\), its missing-block length equals exactly \(\ell\) precisely for the rows
\[
H_{j,\ell+1}\le m<H_{j,\ell}.
\]
The two thresholds differ by \(t+1\), so **each** of the \(t\) intervals contributes \(t+1\) occurrences: altogether \(t(t+1)\) blocks of length \(\ell\).

For the extreme short length \(d-1\), rows \(0\le m<t\) contribute \(\sum_{m=0}^{t-1}m=t(t-1)/2\) interior blocks. In interval \(j\), every row from \(t\) through \(H_{j,d-1}-1=t+j+1\) has a full missing block of length \(d-1\), amounting to \(j+2\) additional blocks. Their total is
\[
\frac{t(t-1)}2+\sum_{j=0}^{t-1}(j+2)
=t(t+1).
\]
This also covers \(d=2\), when the intermediate-length range is empty. Since \(\max_j H_{j,1}=b-2\), every row with \(m\ge b-2\) is entirely represented. All lengths and their frequencies have now been accounted for: every short gap is confined to an interior interval, and every long gap is one of the early suffixes.

**4. From gap blocks to polynomial exponent spacings.** For two coprime generators, the numerical semigroup is symmetric: the reflection \(u\mapsto F-u\) sends represented integers in \([0,F]\) bijectively to nonrepresented integers there. One direct proof uses the Apéry thresholds: there are precisely \(\sum_r h_r=(a-1)(b-1)/2\) nonrepresented integers; the equality follows by summing the standard floor identity \(\sum_{k=0}^{a-1}\lfloor kb/a\rfloor=(a-1)(b-1)/2\). Both \(u\) and \(F-u\) cannot be represented, since then \(F\) would be represented. The represented and nonrepresented counts in \([0,F]\) are both \(c/2\), so reflection must pair them. It follows that the maximal represented blocks and maximal missing blocks have identical length multisets.

The exact semigroup generating series is
\[
\sum_{s\in S}x^s
=\frac{\sum_{k=0}^{a-1}x^{kb}}{1-x^a}
=\frac{1-x^{ab}}{(1-x^a)(1-x^b)},
\]
because every represented integer has a unique expression \(ua+kb\) with \(u\ge0\) and \(0\le k<a\). Therefore \(Q_{a,b}(x)=(1-x)\sum_{s\in S}x^s\). Its coefficient at exponent \(n\) is \(\mathbf1_S(n)-\mathbf1_S(n-1)\) (with \(\mathbf1_S(-1)=0\)); hence nonzero coefficients occur exactly at transitions between a maximal represented block and a maximal missing block. The nonzero-exponent differences are exactly the lengths of all these blocks in \([0,F]\). Since the two block-length multisets agree, each missing-block length is counted twice, proving the polynomial formula and its coefficient-count corollary.

## Verification
The standalone Python 3 program `verify_gap_blocks.py` performs independent additive dynamic programming and Apéry-residue tests for every \(2\le d\le12\), \(2\le t\le16\), compares all missing-block lengths to the formula, and computes polynomial exponent-spacings from coefficient transitions. It also uses a separate explicit two-dimensional generator enumeration for smaller parameters. Executing the included file yielded:

```text
VERIFY_OK general_cases=165 checked_integers=1058035 gap_blocks=109065 independent_enumeration_cases=30 exact_integer=yes
EXAMPLE d=2 t=2 a=5 b=7 gap_block_counts=[(1, 6), (2, 1), (4, 1)]
EXAMPLE d=3 t=2 a=7 b=10 gap_block_counts=[(1, 6), (2, 6), (3, 1), (6, 1)]
EXAMPLE d=4 t=3 a=13 b=17 gap_block_counts=[(1, 12), (2, 12), (3, 12), (4, 1), (8, 1), (12, 1)]
```
The proof, not these finite tests, establishes the assertion for every parameter pair.

## Relationship to prior work
Bachman (2026), arXiv:2605.17157, Theorem 2 evaluates **the set of distinct polynomial gap lengths** using the Euclidean algorithm; its conclusion is set-valued and does not evaluate how often each length occurs. In Section 4, the difference-of-membership coefficient formula is established (equation (32)); the present theorem uses that identity but obtains a new explicit *frequency distribution* for a two-parameter family.

Cafure and Cesaratto (2025), arXiv:2507.19381, Theorem 1.2 gives explicit frequency counts only when the larger generator is congruent to \(1\) or \(-1\) modulo the smaller (as well as the prime case). Here \(b\equiv d\pmod a\) with \(2\le d\le a-2\). Their Theorem 1.1 treats the second-largest length in general; it does not give this complete distribution. Moree (2013), arXiv:1308.3972, provides the classical link between two-generator semigroups and binary inclusion-exclusion polynomials and the symmetry facts used here; these are not claimed as new.

## Limitations
The complete classification is established only for generators \(dt+1\) and \(d(t+1)+1\) with \(d,t\ge2\). It is not a general formula for all coprime generator pairs. The prior-literature comparison covers the most directly relevant full-text works and targeted searches, not every historical source or implication of all older coefficient-word formulas. A prior implicit equivalent distribution remains possible; the claim has not undergone an independent mathematical or historical-priority audit. Finite verification is corroboration, not a replacement for the proof.

## References
1. G. Bachman, *Gaps of Binary Numerical Semigroups and of Binary Inclusion-Exclusion Polynomials*, arXiv:2605.17157, first posted 2026-05-16. https://arxiv.org/abs/2605.17157
2. A. Cafure and E. Cesaratto, *Gaps in binary cyclotomic polynomials*, arXiv:2507.19381, first posted 2025-07-25. https://arxiv.org/abs/2507.19381
3. P. Moree, *Numerical semigroups, cyclotomic polynomials and Bernoulli numbers*, arXiv:1308.3972, first posted 2013-08-19. https://arxiv.org/abs/1308.3972
