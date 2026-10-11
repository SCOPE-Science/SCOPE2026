# Exact angle-modulus-of-smoothness profile of the affine-regular hexagonal plane
## Finding
Let \(X_H=(\mathbb R^2,N)\), where
\[
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
For \(0\le\epsilon\le2\), define
\[
m_H(\epsilon)=
\inf\{N(x+y):x,y\in S_{X_H},\ N(x-y)=\epsilon\}.
\]
Then
\[
m_H(\epsilon)=
\begin{cases}
2-\epsilon/2,&0\le\epsilon\le4/3,\\
4-2\epsilon,&4/3\le\epsilon\le2.
\end{cases}
\]
Consequently the Du–Ahmad–Din–Li angle modulus of smoothness is
\[
\rho_{X_H}^{a}(\epsilon)
=
1-\frac12m_H(\epsilon)^2
=
\begin{cases}
-1+\epsilon-\epsilon^2/8,&0\le\epsilon\le4/3,\\
1-2(2-\epsilon)^2,&4/3\le\epsilon\le2.
\end{cases}
\]
In particular,
\[
\rho_{X_H}^{a}(1)=-\frac18,
\qquad
\rho_{X_H}^{a}(4/3)=\frac19.
\]
The formula has a genuine geometric phase transition: for separations below \(4/3\), a minimizing chord joins adjacent unit-ball edges, while above \(4/3\) a minimizing chord joins edges separated by one edge.

## Assumptions and scope
All scalars are real. The unit sphere is the boundary of the affine-regular hexagon with vertices
\[
(1,1),\ (1,0),\ (0,-1),\ (-1,-1),\ (-1,0),\ (0,1).
\]
The angle modulus of smoothness is defined, for \(0\le\epsilon\le2\), by
\[
\rho_X^{a}(\epsilon)
=
\sup\left\{
1-\frac12\|x+y\|^2:
x,y\in S_X,\ \|x-y\|=\epsilon
\right\}.
\]
Thus computing \(\rho_{X_H}^{a}\) is equivalent to computing the minimum possible value of \(N(x+y)\) at fixed separation.

## Proof
The linear maps
\[
R(s,t)=(s-t,s),
\qquad
Q(s,t)=(t,s)
\]
are isometries of \(N\). They generate the symmetries needed to reduce any unordered pair of unit-sphere edges to one of four relative positions.

Write
\[
E_0=\{(1,u):0\le u\le1\},
\]
and, in cyclic order,
\[
E_1=\{(v,v-1):0\le v\le1\},
\qquad
E_2=\{(-q,-1):0\le q\le1\},
\qquad
E_3=-E_0.
\]

For two points on the same edge, let
\[
x=(1,u),\qquad y=(1,v).
\]
Then
\[
N(x-y)=|u-v|\le1
\]
and
\[
N(x+y)=2.
\]

For adjacent edges, let
\[
x=(1,u)\in E_0,
\qquad
y=(v,v-1)\in E_1.
\]
A direct evaluation of the three defining functionals gives
\[
N(x-y)=1+u-v.
\]
Hence, if this distance is \(\epsilon\), then
\[
v=1+u-\epsilon.
\]
For the sum,
\[
N(x+y)
=
\max\{1+v,\,2-u\}
=
\max\{2+u-\epsilon,\,2-u\}.
\]
The feasible interval for \(u\) contains \(u=\epsilon/2\) for every \(0\le\epsilon\le2\), and the two affine terms are equal there. Therefore the exact minimum within the adjacent-edge class is
\[
2-\frac{\epsilon}{2}.
\]
It is attained by
\[
x=(1,\epsilon/2),
\qquad
y=(1-\epsilon/2,-\epsilon/2).
\]

For edges separated by one edge, let
\[
x=(1,u)\in E_0,
\qquad
y=(-q,-1)\in E_2.
\]
Then
\[
N(x-y)=1+\max\{u,q\}.
\]
Thus this configuration exists only for \(1\le\epsilon\le2\), and the constraint is
\[
\max\{u,q\}=\epsilon-1.
\]
Moreover,
\[
N(x+y)=2-u-q.
\]
The latter is minimized by taking
\[
u=q=\epsilon-1,
\]
which gives the exact value
\[
4-2\epsilon.
\]
An attaining pair is therefore
\[
x=(1,\epsilon-1),
\qquad
y=(1-\epsilon,-1).
\]

For opposite edges, the distance is always \(2\). At that endpoint the minimum of \(N(x+y)\) is \(0\), agreeing with the preceding formula.

These cases exhaust all edge pairs by the hexagonal symmetries. Hence, for \(0\le\epsilon\le1\), the adjacent-edge value beats the same-edge value. For \(1\le\epsilon\le2\), one compares
\[
2-\frac{\epsilon}{2}
\quad\text{and}\quad
4-2\epsilon.
\]
They are equal exactly when
\[
\epsilon=\frac43.
\]
This proves the stated formula for \(m_H\), and substitution into the defining expression for \(\rho_{X_H}^{a}\) proves the result.

## Verification
The bundled checker verifies with exact rational arithmetic that \(R\) and \(Q\) preserve the norm on the defining facet functionals, replays the four edge-pair formulas, verifies the feasibility of the explicit attaining pairs over their stated ranges, and checks the branch crossing at \(\epsilon=4/3\).

The infinite statement is not inferred from finite sampling. Exhaustion of all unit-sphere pairs comes from the analytic edge classification under the two explicit isometries.

## Relationship to prior work
Du, Ahmad, Din and Li introduced the angle modulus of smoothness and proved its relation to a classical smoothness modulus. They computed the new invariant for some concrete spaces, including \(\ell_p\)-type examples, and used \(\rho_X^{a}(1)\) to characterize uniform non-squareness. The inspected source does not give the affine-regular hexagonal profile above.

The closest indexed result located for the same invariant is an exact value at unit separation for the regular octagonal plane. That result concerns a different unit ball and a single parameter value. Other close records compute different geometric constants on the same affine-regular hexagonal plane. None of those statements implies the two-branch angle-modulus profile proved here.

## Limitations
The result is specific to one two-dimensional polyhedral norm. It does not classify the angle modulus of smoothness for arbitrary hexagonal planes or general polygonal norms. The literature search cannot prove absolute novelty, and an equivalent calculation under an older smoothness-modulus notation could exist outside the inspected sources. The proof establishes the full continuum profile directly, including the branch transition and attaining families.

## References
1. D. Du, A. Ahmad, A. Din and Y. Li, “Some Moduli of Angles in Banach Spaces,” *Mathematics* 10 (2022), 2965, DOI 10.3390/math10162965. Published 17 August 2022. MSC 46B20.
