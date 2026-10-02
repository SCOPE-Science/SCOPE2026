# Independent scientific audit — 2026-10-01

**Disposition:** passed

**Final claim:** If a binary \(t\)-PIR encoder maps \(\mathbb F_2^k\) bijectively onto a linear \([n,k]\) associated code with redundancy \(r=n-k\), then each inverse-label coordinate factors through a quotient of dimension at most \(\lfloor r/(t-1)\rfloor\). Hence for \(r\le3t-4\) the labeling is affine and the same recovery sets yield a linear \(t\)-PIR encoder; in particular any binary 3-PIR code of length 11 and size \(2^7\), if it exists, must have a genuinely nonlinear associated code.

## C — PASS

For a fixed requested bit, each recovery set with column span \(W_s\) makes the inverse-label coordinate constant on cosets of \(W_s^\perp\), hence on the sum of these orthogonal complements. The quotient dimension is \(\dim(\cap_s W_s)\). Modding out the common intersection and using disjointness of the recovery sets gives \((t-1)d_j\le n-k=r\). When \(r\le3t-4\), every coordinate therefore factors through at most two binary variables. Because the inverse labeling is a permutation, every coordinate is balanced; every balanced Boolean function on a space of dimension at most two is affine. Thus the whole permutation is affine with invertible linear part and can be converted to a linear encoder without changing recovery sets except fixed output complements. The \((11,7)\) consequence then follows from the standard linear 3-PIR redundancy bound \(\binom r2\ge k\).

Residual risk: The threshold is only sufficient. For quotient dimension three, balanced nonlinear Boolean functions exist, so this argument stops exactly where claimed.

## O — PASS

The full arXiv text of Hollmann–Luhaäär explicitly distinguishes two nonlinear mechanisms—nonlinear associated code versus nonlinear encoder onto a linear code—and states the length-11, size-\(2^7\) existence problem, but it does not prove that low redundancy forces the second mechanism to be affine. It only proves special no-encoder results for Hamming codes and parameter bounds. A Resultary search found no earlier SCOPE theorem equivalent to the quotient-dimension/affine-linearization result.

Residual risk: Equivalent results may exist under Boolean-function factorization or batch-code terminology not surfaced by the searches.

### Equivalent formulations

**Searches:** Resultary: nonlinear 3-PIR code linear associated code nonlinear labeling affine low redundancy; Hollmann–Luhaäär, arXiv:2208.14552 full text

**Evidence:** The primary paper explicitly notes both sources of nonlinearity but supplies no general affine-linearization theorem. Its special Hamming-code theorem is about a specific linear code family, not redundancy \(r\) alone.

**Reasoning:** No inspected source states an equivalent quotient-dimension result.

### Broader coverage

**Searches:** Hollmann–Luhaäär sections 1, 5–7; Rao–Vardy arXiv:1605.01869; Kurz–Yaakobi DOI 10.1007/s10623-020-00828-6

**Evidence:** Hollmann–Luhaäär treats nonlinear codes more broadly but only obtains special parameter results. Rao–Vardy supplies a linear redundancy lower bound, not nonlinear-on-linear reduction.

**Reasoning:** The prior works are broader in general PIR context but do not dominate the final structural theorem.

### Exact database or table

**Searches:** Hollmann–Luhaäär tables of optimal small-size PIR lengths; Brouwer general binary code table cited there

**Evidence:** The tables concern attainable code parameters and minimum distance, not whether a nonlinear labeling of a fixed linear associated code can be affine-linearized.

**Reasoning:** Tabulated small-code data does not imply the general \(r\le3t-4\) theorem.

### Claim versus prior implication

**Searches:** Hollmann–Luhaäär statement that a length-11 size-\(2^7\) code is necessarily nonlinear; Linear 3-PIR redundancy bound

**Evidence:** “Necessarily nonlinear” in the primary paper explicitly allows either a nonlinear associated code or a nonlinear encoder onto a linear associated code. The audited theorem rules out the latter mechanism at \(r=4,t=3\).

**Reasoning:** The prior open-problem statement does not imply the stronger associated-code conclusion; the quotient theorem is needed.

### Source inspections

- **Optimal possibly nonlinear 3-PIR codes of small size** (arXiv:2208.14552): PARTIAL_COVERAGE. Trigger: Direct source motivating nonlinear labeling versus nonlinear associated codes. Material read: Full arXiv HTML including introduction, preliminaries, small-size results, open problem, and conclusions. Method: Full-text primary-source inspection. Evidence: It identifies the two nonlinear mechanisms and the \((11,7)\) open case but does not contain the audited low-redundancy affine theorem.
- **Lower Bound on the Redundancy of PIR Codes** (arXiv:1605.01869): FOUNDATIONAL_PRIOR_ART. Trigger: Source of the linear 3-PIR redundancy obstruction used in the application. Material read: The linear redundancy result as cited and applied in the package and primary PIR paper. Method: Primary/background source inspection. Evidence: It supplies the linear bound, not the nonlinear-labeling reduction.

### Residual risks

- A theorem in Boolean-function or batch-code language may encode the same low-dimensional quotient argument without using PIR-labeling terminology.

## V — PASS

The theorem answers a natural structural ambiguity emphasized by the primary PIR source: in a broad low-redundancy regime, nonlinear labeling of a linear code cannot create extra PIR power. It also strengthens the documented open \((n,k)=(11,7)\) case from “necessarily nonlinear” to “the associated code itself must be nonlinear.”

Residual risk: It does not settle whether the open \((11,7)\) code exists and makes no optimality claim for the threshold.

## Overall disposition

**PASSED**
