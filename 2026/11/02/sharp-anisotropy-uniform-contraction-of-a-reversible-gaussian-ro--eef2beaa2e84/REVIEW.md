# Independent mathematical audit

## correctness

PASS

Whitening maps the rotational noise to √2 JY and the target to N(0,I₂). Each OU half-step and the symmetric-angle rotation kernel is individually self-adjoint and target-preserving, as is the palindromic product. With shared noise the difference is multiplied by DRθD; its two diagonal moments evolve by the stated symmetric positive-entry matrix with determinant kpr and trace (1+k)(p+r)/2. Its strictly positive Perron eigenvector sees every nonzero squared-coordinate initial vector, so the larger root is the exact asymptotic factor. The cross moment has multiplier k√(pr) and does not feed the diagonal. The increasing entries in r give the worst endpoint at r=1. Both endpoint column sums are strictly below 1: the first basis vector is shortened by the first D, and the second is shortened by the last D for a set of angles of positive probability. The first-order endpoint matrix has coefficient [[−4,2],[2,−2]], whose largest eigenvalue is −3+√5; the large-h limit matrix is diag(0,1/2). The matrix operator norm gives the √2 factor via Cauchy–Schwarz conditional on the initial pair; averaging over an initial optimal coupling gives the W₂² bound. For uniqueness without a moment assumption, synchronous pair differences satisfy the deterministic bound ∥e_n∥≤e^(−λhn)∥e_0∥ for λ>0. Couple arbitrary invariant initial laws and apply dominated convergence to bounded Lipschitz test functions. The fresh bounded replay tested the rational determinant and integrated all three moment coordinates independently at h=log(4), λ=1/2 (maximum absolute discrepancy 4.3×10⁻¹⁶).

## originality

PASS

The continuous model, the exact rotational subflow as an immediate special case of the SDE, and the preservation and reversibility principle for symmetric products are not credited as new. The distinction supported by the inspected passages is the exact finite-step synchronous Perron law, including the sharp uniform curvature endpoint for this exact-subflow kernel. The closest paper's numerical split uses RK4 for its perturbation flow and its Gaussian rate is a continuous-time one. Earlier perturbation and deterministic nonreversible splitting results do not supply the discrete moment operator for this chain.

## value

PASS

For a concrete, exactly implementable split model the finite-step proof separates bias-free stationarity from sharp coupling decay and shows that anisotropy does not collapse the normalized squared-error rate. This makes the exact finite-step law, including both step-size boundaries, useful beyond the known continuous guarantee or general symmetry argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
