# Independent audit — Single commutators and trace rigidity in norm reduced products of finite von Neumann algebras

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/18/single-commutators-trace-rigidity-norm-reduced-products--66c3e3c26339`  
**Audited tree:** `27ce6e55fd0020c10f3a862e819a5167524ff0be`

## Disposition

**PASSED.** All three required axes pass. Publication may remain in the validated record set.

## Correctness

**PASS.** The quotient argument is correct. If a class lies in ker(Tbar), subtracting the coordinate center-valued traces changes the representative by a norm-null sequence and yields exact trace-zero coordinates. Wang's uniform finite-von-Neumann single-commutator theorem then gives coordinate commutators with a universal product bound; reciprocal rescaling makes both factor sequences bounded. Conversely center-valued traces kill commutators. Contractivity and the central splitting give the isometric quotient, and every tracial state factors through Tbar because it vanishes on the single-commutator kernel.

## Originality

**PASS.** Wang's 2026 result is a coordinate theorem for finite von Neumann algebras. Hardy's pseudomatricial work already gives unique trace and a self-adjoint self-commutator characterization in matrix ultraproduct/model-theoretic settings. Targeted searches did not locate the exact operator-norm reduced-product statement that all trace-zero elements, without self-adjointness, form the set of single additive commutators with one universal bound, nor the resulting trace-space identification for arbitrary finite centers.

## Scientific Value

**PASS.** The result converts a new uniform coordinate theorem into a clean structural classification for C*-norm reduced products, which need not be von Neumann algebras. Closed linearity of the set of single commutators and the full tracial-state parametrization are useful consequences not automatic in general C*-ultraproducts.

## Independent checks

- Verified Tbar is well defined and contractive because each normalized center-valued trace is unital positive and norm one.
- Checked that a_n=x_n-T_n(x_n) represents the same quotient class and limsup ||a_n|| equals the quotient norm after choosing a representative realizing the limsup.
- Checked reciprocal rescaling of each nonzero commutator pair yields two bounded coordinate sequences with norms bounded by sqrt(K||a_n||).
- Verified dist(x,ker Tbar)=||Tbar(x)|| using both contractivity and x-Tbar(x) in the kernel.
- Verified that the scalar norm ultraproduct of factor centers is canonically C via ultralimit, giving the stated unique trace special case.

## Literature and prior-art boundary

- https://arxiv.org/abs/2609.16932 — Jiaqi Wang (2026), universal single-commutator theorem for center-valued-trace-zero elements of finite von Neumann algebras.
- https://doi.org/10.18130/V38K45 — Stephen Hardy (2016), pseudocompact/pseudomatricial C*-algebras; unique trace and self-adjoint trace-zero self-commutators are prior.
- https://arxiv.org/abs/1307.0111 — Bice and Farah, traces on C*-ultrapowers, illustrating that trace rigidity is not generic.

## Limitations

- The theorem relies essentially on a universal coordinatewise commutator bound and does not extend as stated to arbitrary C*-algebra sequences.
- It concerns operator-norm reduced products, not the usual 2-norm tracial ultraproduct.
- The matrix-factor unique-trace portion substantially overlaps older pseudomatricial trace rigidity; novelty is narrowed to arbitrary elements, the universal single-commutator kernel, and general finite centers.

## Repository identity

The assigned source-tree SHA `27ce6e55fd0020c10f3a862e819a5167524ff0be` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
