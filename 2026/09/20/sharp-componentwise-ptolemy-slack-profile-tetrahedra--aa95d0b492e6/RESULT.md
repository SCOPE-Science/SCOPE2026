# Sharp componentwise Ptolemy-slack profile for tetrahedra

## Result

Let \(T=ABCD\) be a nondegenerate Euclidean tetrahedron, with volume \(V\),
circumradius \(R\), circumcenter \(O\), and centroid \(G\). Put
\[
x=AB\cdot CD,\qquad y=AC\cdot BD,\qquad z=AD\cdot BC,\qquad L=x+y+z.
\]
The three strict Ptolemy slacks are
\[
\sigma_x=y+z-x,\qquad
\sigma_y=z+x-y,\qquad
\sigma_z=x+y-z.
\]
Crelle's theorem says that \(x,y,z\) are the side lengths of a triangle of
area \(6RV\), so all three slacks are positive.

Define normalized slacks
\[
p_i=\frac{\sigma_i}{L},\qquad i\in\{x,y,z\},
\]
and the scale-invariant parameter
\[
\eta=\frac{2304R^2V^2}{L^4}.
\]

### 1. Slack-simplex identity and complete realizability

The normalized slacks form a positive probability vector:
\[
p_x+p_y+p_z=1,
\]
and satisfy the exact product identity
\[
\boxed{\quad
p_xp_yp_z=\frac{576R^2V^2}{L^4}=\frac{\eta}{4}.
\quad}
\tag{1}
\]
Consequently
\[
0<\eta\le \frac4{27}.
\tag{2}
\]

Conversely, every positive probability vector
\((p_1,p_2,p_3)\) occurs as the normalized Ptolemy-slack vector of a
disphenoid. More explicitly, set
\[
X=\frac{1-p_1}{2},\qquad
Y=\frac{1-p_2}{2},\qquad
Z=\frac{1-p_3}{2},
\]
and
\[
u_i=\sqrt{\frac{p_i}{8}}.
\]
The four points
\[
\begin{aligned}
A&=(u_1,u_2,u_3),&
B&=(u_1,-u_2,-u_3),\\
C&=(-u_1,u_2,-u_3),&
D&=(-u_1,-u_2,u_3)
\end{aligned}
\tag{3}
\]
form a nondegenerate disphenoid with
\[
AB^2=CD^2=X,\qquad
AC^2=BD^2=Y,\qquad
AD^2=BC^2=Z.
\]
Hence its opposite-edge products are \(X,Y,Z\), their sum is \(1\), and
their Ptolemy slacks are exactly \(p_1,p_2,p_3\).
Thus the normalized slack map is onto the whole open \(2\)-simplex, already
within the disphenoid family.

### 2. Exact componentwise profile at fixed \(R,V,L\)

For \(0<\eta<4/27\), let
\[
\alpha(\eta)\in(0,1/3),\qquad
\beta(\eta)\in(1/3,1)
\]
be the two roots in \((0,1)\) of
\[
t(1-t)^2=\eta.
\tag{4}
\]
At \(\eta=4/27\), set
\(\alpha(\eta)=\beta(\eta)=1/3\).
Then every one of the three Ptolemy slacks obeys the sharp bounds
\[
\boxed{\quad
\alpha(\eta)L\le \sigma_i\le \beta(\eta)L
\qquad(i=x,y,z).
\quad}
\tag{5}
\]

This is a complete profile, not merely a pair of endpoint estimates:
for every fixed admissible \(\eta\) and every
\(t\in[\alpha(\eta),\beta(\eta)]\), there exists a disphenoid with
that value of \(\eta\) and with one prescribed normalized slack equal to
\(t\).

