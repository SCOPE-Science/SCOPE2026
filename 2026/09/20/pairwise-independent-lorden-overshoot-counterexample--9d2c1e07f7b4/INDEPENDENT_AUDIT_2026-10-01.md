# Independent scientific audit — SCOPE-20260920-9d2c1e07f7b4

Audited at: 2026-10-01T20:13:40.771389Z

Disposition: **passed**

## Correctness — PASS

For distinct indices in the finite-field block, \((U+iV,U+jV)\) is uniform on \(\mathbb F_q^2\), so the indicators and hence increments are pairwise independent with the stated two-point marginal. Because \(b=q-1\) and every increment is at least one, crossing occurs within the first \(q\) positions. The cases \(V=0,U=0\), \(V=0,U\ne0\), and \(V\ne0\) exhaust the \(q^2\) outcomes; in the last case the unique large jump is uniformly positioned. Averaging gives \(\mathbb E R_b=3q/2-1+3/(2q)\), and direct marginal moments give the stated Lorden constant and positive gap for primes \(q\ge11\). The exact verifier enumerates the finite-field block for several primes and confirms the formulas.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify_counterexample.py
- Lorden 1970
- https://arxiv.org/abs/2501.18329

### Correctness risks

- The sequence is not claimed to be strictly stationary; the result only refutes the direct substitution of pairwise independence into the classical marginal-only bound.

## Originality — PASS

The classical and later overshoot literature inspected assumes mutual independence, independent nonidentical increments, random environments, or stronger comparison/domination hypotheses for dependent renewals. The recent dependent-renewal paper was inspected in full and does not reduce its assumptions to pairwise independence. Searches for a pairwise-independent Lorden counterexample found no prior bounded two-point construction or the same \(9/8\) asymptotic violation.

### Equivalent formulations

No equivalent first-passage counterexample was located.

### Broader coverage

None of these broader frameworks implies that the classical constant survives pairwise independence; the audited construction shows that it does not.

### Exact database or table

The claim is an explicit counterexample theorem rather than a tabulated quantity.

### Claim versus prior implication

The counterexample is not a corollary of the prior positive results; it exploits exactly the higher-order dependence those results exclude or control.

### Sources inspected

- On Lorden's Inequality and Renewal-Type Processes with Dependent Inter-Renewal Times — https://arxiv.org/abs/2501.18329. NOT_COVERING: It treats dependent renewal-type processes under stronger structural assumptions and does not establish or refute the classical constant under pairwise independence alone.
- On Excess over the Boundary — https://doi.org/10.1214/aoms/1177697092. BACKGROUND: It assumes independent renewal increments and supplies the benchmark constant.

### Checked sources

- https://doi.org/10.1214/aoms/1177697092
- https://doi.org/10.1214/aoap/1177004913
- https://doi.org/10.1016/j.spl.2007.02.013
- https://math-mprf.org/journal/articles/id952/
- https://arxiv.org/abs/2501.18329
- https://doi.org/10.1016/j.jmaa.2021.124982

### Residual risks

- The construction is elementary enough that an older equivalent example may exist under limited-independence terminology, but targeted searches did not locate one.

## Value — PASS

This is a sharp conceptual boundary example for a standard renewal inequality: bounded positive two-point marginals and pairwise independence still permit a fixed asymptotic violation of the classical constant. It isolates higher-order dependence as genuinely visible to first-passage overshoot and is not merely a numerical counterexample.

### Value sources

- Lorden 1970
- https://arxiv.org/abs/2501.18329

### Value risks

- The theorem does not determine the optimal universal constant, if any, under pairwise independence.

## Limitations

- The constructed sequence is pairwise independent and identically distributed in marginal law but is not claimed to be strictly stationary.
- The theorem refutes only the classical marginal-only Lorden constant under pairwise independence.
- Stronger dependence hypotheses may restore useful overshoot bounds.
