# Pinch points hidden by representation-dependent rank on a quartic symmetroid
## Finding
Over \(\mathbb C\), consider the quartic surface \(S=V(F)\subset\mathbb P^3\) from Example 9.6 of Helsø's *Rational Quartic Symmetroids*. The source gives two nonconjugate symmetric matrix representations \(A_1\) and \(A_2\) with the same determinant and notes that their rank-\(2\) loci differ.

The intrinsic singular locus of \(S\) is
\[
L_a\cup L_b\cup\{N_0,N_1,N_3,N_4\},
\]
where
\[
L_a=V(x_1,x_0-4x_3),\qquad L_b=V(x_3,x_0+4x_1),
\]
and
\[
N_0=[1:0:0:0],\quad N_1=[0:1:0:0],\quad N_3=[0:0:0:1],\quad N_4=[-4:1:0:-1].
\]
The four isolated points are ordinary nodes. Each double line contains exactly two pinch points:
\[
[4:0:i:1],\ [4:0:-i:1]\in L_a,\qquad [-4:1:i:0],\ [-4:1:-i:0]\in L_b.
\]
Away from these four points and from \(L_a\cap L_b\), a point of either line is an ordinary transverse double-curve point. At every listed pinch point the analytic germ is a Whitney pinch point \(W^2-a^2h=0\). At \(p=L_a\cap L_b=[0:0:1:0]\), the completed local equation is analytically equivalent to \(U^2-a^2b^2=0\).

For \(A_1\), \(L_b\) has matrix rank \(2\) everywhere, while \(L_a\) has generic rank \(3\) and drops to rank \(2\) exactly at \([4:0:\pm i:1]\). For \(A_2\), the roles of the two lines are reversed. Thus the pinch set is intrinsic although the determinantal rank stratification is not.

## Assumptions and scope
The ground field is \(\mathbb C\), and analytic equivalence is taken in the complex analytic category; the same completed normal forms hold formally. The finding concerns only the specific quartic in Example 9.6.

The common determinant is
\[
\begin{aligned}
F={}&4x_0^2x_1x_3+x_0^2x_2^2+16x_0x_1^2x_3+8x_0x_1x_2^2-16x_0x_1x_3^2-8x_0x_2^2x_3\\
&+16x_1^2x_2^2-64x_1^2x_3^2-32x_1x_2^2x_3+16x_2^2x_3^2.
\end{aligned}
\]

## Proof
Differentiation gives
\[
\frac{\partial F}{\partial x_2}=2x_2(x_0+4x_1-4x_3)^2.
\]
On \(x_0+4x_1-4x_3=0\), the remaining derivatives reduce to scalar multiples of \(x_1x_3(x_1-x_3)\) and \(x_1x_3(x_1+x_3)\), hence \(x_1x_3=0\) and the singular points there are exactly \(L_a\cup L_b\). On \(x_2=0\), the remaining derivative factors are
\[
x_1x_3(x_0+2x_1-2x_3),\quad x_3(x_0+8x_1)(x_0-4x_3),\quad x_1(x_0+4x_1)(x_0-8x_3).
\]
A projective case split yields only the two already-listed line points together with \(N_0,N_1,N_3,N_4\). The projective Hessian has rank \(3\) at each \(N_j\), so these are ordinary nodes.

On \(L_a\), use \(x_3=1\), \(x_0=4+w\), \(x_1=a\), \(x_2=t\). Then
\[
F=(t^2+4a)w^2+8a(2a+t^2+2)w+16a^2t^2,
\]
whose discriminant in \(w\) is
\[
256a^2(a^2+2a+t^2+1).
\]
At \(a=0\), this vanishes exactly for \(t=\pm i\). There \(t^2+4a\) is a unit and \(h=a^2+2a+t^2+1\) is a local coordinate because \(\partial h/\partial t=2t\ne0\). Completing the square gives \(W^2-a^2h=0\). The identical computation on \(L_b\), in the chart \(x_1=1\) with \(x_0=-4+w\), gives the two points \([-4:1:\pm i:0]\). Away from \(t^2+1=0\), the transverse Hessian has rank \(2\), giving an ordinary transverse double-curve germ.

At \(p=[0:0:1:0]\), use \(x_2=1\), set \(a=x_1\), \(b=x_3\), and \(u=x_0+4a-4b\). Then
\[
F=(1+4ab)u^2+16ab(b-a)u-64a^2b^2,
\]
with discriminant \(256a^2b^2(1+(a+b)^2)\). The two factors \(1+4ab\) and \(1+(a+b)^2\) are units at the origin, so completion of the square yields \(U^2-a^2b^2=0\).

Finally, the \(3\times3\) minors of \(A_1\) vanish identically on \(L_b\), while on \(L_a\) their common nonconstant factor is \(t^2+1\). For \(A_2\) the roles reverse. Hence the generically rank-\(3\) line in each representation drops to rank \(2\) exactly at its two intrinsic pinch points.

## Verification
The standalone script `verify.py` reconstructs both matrices, checks determinant equality, the derivative factorizations, all four node Hessian ranks, the line-Hessian rank drops, both pinch discriminants, the line-intersection discriminant, and the \(3\times3\)-minor rank behavior. Running `python verify.py` returns `VERIFY_OK`.

## Relationship to prior work
Helsø's Example 9.6 states that the same quartic has two singular lines, four isolated nodes, and two nonconjugate symmetric-matrix representations with different rank-\(2\) loci. The paper does not identify pinch points or Whitney local forms; full-text searches for “pinch” and “Whitney” return no occurrence. Helsø--Ranestad later summarize rational quartic symmetroid families and discuss intersecting singular lines, but the inspected statements do not give this named example's local analytic stratification or connect its representation-dependent rank drops with intrinsic pinch points.

The new content is the exact local stratification of Example 9.6: the four pinch-point coordinates, the intersection normal form, and the exact coincidence between intrinsic pinch points and isolated rank drops on whichever line is generically rank \(3\) in the chosen representation.

## Limitations
This does not classify all quartic symmetroids with double curves. Classical literature may contain general results on pinch points of quartic double lines; such literature was not exhaustively inspected. The claim is therefore restricted to this exact named example and its two displayed determinant representations. No claim is made about real pinch points or spectrahedral realizability.

## References
1. M. Helsø, *Rational Quartic Symmetroids*, arXiv:1708.04101v1, first posted 2017-08-14; DOI:10.1515/advgeom-2018-0037. See Remark 2.1 and Example 9.6.
2. M. Helsø and K. Ranestad, *Rational Quartic Spectrahedra*, arXiv:1810.11235v1, first posted 2018-10-26.
