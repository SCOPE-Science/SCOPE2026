# Sharp Ball–Santaló quadratic-moment product for centrally symmetric hexagons

## Finding
For every centrally symmetric convex hexagon \(K\subset\mathbb R^2\) with six genuine vertices, translate its center to the origin, and write \(K^\circ=\{y:\langle x,y\rangle\le1\text{ for every }x\in K\}\). Define the affine-invariant quadratic polar moment product
\[
\mathcal B(K)=\int_K\int_{K^\circ}\langle x,y\rangle^2\,dy\,dx.
\]
Then the sharp two-sided range is
\[
\boxed{\frac89<\mathcal B(K)\le\frac{25}{24}.}
\]
**Equality at the upper endpoint holds exactly for affine-regular hexagons**, that is, the invertible affine images of the Euclidean regular hexagon. The lower endpoint \(8/9\) is not attained by a genuine hexagon; it is the value for every centrally symmetric parallelogram and is approached as a hexagon loses a pair of sides.

More precisely, represent the centered hexagon as \(K=[-a,a]+[-b,b]+[-c,c]\), with three pairwise nonparallel segment directions. Define
\[
x=|\det(a,b)|,\quad y=|\det(b,c)|,\quad z=|\det(c,a)|,\quad
s_1=x+y+z,\quad s_2=xy+yz+zx,\quad s_3=xyz,
\]
and \(D=(x+y)^3(y+z)^3(z+x)^3\). The exact affine-invariant formula is
\[
\boxed{\mathcal B(K)=\frac{8}{9D}\bigl(s_1^3s_2^3-s_1^3s_3^2-s_1^2s_2^2s_3+s_1s_2s_3^2-s_2^3s_3-3s_3^3\bigr).}
\]
In particular, the product depends only on the three determinant magnitudes up to their common scale, and its equality case is characterized by \(x=y=z\).

## Assumptions and scope
A genuine hexagon is a full-dimensional compact convex polygon with exactly six vertices and no redundant adjacent collinear edges. Central symmetry is essential. The integrals are ordinary unnormalized two-dimensional Lebesgue integrals, and polarity is taken *after* translating the center of symmetry to the origin. The product is invariant under invertible linear maps because \((TK)^\circ=T^{-\mathsf T}K^\circ\), the two Jacobians cancel, and the scalar product is preserved. The claim does not concern arbitrary translations of the origin or noncentrally symmetric six-gons.

Every centered centrally symmetric genuine hexagon is a Minkowski sum of three centered segments whose directions are distinct. Suitable choices of signs and a linear change of variables reduce their generators to \(a=(1,0)\), \(b=(0,1)\), and \(c=(p,q)\), for \(p,q>0\). Then \((x,y,z)\) is a common multiple of \((1,p,q)\); the three variables may be permuted freely.

## Proof
**1. Exact moments.** With normalized generators \(a,b,c\) as above, the counterclockwise vertices of \(K\) are
\[
(-1-p,-1-q),\ (1-p,-1-q),\ (1+p,q-1),\ (1+p,1+q),\ (p-1,1+q),\ (-1-p,1-q).
\]
Each edge supports one vertex of the polar, and the counterclockwise polar vertices are
\[
\left(0,-\frac1{1+q}\right),\ \left(\frac q{p+q},-\frac p{p+q}\right),\
\left(\frac1{1+p},0\right),\ \left(0,\frac1{1+q}\right),\
\left(-\frac q{p+q},\frac p{p+q}\right),\ \left(-\frac1{1+p},0\right).
\]
For any counterclockwise polygon with vertices \(v_i=(v_{i1},v_{i2})\), where indices are cyclic, the standard triangle-decomposition formulas give its unnormalized moment matrix \(M=\int_P xx^{\mathsf T}\,dx\):
\[
M_{11}=\frac1{12}\sum_i d_i(v_{i1}^2+v_{i1}v_{i+1,1}+v_{i+1,1}^2),\quad
M_{22}=\frac1{12}\sum_i d_i(v_{i2}^2+v_{i2}v_{i+1,2}+v_{i+1,2}^2),
\]
\[
M_{12}=\frac1{24}\sum_i d_i(2v_{i1}v_{i2}+v_{i1}v_{i+1,2}+v_{i+1,1}v_{i2}+2v_{i+1,1}v_{i+1,2}),
\quad d_i=\det(v_i,v_{i+1}).
\]
Direct substitution, using \(\mathcal B(K)=\operatorname{tr}(M(K)M(K^\circ))\), yields the symmetric exact formula in the finding. This identity is also reconstructed without pre-entered matrices by the accompanying `verify.py`.

**2. Sharp upper endpoint and rigidity.** Let \(N=s_1^3s_2^3-s_1^3s_3^2-s_1^2s_2^2s_3+s_1s_2s_3^2-s_2^3s_3-3s_3^3\). Then
\[
72D\left(\frac{25}{24}-\mathcal B(K)\right)=75D-64N=Q,
\]
where the polynomial certificate is
\[
Q=11s_1^3s_2^3+64s_1^3s_3^2-161s_1^2s_2^2s_3+161s_1s_2s_3^2+64s_2^3s_3+117s_3^3.
\]
Since the expression is symmetric, assume \(x\ge y\ge z>0\). Set \(z=W\), \(y=W+U\), \(x=W+U+V\), with \(W>0\) and \(U,V\ge0\). Expanding \(Q\) gives a homogeneous degree-nine polynomial with **46 strictly positive coefficients**. For a fully explicit certificate, write the coefficient of \(W^k\) as \(\sum c_{k,i} U^iV^{9-k-i}\). Listed in decreasing order of \(i\), the coefficient arrays are:

