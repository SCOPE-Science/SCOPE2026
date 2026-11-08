# Independent mathematical audit

## correctness

PASS

In orthonormal (p,q) coordinates the error matrix has rows (0,-h/a) and (-alpha h,1-alpha b). Direct independent SymPy expansion of det(I-T^T T) agrees identically with -r^2+2y-[1+(1-r^2)s^2]y^2. If r>=1, ||T q||>=r; if r<1 the determinant criterion gives exactly the root interval. Setting alpha=1/b gives norm max(r,s), bounded by (kappa-1)/(2sqrt(kappa)) by AM-GM on rotated diagonal SPD matrices. Choosing tan(theta)=sqrt(mu/L) forces r to attain this value for every alpha, proving exact minimax, including kappa=1, h=0 and the critical 3+2sqrt2 threshold.

## originality

PASS

Fan–Hu–Zhang establish Type-II reduced-basis correction, invertibility and general Richardson error discussion. The rank-one 2D Euclidean one-step minimax, exact tunable window and the nonnormal amplification threshold differ mathematically from spectral/energy-norm bounds and the separate published weighted-Jacobi problem. Full motivating paper was not accessible in this run; this is best-knowledge with explicit implication risk.

## value

PASS

One-step Euclidean amplification of a convergent preconditioned iteration is a natural numerical stability invariant. The exact worst-orientation condition-number threshold separates universal contractivity from unavoidable optimally tuned spikes; the sharp safety interval supports practical coefficient selection in the specified 2D model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
