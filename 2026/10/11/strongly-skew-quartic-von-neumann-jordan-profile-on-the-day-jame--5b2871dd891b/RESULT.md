# Strongly skew quartic von Neumann--Jordan profile on the Day--James hexagon
## Finding
Let \(H=(\mathbb R^2,N)\) be the Day--James hexagonal plane
\[
N(u,v)=
\begin{cases}
\max\{|u|,|v|\},&uv\ge0,\\
|u|+|v|,&uv\le0.
\end{cases}
\]
For the skew generalized von Neumann--Jordan constant of Ni, Liu and Zhou at exponent \(p=4\), homogeneity in the two positive weights allows us to write
\[
\zeta=1,\qquad \eta=r,\qquad 0<r\le1.
\]

Let \(\rho\in(0,1)\) be the unique positive root of
\[
\rho^3+2\rho^2-2=0.
\]
Numerically,
\[
\rho\approx0.839286755214161.
\]

For every
\[
0<r\le\rho,
\]
there is a unique \(t_r\in(r,1]\) satisfying
\[
\boxed{
(t_r^3-r)(1+r t_r)^3=t_r^3
}.
\tag{1}
\]
For \(r<\rho\), one has \(t_r<1\), while \(t_\rho=1\). The exact constant is
\[
\boxed{
C^4_{NJ}(1,r,H)
=
\frac{(1+r t_r)^4+t_r^4}
{4(1+r^4)(1+t_r^4)}
}.
\tag{2}
\]

A maximizing pair is given by adjacent vertices of the hexagonal unit ball. Thus the strongly skew regime is governed by a different vertex mechanism from the branch treated in the defining paper.

The threshold is exact:
\[
(1-r)(1+r)^3<1
\quad\Longleftrightarrow\quad
r>\rho.
\tag{3}
\]
Hence (2) fills precisely the complementary quartic parameter range left outside the hypothesis of the published Day--James example.

## Assumptions and scope
All scalars are real. The exponent is fixed at \(p=4\).

For \(\zeta,\eta>0\), the skew generalized von Neumann--Jordan constant is
\[
C^4_{NJ}(\zeta,\eta,X)
=
\sup_{(x,y)\ne(0,0)}
\frac{\|\zeta x+\eta y\|^4+\|\eta x-\zeta y\|^4}
{4(\zeta^4+\eta^4)(\|x\|^4+\|y\|^4)}.
\]
The homogeneous unit-sphere reduction is
\[
C^4_{NJ}(\zeta,\eta,X)
=
\sup_{\substack{x,y\in S_X\\0\le t\le1}}
\frac{\|\zeta x+\eta t y\|^4+\|\eta x-\zeta t y\|^4}
{4(\zeta^4+\eta^4)(1+t^4)}.
\tag{4}
\]

Scaling both weights by the same positive number does not change the quotient. Interchanging the two weights also leaves the constant unchanged after exchanging the two transformed chords. Therefore it is enough to take \(\zeta=1\) and \(0<r=\eta/\zeta\le1\).

The six vertices of \(B_H\) are
\[
(1,0),\ (1,1),\ (0,1),\ (-1,0),\ (-1,-1),\ (0,-1).
\]

## Proof
Fix \(0<r\le1\) and \(0\le t\le1\). Because the fourth power of a norm is convex, maximizing the numerator in (4) over each variable separately reduces to the six extreme points of the hexagonal ball.

A direct evaluation of the finite vertex orbits gives the exact numerator envelope
\[
M_r(t)
=
\max\left\{
1+(r+t)^4,\,
(1+rt)^4+\max\{r,t\}^4
\right\}.
\tag{5}
\]
Both entries in (5) are attained by explicit vertex pairs. Thus no relaxation occurs in the reduction.

Write
\[
A_r(t)=\frac{1+(r+t)^4}{1+t^4}.
\]
Differentiation gives
\[
\operatorname{sgn} A_r'(t)
=
\operatorname{sgn}\left(
1-r t^3-\left(\frac{t}{r+t}\right)^3
\right).
\tag{6}
\]
The expression in parentheses is strictly decreasing in \(t\). At \(t=1\), its sign is the sign of
\[
1-r-\frac1{(1+r)^3}.
\]
After multiplication by \((1+r)^3\), this is the negative of
\[
r(r^3+2r^2-2).
\]
Consequently, if \(0<r\le\rho\), then
\[
A_r(t)\le A_r(1).
\tag{7}
\]

Now consider the second entry of (5). On \(0\le t\le r\), put
\[
B_{0,r}(t)
=
\frac{(1+rt)^4+r^4}{1+t^4}.
\]
Its derivative has the sign of
\[
E_r(t)
=
(1+rt)^3(r-t^3)-r^4t^3.
\tag{8}
\]
For \(t\le r\le\rho<0.84\),
\[
r-t^3\ge r(1-t^2),
\qquad
1+rt\ge1+t^2.
\]
Therefore
\[
E_r(t)
\ge
r\left((1+t^2)^3(1-t^2)-r^3t^3\right).
\]
For \(0\le t\le0.84\),
\[
(1+t^2)^3(1-t^2)
=
1+2t^2-2t^6-t^8
\ge1,
\]
because \(2\ge2t^4+t^6\) on this interval. Since \(r^3t^3<1\), (8) is positive. Hence
\[
B_{0,r}(t)\le B_{0,r}(r).
\tag{9}
\]

