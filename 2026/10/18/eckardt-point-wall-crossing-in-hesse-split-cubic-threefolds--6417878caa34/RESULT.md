# Eckardt-point wall crossing in Hesse-split cubic threefolds

## Finding
Let \(A\in\mathbb C[x,y,z]\) be a homogeneous cubic defining a **smooth** plane cubic \(E=V(A)\subset\mathbb P^2_{\mathbb C}\). Define the smooth cubic threefold
\[
X_E=\big\{[x:y:z:u:v]\in\mathbb P^4_{\mathbb C}: A(x,y,z)+u^3+v^3=0\big\}.
\]
An *Eckardt point* (also called a *star point*) on a smooth cubic threefold is a point at which its tangent hyperplane section is a cone with that point as vertex. Then the number of **distinct geometric Eckardt points** is exactly
\[
\boxed{\#\operatorname{Eck}(X_E)=
\begin{cases}
12,&j(E)\ne0,\\
30,&j(E)=0.
\end{cases}}
\]
The result holds for every smooth complex plane cubic, not only a general member of a pencil. More precisely, in any Hesse normal form
\[
A_\lambda=x^3+y^3+z^3+\lambda xyz,\qquad \lambda^3\ne-27,
\]
there are always **nine** points lifted from the flexes of \(E\), plus **three** points supported in the \((u,v)\)-coordinate line. Exactly when \(\lambda=0\) or \(\lambda^3=216\), a further **eighteen** distinct points occur. These parameter values are precisely the smooth members with \(j(E)=0\).

## Assumptions and scope
The ground field is \(\mathbb C\), with the usual characteristic-zero notion of a smooth embedded cubic. All counts concern geometric projective **points**, without scheme-theoretic multiplicity. We impose no genericity besides smoothness of \(E\). The variables \(u,v\) occur in the fixed diagonal binary cubic \(u^3+v^3\); no claim is made for an arbitrary binary cubic with repeated roots, for singular \(E\), or for positive characteristic.

Changing coordinates in the \((x,y,z)\)-plane, and multiplying \(A\) by any nonzero scalar while rescaling \(u,v\) by a cube root, yields a projective isomorphism of the associated threefolds. Hence one may replace \(A\) by a Hesse normal form. For \(A_\lambda\), smoothness is equivalent to \(\lambda^3\ne-27\). In this case \(X_E\) is smooth: a singular point would force \(u=v=0\) by differentiation and then a singular point of \(E\).

## Proof
**Polar-rank characterization.** For a smooth cubic threefold, an Eckardt point \(P\) is equivalent to the polar quadric at \(P\) having rank at most two [1, Lemma 3.14]. Its quadratic matrix, up to a harmless nonzero scalar, is the Hessian of the defining cubic evaluated at \(P\). Put
\[
H_\lambda(x,y,z)=
\begin{pmatrix}
6x&\lambda z&\lambda y\\
\lambda z&6y&\lambda x\\
\lambda y&\lambda x&6z
\end{pmatrix}.
\]
At \(P=[x:y:z:u:v]\), the full matrix is the block diagonal matrix
\[
\operatorname{diag}\big(H_\lambda(x,y,z),6u,6v\big).
\]
We classify all points on \(X_E\) for which this matrix has rank at most two.

**Points supported only in \(u,v\).** If \((x,y,z)=(0,0,0)\), the equation is \(u^3+v^3=0\), giving exactly **three** points
\[
[0:0:0:1:\eta],\qquad \eta^3=-1.
\]
Each has polar rank two because neither \(u\) nor \(v\) is zero.

**Points with \(u=v=0\).** These lie on \(E_\lambda\). An exact polynomial identity is
\[
\det H_\lambda=-6\lambda^2 A_\lambda+8(\lambda^3+27)xyz.
\]
On \(E_\lambda\), and since \(\lambda^3+27\ne0\), the Hessian has rank at most two exactly when \(xyz=0\). The plane cubic meets each coordinate line in three reduced points. These are the **nine distinct points**
\[
[1:-\rho:0:0:0],\quad [1:0:-\rho:0:0],\quad
[0:1:-\rho:0:0],\qquad \rho^3=1.
\]
The three sets are disjoint. They are the classical nine flexes. Directly, their Hessian matrices have rank two, so all nine are Eckardt points of the threefold.

**No points with both \(u,v\ne0\) and nonzero plane coordinates.** In this case the last two diagonal blocks already contribute rank two, so the total-rank bound would require \(H_\lambda=0\). But its diagonal entries force \(x=y=z=0\), contrary to the assumed nonzero triple.

**Exactly one of \(u,v\) nonzero.** Now \((x,y,z)\ne(0,0,0)\), and the polar-rank bound is equivalent to \(\operatorname{rank}H_\lambda\le1\). The diagonal entries ensure the rank is actually one. If \(\lambda=0\), the matrix is diagonal and has rank one precisely at the three coordinate vertices
\[
q\in\{[1:0:0],[0:1:0],[0:0:1]\},
\]
where \(A_0(q)=1\) with the indicated normalization.

