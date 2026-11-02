# Sharp maximum-norm sensitivity of conservative capped-simplex cell-average limiters

## Finding

Fix an integer \(N\ge2\) and any mass \(s\in(0,N)\). Define
\[
H_s=\{x\in\mathbb R^N:\sum_{i=1}^N x_i=s\},\qquad
C_s=H_s\cap[0,1]^N,
\]
and let \(Q_s:H_s\to C_s\) be the unique Euclidean nearest-point projection. On a mesh of \(N\) equal-volume cells, \(Q_s\) is precisely the conservative, unit-bound cell-average limiting step. Its **exact global maximum-norm Lipschitz modulus on the fixed-mass input hyperplane** is
\[
\boxed{\sup_{x\ne y\in H_s}\frac{\|Q_s(x)-Q_s(y)\|_\infty}{\|x-y\|_\infty}
=2-\frac{2}{\lfloor N/2\rfloor+1}.}
\]
The supremum is attained by distinct inputs in a common strict active-set region for every \(N\ge3\) and every interior mass \(s\), and by a feasible interior pair for \(N=2\). Thus the mapping is \(\ell_\infty\)-nonexpansive for \(N=2,3\), strictly expansive for every \(N\ge4\), and the sharp factor approaches \(2\) as \(N\) increases. In particular, the first expansive configuration has four cells and sharp factor \(4/3\).

## Assumptions and scope

The cells all have the **same volume**, the admissible interval is shared and normalized to \([0,1]\), the input vectors have **identical prescribed mass** \(s\), and the correction minimizes ordinary squared Euclidean distance between cell averages. Both compared inputs may violate the bound; neither is assumed feasible. The theorem is about this single cell-average projection, not about a complete DG timestep or the high-order-moment scaling limiter. Translation and positive scaling of the common admissible interval leave the dimensionless constant unchanged.

## Proof

