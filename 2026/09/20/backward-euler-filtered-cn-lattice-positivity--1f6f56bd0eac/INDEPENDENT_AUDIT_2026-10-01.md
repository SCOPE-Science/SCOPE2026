# Independent mathematical audit — SCOPE-20260920-1f6f56bd0eac

Audited at: 2026-10-01T18:05:11.787582Z

Disposition: **passed**

## Correctness — PASS

The lattice resolvent solves a second-order recurrence with decaying root \(q\), giving \(r_j=((1-q)/(1+q))q^{|j|}\). Direct convolution yields \(2(r*r)_j-r_j=q^{|j|}(1-q)^2(2|j|(1+q)+1-q)/(1+q)^3>0\), proving unconditional positivity and mass conservation of \(C_sR_s\). Absolute summability justifies periodization to finite cycles, and commutativity gives \(C_s^kR_s^m=(C_sR_s)^kR_s^{m-k}\) for \(m\ge k\). The displayed two-point Dirichlet matrices are exact and show the boundary-sensitive failure. The numerical script independently reproduces these identities.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify_lattice_positivity.py
- Higueras-Roldan arXiv:2301.01066

### Correctness risks

- The theorem is specific to the uniform one-dimensional nearest-neighbor lattice and periodic cycles.

## Originality — PASS

The classical and modern literature inspected covers Crank-Nicolson positivity bounds, Rannacher/backward-Euler smoothing, and positivity-preserving Padé smoothing. None of the material read states the exact all-step-ratio positive convolution kernel for the composite \(C_sR_s\), its \(m\ge k\) consequence, and the paired Dirichlet obstruction. Resultary did not expose a prior SCOPE theorem with this exact composite.

### Equivalent formulations

The inspected statements are not equivalent to positivity of the specific rational composite \((I-sL)(I+sL)^{-2}\) on the translation-invariant lattice.

### Broader coverage

Their broader numerical-analysis scope does not imply the exact lattice Green-kernel positivity theorem.

### Exact database or table

This is an analytic kernel identity, not a tabulated quantity.

### Claim versus prior implication

The proof uses a genuinely spatial convolution cancellation not supplied by the prior scalar/smoothing statements.

### Sources inspected

- A new insight on positivity and contractivity of the Crank-Nicolson scheme for the heat equation — https://arxiv.org/abs/2301.01066. NOT_COVERING: The paper analyzes CN itself under Dirichlet boundaries, not a backward-Euler-filtered composite on the infinite or periodic lattice.
- Smoothing with positivity-preserving Padé schemes for parabolic problems with nonsmooth data — https://doi.org/10.1002/num.20039. PLAUSIBLE_BUT_NOT_DECISIVE: The accessible statement does not identify the audited composite or kernel; incomplete full-text access is retained as a risk.

### Checked sources

- https://arxiv.org/abs/2301.01066
- https://doi.org/10.1002/num.20039
- Resultary semantic search
- web searches for Rannacher/backward-Euler positivity

### Residual risks

- Several older smoothing papers were not available in complete theorem-level text in this run, so an older equivalent specialization cannot be excluded absolutely.

## Value — PASS

The result isolates an exact and counterintuitive positivity mechanism for a canonical heat lattice, gives a closed positive Green kernel and a reusable \(m\ge k\) certificate, and sharply demonstrates that the phenomenon fails under Dirichlet boundaries. That is a motivated structural numerical-analysis fact.

### Value sources

- Higueras-Roldan arXiv:2301.01066
- assigned RESULT.md

### Value risks

- It does not extend to arbitrary diffusion matrices or prove an optimal startup length.

## Limitations

- Restricted to the standard one-dimensional nearest-neighbor infinite or periodic lattice.
- The condition \(m\ge k\) is sufficient, not necessary.
- Older smoothing literature was not fully inspectable theorem by theorem in this run.
