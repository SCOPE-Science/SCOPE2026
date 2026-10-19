# Scientific review of planar rank-one stabilization thresholds

## Correctness

PASS. For every \(a>0\), \(b\geq0\), and \(\delta\geq0\), the proof shifts by \(\delta I\) and uses the necessary-and-sufficient two-by-two trace/determinant conditions. The rank-one parametrization \(\Delta=uv^{\mathsf T}\) gives exact invariants \(p=v^{\mathsf T}u\), \(q=v^{\mathsf T}Ju\), and \(p^2+q^2=\|\Delta\|_F^2\). Maximal determinant at fixed norm is proved analytically, yielding the exact minimal norm, its complete minimizer geometry, and the exceptional zero-rotation impossibility. The symmetric damping amplitude interval follows directly from determinant and trace. Explicit rank-one families approaching the boundary establish the nonattained strict-margin infima. Independent rational arithmetic checks on 39,823 assertions reproduce critical algebra, but finite checks do not replace the universal proof.

## Originality

PASS under the available evidence, not an assertion of absolute priority. The primary paper by He and Liu (2024, DOI 10.3934/math.2024931, MSC 65F18) establishes robust regional assignment of poles of undamped *second-order* gyroscopic pencils under constrained rank-one feedback, not this full first-order free-direction Frobenius distance and optimal geometry. The 2024 Guglielmi–Sicilia arXiv manuscript 2402.14657 provides a broad rank-adaptive numerical approach for matrix-nearness stabilization but no matching exact rotating two-by-two profile in its accessible full text. The earlier Guglielmi–Lubich SIAM paper (DOI 10.1137/16M1105840) explicitly studies general norm-nearest stabilization under optional maximal-rank constraints, and therefore presents the most substantive conceptual overlap; only its published abstract was accessible. Nothing actually inspected establishes the precise piecewise cost, the nilpotent/oscillatory extremizer transition, and the finite passive overdamping window jointly. The older paper and potential other structured stabilization literature remain material originality risks; a search miss is not proof of uniqueness.

## Value

PASS. Low-rank regional eigenvalue correction is an established numerical matrix-nearness and feedback task. The result supplies a natural sharp two-dimensional benchmark with freely chosen rank-one directions: an exact penalty relative to unrestricted correction, impossibility at zero rotation, a nonnormal defective optimum for weak rotation, and a sharp finite range of effective passive damping. It shows why algorithms optimizing small perturbations can approach a highly sensitive defective boundary and why indiscriminate extra damping can lose stability. The characterization is motivated by the actual achievable spectral margin and Frobenius cost, not by an arbitrary auxiliary invariant; it does not purport to solve high-dimensional, fixed-actuator, nonlinear or gyroscopic-pencil problems.

## Closest literature and limitations

The closest prior sources are He–Liu (2024), Guglielmi–Sicilia (2024), and Guglielmi–Lubich (2017). Standard trace/determinant Hurwitz criteria and rank-one determinant identities are deliberately treated as known. The closed-margin extremizers are not strictly stable. The strict-margin results are infimum statements, and no claim is made about robustness of the defective optimum. The 2017 full text could not be examined; the degree of equivalent coverage in inaccessible literature remains uncertain. The numerical checker covers a finite rational grid, whereas the theorem covers continuous parameter ranges by analytic inequalities.

Self-review: passed. Independent audit: not yet performed.
