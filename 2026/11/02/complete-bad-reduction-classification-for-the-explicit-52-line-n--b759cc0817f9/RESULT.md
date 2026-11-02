# Complete bad-reduction classification for the explicit 52-line nodal quartic

## Finding

Let \(X\subset\mathbf P^3_{\mathbf Z}\) be the integral quartic of Veniani's Example 5.5, with equation
\[
\begin{aligned}
F={}&x_0^2x_1x_2-x_1^3x_2-2x_1^2x_2^2-x_1x_2^3
 +x_0^3x_3+x_0x_1^2x_3+2x_0x_1x_2x_3\\
 &+x_0x_2^2x_3+2x_0^2x_3^2+x_1x_2x_3^2+x_0x_3^3.
\end{aligned}
\]
For every algebraically closed field \(k\) of characteristic \(p\), with \(p=0\) allowed, the geometric singular locus of \(X_k\) is exactly as follows:

| Characteristic | Singularities of the geometric special fiber |
| --- | --- |
| \(p=0\) or \(p\ge7\) | Exactly two ordinary nodes (\(A_1\)) |
| \(p=3\) | Exactly ten ordinary nodes (\(A_1\)) |
| \(p=5\) | Exactly four ordinary nodes (\(A_1\)) |
| \(p=2\) | The entire double plane \(H^2=0\) as the intrinsic projective Jacobian singular scheme, where \(H=x_0+x_1+x_2+x_3\) |

Here the term *intrinsic projective Jacobian singular scheme* means the projective scheme cut out by \(F\) and all four first partial derivatives, with homogeneous-ideal saturation. In characteristic two the **whole quartic**, not merely its singular scheme, is the nonreduced union
\[
X_k=V\!\left(H^2(x_0x_3+x_1x_2)\right).
\]
The quadric \(x_0x_3+x_1x_2=0\) is smooth, and its intersection with the plane \(H=0\) is the union of two distinct lines. Thus precisely the rational primes \(2,3,5\) change the geometric singularity configuration of this fixed integral coordinate model. No statement about preservation of its line count at other primes is implied.

## Assumptions and scope

The coordinates are the literal integral coordinates appearing in Veniani's Example 5.5 (not an arbitrary integral model of its complex projective-isomorphism class). Work over an algebraic closure of the stated characteristic. For every odd characteristic define a projectively invertible linear coordinate change
\[
u=x_0+x_3,\quad v=x_0-x_3,\quad w=x_1+x_2,\quad t=x_1-x_2.
\]
The two fixed points, corresponding to the two classical nodes, are \([u:v:w:t]=[0:1:0:0]\) and \([0:0:0:1]\). In the original coordinates these are respectively \([1:0:0:-1]\) and \([0:1:-1:0]\).

The additional characteristic-three nodes have the following description in the new coordinates (all square roots interpreted in \(k\)):
\[
[u:v:w:t]=[1:v:w:0],\quad v^2=2,\quad w^2=1,
\]
and
\[
[u:v:w:t]=[1:0:w:t],\quad w^2=2,\quad t^2=1.
\]
Each family contains four points. The additional characteristic-five nodes are
\[
[u:v:w:t]=[u:0:1:0],\qquad u^2=3,
\]
which gives two points.

## Proof

**An integral biquadratic identity.** Put \(q=(u^2,v^2,w^2,t^2)^T\) and
\[
M=\begin{pmatrix}-4&2&-3&1\\2&0&1&1\\-3&1&4&-2\\1&1&-2&0\end{pmatrix}.
\]
A polynomial expansion over \(\mathbf Z\) gives the exact identity
\[
8F=-Q,\qquad Q=\tfrac12q^TMq
\]
after the displayed change of coordinates. Equivalently,
\[
Q=t^2u^2+t^2v^2-2t^2w^2-2u^4+2u^2v^2
 -3u^2w^2+v^2w^2+2w^4.
\]
For every odd characteristic this is an invertible coordinate change and the factor \(8\) is invertible. The four first derivatives of \(Q\) are
\[
\frac{\partial Q}{\partial\xi_i}=2\xi_i(Mq)_i,
\qquad (\xi_0,\xi_1,\xi_2,\xi_3)=(u,v,w,t).
\]
At a geometric critical point let \(S\) be the nonempty support of its four coordinates. The vector \(q_S\) has no zero entries and lies in \(\ker M_{S,S}\). Conversely any such nonzero projective vector of squares determines critical points in the algebraic closure. By Euler's identity \(4Q=\sum_i\xi_i\partial Q/\partial\xi_i\), every critical point for odd \(p\) also lies on the quartic.

**Exhaustive principal-minor obstruction.** The determinants of all fifteen nonempty principal submatrices are:

| Size | Index sets (\(u,v,w,t\)) and determinants |
| --- | --- |
| 1 | \(u:-4,\ v:0,\ w:4,\ t:0\) |
| 2 | \(uv:-4,\ uw:-25,\ ut:-1,\ vw:-1,\ vt:-1,\ wt:-4\) |
| 3 | \(uvw:-24,\ uvt:8,\ uwt:24,\ vwt:-8\) |
| 4 | \(uvwt:64\) |

