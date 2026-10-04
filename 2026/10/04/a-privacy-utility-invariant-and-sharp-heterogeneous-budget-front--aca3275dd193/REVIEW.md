# Same-model review

## Correctness
PASS. With independent canonical perturbations, each factor has \(\mathbb E[e^{-\xi_k}]=1\), so independence preserves e-value validity of the product. The summed log-noise is exactly Gaussian with mean \(V/2\) and variance \(V\). Disjoint adjacency changes one block, giving product log sensitivity \(\Delta_{\max}\). Equal-variance Gaussian trade-off functions therefore give the sharp parameter \(\Delta_{\max}/\sqrt V\); the supremum definition of sensitivity supplies sharpness. The constrained frontier follows from two necessary lower bounds on \(V\), both of which are explicitly attained.

## Originality
PASS. The motivating Gaussian-private-e-value paper states generic heterogeneous GDP composition but its sharper disjoint-product theorem uses a common \(\mu\). Its proof isolates product sensitivity and summed Gaussian variance, which permits the heterogeneous extension. The earlier differentially private e-value product result inspected is under Rényi DP and does not state the heterogeneous Gaussian-DP law. Targeted semantic searches did not reveal the privacy–utility invariant or complete cap frontier. A natural extension can have terminologically different or unindexed antecedents, so this remains a residual risk rather than a novelty proof by failed search.

## Value
PASS. Heterogeneous local privacy requirements are natural in decentralized or multi-source analyses. The result turns the product mechanism into a complete one-dimensional design problem: every allocation is summarized by \(V\), the exact privacy/evidence-loss trade-off is fixed by an invariant, and arbitrary local caps plus an aggregate cap admit a closed-form optimum and constructive attainment. This is a structural design law rather than a parameter substitution or numerical recomputation.

## Closest literature and limitations
The closest source is Kuang, Gang, and Xia, arXiv:2605.29388, especially the general aggregation proposition, common-budget product theorem, and its proof. Csillag and Mesquita, arXiv:2510.18654, gives an adjacent private-e-value product property under Rényi DP. Dong, Roth, and Su provides the GDP trade-off framework. The claim is restricted to the published scalar product under independent Gaussian perturbations and disjoint blocks; factor-level release and overlapping data require different accounting.

Same-model review: passed. Independent audit: not yet performed.
