# Independent mathematical audit

## correctness

PASS

The Fourier eigenvalues E_k=2J cos((2 pi k+phi)/N) are distinct except phi modulo 2pi equals 0 or pi; degeneracies pair k with -k (zero) or -1-k (pi). Each Fourier mode contributes seed spectral weight 1/N, so generic dephased cyclic density is the maximally mixed state and all N Krylov populations equal 1/N. Even N half-flux has all paired weights 2/N, giving m equal populations; at zero flux the reflection-shell Lanczos vectors and finite cosine-square sums give endpoint/interior populations, with the odd-N pi case gauge equivalent to minus the zero-flux Hamiltonian. Independent NumPy Hamiltonian/Lanczos/eigenprojection dephasing reproduced every branch for N=3..12, not relying on source claimed populations. Spectral theory and finite geometric-series identities prove all N; noncommuting infinite-time and phi limits arise from fixed-time continuity versus dephasing degeneracy.

## originality

PASS

Jeevanesan primary quantum-walk spread-complexity article develops the exact measure and covers path, complete graph, stars, attached hubs/trees, but inspected mathematical sections do not state flux-threaded cycle parity and Krylov index populations. Adamczak et al study vertex average mixing, a different observable; spectral energy degeneracies are known and not claimed new. Luppi studies flux and measurement correlations, not the exact Krylov time-averaged law in accessible abstract. No direct Resultary match.

## value

PASS

Complete all-cycle magnetic-flux and parity classification for a natural quantum-information complexity observable, with a discontinuous Cesaro limit despite continuous finite-time dynamics; this distinguishes Krylov spreading from spatial mixing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