An explicit closed form is obtained by putting
\[
\theta=\arccos\!\left(\frac{27\eta}{2}-1\right):
\]
\[
\alpha(\eta)=
\frac23+\frac23\cos\!\left(\frac{2\pi+\theta}{3}\right),\qquad
\beta(\eta)=
\frac23+\frac23\cos\!\left(\frac{2\pi-\theta}{3}\right).
\tag{6}
\]
The lower profile has the small-\(\eta\) expansion
\[
\alpha(\eta)=\eta+2\eta^2+7\eta^3+30\eta^4+O(\eta^5).
\tag{7}
\]
In particular, every tetrahedron satisfies the simpler quantitative
strict-Ptolemy bound
\[
\boxed{\quad
\sigma_i\ge
\frac{2304R^2V^2}{L^3}
\qquad(i=x,y,z),
\quad}
\tag{8}
\]
and the constant \(2304\) is asymptotically sharp along degenerating
disphenoids.

### 3. Exact defect identity for the tetrahedral \(d_3\) inequality

Let
\[
E=(AB-CD)^2+(AC-BD)^2+(AD-BC)^2.
\]
Then the product of the three Ptolemy slacks has the exact decomposition
\[
\boxed{\quad
\sigma_x\sigma_y\sigma_z-72V^2
=
\frac{36V^2}{L}\left(E+16\,OG^2\right).
\quad}
\tag{9}
\]
Thus the known inequality
\[
\sigma_x\sigma_y\sigma_z\ge 72V^2
\tag{10}
\]
has a sum-of-squares/center-displacement defect, and equality occurs
exactly for equifacial (disphenoid) tetrahedra.

## Proof

Crelle's theorem gives a triangle with side lengths \(x,y,z\) and area
\(K=6RV\). Heron's formula in its factored form gives
\[
16K^2
=(x+y+z)(-x+y+z)(x-y+z)(x+y-z)
=L\,\sigma_x\sigma_y\sigma_z.
\]
Since \(K^2=36R^2V^2\),
\[
L\,\sigma_x\sigma_y\sigma_z=576R^2V^2.
\tag{11}
\]
Also
\[
\sigma_x+\sigma_y+\sigma_z=L.
\tag{12}
\]
Dividing (11) by \(L^4\) proves (1), and AM--GM applied to the three
normalized slacks gives (2).

For the converse in Part 1, direct calculation from (3) gives
\[
AB^2=CD^2=4(u_2^2+u_3^2)=\frac{1-p_1}{2}=X
\]
and cyclically. Therefore the three opposite-edge products are \(X,Y,Z\),
and their slacks are \(p_1,p_2,p_3\). Positivity of the \(p_i\) makes
\(u_1u_2u_3>0\), so the tetrahedron is nondegenerate. This proves
surjectivity.

Now fix one normalized slack, say \(p_x=t\). The other two have
\[
p_y+p_z=1-t,\qquad
p_yp_z=\frac{\eta}{4t}.
\]
They are positive real numbers exactly when
\[
(1-t)^2-\frac{\eta}{t}\ge0,
\]
or equivalently
\[
t(1-t)^2\ge\eta.
\tag{13}
\]
On \((0,1)\), the function \(f(t)=t(1-t)^2\) increases from \(0\) to
\(4/27\) on \((0,1/3)\) and decreases from \(4/27\) to \(0\) on
\((1/3,1)\). Hence (13) is equivalent to
\[
t\in[\alpha(\eta),\beta(\eta)],
\]
which proves (5). Conversely, every \(t\) in this interval gives the two
positive roots
\[
p_{y,z}=
\frac{1-t\pm\sqrt{(1-t)^2-\eta/t}}{2}.
\tag{14}
\]
The disphenoid construction (3) then realizes the resulting probability
vector, proving sharpness and complete attainability. Formula (6) is the
trigonometric solution of the cubic (4), and (7) follows by series
inversion. Since \(\eta=\alpha(1-\alpha)^2\le\alpha\), (8) follows from
(5); (7) gives its asymptotic sharpness.

