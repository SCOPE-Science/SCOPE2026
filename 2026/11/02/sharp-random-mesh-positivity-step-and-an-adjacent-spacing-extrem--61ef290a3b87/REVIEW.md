# Scientific review

## Correctness — PASS

With \(n\) positive cell lengths \(H_i\), the exact lumped mass/stiffness entries give a sharp positivity threshold \(\tau_n^*=(1/2)\min_iH_iH_{i+1}\). The uniform-order-statistic spacing vector is Dirichlet and equals independent exponentials divided by their sum. The product small-ball probability is \(t\log(1/t)+O(t)\); the probability of two overlapping small-product events is at most \(2t\). A separated-block Bonferroni argument proves the Poisson zero-event limit without assuming adjacent-product independence. The sum of exponentials has law of large numbers, proving the limiting constant. Dirichlet negative moments give the exact integrability threshold. Exact-rational verification passed 800 operator cases. Simulation is only diagnostic.

## Originality — PASS, qualified

The closest literature includes random perturbation finite elements (Abdulle–Garegnani, arXiv:2103.06204), lumped-mass maximum-principle methods with exponential integration (Li–Yang–Zhou, arXiv:2010.08789), and the classical heat-equation positivity study (Chatzipantelidis–Horváth–Thomée, 2015, doi:10.1515/cmam-2015-0018). The deterministic sign criterion is prior/elementary content; the distinct assertion here is the distributional \(n^3\log n\) law and the inverse-moment barrier for *unrestricted order-statistic knots*. The first two primary papers were materially inspected in accessible full HTML. The 2015 original full PDF was not accessible at the attempted address; its abstract and bibliographic record were read. No directly dominating random-mesh time-step extreme-value theorem was found in the searched evidence, but absence of search matches cannot prove priority. Published material on dependent product extremes remains a residual overlap risk.

## Value — PASS

A random order-statistic mesh has a typical explicit positivity timestep smaller than a uniform mesh by order \(n\log n\). This separates mesh-error behavior from time-step feasibility, supplies a sharp distribution rather than a loose minimum-spacing bound, and proves infinite expected reciprocal step budget for every fixed size. This is a structural warning for unrestricted random-knot meshes, not an assertion about shape-regular perturbations.

## Remaining limitations

Exact arithmetic and one-dimensional Dirichlet heat flow only. The result concerns positivity, not the spectral stability radius. Primary publication priority and the deterministic positivity literature require independent review.

Self-review: passed. Independent audit: not yet performed.
