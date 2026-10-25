# Sharp backward-Euler positivity on arbitrary graded Dirichlet interval meshes

## Finding
For every integer \(n\ge3\), every positive mesh-length vector \(h_1,\ldots,h_{n+1}\), and every time step \(\tau\ge0\), the consistent-mass linear finite-element backward-Euler update for the one-dimensional unit-diffusivity heat equation with homogeneous Dirichlet boundaries satisfies
\[
P_\tau=(M+\tau K)^{-1}M\ge0\quad\Longleftrightarrow\quad
\tau=0\quad\text{or}\quad\tau\ge\tau_*,
\qquad \tau_*:=\frac16\max_{2\le j\le n}h_j^2.
\]
The matrix inequality means entrywise nonnegativity, not a positive-semidefinite comparison. For every strictly positive \(\tau<\tau_*\), at least one entry connecting nodes at index distance two is negative. Moreover, every entry \( (P_\tau)_{i,i+1}\) and \((P_\tau)_{i+1,i}\) is strictly positive for \(\tau>0\). The two endpoint-adjacent element lengths do not enter \(\tau_*\).

For one or two interior degrees of freedom, by contrast, the update is entrywise nonnegative at every \(\tau\ge0\). Thus three interior nodes are the minimal order for a nontrivial positive-step barrier in this Dirichlet family.

## Assumptions and scope
Fix strictly increasing nodes \(x_0<\cdots<x_{n+1}\), with \(h_j=x_j-x_{j-1}>0\). The unknowns are the coefficients of continuous \(P_1\) hat functions attached to interior nodes \(x_1,\ldots,x_n\). The diffusivity is the constant \(1\), the source and Dirichlet endpoint data are zero, and the consistent (not mass-lumped) mass matrix is used. For \(1\le i\le n\), put
\[
M_{ii}=\frac{h_i+h_{i+1}}3,\quad K_{ii}=\frac1{h_i}+\frac1{h_{i+1}},
\qquad M_{i,i+1}=\frac{h_{i+1}}6,\quad K_{i,i+1}=-\frac1{h_{i+1}}.
\]
Their remaining off-diagonal entries are zero, and both matrices are symmetric. The statement concerns the homogeneous one-step mapping of nonnegative interior nodal values to nonnegative interior nodal values; it makes no assertion about nonhomogeneous boundary or forcing data or about an arbitrary higher-dimensional triangulation.

## Proof
**Step 1: strict tridiagonal dominance.** Let \(A=M+\tau K\), \(d_i=A_{ii}\) and \(c_i=A_{i,i+1}=h_{i+1}/6-\tau/h_{i+1}\). The matrix \(A\) is positive definite since \(M\) is positive definite and \(K\) is positive definite under homogeneous Dirichlet conditions. It is also strictly diagonally dominant in absolute value. Indeed, for every cell length \(h>0\),
\[
\frac h3+\frac{\tau}h-\left|\frac h6-\frac{\tau}h\right|>0.
\]
Summing the contributions from the cells meeting each interior node proves \(d_i>|c_{i-1}|+|c_i|\), with out-of-range \(c\) taken as zero. Consequently all leading principal determinants \(\Delta_i=\det A_{[1:i],[1:i]}\) are positive, with \(\Delta_0=1\). The backward elimination pivots \(\gamma_i=d_i-c_i^2/\gamma_{i+1}\), \(\gamma_n=d_n\), satisfy \(\gamma_i>|c_{i-1}|\): this follows by descending induction from strict diagonal dominance.

**Step 2: nearest-neighbor update entries never vanish.** Fix adjacent interior indices \(i,j=i+1\), and solve \(Au=Me_j\). Eliminate all nodes left of \(i\) and all nodes right of \(j+1\), then eliminate \(j+1\). Write \(a=h_{i+1}\), \(b=h_{i+2}\), \(c=c_i=a/6-\tau/a\), \(e=c_{i+1}=b/6-\tau/b\) when \(j<n\). At \(j=n\), set \(e=0\) and interpret \(e/\gamma=0\). The right-side Schur pivot \(\gamma\) for node \(j+1\) satisfies \(\gamma>|e|\); the final \(2\times2\) Schur complement is positive definite. Therefore \(u_i\) has the sign of
\[
\begin{aligned}
N&=\frac a6\left(d_j-\frac{e^2}{\gamma}\right)
-c\left(\frac{a+b}3-\frac{e}{\gamma}\frac b6\right)\\
&=\tau\left[\frac12+\frac{a}{6b}+\frac{b}{3a}
+\frac e\gamma\left(\frac{a}{6b}-\frac{b}{6a}\right)\right]>0.
\end{aligned}
\]
The last inequality follows from \(|e/\gamma|<1\): the expression in brackets is greater than or equal to \(1/2+a/(6b)+b/(3a)-|a/(6b)-b/(6a)|>0\). Hence \((P_\tau)_{i,i+1}>0\) for every \(\tau>0\). Reversing the order of the mesh proves \((P_\tau)_{i+1,i}>0\). This computation also covers an end pair, since the missing outside matrix off-diagonal is zero.

