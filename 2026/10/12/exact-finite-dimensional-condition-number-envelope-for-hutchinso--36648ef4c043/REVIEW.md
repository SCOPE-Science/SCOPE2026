# Self-review

## Correctness
PASS. The exact Rademacher variance formula reduces orientation dependence to the squared diagonal. Cauchy--Schwarz supplies the sharp lower bound \(\sum_i a_{ii}^2\ge \operatorname{tr}(A)^2/n\), and real Schur--Horn supplies equality for any prescribed spectrum. The remaining spectral ratio is coordinatewise endpoint-maximized because each one-variable slice has only an interior minimum. The resulting integer objective is unimodal with continuous maximizer \(n/(\kappa+1)\), proving the floor/ceiling law. The independent-probe factor \(1/m\) is immediate. Exact replay verifies representative rational cases and the equality witness.

## Originality
PASS, with explicit residual risk. Classical and modern trace-estimation literature gives the variance identity, general sample-complexity bounds, matrix-dependent off-diagonal-energy bounds, and later stable-rank/tail estimates. The closest inspected archive source, Roosta-Khorasani--Ascher, defines a columnwise off-diagonal-energy parameter and proves sufficient sample bounds, but does not state the exact condition-number-only finite-dimensional variance envelope, the two-adjacent-integers multiplicity law, or Schur--Horn attainability. Focused published-finding corpus and web searches for condition-number, relative-variance, Schur--Horn, endpoint-spectrum, and equivalent formulations found no implication-equivalent result. The simple continuous \((\kappa-1)^2/(2\kappa n)\) corollary is recognized as Kantorovich-type prior structure and is not the novelty claim.

## Value
PASS. Condition number is routinely available or targeted by preconditioning, while Hutchinson variance is basis- and matrix-structure dependent. The theorem gives the exact worst uncertainty compatible with only \((n,\kappa)\), identifies the extremal spectrum and orientation, and quantifies the finite-dimensional gap left by continuous bounded-ratio inequalities. It is a natural complete extremal classification rather than an arbitrary numerical slice.

## Closest literature and limitations
Hutchinson supplies the estimator and variance analysis; Avron--Toledo and Roosta-Khorasani--Ascher analyze probabilistic sample complexity and matrix-dependent behavior; later stable-rank work sharpens tail bounds. The principal residual risk is that an older inequality on bounded finite samples or coefficient of variation may encode the same spectral endpoint optimization without trace-estimation terminology. The claim is therefore limited to the exact finite-\(n\) Hutchinson formulation and does not claim novelty for the underlying continuous Kantorovich-type scalar inequality.

Self-review: passed. Independent audit: not yet performed.
