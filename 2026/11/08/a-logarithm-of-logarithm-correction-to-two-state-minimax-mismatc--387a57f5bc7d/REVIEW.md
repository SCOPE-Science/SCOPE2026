# Scientific review

## Correctness — PASS

The proof directly computes both off-diagonal rates of the two-state Markov transition matrix, uses the identity \(H(X_0\mid X_t)=H(X_0)+H(X_t\mid X_0)-H(X_t)\), and establishes strict concavity from an exact positive variance decomposition. It controls the optimizer's boundary layer: first \(\varepsilon_t\to0\), then \(\varepsilon_t/t\to\infty\), then \(\varepsilon_t\log(1/t)\to a/(a-b)\). Taylor remainders are \(o(t)\) at that scale, providing a full constant-order expansion; the symmetric case follows from strict symmetry. The standalone verifier checks the exact finite-time identities and examples, not the infinite-time limit. The expansion is pointwise for fixed unequal rates, not uniform near equality.

## Originality — PASS, with residual priority risk

The closest primary result, Yousef–Ansbacher–Wolpert, arXiv:2610.03478 (2026-10-02), identifies the minimax cost with maximum conditional entropy and proves its leading \(\lambda_{\max}t\log(1/t)\) behavior and qualitative maximizing-prior concentration, including supplemental Section SX. Inspection found no quantified optimizer rate or log–log and order-\(t\) asymptotic. Nedić–Kovačević–Čapko–Vukmirović (doi:10.37190/0208-4147.00246) gives general maximum-equivocation theory and algorithms but not Markov short-time asymptotics. Semantic claim searches and previously accessible claim records disclosed no statement implying this one. These searches do not establish priority exhaustively; classical binary-channel asymptotics remain a residual comparison risk.

## Value — PASS

The leading escape-rate law alone fails to specify how the optimal input prior approaches the boundary, and cannot resolve whether the next correction is of ordinary order \(t\) or the substantially larger order \(t\log\log(1/t)\). This theorem resolves both questions with exact coefficients for the minimal nontrivial continuous-time chain and isolates the singular balanced-rate boundary. The distinction matters when using near-identity channels or minimax mismatch costs at short times, since a fixed interior prior misses the sharp optimization regime. It is an asymptotic classification, not a claim of a full higher-state theory.

## Closest literature and scientific limits

[1] M. Yousef, B. Ansbacher and D. H. Wolpert, *Minimax entropy production for arbitrary processes*, arXiv:2610.03478, including the Supplemental Material, https://arxiv.org/html/2610.03478v3 .

[2] N. Nedić, M. Kovačević, D. Čapko and S. Vukmirović, *Notes on conditional entropy and commitment capacity*, Probability and Mathematical Statistics **45** (2025), 115–126, doi:10.37190/0208-4147.00246, https://www.math.uni.wroc.pl/~pms/files_doi/g00246/g00246.pdf .

No higher-dimensional, uniform-near-symmetry or total-entropy-production theorem is asserted. Bibliographic incompleteness, especially broader asymmetric binary-channel expansions, remains possible. Computational checks are supporting finite-precision checks only.

Self-review: passed. Independent audit: not yet performed.
