# Independent mathematical audit

## correctness

PASS

The normalized sine basis diagonalizes the specified Toeplitz path, with distinct real eigenvalues since β≠0. In that basis W_H=D_j K_H D_j, where K_H is the Gram matrix of sequences (1,λ_k,…,λ_k^(H−1)); the Vandermonde square at H=n proves K_H positive definite for all H≥n. Exactly gcd(j,n+1)−1 sensor weights vanish. At each coprime node the multiplication-by-j permutation modulo n+1 gives identical absolute sine products, and the roots-of-unity evaluation gives the squared modal product 2^(−n)(n+1)^(2−n). This establishes positive ties versus singular positions. The endpoint Krylov matrix is triangular with diagonal β^t for 0≤t<n, so its Gramian determinant is β^(n(n−1)); the modal tie transfers it. At strict Schur stability, K∞ has entries 1/(1−λ_kλ_l) and is positive definite by the first n samples. The double-alternant identity gives its determinant as the squared Vandermonde divided by the ordered-pair product; division by the finite K_n determinant gives the claimed stable value, including zero λ by continuity. The inspected checker.py corroborates bounded finite-horizon ranks and determinants only; it was not executed and does not test the stable formula. The proof does not extend these placement conclusions to heterogeneous couplings, other graph boundary conditions or other criteria.

## originality

PASS

The strongest earlier related determinant/placement result located is on the normalized path and gives a different rank index and optimizer family. Other primary comparisons supply path rank analysis or the Gramian determinant metric but not the supported exact all-horizon determinant law on the Dirichlet Toeplitz path. The rank criterion and generic determinant tools are not themselves claimed as new.

## value

PASS

A uniform Dirichlet path is a standard discrete diffusion/network model, and the determinant is the reachable or observable volume criterion. The result gives all exact optimal single-node choices, including interior ties that rank positivity alone cannot distinguish, independent of horizon and coefficients, and provides usable minimal and stable infinite values. It does not claim a novel sine basis, general rank test, or optimization of trace or conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
