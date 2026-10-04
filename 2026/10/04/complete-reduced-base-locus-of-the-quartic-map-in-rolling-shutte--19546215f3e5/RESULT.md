# Complete reduced base locus of the quartic map in rolling-shutter Example 21
## Finding
For the homogeneous quartic coordinate representation \(\Phi=[F_0:F_1:F_2]\) printed in Example 21 of Hahn--Kohn--Marigliano--Pajdla, define
\[
d=X_0-X_3,\qquad q=2X_1X_2+X_3^2-X_0^2.
\]
Over \(\mathbb C\), the reduced projective base locus of the displayed base ideal \(I_\Phi=(F_0,F_1,F_2)\) is
\[
V(I_\Phi)_{\mathrm{red}}=\mathcal C\cup K\cup L_\infty\cup M_+\cup M_-.
\]
Here \(\mathcal C\) is the twisted cubic printed in Example 21, \(K=V(X_1,d)\) is the common rolling-plane line printed there,
\[
L_\infty=V(X_0,X_3),
\]
and, for \(r_\pm=\pm i\sqrt2\),
\[
M_r=V\bigl(2X_1-r(X_0-X_3),\;rX_2-X_0-X_3\bigr),\qquad r^2=-2.
\]
The two lines \(M_+\) and \(M_-\) are complex conjugate and have no real points. Hence
\[
V(I_\Phi)_{\mathrm{red}}(\mathbb R)=\mathcal C(\mathbb R)\cup K(\mathbb R)\cup L_\infty(\mathbb R).
\]
In addition, the displayed quartic linear system has exact generic base order three along \(K\):
\[
(F_0,F_1,F_2)\subset I_K^3,\qquad (F_0,F_1,F_2)\not\subset I_K^4.
\]

## Assumptions and scope
The calculation is over \(\mathbb C\) for the projective reduced base locus, using exactly the three homogeneous quartics printed in Example 21 of arXiv:2403.11295v2. The real-locus statement is obtained by taking real points of that reduced support. The phrase “base order three along \(K\)” means the minimum \(I_K\)-adic order of the three displayed coordinate quartics at the generic point of \(K\) is three.

No claim is made about a primary decomposition of \(I_\Phi\), embedded components, scheme-theoretic multiplicities of the reduced components, or a resolution of \(\Phi\). The source's statement that \(\mathcal C\) and \(K\) lie in the base locus remains correct; the result here determines the full reduced support of this particular displayed homogeneous base ideal.

## Proof
Write the three quartics from Example 21 as \(F_0,F_1,F_2\). Direct exact expansion gives
\[
F_0=X_1dq,\qquad F_2=d^2q.
\]
Therefore every common zero lies either on \(V(d)\) or on the smooth quadric \(Q=V(q)\).

On \(V(d)\), substituting \(X_3=X_0\) into the middle coordinate gives
\[
F_1\big|_{d=0}=-2X_0X_1^3.
\]
Thus the reduced base set on this hyperplane is exactly
\[
V(d,X_1)\cup V(d,X_0)=K\cup L_\infty.
\]

For the quadric \(Q\), use the Segre parametrization
\[
\psi([s:t],[u:v])=(2su:2tv:tu-2sv:tu+2sv).
\]
It satisfies \(q\circ\psi=0\). Put
\[
h=2suv-tu^2-4tv^2.
\]
Exact substitution gives
\[
F_1\circ\psi=16s^3(u^2+2v^2)h.
\]
The three quadrics defining the source's twisted cubic \(\mathcal C\) pull back to
\[
-2sh,\qquad -2th,\qquad 0.
\]
Hence \(h=0\) is precisely \(\psi^{-1}(\mathcal C)\). The factor \(s=0\) maps precisely to \(K\). The remaining factor \(u^2+2v^2=0\) is the union of two fibers of the second \(\mathbb P^1\)-factor. If \(u=rv\) with \(r^2=-2\), their images satisfy
\[
2X_1=r(X_0-X_3),\qquad rX_2=X_0+X_3,
\]
which are the two lines \(M_\pm\) displayed above. Since \(Q\cong\mathbb P^1\times\mathbb P^1\), this factorization exhausts the reduced base set on \(Q\), and together with the \(d=0\) calculation exhausts all of \(V(I_\Phi)_{\mathrm{red}}\).

For real coordinates, \(u^2+2v^2=0\) has no projective real solution, proving the real-locus assertion.

Finally, with \(I_K=(X_1,d)\), the factorization of \(q\) as
\[
q=2X_1X_2-d(X_0+X_3)
\]
shows \(F_0\in I_K^3\) and \(F_2\in I_K^3\). Replacing \(X_3\) by \(X_0-d\) in \(F_1\) yields
\[
F_1=2d^3X_1-d^3X_2-3d^2X_0X_1+2dX_1^3-2X_0X_1^3.
\]
Every term has \((X_1,d)\)-degree at least three, while the final term has degree exactly three and nonzero coefficient at the generic point of \(K\). Thus the generic base order is exactly three.

## Verification
The accompanying `verify.py` uses only Python's standard library and exact sparse integer polynomial arithmetic. It reconstructs the three printed quartics, verifies the two global factorizations, the hyperplane restriction, the Segre identity, the complete factorization of \(F_1\circ\psi\), the pullbacks of the three twisted-cubic quadrics, and the exact \(I_K\)-adic order calculation. Running it prints `VERIFY_OK`.

## Relationship to prior work
Hahn--Kohn--Marigliano--Pajdla define Example 21, print its twisted cubic \(\mathcal C\), its rolling-plane line \(K\), and the three quartics of \(\Phi\). In their proof of Lemma 54 they explicitly note that both \(\mathcal C\) and \(K\) lie in the base locus. Their Appendix proof of Proposition 20 uses Example 21 to observe that the three quartics have no common factor. The inspected source does not state that \(\mathcal C\cup K\) is the complete base locus and does not give the two further real/complex line types or the generic order-three calculation along \(K\).

Trager--Sturmfels--Canny--Hebert provide a broader algebraic framework for rational camera maps and multi-slit projections, but the inspected material does not specialize to this rolling-shutter Example 21 or imply the displayed five-component reduced base locus. Searches of the published published-finding corpus index for the source, the complete base-locus formulation, aliases involving the twisted cubic and line \(K\), and quartic-camera base ideals did not return a statement implying this result. The closest returned published-finding corpus item concerns quartic plane Cremona maps over a finite field and has different source, ambient map, and base geometry.

## Limitations
The result is coordinate-specific to the homogeneous quartic representation printed for Example 21. It does not compute the full scheme-theoretic primary decomposition, embedded components, component multiplicities, blowups, or exceptional divisors. The originality assessment is limited by the inspected primary and supporting sources and semantic database searches; absence from those searches is not a proof of global novelty.

## References
1. M. A. Hahn, K. Kohn, O. Marigliano, T. Pajdla, *Order-One Rolling Shutter Cameras*, arXiv:2403.11295. First public version: 2024-03-17. Example 21 and the proof of Lemma 54 are the primary source material.
2. M. Trager, B. Sturmfels, J. Canny, M. Hebert, J. Ponce, *General Models for Rational Cameras and the Case of Two-Slit Projections*, arXiv:1612.01160.
