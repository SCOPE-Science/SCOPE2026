# Sharp negative-type thresholds for bouquets of five-cycles

## Finding

Let \(B_m\), for each integer \(m\ge2\), be the finite unit-edge graph obtained from \(m\) copies of the five-cycle \(C_5\) by identifying one vertex from every copy and making no other identifications. Let \(d\) be its shortest-path metric. Define the supremal negative-type exponent by
\[
\wp(B_m)=\sup\left\{p\ge0:\sum_{x,y\in B_m}z_xz_y d(x,y)^p\le0\text{ for every real }z\text{ with }\sum_xz_x=0\right\}.
\]
Set \(p_c=\log_2((3+\sqrt5)/2)\) and, for \(1\le p\le p_c\), put \(a=2^p\), \(b=3^p\), and
\[
M_m(p)=\begin{pmatrix}
(2m-1)a-4m & 2(m-1)b-(2m-1)(a+1)\\
2(m-1)b-(2m-1)(a+1) &1-4ma+2(m-1)a^2
\end{pmatrix}.
\]
**Theorem.** There is exactly one \(p_m\in(1,p_c)\) such that the largest eigenvalue of \(M_m(p_m)\) is zero. Equivalently, \(p_m\) is the unique root in that interval of \(\det M_m(p)=0\) for which \(\operatorname{tr}M_m(p)<0\). Then
\[
\boxed{\wp(B_m)=p_m.}
\]
The metric has strict \(p\)-negative type for \(0\le p<p_m\), has nonstrict \(p_m\)-negative type with exactly one independent zero-sum equality load, and fails \(p\)-negative type for \(p>p_m\). Thus \(d^{p/2}\) embeds isometrically into a real Hilbert space exactly for \(0\le p\le p_m\). Its minimum affine embedding dimension is \(4m\) below the threshold and \(4m-1\) at the threshold.

The thresholds decrease strictly with the number of petals and converge to one. More precisely, writing \(L_2=\log2\), \(L_3=\log3\),
\[
B_0=68L_2-36L_3,\quad \Delta_0=16L_2^2+48L_2L_3-36L_3^2,\quad
\theta=\frac{10}{B_0+\sqrt{B_0^2-20\Delta_0}},
\]
where \(\theta\approx0.712036959714\), we have
\[
\boxed{p_m=1+\frac{\theta}{m-1}+O(m^{-2})\qquad(m\to\infty).}
\]
The first thresholds are \(p_2\approx1.292103194526\), \(p_3\approx1.219261982617\), \(p_4\approx1.171450502792\).

## Assumptions and scope

All graphs are finite, undirected, unweighted, connected, and carry their ordinary shortest-path distances. Each petal is the five-cycle with cyclic vertices \((o,1,2,3,4)\); only the vertex \(o\) is shared. Distances between different petals are sums of their distances to \(o\). The zero-sum loads are real, and zero-exponent powered distances use the standard convention of zero on the diagonal and one on pairs of distinct vertices. The theorem concerns the exact negative-type inequality, not merely tested dimensions or an approximate spectral calculation.

## Proof

**1. Anchoring and exact symmetry reduction.** For each petal \(j\), let \(x_j\in\mathbb R^4\) contain the coefficients of the nonshared vertices \((1,2,3,4)\). The coefficient at \(o\) is uniquely \(-\sum_j\mathbf1^{\mathsf T}x_j\). If \(r=(1,2,2,1)\), the zero-sum powered-distance quadratic form becomes \(\sum_{j,k}x_j^{\mathsf T}T_{jk}(p)x_k\), where
\[
T_{jj}(p)_{uv}=d_{C_5}(u,v)^p-r_u^p-r_v^p,
\qquad T_{jk}(p)_{uv}=(r_u+r_v)^p-r_u^p-r_v^p\quad(j\ne k).
\]
Use on every petal the orthonormal reflection-symmetric vectors \((1,0,0,1)/\sqrt2\), \((0,1,1,0)/\sqrt2\) and the reflection-antisymmetric vectors \((1,0,0,-1)/\sqrt2\), \((0,1,-1,0)/\sqrt2\). The within-petal forms in these two sectors are respectively
\[
S_p=\begin{pmatrix}a-4&-a-1\\-a-1&1-4a\end{pmatrix},\qquad
A_p=\begin{pmatrix}-a&1-a\\1-a&-1\end{pmatrix}.
\]
The between-petal form vanishes on all antisymmetric vectors and has symmetric block
\[
C_p=2\begin{pmatrix}a-2&b-a-1\\b-a-1&a^2-2a\end{pmatrix}.
\]
Diagonalizing the all-ones and sum-zero representations of petal permutations gives the **complete** orthogonal block decomposition
\[
\boxed{T(p)\simeq A_p^{\oplus m}\oplus(S_p-C_p)^{\oplus(m-1)}\oplus\big(S_p+(m-1)C_p\big).}
\]
The final two-dimensional block is exactly \(M_m(p)\). There are \(2m+2(m-1)+2=4m\) dimensions, so no modes have been omitted.

**2. Negativity of all competing modes.** For \(1\le p<p_c\), we have \(2\le a<(3+\sqrt5)/2\) and
\[
\det A_p=-a^2+3a-1>0,\qquad \det S_p=5(-a^2+3a-1)>0.
\]
Both symmetric matrices have negative leading diagonal entries, hence are negative definite. For \(1<p<2\), the scalar kernel \((s+t)^p-s^p-t^p\) on positive arguments is positive definite: indeed
\[
(s+t)^p-s^p-t^p=\frac{p(p-1)}{\Gamma(2-p)}\int_0^\infty(1-e^{-su})(1-e^{-tu})u^{-p-1}\,du.
\]
This follows by taking two derivatives and checking the zero boundary values. The two functions \(1-e^{-u}\) and \(1-e^{-2u}\) are linearly independent, so their resulting two-by-two Gram matrix \(C_p\) is strictly positive definite. Therefore \(S_p-C_p\) is negative definite throughout \(1<p<p_c\). At \(p=1\), \(C_1=0\) and all blocks are negative definite.

