# Radon sharp bound and exact skew-orthogonality profile of the affine-regular hexagon
## Finding
For \(\alpha,\beta>0\), Zhou, Ni and Liu define
\[
B_{\alpha-\beta}(X)
=
\sup\left\{
\frac{\|\alpha x+\beta y\|-\|\beta x-\alpha y\|}{\alpha}:
x,y\in S_X,\ x\perp_B y
\right\}.
\]

If Birkhoff orthogonality is symmetric on \(X\), meaning
\[
x\perp_B y\Longrightarrow y\perp_B x,
\]
then
\[
B_{\alpha-\beta}(X)
\le
\min\left\{1,\frac{\beta}{\alpha}\right\}.
\]
In particular this applies to every Radon plane.

The bound is sharp for every positive parameter pair. Let
\[
H=(\mathbb R^2,N),
\qquad
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
Its unit ball is an affine-regular hexagon. Then
\[
B_{\alpha-\beta}(H)
=
\min\left\{1,\frac{\beta}{\alpha}\right\}.
\]
Thus the profile has exactly two branches:
\[
B_{\alpha-\beta}(H)
=
\begin{cases}
1,&0<\alpha\le\beta,\\[4pt]
\dfrac{\beta}{\alpha},&0<\beta\le\alpha.
\end{cases}
\]

## Assumptions and scope
All spaces are real and have dimension at least two. Birkhoff orthogonality is
\[
x\perp_B y
\quad\Longleftrightarrow\quad
\|x+\lambda y\|\ge\|x\|
\quad\text{for every }\lambda\in\mathbb R.
\]

The structural upper bound uses only symmetry of Birkhoff orthogonality. In dimension two, a normed plane with symmetric Birkhoff orthogonality is commonly called a Radon plane.

For the exact example,
\[
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
The six unit-ball vertices are
\[
(1,0),\ (1,1),\ (0,1),\ (-1,0),\ (-1,-1),\ (0,-1).
\]
The signed supporting functionals are
\[
s,\quad t,\quad s-t,\quad -s,\quad -t,\quad t-s.
\]

## Proof
Let \(X\) have symmetric Birkhoff orthogonality, and let
\[
x,y\in S_X,
\qquad
x\perp_B y.
\]
Then also
\[
y\perp_B x.
\]
The triangle inequality gives
\[
\|\alpha x+\beta y\|
\le
\alpha+\beta.
\]
From
\[
x\perp_B y
\]
we obtain
\[
\|\beta x-\alpha y\|
=
\beta\left\|x-\frac{\alpha}{\beta}y\right\|
\ge
\beta.
\]
From the reverse orthogonality
\[
y\perp_B x
\]
we also obtain
\[
\|\beta x-\alpha y\|
=
\alpha\left\|y-\frac{\beta}{\alpha}x\right\|
\ge
\alpha.
\]
Hence
\[
\|\beta x-\alpha y\|
\ge
\max\{\alpha,\beta\}.
\]
Therefore
\[
\frac{\|\alpha x+\beta y\|-\|\beta x-\alpha y\|}{\alpha}
\le
\frac{\alpha+\beta-\max\{\alpha,\beta\}}{\alpha}
=
\min\left\{1,\frac{\beta}{\alpha}\right\}.
\]
Taking the supremum proves the structural bound.

It remains to prove that the affine-regular hexagonal plane \(H\) has symmetric Birkhoff orthogonality and attains the bound.

The linear maps
\[
R(s,t)=(t,t-s)
\]
and
\[
S(s,t)=(t,s)
\]
are isometries of \(H\). Their action is transitive on the six edges and on the six vertices of the unit ball.

First take a point in the relative interior of the edge
\[
x=(1,u),
\qquad
0<u<1.
\]
Its unique norming functional is
\[
f(s,t)=s.
\]
Thus
\[
x\perp_B y
\]
forces
\[
y=(0,1)
\quad\text{or}\quad
y=(0,-1).
\]
For \(y=(0,1)\), the functional
\[
g(s,t)=t-us
\]
is a convex combination of the two norming functionals \(t\) and \(t-s\) at \(y\), and
\[
g(x)=0.
\]
Hence
\[
y\perp_B x.
\]
For \(y=(0,-1)\), the functional
\[
h(s,t)=us-t
\]
is a convex combination of the norming functionals \(-t\) and \(s-t\) at \(y\), and again
\[
h(x)=0.
\]
Thus the reverse Birkhoff orthogonality holds at every nonvertex boundary point.

At a vertex, by symmetry it is enough to take
\[
x=(1,0).
\]
The norming functionals at \(x\) are the convex hull of
\[
s
\quad\text{and}\quad
s-t.
\]
Therefore \(x\perp_B y\) holds exactly when, up to changing the sign of \(y\),
\[
y=(v,1),
\qquad
0\le v\le1.
\]
Indeed,
\[
s-vt
=
(1-v)s+v(s-t)
\]
is norming at \(x\) and annihilates \(y\). Conversely the kernel of a convex combination of the two endpoint norming functionals has precisely such a unit direction.

For every \(y=(v,1)\) on that edge, the functional
\[
t
\]
is norming at \(y\) and satisfies
\[
t(x)=0.
\]
Thus
\[
y\perp_B x.
\]
The negative case is identical. Hence Birkhoff orthogonality is symmetric on \(H\).

Finally choose
\[
x=(1,0),
\qquad
y=(0,-1).
\]
The functional \(s\) norms \(x\) and annihilates \(y\), so
\[
x\perp_B y.
\]
Moreover
\[
N(\alpha x+\beta y)
=
N(\alpha,-\beta)
=
\alpha+\beta,
\]
while
\[
N(\beta x-\alpha y)
=
N(\beta,\alpha)
=
\max\{\alpha,\beta\}.
\]
Therefore
\[
\frac{N(\alpha x+\beta y)-N(\beta x-\alpha y)}{\alpha}
=
\min\left\{1,\frac{\beta}{\alpha}\right\}.
\]
This attains the structural upper bound and proves the exact profile.

## Verification
The bundled `verify.py` checks the affine-regular hexagon directly.

It verifies that the six signed facet functionals give exactly the stated six vertices and that the maps
\[
R(s,t)=(t,t-s)
\quad\text{and}\quad
S(s,t)=(t,s)
\]
permute the facet set.

It symbolically checks the norming-functional certificates used for every canonical Birkhoff pair:
\[
g=t-us
\]
for \(x=(1,u)\), \(y=(0,1)\),
\[
h=us-t
\]
for \(x=(1,u)\), \(y=(0,-1)\), and
\[
s-vt
\]
for the vertex family \(x=(1,0)\), \(y=(v,1)\).

It also checks the equality pair for representative rational parameter pairs on both sides of
\[
\alpha=\beta.
\]
The infinite-parameter theorem itself is established by the analytic inequalities in the proof; finite checks are only reproducibility aids.

## Relationship to prior work
Zhou, Ni and Liu introduced \(B_{\alpha-\beta}(X)\) in 2024 to quantify the difference between Birkhoff orthogonality and their skew orthogonality. They proved the universal bound
\[
0\le B_{\alpha-\beta}(X)\le1,
\]
showed that vanishing characterizes inner-product spaces, and compared the constant with \(J_\perp(X)\), \(D'(X)\), and the modulus of convexity.

Their explicit non-Hilbert example is a different piecewise \(\ell_\infty\)-\(\ell_1\) plane and establishes
\[
B_{\alpha-\beta}=1
\]
only in the parameter regime
\[
\alpha\le\beta.
\]
The inspected full text contains no occurrence of “Radon” or “hexagon”. The structural improvement
\[
B_{\alpha-\beta}(X)
\le
\min\left\{1,\frac{\beta}{\alpha}\right\}
\]
uses symmetry of Birkhoff orthogonality, a feature not exploited by the published universal estimate.

Targeted public-research searches under the exact constant notation, skew-orthogonality aliases, Radon-plane terminology, the affine-regular-hexagon normalization, and the candidate profile returned no covering statement. The closest indexed findings concern other Birkhoff-based constants or other invariants on the same hexagonal plane.

## Limitations
The general theorem assumes symmetric Birkhoff orthogonality. Outside that class, the sharper branch
\[
B_{\alpha-\beta}(X)\le\frac{\beta}{\alpha}
\]
need not hold.

The exact profile is proved only for the affine-regular hexagonal plane. It does not classify \(B_{\alpha-\beta}\) on all Radon planes or all polygonal Banach planes.

Bibliographic and semantic searches cannot prove absolute novelty. An equivalent formulation under alternate notation for the Zhou--Ni--Liu constant remains a residual literature risk.

## References
1. Y. Zhou, Q. Ni and Q. Liu, “The skew constant and orthogonalities in Banach spaces,” Open Journal of Mathematical Sciences 8 (2024), 1–7, doi:10.30538/oms2024.0219. Published 15 May 2024. Primary MSC 46B20.
