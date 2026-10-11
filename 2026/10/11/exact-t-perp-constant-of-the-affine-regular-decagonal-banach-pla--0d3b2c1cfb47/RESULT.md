# Exact \(T_{\perp}\) constant of the affine-regular decagonal Banach plane
## Finding
Let \(X_{10}=(\mathbb R^2,N_{10})\), put
\[
r=\frac{\sqrt5-1}{2},
\]
and define
\[
N_{10}(s,t)=
\max\left\{
|s+t|,\ |rs+t|,\ r|t|,\ r|s|,\ |s+rt|
\right\}.
\]
The unit sphere is an affine regular decagon.

For the Ahmad--Xie--Li Birkhoff-orthogonal geometric-mean constant
\[
T_{\perp}(X)=
\sup\left\{
\sqrt{\|x+y\|\,\|2x-y\|}:
 x,y\in S_X,\ x\perp_B y
\right\},
\]
one has
\[
T_{\perp}(X_{10})=
\frac12\sqrt{2+5\sqrt5}.
\]
Numerically this is approximately \(1.815236891393169\).

A maximizing pair is
\[
x=(0,1),
\qquad
y=\left(-\frac{1+\sqrt5}{2},\frac{3+\sqrt5}{4}\right).
\]

## Assumptions and scope
All scalars are real. Birkhoff orthogonality is
\[
x\perp_B y
\quad\Longleftrightarrow\quad
\|x+\lambda y\|\ge \|x\|
\quad\text{for every }\lambda\in\mathbb R.
\]

Write
\[
\varphi=\frac{1+\sqrt5}{2}.
\]
A cyclic list of vertices of the unit decagon is
\[
(0,1),\ (-1,\varphi),\ (-\varphi,\varphi),\ (-\varphi,1),\ (-1,0)
\]
and their negatives. The linear map
\[
S=\begin{pmatrix}0&-1\\1&\varphi\end{pmatrix}
\]
sends each listed vertex to the next and satisfies \(S^5=-I\). Since \(\det S=1\) and \(\operatorname{tr}S=\varphi=2\cos(\pi/5)\), it is real-conjugate to a rotation by \(\pi/5\). Thus this polygon is a nonsingular linear image of a Euclidean regular decagon.

The ten signed support functionals can be indexed cyclically by
\[
\begin{aligned}
f_0(s,t)&=s+t,&
f_1(s,t)&=rs+t,&
f_2(s,t)&=rt,\\
f_3(s,t)&=-rs,&
f_4(s,t)&=-s-rt,&
f_{i+5}&=-f_i\quad(0\le i<5).
\end{aligned}
\]
Then \(N_{10}(z)=\max_i f_i(z)\).

## Proof
For a unit vector \(x\), the standard supporting-functional characterization of Birkhoff orthogonality says that
\[
x\perp_B y
\]
if and only if there is a norming functional \(f\) for \(x\) such that \(f(y)=0\).

Every point of the polygonal unit sphere is either in the relative interior of one edge or is a vertex. These two cases exhaust all admissible pairs.

If \(x\) lies in the relative interior of the edge \(f_i=1\), then \(f_i\) is its unique norming functional. Hence \(x\perp_B y\) forces
\[
f_i(y)=0.
\]
The line \(\ker f_i\) meets the unit sphere in exactly two antipodal points. Thus, for each of the ten edges, there are only two possible unit directions for \(y\), while \(x\) remains one-dimensional along the edge.

If \(x=v_i\) is the vertex where \(f_i=f_{i+1}=1\), then the norming functionals at \(x\) form the segment joining \(f_i\) and \(f_{i+1}\). Therefore
\[
x\perp_B y
\quad\Longleftrightarrow\quad
f_i(y)f_{i+1}(y)\le0.
\]
Intersecting this condition with the ten unit edges gives exactly twenty nonempty closed edge subsegments for \(y\) when all ten vertices are enumerated.

Set
\[
P(x,y)=N_{10}(x+y)N_{10}(2x-y).
\]
On every edge or allowed edge subsegment, each factor in \(P\) is the maximum of ten affine functions of one parameter. The checker partitions the parameter interval at every pairwise crossing of those affine functions. On each resulting cell the two active support functionals are fixed, so \(P\) is an ordinary quadratic polynomial. Its maximum is therefore attained at a cell endpoint or at its unique stationary point, if that point lies in the cell. Checking those finitely many candidates with exact arithmetic is exhaustive for the continuum problem.

