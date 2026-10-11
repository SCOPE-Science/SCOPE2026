# Complete generalized Zbăganu profile of the affine-regular hexagonal plane
## Finding
Let
\[
X_H=(\mathbb R^2,N),
\qquad
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
This is the affine-regular hexagonal Banach plane.

For \(\lambda,\mu>0\), the generalized Zbăganu constant of Liu, Sarfraz and Li is
\[
C_Z(\lambda,\mu,X)
=
\sup_{(x,y)\ne(0,0)}
\frac{2\|\lambda x+\mu y\|\,\|\mu x-\lambda y\|}
{(\lambda^2+\mu^2)(\|x\|^2+\|y\|^2)}.
\]
Put
\[
r=\frac{\min\{\lambda,\mu\}}{\max\{\lambda,\mu\}}
\in(0,1],
\qquad
r_*=\sqrt{\frac{\sqrt5-1}{2}}.
\]
Then
\[
C_Z(\lambda,\mu,X_H)
=
\begin{cases}
\dfrac{r+\sqrt{1+r^2}}{1+r^2},
&0<r\le r_*,
\\[6pt]
\dfrac{1+3r^2+r^4}{2r(1+r^2)},
&r_*\le r\le1.
\end{cases}
\]
The transition is exact:
\[
r_*^4+r_*^2=1.
\]
At the symmetric point,
\[
C_Z(1,1,X_H)=\frac54.
\]

## Assumptions and scope
The space is real and two-dimensional. The parameter pair satisfies
\[
\lambda,\mu>0.
\]
The definition is invariant under a common rescaling of \((\lambda,\mu)\), and interchanging \(\lambda,\mu\) is compensated by interchanging \(x,y\). Hence it is enough to set
\[
\lambda=1,\qquad \mu=r,\qquad 0<r\le1.
\]

Use the linear embedding
\[
T(s,t)=(s,t,s-t).
\]
Its image is the plane
\[
H=\{(a,b,c)\in\mathbb R^3:a-b-c=0\},
\]
and
\[
N(s,t)=\|T(s,t)\|_\infty.
\]
For the three coordinate functionals \(e_1,e_2,e_3\) restricted to \(H\), the dual norm has the elementary property that for distinct \(i,j\), signs \(\sigma,\tau\in\{-1,1\}\), and \(a,b\ge0\), the two numbers
\[
\|\sigma a e_i+\tau b e_j\|_*,
\qquad
\|\sigma a e_i-\tau b e_j\|_*
\]
are, in some order,
\[
a+b,\qquad \max\{a,b\}.
\]
This follows directly from the six vertices
\[
(1,0),\ (1,1),\ (0,1),\ (-1,0),\ (-1,-1),\ (0,-1)
\]
of the unit ball in the original coordinates.

## Proof
Write
\[
p=N(x),\qquad q=N(y),
\]
and, in the three-coordinate model,
\[
u=T(x),\qquad v=T(y).
\]
Set
\[
A=N(x+ry),
\qquad
B=N(rx-y).
\]
Choose coordinate indices \(i,j\) and signs \(\sigma,\tau\) so that
\[
A=\sigma(u_i+rv_i),
\qquad
B=\tau(ru_j-v_j),
\]
with both displayed quantities nonnegative.

If \(i=j\), then
\[
2AB
\le
(u_i+rv_i)^2+(ru_i-v_i)^2
=
(1+r^2)(u_i^2+v_i^2)
\le
(1+r^2)(p^2+q^2).
\]
Thus this case contributes at most \(1\), below the claimed profile.

Assume \(i\ne j\). For every \(\kappa>0\),
\[
AB
\le
\frac14\left(\kappa A+\kappa^{-1}B\right)^2.
\]
The expression in parentheses splits into one functional of \(u\) and one functional of \(v\):
\[
\kappa A+\kappa^{-1}B
=
\left(\kappa\sigma e_i+\kappa^{-1}r\tau e_j\right)(u)
+
\left(\kappa r\sigma e_i-\kappa^{-1}\tau e_j\right)(v).
\]
By the dual-norm fact above, there are only two possibilities. In the first,
\[
a_\kappa=\kappa+\frac r\kappa,
\qquad
b_\kappa=\max\left\{r\kappa,\frac1\kappa\right\}.
\]
In the second,
\[
a_\kappa=\max\left\{\kappa,\frac r\kappa\right\},
\qquad
b_\kappa=r\kappa+\frac1\kappa.
\]
The second case becomes the first after replacing \(\kappa\) by \(\kappa^{-1}\), so both have the same optimal bound.

Using Cauchy--Schwarz,
\[
\kappa A+\kappa^{-1}B
\le
pa_\kappa+qb_\kappa
\le
\sqrt{p^2+q^2}\sqrt{a_\kappa^2+b_\kappa^2}.
\]
Consequently
\[
\frac{2AB}{(1+r^2)(p^2+q^2)}
\le
\frac{a_\kappa^2+b_\kappa^2}{2(1+r^2)}.
\tag{1}
\]

Put
\[
z=\kappa^2.
\]
For the first orientation, if
\[
z\le\frac1r,
\]
then (1) becomes
\[
G_1(z)
=
\frac{z+2r+(1+r^2)/z}{2(1+r^2)}.
\]
Its unconstrained minimizer is
\[
z=\sqrt{1+r^2}.
\]
This lies in the present region exactly when
\[
r^4+r^2\le1,
\]
or equivalently \(r\le r_*\). At that minimizer,
\[
G_1=
\frac{r+\sqrt{1+r^2}}{1+r^2}.
\]

If
\[
z\ge\frac1r,
\]
then
\[
G_2(z)
=
\frac{(1+r^2)z+2r+r^2/z}{2(1+r^2)}.
\]
On this region \(G_2\) is increasing, so its minimum is at
\[
z=\frac1r.
\]
When \(r\ge r_*\), the first-region minimum is also forced to the same boundary. Hence
\[
G_2\!\left(\frac1r\right)
=
\frac{1+3r^2+r^4}{2r(1+r^2)}.
\]
This proves the global upper bounds.

It remains to attain them.

For
\[
0<r\le r_*,
\]
put
\[
t=r+\sqrt{1+r^2},
\qquad
x=(1,0),
\qquad
y=(0,-t).
\]
Then
\[
N(x)=1,\qquad N(y)=t,
\]
and
\[
N(x+ry)=1+rt,
\qquad
N(rx-y)=t.
\]
Since
\[
t^2=1+2rt,
\]
the defining quotient equals
\[
\frac{r+\sqrt{1+r^2}}{1+r^2}.
\]

For
\[
r_*\le r\le1,
\]
put
\[
t=\frac{1+r^2}{r},
\qquad
s=\frac{r^4+r^2-1}{2r^2}.
\]
The threshold guarantees
\[
0\le s\le\frac12.
\]
Take
\[
x=(-1,-s),
\qquad
y=(0,t).
\]
Then
\[
N(x)=1,\qquad N(y)=t,
\]
while direct evaluation gives
\[
N(x+ry)=1+rt-s,
\qquad
N(rx-y)=t+rs.
\]
Substitution yields
\[
\frac{2N(x+ry)N(rx-y)}
{(1+r^2)(N(x)^2+N(y)^2)}
=
\frac{1+3r^2+r^4}{2r(1+r^2)}.
\]
Thus both upper bounds are sharp, completing the profile.

## Verification
The bundled `verify.py` checks the dual-norm two-value lemma directly on all six unit-ball vertices and all ordered distinct coordinate pairs. It then verifies symbolically the two minimization branches, the threshold equation
\[
r^4+r^2=1,
\]
the matching of the two formulas at \(r_*\), and both explicit extremizer families.

It also performs an independent deterministic search over many unit-sphere directions, relative magnitudes and parameter values. Those samples agree with the closed form, but the finite search is not used as proof.

## Relationship to prior work
Liu, Sarfraz and Li introduced \(C_Z(\lambda,\mu,X)\), proved the general bounds
\[
1\le C_Z(\lambda,\mu,X)\le2,
\]
and related it to the von Neumann--Jordan and classical Zbăganu constants. Their Example 4.5 treats a regular-octagonal norm and gives an upper estimate rather than an exact parameter profile. The inspected full text contains no occurrence of “hexagon” or “regular” and no affine-regular-hexagonal computation.

The closest public semantic-index result on the same hexagonal plane computes a different parameterized isosceles von Neumann--Jordan constant. Its objective is a sum of squared norms under an isosceles constraint, not the product defining \(C_Z(\lambda,\mu,X)\), so it does not imply the present two-branch profile.

The phase transition here is intrinsic to the generalized Zbăganu optimization: for small \(r\), the optimal dual certificate has an interior weight
\[
\kappa^2=\sqrt{1+r^2},
\]
whereas after
\[
r^4+r^2=1
\]
the optimum sticks to the facet-switch boundary
\[
\kappa^2=\frac1r.
\]

## Limitations
The result is specific to the affine-regular hexagonal plane. It does not provide the generalized Zbăganu profile for every regular polygon or for arbitrary absolute normalized norms.

The proof gives exact extremizing families but does not classify every extremizer. Bibliographic and semantic searches cannot prove absolute uniqueness; an equivalent formula under another affine normalization remains a residual literature risk.

## References
1. Q. Liu, M. Sarfraz and Y. Li, “Some aspects of generalized Zbăganu and James constant in Banach spaces,” Demonstratio Mathematica 54 (2021), 299–310, doi:10.1515/dema-2021-0033. Published 16 August 2021. MSC 2020: 46B20.
