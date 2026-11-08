# Independent mathematical audit

## correctness

PASS

For any nonsingular real M-matrix A=D-E-F and nonnegative g=D^-1 b, forward SOR from zero has x1=omega*R*g with R=(I-omega L)^-1>=0, and x2=omega*(R+(1-omega)R^2+omega*R U R)*g. Nilpotent L^q=0 gives coefficients (j+2-(j+1)*omega) of (omega L)^j, all >=0 exactly for omega<=1+1/q within 0<omega<2. Since q<=n yields n-universal bound. For symmetric Stieltjes path A=I-epsilon*T_n, response (n,1) is omega^n epsilon^(n-1)*(n+1-n omega)+O(epsilon^(n+1)), negative for all omega>1+1/n sufficiently small epsilon. Independently reconstructed exact rational small-n SOR sweeps and n-dependent boundary/above examples. Limit is two forward sweeps from zero, not all iterates or general convergence.

## originality

PASS

Exact n-dimensional two-sweep coordinatewise sign frontier for M-matrices and nilpotency-index refinement are not in the inspected earlier two-dimensional published special case. General SOR norm convergence and splitting regularity are logically weaker/different properties. 2D threshold 3/2 is explicitly known and not represented as new. Best-of-knowledge PASS for n>=3 and general result.

## value

PASS

A sharp finite-time positivity guarantee for a classical numerical method exposes order-dependent nonnegativity despite eventual convergence. Uniform margin 1/n and nontrivial nilpotency-index refinement inform positivity-sensitive iterations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