| \(k\) | descending \(i\) | coefficients \(c_{k,i}\) in the same order |
|---:|:---|:---|
| 0 | 9, 8, 7, 6, 5, 4, 3 | 88, 396, 726, 693, 363, 99, 11 |
| 1 | 8, 7, 6, 5, 4, 3, 2 | 872, 3488, 5698, 4886, 2336, 598, 66 |
| 2 | 7, 6, 5, 4, 3, 2, 1 | 3720, 13020, 18756, 14340, 6156, 1404, 132 |
| 3 | 6, 5, 4, 3, 2, 1, 0 | 8856, 26568, 33272, 22264, 8184, 1480, 88 |
| 4 | 5, 4, 3, 2, 1, 0 | 12672, 31680, 34112, 19488, 5600, 608 |
| 5 | 4, 3, 2, 1, 0 | 10848, 21696, 20256, 9408, 1632 |
| 6 | 3, 2, 1, 0 | 5120, 7680, 6656, 2048 |
| 7 | 2, 1, 0 | 1024, 1024, 1024 |

In particular, the \(W^7\) term is \(1024W^7(U^2+UV+V^2)\). Hence \(Q\ge0\) for all positive \(x,y,z\), and \(Q=0\) only when \(U=V=0\), namely \(x=y=z\). In the normalized representation \((x,y,z)=(1,p,q)\), this means \(p=q=1\), for which the six vertices form an affine-regular hexagon. Conversely, every affine-regular hexagon has equal determinant magnitudes. The formula gives \(\mathcal B=25/24\) there.

**3. Strict lower endpoint.** In normalized coordinates the same vertex integrations give
\[
\mathcal B(K)-\frac89=\frac{8pq\,H(p,q)}{9(1+p)^3(p+q)^3(1+q)^3},
\]
with
\[
\begin{aligned}
H(p,q)={}&2p^4q^2+3p^4q+2p^4+3p^3q^3+8p^3q^2+8p^3q+3p^3\\
&+2p^2q^4+8p^2q^3+10p^2q^2+8p^2q+2p^2\\
&+3pq^4+8pq^3+8pq^2+3pq+2q^4+3q^3+2q^2.
\end{aligned}
\]
All 19 coefficients are positive, so \(\mathcal B(K)>8/9\) when \(p,q>0\). At fixed \(q>0\), letting \(p\downarrow0\) makes one generator parallel to another, and \(\mathcal B\to8/9\). The limiting polygon is a parallelogram; direct integration for the square and linear invariance show every centered parallelogram has \(\mathcal B=8/9\).

## Verification
Run `python verify.py` in a Python 3 environment with SymPy installed. The standalone script independently constructs both vertex lists, obtains their unnormalized moment matrices from shoelace-type formulas, and checks the exact symmetric rational identity, the 46-term nonnegative certificate and its strictness, the 19-term lower positivity polynomial, the two endpoints, and 20 exact rational test cases. All symbolic equalities and polynomial-sign claims use rational/integer arithmetic, rather than approximate floating-point tests. The code is reproducibility evidence and a finite symbolic identity checker; the stated universal inequalities follow from the displayed positive-coefficient identities and geometric reductions, not from numerical sampling.

## Relationship to prior work
Böröczky, Patsalos and Saroglou (first posted February 23, 2026) proved Keith Ball's conjectured quadratic Santaló-type inequality, which bounds \(\mathcal B(K)\) for every origin-symmetric planar convex body by the Euclidean disk value \(\pi^2/8\) and characterizes ellipsoids at equality. That global result does **not** give the sharp six-vertex maximum \(25/24\). The published *Strict log-concavity of Ball's Santaló moment product along the \(\ell_p\) scale* treats a very different one-parameter family of \(\ell_p\) balls, not the full affine moduli of centrally symmetric hexagons. The published *Exact enclosing-parallelogram profile and sharp affine stability for symmetric hexagons* concerns minimum enclosing **area**, not polar second moments. These distinctions are of hypotheses and mathematical implications, not merely titles.

Specific searches for Ball's polar quadratic moment integral, its dual-covariance formulation, affine-regular hexagons, the sharp \(25/24\) constant, and equivalent zonotope determinant parameters did not locate an equivalent published result in the accessible material. The existing general theorem and the published specialized results therefore do not imply the present exact all-hexagon profile. This is a best-knowledge priority assessment, not a proof of historical uniqueness.

## Limitations
The bound requires central symmetry, genuine six-sidedness, and center-based polarity. It does not classify arbitrary polygons or prove a maximum for all polygonal side counts. It is not an independently audited mathematical result. Older literature on polygonal affine inequalities, polar moment tensors, or special cubature identities remains a possible source of earlier equivalent statements. No claim is made that absence from the searched records proves novelty.

## References
1. K. J. Böröczky, K. Patsalos, C. Saroglou, *On Ball's conjectured Santaló type inequality*, arXiv:2602.20325, first publicly posted 2026-02-23 (primary MSC2020 52A20). https://arxiv.org/abs/2602.20325
2. K. Ball, *Isometric problems in \(\ell_p\) and sections of convex sets*, PhD thesis, University of Cambridge, 1986 (original conjecture; cited in reference 1).
3. *Strict log-concavity of Ball's Santaló moment product along the \(\ell_p\) scale*, publicly available mathematical research record, October 2026 (specialized comparison).
4. *Exact enclosing-parallelogram profile and sharp affine stability for symmetric hexagons*, publicly available mathematical research record, October 2026 (same geometric class; different invariant).