**3. Critical crossing.** At \(p=1\), \(M_m(1)=\bigl(\begin{smallmatrix}-2&-3\\-3&-7\end{smallmatrix}\bigr)\), which is negative definite. At \(p=p_c\), \(S_{p_c}\) is singular negative semidefinite; since \(C_{p_c}\) is positive definite and \(m\ge2\), \(M_m(p_c)\) has a positive Rayleigh quotient along the kernel of \(S_{p_c}\). Continuity therefore produces a crossing in \((1,p_c)\). The standard strictness/interval theorem for negative type on finite metrics states that having \(q\)-negative type implies **strict** \(p\)-negative type for every \(p<q\). Thus once a nonzero equality direction appears, negative type cannot hold again at a larger exponent. Consequently the top eigenvalue of \(M_m\) has exactly one zero, its first crossing \(p_m\), and all other blocks remain negative definite there. Its other eigenvalue is negative at the crossing, proving uniqueness of the equality-load direction and the trace-qualified determinant characterization. For \(p>p_c\) the isometric five-cycle subspace itself fails negative type, so the failure persists over the entire upper range.

**4. Monotonicity and asymptotic.** For every fixed \(p\in(1,p_c)\), \(C_p\) is positive definite, and hence the largest eigenvalue of \(M_{m+1}(p)=M_m(p)+C_p\) is strictly larger than that of \(M_m(p)\). The interval property therefore gives \(p_{m+1}<p_m\). Since \(M_m(p)\) eventually has a positive eigenvalue for every fixed \(p>1\) sufficiently close to one, \(p_m\downarrow1\).

Put \(t=(m-1)(p-1)\). Uniformly on compact \(t\)-intervals, Taylor expansion at \(p=1\) gives
\[
M_m(1+t/(m-1))=S_1+tC'_1+O(m^{-1}),\quad
C'_1=\begin{pmatrix}4L_2&6L_3-4L_2\\6L_3-4L_2&8L_2\end{pmatrix}.
\]
Here \(S_1\) is negative definite and \(C'_1\) is positive definite by the limiting integral Gram representation. Direct expansion yields
\[
\det(S_1+tC'_1)=5-B_0t+\Delta_0t^2.
\]
Its two positive roots are distinct; the smaller root is \(\theta\) in the theorem. The upper eigenvalue crosses transversely there, so the implicit-function theorem gives \((m-1)(p_m-1)=\theta+O(m^{-1})\), as required.

**5. Embedding dimension.** For a finite metric, the centered Gram matrix of \(d^p\) has rank equal to the dimension of the zero-sum space minus the nullity of its negative-type quadratic form. Here that space has dimension \(4m\), with nullity zero before the endpoint and one at it. This proves both asserted minimum affine dimensions and finishes the theorem.

## Verification

The standalone script `checker.py` independently reconstructs the graph by breadth-first search, constructs the full anchored powered-distance quadratic form, and compares its entire spectrum with the exact orthogonal block decomposition. It checks parameter examples on both sides of the crossing, endpoint nullity, strict decrease in sampled petal counts, and the first-order asymptotic against the analytic constant. A completed replay returned `PASS: 1993 supplementary finite spectral and asymptotic assertions`; representative thresholds are printed in the theorem. These finite checks are **not** the infinite-dimensional or all-parameter proof: the proof is the analytic reduction above.

## Relationship to prior work

Doust and Weston's *Polygonal equalities and p-negative type* (arXiv:2404.06658; first posted 9 April 2024) establishes general correspondence between the endpoint and polygonal equalities; it does not calculate this graph family. Li and Weston (arXiv:0901.0695) give the strict-negative-type interval principle used above. Sánchez (arXiv:1108.0451) gives a general finite-metric determinant method but not the two-by-two family classification or petal asymptotic. Kokkendorff's *Geometry and Combinatorics* (2002), Corollary 5, establishes stability of ordinary (strict) negative type under one-point gluing. That \(p=1\) theorem is consistent with, but does not imply, the sharp \(p>1\) behavior obtained here. Doust and Weston's *Beyond trees* (arXiv:2404.06684) concerns subsets of weighted Hamming cubes and strict one-negative-type criteria, not the present explicit variable-exponent bouquet thresholds.

## Limitations

The result concerns only unweighted bouquets of at least two identical five-cycles. Mixed cycle lengths, weighted petals, attachments along edges rather than a single vertex, and nonlinear Hilbert distortion beyond exact snowflake embeddability are not classified. A literature search cannot rule out unindexed historical equivalent formulas, and independent mathematical validation has not been performed.

## References

1. I. Doust and A. Weston, *Polygonal equalities and p-negative type*, arXiv:2404.06658 (2024), https://arxiv.org/pdf/2404.06658.
2. I. Doust and A. Weston, *Beyond trees: the metric geometry of subsets of weighted Hamming cubes*, arXiv:2404.06684 (2024), https://arxiv.org/pdf/2404.06684.
3. H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695 (2009), https://arxiv.org/pdf/0901.0695.
4. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451 (2011), https://arxiv.org/pdf/1108.0451.
5. S. L. Kokkendorff, *Geometry and Combinatorics*, Ph.D. thesis, Technical University of Denmark (2002), Corollary 5, https://backend.orbit.dtu.dk/ws/files/6303901/phd-2002-SimonKokkendorf.pdf.
