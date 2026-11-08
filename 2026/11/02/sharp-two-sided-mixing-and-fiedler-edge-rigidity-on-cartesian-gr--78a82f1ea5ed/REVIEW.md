# Independent mathematical audit

## correctness

PASS

Reconstructed the orbit average of a general symmetric stochastic matrix to directional weights w_i, the eigenvalue extrema 1-min_i(alpha_i w_i) and 1-sum_i(beta_i w_i), and the budget/minimax lower bound. The weights tau/alpha_i attain it. For unrestricted Q, the PSD matrix (1-tau)I-(Q-J/N) and zero averaged Fiedler quadratic forms force Q to agree on each factor Fiedler eigenspace; independence of the local projected neighbor differences fixes every edge. Petersen adjacency identity A^2=2I-A+J gives Pi=(4I+2A-J)/6 with Gram (2/3)I_3; cycle trigonometric Fiedler columns independent. Recomputed all ten Petersen local Gram matrices and 84 k,m branch instances. For odd m, (4-beta_m)/alpha_m=1/(4 cos^2(pi/(2m))) yields positive hold only k=1. Finite checks corroborate, while tensor/PSD proof covers all stated finite factors.

## originality

PASS

The value formula is a symmetry-reduced standard fastest-mixing SDP application, and is not claimed novel alone. Best-of-knowledge surviving claim is a local Fiedler-edge independence criterion that proves uniqueness even for arbitrary non-invariant edge/loop weights, and the exact Petersen-cycle holding transition. The inspected Boyd–Diaconis–Parrilo–Xiao paper develops symmetry-based semidefinite optimization and Cartesian examples but its checked product and Petersen discussions do not establish this unrestricted local rigidity theorem. An implicit SDP strict-complementarity consequence elsewhere remains possible.

## value

PASS

The local spectral independence test upgrades a symmetric optimum to an unrestricted uniqueness certificate, a structural issue not decided by averaging. The alternating zero/nonzero holding transition on a natural mixed Petersen-cycle family is an exact, parameter-uniform boundary, not a standalone generic numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
