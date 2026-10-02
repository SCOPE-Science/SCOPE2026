# Independent scientific audit — SCOPE-20260919-71dd3abf0659

Audited at: 2026-10-01T17:15:19.026518Z

Disposition: **passed**

## Correctness — PASS

After normalizing the complete pivot to one, write \(A=\begin{bmatrix}1&c^\top\\ r&X\end{bmatrix}\). The residual block is \(X-rc^\top\). With \(R=\|r\|_2\), \(C=\|c\|_2\), \(x=\|X\|_F\), and \(B=1+R^2+C^2\), the exact identity \((1+R^2C^2/B)(B+x^2)-(x+RC)^2=(B-xRC)^2/B\) gives the sharp scalar bound; complete pivoting gives \(R^2\le n-1\) and \(C^2\le m-1\). The square family in the package makes both inequalities asymptotically equal and has a unique largest pivot for \(N\ge4\) when the parameter is sufficiently close to one. The general norm-change identity and the PSD Schur-complement monotonicity statement also check directly. The numerical artifact reproduces the sharp family but is not used as proof.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify_aca_frobenius_growth.py
- assigned artifacts/verification_output.txt
- https://arxiv.org/abs/2609.17947

### Correctness risks

- The theorem is exact-arithmetic and one-step only; it does not bound a multi-step product or floating-point growth.
- Full text of the closest ACA preprint could not be verified in this run, so comparison beyond its public theorem-level description remains a literature-access risk.

## Originality — PASS

The fresh Resultary and web searches found the assigned record as the only exact match. The closest primary ACA paper studies exterior-algebra geometry, \(\sigma_{k+1}\)-type error control, PSD quasi-optimality, and an angle-based rank-one update bound; the material available for inspection does not state the dimension-only sharp factor \(\sqrt{nm/(n+m-1)}\) or the unique-pivot extremal family. Classical Gaussian-elimination complete-pivot literature measures max-entry growth, not this one-step Frobenius residual ratio.

### Equivalent formulations

No equivalent formulation or implication was located under ACA, Schur-complement, or complete-pivot growth terminology.

### Broader coverage

Neither inspected framework mechanically implies the stated sharp Frobenius one-step factor.

### Exact database or table

This is not a known-table computation; absence of an exact hit is supporting evidence only.

### Claim versus prior implication

The scalar optimization and sharp unique-pivot family supply an additional implication not found in the inspected prior results.

### Sources inspected

- A Geometric View of Adaptive Cross Approximation via Exterior Algebra — https://arxiv.org/abs/2609.17947. PARTIAL_ACCESS_NOT_DECISIVE: The available material describes geometric, singular-value, PSD, and angle-based bounds but not the audited sharp dimension-only ratio.
- A new upper bound for the growth factor in Gaussian elimination with complete pivoting — https://doi.org/10.1112/blms.70034. NOT_COVERING: It studies max-entry growth over elimination, not one-step Frobenius residual amplification.

### Checked sources

- https://arxiv.org/abs/2609.17947
- https://doi.org/10.1112/blms.70034
- Resultary semantic search

### Residual risks

- A normwise Schur-complement extremum may exist in older numerical-linear-algebra literature under terminology not surfaced by the searches.
- Full text of arXiv:2609.17947 was not verifiable in this run.

## Value — PASS

The sharp \(\Theta(\sqrt N)\) one-step Frobenius amplification under a unique complete pivot is a motivated boundary for greedy ACA: it quantifies a concrete instability mechanism while contrasting it with monotone PSD diagonal pivoting. It is a natural exact local invariant of the algorithm rather than an arbitrary matrix example.

### Value sources

- https://arxiv.org/abs/2609.17947
- assigned RESULT.md

### Value risks

- The value is local to one exact-arithmetic step and should not be read as a sharp end-to-end ACA error theorem.

## Limitations

- The theorem is a one-step exact-arithmetic result.
- The sharp family is adversarial and does not establish typical application-matrix behavior.
- No sharp multi-step product or floating-point stability theorem is claimed.
