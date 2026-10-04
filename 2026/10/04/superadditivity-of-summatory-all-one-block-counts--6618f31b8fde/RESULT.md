# Superadditivity of summatory all-one block counts
## Finding
For every integer \(r\ge 2\), let \(b_r(n)\) denote the number of overlapping occurrences of the block \(1^r\) in the ordinary binary expansion of \(n\), with \(b_r(0)=0\), and define
\[
B_r(N)=\sum_{0\le j<N} b_r(j).
\]
Then for all integers \(m,n\ge 0\),
\[
B_r(m+n)\ge B_r(m)+B_r(n).
\]

The inequality is sharp in a stronger form. If \(k\ge r-1\) and
\[
0\le m\le 2^k-2^{k-r+1},
\]
then
\[
B_r(2^k+m)=B_r(2^k)+B_r(m).
\]
Consequently no universally positive additive correction depending only on the smaller addend can strengthen the inequality. In particular, the case \(r=2\) gives a summatory inequality for the number of occurrences of \(11\) in binary expansions.

## Assumptions and scope
Occurrences overlap. Binary expansions are the usual finite expansions without leading zeroes; the convention \(b_r(0)=0\) is used. The result concerns the all-one blocks \(1^r\). It does not assert superadditivity for arbitrary binary blocks.

The literature source motivating the question uses summatory digit functions and explicitly asks whether similar inequalities hold when the digit sum is replaced by a block-counting function, giving the number of \(11\) occurrences as its example. The present statement answers that example and, with the same proof, every longer all-one block.

## Proof
Fix \(r\ge 2\). For each bit position \(i\ge 0\), put \(q=2^i\) and
\[
M=2^r q.
\]
An occurrence of \(1^r\) whose least significant position is \(i\) occurs in an integer \(t\) exactly when
\[
t\bmod M\in\{M-q,M-q+1,\ldots,M-1\}.
\]
Therefore the number of such occurrences contributed by position \(i\) among \(0\le t<N\) is
\[
F_q(N)
=
q\left\lfloor\frac{N}{M}\right\rfloor
+
\max\!\bigl\{0,(N\bmod M)-(M-q)\bigr\}.
\]
Only finitely many positions contribute, and hence
\[
B_r(N)=\sum_{i\ge 0}F_{2^i}(N).
\]

It is enough to prove every \(F_q\) is superadditive. Write
\[
m=aM+x,\qquad n=bM+y,\qquad 0\le x,y<M,
\]
and set
\[
h(z)=\max\{0,z-(M-q)\}\qquad(0\le z<M).
\]
The complete-period terms cancel, so the desired inequality is
\[
q\left\lfloor\frac{x+y}{M}\right\rfloor
+h\bigl((x+y)\bmod M\bigr)
\ge h(x)+h(y).
\]

There are three cases. If both \(x\) and \(y\) are below \(M-q\), the right side is zero. If, say, \(x\ge M-q\) and \(y<M-q\), then before a wrap the left residual term increases by \(y\), while after a wrap the left side contains the full contribution \(q\), which is at least \(h(x)\). Finally suppose both \(x,y\ge M-q\). Then one wrap occurs. Put \(z=x+y-M\). The right side is
\[
z-M+2q.
\]
If \(z<M-q\), this is at most \(q\), which is the left side. If \(z\ge M-q\), the left side is
\[
q+z-(M-q)=z-M+2q,
\]
so equality holds. Thus \(F_q(m+n)\ge F_q(m)+F_q(n)\) in every case. Summing over \(i\) proves the first claim.

For the equality strip, fix \(k\ge r-1\). For \(0\le j<2^k\), the binary expansion of \(2^k+j\) is a leading \(1\) followed by the \(k\)-bit expansion of \(j\), padded on the left by zeroes. Occurrences entirely inside those last \(k\) bits are exactly the occurrences counted by \(b_r(j)\). The only possible new occurrence using the leading \(1\) requires the next \(r-1\) bits all to be \(1\), which is equivalent to
\[
j\ge 2^k-2^{k-r+1}.
\]
Hence for every
\[
0\le j<2^k-2^{k-r+1}
\]
we have \(b_r(2^k+j)=b_r(j)\). Summing this identity for \(0\le j<m\) gives the asserted equality whenever \(m\le 2^k-2^{k-r+1}\).

For every fixed positive \(m\), the equality applies for all sufficiently large \(k\). Therefore a universal strengthening of the form
\[
B_r(m+n)\ge B_r(m)+B_r(n)+\phi(\min\{m,n\})
\]
forces \(\phi(m)=0\) for every \(m\ge 1\).

## Verification
The standalone verifier computes the block counts directly from binary strings and independently through the positional formula above. It checks the two descriptions for every \(N\le 4096\) and \(2\le r\le 6\), exhaustively tests all pairs \(0\le m,n\le 512\) for those five block lengths, stress-tests complete residue periods and boundary residues for the positional lemma, and exhaustively verifies the equality strip through dyadic scale \(2^{10}\).

These finite checks are corroborative. The all-\(N\), all-\(r\) result is proved by the residue case analysis and the binary-prefix argument, not inferred from the finite tests.

## Relationship to prior work
Allouche and Stipulanti study inequalities for summatory digit sums. In their final section they explicitly ask whether analogous inequalities exist for other block-counting functions and give the number of \(11\) occurrences in the binary expansion as the concrete example. Their earliest public arXiv version is dated 2023-11-28, and their listed 2020 Mathematics Subject Classification begins with \(68R15\).

Kirschenhofer studies mean values of subblock occurrences in \(q\)-ary representations. Muramoto, Okada, Sekiguchi, and Shiota give a general exact representation for summatory subblock occurrences, and their full text develops explicit and asymptotic formulas rather than additive inequalities in two independent arguments. Prodinger studies a generalized sum-of-digits function and its summatory behavior. These sources establish that the block-counting summatory function is classical, but the inspected statements do not give the superadditivity theorem or the sharp dyadic equality strip above.

The general exact representation is the closest broader result: in principle it contains enough information to evaluate each individual \(B_r(N)\), but the global comparison of the three values at \(m\), \(n\), and \(m+n\) is not a direct parameter specialization of its theorem. The new proof instead decomposes the all-one block count into tail-interval summands and proves each summand superadditive.

## Limitations
No claim is made for arbitrary binary words. Indeed, changing the location of the relevant residue interval destroys the one-position superadditivity argument, so extending the theorem to other blocks requires separate analysis.

The oldest subblock literature is broad and uses several equivalent notations. Although the direct 2024 question, targeted searches, and inspection of the closest exact-formula paper found no prior additive inequality matching this statement, an unindexed or differently phrased earlier corollary remains a residual originality risk.

## References
1. J.-P. Allouche and M. Stipulanti, “Summing the sum of digits,” arXiv:2311.16806, first public version 2023-11-28; Communications in Mathematics, DOI 10.46298/cm.12610.
2. P. Kirschenhofer, “Subblock occurrences in the q-ary representation of n,” SIAM Journal on Algebraic and Discrete Methods 4 (1983), 231–236, DOI 10.1137/0604025.
3. K. Muramoto, T. Okada, T. Sekiguchi, and Y. Shiota, “An Explicit Formula of Subblock Occurrences for the p-Adic Expansion,” Interdisciplinary Information Sciences 8 (2002), 115–121, DOI 10.4036/iis.2002.115.
4. H. Prodinger, “Generalizing the Sum of Digits Function,” SIAM Journal on Algebraic Discrete Methods 3 (1982), 35–42, DOI 10.1137/0603004.
