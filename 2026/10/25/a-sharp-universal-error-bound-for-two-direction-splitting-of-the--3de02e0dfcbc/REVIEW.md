# Review of the sharp two-factor first-exponential-integral bound

## Correctness — PASS

The conclusion reduces by orthogonal tensor diagonalization to covariance of two decreasing exponentials of the *same* uniform random variable. The positive-semidefinite order, strictness and kernel follow from an explicit double-integral identity; Cauchy–Schwarz reduces the exact global spectral-norm bound to a one-variable variance maximization. The derivative numerator has a rigorously proved single positive zero through a third-derivative sign-change chain. This establishes the equality characterization, and the scalar example attains the bound. Exact rational Taylor bounds bracket the maximizing stiffness and error constant; the grid experiment is ancillary. No conclusion requires a finite enumeration to cover a continuum.

## Originality — PASS, with residual priority uncertainty

The closest published construction is Caliari–Cassini, arXiv:2304.02327, Theorem 1 and Sections 3–5, whose full open HTML text was inspected. Its local \(O(h^2)\) tensor factorization is an explicit precursor, but it does not state the dissipative Loewner ordering, the universal optimum \(C_*\), the unique attaining stiffness, or the relative-error degeneration. The Sylvester-based recovery work of Muñoz-Matute–Pardo–Calo (doi:10.1002/nme.6929) and the PHIKS/quadrature papers (arXiv:2210.07667 and arXiv:2211.00696) solve different matrix-function evaluation problems; their abstracts were available but the full texts were not inspected. Targeted mathematical-literature and published-mathematical-record searches did not identify a result implying the sharp constant. General covariance and Laplace-transform theory could conceal an equivalent scalar optimum, so independent publication priority is not certified.

## Mathematical value — PASS

The source's formal fixed-generator splitting estimate alone does not quantify its *stiffness-uniform* error. A sharp dimension-independent absolute operator-norm bound, attainable eigenvalue geometry, positive-semidefinite error sign, and a relative error arbitrarily close to unity give concrete design information for tensor-structured exponential integrators. The exact optimizer is a motivated natural invariant: the maximal worst-case operator action discrepancy of the published two-direction splitting. The result is not claimed as a convergence theorem for arbitrary stiff PDEs or as a method improvement.

## Remaining risks

The self-adjoint hypothesis is essential for the Loewner and operator-norm reduction. The result does not include three-factor or higher-function analogues. Relevant generic probability literature may contain an independently derived maximization of the same uniform-Laplace-transform variance; the related numerical quadrature papers were not fully inspected. Numerical approximation claims are supported by exact-rational enclosures, but no external replication has occurred.

Self-review: passed. Independent audit: not yet performed.
