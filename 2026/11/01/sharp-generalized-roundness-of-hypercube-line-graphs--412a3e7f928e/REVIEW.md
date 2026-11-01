# Scientific review: sharp generalized roundness of hypercube line graphs

## Correctness

PASS. The intrinsic line-graph distance between distinct cube edges equals one plus the minimum endpoint Hamming distance. Walsh diagonalization groups the powered-distance matrix into explicit constant-off-diagonal axis blocks. For \(0<p<1\), the Bernstein integral makes every nonconstant block's axial eigenvalue strictly negative and orders all transverse eigenvalues strictly below the empty-Walsh-support transverse eigenvalue, apart from that leading mode itself. The leading mode is precisely \(S_n(p)-1\), so its unique root yields the sharp threshold and \((n-1)\)-dimensional endpoint nullspace. The four-cycle case \(n=2\) is handled directly at \(p=1\). The binomial concentration estimate and integration inequalities prove the exact first-order asymptotic for arbitrary \(n\). The companion checker independently builds line-graph distances by BFS and matches twenty direct dense spectra for dimensions two through five; finite computations are not used as an infinite proof.

## Originality

PASS under bounded historical review. Sánchez (arXiv:1108.0451v1, §§1–3) gives the general finite negative-type determinant criterion and an explicit calculation for complete bipartite graphs, not the hypercube-edge family. Murugan (arXiv:1112.5657v1, §§2–4) treats vertex-transitive spaces generally and Hamming-*vertex* subsets; the latter metric is not the intrinsic line-graph metric. Prior all-bandwidth Walsh spectral results for exponential-distance kernels on the same graph make the block decomposition non-novel and could be transformed to yield powered-distance spectra, but they do not state the sharp powered negative-type threshold, its uniquely responsible sector, the endpoint Euclidean rank, or the exponential dimension asymptotic. Searches for alternate terminology, including cuboctahedral graph, snowflake exponent, Schoenberg exponent, and line graph of a hypercube, located no explicitly covering theorem. This negative search is not a proof of novelty. A hidden earlier optimization within graph-metric negative-type literature remains possible.

## Value

PASS. Cube vertex Hamming metrics have negative type at power one, yet the natural edge-adjacency passage collapses the sharp negative-type exponent to order \(n2^{-n}\). This is a sharp infinite-family geometric boundary, not a fixed-size numerical computation. The result identifies the exact equality eigenspace, strictness range, minimal squared-Euclidean embedding dimension, and dimension asymptotics. It is relevant to snowflake embeddings and Schoenberg kernel theory on highly symmetric graph metrics. It is not claimed to settle other line-graph families or independent external validation.

## Closest literature and limitations

- Stephen Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451v1 (2011-08-02), §§1–3.
- Mathav Kishore Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657v1 (2011-12-23), §§2–4.
- Existing exponential-distance Walsh spectra on these same line graphs are a relevant stronger algebraic starting point, but the new sharp power optimization is a distinct assertion; equivalence through a further integration and global sign argument is the main residual coverage risk.
- The checker uses NumPy. The proof does not require NumPy or finite enumeration.

Self-review: passed. Independent audit: not yet performed.
