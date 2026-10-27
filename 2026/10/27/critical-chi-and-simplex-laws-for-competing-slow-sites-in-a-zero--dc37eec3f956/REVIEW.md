# Self-review

## Correctness: PASS

The exact finite canonical marginal follows from pairwise detailed balance and stars-and-bars. A geometric-sum representation reduces the critical window to the lattice local central limit theorem with mean \(M/(a-1)\) and variance \(Ma/(a-1)^2\). The exact negative-binomial mass ratio bounds the entire left tail of that bulk sum by a uniform sub-Gaussian envelope, including arbitrary fixed-rate weak tilts, so normalization and moment convergence follow rigorously. The orthant-to-simplex change of variables yields the independent Dirichlet allocation and the \(\chi_r\) total at exact criticality. The standard-library checker passed independent stationary-generator, exact-marginal, and limiting-mean comparisons. It verifies only finite examples and does not certify the infinite theorem independently.

## Originality: PASS with residual risk

The general canonical factorization and single-defect phase transition are established by Angel–Evans–Mukamel (2004) and Evans–Hanney (2005); they are used as background and are not asserted as new. Armendáriz–Grosskinsky–Loulakis (2009) treat a different homogeneous occupancy-dependent condensation mechanism. Mailler–Mörters–Ueltschi (2015) treat random weak disorder above criticality, not the deterministic finite-defect joint window. Comparisons of primary material and research records did not disclose the complete \(r\)-site chi/Dirichlet/weak-splitting theorem. A specialized published calculation or a broadly stated conditional-local-limit result could nevertheless imply it; historical priority is uncertain.

## Mathematical value: PASS

The number of nearly degenerate slow sites changes the shape of critical fluctuations, not only a multiplicative constant: the full \(\chi_r\) family and independent simplex allocation identify a multi-site critical response. The \(\sqrt M\) excess-mass and \(M^{-1/2}\) weak-mobility windows are intrinsic to competing Gaussian bulk fluctuations, and the explicit tilted law quantifies how small microscopic advantages bias the finite-size onset of macroscopic localization. This is a finite-size stationary theorem, not a dynamic or infinite-density condensation classification.

Self-review: passed. Independent audit: not yet performed.
