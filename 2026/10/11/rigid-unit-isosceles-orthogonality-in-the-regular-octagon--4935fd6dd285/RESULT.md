# Rigid unit isosceles orthogonality in the regular octagon
## Finding
Let
\[
X_8=(\mathbb R^2,N_8),
\qquad
N_8(s,t)
=
\max\left\{
|s|,
|t|,
\frac{|s|+|t|}{\sqrt2}
\right\},
\]
whose unit ball is the Euclidean regular octagon, and let
\[
R(s,t)=(-t,s).
\]
Then for every pair
\[
x,y\in S_{X_8},
\]
one has
\[
\boxed{
N_8(x+y)=N_8(x-y)
\quad\Longleftrightarrow\quad
y=Rx\ \text{or}\ y=-Rx.
}
\tag{1}
\]
In particular, every unit isosceles-orthogonal pair has the same two chord lengths:
\[
\boxed{
N_8(x+y)=N_8(x-y)=\sqrt2.
}
\tag{2}
\]

## Assumptions and scope
All scalars are real. Isosceles orthogonality is
\[
x\perp_I y
\quad\Longleftrightarrow\quad
N_8(x+y)=N_8(x-y).
\]

Put
\[
r=\sqrt2-1,
\qquad
d=2-\sqrt2=1-r.
\]
The consecutive vertices in the upper and left half of the unit octagon are
\[
v_0=(1,r),\quad
v_1=(r,1),\quad
v_2=(-r,1),\quad
v_3=(-1,r),
\]
and
\[
v_{j+4}=-v_j.
\]
Let
\[
E_j=[v_j,v_{j+1}],
\]
with indices modulo \(8\).

The dihedral symmetry group of the regular octagon acts transitively on its edges. Hence, after a norm isometry and possibly interchanging edge endpoints, it suffices to put
\[
x=x(a)=v_0+a(v_1-v_0)
=
(1-da,\ r+da),
\qquad
0\le a\le1.
\tag{3}
\]

## Proof
Write
\[
F(x,y)=N_8(x+y)-N_8(x-y).
\]
We classify the zeros of \(F\) edge by edge.

First suppose
\[
y\in E_0.
\]
Writing
\[
y=v_0+b(v_1-v_0),
\qquad
0\le b\le1,
\]
both \(x\) and \(y\) lie on the same facet
\[
s+t=\sqrt2.
\]
Therefore
\[
N_8(x+y)=2.
\]
Also
\[
x-y=d(b-a)(1,-1),
\]
and
\[
N_8(1,-1)=\sqrt2.
\]
Hence
\[
N_8(x-y)=\sqrt2\,d|a-b|
=
2(\sqrt2-1)|a-b|
<2.
\]
Thus
\[
F(x,y)>0
\quad\text{on }E_0.
\tag{4}
\]

Now let
\[
y\in E_1.
\]
Then
\[
y=(r-2rb,1).
\]
A direct substitution gives
\[
x+y=
(\sqrt2-da-2rb,\ \sqrt2+da).
\]
Both coordinates are nonnegative, and hence
\[
N_8(x+y)
=
\max\{\sqrt2+da,\ 2-db\}
\ge\sqrt2.
\tag{5}
\]
On the other hand,
\[
x-y=
(d(1-a)+2rb,\ -d(1-a)).
\]
The first absolute coordinate is at most \(\sqrt2\), the second is at most \(d\), and
\[
|x_1-y_1|+|x_2-y_2|
=
2d(1-a)+2rb
\le2.
\]
Consequently
\[
N_8(x-y)\le\sqrt2.
\tag{6}
\]
Equality in both (5) and (6) occurs exactly at
\[
(a,b)=(0,1).
\]
Thus
\[
F(x,y)\ge0\text{ on }E_1,
\]
with equality only at
\[
x=v_0,\qquad y=v_2=Rv_0.
\tag{7}
\]

The decisive branch is
\[
y\in E_2.
\]
Write
\[
y=(-r-db,\ 1-db)
\]
and put
\[
\delta=a-b,
\qquad
w=d(1-a-b).
\]
Then
\[
x+y=(w,\ \sqrt2+d\delta),
\]
while
\[
x-y=(\sqrt2-d\delta,\ -w).
\tag{8}
\]
The octagonal norm is invariant under coordinate interchange and coordinate sign changes. Hence
\[
N_8(x+y)=N_8(\sqrt2+d\delta,w),
\]
and
\[
N_8(x-y)=N_8(\sqrt2-d\delta,w).
\]
Because
\[
|w|\le d
<
2(\sqrt2-1)
\le
\sqrt2\pm d\delta,
\]
the function
\[
z\longmapsto N_8(z,w)
=
\max\left\{
z,\,
\frac{z+|w|}{\sqrt2}
\right\}
\]
is strictly increasing on the whole relevant interval. Therefore
\[
\operatorname{sgn}F(x,y)
=
\operatorname{sgn}(a-b).
\tag{9}
\]
Thus equality on \(E_2\) occurs exactly when
\[
a=b.
\]
But
\[
v_2+a(v_3-v_2)
=
R\bigl(v_0+a(v_1-v_0)\bigr),
\]
so this equality family is precisely
\[
y=Rx.
\tag{10}
\]

