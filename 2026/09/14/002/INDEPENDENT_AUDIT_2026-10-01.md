# Independent mathematical audit — 2026-10-01

## Final claim

For the explicit algebra \(E=k\langle x,y,z\rangle/(x^2,y^2,zx+zy)\), the truncation \(W_4\to W_3\) is surjective, every scheme-theoretic fiber is \(\mathbf P^0\) or \(\mathbf P^1\), and \(W_3\) is singular at the displayed triple point.

## Correctness — PASS

Reconstructing the fiber equations from the three bilinear relations gives the matrix \(M(c)=\begin{pmatrix}c_0&0&0\\0&c_1&0\\c_2&c_2&0\end{pmatrix}\). Its third column is identically zero, so the section \([0:0:1]\) exists over every last factor. For every nonzero projective \(c\), the rank is 1 or 2, hence the scheme fiber cut out by these linear forms is respectively \(\mathbf P^1\) or \(\mathbf P^0\). In the affine chart at the stated point, the Jacobian rank is 2; eliminating the two linear equations gives the ideal \((x_0x_1,y_0x_1,x_1x_2)=(x_1)\cap(x_0,y_0,x_2)\), so a 3-dimensional and a 1-dimensional component meet there and the tangent dimension is 4. These calculations prove the stated surjectivity, connected fibers, and singularity for the explicit algebra.

## Originality — PASS

Exact searches for the relation space and truncation statement found no prior exact theorem. Chirvasitu–Kanda study flat families of truncated point schemes generically, but their published result does not imply the fiber ranks or the singular local decomposition for this special relation space. The published-record semantic search returned this record itself and a distinct Heisenberg-quotient point-scheme calculation, not a covering statement. The nomenclatural identification with a Hwang exceptional-divisor presentation was not independently sourced and is treated only as context, not as originality evidence.

### Equivalent formulations

Rephrasing the claim as a kernel-dimension statement for the last-factor incidence matrix yields the same theorem, but no prior source located states that matrix-specific result.

### Broader coverage

Generic flat-family theory does not force this special fiber classification or the displayed singular local decomposition.

### Exact database or table

The absence of an indexed exact row is only best-knowledge evidence; it is not by itself a novelty proof.

### Claim versus prior implication

The prior theorem does not logically imply that every fiber here is projective space of dimension at most one or that the specified point has the stated component intersection.

## Scientific value — PASS

A complete fiber description and an explicit singularity certificate for a concrete degenerate quadratic algebra are structural facts about its truncated point schemes, not just a numerical spot check. The result identifies a global section, all possible fiber dimensions, and a singular component intersection, making it a reusable boundary example for point-scheme geometry.

## Sources inspected

- **Alex Chirvasitu and Ryo Kanda, Flat families of point schemes for connected graded algebras** — https://arxiv.org/abs/1709.08757. GENERAL_FRAMEWORK_NOT_EXACT_COVERAGE: The paper studies generic families and does not state the explicit relation-space fiber theorem audited here.
- **Published record: connectedness of a Heisenberg-quotient point scheme** — https://github.com/Resultary/2026/tree/main/2026/9/13/SCOPE071. RELATED_DIFFERENT_ALGEBRA: It concerns a different Heisenberg quotient and a different point-scheme incidence calculation.

## Checked evidence

- Assigned RESULT.md and artifacts/verify.py from the exact Git tree.
- Fresh symbolic rank and Jacobian reconstruction independent of the saved verifier.
- Primary generic point-scheme literature and published-record semantic search.

## Residual risks

- The contextual identification with a particular Hwang thesis exceptional-divisor presentation was not independently verified from the thesis; the audited theorem is therefore certified only for the explicit displayed algebra.
- The archived RESULT.md uses a historical output/artifacts path although the actual verifier is at artifacts/verify.py; this does not affect the mathematical reconstruction.

## Disposition

**passed**