Each nonzero minor has prime factors only in \(\{2,3,5\}\). Hence for any odd characteristic other than three or five the only critical supports are \(\{v\}\) and \(\{t\}\), each producing one point. For \(p=3\) the only further singular supports are \(\{u,v,w\}\) and \(\{u,w,t\}\), whose one-dimensional kernels of square-coordinates have ratios \((1,2,1)\). These give four points each. For \(p=5\) the only further support is \(\{u,w\}\), whose squares satisfy \((u^2,w^2)=(3,1)\) after normalization. These assertions follow by direct substitution into the displayed matrix and exhaustion of its fifteen supports, not by a finite-field point search.

**All isolated singularities are nodes.** In odd characteristic the affine quadratic tangent cone at any singular point is nondegenerate: take an affine chart with one nonzero coordinate normalized to one, and restrict the Hessian of \(Q\) to the remaining three coordinates. At the \(v\)- and \(t\)-axis points the Hessian determinant is respectively \(16\) and \(-16\), nonzero in every odd characteristic. At a characteristic-three point with support \(uvw\) (respectively \(uwt\)) the determinant is \(2\) (respectively \(1\)) modulo three, in the chart \(u=1\). At a characteristic-five point with support \(uw\) it is \(1\) modulo five, in the chart \(w=1\). The affine formal Morse lemma (valid because \(2\) is invertible) makes each a three-variable ordinary quadratic double point. The presence of finitely many isolated singularities also forces every odd-characteristic quartic to be geometrically integral: distinct hypersurface components in \(\mathbf P^3\) would intersect along a singular curve, and a repeated component would be singular in positive dimension.

**The characteristic-two scheme.** Direct reduction in the original integral coordinates yields
\[
F\equiv H^2G\pmod2,\qquad H=x_0+x_1+x_2+x_3,
\qquad G=x_0x_3+x_1x_2.
\]
In characteristic two, \(\partial F/\partial x_i=H^2\,\partial G/\partial x_i\); the four partials of \(G\) are \((x_3,x_2,x_1,x_0)\), which generate the irrelevant homogeneous ideal. Thus the saturated Jacobian ideal, including \(F\), equals exactly \((H^2)\). The quadratic-form gradient proves \(G\) smooth. On \(H=0\), elimination of \(x_3\) shows \(G=(x_0+x_1)(x_0+x_2)\), proving the asserted two-line intersection with the doubled plane.

## Verification

Run `python3 verify_veniani.py` with SymPy installed. It checks the integral polynomial identity, all fifteen exact principal determinants, the exhaustive support-kernel possibilities in characteristics three, five, seven and eleven, the nondegenerate local Hessian determinants, and the characteristic-two factorization and Jacobian partial identities. The universal exclusion of every odd prime outside \(3,5\) is proved by the **integer** determinant table, not by the two control-characteristic enumerations. The expected success token is:

`VENIANI52_PRINCIPAL_MINORS_ALL_ODD_PRIMES_AND_CHAR2_DOUBLE_PLANE_PASS`

## Relationship to prior work

Veniani's 2021 Example 5.5 is the source of the integral equation, the 52 classical lines, the two characteristic-zero nodes, the ten characteristic-three nodes, and the four characteristic-five nodes. It also notes a characteristic-two singular line, but does not state the complete double-plane Jacobian scheme or prove a uniform absence of other exceptional characteristics. The conclusion here concerns **exactly** those two omitted arithmetic assertions and their unifying principal-minor mechanism; the listed characteristic-three and characteristic-five point totals are cited prior facts with an independent proof. Degtyarev and Rams establish the extremal line count over \(\mathbf C\), without a characteristic-by-characteristic singularity classification.

The 2016 version of Veniani's preprint describes a 52-line complex surface whose equation was **then unknown**; the exact displayed integral presentation appears publicly in the source dated 7 February 2021. The two dates are not interchangeable.

## Limitations

This classifies geometric singularities and the saturated Jacobian singular scheme of one integral model; it does not classify its line scheme in every characteristic, nor prove that arbitrary alternative integral models share its reductions. The source already reports the individual characteristic-three and characteristic-five node counts, so neither is asserted to be a new discovery. An equivalent complete-prime argument could occur in unindexed work. Independent validation has not been performed.

## References

1. D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, Manuscripta Mathematica, first public version of record 7 February 2021, Example 5.5, DOI: `10.1007/s00229-021-01284-9`, https://link.springer.com/article/10.1007/s00229-021-01284-9.
2. D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, original arXiv version of 15 August 2016, https://arxiv.org/abs/1608.04209. In that initial version the 52-line surface's equation is stated to be unknown.
3. A. Degtyarev and S. Rams, *Lines on K3-Quartics Via Triangular Sets*, initial preprint 10 January 2023, journal online 6 October 2024, DOI: `10.1007/s00454-024-00690-6`, https://link.springer.com/article/10.1007/s00454-024-00690-6.
