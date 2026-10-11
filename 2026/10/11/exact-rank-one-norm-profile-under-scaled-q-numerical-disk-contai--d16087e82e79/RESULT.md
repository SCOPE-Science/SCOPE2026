# Exact rank-one norm profile under scaled \(q\)-numerical disk containment
## Finding
Let \(H\) be a complex Hilbert space with \(\dim H\ge2\), let \(0<|q|\le1\), and write \(r=|q|\). For every nonzero rank-one operator \(A\in\mathcal B(H)\), define
\[
\tau(A)=\frac{|\operatorname{tr}A|}{\|A\|}\in[0,1].
\]
Then
\[
\Omega_q(A)\subseteq\overline{\mathbb D}
\quad\Longleftrightarrow\quad
\|A\|\le
\frac{2r}{1+r\tau(A)+\sqrt{1-r^2}\sqrt{1-\tau(A)^2}}.
\]
Consequently
\[
R_1(r):=\sup\{\|A\|:\operatorname{rank}A=1,\ \Omega_q(A)\subseteq\overline{\mathbb D}\}
=
\begin{cases}
\dfrac{2r}{1+r},&0<r\le2^{-1/2},\\[4pt]
\dfrac{2r}{1+\sqrt{1-r^2}},&2^{-1/2}\le r\le1.
\end{cases}
\]
For \(0<r<2^{-1/2}\), equality occurs exactly for scalar multiples of rank-one orthogonal projections. For \(2^{-1/2}<r\le1\), equality occurs exactly for nonzero rank-one square-zero operators. At \(r=2^{-1/2}\), these are precisely the two extremal types.

Thus the rank-one extremizer geometry switches at \(r=2^{-1/2}\). Moreover \(R_1(r)<1\) for \(r<4/5\), \(R_1(4/5)=1\), and
\[
R_1(r)=\rho_q=\frac{2r}{1+\sqrt{1-r^2}}\qquad(4/5<r\le1),
\]
so rank-one square-zero operators attain the universal dilation coefficient exactly after that universal coefficient rises above one.

## Assumptions and scope
The Hilbert space is complex and has dimension at least two. The parameter satisfies \(0<|q|\le1\). The claim concerns nonzero rank-one bounded operators only. The scaled range is \(\Omega_q(A)=W_q(A)/q\). No assertion is made about the optimal norm profile at rank two or higher.

## Proof
Write \(A=a\otimes b\). Then \(\|A\|=\|a\|\|b\|\) and \(|\operatorname{tr}A|=|\langle a,b\rangle|\). Denčić--Stanković--Krstić--Damnjanović proved, for \(0\le r\le1\),
\[
\omega_r(a\otimes b)=\frac12\left(\|a\|\|b\|+r|\langle a,b\rangle|+\sqrt{1-r^2}\sqrt{\|a\|^2\|b\|^2-|\langle a,b\rangle|^2}\right).
\]
The \(q\)-numerical radius depends only on \(|q|\). Hence with \(N=\|A\|\), \(\tau=\tau(A)\), and \(s=\sqrt{1-r^2}\),
\[
\omega_q(A)=\frac N2\left(1+r\tau+s\sqrt{1-\tau^2}\right).
\]
Since \(\Omega_q(A)=W_q(A)/q\), containment in the closed unit disk is equivalent to \(\omega_q(A)\le r\). Rearrangement gives the stated pointwise criterion.

For fixed \(r\), maximizing the allowed \(N\) is equivalent to minimizing
\[
g_r(\tau)=r\tau+s\sqrt{1-\tau^2},\qquad 0\le\tau\le1.
\]
For \(0<r<1\), this is strictly concave on \((0,1)\), so its minimum on \([0,1]\) lies at an endpoint. The endpoint values are \(g_r(0)=s\) and \(g_r(1)=r\). For \(r=1\), \(g_1(\tau)=\tau\), giving the same endpoint conclusion. Therefore
\[
\min_{0\le\tau\le1}g_r(\tau)=\min\{r,\sqrt{1-r^2}\},
\]
which yields the two branches and the transition \(r=2^{-1/2}\).

If \(\tau=1\), equality in Cauchy--Schwarz makes the two rank-one factor vectors linearly dependent, so \(A\) is a scalar multiple of a rank-one orthogonal projection. If \(\tau=0\), then \(\operatorname{tr}A=0\); for rank-one operators \(A^2=(\operatorname{tr}A)A\), so this is equivalent to \(A^2=0\). Strict concavity gives no other extremizers when the endpoint values differ. At \(r=2^{-1/2}\), the two endpoint values agree and every interior value is larger, so exactly both endpoint types are extremal.

Finally, on the square-zero branch,
\[
\frac{2r}{1+\sqrt{1-r^2}}=1
\]
holds exactly at \(r=4/5\). The projection branch is always strictly below one. This proves the comparison with \(\rho_q\).

## Verification
The proof is symbolic. Its only non-elementary input is the published exact rank-one formula for \(\omega_q\), checked in the source theorem. The dependence on \(|q|\), the scaled-disk condition, the one-variable endpoint minimization, and the rank-one trace and squaring identities were separately reconstructed. No finite experiment or numerical sampling is used as proof.

The boundary cases were checked explicitly: \(r=1\) gives \(R_1(1)=2\) with square-zero extremizers; \(r=2^{-1/2}\) has exactly the two endpoint extremizer types; and \(r=4/5\) gives \(R_1(r)=1\).

## Relationship to prior work
Kaunisto--O'Loughlin--Virtanen prove that \(\Omega_q(A)\subseteq\overline{\mathbb D}\) implies a unitary \(\rho_q\)-dilation, with
\[
\rho_q=\max\left\{1,\frac{2|q|}{1+\sqrt{1-|q|^2}}\right\},
\]
and show sharpness for \(4/5<|q|\le1\) using a \(2\times2\) nilpotent. Their theorem is universal in operator rank and does not classify the exact operator-norm envelope inside rank one.

Denčić--Stanković--Krstić--Damnjanović give the exact \(q\)-numerical radius of an arbitrary rank-one operator. The present result uses that formula to solve the scaled-disk norm optimization completely, including the projection-to-square-zero transition at \(|q|=2^{-1/2}\) and its relation to the universal \(4/5\) threshold.

Aouichaoui--O'Loughlin establish sharp spectral constants for scaled \(q\)-numerical ranges by a similarity representation. The available statement controls arbitrary matrices but does not give this rank-one trace-profile criterion or equality classification.

## Limitations
This is a rank-one classification. It neither improves the universal dilation coefficient nor determines optimal norm profiles for higher-rank operators. Literature comparisons found no covering statement, but an older equivalent rank-one optimization under different terminology remains a residual risk.

## References
1. M. Kaunisto, R. O'Loughlin, and J. Virtanen, *Dilation Theory for Scaled \(q\)-Numerical Ranges*, arXiv:2610.00443v1 (2026).
2. D. Denčić, H. Stanković, M. Krstić, and I. Damnjanović, *\(q\)-numerical radius of rank-one operators and the generalized Buzano inequality*, arXiv:2503.05036v1 (2025).
3. M. A. Aouichaoui and R. O'Loughlin, *Sharp spectral constants for scaled \(q\)-numerical ranges*, arXiv:2608.09866v1 (2026).
4. R. O'Loughlin and J. Rani, *\(q\)-Numerical Ranges and Spectral Sets*, arXiv:2603.15536v1 (2026).
