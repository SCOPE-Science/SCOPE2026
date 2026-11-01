# Independent mathematical audit

## correctness

PASS

Specializing Carrel–Vandereycken Eq (31) to scalar drift -aI and constant PSD forcing C gives W=sY+q(PC+CP-PCP), with s=exp(-2ah), q=(1-s)/(2a) or h for a=0, and t=q/s. For rank-one Y=sigma uu^T, the only nonzero block of W/s is [[sigma+tc,t||w||],[t||w||,0]], whose positive eigenvalue has strictly larger magnitude than any negative eigenvalue, so every best rank-one Frobenius/SVD truncation is uniquely PSD. For Y=diag(d,e,0), C=(1,0,1)(1,0,1)^T, R=W/s has spectrum p(t)>0,e>0,-b(t), b=[sqrt((d+t)^2+4t^2)-(d+t)]/2. The SVD rank-two selection flips to the negative eigenmode when b>e, equivalently t^2>e(d+t+e), with unique t_*=(e+sqrt(4de+5e^2))/2. h_* follows by inverting t(h). At equality both PSD and indefinite optimal truncations are possible. Higher-rank embedding discards a smaller positive e, retains negative -b, and minimum dimension/rank are 3/2. PSD-constrained best approximation residual s*b versus unrestricted s*e, unbounded b/e as e to zero; exact flow sY+qC remains PSD. Independent SymPy characteristic polynomial, threshold relation and exact witness eigenvalues (1+sqrt2,1/10,1-sqrt2) verify critical arithmetic; not a proof substitute.

## originality

PASS

Carrel–Vandereycken introduced the exact tangent-projected exponential Euler and Eq (31); the algorithm is unequivocally prior. Other Lyapunov solvers (Kressner et al.) were already known to yield indefinite approximants and need positive-part repair; this generic phenomenon is not new. The assessed contribution is the specific method-wide rank-one safety theorem, rank-two minimal counterexample, exact step boundary including tie and damping, and unbounded constrained repair cost. The primary original method paper does not state those facts. Risk remains that an older generic best-rank PSD perturbation theorem subsumes these exact formulas.

## value

PASS

Positive-semidefinite invariance is crucial for covariance and Lyapunov solvers. The sharp minimal rank-two three-dimensional counterexample distinguishes a numerical method preserving low rank from one preserving physical covariance positivity. The exact damping-compatible step threshold, tie behaviour, and arbitrarily costly PSD repair quantify a motivated failure, beyond a routine negative eigenvalue example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
