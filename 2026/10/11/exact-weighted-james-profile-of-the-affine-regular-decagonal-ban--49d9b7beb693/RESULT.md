# Exact weighted James profile of the affine-regular decagonal Banach plane
## Finding
Put
\[
r=\frac{\sqrt5-1}{2}
\]
and define
\[
X_{10}=(\mathbb R^2,N_{10}),
\qquad
N_{10}(u,v)
=
\max\left\{
|u+v|,
|ru+v|,
r|v|,
r|u|,
|u+rv|
\right\}.
\]
The unit ball is an affine-regular centrally symmetric decagon.

For \(0<\lambda<1\), define the Liu--Sarfraz--Li generalized James constant by
\[
J(\lambda,X)
=
\sup_{x,y\in S_X}
\min\left\{
\|\lambda x+(1-\lambda)y\|,
\|\lambda x-(1-\lambda)y\|
\right\}.
\]
Let
\[
s=\max\{\lambda,1-\lambda\}.
\]
Then
\[
\boxed{
J(\lambda,X_{10})
=
\begin{cases}
r+\dfrac{3-\sqrt5}{4}s,
&
\dfrac12\le s\le r,
\\[7pt]
\dfrac{\sqrt5-1}{4}
+
\dfrac{5-\sqrt5}{4}s,
&
r\le s<1.
\end{cases}
}
\tag{1}
\]

Thus the weighted profile has a genuine extremizer transition at
\[
s=r=\frac{\sqrt5-1}{2}.
\]
At the midpoint,
\[
J\left(\frac12,X_{10}\right)
=
\frac{3\sqrt5-1}{8},
\]
so the ordinary James constant is
\[
J(X_{10})
=
\frac{3\sqrt5-1}{4}.
\tag{2}
\]

## Assumptions and scope
All scalars are real. The generalized James constant is used with the normalization in the defining 2021 paper.

It is convenient to introduce
\[
F(t)
=
\sup_{x,y\in S_{X_{10}}}
\min\{N_{10}(x+ty),N_{10}(x-ty)\},
\qquad
0\le t\le1.
\tag{3}
\]
The exact chord profile is
\[
\boxed{
F(t)
=
\begin{cases}
1+\dfrac{\sqrt5-1}{4}t,
&
0\le t\le r,
\\[7pt]
\dfrac{1+\sqrt5}{4}+rt,
&
r\le t\le1.
\end{cases}
}
\tag{4}
\]

Formula (1) follows from (4). Indeed, symmetry under
\[
\lambda\longleftrightarrow1-\lambda
\]
allows \(s=\max\{\lambda,1-\lambda\}\), and with
\[
t=\frac{1-s}{s}
\]
homogeneity gives
\[
J(\lambda,X_{10})=sF(t).
\tag{5}
\]
The threshold \(t=r\) is equivalent to \(s=r\), because
\[
\frac1{1+r}=r.
\]

## Proof
Write
\[
\varphi=\frac{1+\sqrt5}{2}=\frac1r.
\]
The vertices of the unit ball, in cyclic order, are
\[
(-1,0),\ (0,-1),\ (1,-\varphi),\ (\varphi,-\varphi),\ (\varphi,-1)
\]
and their negatives. The linear map
\[
Q(u,v)=(-v,u+\varphi v)
\]
cycles these ten vertices, while
\[
R(u,v)=(v,u)
\]
is a reflection. Hence the linear isometry group is transitive on edges and contains a reflection interchanging the endpoints of a fixed edge.

The norm is the maximum of the ten linear functionals obtained by attaching both signs to
\[
(u,v)\longmapsto u+v,\quad
(u,v)\longmapsto ru+v,\quad
(u,v)\longmapsto rv,\quad
(u,v)\longmapsto ru,\quad
(u,v)\longmapsto u+rv.
\tag{6}
\]

We prove the upper bound in (4) by an exact finite polyhedral reduction. By the dihedral symmetry, put
\[
x=(-1+\alpha,-\alpha),
\qquad
0\le\alpha\le\frac12.
\tag{7}
\]
Changing \(y\) to \(-y\) only swaps the two chords, so it is enough to let \(y\) run through five consecutive edge classes \(E_0,\ldots,E_4\).

On an edge \(E_j=[p_j,p_{j+1}]\), write
\[
y=p_j+\beta(p_{j+1}-p_j),
\qquad
0\le\beta\le1.
\]
For \(t\ge0\), introduce
\[
w=t\beta.
\]
Then
\[
ty=tp_j+w(p_{j+1}-p_j),
\qquad
0\le w\le t,
\tag{8}
\]
so every support value of \(x\pm ty\) is affine in the three variables
\[
(\alpha,t,w).
\]

Let \(L(t)\) denote the appropriate right-hand side of (4). For a support pair \(f,g\) from the ten functionals in (6), consider
\[
E_{f,g}(\alpha,t,w)
=
\min\{
f(x+ty)-L(t),
g(x-ty)-L(t)
\}.
\tag{9}
\]
On each of the two parameter intervals
\[
0\le t\le r,
\qquad
r\le t\le1,
\]
the function \(L(t)\) is affine. Hence (9) is the minimum of two affine functions on the triangular-prism domain
\[
0\le\alpha\le\frac12,
\qquad
t_0\le t\le t_1,
\qquad
0\le w\le t.
\tag{10}
\]

