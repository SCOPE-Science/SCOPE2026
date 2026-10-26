# A two-parameter tensor-generation frontier in the Oda–Miyake toric threefolds

## Finding
Let \(a,d\in\mathbb Z\), put \(k=d-a\), and let \(X_{a,d}=Z''_{13}(a,2,a+2,d)\) be the smooth complete nonprojective toric threefold of Construction 6.1 in Ito–Zeng–Zeng [1]. Then
\[
\omega_{X_{a,d}}\text{ is tensor-generating}\quad\Longleftrightarrow\quad
k=\pm1\ \text{ or }\ (k=0\text{ and }a\notin\{-1,-2\}).
\]
For every \(|k|\ge2\), the failure is already detected by a torus-invariant prime divisor, not merely by a zero-degree invariant curve. In particular, for \(a=0\) and every integer \(d\le-5\) or \(d\ge4\), the canonical bundle is **not** tensor-generating although its degree on **every torus-invariant curve is nonzero**. This last clause does not exclude non-invariant zero-degree curves.

A line bundle \(L\) on a proper variety is tensor-generating if its integral tensor powers generate the triangulated category of perfect complexes. An invariant divisor \(D_i\) obstructs tensor-generation if neither the canonical bundle nor its inverse is big on \(D_i\).

## Assumptions and scope
Work over any field, using the smooth complete fan in \(N=\mathbb Z^3\). Its eight primitive generators are
\[
\begin{aligned}
v_1&=(1,1,2),&v_2&=(1,0,0),&v_3&=(0,-1,0),&v_4&=(0,0,-1),\\
v_5&=(-1,a,d),&v_6&=(0,1,0),&v_7&=(0,0,1),&v_8&=(-1,a+2,d+1).
\end{aligned}
\]
The maximal cones, written by their ray indices, are `124,234,345,456,146,167,127,237,358,568,378,678`. These give a smooth complete nonprojective fan by [1, Construction 6.1 and Remark 6.2]. The conclusion concerns precisely the two-parameter subfamily with the second fan parameter \(b=2\) and third parameter \(c=a+2\), not all four parameters of \(Z''_{13}\).

## Proof
By the hyperplane criterion [1, Corollary 3.6], on a smooth complete toric threefold the canonical bundle is tensor-generating precisely if (i) each primitive ray generator is a vertex of the convex hull of itself and all rays sharing a cone with it, and (ii) the anticanonical degree of every invariant wall curve is nonzero. Maximal cones contribute no further condition.

**Ray analysis.** The extreme-coordinate planes \(x=1\) and \(x=-1\) make \(v_1,v_2,v_5,v_8\) vertices for every \(a,d\): the intersections with the respective neighbor hulls are segments with these rays as distinct endpoints. On the plane \(x=0\), use coordinates \(h=y-z\) and \(g=y+z\). Then
\[
(h,g)(v_3)=(-1,-1),\quad(h,g)(v_4)=(1,-1),\quad
(h,g)(v_6)=(1,1),\quad(h,g)(v_7)=(-1,1).
\]
Set \(A=(v_2+v_5)/2\), \(B=(v_2+v_8)/2\), \(C=(v_1+v_5)/2\), and \(D=(v_1+v_8)/2\). Their relevant values are
\[
h(A)=h(D)=-k/2,\qquad h(B)=(1-k)/2,\qquad h(C)=(-1-k)/2,
\]
\[
g(A)=a+k/2,\qquad g(D)=a+k/2+3.
\]
The sections \(x=0\) of the neighbor convex hulls of rays \(3,4,6,7\) are, respectively, the convex hulls of
\[
\{v_4,v_7,A,B\},\quad\{v_3,v_6,A,C\},\quad
\{v_4,v_7,C,D\},\quad\{v_3,v_6,B,D\}.
\]
Indeed all nonzero-\(x\) neighbor rays in each case have first coordinate \(+1\) or \(-1\), so their balanced convex combinations are exactly the indicated pairwise midpoints. When \(|k|\le1\), the plane \(h=-1\) supports the first and fourth sections only at their edge \([v_3,v_7]\), and \(h=1\) supports the second and third sections only at \([v_4,v_6]\). Thus all eight rays pass the vertex criterion.

Suppose \(k\ge2\) and put \(t=4/(k+2)\in(0,1]\). The points
\[
Q_A=tA+(1-t)v_4,\qquad Q_D=tD+(1-t)v_6
\]
have \(h=-1\) and, respectively,
\[
g(Q_A)=\frac{4a+k+2}{k+2},\qquad g(Q_D)=\frac{4a+3k+10}{k+2}.
\]
If \(2a+k+2\le0\), then \(g(Q_A)\le-1\); hence \(v_3\) belongs to the segment \([Q_A,v_7]\), contained in the convex hull of the other neighbors \(v_2,v_4,v_5,v_7\) of ray \(3\). If \(2a+k+4\ge0\), then \(g(Q_D)\ge1\); hence \(v_7\) belongs to \([v_3,Q_D]\), contained in the neighbor convex hull \(\operatorname{conv}\{v_1,v_3,v_6,v_8\}\). At least one inequality always holds, because their negations are incompatible. Therefore some divisor fails the ray criterion.