**1. KKT map and affine regions.** The standard capped-simplex KKT equations yield the water-level formula
\[
Q_s(x)_i=\min\{1,\max\{0,x_i-\lambda\}\},\qquad
\sum_i Q_s(x)_i=s.
\]
The projected point is unique although \(\lambda\) need not be unique if all output coordinates are at bounds. The mapping is continuous and piecewise affine: each strict active region has free indices \(F=\{i:0<Q_s(x)_i<1\}\), with \(k=|F|\), and clipped complement \(B\) with \(b=N-k\). If \(k\ge1\), the active region's shift satisfies
\[
\lambda=\frac{\sum_{i\in F}x_i+\#\{i\in B:Q_s(x)_i=1\}-s}{k}.
\]
Let \(v\in H_0=\{v:\sum_i v_i=0\}\). On this region, for \(i\in F\),
\[
(DQ_s(x)v)_i=v_i-\frac1k\sum_{j\in F}v_j
=v_i+\frac1k\sum_{j\in B}v_j,
\]
while clipped output coordinates have derivative zero. If \(k=0\) or \(k=1\), the local derivative vanishes on \(H_0\); when \(B=\varnothing\) and \(k=N\), the derivative is the identity on \(H_0\).

**2. Exact fixed-mass operator norm of each active-region derivative.** For \(2\le k\le N\), choose a free coordinate \(i\) and \(\|v\|_\infty\le1\) with \(\sum_j v_j=0\). Writing \(a=v_i\in[-1,1]\) and \(S_B=\sum_{j\in B}v_j\), the cube constraints and zero sum imply simultaneously
\[
S_B\le b,\qquad S_B=-a-\sum_{j\in F\setminus\{i\}}v_j\le k-1-a.
\]
Hence
\[
(DQ_s(x)v)_i\le a+\frac{\min\{b,k-1-a\}}{k}
\le1+\frac{\min\{b,k-2\}}{k},
\]
since both affine branches of the expression are nondecreasing in \(a\). Replacing \(v\) by \(-v\) handles the absolute value. Both bounds are attained by zero-sum sign/zero configurations: when \(b\le k-2\), set \(v_i=1\), all \(b\) clipped perturbations to \(1\), and \(b+1\) other free perturbations to \(-1\); set the remaining free perturbations to zero. When \(b\ge k-2\), set \(v_i=1\), all other \(k-1\) free perturbations to \(-1\), and exactly \(k-2\) clipped perturbations to \(1\), the remainder zero. Consequently the precise restricted derivative norm is
\[
L_{k,N}=1+\frac{\min\{N-k,k-2\}}k\quad(2\le k\le N),
\]
with the one-free-coordinate value zero. For \(k\le(N+2)/2\), this equals \(2-2/k\) and increases with \(k\); for \(k\ge(N+2)/2\), it equals \(N/k\) and decreases with \(k\). Therefore
\[
\max_{1\le k\le N}L_{k,N}=2-\frac{2}{\lfloor N/2\rfloor+1}.
\]
Because \(Q_s\) is continuous piecewise affine, integrate these bounds along a generic segment in \(H_s\); use continuity to pass to nongeneric endpoints and segments. This proves the global upper bound.

**3. Attainability for each prescribed mass.** For \(N\ge3\) set \(k=\lfloor N/2\rfloor+1\), \(b=N-k\); then \(1\le b<k\). As \(b<k\), every \(s\in(0,N)\) satisfies either \(s<k\) or \(s>b\). In the first case choose the projected free values \(z_i=s/k\) for \(i\in F\), with all clipped projected values zero. For small \(\eta>0\), let \(x_i=s/k+\eta\) on \(F\) and \(x_i=-k\eta/b\) on \(B\). These inputs have total mass \(s\), and KKT gives \(Q_s(x)=z\) with a strict lower-clipped region. In the second case set the clipped projected values to one, the free projected values to \((s-b)/k\), and take the corresponding input coordinates \(x_i=(s-b)/k-\eta\) on \(F\), \(x_i=1+k\eta/b\) on \(B\). These give a strict upper-clipped region. For either construction, fix a free index \(i_0\) and take
\[
v_{i_0}=1,\quad v_j=-1\ (j\in F\setminus\{i_0\}),\quad
v_j=(k-2)/b\ (j\in B).
\]
Then \(\sum_jv_j=0\) and \(\|v\|_\infty=1\) (because \(k-2\le b\)). For sufficiently small \(t>0\), \(x+tv\) remains in the same strict active region; its first free output changes by \(t(2-2/k)\). Thus the upper bound is attained by \(x\) and \(x+tv\). For \(N=2\), choose two distinct feasible points near the constant interior vector \((s/2,s/2)\); projection acts as the identity and the constant is one.

An explicit four-cell example with \(s=2\) is
\[
x=(23/30,23/30,23/30,-3/10),\quad v=(1,-1,-1,1).
\]
For all sufficiently small positive \(t\),
\[
Q_2(x)=(2/3,2/3,2/3,0),\qquad
Q_2(x+tv)=(2/3+4t/3,2/3-2t/3,2/3-2t/3,0),
\]
so the output-to-input maximum-norm perturbation ratio is exactly \(4/3\).

## Verification

The standalone standard-library Python script `verify_limiter.py` verifies the active-region constants against exact rational enumeration of the vertices of \(H_0\cap[-1,1]^N\) for \(2\le N\le10\), checks explicit sharpness witnesses for three different interior masses in each \(3\le N\le32\), and tests random projected pairs using an independently implemented water-level bisection solver. It reports 2,528 successful checks. The finite computations supplement, but do not replace, the all-dimension proof above.

## Relationship to prior work

Lee, Lee and Liu (2026), arXiv:2610.33449v1, identify the conservation-and-bounds cell-average limiter as a metric projection and prove its \(L^2\)-nonexpansiveness. Their Section 3 does not supply an exact \(\ell_\infty\) pairwise modulus on fixed-mass input hyperplanes; Euclidean nonexpansiveness alone does not imply such a modulus. Wang and Lu (2015), arXiv:1503.01002v1, give the capped-simplex projection and its KKT active-set algorithm. The active-set formula is prior knowledge; the sharp restriction-sensitive supnorm optimization and its mass-uniform dimension frontier are the claimed additional result. Gomez, Wang and Tang (2026), arXiv:2602.23336v1, study hypersimplex projections and Euclidean Lipschitz/differentiability in classification, not this fixed-mass supnorm constant. Amos, Koltun and Kolter (2019), arXiv:1906.08707v3, use an entropy-regularized projection onto the same cube-slice feasible set, rather than the Euclidean metric projector or its fixed-mass supnorm sensitivity. Related published sharp-norm results for cross-polytope and polynomial projectors concern different feasible sets and input domains.

## Limitations

The theorem requires equal cell volumes, a common bound interval, Euclidean projection, and exactly equal input total masses. No sharp assertion is made for unequal-volume meshes, different total masses, general \(\ell_p\) norms, or the full high-order DG limiter. This is a pairwise perturbation bound between **possibly infeasible** mass-conserving inputs; it does not disprove separate one-sided estimates relative to a feasible exact solution. A prior general polyhedral-projection sensitivity theorem might imply this special classification; historical priority is not independently certified.

## References

- Seungmin Lee, Sanghyun Lee, Chen Liu, *Optimization-based Cell Average Limiters as Metric Projections: Constrained Evolution and Convergence Analysis for Convection-diffusion Equations*, arXiv:2610.33449v1, first public 2026-10-24. https://arxiv.org/html/2610.33449v1
- Weiran Wang, Canyi Lu, *Projection onto the capped simplex*, arXiv:1503.01002v1, 2015-03-03. https://arxiv.org/html/1503.01002v1
- Camilo Gomez, Pengyang Wang, Liansheng Tang, *Differentiable Zero-One Loss via Hypersimplex Projections*, arXiv:2602.23336v1, 2026-02-26. https://arxiv.org/html/2602.23336v1
- Brandon Amos, Vladlen Koltun, J. Zico Kolter, *The Limited Multi-Label Projection Layer*, arXiv:1906.08707v3 (first public 2019-06-20). https://arxiv.org/html/1906.08707v3
