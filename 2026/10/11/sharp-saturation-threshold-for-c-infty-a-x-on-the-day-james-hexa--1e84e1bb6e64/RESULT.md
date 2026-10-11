# Sharp saturation threshold for \(C_{-\infty}(a,X)\) on the Day–James hexagon
## Finding
Let \(X_D=(\mathbb R^2,N)\) with
\[
N(s,t)=\max\{{|s|,|t|,|s-t|\}}.
\]
This is the real Day–James \(\ell_\infty-\ell_1\) plane. For the generalized von Neumann–Jordan type constant introduced by Liu, Din and Li,
\[
C_{{-\infty}}(a,X_D)=1\quad\Longleftrightarrow\quad a\ge1,
\]
for every \(a>0\). Hence the sharp saturation threshold of the universal upper bound is exactly \(1\).

## Assumptions and scope
The scalar field is real and \(a>0\). We use the defining three-vector formulation
\[
C_{{-\infty}}(a,X)=\sup \min\left\{{\frac{{\|x+y\|^2}}{{D}},\frac{{\|x-z\|^2}}{{D}}}}\right\},\qquad D=2\|x\|^2+\|y\|^2+\|z\|^2,
\]
with the separation condition \(\|y-z\|\le a\|x\|\); using a strict inequality instead gives the same threshold because the endpoint is obtained as a supremum. The cited 2021 paper proves the universal upper bound \(C_{{-\infty}}(a,X)\le1\).

## Proof
For \(a>1\), the published example uses \(x=(1,1)\), \(y=(0,1)\), and \(z=(-1,0)\). All three vectors have norm \(1\), the separation is \(N(y-z)=1\), and both shifted norms are \(2\); hence the quotient equals \(1\). At \(a=1\), set \(\varepsilon>0\), \(x=(1,1)\), \(y=(0,1-\varepsilon)\), and \(z=(-(1-\varepsilon),0)\). Then \(N(y-z)=1-\varepsilon<1\), while both quotients equal
\[
\frac{{(2-\varepsilon)^2}}{{2+2(1-\varepsilon)^2}},
\]
which tends to \(1\) as \(\varepsilon\downarrow0\). Thus the supremum is \(1\) also at the endpoint.

It remains to exclude \(0<a<1\). Suppose instead that \(C_{{-\infty}}(a,X_D)=1\). By the unit-ball reduction in the defining paper, choose admissible triples \((x_n,y_n,z_n)\) in the closed unit ball, with at least one member of each triple on the unit sphere, whose minimum quotient tends to \(1\). Passing to a subsequence gives a limit \((x,y,z)\). Write \(r=N(x)\), \(s=N(y)\), \(t=N(z)\), \(A=N(x+y)\), \(B=N(x-z)\), and \(D=2r^2+s^2+t^2\). For every triple,
\[
A^2+B^2\le(r+s)^2+(r+t)^2\le2D.
\]
Since each of the two normalized squared shifted norms is asymptotically at least \(1\), both inequalities become equalities in the limit. The second equality is equivalent to \((r-s)^2+(r-t)^2=0\), so \(r=s=t\); the unit-sphere normalization then gives \(r=s=t=1\). Consequently \(A=B=2\).

Equality \(N(x+y)=2\) means that \(x\) and \(y\) lie on a common exposed edge of the hexagonal unit ball, and equality \(N(x-z)=2\) means that \(x\) and \(-z\) lie on a common exposed edge. If \(x\) lies in the relative interior of an edge, both companions lie on that same edge and \(N(y-z)=N(y+(-z))\ge2\). If \(x\) is a vertex, symmetry reduces to \(x=(1,1)\). Its incident edges are \(u=1\) and \(v=1\). The same-edge case again gives separation at least \(2\); in the cross-edge case write \(y=(1,q)\) and \(-z=(p,1)\) with \(0\le p,q\le1\). Then
\[
N(y-z)=N(1+p,1+q)=1+\max\{{p,q\}}\ge1.
\]
Thus every limiting saturation configuration has \(N(y-z)\ge1\). But admissibility gives \(N(y_n-z_n)\le aN(x_n)\), hence \(N(y-z)\le a<1\), a contradiction. Therefore \(C_{{-\infty}}(a,X_D)<1\) whenever \(0<a<1\).

## Verification
The proof is analytic. The bundled `verify.py` independently checks the endpoint approximants in exact rational arithmetic and exhausts the incident-face pairs of the hexagonal unit ball by exact linear programming; it confirms that the minimum possible limiting separation under the two equality-face conditions is \(1\).

## Relationship to prior work
Liu, Din and Li introduced \(C_{{-\infty}}(a,X)\), proved the universal upper bound \(1\), and gave the Day–James triple showing saturation for \(a>1\). Dinarvand and Sanatpour later introduced a \(p\)-generalization and observed that the same triple yields saturation for \(a\ge1\) in their closed-constraint normalization. Neither inspected source supplies the converse \(0<a<1\Rightarrow C_{{-\infty}}(a,X_D)<1\). Published computations of other constants on the same hexagonal plane concern different two-vector invariants and do not imply this three-vector separation threshold.

## Limitations
This result determines only the sharp parameter at which the upper bound is saturated. It does not give an exact formula for \(C_{{-\infty}}(a,X_D)\) on \(0<a<1\), nor does it assert the same threshold for other Day–James planes or other Banach spaces.

## References
1. Q. Liu, A. Din, Y. Li, “Some aspects of generalized von Neumann-Jordan type constant,” AIMS Mathematics 6 (2021), 6309–6321, DOI 10.3934/math.2021370. Published 12 April 2021; primary MSC 46B20.
2. M. Dinarvand, A. H. Sanatpour, “Normal structure and generalized von Neumann-Jordan type constant,” Filomat 39 (2025), 11701–11716, DOI 10.2298/FIL2533701D.
