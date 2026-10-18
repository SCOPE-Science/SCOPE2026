# Determinant growth and nonsliceness in a two-site delta-unknotting family

## Finding

For every integer \(b\ge -1\), consider the Montesinos knot
\[
K_b=M\bigl(0;(3b+5,-3),(8b+13,8),(8b+13,8)\bigr).
\]
Nakamura's Example 3.1 and accompanying delta-unknotting result supply two distinct Type-I tangle regions, each admitting a delta-move to the unknot, and yield
\(u(K_b)=u^{\Delta}(K_b)=1\).
For this entire one-parameter subfamily,
\[
\boxed{\det(K_b)=(8b+13)(24b+41).}
\]
The determinants are strictly increasing and nonsquare. Consequently the knots \(K_b\) are pairwise nonisotopic; none is algebraically slice, and none is topologically locally flat slice.

## Assumptions and scope

The integer parameter satisfies \(b\ge-1\). Set \(p=3b+5\) and \(q=8b+13\). Then \(p\ge2\), \(q\ge5\), \(\gcd(p,3)=\gcd(q,8)=1\), so the displayed Montesinos parameters are reduced in the convention of Nakamura's construction. The existence and distinctness of the two unknotting delta-move regions, and the value of the unknotting numbers, are imported from Nakamura; the determinant formula and its implications below are established independently of the delta-move diagrams. The claim does not identify the two moves using determinants.

## Proof

For the three-branch Montesinos presentation \(M(0;(\alpha_1,\beta_1),(\alpha_2,\beta_2),(\alpha_3,\beta_3))\), the standard double-branched-cover homology calculation gives the determinant identity
\[
\det M(0;(\alpha_1,\beta_1),(\alpha_2,\beta_2),(\alpha_3,\beta_3))
=\left|\alpha_1\alpha_2\alpha_3\left(\frac{\beta_1}{\alpha_1}+\frac{\beta_2}{\alpha_2}+\frac{\beta_3}{\alpha_3}\right)\right|.
\]
This is the formula recorded as Lemma 5 by Baker and Moore. With \((\alpha_1,\beta_1)=(p,-3)\) and \((\alpha_2,\beta_2)=(\alpha_3,\beta_3)=(q,8)\), we obtain
\[
\begin{aligned}
\det(K_b)
&=\left|pq^2\left(-\frac3p+\frac8q+\frac8q\right)\right|\\
&=\left|-3q^2+16pq\right|=q\,(16p-3q)\\
&=(8b+13)(24b+41).
\end{aligned}
\]
Both factors are positive on the stipulated half-line. Direct subtraction yields
\[
\det(K_{b+1})-\det(K_b)=384b+832>0\qquad(b\ge-1).
\]
As the determinant is an isotopy invariant, these knots are pairwise nonisotopic.

Next write \(r=24b+41\). The positive integers \(q\) and \(r\) are odd, and
\[
\gcd(q,r)=\gcd(q,r-3q)=\gcd(q,2)=1.
\]
Also \(r\equiv2\pmod3\), whereas every integer square is congruent to \(0\) or \(1\) modulo \(3\). Thus \(r\) is not a square. Were \(qr\) a square, coprimality would force \(q\) and \(r\) separately to be squares, a contradiction. Hence \(\det(K_b)\) is never square.

For an algebraically slice knot, the Fox--Milnor factorization \(\Delta_K(t)\doteq f(t)f(t^{-1})\) forces \(\det K=|\Delta_K(-1)|=|f(-1)|^2\) to be a square. The nonsquare determinant therefore rules out algebraic sliceness. A topologically locally flat slice knot is algebraically slice, so the topological sliceness conclusion follows.

## Verification and limits

The symbolic determinant expansion is \(192b^2+640b+533\). Its first difference is \(384b+832\), the factors have gcd one, and \(24b+41\equiv2\pmod3\), proving the complete infinite-family assertions. Independent integer checks for \(-1\le b\le150\) corroborate, but do not replace, these symbolic arguments. The result does not determine concordance order, distinguish the two delta-moves by an invariant, classify other signed Montesinos parameter families, or supply an independent geometric proof of Nakamura's two-move construction.

## Relationship to prior work

Nakamura's paper gives this family and its two delta-unknotting constructions, but the inspected publicly available description and the targeted statement searches do not supply the closed determinant factorization and uniform nonsliceness obstruction. Baker--Moore give the general Montesinos determinant formula; substituting this family is necessary to obtain the arithmetic statement. The Fox--Milnor obstruction is classical, not new. The significance of the added exact result is to exhibit a whole explicit family of two-site delta-unknottable knots that are all nonslice and distinguished by strictly growing determinants. These conclusions are bounded to the displayed family; novelty is best-of-knowledge and subject to the primary-source-access limitation stated in the independent review.

## References

1. K. Nakamura, *Montesinos Knots with Delta-Unknotting Number One*, arXiv:2609.39565v1 (2026), Theorem 1.3 and Example 3.1.
2. K. L. Baker and A. H. Moore, *Montesinos knots, Hopf plumbings, and L-space surgeries*, arXiv:1404.7585v1; J. Math. Soc. Japan 70 (2018), Lemma 5.
3. The classical Fox--Milnor factorization of the Alexander polynomial of an algebraically slice knot; see also S. Saurabh, *Exceptional pretzel knots are not algebraically slice*, arXiv:2609.34522v1 (2026).
