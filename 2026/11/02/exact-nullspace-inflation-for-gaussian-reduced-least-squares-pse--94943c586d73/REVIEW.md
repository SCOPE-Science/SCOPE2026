# Scientific review

**Correctness — PASS.** Two separate Gaussian-block factorizations, a standard Wishart Schur-complement identity with an explicit proof, and direct Gamma-integral calculations establish all cases of the two distribution laws. The full-span \(\ell=d\) exception is stated separately. The standalone verifier reproduced 7,214 numerical or algebraic consistency checks; finite checks do not prove the tail statements.

**Originality — PASS (qualified).** The numerical literature motivates sketched reduced Gauss–Newton models, physical minimum-norm completion and Gaussian pseudoinverses; it does not in the inspected texts state the exact pair of finite-dimensional excess-error laws for the two different pseudoinverse choices. The strongest nearby published result studies asymptotic sketched-pseudoinverse behavior rather than this finite-sample tie-breaking dichotomy. The Gaussian inverse-Wishart ratio identity is classical, and a previously unnoticed finite-dimensional specialization of it or of the randomized inverse-problem literature remains a priority risk. This assessment does not claim independently established novelty.

**Value — PASS.** The result isolates an operationally consequential ambiguity in rank-deficient reduced solves: minimizing the stored coefficient norm is not the same as minimizing the physical step norm. The exact oversampling threshold predicts when their population squared errors are finite, and the full-space example demonstrates that adding subspace dimensions need not remove the coefficient metric artifact. This is a self-contained sharp model, not a general convergence theorem for safeguarded Gauss–Newton.

Closest literature: Pes–Rodriguez (arXiv:2101.07560), Cartis–Fowkes–Shao (arXiv:2211.05727), and LeJeune et al. (DOI:10.1137/22M1530264). The analytical components use classical chi-squared and Wishart identities. The result excludes finite-precision effects and nonlinear/safeguarded iteration; a comprehensive independent priority audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