Next let
\[
y\in E_3.
\]
Then
\[
y=(-1,\ r-2rb).
\]
One has
\[
x+y=(-da,\ 2r+da-2rb).
\]
Both absolute coordinates are at most \(\sqrt2\), and their sum is at most \(2\), so
\[
N_8(x+y)\le\sqrt2.
\tag{11}
\]
Meanwhile
\[
x-y=(2-da,\ da+2rb),
\]
whose first coordinate is at least \(\sqrt2\). Hence
\[
N_8(x-y)\ge\sqrt2.
\tag{12}
\]
Equality in both (11) and (12) occurs exactly at
\[
(a,b)=(1,0),
\]
which is again the shared endpoint of the family \(y=Rx\). Therefore
\[
F(x,y)\le0\text{ on }E_3,
\]
with no new zero.

The remaining four edges follow by central symmetry. Replacing \(y\) by \(-y\) interchanges the two chord norms, so
\[
F(x,-y)=-F(x,y).
\]
Thus \(E_4\) has no zero; \(E_5\) and \(E_7\) have only endpoint zeros already represented by the adjacent branch; and on \(E_6=-E_2\) equality occurs exactly when
\[
y=-Rx.
\tag{13}
\]
This exhausts the unit sphere and proves (1).

Finally, for \(x=x(a)\),
\[
Rx=(-r-da,\ 1-da).
\]
Therefore
\[
x+Rx=(d(1-2a),\sqrt2),
\]
and
\[
x-Rx=(\sqrt2,d(2a-1)).
\]
Since
\[
|d(1-2a)|\le d
\]
and
\[
\frac{\sqrt2+d}{\sqrt2}=\sqrt2,
\]
both vectors have octagonal norm exactly \(\sqrt2\). This proves (2).

## Verification
The bundled `verify.py` uses exact arithmetic in
\[
\mathbb Q(\sqrt2).
\]
It reconstructs all eight edges, verifies the quarter-turn identities
\[
E_2(a)=R(E_0(a)),
\qquad
E_6(a)=-R(E_0(a)),
\]
and checks the sign pattern of
\[
F(x,y)=N_8(x+y)-N_8(x-y)
\]
on all eight relative edge classes on an exact rational grid. It also verifies exactly that every classified equality pair has both chord norms equal to \(\sqrt2\).

The finite grid is only a replay check. Exhaustiveness comes from the analytic edge proof above: equations (4)--(13) determine the sign and equality set on every closed edge.

## Relationship to prior work
Chen, Yang, Liu and Li introduced a James-type constant based on unit isosceles-orthogonal pairs in 2022, motivating exact understanding of such pairs rather than only arbitrary unit pairs. Sain, Ghosh and Paul subsequently connected James-constant attainment to isosceles orthogonality and proved attainment results for two-dimensional polyhedral Banach spaces.

Those general results determine extremal scalar information once the James constant of a particular polygon is known, but they do not classify the complete unit isosceles-orthogonality relation. The present result is stronger in a different direction: every admissible unit pair in the regular octagon is forced to be a quarter-turn pair, and therefore every admissible common chord has the same length.

Published exact computations for the regular octagon concerning von Neumann--Jordan profiles, angle moduli, Ptolemy constants, and other James-type quantities also optimize different functions over larger or differently constrained pair sets. They do not imply the equivalence in (1).

## Limitations
The rigidity statement is proved only for unit vectors in the regular-octagonal norm. It does not classify non-unit isosceles-orthogonal pairs.

No analogous quarter-turn classification is asserted for arbitrary regular polygons. In particular, the proof uses the special three-facet description of the regular-octagonal norm.

Literature and semantic-index searches cannot establish absolute novelty. An equivalent classification could exist under a different affine normalization or under terminology focused on the orthogonality graph rather than geometric constants.

## References
1. B. Chen, Z. Yang, Q. Liu and Y. Li, “Some New James Type Geometric Constants in Banach Spaces,” *Symmetry* 14 (2022), 405, doi:10.3390/sym14020405. Published 18 February 2022.
2. D. Sain, S. Ghosh and K. Paul, “On isosceles orthogonality and some geometric constants in a normed space,” *Aequationes Mathematicae* 97 (2023), 147--160, doi:10.1007/s00010-022-00909-y. Published online 1 September 2022.
