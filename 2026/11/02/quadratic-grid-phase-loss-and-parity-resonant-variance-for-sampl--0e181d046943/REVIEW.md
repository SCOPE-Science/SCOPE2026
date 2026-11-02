# Self-review

## Correctness — PASS

The claim is an exact affine control reduction followed by an explicit cellwise optimization. Integration by parts gives the adjoint-weighted switching function; pointwise and cellwise minimization give the objective gap as a sum of nonnegative local absolute-integral differences. On a cell containing a simple zero, uniform Taylor remainder and a \(2\)-Lipschitz local-loss functional yield the uniform \(O(h^3)\) error from its exact linear crossing value. The periodic squared-distance function has mean \(1/12\), variance \(1/180\), and Fourier coefficients \((-1)^k/(\pi^2 k^2)\); Parseval yields the stated common-shift covariance. The two-switch half-grid offset removes odd modes, giving \(1/2880\) versus \(1/180\). Endpoint alignment and short physical endpoint cells have been accounted for. The packaged rational verifier independently checks illustrative instances; infinite validity comes from the proof rather than numerical enumeration.

## Originality — PASS (qualified)

The source on sampled-data convergence by Bourdin–Trélat establishes convergence but does not contain the phase-resolved objective-gap coefficient or common-shift variance. Aghaee–Hager optimize switching times rather than locking them to a grid. Scarinci–Veliov's higher-order numerical scheme permits within-cell switching and uses a different augmented discretization, so its second-order error bound neither specializes to the sharp \(g(r)\) loss nor dominates the Fourier resonance profile. The closest published qubit grid-phase result concerns cubic **time excess**, an endpoint-constrained quantum system, and one adjustable interior pulse; it does not imply the scalar affine **objective value** law. Targeted semantic search did not identify the combined claim. The local crossing calculation is an elementary component, not an independently claimed novelty. Residual priority risk: generic switching-time quantization or random shifted-grid quadrature literature may contain an equivalent covariance law under other terminology; a search is not a uniqueness proof.

## Value — PASS

Fixed-rate digital control has no freedom to place bang-bang switching times at arbitrary instants. The theorem makes the discretization-induced value loss explicit in the continuous-time switching slopes and fractional switch positions. A single randomized mesh phase restores a universal mean coefficient but not a universal variance coefficient; a two-switch example shows a sharp sixteenfold variance resonance with mesh parity. This provides a concrete sampling-diagnostics benchmark and distinguishes qualitative convergence from leading-order risk. No broad nonlinear or downstream theorem is claimed or needed.

## Limits and publication priority

Only exact zero-order-hold restrictions of the scalar linear-affine free-terminal model are proved. The two-switch parity ratio concerns leading asymptotic variances; it is not an exact finite-m statement. Specialized bang-bang grid-phase literature beyond the material examined could overlap and should be checked independently.

Self-review: passed. Independent audit: not yet performed.
