# Sharp small-box counts and all radius-two extremizers for unimodular matrices

## Finding

For a real \(2\times2\) matrix \(K\) and \(T\ge0\), let
\[
N(K,T)=\#\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\mathrm{SL}_2(\mathbb Z): |a-K_{11}|,|b-K_{12}|,|c-K_{21}|,|d-K_{22}|\le T\right\},
\qquad F(T)=\max_{K\in\mathbb R^{2\times2}}N(K,T).
\]
The following sharp profile holds on the entire range \(0\le T\le2\):
\[
F(T)=\begin{cases}
1,&0\le T<\tfrac12,\\
6,&\tfrac12\le T<1,\\
20,&1\le T<\tfrac32,\\
36,&\tfrac32\le T<2,\\
60,&T=2.
\end{cases}
\]
At \(T=2\), equality \(N(K,2)=60\) holds **exactly** at eight centres, namely
\[
K=\begin{pmatrix}\varepsilon&0\\0&\eta\end{pmatrix}
\quad\text{or}\quad
K=\begin{pmatrix}0&\varepsilon\\\eta&0\end{pmatrix},
\qquad \varepsilon,\eta\in\{-1,1\}.
\]
In particular, \(N(0,2)=52<60\). Thus centring the radius-two coordinate box at the origin does not maximize the number of determinant-one integer matrices; the discrepancy is eight matrices.

## Assumptions and scope

Every matrix entry is an ordinary integer and the determinant is exactly \(+1\). All boxes are closed, axis-parallel, use the same coordinate radius \(T\), and may have any real matrix centre. The claimed exact profile is restricted to \(0\le T\le2\); the eight-centre classification concerns \(T=2\) alone. No assertion is made about the maximizing centre for larger radii or for higher-rank symplectic groups.

## Proof

**1. Reduction to integer blocks.** Set \(w=\lfloor2T\rfloor+1\). A real interval of length \(2T\) contains at most \(w\) consecutive integers, so its integer intersection lies in a block \(I_w(s)=\{s,s+1,\ldots,s+w-1\}\) for some integer \(s\). Conversely any prescribed block of \(w\) consecutive integers fits into an interval of radius \(T\), centred at its midpoint, because \(w-1\le2T\). Therefore \(F(T)\) is the maximum count of \(ad-bc=1\) over four independently shifted blocks of width \(w\). If \(w=1\), a box contains at most one integer matrix, and a determinant-one matrix can be centred in such a box, giving \(F(T)=1\).

**2. Localization lemma.** Fix \(w\ge2\). Suppose some coordinate block \(I_w(s)\) avoids the interval \([-(w-1),w-1]\). Then each integer in that block has absolute value at least \(w\). Take the column containing this entry as the fixed column. For any fixed primitive column \(v\in\mathbb Z^2\), two possible complementary integer columns \(u,u'\) satisfying determinant one differ by \(u-u'=kv\), \(k\in\mathbb Z\), by Bézout's identity. A nonzero difference in the coordinate corresponding to the large entry has magnitude at least \(w\), whereas the corresponding complementary coordinate varies inside an interval of integer diameter \(w-1\). Thus there is at most one complementary column for each fixed column. Nonprimitive fixed columns have no determinant-one completions. There are at most \(w^2\) choices of the fixed column. Consequently any four-block box with one coordinate block avoiding \([-(w-1),w-1]\) contains at most \(w^2\) qualifying matrices.

Accordingly, whenever an example with more than \(w^2\) qualifying matrices exists, every maximizing four-block box has all four starting positions in
\[
-2(w-1)\le s\le w-1,
\]
which is the exact condition that \(I_w(s)\) meet \([-(w-1),w-1]\). This is a finite reduction of the optimization over all real centres, including arbitrarily remote centres.

**3. Exhaustive finite computation.** For a starting tuple \(\mathbf{s}=(s_a,s_b,s_c,s_d)\), define
\[
C_w(\mathbf{s})=\sum_{a=s_a}^{s_a+w-1}\sum_{b=s_b}^{s_b+w-1}\sum_{c=s_c}^{s_c+w-1}\sum_{d=s_d}^{s_d+w-1}\mathbf 1_{\{ad-bc=1\}}.
\]
The attached `verify.py` checks this formula using exact integer operations for **every** \(\mathbf s\in[-2(w-1),w-1]^4\cap\mathbb Z^4\). At widths \(w=2,3,4,5\), the numbers of starting tuples checked are respectively \(256,2401,10000,28561\), and their exact maxima are \(6,20,36,60\). The corresponding numbers of maximizing starting tuples are \(4,1,16,8\). Each maximum exceeds \(w^2\), so Step 2 proves that this finite enumeration is exhaustive over all translations.