The maximum of a minimum of two affine functions on a polytope occurs either at a vertex of the polytope or on the equality plane of the two affine functions together with two active facets of the polytope. Therefore every support-pair comparison in (9) reduces to finitely many points in \(\mathbb Q(\sqrt5)^3\).

The bundled exact certificate exhausts all
\[
5\cdot2\cdot10\cdot10=1000
\]
edge-interval-support cases. It uses exact arithmetic in \(\mathbb Q(\sqrt5)\), not floating-point optimization. The largest possible simultaneous support excess for each edge class is

\[
\begin{array}{c|cc}
\text{edge class}
&
0\le t\le r
&
r\le t\le1
\\ \hline
E_0&0&\dfrac{-9+3\sqrt5}{4}\\[4pt]
E_1&0&\dfrac{-3+\sqrt5}{4}\\[4pt]
E_2&0&0\\[4pt]
E_3&0&0\\[4pt]
E_4&0&\dfrac{-3+\sqrt5}{2}
\end{array}
\tag{11}
\]
and every entry is nonpositive.

If both chord norms exceeded \(L(t)\), some support of \(x+ty\) and some support of \(x-ty\) would both exceed \(L(t)\), contradicting (11). Thus
\[
\min\{N_{10}(x+ty),N_{10}(x-ty)\}\le L(t)
\]
for every admissible \(x,y,t\).

It remains to prove sharpness. Put
\[
x_1=(-1,0),
\qquad
y_1=
\left(
\frac{3+\sqrt5}{4},
-\frac{1+\sqrt5}{2}
\right).
\]
Then
\[
N_{10}(x_1)=N_{10}(y_1)=1
\]
and, for every \(0\le t\le r\),
\[
N_{10}(x_1+ty_1)
=
N_{10}(x_1-ty_1)
=
1+\frac{\sqrt5-1}{4}t.
\tag{12}
\]

For the second branch put
\[
x_2=\left(-\frac12,-\frac12\right),
\qquad
y_2=
\left(
\frac{1+\sqrt5}{2},
-\frac{1+\sqrt5}{2}
\right).
\]
Again
\[
N_{10}(x_2)=N_{10}(y_2)=1,
\]
and for every \(r\le t\le1\),
\[
N_{10}(x_2+ty_2)
=
N_{10}(x_2-ty_2)
=
\frac{1+\sqrt5}{4}+rt.
\tag{13}
\]

Equations (11)--(13) prove (4), and (5) gives (1).

## Verification
The bundled `verify.py` is an exact continuum certificate for the polyhedral upper bound. It represents every number as
\[
a+b\sqrt5,
\qquad
a,b\in\mathbb Q,
\]
with exact rational arithmetic and exact sign comparisons.

For each edge class, each branch of \(L(t)\), and each of the one hundred ordered support pairs, it enumerates every possible maximizer described after (10). It verifies that all support-pair excesses are nonpositive and reproduces the five-by-two table (11).

The same file verifies algebraically that the two displayed sharp pairs are unit vectors and attain the branch formulas throughout their stated parameter intervals. No finite grid, random sample, timeout, or numerical optimization is used in the correctness certificate.

## Relationship to prior work
Liu, Sarfraz and Li introduced \(J(\lambda,X)\) in 2021 and established general bounds and structural properties. Their defining section includes the normalization used here and relates the midpoint to the ordinary James constant. The inspected full text does not compute the affine-regular decagonal profile.

A same-invariant exact computation for real \(\ell_p\) spaces was compared because it gives broad coverage of a major classical family, but it does not imply the polyhedral decagonal formula or its golden-ratio transition.

The ordinary James constant of the affine-regular decagon is a previously encountered endpoint value. The new content here is the complete weighted profile (1), equivalently the full radius profile (4), together with the sharp change of extremizing configuration at \(r=(\sqrt5-1)/2\).

A previous exact weighted-James computation for the regular octagonal plane has one affine branch after the symmetry reduction. It does not imply the two-branch decagonal law.

## Limitations
The proof is specific to this affine-regular decagonal norm and uses its finite dihedral support structure.

No classification of every maximizing pair is claimed. The result identifies explicit maximizers for both branches and proves the exact supremum.

The ordinary midpoint value in (2) is not claimed as a new standalone invariant; the accepted claim is the complete weighted profile and its extremizer transition.

Bibliographic and semantic searches cannot establish absolute novelty. An equivalent profile could conceivably have appeared under another affine normalization or under a radius parameter rather than \(\lambda\).

## References
1. Q. Liu, M. Sarfraz and Y. Li, “Some aspects of generalized Zbăganu and James constant in Banach spaces,” *Demonstratio Mathematica* 54 (2021), 299--310, doi:10.1515/dema-2021-0033. Published online 16 August 2021.
