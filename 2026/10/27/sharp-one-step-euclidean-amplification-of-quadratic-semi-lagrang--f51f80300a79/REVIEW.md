# Scientific review

## Correctness — PASS

The result specifies the exact periodic nodal quadratic operator, the unweighted Euclidean norm, all \(N\ge2\) and all signed displacements. Even–odd block Fourier decomposition is unitary. An independent algebraic expansion of the symbol gives the exact squared-singular-value sum \(F(z)\) and product \(D(z)\), with \(z=(1-\operatorname{Re}q)/2\). At zero frequency the largest squared singular value is \(X(u)\). For noninteger displacement, the strict polynomial comparison \(P_z(X)=uz[(2+u)-2(1-u)X]>0\), together with \(X\ge F(z)/2\), eliminates every nonzero frequency. The derivative \(X'(u)>0\) establishes the sharp half-step boundary. Grid shifts and reflection give all real displacements. The rational positive equality witness is exact; finite checker experiments are corroborative, not an infinite proof. A scope warning separates the nodal norm from a finite-element mass norm.

## Originality — PASS, with a disclosed historical-access risk

The recent Ferretti–Mehrenberger paper supplies the same block-circulant operator and proves uniform power stability via eigenvalues and eigenvectors, not this sharp one-step **singular-value norm**. Its Section 3 was inspected through the full lawful open HTML version. Ferretti–Mehrenberger (2020) establishes stability for odd-degree symmetric interpolation instead. The classical eigenvalue-bound study by Ferretti–Perrone (2007) treats the same quadratic finite-element subject, but its indexed abstract emphasizes eigenvalues and is not sufficiently detailed to exclude an equivalent one-step norm theorem; full text remained inaccessible. Hence novelty is assessed on the accessible implications and record comparisons, with this explicit nonzero residual priority risk; lack of hits by itself is not proof of novelty. Published mathematical-record comparisons include two-periodic scalar recurrence norms, a simplex least-squares projector norm, and cyclic convolution norms, none of which dominates or specializes to the full quadratic semi-Lagrangian matrix norm claim.

## Mathematical value — PASS

The theorem determines the **exact** mesh-independent one-step stability budget for a natural high-order advection method, identifies a unique displacement class and zero-frequency singular mechanism, and exhibits a strictly positive state suffering \(25\%\) instantaneous squared-norm growth. Standard spectral stability and uniform power bounds do not yield this optimal transient constant. This supplies a meaningful stability diagnostic and a precise separation between nodal one-step amplification and asymptotic power stability, not an arbitrary parameter slice or a routine numerical recomputation.

## Limits and closest prior literature

The technical ingredients of cellwise Lagrange interpolation, Fourier block diagonalization and two-by-two singular-value formulas are classical and not claimed as original. The strongest direct prior study is Ferretti–Mehrenberger, arXiv:2610.19806v1 (2026-10-14); the older plausible P2 study is Ferretti–Perrone (2007, institutional abstract only); the related odd-degree theorem is Ferretti–Mehrenberger, Math. Comp. 89 (2020). Independent historical audit and broader expert review have not been performed.

Self-review: passed. Independent audit: not yet performed.
