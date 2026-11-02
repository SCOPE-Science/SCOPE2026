# Scientific review

## Correctness — PASS

The first-lag coefficient follows exactly by one derivative of the published generating function, not by empirical sign inspection. The identity \(\Psi'/\Psi=-q(s/c)/[c(1+s/c)^2]\) reduces the full positive-parameter domain to a scalar function whose derivative factors as \((x+1)(ax-b)/x^2\). Both endpoint divergences, uniqueness of the minimum, the threshold equality, the two roots, the finite-step sign region, and the square-root opening are proved directly. The positive-SOE error floor follows from monotonicity and is attained as an infimum by explicit positive one-exponential approximations. The inverse-transform sign argument uses established locally integrable kernels. A standalone standard-library checker supplies supplementary numerical checks and verifies an explicit parameter example inside the published sufficient sector hypothesis. Computation is not used to prove infinite claims.

## Originality — PASS with residual priority uncertainty

The principal source Yuan–Zegeling (2026), Sections 2, 4 and 5, provides the Scarpi transform, uncorrected BE-CQ generating series and its fast-history context. Garrappa–Giusti (2023), Sections 3 and 4, derives the same continuous symbol and develops CQ weight computations. These are foundational ingredients, but neither inspected source states the exact three-parameter sign criterion, its unique two-boundary timestep window or the sharp error floor for positive SOEs. The 2021 Scarpi paper already documents failures of complete monotonicity for variable-order derivative kernels, and the 2023 renewal paper considers distinct Bernstein conditions for relaxation solutions: neither is claimed as new. A 2026 approximated-kernels paper is a plausible specialized source whose full text could not be checked; an equivalent earlier result remains possible. Published mathematical-record comparisons returned generic positivity results concerning different schemes and kernels, not a theorem implying the specific classification and SOE bound. Novelty is therefore a best-knowledge assessment, not a uniqueness certificate.

## Value — PASS

The first memory coefficient governs the earliest nonlocal interaction in precisely the CQ construction used by the motivating numerical work. The exact phase diagram is a meaningful parameter/stepsize boundary, not a chosen isolated negative example. The square-root law quantifies emergence of the failing interval, and the sharp positive-SOE minimax obstruction states when a common sign-restricted fast-memory representation cannot be accurate on the entire natural frequency window. This concerns a distinguishable design constraint and does not assert failure of the authors' signed/adaptive discrete compression, nor stability failure of the PDE scheme. All limitations are preserved in the result.

## Closest literature and remaining risks

- Yuan–Zegeling (2026), arXiv:2610.27262v1, full HTML: source model and BE generating weights; no matched classification in sections inspected.
- Garrappa–Giusti (2023), DOI 10.1007/s10915-023-02283-6, open full HTML: general CQ and same symbol; no matched sign-window result in inspected sections.
- Garrappa–Giusti–Mainardi (2021), arXiv:2102.09932, full HTML: prior non-complete-monotonicity examples for different Scarpi kernels.
- Beghin–Cristofaro–Garrappa (2023), arXiv:2303.14743, full HTML: relaxation Bernstein conditions, not this exact BE first weight.
- Al-Mutairi–Furati–Garrappa (2026), DOI 10.1007/s13540-026-00577-8: abstract inspected only. Detailed contents are an unresolved historical-priority risk.

Self-review: passed. Independent audit: not yet performed.