Suppose instead \(\lambda\ne0\). A rank-one point cannot have a zero coordinate: for example, if \(z=0\), the principal minors using the third row yield \(-\lambda^2y^2=0\) and \(-\lambda^2x^2=0\), forcing all coordinates to vanish. Thus \(xyz\ne0\). Three mixed minors of \(H_\lambda\) then impose
\[
\lambda xz=6y^2,\qquad \lambda xy=6z^2,\qquad \lambda yz=6x^2.
\]
Multiplying them and canceling \((xyz)^2\ne0\) gives \(\lambda^3=216\). Conversely, if \(\lambda=6c\) with \(c^3=1\), the displayed equations have **exactly three** projective solutions, obtained after normalizing \(x=1\):
\[
q_\rho=[1:\rho:c^2\rho^2],\qquad \rho^3=1.
\]
At each such point, direct substitution gives \(\operatorname{rank}H_\lambda(q_\rho)=1\) and \(A_\lambda(q_\rho)=9\).

For each of the three rank-one base points in either exceptional case, the equation of \(X_E\) forces the one nonzero tail coordinate to be a cube root of \(-A_\lambda(q)\). Since \(A_\lambda(q)=1\) or \(9\), there are **three distinct roots** and **two choices** of which tail coordinate is nonzero. This gives \(3\cdot3\cdot2=18\) additional points in each exceptional case. They are distinct from each other and from the preceding twelve by their support. In all other smooth parameters, there are no rank-one plane Hessian points and hence no additional Eckardt points.

**Intrinsic form of the jump.** Write the standard Hesse parameter as \(k=-\lambda/3\), so the plane cubic is \(x^3+y^3+z^3=3kxyz\). The classical modular invariant formula [2, equation (14)] gives
\[
\frac{j(E_\lambda)}{1728}
=\left(\frac{k(k^3+8)}{4(k^3-1)}\right)^3,
\qquad
j(E_\lambda)=\frac{\lambda^3(216-\lambda^3)^3}{(\lambda^3+27)^3}.
\]
For smooth parameters the denominator never vanishes. Therefore \(j(E_\lambda)=0\) **exactly** when \(\lambda=0\) or \(\lambda^3=216\), establishing the claimed moduli-invariant dichotomy.

## Verification
The accompanying `verify_hesse.py` uses exact SymPy expressions (including algebraic cube roots of unity) to check the Hessian determinant identity, the change-of-parameter modular identity, the on-curve and Hessian-rank conditions at all nine flexes for three parameter representatives, and the three rank-one base points at both exceptional parameters. Execute `python3 verify_hesse.py` with Python 3 and SymPy installed. The script prints `PASS` when all assertions hold.

The essential **infinite-parameter completeness** does not rely on finite sample checks: it follows from the algebraic rank case split and the three mixed-minor equations in the proof. SymPy checks support, but do not replace, those universally quantified arguments.

## Relationship to prior work
Bockondas and Bossoto [1] give the equivalence between Eckardt points and polar quadrics of rank at most two, together with explicit examples. Their Example 4.1 computes the **30** points of the Fermat cubic threefold; Section 5, Table 2 records **12** points for their single example with coefficient \(\lambda=3\). Those two examples do not determine the count for **every** smooth Hesse parameter or identify the exact jump locus as \(j(E)=0\). The present theorem uses their criterion but performs that parameter-uniform classification.

Bonifant and Milnor [2] classify complex plane cubics and compute the Hesse modular invariant. Their results by themselves classify curves, not Eckardt points on the associated **threefolds**. Cools and Coppens [3, Example 2.13] classify the star points of Fermat hypersurfaces, providing the known extremal **30-point** case, but not the non-Fermat Hesse-split threefolds.

## Limitations
This is a point-set classification for the specified split family over \(\mathbb C\), not a classification of all cubic threefolds. It neither determines the scheme structure of the Eckardt locus nor counts triple lines or intersection numbers of associated curves on the Fano surface. The endpoints where \(E\) is singular are excluded, and no statement is made about degeneration schemes there. The maximal case is consistent with the known uniqueness of the Fermat cubic threefold at 30 Eckardt points. Earlier or poorly indexed equivalent treatments of this particularly symmetric family cannot be absolutely excluded by a finite literature search; no independent audit of this theorem has been performed.

## References
[1] G. G. Bockondas and B. G. R. Bossoto, *Eckardt points on a cubic threefold*, arXiv:2309.08124, first released 2023-09-15; Lemma 3.14, Example 4.1 and Table 2. https://arxiv.org/abs/2309.08124

[2] A. Bonifant and J. Milnor, *On Real and Complex Cubic Curves*, arXiv:1603.09018, first released 2016-03-30; Hesse normal form, nine flexes and equation (14) for the modular invariant. https://arxiv.org/abs/1603.09018

[3] F. Cools and M. Coppens, *Star points on smooth hypersurfaces*, arXiv:0903.2005, first released 2009-03-11; Lemma 2.12 and Example 2.13. https://arxiv.org/abs/0903.2005