Suppose \(k\le-2\), with \(t=4/(2-k)\in(0,1]\). Now
\[
Q_A=tA+(1-t)v_3,\qquad Q_D=tD+(1-t)v_7
\]
have \(h=1\) and
\[
g(Q_A)=\frac{4a+3k+2}{2-k},\qquad g(Q_D)=\frac{4a+k+10}{2-k}.
\]
If \(2a+k+2\le0\), then \(g(Q_A)\le-1\), so \(v_4\in[Q_A,v_6]\), which is contained in the convex hull of its other neighbors \(v_2,v_3,v_5,v_6\). If \(2a+k+4\ge0\), then \(g(Q_D)\ge1\), so \(v_6\in[v_4,Q_D]\), contained in the convex hull of its other neighbors \(v_1,v_4,v_7,v_8\). Again the two alternatives cover all \(a\). This proves a divisor obstruction for every \(|k|\ge2\), with exact convex-combination certificates, including boundary equalities.

**Wall analysis.** Denote the invariant curve for the wall spanned by \(v_i,v_j\) by \(C_{ij}\). For each wall, if \(v_m,v_n\) are the two rays on its opposite sides, the smooth toric wall relation has the form \(v_m+v_n=\alpha v_i+\beta v_j\), and
\[
(-K_X)\cdot C_{ij}=2-\alpha-\beta.
\]
Enumerating the 18 wall relations from the listed fan gives the following exact degrees:

| Wall | \((-K_X)\cdot C_{ij}\) | Wall | \((-K_X)\cdot C_{ij}\) |
| --- | ---: | --- | ---: |
| 12 | \(2\) | 14 | \(-1\) |
| 16 | \(2\) | 17 | \(3\) |
| 23 | \(2\) | 24 | \(3\) |
| 27 | \(-1\) | 34 | \(2a+k+2\) |
| 35 | \(3\) | 37 | \(3-k\) |
| 38 | \(-1\) | 45 | \(2\) |
| 46 | \(k+3\) | 56 | \(-1\) |
| 58 | \(2\) | 67 | \(-2a-k-4\) |
| 68 | \(3\) | 78 | \(2\) |

When \(|k|\le1\), the only possible zeroes are at \(k=0,a=-1\) for wall \(34\), and at \(k=0,a=-2\) for wall \(67\). Thus combining wall and ray criteria proves the classification. With \(a=0\) and \(k=d\), the four variable degrees are \(d+2\), \(3-d\), \(d+3\), and \(-d-4\), all nonzero when \(d\le-5\) or \(d\ge4\). Divisor obstructions persist in those ranges by the ray analysis, proving the final assertion.

## Verification
Run `python verify.py` with Python 3 and SymPy. The script reconstructs the 18 wall relations from the maximal cones and symbolically verifies every table entry; verifies the four exact rational convex certificates; and checks representative integer parameters in both infinite wings. The universal conclusions are proved by the symbolic identities and elementary inequalities above, not by the finite samples.

## Relationship to prior work
Ito–Zeng–Zeng [1] establish the invariant-orbit combinatorial criterion, the fan, the complete \(k=1\) family, and the \(k=0\) family. In their Question 6.6 they request a broader parameter classification and ask whether obstructions always come from invariant \((-1,-1)\)-curves. The present two-parameter theorem extends their \(k=0,1\) calculations to all integer \(k\), adds the negative \(k=-1\) tensor-generating family, and gives explicit invariant-divisor obstructions and infinite regimes without any invariant zero-degree curve. The general phenomenon that invariant divisors may obstruct is not claimed to originate here: it is part of [1, Section 7]. A preceding explicit calculation already treats the one-dimensional subfamily \(a=-2,d\ge2\), exhibits a divisor obstruction with no invariant zero-degree curve, and constructs non-invariant zero-degree curves. That previously established subcase is included here, not claimed as new; the contribution is the complete two-parameter classification and extension beyond that slice. Fujino–Sato [2] treat projectivity, fans, and related birational behavior; a matching tensor-generation classification was not found in the material checked.

## Limitations
The statement is restricted to the explicit \((a,2,a+2,d)\) slice of the four-parameter family. It does not classify all \(Z''_{13}(a,b,c,d)\), all toric autoequivalences, or all obstructing non-invariant curves. The nonzero-degree assertion is only for torus-invariant curves; the general curve criterion of [1] guarantees a non-invariant degree-zero curve whenever tensor-generation fails but no invariant curve has zero degree. The proofs use the published tensor-generation criterion. Exact priority against unindexed literature has not been independently established.

## References
[1] D. Ito, M. R. Zeng, X. Zeng, *Tensor-generating line bundles on toric varieties*, arXiv:2610.22279v1 (first public 15 October 2026), Sections 3, 6.1, 7. https://arxiv.org/abs/2610.22279

[2] O. Fujino and H. Sato, *On non-projective complete toric varieties*, arXiv:2412.02392 (2024), cited for classification and birational context. https://arxiv.org/abs/2412.02392
