# Complete centered-distance spectrum and sharp negative-type transition for subdivided hypercubes

## Finding

Let \(Q_d\) denote the binary \(d\)-cube, let \(S(Q_d)\) denote its **once-subdivision** (each edge is replaced by a path of length two), and let \(D_d\) be the matrix of ordinary unweighted shortest-path distances between the vertices of \(S(Q_d)\). Set \(N_d=(d+2)2^{d-1}\), \(a=2^{d-1}\), and \(J_d=I_{N_d}-\mathbf1\mathbf1^{\mathsf T}/N_d\). For every integer \(d\ge2\), define

\[
\eta_{\pm}=
\frac{-((d+1)a+2)\pm\sqrt{((d+1)a+2)^2-16a}}{2}.
\]

**Theorem.** The complete multiset of eigenvalues of the centered distance matrix \(J_dD_dJ_d\), with multiplicities, is

\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
 a-2&d-1\\
 2(a-2)/(d+2)&1\\
 \eta_+&d\\
 \eta_-&d\\
 -2&da-2d\\
 0&2^d-d.
\end{array}
\]

Coincident eigenvalues are counted with additive multiplicity, including the two zero-valued expressions when \(d=2\). For \(d=1\), the centered spectrum is \(\{-2,-2/3,0\}\). Thus the inertia (positive, negative, zero) is exactly

\[
\begin{cases}
(0,2,1),&d=1,\\
(0,4,4),&d=2,\\
(d,\ d2^{d-1},\ 2^d-d),&d\ge3.
\end{cases}
\]

Consequently the shortest-path metric on \(S(Q_d)\) is conditionally negative semidefinite **if and only if** \(d\le2\). Equivalently, the matrix with entries \(\exp(-tD_d(u,v))\) is positive semidefinite for every \(t>0\) if and only if \(d\le2\). In the two admissible dimensions it is strictly positive definite for every positive \(t\); for \(d\ge3\), it fails positive semidefiniteness for every sufficiently small positive \(t\).

There is an explicit obstruction when \(d\ge3\): place coefficient \(+1\) on every edge midpoint of coordinate direction \(1\), coefficient \(-1\) on every edge midpoint of coordinate direction \(2\), and \(0\) elsewhere. This zero-sum coefficient vector \(c\) obeys

\[
 c^{\mathsf T}D_dc=2a(a-2)>0,\qquad
 \lVert c\rVert^2=2a.
\]

**Additional full-distance spectrum.** For \(d\ge2\), put

\[
\Lambda_\pm=\frac{(d+1)^2a-2\pm\sqrt{((d+1)^2a-2)^2-8da(a-2)}}2.
\]

The *uncentered* matrix \(D_d\) has eigenvalues \(\Lambda_+,\Lambda_-\) (each once), \(a-2\) (multiplicity \(d-1\)), \(\eta_+,\eta_-\) (each multiplicity \(d\)), \(-2\) (multiplicity \(da-2d\)), and \(0\) (multiplicity \(2^d-d-1\)). When \(d=1\), its eigenvalues are \(1+\sqrt3,1-\sqrt3,-2\).

## Assumptions and scope

All graph edges in the subdivision have length one. An original vertex of \(Q_d\) is indexed by a binary word \(x\in\{0,1\}^d\). An inserted midpoint \(e_{i,u}\) is indexed by its coordinate direction \(i\in\{1,\ldots,d\}\) and the unique endpoint \(u\) having \(u_i=0\). There are \(2^d=2a\) original vertices and \(da\) midpoints. The distance spectrum is an exact real-matrix spectrum, and positive semidefiniteness concerns all real or complex coefficient vectors. For a metric \(\rho\), conditional negative semidefiniteness means \(\sum_{u,v}c_uc_v\rho(u,v)\le0\) for every real \(c\) with \(\sum_uc_u=0\). No assertion is made about other subdivisions, fractional powered distances, or kernels at a single large scale in the excluded dimensions.

## Proof

**1. Distances.** For binary words \(x,y\) and a coordinate set \(T\), write \(h_T(x,y)\) for their number of differing coordinates in \(T\). Directly minimizing over the endpoints of every midpoint yields

