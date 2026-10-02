# Independent scientific audit — SCOPE-20260921-348ea42cbf67

Audited at: 2026-10-01T23:13:29.436856Z

Disposition: **passed**

## Correctness — PASS

Expanding \(A=r\sum x_i\log x_i\) and \(B_i=rx_i\sum_j\log x_j\) at a diagonal point cancels the constant and linear terms and factors the quadratic term into the variance form with coefficient \(r/t-(nr^2/2)(\log t)^2\). Since \(t(\log t)^2\) has maximum \(4/e^2\) at \(t=e^{-2}\), the exact transverse-Hessian threshold is \(r=e^2/(2n)\). The displayed one-coordinate factorization at the critical value gives the negative cubic coefficient for \(n\ge3\), while \(n=2\) correctly remains undecided there. The numerical artifact is corroborative only.

### Correctness sources

- assigned RESULT.md
- Coronel--Huancas 2014 full accessible statement
- assigned artifacts/verify_power_exponential_instability.py

### Correctness risks

- The stable side of the local Hessian threshold is not a global validity theorem.

## Originality — PASS

An earlier 2026-09-20 SCOPE record already falsifies Coronel--Huancas Conjecture 3.3 in every \(n\ge2\) using a fixed two-level counterexample family; that consequence is therefore prior and is not credited as new here. However, it does not address the published \(r=1\) Theorem 1.4, does not derive the exact diagonal Hessian boundary \(e^2/(2n)\), and does not identify the critical cubic instability. Searches centered on those sharper statements found the assigned result but no earlier covering theorem.

### Equivalent formulations

The prior counterfamily overlaps one consequence but is not equivalent to the sharp instability boundary or the \(r=1\) theorem refutation.

### Broader coverage

No inspected broader theorem implies the exact local threshold and critical cubic term.

### Exact database or table

The threshold is a derived analytic boundary, not a table value.

### Claim versus prior implication

The surviving sharp local theorem and refutation of the published \(r=1\) all-\(n\) theorem require new calculations and are not mechanical corollaries of the prior counterfamily.

### Sources inspected

- Uniform counterexamples to Coronel--Huancas Conjecture 3.3 — published SCOPE 2026/09/20/coronel-huancas-conjecture-3-3-counterexamples--beb90a3a9bef. PARTIAL_COVERAGE: It owns the dimension-wise falsity of Conjecture 3.3 but not the assigned sharp local boundary, critical cubic, or \(r=1\) theorem refutation.
- The proof of three power-exponential inequalities — https://doi.org/10.1186/1029-242X-2014-509. OPEN_CLAIM_SOURCE: The assigned analysis refutes the all-\(n\) Theorem 1.4 for \(n\ge4\) and sharpens the local parameter picture.

### Checked sources

- Coronel--Huancas 2014
- published SCOPE 2026/09/20/coronel-huancas-conjecture-3-3-counterexamples--beb90a3a9bef
- Matejíčka correction literature
- Resultary semantic search

### Residual risks

- A poorly indexed correction could contain an \(r=1\) counterexample or related expansion, but no concrete source was located.
- The all-dimensional falsity of Conjecture 3.3 itself is prior in the earlier SCOPE record and is explicitly not treated as novel here.

## Value — PASS

The surviving contribution identifies a sharp local phase boundary for a natural published product inequality, refutes a stated theorem at its original parameter \(r=1\) in every dimension \(n\ge4\), and resolves the critical local endpoint for \(n\ge3\). Those are substantive corrections and structural boundary information even though a different counterfamily had already disproved the parameterized conjecture.

### Value sources

- Coronel--Huancas 2014
- published SCOPE 2026/09/20 fixed counterfamily

### Value risks

- The result does not decide global validity below the Hessian threshold or the critical \(n=2\) case.

## Limitations

- The local nonnegative Hessian side does not prove the global inequality.
- The critical case \(n=2,\ r=e^2/4\) remains unresolved.
- The global \(r=1\) cases \(n=2,3\) are not classified.
- The prior 2026-09-20 record already owns the bare all-dimensional falsity of Conjecture 3.3.
