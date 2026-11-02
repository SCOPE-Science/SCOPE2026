# All-degree kernel cloning for spline projection on bipartite metric graphs

## Finding

Consider the unit-edge metric realization of \(K_{p,q}\), where \(p,q\ge1\) are integers. Fix any polynomial degree \(d\ge1\), and let \(P_{p,q}^{(d)}\) be real arclength-\(L^2\) orthogonal projection onto functions continuous at vertices and polynomial of degree at most \(d\) on each edge, without matching vertex derivatives. For any vertex \(v\) in the part of size \(p\), denote its evaluation kernel by \(K_v^{(p,q,d)}(e,t)\), with edge coordinate \(t\in[0,1]\) measured from the part of size \(p\).

**Kernel-cloning theorem.** Identify the edges of the \(p\)-leaf star \(K_{p,1}\) with their \(q\) corresponding copies in \(K_{p,q}\), preserving their orientations. For every \(d,p,q\), every source vertex \(v\) in the part of size \(p\), every edge \(e\), and every \(t\in[0,1]\),
\[
K_v^{(p,q,d)}(e,t)=\frac1q K_v^{(p,1,d)}(e',t),
\]
where \(e'\) is the corresponding edge of the \(p\)-leaf star. This is a **pointwise reproducing-kernel identity** across nonisomorphic graphs, not merely a norm comparison.

Consequently, the sharp vertex-evaluation norm
\[
V_d(p)=\sup_{\|f\|_{L^\infty}\le1}|(P_{p,q}^{(d)}f)(v)|
\]
is independent of \(q\): it equals the evaluation norm at a leaf of the \(p\)-leaf star. Its exact formula is given below by two explicitly constructible polynomials and two absolute integrals. For every fixed \(d\), \(V_d(p)\) is nondecreasing in the positive integer \(p\). Thus the maximum vertex-evaluation norm on \(K_{p,q}\) is \(V_d(\max\{p,q\})\), attained at vertices in a largest part. Furthermore,
\[
\lim_{p\to\infty}V_d(p)=\int_0^1\bigl(|A_d(t)|+|B_d(t)|\bigr)\,dt,
\]
with \(A_d,B_d\) explicitly defined below. The sharp negative excursion at the specified vertex for inputs \(0\le f\le1\) is \((V_d(p)-1)/2\).

**Exact formula.** Let \(h_0,h_1\) be the unique minimum-\(L^2[0,1]\)-norm polynomials of degree at most \(d\) having endpoint values respectively \((1,0)\) and \((0,1)\). Equivalently, both are orthogonal to all degree-at-most-\(d\) polynomials vanishing at both endpoints. Put
\[
a_d=\frac1{d(d+2)},\quad b_d=\frac{(-1)^{d+1}}{(d+1)d(d+2)},\quad \Delta_d=a_d^2-b_d^2>0,
\]
and define polynomials
\[
A_d(t)=\frac{h_0(t)}{a_d},\qquad
B_d(t)=\left(\frac{a_d}{\Delta_d}-\frac1{a_d}\right)h_0(t)-\frac{b_d}{\Delta_d}h_1(t).
\]
Then the exact, attained vertex-evaluation norm is
\[
\boxed{V_d(p)=\int_0^1\left|A_d(t)+\frac{B_d(t)}p\right|dt+
\left(1-\frac1p\right)\int_0^1|B_d(t)|dt.}
\]
The polynomials are specified by finite rational linear systems, so this formula determines an algebraic number for every fixed \((d,p)\). As a consistency check, degree one simplifies to \(V_1(p)=(7p+3)/(3(p+1))\), but the theorem applies to *every* degree, not just linear or quadratic elements.

## Assumptions and scope

Every edge has length one and unit arclength density. All edge-polynomial functions are continuous at the original graph vertices; no derivative continuity is required. Input data are essentially bounded measurable real functions on all edges. Evaluation is at an **original vertex**, not at an arbitrary interior edge point. The displayed norm is a norm of a point-evaluation functional after orthogonal projection; it is not claimed to be the full \(L^\infty\)-operator norm when higher-degree elements may have interior norming points.

For \(d=1\), the local bubble space below is zero. For all \(d\ge1\), the endpoint-minimum-norm polynomials exist uniquely because the endpoint trace map onto \(\mathbb R^2\) is surjective.

## Proof

### 1. Local endpoint orthogonalization

Let \(\mathcal P_d\) be the polynomial space of degree at most \(d\) on a unit edge. Let \(W_d=\{g\in\mathcal P_d:g(0)=g(1)=0\}\). The orthogonal complement of \(W_d\) is two-dimensional. The endpoint-interpolating minimum-norm elements \(h_0,h_1\) form a basis of it. Their Gram matrix is
\[
H_d=\begin{pmatrix}a&b\\b&a\end{pmatrix},
\qquad a=\int_0^1h_0^2,\quad b=\int_0^1h_0h_1.
\]
Here symmetry under \(t\mapsto1-t\) gives \(\int h_1^2=a\).

For completeness, the endpoint-reproducing kernels of \(\mathcal P_d\), using Legendre polynomials \(P_j\), have endpoint evaluation Gram matrix
\[
R_d=\begin{pmatrix}(d+1)^2&(-1)^d(d+1)\\(-1)^d(d+1)&(d+1)^2\end{pmatrix}.
\]
Indeed, orthonormal Legendre polynomials on \([0,1]\) are \(\sqrt{2j+1}P_j(2t-1)\), so the diagonal sum is \(\sum_{j=0}^d(2j+1)=(d+1)^2\), and the off-diagonal alternating sum is \(\sum_{j=0}^d(-1)^j(2j+1)=(-1)^d(d+1)\). The minimum-energy endpoint-interpolant Gram matrix is \(H_d=R_d^{-1}\), yielding exactly \(a=a_d\), \(b=b_d\), and \(\Delta_d=a^2-b^2>0\).

### 2. Global nodal mass matrix and inverse row

For the metric graph, each local polynomial decomposes orthogonally as endpoint data in \(\operatorname{span}\{h_0,h_1\}\) plus an edge-interior bubble in \(W_d\). The bubbles from distinct edges are mutually orthogonal and vanish at every vertex. The nodal Gram matrix is therefore
\[
\mathcal M=\begin{pmatrix}a q I_p&b\mathbf1_p\mathbf1_q^T\\b\mathbf1_q\mathbf1_p^T&a p I_q\end{pmatrix}.
\]
To invert its row at a specified vertex \(v\) in the part of size \(p\), split its indicator into a within-part zero-sum component and a part-constant component. On the zero-sum subspace, the matrix acts by \(aq\); on the two part-constant values it is represented by
\[
\begin{pmatrix}aq&bq\\bp&ap\end{pmatrix},
\quad\text{whose inverse is}\quad
\frac1\Delta\begin{pmatrix}a/q&-b/p\\-b/q&a/p\end{pmatrix}.
\]
The resulting inverse-mass row has just three distinct entries:
\[
\begin{array}{c|c}
\text{column vertex}&(\mathcal M^{-1})_{v,\cdot}\\\hline
v & \dfrac{(p-1)/a+a/\Delta}{pq}\\[4pt]
\text{another vertex in the part of size }p&\dfrac{a/\Delta-1/a}{pq}\\[4pt]
\text{a vertex in the opposite part}&-\dfrac{b}{pq\Delta}.
\end{array}
\]
Because vertex evaluation annihilates every bubble, the global reproducing kernel is the above inverse row combined with \(h_0(t)\) and \(h_1(t)\) on each edge. For edges incident with \(v\), its polynomial is
\[
\frac1{pq}\left(\left(\frac{p-1}a+\frac a\Delta\right)h_0(t)-\frac b\Delta h_1(t)\right)
=\frac1q\left(A_d(t)+\frac{B_d(t)}p\right).
\]
On the remaining edges its polynomial is \(B_d(t)/(pq)\). Both types are **exactly \(1/q\) times** the corresponding polynomial for the \(p\)-leaf star (obtained by setting \(q=1\)). This proves pointwise kernel cloning, including endpoint values.

### 3. Norms, monotonicity and sharpness

There are exactly \(q\) edges incident with \(v\) and \((p-1)q\) nonincident edges. The norm of the evaluation functional on \(L^\infty\) is the sum of the \(L^1\) norms of its reproducing kernel on all edges. Summing the two edge types cancels the factor \(q\) and yields the claimed formula for \(V_d(p)\). Taking input equal almost everywhere to the sign of that kernel attains the norm.

Write \(r=1/p\) and \(I(r)=\int_0^1|A_d+rB_d|+(1-r)\int_0^1|B_d|\). For \(0\le r_1\le r_2\le1\), the triangle inequality gives
\[
\int_0^1|A_d+r_2B_d|\le\int_0^1|A_d+r_1B_d|+(r_2-r_1)\int_0^1|B_d|,
\]
so \(I(r_2)\le I(r_1)\). Thus \(V_d(p)\) is nondecreasing in \(p\). Reversing the graph's two parts shows that its largest-part vertices maximize vertex-evaluation norm. The limit as \(p\to\infty\) follows by dominated convergence in the explicit formula.

Finally, since the projection reproduces the constant function one, the kernel integrates to one. For measurable \(0\le f\le1\), the minimum of its integral against the kernel is the integral over the negative kernel region, equal to \((1-V_d(p))/2\). The indicator of the negative region attains this value; hence the sharp negative excursion is \((V_d(p)-1)/2\).

## Verification

Execute `python3 check_clone.py` (Python standard library only). The verifier independently computes the local endpoint-minimal polynomials by exact rational Gram orthogonalization, establishes their general-degree scalar Gram entries for degrees one through eight, directly inverts the global nodal Gram matrices for \(1\le p,q\le6\), and checks the pointwise cloning identities at rational edge coordinates. Its completed execution reported:

```
PASS: independent exact Gram inversions and edge-kernel cloning in 4032 rational cases over degrees 1 through 8
```

The **all-degree, all-size result** is proved analytically by the Legendre endpoint Gram identity and the block inverse, not by the finite calculations.

## Relationship to prior work

Kayumov (2004) studies the endpoint stability of orthogonal least-squares projection for interval \(L\)-splines and gives the historical framework of spline-projector norm questions. Arioli and Benzi (2017) analyze finite-element mass matrices on metric graphs, particularly linear elements and diffusion problems; their accessible detailed presentation does not give an arbitrary-degree complete-bipartite **kernel-cloning identity** or the sharp all-degree endpoint norm reduction.

Known linear-spline and quadratic-spline special cases on balanced multipartite graphs and stars agree with the formula, but these isolated formulas do not supply the degree-uniform pointwise identity, the reduction to a star for every complete bipartite part profile, or the all-degree monotonicity argument. No assertion is made that generic Schur complements, Legendre identities, or known single-degree formulas are individually new.

## Limitations

The theorem needs unit edge lengths, constant unit densities, and all edges bearing the same polynomial degree. Arbitrary positive independent edge weights, subdivided edges, derivative-matching conditions, multigraphs, and vertex boundary conditions are not covered. Only original-vertex evaluation is classified; interior-point evaluation may dominate the full orthoprojector norm. The exact integral formula may require finding roots of a polynomial for numerical evaluation. Previously unindexed equivalent graph-spline identities are a residual publication-priority risk; no independent scientific audit has been carried out.

## References

1. A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418v1, first made public 2004-08-30. https://arxiv.org/abs/math/0408418
2. M. Arioli and M. Benzi, *A finite element method for quantum graphs*, IMA Journal of Numerical Analysis 38 (2018), 1119–1163, first journal online 2017-06-21. https://doi.org/10.1093/imanum/drx029