\[
\begin{aligned}
 D_d(v_x,v_y)&=2h_{[d]}(x,y),\\
 D_d(v_x,e_{i,u})&=1+2h_{[d]\setminus\{i\}}(x,u),\\
 D_d(e_{i,u},e_{j,v})&=
 \begin{cases}
 0,&(i,u)=(j,v),\\
 2+2h_{[d]\setminus\{i,j\}}(u,v),&(i,u)\ne(j,v).
 \end{cases}
\end{aligned}
\]

The last formula includes two distinct midpoints in the same direction; the sole zero diagonal is handled separately. Indeed, any path from one midpoint to another begins and ends with their half-edges to cube vertices, and every intermediate cube edge contributes length two. Minimizing the underlying Hamming distance over allowed endpoint bits proves all three formulas.

**2. Exact Walsh blocks.** For \(S\subseteq[d]\), define the Walsh character \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\). Use the normalized vector basis \(2^{-d/2}\chi_S\) on original vertices, and \(a^{-1/2}\chi_S\) on midpoint direction \(i\) whenever \(i\notin S\). These vectors form an orthonormal basis indexed by a frequency \(S\) and its eligible vertex/edge types. Every entry of the distance matrix is a sum of functions affine in Hamming weight, so the elementary identity

\[
 \sum_{z\in\{0,1\}^r}(2|z|+c)\chi_S(z)
 =\begin{cases}2^r(r+c),&S=\varnothing,\\-2^r,&|S|=1,\\0,&|S|\ge2\end{cases}
\]

(with \(S\subseteq[r]\)) makes distinct Walsh frequencies orthogonal invariant blocks. Direct substitution of the distance formulas gives:

* For \(S=\varnothing\), in the original-vertex slot followed by \(d\) midpoint-direction slots, the symmetric block is

\[
 B_0=\begin{pmatrix}
 2da&\sqrt2 da\,\mathbf1_d^{\mathsf T}\\
 \sqrt2 da\,\mathbf1_d&(a-2)I_d+da\,\mathbf1_d\mathbf1_d^{\mathsf T}
 \end{pmatrix}.
\]

The \(d-1\) independent contrasts between midpoint directions have eigenvalue \(a-2\). On the span of the original-vertex mean and midpoint-direction mean, the remaining matrix is

\[
 C_0=\begin{pmatrix}2da&d\sqrt{2d}a\\d\sqrt{2d}a&(d^2+1)a-2\end{pmatrix}.
\]

Its trace is \((d+1)^2a-2\) and determinant \(2da(a-2)\), proving the formulas for \(\Lambda_\pm\). The all-ones vector lies in this plane. Orthogonally projecting this plane onto the all-ones complement leaves exactly one direction, whose Rayleigh quotient is \(2(a-2)/(d+2)\). Thus *centering is a compression*, not a deletion of an uncentered eigenvalue; it replaces the two \(\Lambda\)-eigenvalues by \(0\) and \(2(a-2)/(d+2)\).

* For each singleton \(S=\{k\}\), in the original-vertex slot and the other \(d-1\) midpoint-direction slots the block is

\[
 B_k=\begin{pmatrix}
 -2a&-\sqrt2a\,\mathbf1_{d-1}^{\mathsf T}\\
 -\sqrt2a\,\mathbf1_{d-1}&-2I_{d-1}-a\,\mathbf1_{d-1}\mathbf1_{d-1}^{\mathsf T}
 \end{pmatrix}.
\]

Midpoint-direction contrasts contribute \(d-2\) eigenvalues equal to \(-2\). The remaining two-dimensional block is

\[
 \begin{pmatrix}-2a&-a\sqrt{2(d-1)}\\-a\sqrt{2(d-1)}&-(d-1)a-2\end{pmatrix},
\]

of trace \(-((d+1)a+2)\) and determinant \(4a>0\); its two eigenvalues are exactly \(\eta_+,\eta_-\), both strictly negative.

* For every \(|S|\ge2\), the original-vertex slot has eigenvalue \(0\), and each of the \(d-|S|\) eligible midpoint slots has eigenvalue \(-2\). These are already orthogonal to the global constant and are unchanged by centering.

**3. Counting and sign transition.** There are \(\sum_{s=2}^d\binom ds=2^d-d-1\) high-frequency original-vertex zeros. Adding the centered constant gives \(2^d-d\) zeros. The multiplicity of \(-2\) is

\[
 d(d-2)+\sum_{s=2}^d\binom ds(d-s)
 =d2^{d-1}-2d=da-2d.
\]

