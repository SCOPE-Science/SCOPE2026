# Scientific review

## Correctness — PASS

A binary conditioning variable makes conditional expectations affine, so MTP2 implies nonnegative least-squares residual covariance for every pair among at most three spins. For the four-spin family, pairwise nonnegative log interactions establish MTP2, and conditional independence of the two leaves makes their linear residual covariance exactly the product of two logistic second differences and a strictly positive binary-interaction residual variance. The Schur-complement inverse sign is therefore exact. The rational example and exact arithmetic checks agree. Finite checks do not substitute for the analytical argument.

## Originality — PASS (with residual priority risk)

The closest primary work, Fallat et al., *Total positivity in Markov structures* (arXiv:1510.01290), proves general MTP2 conditional-independence and factorization properties, and discusses M-matrices for Gaussian MTP2. Its inspected binary and Gaussian sections do not state the dimension-three boundary or the four-spin logistic-curvature precision sign rule. Karlin–Rinott establish the Gaussian equivalence, which does not imply the non-Gaussian conclusion. Slawski–Hein is Gaussian-specific. Baba–Shibata–Sibuya show the broader separation of partial and conditional correlation; their abstract was available, but their full text was not verified here, so priority risk remains. The novelty claim excludes all general MTP2 preservation and Gaussian results. Similarity-search results on unrelated occupancy and inversion precision models were compared by implication, not by title.

## Mathematical value — PASS

A basic Gaussian shortcut identifies attractive dependence with a nonpositive off-diagonal precision. The theorem proves that shortcut cannot automatically be transferred to binary MTP2 models, gives the least possible binary dimension, and determines the complete sign transition for a natural nontrivial ferromagnetic graph. The explicit curvature mechanism explains *why* conditional independence and negative linear partial correlation coexist, which is relevant to graphical modeling and covariance-based surrogate inference.

## Limitations

An earlier formulation via general nonlinear-regression Schur complements or log-linear Ising methods may implicitly contain the conclusion. Such priority has not been independently audited. The four-spin formula concerns one precision entry of the given model, not arbitrary four-spin laws.

Self-review: passed. Independent audit: not yet performed.
