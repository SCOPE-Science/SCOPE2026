# Review: finite nonnormality defect for Bernstein–Kantorovich averaging

## Correctness
**PASS.** The definition is the equal-bin classical Bernstein–Kantorovich operator on \(L^2(0,1)\). Polynomial degree filtration yields the complete nonzero spectrum \(\lambda_{n,k}=(n)_k/(n+1)^k\). Direct beta integration and central-binomial convolution give the exact Hilbert–Schmidt norm. An Euler–Maclaurin calculation with a uniformly Gaussian-dominated remainder proves
\[\Delta_n=1/6-5\sqrt\pi/(96\sqrt{n+1})+O(n^{-1}).\]
Strict positivity follows from finite-rank Schur triangularization and the asymmetric real kernel. Exact rational checks and trace-power comparisons reproduce these identities at finite sizes but are not used to infer the infinite limit.

## Originality
**PASS with bibliographic risk.** Full source inspections of Păltănea (2012), Acu–Gonska (2019), and Obie et al. (2023) identify approximation, shape-preservation and \(L^p\)-boundedness results rather than the spectral–singular energy defect. The closest available results on Bernstein collocation and Jacobi Bernstein–Durrmeyer spectral energy concern different operators; in particular, their self-adjoint spectral traces cannot imply the discrepancy for non-self-adjoint equal-bin Kantorovich averaging. Published mathematical-record queries on the operator, Hilbert–Schmidt energy, eigenvalue squares, normality and \(1/6\) found no covering record. Gonska–Heilmann–Raşa (2011) was checked through its publisher abstract and bibliographic context but its full text remained inaccessible, preserving priority risk. Search failure or index partition is not treated as uniqueness proof.

## Value
**PASS.** The squared-Hilbert–Schmidt energy and the squared-eigenvalue sum are independent, natural invariants for a nonnormal finite-rank approximation operator. Their difference is exactly the off-diagonal Schur energy (including leakage from the orthogonal complement of the polynomial range); its nonzero limit distinguishes strong convergence to identity from asymptotic spectral normality. The exact identity for the first invariant and the two-term defect give a reproducible benchmark for spectral approximation of positive averaging kernels. This is not merely a new normalization or an arbitrary finite index slice.

## Remaining limitations
The result does not give individual singular values or the metric distance to the normal operators. It is restricted to the unweighted one-dimensional classical family. A stronger historical statement outside the inspected full texts remains possible, and the 2011 full text could not be retrieved through accessible channels. Independent mathematical and bibliographic assessment has not been performed.

Self-review: passed. Independent audit: not yet performed.