**Step 3: negative witnesses below the threshold.** The standard tridiagonal inverse formula gives, for \(k\ge i+1\),
\[
(A^{-1})_{i,k}=-c_i\frac{\Delta_{i-1}}{\Delta_i}(A^{-1})_{i+1,k}.
\]
Since column \(i+2\) of \(M\) has support only in rows \(i+1,i+2,i+3\), the same relation yields
\[
(P_\tau)_{i,i+2}=-c_i\frac{\Delta_{i-1}}{\Delta_i}(P_\tau)_{i+1,i+2},
\qquad 1\le i\le n-2.
\]
Thus \(c_i>0\) implies \((P_\tau)_{i,i+2}<0\) by Step 2. For the final edge \(c_{n-1}>0\), the reflected identity gives \((P_\tau)_{n,n-2}=-c_{n-1}(P_\tau)_{n-1,n-2}/d_n<0\). Hence entrywise nonnegativity for any positive \(\tau\) forces every \(c_i\le0\), which is precisely \(\tau\ge\tau_*\).

**Step 4: sufficiency and low orders.** If \(\tau\ge\tau_*\), every off-diagonal of \(A\) is nonpositive. As a positive-definite Stieltjes matrix, \(A\) has an entrywise nonnegative inverse. Since \(M\ge0\), it follows that \(P_\tau=A^{-1}M\ge0\). At \(\tau=0\), the update is the identity. When \(n=1\), the update is a positive scalar. For \(n=2\), direct inversion gives positive off-diagonal entries \((P_\tau)_{12},(P_\tau)_{21}\) for \(\tau>0\) and positive diagonal entries (by positive definiteness of \(A\) and the two-by-two formulas); hence no positive lower-step barrier exists.

## Verification
The standalone script `verify_graded_mesh.py` assembles \(M,K\) from arbitrary exact rational cell lengths, solves the update equations using rational Gaussian elimination, and checks nonnegative/negative signs without floating-point tolerances. It passed **618** exact tests for \(n=3,\ldots,8\), covering independently sampled graded meshes, time steps below, at and above the proposed threshold, and all adjacent-entry positivity checks. The infinite-parameter theorem relies on Steps 1–4, not on finite enumeration. To reproduce, run `python verify_graded_mesh.py` using Python's standard library.

## Relationship to prior work
Li and Huang's 2012 preprint (arXiv:1209.5657), Theorem 3.1, gives a sufficient mesh-dependent lower time-step bound for maximum-principle preservation in arbitrary dimensions. Schatz, Thomée and Wahlbin (2010), Theorem 5.7, give the sufficient Stieltjes-matrix criterion for fully discrete finite elements. On an interval, their criterion specializes to \(\tau\ge\max h_j^2/6\) for interior-to-interior cells. The new part is necessity for every individual graded Dirichlet mesh with at least three interior nodes, proved by strictly positive nearest-neighbor entries and explicit two-step negative witnesses. The low-order exception and the irrelevance of boundary cell lengths are also established here. Thomée and Wahlbin (2008) address semidiscrete and lumped-mass positivity questions; full-text comparison was unavailable, so possible further related results remain a literature risk. Previously available periodic-grid special cases are not used to infer necessity for nonuniform Dirichlet grids.

## Limitations
The claim is one-dimensional, uses constant diffusivity and continuous piecewise-linear consistent-mass finite elements, and concerns one backward-Euler step with homogeneous data. It does not imply a maximum principle for nonzero boundary or source terms, other temporal schemes, or general multidimensional meshes. Publication novelty has not been independently certified; one historically relevant full text was inaccessible. The provided finite tests do not replace the proof or establish originality.

## References
- X. Li and W. Huang, *Maximum principle for the finite element solution of time dependent anisotropic diffusion problems*, arXiv:1209.5657, initially public September 25, 2012; Theorem 3.1 and Section 5. https://arxiv.org/abs/1209.5657
- A. H. Schatz, V. Thomée and L. B. Wahlbin, *On Positivity and Maximum-Norm Contractivity in Time Stepping Methods for Parabolic Equations*, Comput. Methods Appl. Math. 10 (2010), 421–443, Theorems 5.5 and 5.7. https://doi.org/10.2478/cmam-2010-0025
- V. Thomée and L. B. Wahlbin, *On the existence of maximum principles in parabolic finite element equations*, Math. Comp. 77 (2008), 11–19. https://doi.org/10.1090/S0025-5718-07-02021-2
