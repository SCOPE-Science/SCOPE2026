# Self-review

## Correctness — PASS

For a full-row-rank residual constraint the Gaussian reduced matrix has full row rank almost surely. The proof decomposes every feasible correction orthogonally into the unique global row-space correction and a nullspace component. A Gaussian-row Schur complement gives the classical inverse chi-squared coefficient law; conditional Gaussian independence gives the raw correction's independent chi-squared numerator. A second Schur complement on a Gaussian representation of the orthogonal-complement Haar plane gives the orthonormalized correction's distinct chi-squared numerator. Gamma integrals establish **all** positive real moment thresholds, including divergent boundaries. The explicit rational example and standalone program test critical identities and distributions, without replacing the universal proof.

## Originality — PASS, with residual priority risk

The closest direct antecedent is Cartis and Otemissov, Optimization Online (2020), Theorem 3.7 and Corollary 3.9. Their exact inverse chi-squared distribution and second moment concern the **reduced coefficient vector**, which is explicitly acknowledged as prior work. The present claim compares exact **ambient nullspace components** for two different tie-breakers on the **same** random subspace, with an exact dual family of marginal distributions and the sharp integrability threshold. The 2022 random-subspace Gauss–Newton analyses treat safeguarded methods; a 2024 sketched-pseudoinverse analysis treats asymptotic regularized operator equivalents. Neither inspected source implies the complete finite-dimensional same-subspace comparison without additional analysis. A different formulation using inverse-Wishart and random-Grassmannian geometry may already exist; independent priority verification remains open.

## Value — PASS

An exact-fit objective alone does not control parameter displacement in rank-deficient Gauss–Newton models. The classification distinguishes two realistic pseudoinverse tie-breakers with identical subspace and zero residual, quantifies the benefit of QR in the physically meaningful Euclidean norm, and identifies the exact two-extra-direction threshold below which squared step lengths have infinite expectation. The dimension- and residual-independent formulas make the fact useful as a reproducible benchmark for deciding when a bare Gaussian subspace coefficient norm is a misleading proxy for physical step control. Its value does not rely on novelty of the inverse-Wishart primitive itself.

## Scope and independent review

The result is a one-step exact-arithmetic analysis of an unregularized, fully consistent residual model. It does not apply without qualification to published trust-region or regularized algorithm variants, nonlinear iteration trajectories, or floating-point runtime. No sample-path infinity is asserted; only divergence of particular expectations is proved. The possible independent discovery of the equivalent finite-dimensional Grassmannian law remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
