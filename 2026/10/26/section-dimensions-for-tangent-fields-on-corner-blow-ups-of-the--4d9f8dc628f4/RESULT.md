# Section dimensions for tangent fields on corner blow-ups of \(\mathbb P^1\times\mathbb P^1\)

## Finding

Let \(k\) be an algebraically closed field and let \(Y=\mathbb P^1_k\times\mathbb P^1_k\). Let \(Z\) be any subset of the four torus-fixed corners \(\{0,\infty\}\times\{0,\infty\}\), let \(\pi:S=\operatorname{Bl}_Z(Y)\to Y\), and let \(E\) be the sum of the exceptional curves. For \(Z=\varnothing\), take \(S=Y\) and \(E=0\).

The exact value of \(h^0(S,T_S\otimes\mathcal O_S(-E))\) is

| Number of centers | Configuration | \(\operatorname{char}k\ne2\) | \(\operatorname{char}k=2\) |
|---:|---|---:|---:|
| 0 | no blow-up | 6 | 6 |
| 1 | one corner | 3 | 3 |
| 2 | opposite corners | 1 | 1 |
| 2 | adjacent corners (same row or column) | 1 | 2 |
| 3 | any three corners | 0 | 1 |
| 4 | all four corners | 0 | 1 |

Thus the characteristic-two jump is not limited to the four-point blow-up: it also occurs for two adjacent centers and for every three-center subset. The dimension for two opposite centers does not jump.

## Assumptions and scope

All schemes are over an algebraically closed field \(k\), with arbitrary characteristic. The four centers are the distinct coordinate corners of the split quadric surface \(Y\). The sheaf is the tangent bundle twisted by the negative of the reduced sum of the exceptional curves, so its global sections are vector fields on \(S\) vanishing along every exceptional curve. No assertion is made for non-corner centers, infinitely near points, weighted exceptional divisors, or higher-dimensional blow-ups.

## Proof

A global vector field on \(Y\) has the form

\[
 v=(a_0+a_1x+a_2x^2)\frac{\partial}{\partial x}+(b_0+b_1y+b_2y^2)\frac{\partial}{\partial y}.
\]

The blow-down is an isomorphism away from the centers. A vector field on \(S\) therefore descends uniquely to \(Y\) minus the centers and extends uniquely across them because \(T_Y\) is locally free and the omitted set has codimension two. A vector field on \(Y\) lifts to the blow-up at a point precisely when it vanishes at that point.

It remains to impose vanishing along the exceptional curve. In local coordinates \((u,v)\) at a center, write the linear terms of the vector field as

\[
 A(u,v)\frac{\partial}{\partial u}+B(u,v)\frac{\partial}{\partial v},\qquad
 A=au+cv+O((u,v)^2),\quad B=du+bv+O((u,v)^2).
\]

In the blow-up chart \(v=ut\), the lifted field is

\[
 A(u,ut)\frac{\partial}{\partial u}+
 \frac{B(u,ut)-tA(u,ut)}{u}\frac{\partial}{\partial t}.
\]

On the exceptional curve \(u=0\), the second coefficient restricts to \(d+(b-a)t-ct^2\). It vanishes identically exactly when \(c=d=0\) and \(a=b\). Hence the differential of the original vector field at each blown-up corner must be scalar in local coordinates.

Vanishing at the selected \(x\)-coordinates imposes \(a_0=0\) if \(0\) is selected and \(a_2=0\) if \(\infty\) is selected. The analogous conditions are \(b_0=0\) and \(b_2=0\) for the \(y\)-coordinates. If \(A_Z\) and \(B_Z\) are the sets of selected first and second coordinates, respectively, these conditions leave \(6-|A_Z|-|B_Z|\) coefficients before the scalar-differential equations.

In local coordinate \(x\) at \(0\), the derivative coefficient is \(a_1\); at \(\infty\), using \(u=1/x\), it is \(-a_1\). The same sign rule holds for \(b_1\). Each selected corner therefore imposes \(\epsilon_i a_1=\epsilon_j b_1\), where \(\epsilon_0=1\) and \(\epsilon_\infty=-1\). If the selected corners belong to only one of the two parity classes (the diagonal or the anti-diagonal), all these equations have rank one. If both classes occur, the equations include both \(a_1=b_1\) and \(a_1=-b_1\): their rank is two when the characteristic is not two and one in characteristic two.

Consequently, for nonempty \(Z\), the dimension is \(6-|A_Z|-|B_Z|-r\), with \(r=1\) for a single parity class or characteristic two, and \(r=2\) otherwise. Substituting the six possible configurations in the table gives the stated values. For the empty set, \(h^0(Y,T_Y)=h^0(\mathbb P^1,T_{\mathbb P^1})+h^0(\mathbb P^1,T_{\mathbb P^1})=3+3=6\).

## Verification

The standalone script `artifacts/verify_corner_blowups.py` constructs the six-variable constraint matrix for every one of the \(16\) subsets of corners and computes its rank exactly over \(\mathbb Q\) and over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\). It completes with `CHECK_OK: all 16 corner subsets over Q, F2, F3 and F5`. This verifies the linear-algebra census for these fields; the proof above, not finite computation, establishes the formula for all algebraically closed fields of characteristic different from two or equal to two.

## Relationship to prior work

Fujino and Sato, *Characteristic-free characterizations of projective space for smooth toric varieties*, arXiv:2609.03282, Remark 6.2, compute the four-center case: the section space is zero outside characteristic two and one-dimensional in characteristic two. Their local calculation gives the two conditions \(a-b=0\) and \(a+b=0\). The present statement classifies every subset of the four corners, distinguishing opposite from adjacent two-point configurations and giving the three-point cases. The source's four-center calculation alone does not imply those intermediate cases.

## Limitations

The result is restricted to subsets of the four coordinate corners. The calculation does not classify blow-ups at arbitrary points of \(\mathbb P^1\times\mathbb P^1\), nor does it determine higher cohomology of \(T_S\otimes\mathcal O_S(-E)\). The literature search was targeted rather than exhaustive; a broader treatment of vector fields on blow-ups could contain related formulations.

## References

1. O. Fujino and H. Sato, “Characteristic-free characterizations of projective space for smooth toric varieties,” arXiv:2609.03282, especially §6, Remark 6.2 (version 2, posted 2026-09-12; first submitted 2026-09-03). https://arxiv.org/abs/2609.03282
2. The local blow-up chart calculation is given explicitly in the proof above; the cited source uses the same calculation for the all-four-centers case.
