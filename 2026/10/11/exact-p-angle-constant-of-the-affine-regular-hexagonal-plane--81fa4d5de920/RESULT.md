# Exact P-angle constant of the affine-regular hexagonal plane
## Finding
Let \(X_H=(\mathbb R^2,N)\) with
\[
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
Using the P-angle constant
\[
S_P(X)=\sup\{\cos\operatorname{ang}_P(x+y,x-y):x,y\in S_X,\ x\ne\pm y\},
\]
one has the exact value
\[
S_P(X_H)=\frac14.
\]
The supremum is attained, for example, by \(x=(1,1)\) and \(y=(1,0)\).

## Assumptions and scope
All spaces and scalars are real. For nonzero \(u,v\), the P-angle is defined by
\[
\cos\operatorname{ang}_P(u,v)
=
\frac{\|u\|^2+\|v\|^2-\|u-v\|^2}{2\|u\|\|v\|}.
\]
The displayed formula for \(S_P\) is the one introduced by Yang and Li. Their paper states a standing dimension convention earlier in the preliminaries, while Definition 3.1 itself is stated for a Banach space and Remark 3.2 explicitly discusses the two-dimensional Euclidean plane. Here the same formula is evaluated directly on the two-dimensional hexagonal norm above.

## Proof
Write
\[
\phi_1(s,t)=s,\qquad \phi_2(s,t)=t,\qquad \phi_3(s,t)=s-t.
\]
Then
\[
N(z)=\max_{f\in E}f(z),
\qquad
E=\{\pm\phi_1,\pm\phi_2,\pm\phi_3\}.
\]
For \(x,y\in B_{X_H}\), put
\[
A=N(x+y),\qquad B=N(x-y).
\]
Choose \(f,g\in E\) attaining these two maxima. Then
\[
A+B
=f(x+y)+g(x-y)
=(f+g)(x)+(f-g)(y)
\le \|f+g\|_*+\|f-g\|_*.
\]
The dual unit ball has extreme points \(E\). If \(g=\pm f\), the last sum is \(2\). If \(f\) and \(g\) are distinct and nonopposite members of \(E\), direct evaluation on the six vertices
\[
(1,1),(1,0),(0,-1),(-1,-1),(-1,0),(0,1)
\]
of \(B_{X_H}\) shows that the two dual norms are \(1\) and \(2\), in some order. Hence
\[
N(x+y)+N(x-y)\le3.
\]
Triangle inequality also gives \(0\le A,B\le2\).

Now take \(x,y\in S_{X_H}\) with \(x\ne\pm y\), so \(A,B>0\). Since
\[
(x+y)-(x-y)=2y,
\]
the P-angle expression is
\[
\cos\operatorname{ang}_P(x+y,x-y)
=
\frac{A^2+B^2-4}{2AB}.
\]
It remains to prove
\[
2A^2+2B^2-AB\le8.
\]
Let \(s=A+B\). If \(s\le2\), then
\[
2A^2+2B^2-AB=2s^2-5AB\le2s^2\le8.
\]
If \(2\le s\le3\), the inequalities \(A,B\le2\) imply
\[
(2-A)(2-B)\ge0,
\]
hence \(AB\ge2s-4\). Therefore
\[
2A^2+2B^2-AB
=2s^2-5AB
\le2s^2-10s+20
\le8
\]
for \(2\le s\le3\). Consequently
\[
\cos\operatorname{ang}_P(x+y,x-y)\le\frac14.
\]

For \(x=(1,1)\) and \(y=(1,0)\), both vectors are unit, while
\[
N(x+y)=N(2,1)=2,\qquad N(x-y)=N(0,1)=1.
\]
Thus
\[
\cos\operatorname{ang}_P(x+y,x-y)
=
\frac{4+1-4}{2\cdot2\cdot1}
=
\frac14,
\]
which proves sharpness.

## Verification
The bundled verifier enumerates every pair of signed facet functionals in \(E\), checks
\[
\|f+g\|_*+\|f-g\|_*\le3,
\]
verifies the six unit-ball vertices, and checks the attaining pair exactly with rational arithmetic. It also exhaustively checks the algebraic envelope on the vertices of the feasible \((A,B)\)-polygon
\[
0\le A\le2,\qquad 0\le B\le2,\qquad A+B\le3.
\]
The proof of the infinite statement is the analytic argument above; the finite script checks only the finite polyhedral steps used in that proof.

## Relationship to prior work
Yang and Li introduced \(S_P(X)\), proved the universal bound \(0\le S_P(X)\le1/2\), characterized Hilbert spaces by \(S_P(X)=0\), and gave estimates for classical \(\ell_p\) spaces. Their source does not compute the affine-regular hexagonal plane. A separate later result gives the exact \(S_P\) value for real \(\ell_p\) sequence spaces; that statement does not cover this hexagonal norm, whose unit ball is a six-gon rather than an \(\ell_p\) ball. Searches for the exact value, the hexagonal norm, and the P-angle aliases found no statement implying the equality above.

## Limitations
This result concerns one two-dimensional polyhedral norm and one angular constant. It does not classify \(S_P\) on all hexagonal norms, nor does it assert monotonicity under subspaces, quotients, or Banach–Mazur comparison. The bibliographic search cannot prove global uniqueness; no stronger or equivalent covering statement was found in the inspected sources.

## References
1. Z. Yang and Y. Li, “New Geometric Constant Related to the P-angle Function in Banach Spaces,” arXiv:2208.11239, first public version 24 August 2022. Primary MSC: 46B20.
2. “Exact P-angle constant of real \(\ell_p\) sequence spaces,” public research record, 2026. This is used only for an implication comparison with the classical \(\ell_p\) family.
