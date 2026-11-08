# Independent mathematical audit

## correctness

PASS

For dV=kappa dW, dX=V dt, Gaussian Kac–Rice gives conditional velocity mean v0+3(u-v0t)/(2t), variance kappa²t/4 and the two explicit erfc/erf H_u,H_v crossing kernels. Their z-scaled derivative functions G_u,G_v are positive below first thresholds and negative above second, while positive integral representations imply E_j′/E_j ≤1/z. In intermediate intervals the P_u,P_v logarithmic derivatives are strictly negative (bounds <−2 and <−20 respectively), so each time kernel has exactly one peak. Splitting -∫t e^(−rt)h′ as B−A, the ratio A/B is strictly increasing 0→∞ by separated support, proving exactly one global r maximum. Independent scipy quadrature reconstructed s_u≈0.520327681 and s_v≈0.505942998, and rates ≈0.1046702621 and 0.05846588284, in agreement at numerical precision; original code verify.py was read. Reset jumps are excluded. Decimal values are not certified intervals.

## originality

PASS

PASS best-of-knowledge: Montero–Palassini–Masoliver 2024 explicitly derive identical scaling integrals and show numerical maxima, yet §IV.1.1 says maximizing constant could be obtained from integral stationary equation but they did not attempt it, and no unique-peak proof occurs in their inspected §IV or appendices. New mathematical content is model-specific strict unimodality and constants, not renewal or Rice formulas.

## value

PASS

Finding a best reset rate is a natural experimentally motivated control objective in the original physics study. Existence and plots do not prove global uniqueness or forbid secondary maxima; the strict one-crossing theorem for two distinct canonical experiments supplies exact no-reentrance classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
