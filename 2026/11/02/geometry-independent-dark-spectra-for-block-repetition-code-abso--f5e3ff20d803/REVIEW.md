# Independent mathematical audit

## correctness

PASS

For the one-particle uniform-hopping Q_N graph, each Walsh character of weight w has energy N-2w and its restriction to all block repetition codeword traps is the m-bit Walsh character indexed by block coordinate parities. Orthogonality of distinct syndromes makes r_w exactly the number of feasible parities at weight w. For syndrome s, admissible weights are h(s),h(s)+2,...,h(s)+2u(s). Summing their finite geometric polynomials and using the block identity {2 floor(b/2),1+2 floor((b-1)/2)}={b,b-1} gives F(z)=(1+z)^(m-1) sum_(j=0)^(N-m+1) z^j. F(1)=2^(m-1)(N-m+2). Complement is strictly dissipative because any eigenvector with zero imaginary eigenvalue lies in ker Gamma and an adjacency eigenshell kernel; hence maximally mixed capture B/2^N and loss-rate independence hold. Independently evaluated all ordered block compositions N=2,...,8 (254 cases), separately of source checker; inspected verify.py GF3 Walsh restriction rank and GF101 Krylov approach. Positive loss EVERY trap and all codewords essential; no finite-time decay claim.

## originality

PASS

Best-of-knowledge PASS: standard quantum-walk eigenbasis and dark-state framework do not directly supply the geometry-independent all-shell polynomial for arbitrary positive block sizes. The result is mathematically equivalent to a code Fourier-restriction rank profile and is searched in that form. General coding-theory subgroup evaluation may contain an equivalent proof.

## value

PASS

Complete invariance of bright/dark dimensions across nonisometric trap-code geometries is a nontrivial spectral rigidity phenomenon with an explicit all-shell formula and exact capture fraction. It is an analytically useful benchmark for lossy walks and control/observability, not a routine single-eigenvalue calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
