# Scientific review: sharp Gaussian fluctuations of the intrinsic-volume index

## Correctness — PASS
The geometric cone and Gaussian face-count random variable are identified exactly by projection KKT conditions. The threshold is uniquely specified and its normal-tail asymptotics are explicit. A two-dimensional triangular-array Lyapunov argument gives covariance matrix \(\begin{psmallmatrix}1&1\\1&2\end{psmallmatrix}\). Monotone bracketing of the self-consistent threshold, plus a locally uniform empirical tail-count estimate, yields an explicit normal limit of variance \(2\) at scale \(t_m\). Universal conic variance and exponential-moment inequalities from McCoy–Tropp, read at their theorem statements, justify uniform integrability and hence the exact leading variance \(4\log m\). The independent finite verifier checks the KKT count representation, threshold identities and finite instances, not the infinite limit.

## Originality — PASS, with residual historical risk
McCoy–Tropp (2013, Theorems 4.5 and 4.8) provide the universal variance and moment bounds, but not a logarithmic normal limit for simplex vertex cones. Goldstein–Nourdin–Peccati (2014, Theorem 1.1 and Table 1) obtain general normal approximation for conic indices using their *unknown* intrinsic-volume means and variances; their examples are orthants, circular cones, positive-semidefinite cones and Weyl chambers, not this cone family. Kabluchko–Seidel (2020, Theorem 2.4) give explicit finite-dimensional cone volumes and related geometry without the present explicit centered/scaled CLT and saturation law. Existing first-order logarithmic localization, when available, is insufficient to infer a Gaussian limit or the variance coefficient. The source and alias searches did not identify a stronger covering claim; this is not a proof of absolute novelty, and a hidden equivalent asymptotic remains a risk.

## Value — PASS
The theorem supplies an explicit Gaussian fluctuation scale for the intrinsic-volume profile of a natural geometrically defined regular-simplex cone family and shows that this noncircular family sharply saturates the optimal universal conic variance bound. These are quantitative structural additions to both exact finite formulas and general concentration bounds, with implications for widths of conic Crofton phase transitions. The result is not an arbitrary finite slice, a computational table, or only a reformulation of a general CLT.

## Scope and limitations
Only the indicated regular-simplex vertex cones are addressed. Neither a Berry–Esseen rate nor a local limit theorem is claimed, and an earlier equivalent specialization might exist. The finite verifier supplements but does not establish the analytic proof.

Same-model review: passed. Independent audit: not yet performed.