Together with the remaining \(2d+d\) eigenvalues and the two-dimensional mean contribution, the multiplicities add to \(N_d=(d+2)a\). For \(d\ge3\), exactly the \(d-1\) midpoint contrasts and one class-contrast eigenvalue are positive, while all \(\eta\)-eigenvalues and all \(-2\)-eigenvalues are negative. At \(d=2\), \(a-2=0\); the centered matrix has four zeros and four negative eigenvalues. For \(d=1\), the graph is a three-vertex path, with centered spectrum \(\{-2,-2/3,0\}\) computed directly.

**4. Positive definite kernels.** Schoenberg's finite-metric criterion identifies conditional negative semidefiniteness of \(D_d\) with positive semidefiniteness of \(\exp(-tD_d)\) for every \(t>0\). In dimensions one and two, the squared Euclidean representation supplied by this criterion maps distinct graph vertices to distinct points, so the corresponding Gaussian kernel is strictly positive definite at positive scales. For \(d\ge3\), the explicit zero-sum witness above yields a negative quadratic form for \(\exp(-tD_d)\) when \(t>0\) is sufficiently small, since its first derivative at zero in that direction is \(-c^{\mathsf T}D_dc<0\). This completes every asserted case.

## Verification

A standalone Python 3 and NumPy checker, `verify_subdivided_cube.py`, reconstructs independent graph adjacency and computes exact breadth-first shortest-path distances for every vertex pair at dimensions \(1\le d\le6\). It then checks every distance against the closed formulas, verifies all unnormalized Walsh invariant-block identities by exact integer matrix multiplication, checks the centered and uncentered eigenvalue lists, and verifies the explicit integer zero-sum obstruction. Successful run output:

```
SUBDIVIDED_CUBE_EXACT_BLOCKS_AND_BFS_OK
dimensions=1..6; vertices= [3, 8, 20, 48, 112, 256]
all_pairs_distances_checked= 80857
Walsh_basis_dimensions_checked= 447
analytic_eigenvalue_crosschecks=12 (centered and uncentered)
No finite computation is claimed to certify all dimensions.
```

Run with `python3 verify_subdivided_cube.py` after installing NumPy (`python3 -m pip install numpy`). The universal proof is the exact block calculation and sign analysis above; finite tests are consistency checks only.

## Relationship to prior work

Liu and collaborators (2013) explicitly study the subdivision graph of the binary cube, but calculate Kirchhoff indices and Laplacian/resistance invariants, **not** its geodesic distance-matrix inertia. Aalipour and collaborators (2015) study distance spectra of several distance-regular graph families (including halved cubes), but not the once-subdivided cube. Howlader and Panigrahi (2021) obtain distance spectra of subdivisions of certain minimal cages, including complete and complete bipartite examples. The binary cube of dimension at least three is not a minimal degree-\(d\), girth-four cage (the minimum is the \(2d\)-vertex graph \(K_{d,d}\)); their enumerated families therefore do not imply the theorem for the arbitrary-dimensional subdivided cube. The present result distinguishes geodesic distance from the electrical-resistance metric and distinguishes midpoint subdivision from the cube's line graph.

The named earlier methods and results are acknowledged; an equivalent theorem hidden in less searchable older distance-spectral or Fourier literature has not been conclusively excluded.

## Limitations

The theorem concerns precisely **one subdivision** of each binary cube edge, ordinary unit-edge geodesic distances, every integer cube dimension, and the all-scales Gaussian-kernel criterion. It does not calculate the largest fractional negative-type exponent for the excluded dimensions, nor the individual scales where kernels may regain positivity. Originality has received a bounded literature comparison, not an exhaustive historical classification. The supplied checker does not constitute a proof for untested dimensions, and no independent mathematical audit has been performed.

## References

1. J. Liu et al., *The Kirchhoff Index of Hypercubes and Related Complex Networks*, *Discrete Dynamics in Nature and Society* (2013), article 543189. First published 12 December 2013. DOI: `10.1155/2013/543189`.
2. G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196 (2015), `https://arxiv.org/abs/1509.01196`.
3. A. Howlader and P. Panigrahi, *On the distance spectrum of minimal cages and associated distance biregular graphs*, arXiv:2109.05274 (2021), `https://arxiv.org/abs/2109.05274`.
4. I. J. Schoenberg, *Metric spaces and positive definite functions*, *Transactions of the American Mathematical Society* 44 (1938), 522–536.
