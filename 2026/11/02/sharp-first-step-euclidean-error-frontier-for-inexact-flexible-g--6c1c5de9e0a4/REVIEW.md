# Mathematical assessment

## Correctness — PASS

The first FGMRES least-squares residual is a Euclidean projection, so the attainable residuals are precisely \(tu\) with \(u,v\) unit and \(v^{\mathsf T}u=t\le\mu\); the reverse construction \(Az=v-tu\) proves there is no relaxation gap. The ratio of physical errors is \(t\|A^{-1}u\|_2/\|A^{-1}v\|_2\). Compression of \(A^{-2}\) to the span of \(u,v\) and a determinant-one two-by-two singular-value calculation give the exact fixed-\(t\) envelope. Its one-variable derivative has one maximizing point. Direct algebra yields the unique safe-tolerance crossing, and an explicit two-mode singular-vector construction attains equality. A standard-library verifier checked 99 exact-rational identities and 27,461 numerical conditions; finite checks supplement the proof.

## Originality — PASS, subject to historical priority

The inspected full first arXiv version of Güttel–Nyman develops sharp FGMRES residual contraction but not the Euclidean solution-error envelope, sharp nonexpansion threshold, or the saturated two-mode gain. Weiss's accessible abstract establishes a qualitative error/residual distinction, not the exact dependence on both \(\kappa\) and \(\mu\). Bauer–Householder spectral inequalities are related background and may subsume the angular lemma; the new assertion is the entire exact FGMRES optimization. A published unpreconditioned symmetric GMRES(1) error-barrier theorem uses a different search direction and no inner tolerance, so neither statement implies the other as given. The strongest residual risk is an older equivalent result in a minimum-error/Krylov or matrix-angle formulation not located in the inspected material.

## Mathematical value — PASS

The naturally motivated target is the smallest **inner residual tolerance sufficient to prevent a one-step solution-error increase**. The theorem gives its sharp dependence on conditioning, the complete minimax profile, and exact adversarial equality witnesses: for \(\kappa=10\) and \(\mu=1/5\), a residual contraction of \(1/5\) can coexist with solution-error amplification almost twofold. This is a substantive stopping-rule boundary, not merely a generic norm inequality. It is intentionally limited to first-step exact-arithmetic SPD systems.

## Closest literature and limitations

Güttel–Nyman (arXiv:2604.27971v1) supplies the first-step residual guarantee and the motivating preconditioner criterion. Weiss (1994) supplies qualitative error/residual separation. Bauer–Householder (1960) supplies classical condition-number geometry. A publicly available unpreconditioned GMRES(1) theorem establishes a different sharp Euclidean error bound. These comparisons cannot certify historical uniqueness; some older primary full texts were not accessible. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
