# Rigidity and phase transition of modified von Neumann--Jordan extremizers in a classical octagonal family
## Finding
For \(\frac12<\beta<1\), define
\[
N_\beta(u,v)=\max\{|u|,|v|,\beta(|u|+|v|)\},
\qquad
c_\beta=\frac{1-\beta}{\beta}.
\]
For
\[
C'_{\mathrm{NJ}}(X_\beta)
=
\sup_{x,y\in S_{X_\beta}}
\frac{N_\beta(x+y)^2+N_\beta(x-y)^2}{4},
\]
the known value is
\[
C'_{\mathrm{NJ}}(X_\beta)=
\begin{cases}
1+c_\beta^2,&\frac12<\beta\le\frac1{\sqrt2},\\[2mm]
2\bigl(\beta^2+(1-\beta)^2\bigr),&\frac1{\sqrt2}<\beta<1.
\end{cases}
\]
The complete equality set is as follows.

If
\[
\frac12<\beta<\frac1{\sqrt2},
\]
then equality holds exactly when, up to a common signed-coordinate permutation, exchanging \(x\) and \(y\), and changing the sign of either vector,
\[
(x,y)=\bigl((1,c_\beta),(1,-c_\beta)\bigr).
\]

If
\[
\frac1{\sqrt2}<\beta<1,
\]
then equality holds exactly when, under the same equivalences,
\[
(x,y)=\bigl((1,c_\beta),(c_\beta,1)\bigr).
\]

At
\[
\beta=\frac1{\sqrt2},
\]
the equality set is the union of these two coordinate classes.

## Assumptions and scope
The scalar field is real. The endpoints \(\beta=1/2\) and \(\beta=1\) are excluded because the octagon degenerates to a square or diamond and the equality set changes dimension.

The unit ball has the eight vertices
\[
(\pm1,\pm c_\beta),\qquad(\pm c_\beta,\pm1),
\]
with independent signs. Signed coordinate permutations are linear isometries for every parameter in the stated interval.

Write
\[
E(u,v)=\sqrt{u^2+v^2},
\qquad
M_2=\sqrt{1+c_\beta^2}.
\]
Every vertex has Euclidean norm \(M_2\).

## Proof
The first comparison is
\[
E(z)\le M_2N_\beta(z)
\qquad(z\in\mathbb R^2).
\]
Indeed, on \(N_\beta(z)=1\) the vector \(z\) lies on the boundary of the convex octagon. The Euclidean squared norm is strictly convex along every nondegenerate edge, so its maximum on each edge is attained only at an endpoint. Since all eight vertices have Euclidean norm \(M_2\),
\[
E(z)\le M_2N_\beta(z),
\]
and equality for nonzero \(z\) holds exactly on vertex rays.

### The regime \(\frac12<\beta<1/\sqrt2\)

For every \(z=(u,v)\),
\[
N_\beta(z)\le E(z).
\]
The coordinate terms satisfy \(\max\{|u|,|v|\}\le E(z)\). Also
\[
\beta(|u|+|v|)
\le \beta\sqrt2\,E(z)
<E(z)
\]
whenever both coordinates are nonzero. Hence equality in
\[
N_\beta(z)\le E(z)
\]
for nonzero \(z\) occurs exactly on the coordinate axes.

For \(x,y\in S_{X_\beta}\),
\[
\begin{aligned}
N_\beta(x+y)^2+N_\beta(x-y)^2
&\le E(x+y)^2+E(x-y)^2\\
&=2E(x)^2+2E(y)^2\\
&\le4M_2^2.
\end{aligned}
\]
Therefore
\[
C'_{\mathrm{NJ}}(X_\beta)\le M_2^2.
\]
The known value is \(M_2^2\), so equality in the modified von Neumann--Jordan functional forces equality in every displayed inequality. Thus \(x\) and \(y\) lie on vertex rays; because they are \(N_\beta\)-unit, they are vertices. Moreover, both \(x+y\) and \(x-y\), when nonzero, lie on coordinate axes.

After a common signed-coordinate permutation, take
\[
x=(1,c_\beta).
\]
Among the eight vertices, requiring both sum and difference to be coordinate-axis vectors forces
\[
y=(1,-c_\beta)
\quad\text{or}\quad
y=(-1,c_\beta).
\]
These two are equivalent by changing the sign of \(y\). This proves the first classification.

### The regime \(1/\sqrt2<\beta<1\)

For a nonzero vector \(z\), let
\[
a=\max\{|u|,|v|\},\qquad
t=\frac{\min\{|u|,|v|\}}{a}\in[0,1].
\]
Then
\[
\frac{N_\beta(z)}{E(z)}
=
\frac{\max\{1,\beta(1+t)\}}{\sqrt{1+t^2}}.
\]
The first branch is at most \(1<\sqrt2\,\beta\). On the second branch,
\[
\frac{\beta(1+t)}{\sqrt{1+t^2}}
\]
is strictly increasing for \(0\le t<1\), so
\[
N_\beta(z)\le \sqrt2\,\beta\,E(z),
\]
with equality for nonzero \(z\) exactly on the diagonal rays
\[
|u|=|v|.
\]

