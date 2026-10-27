# Scientific review — two-candidate common-threshold distortion

## Correctness — PASS

Each pair of threshold reports determines the intersection of two scalar utility bins. Under the two-alternative unit-sum equation this is precisely one cell of the reflected mesh. The midpoint comparison guarantees the claimed distortion because every reported interval is at most the mesh width. The two-voter reflected-cell construction forces the opposite endpoints on any fixed deterministic decision, obtaining the same bound as a supremum. Pigeonholing the at most \(2t+1\) cells and enforcing equal lengths establishes both the optimum and the exact \(2^t\) equality family. The no-endpoint-inclusion assumption is unnecessary because utilities approach every cell endpoint from within. An executed standard-library exact-rational program confirms 57,568 assertions over 639 threshold vectors, including exhaustive cell-report profiles with one to three voters for each tested vector; the infinite quantifiers are justified by the analytical proof, not enumeration.

## Originality — PASS (priority risk remains)

The closest primary manuscript, Latifian–Nilipour–Voudouris (2026), gives general geometrically spaced threshold upper bounds and asymptotic lower bounds, not the exact fixed-threshold formula at two candidates or full optimizing threshold-set classification. The earlier threshold-matching study concerns matching rather than a common winner, and the general elicitation-versus-communication literature does not imply this exact formula in its inspected results. Approval with runoff supplies extra voter comparisons and differs from deterministic one-stage winner selection. Semantic mathematical record searches found no exact matching implication, though absence in a search is not proof of historical novelty. The two-candidate reflected-mesh reduction distinguishes the result from general dimension-dependent bounds. Historical-priority uncertainty is retained explicitly.

## Mathematical value — PASS

The paper's universal deterministic bound \(2(2m)^{1/t}\) does not reveal the sharp behavior in the smallest nontrivial election as thresholds grow. This theorem gives an exact complete threshold-design problem with a nontrivial reflection constraint, certifies a precise \(1+1/t\) distortion frontier and classifies every optimum. It identifies how much welfare information an extra public threshold is worth, and supplies an attainable benchmark for studying richer elections. Its exact all-electorate guarantee is not a mere fixed-size enumeration or a restatement of the literature's asymptotic guarantee.

## Closest literature and remaining limitations

Relevant comparisons: Latifian, Nilipour, Voudouris (2026), arXiv:2610.13725, model and Sections 3–4; Latifian and Voudouris (2024), arXiv:2401.09858, matching scope; Mandal et al. (2019), general communication–distortion framework; Ebadian, Latifian, Shah, *The Distortion of Approval Voting with Runoff*, different two-stage protocol. The result assumes two candidates, truthful nonadaptive shared threshold reports, unit-sum utilities and deterministic rules. An earlier equivalent derivation not located in the inspected sources remains possible.

Self-review: passed. Independent audit: not yet performed.
