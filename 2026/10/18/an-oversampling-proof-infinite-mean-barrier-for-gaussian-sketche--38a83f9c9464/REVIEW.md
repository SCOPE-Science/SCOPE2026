# Independent mathematical audit

## correctness

PASS

For grade(A,r)>k, AV_k=V_kH+βv_{k+1}e_kᵀ and nonzero irreducible tridiagonal Lanczos cofactor γ=βe_kᵀH^-1e1. Orthogonal invariance of Gaussian sketches makes U=SV_k and h=Sv_{k+1} independent; z=(UᵀU)^-1Uᵀh=G/R with independent G∼N_k and R∼χ_{s-k+1}. The sketched Galerkin operator H+βze_kᵀ has determinant det(H)(1+wᵀz), and Sherman–Morrison y=a-γH^-1G/(R+wᵀG). The numerator does not cancel the denominator on the open half-space wᵀG<0 where a positive chi density meets L=R+wᵀG=0. Integrating this transversal simple pole yields a finite positive C/T energy-error tail; p<1 is exactly locally integrable, p≥1 diverges for every finite s. The sketch of the ordinary least-squares projection instead produces an affine nonsingular transform of Student_ν, yielding exact ν-moment cutoff. Under the terminal-grade case β=0 the obstruction disappears, appropriately excluded. Independent analytic algebra checked against the pinned checker defining equations, 1-step and multistep rank-one matrix reductions; bounded source rational and numerical checks are not proof of tail convergence. We did not independently execute every source numerical tail test in this audit.

## originality

PASS

Best of knowledge after inspection of specified pinned source and actual primary literature. The Student law overlaps classical randomized least squares; it does not directly state the heavy-tailed nonlinear inverse affine-hyperplane pole caused by nonzero Lanczos coupling γ in every nonterminated grade. The known Student fact and sketch projection definitions supply ingredients, but their original statements do not appear to assert every finite s/k energy-error 1/T tail with positive constant; this is a nontrivial derived result, yet implication via an unindexed general inverse-regression theorem remains possible.

## value

PASS

This identifies an important unconditional instability masked by high-probability subspace embedding guarantees: arbitrarily large finite Gaussian oversampling cannot make unsafeguarded sketched FOM/Galerkin have finite absolute mean energy error, despite SPD A. The minimal-residual contrast explains which projection/safeguard mitigates heavy tails and separates rare failures from typical performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
