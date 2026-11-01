# Scientific review: Bergman diameter trace spectral outlier

## Correctness — PASS

The monomial basis gives an exact positive parity-block Gram matrix. A strict weighted Schur bound proves contraction on functions with zero constant coefficient. A concrete two-dimensional minor forces a top eigenvalue above one; the finite-rank coupling bounds the essential spectral edge from above. A weakly null logarithmic-block Weyl sequence gives its matching lower bound. Codimension-one min–max then proves the supercritical eigenvalue is unique and simple. The off-diagonal squared norm and the finite minor give the displayed numerical-free bounds. The standalone standard-library checker passed 8,705 deterministic assertions; this is corroboration, not an infinite proof.

## Originality — PASS, with historical risk

The focal full-text primary source Ghiloufi–Zaway (arXiv:2309.00552, 2023) provides related Fejér–Riesz and Toeplitz estimates but not the specific spectral classification. The inspected Kasuga 2025 paper states and contextualizes weighted Fejér–Riesz inequalities, including Euclidean boundary-distance weights, but does not claim the codimension-one sharp contraction or unique isolated outlier. The closest indexed claims concern logarithmic Bergman Hilbert-matrix essential norms, weighted harmonic line bounds, or circle traces, with different quadratic forms and no implication identified. The Andreev 2012 paper is a genuine residual priority risk because its full text could not be accessed.

## Value — PASS

The theorem distinguishes two geometrically canonical Hilbert-space regimes within the same exact diameter trace: the best contractive constant on vanishing-at-origin functions equals the essential norm, whereas the unrestricted trace has precisely one simple unstable spectral mode. This is a natural sharp spectral-strengthening of trace inequalities, not a finite table recomputation or parameter substitution. The complete outlier geometry supplies a useful benchmark for finer trace-operator stability, even though its isolated eigenvalue is not given in closed form.

## Scope and residual limitations

Results concern the precise normalized \(A^2(\mathbb D)\) norm, weight \(1-|t|\), and symmetric full diameter. The lower and upper bounds are rigorous but not optimal enclosures for the numerical eigenvalue. Historical priority and generalization to other weights remain unverified.

Self-review: passed. Independent audit: not yet performed.