Finally, the standard centroid identity used in tetrahedral geometry is
\[
16R^2=
AB^2+AC^2+AD^2+BC^2+BD^2+CD^2+16\,OG^2.
\tag{15}
\]
Pairing opposite edges gives
\[
AB^2+CD^2=2AB\cdot CD+(AB-CD)^2
\]
and its two analogues, hence
\[
AB^2+AC^2+AD^2+BC^2+BD^2+CD^2=2L+E.
\tag{16}
\]
Equations (15)--(16) yield
\[
\frac{8R^2}{L}
=
1+\frac{E+16\,OG^2}{2L}.
\tag{17}
\]
From (11),
\[
\sigma_x\sigma_y\sigma_z
=72V^2\,\frac{8R^2}{L}.
\]
Substituting (17) proves (9). \(\square\)

## Context and originality boundary

The underlying ingredients are classical and are not claimed as new.
Crelle's 1821 theorem identifies the three products of opposite edge
lengths with the sides of a triangle and gives its area as \(6RV\).
Mazur and Petrenko (2011) use this Crelle triangle in their study of the
Atiyah--Sutcliffe conjectures, define
\[
d_3(x,y,z)=(x+y-z)(x+z-y)(y+z-x),
\]
and record the tetrahedral inequality
\(d_3\ge72V^2\), with equality for isosceles/equifacial tetrahedra.
Mazur (2018) gives a short proof of the same volume inequality and the
equivalent estimate \(8R^2\ge x+y+z\), using the centroid identity (15).
Minculete and Piscoran (2022) explicitly develop further tetrahedral
inequalities by applying plane-triangle inequalities to the Crelle
triangle. Recent general work on Ptolemy's inequality, such as
Gomez--Memoli (2024), addresses a different metric-space direction.

The contribution asserted here is the normalized slack-simplex
description with constructive surjectivity by disphenoids, the complete
sharp componentwise interval (5) at fixed \(\eta\) including attainment of
every intermediate value, and the exact defect decomposition (9).
No source located in the literature checked states these formulations or
an equivalent complete profile. Originality is therefore asserted only
**to the best of our knowledge**. The residual risk is material: the
proofs are short consequences of Crelle/Heron identities and elementary
symmetric-variable algebra, so equivalent statements may occur in older
triangle-inequality or solid-geometry literature under different
terminology.

## Limitations

- The result is for nondegenerate Euclidean tetrahedra. Degenerate
  configurations are represented only as limits.
- The sharp profile controls the three opposite-edge-product Ptolemy
  slacks, not the six individual edge lengths or a Hausdorff distance
  between tetrahedra.
- The parameter \(\eta\) uses the circumradius as well as volume and the
  sum of opposite-edge products; no claim is made that it is optimal for
  other notions of tetrahedral shape.
- The exact defect identity is an elementary refinement of identities
  already present in the proof framework of Mazur's inequality; its
  separate appearance in older literature cannot be excluded.

## References

1. A. L. Crelle, *Einige Bemerkungen uber die dreiseitige Pyramide*,
   Sammlung mathematischer Aufsatze u. Bemerkungen 1 (1821), 105--132.
   https://archive.org/details/sammlungmathemat01crel

2. M. Mazur and B. V. Petrenko, *On the conjectures of Atiyah and
   Sutcliffe*, arXiv:1102.4662v2 (2011).
   https://arxiv.org/abs/1102.4662

3. M. Mazur, *An Inequality for the Volume of a Tetrahedron*,
   American Mathematical Monthly 125 (2018), 273--275.
   https://doi.org/10.1080/00029890.2018.1411741

4. N. Minculete and L.-I. Piscoran, *Vectorial and metrical relations in
   tetrahedron*, Journal of Mathematical Inequalities 16 (2022),
   687--706.
   https://doi.org/10.7153/jmi-2022-16-49

5. M. Gomez and F. Memoli, *The Four Point Condition: An Elementary
   Tropicalization of Ptolemy's Inequality*, American Mathematical
   Monthly 131 (2024), 187--203.
   https://doi.org/10.1080/00029890.2023.2285695