On \(r\le t\le1\), the second branch is
\[
B_r(t)
=
\frac{(1+rt)^4+t^4}{1+t^4}.
\]
Its derivative has the sign of
\[
D_r(t)
=
t^3+(r-t^3)(1+rt)^3.
\tag{10}
\]
The equation \(D_r(t)=0\) is equivalent to
\[
t^3\left(1-(1+rt)^{-3}\right)=r,
\tag{11}
\]
or equivalently to (1). The left side of (11) is strictly increasing for \(t>0\), so there is at most one critical point.

At \(t=r\), (10) is positive. At \(t=1\),
\[
\operatorname{sgn}D_r(1)
=
\operatorname{sgn}(r^3+2r^2-2).
\]
Thus, for \(0<r<\rho\), there is a unique
\[
t_r\in(r,1)
\]
at which \(B_r\) changes from increasing to decreasing. For \(r=\rho\), the unique maximum is reached at \(t_\rho=1\).

Equations (9) and the monotonic increase of \(B_r\) from \(t=r\) show that the entire second branch is maximized at \(t_r\). By (7),
\[
\max_t A_r(t)=A_r(1).
\]
But
\[
A_r(1)=B_r(1),
\]
and for \(r<\rho\),
\[
B_r(t_r)>B_r(1).
\]
Hence the second branch strictly dominates the first. At \(r=\rho\), both meet at \(t=1\). Substitution into (4) proves (2).

Finally,
\[
(1-r)(1+r)^3-1
=
-r(r^3+2r^2-2),
\]
which proves (3).

## Verification
The proof is analytic and covers every admissible unit pair and every \(0<r\le\rho\).

The bundled `verify.py` performs three independent reproducibility checks. It enumerates all \(36\) ordered vertex pairs on dense rational parameter grids and confirms the exact envelope (5) numerically; it solves (11) by bisection and compares (2) with exhaustive one-dimensional searches; and it checks that the phase transition is governed by the root of \(r^3+2r^2-2\).

The finite computations are not used as a proof of the continuum theorem. The continuum argument consists of the extreme-point reduction, the exact finite vertex envelope, and the derivative signs (6), (8), and (10).

## Relationship to prior work
Ni, Liu and Zhou introduced the skew generalized von Neumann--Jordan constant and gave a Day--James hexagonal example under a parameter condition. At \(p=4\), after setting \(r=\eta/\zeta\le1\), that condition becomes
\[
(1-r)(1+r)^3<1,
\]
which is exactly the regime \(r>\rho\). Their proof then optimizes the branch represented here by \(A_r\).

The present result analyzes the complementary range
\[
0<r\le\rho.
\]
In this range the published branch is maximized at the endpoint \(t=1\), but a different adjacent-vertex branch becomes larger and has a unique interior optimizer when \(r<\rho\). Thus the result is not a restatement or specialization of the published formula; it identifies a genuine change of extremal mechanism at the exact boundary of that formula's hypothesis.

Yang and Wang's earlier 2017 paper computes the balanced generalized von Neumann--Jordan constant \(C^{(p)}_{NJ}(H)\). The balanced case corresponds to \(r=1\), outside the strongly skew range considered here, and does not imply the two-weight phase transition.

Targeted database searches used the exact skew invariant, the Day--James and hexagonal aliases, the polynomial threshold \(r^3+2r^2-2\), the critical equation (1), and the phrase “complementary regime.” No indexed record located states (1)--(3).

## Limitations
The result treats the quartic exponent \(p=4\) and the strongly skew range \(0<r\le\rho\). It does not claim a new formula for \(r>\rho\), where the defining paper already supplies the relevant Day--James branch under its stated condition.

The result does not classify every maximizing ordered vertex pair; it identifies the exact maximal value and supplies an adjacent-vertex maximizer.

The finite checker samples parameter grids and therefore does not certify continuum inequalities by itself. Those inequalities are proved analytically above.

Bibliographic and semantic searches cannot prove absolute novelty. An equivalent complementary branch could exist under another normalization of the Day--James hexagon or another ordering of the two weights.

## References
1. Q. Ni, Q. Liu and Y. Zhou, “Skew generalized von Neumann-Jordan constant in Banach spaces,” *Hacettepe Journal of Mathematics and Statistics* 54 (2025), 436--444, doi:10.15672/hujms.1451136. Early publication 27 August 2024. MSC 46B20.
2. C. Yang and T. Wang, “Generalized von Neumann-Jordan constant \(C^{(p)}_{NJ}(X)\) for the regular octagon space,” *Mathematical Inequalities & Applications* 20 (2017), 483--490, doi:10.7153/mia-20-32.
