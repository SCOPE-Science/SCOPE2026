# Independent mathematical audit

## correctness

PASS

The exact state is the Boolean cubic phase f_n(x)=binom(|x|,3)+x1*x2*x3 mod2. Its translated difference has alternating GF2 polar matrix entries B_ij=s+a_i+a_j plus the missing-triple correction when i,j in {1,2,3}. Partitioning coordinates by exceptional/outside and bit value into at most four groups reduces the rank computation to a <=4 dimensional matrix, accounting for even/odd group sizes and empty groups. Enumerating h=0..3 and w=0..n-3 symbolically yields five rank-count contributions for both parity classes; their sum is 2^n and colliding ranks at n=4 or 5 are explicitly additive. For quadratic Walsh transforms of rank r, exactly 2^r Fourier values have magnitude 2^{-r/2}, yielding all Pauli magnitudes and m_alpha=2^{-n} sum_r N_r 2^{(1-alpha)r}. The order-two specialization is 11/256+77/2^{n+4} (even) or +70/2^{n+4} (odd), and the alpha>1 limit follows from fixed-rank fractions. Independent direct GF2 matrix elimination reconstructed the full rank histogram for every translation at n=4..9 and exact m2 rational values; universal statement is based on the explicit 4-group linear-algebra reduction, not finite extrapolation.

## originality

PASS

Kagamihara–Tsuchiya establish the general binary-matrix rank characterization for 3-uniform hypergraph states (already prior). Chen–Yan–Zhou establish fully complete hypergraph state moments and random-retention ensemble average order-two moment. Differentiating the ensemble average at full retention determines a scalar m2 for exactly one missing gate, so that scalar is explicitly NOT independently original. Neither inspected primary full article computes the five-term rank-count histogram for the exactly one-edge-deleted complete family; that rank/magnitude distribution genuinely supplies all-order PL moments.

## value

PASS

A complete single-gate deletion is the most basic structural fault of a dense permutation-symmetric non-Clifford resource state. The exact distribution of individual Pauli magnitudes is a natural spectral invariant and yields all Rényi orders, not merely a scalar already implied by an ensemble average. Showing the order-two magic increases from the intact limit 3 to log2(256/11) for n>=6 makes a concrete counterintuitive boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