For the smooth-edge cases the exact maximum product is
\[
P_{\mathrm{edge}}
=
\frac{63-5\sqrt5}{16}.
\]
For the vertex cases the exact maximum is
\[
P_{\mathrm{vertex}}
=
\frac{2+5\sqrt5}{4}.
\]
Moreover,
\[
P_{\mathrm{vertex}}-P_{\mathrm{edge}}
=
\frac{25\sqrt5-55}{16}>0.
\]
Thus the global maximizer is necessarily a nonsmooth vertex configuration.

For
\[
x=(0,1),
\qquad
y=\left(-\varphi,\frac{1+\varphi}{2}\right),
\]
the two support functionals active at \(x\) satisfy
\[
f_0(y)=\frac{1-\sqrt5}{4}<0,
\qquad
f_1(y)=\frac{\sqrt5-1}{4}>0.
\]
Hence a convex combination of \(f_0\) and \(f_1\) annihilates \(y\), proving \(x\perp_B y\). Direct exact evaluation gives
\[
N_{10}(x+y)=\frac{3\sqrt5-1}{4},
\qquad
N_{10}(2x-y)=\frac{7+\sqrt5}{4},
\]
so
\[
P(x,y)=\frac{2+5\sqrt5}{4}.
\]
Taking square roots proves
\[
T_{\perp}(X_{10})=\frac12\sqrt{2+5\sqrt5}.
\]

## Verification
The bundled `verify.py` performs the finite reduction entirely in exact \(\mathbb Q(\sqrt5)\) arithmetic. It reconstructs the ten signed support functionals and ten vertices, verifies every edge incidence, checks all twenty signed smooth-edge Birkhoff cases, and enumerates all vertex Birkhoff subsegments.

For every one-dimensional case it computes all crossings of the two ten-function affine envelopes and tests every endpoint and every interior quadratic stationary point. It certifies
\[
\max P_{\mathrm{edge}}=\frac{63-5\sqrt5}{16},
\qquad
\max P_{\mathrm{vertex}}=\frac{2+5\sqrt5}{4},
\]
and checks the explicit maximizing pair separately. No floating-point sampling is used as a proof.

## Relationship to prior work
Ahmad, Xie and Li introduced \(T_{\perp}\), proved the universal bounds
\[
\sqrt2\le T_{\perp}(X)\le\sqrt6,
\]
computed the square and Hilbert cases, and explicitly noted that values on further specific spaces remained to be determined. Their paper contains no regular-polygon or decagon computation.

Mandal, Sain and Paul proved that every regular polygon with \(4n+2\) vertices is the unit sphere of a Radon plane and described Birkhoff-James orthogonality in polygonal planes through supporting geometry. Their work predates the definition of \(T_{\perp}\), so it supplies structural background rather than the present extremal value.

Mizuguchi studied James constants in Radon planes, including Birkhoff orthogonality as part of that geometry. The publicly accessible preview is highly relevant to the same class of spaces but predates \(T_{\perp}\); it does not state the present constant in the material that was available for inspection. The defining \(T_{\perp}\) paper gives only a one-sided comparison with the James constant, so a James-constant computation does not imply this exact value.

The closest located exact \(T_{\perp}\) computation concerns the smooth plane \(\ell_3^2\), while the closest located exact result on the affine regular decagon concerns a different geometric invariant. Neither statement implies the decagonal Birkhoff-geometric-mean maximum above.

## Limitations
The theorem is specific to the affine regular decagonal plane. It does not give \(T_{\perp}\) for every regular \((4n+2)\)-gonal Radon plane or classify polygonal spaces by the value of \(T_{\perp}\).

The proof is computer-assisted but finite and exact: the mathematical reduction proves that only the enumerated one-dimensional cells need be checked, and the checker evaluates those cells symbolically. Bibliographic and research-index searches cannot prove absolute novelty. The main residual literature risk is an equivalent decagonal computation hidden under different notation or in a source whose full text was not accessible.

## References
1. A. Ahmad, H. Xie and Y. Li, “Some new geometric constants in Banach spaces,” Advances in Fixed Point Theory 12 (2022), Article ID 9, doi:10.28919/afpt/7588. Published 25 August 2022.
2. K. Mandal, D. Sain and K. Paul, “A complete characterization of polygonal Radon planes,” arXiv:1809.04760, first posted 13 September 2018.
3. H. Mizuguchi, “The James constant in Radon planes,” Aequationes Mathematicae 94 (2020), 201–217, doi:10.1007/s00010-020-00698-2.
