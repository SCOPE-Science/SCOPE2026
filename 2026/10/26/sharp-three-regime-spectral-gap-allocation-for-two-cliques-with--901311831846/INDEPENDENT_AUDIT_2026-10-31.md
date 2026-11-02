# Independent mathematical audit

## correctness

PASS

The Rayleigh-min formula makes lambda2 concave in the weights; averaging over both gateway/nongateway permutations and layer swap reduces global optimization to a,c,d,b. Explicit invariant-subspace diagonalization yields odd-mode polynomial mu²-(nd+2kb)mu+2k²bd and gateway fluctuation eigenvalue ka+ud+kb, while mu_-<kd<nd, making nongateway-nongateway c never useful. With kd=lambda(1+t), the Schur inequality gives b0=lambda[((n/k)(1+t)-1)]/(2kt); additional b can be transferred to cheaper a. The budget equals lambda F(t) and both spectral constraints attain it. The involution t->1/(2t), convex active derivative u(1+1/k-1/(2kt²)) and H(t)=1 thresholds yield t*=1/2, t_- or tau_k exactly; averaging and nonnegativity force the claimed supports in every optimum. Independent direct Laplacian eigenvalue/budget calculations checked 110 (k,u) pairs (matrix checks up to n=16), rather than treating source VERIFY.py success as proof. No normalized/Markov Laplacian is claimed.

## originality

PASS

Best-of-knowledge: compared mathematical implication, equivalent aliases, broader frameworks and exact tables; not directly covered by sources actually inspected. Residual literature risks and incomplete full-text access are explicitly recorded.

## value

PASS

A joint intra-/interlayer resource allocation of intrinsic interest in spectral graph optimization: exact lambda2, support-regime transitions and globally forced edge deletions across a natural two-community family. The mixed optimization distinguishes what to build inside communities from the interconnection budget; not a routine substitution of fixed-layer weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
