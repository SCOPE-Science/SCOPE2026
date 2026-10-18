# Scientific review — exact odd-epoch bias cancellation

## Correctness — PASS

For every admissible step, all local round factors have modulus less than one, so their average is an affine contraction. The synchronized fixed-point weights are exactly \(1-(1-\alpha h_i)^E\); equality with original-Hessian weights for all center vectors is equivalent to the polynomial distortion \(F_E(\alpha h_i)\) being constant across agents. For even epochs this polynomial is strictly decreasing on \((0,2)\). For odd epochs its graph has a unique fold on \((1,2)\), and levels cannot coincide across \((0,1]\) and \((1,2)\). Endpoint sign changes prove existence for precisely two curvatures with ratio below two; derivative signs at every root prove uniqueness. The odd-epoch boundary layer follows from convergent subsequences and an exact identity for two odd powers. The exact two-agent rational example and 1,148 reproducible finite assertions agree with the proof. Numerical checks do not replace analytical statements.

## Originality — PASS, with residual bibliographic risk

The broad affine iteration and curvature-distortion/surrogate viewpoint are **not** new. The strongest prior formulation appears in Charles and Konečný (PMLR 130, 2021, equations (6)–(8), Theorem 1), which characterizes surrogate gradient operators for quadratic local-update methods. Wu et al. (arXiv:2403.02589v1, equations (7)–(9)) introduce the inexact MUSIC schedule and prove sufficient convergence-to-neighborhood bounds; Wang et al. (arXiv:2206.04723v1) study average drift at the optimum. Neither inspected result states the parity-complete classification within the full \(0<\alpha h<2\) individual-contraction region, the sharp \(b/a<2\) condition, the unique nontrivial odd-epoch step, or its logarithmic boundary layer. Published mathematical-record searches including parity-aware local-update aliases did not produce those statements. The nearest parity-related record treats Lookahead-SGD minimax stability, not exact preservation of an empirical minimizer for heterogeneous client objectives. A logically equivalent characterization could still be implicit in less accessible surrogate-loss or fixed-point research; a finite search cannot certify priority.

## Value — PASS

The result answers a parameter-selection question for an established distributed optimization method: exactly when can repeated local gradient steps followed by a single uncorrected averaging step remain unbiased **for all heterogeneous centers**? The answer gives a sharp positive case and two substantial impossibility mechanisms (even epochs, or three curvature levels), rather than tuning a benchmark accidentally. The factor-of-two curvature barrier, unique stepsize, and logarithmic approach to the higher-curvature stability frontier delimit a delicate but meaningful structural exception to generic client drift. It supplies a reproducible test case for local-update gradient solvers without asserting practical robustness of near-boundary tuning.

## Closest sources and limitations

Wu–Liao–Ding–Xiao (2024), Charles–Konečný (2021), Wang–Das–Joshi–Kale–Xu–Zhang (2022), Charles–Rush (2022), and Khaled–Mishchenko–Richtárik (2019–2020) were compared at the level of their stated algorithms, exact surrogate equations, results and parameter restrictions. The strong common-polynomial viewpoint is credited; the claim is limited to the additional complete level-set classification. The output concerns synchronized epochs, exact scalar quadratics and full averaging only. Equivalent older results, finite-precision fragility, and failure of extension to general mixing weights are acknowledged risks. No independent review is reported.

Self-review: passed. Independent audit: not yet performed.