Consequently, for \(x,y\in S_{X_\beta}\),
\[
\begin{aligned}
N_\beta(x+y)^2+N_\beta(x-y)^2
&\le2\beta^2\bigl(E(x+y)^2+E(x-y)^2\bigr)\\
&=4\beta^2\bigl(E(x)^2+E(y)^2\bigr)\\
&\le8\beta^2M_2^2.
\end{aligned}
\]
Dividing by \(4\) gives
\[
C'_{\mathrm{NJ}}(X_\beta)
\le2\beta^2M_2^2
=
2\bigl(\beta^2+(1-\beta)^2\bigr),
\]
which is the known sharp value.

Equality again forces \(x\) and \(y\) to be vertices and both \(x+y\) and \(x-y\), when nonzero, to lie on diagonal rays. Put \(x=(1,c_\beta)\) after a common signed-coordinate permutation. The exact diagonal conditions
\[
|x_1+y_1|=|x_2+y_2|,
\qquad
|x_1-y_1|=|x_2-y_2|
\]
leave, among the eight vertices, only
\[
y=(c_\beta,1)
\quad\text{or}\quad
y=(-c_\beta,-1).
\]
These are equivalent by sign change of \(y\). This proves the second classification.

### The transition \(\beta=1/\sqrt2\)

At the transition,
\[
N_\beta(z)\le E(z)
\]
still holds, but equality for nonzero \(z\) occurs exactly on the union of the coordinate-axis and diagonal rays. Equality in the same parallelogram chain still forces \(x\) and \(y\) to be vertices. Fixing \(x=(1,c_\beta)\), the exact vertex check then gives precisely the two classes already displayed: the coordinate-reflected class and the coordinate-swapped class. No other vertex pair survives.

## Verification
The proof is an equality analysis of two sharp Euclidean norm comparisons and the exact parallelogram identity
\[
E(x+y)^2+E(x-y)^2=2E(x)^2+2E(y)^2.
\]
It does not infer an infinite statement from finite sampling.

The only finite step occurs after equality has already forced both vectors to the eight vertices. That eight-vertex check is exhaustive and can be replaced by the two displayed coordinate equations.

The value formulas agree with Mizuguchi--Saito's Example 4.4:
\[
C'_{\mathrm{NJ}}=
\frac{\beta^2+(1-\beta)^2}{\beta^2}
\]
up to \(\beta=1/\sqrt2\), and
\[
C'_{\mathrm{NJ}}
=
2\bigl(\beta^2+(1-\beta)^2\bigr)
\]
above it.

## Relationship to prior work
Mizuguchi and Saito compute the modified von Neumann--Jordan constant for exactly this family in Example 4.4 of their 2011 paper. Their proof uses Euclidean comparison constants \(M_1\) and \(M_2\) and identifies the same threshold \(\beta=1/\sqrt2\). The inspected example states the sharp values but does not state the complete set of equality pairs or the change in their geometric type.

Their general Proposition 2.1 supplies the sharp comparison argument in the lower-parameter regime, and Proposition 2.3 supplies the value mechanism in the upper regime. The classification here retains equality conditions throughout those inequalities and resolves them explicitly on the octagonal boundary.

Later work on extreme absolute normalized norms reports modified von Neumann--Jordan constants for broad classes of extreme norms, while later work on upper bounds studies when geometric constants reach global envelopes. The inspected public descriptions do not state the parameterwise equality-pair classification above.

## Limitations
The theorem classifies extremizers only for the classical octagonal family with \(1/2<\beta<1\). It deliberately excludes the degenerate square and diamond endpoints.

The originality comparison is strongest against the full 2011 source. A later or differently indexed source could contain an equality-case observation not exposed by the checked public descriptions; this remains a bibliographic risk.

## References
1. H. Mizuguchi and K.-S. Saito, “Some geometric constants of absolute normalized norms on \(\mathbb R^2\),” *Annals of Functional Analysis* 2 (2011), 22--33, DOI 10.15352/afa/1399900191.
2. H. Mizuguchi and K.-S. Saito, “On the upper bound of some geometric constants of absolute normalized norms on \(\mathbb R^2\),” *Mediterranean Journal of Mathematics* 13 (2016), 1067--1079, DOI 10.1007/s00009-014-0485-z.
3. N. Komuro, K.-I. Mitani, and T. Okazaki, “Geometrical constants of 2-dimensional spaces with extreme norms in \(\mathcal{AN}_2\),” *RIMS Kokyuroku* 2260 (2023), 129--136.
