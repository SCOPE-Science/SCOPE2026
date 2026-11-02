# Scientific review

## Correctness

PASS. The full five-dimensional Laplacian splits by reflection into two nontrivial two-dimensional spectral blocks. Explicit branch equations give the candidate; a polynomial with seven strictly negative Bernstein coefficients proves uniqueness of the price parameter on the entire claimed interval. Two positive spectral-dual multipliers furnish an exact edgewise supporting certificate valid for unrestricted conductance vectors, and equality forces the original symmetric solution by five eigenvector equations. All central symbolic identities are independently recomputed by `verify.py`; the finite numerical tests only supplement the proof. The boundaries are explicitly excluded from uniqueness.

## Originality

PASS on inspected evidence, with priority risk. Sun–Boyd–Xiao–Diaconis (2006), Sections 3–5, solve the general problem by SDP and the equal-price cycle case, but do not give the claimed exact price-to-conductance law on an unequal-price five-cycle. Their Result 6 bounds the cycle eigenvalue multiplicity, which does not imply the explicit active-phase allocation. Boyd–Diaconis–Xiao (2004) optimize a different discrete-time SLEM objective. An earlier cycle-edge-screening result already gives the closing-edge threshold at \(q=16\) and is not superseded by claiming that threshold again. Exact all-parameter active allocation, global uniqueness and strict monotone rational inversion are the distinctive claim. Specialist older spectral extremal literature, including Fiedler's 1993 minimax work, remains a possible priority overlap because its full text was not available.

## Mathematical value

PASS. Four identical prices and one exceptional price are a canonical one-defect graph-design problem. The smallest nontrivial odd cycle beyond a triangle has a two-dimensional competing Fiedler eigenspace, so the allocation is not a direct one-branch path calculation. The new explicit active-phase solution and global asymmetric uniqueness complement the already known edge-screening price and provide an exactly solvable benchmark for cost-sensitive spectral optimization.

## Limits and closely related literature

The result is restricted to \(C_5\), ordinary Laplacian mass normalization, continuous-time gap and \(0<q<16\). It does not claim general-cycle formulas or rates at endpoint prices. The historical full-text access limitation is a residual originality risk rather than a claim of having read inaccessible work. Numerical checks do not certify an infinite parameter continuum; the analytic Bernstein and dual identities do.

Self-review: passed. Independent audit: not yet performed.