At width five, the eight maximizing starting tuples are exactly those with either (i) \(s_a,s_d\in\{-3,-1\}\) and \(s_b=s_c=-2\), or (ii) \(s_a=s_d=-2\) and \(s_b,s_c\in\{-3,-1\}\). The program also checks the values \(C_5(-2,-2,-2,-2)=52\) and \(C_5(-2,-1,-1,-2)=60\).

**4. Exact real-centre classification at radius two.** For every one of the eight width-five maximizing blocks, `verify.py` additionally establishes that each of its five integers occurs as each respective matrix coordinate in at least one determinant-one matrix counted by the box. Hence removing even one integer from any coordinate block reduces its count strictly below \(60\). A real radius-two interval contains five consecutive integers only when its centre is the integer midpoint. It follows that each of the four real centre coordinates must be the midpoint of its maximizing block, or \(s+2\). Translating the two patterns from Step 3 yields precisely the eight matrices displayed in the theorem. All eight attain \(60\), concluding the proof.

## Verification

Run `python3 verify.py` using Python 3's standard library. The verifier enumerates all localized starting tuples for widths two through five, independently recomputes the counts at maximizing tuples by solving the determinant equation columnwise, and compares two methods on 1,200 fixed-seed further tuples. It checks the origin and shifted radius-two counts, enumerates the eight maximizing radius-two centres, and verifies that every boundary coordinate value occurs at each maximizer. Expected final line: `VERIFY_OK width=2..5, all reduced starts, exact integer determinant, finite certificate`.

The exhaustive search is a proof only in conjunction with the localization and width-reduction arguments above. Neither finite checks at larger radii nor asymptotic extrapolation is asserted.

## Relationship to prior work

Wurzinger's arXiv:2610.29794v1 (21 October 2026), primary MSC 11C20, proves an asymptotically sharp count bound uniform over all real box centres in symplectic groups, identifies the rank-one group with \(\mathrm{SL}_2(\mathbb Z)\), and contrasts uniform translations with origin-centred asymptotics. Its stated Theorems 1.1–1.2 and the inspected discussions do not supply any exact radius-two maximum or maximizing-centre classification. Shparlinski's earlier fixed-determinant box count addresses uniform large-box estimates, not the finite profile established here. Krieg's maximum-norm enumeration concerns the origin-centred count; it is compatible with the computed value \(52\), but does not imply the shifted maximum \(60\). OEIS A171503 enumerates determinant-one matrices in a single nonnegative-coordinate cube, not arbitrary translated four-coordinate blocks.

The contribution is an exact small-scale sharp uniform bound, its complete radius-two equality classification, and a concrete obstruction to transferring origin-centred extremality to arbitrary centres. These results neither strengthen nor challenge the cited large-radius asymptotic theorems.

## Limitations

The finite thresholds \(T\le2\) are natural initial integer-entry phase transitions, not a claim about all radii. Although the exact finite certificate handles every translated centre at these scales through a proved localization, it gives no general formula for \(T>2\). Unindexed prior enumerations or implicit consequences of earlier papers remain possible. The full text of Shparlinski's 2010 article was not inspected; only its abstract and the precise statement of its cited bound in Wurzinger were available for comparison.

## References

1. Lena Wurzinger, *Integer symplectic matrices in expanding boxes*, arXiv:2610.29794v1, submitted 21 October 2026, https://arxiv.org/html/2610.29794v1.
2. I. E. Shparlinski, *Some counting questions for matrices with restricted entries*, Linear Algebra Appl. **432** (2010), 155–160, https://doi.org/10.1016/j.laa.2009.07.036.
3. A. Krieg, *Counting modular matrices with specified maximum norm*, Linear Algebra Appl. **196** (1994), 273–278.
4. OEIS A171503, *Number of 2 X 2 integer matrices with entries from {0,1,...,n} having determinant 1*, https://oeis.org/A171503.
