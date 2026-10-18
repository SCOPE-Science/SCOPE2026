# Independent mathematical audit

## correctness

PASS

For SPD A,B and C=A^(1/2) B A^(1/2) with eigenvalues in [1−δ,1+δ], δ∈[0,1), the residual map is T=I−AB=A^(1/2)(I−C)A^(−1/2). Therefore ||T||₂<=δ sqrt(κ₂(A)), and in the A^(−1) norm its factor is ≤δ. For any κ≥1, take A=diag(κ,1), C=I−δ[[0,1],[1,0]], B=A^(−1/2) C A^(−1/2) SPD. Then T=δ[[0,sqrtκ],[1/sqrtκ,0]] has norm EXACTLY δ sqrtκ (for κ>=1), so the sharp uniform nonexpansion threshold is δ sqrtκ<=1. For κ>1 converting κ_p=(1+δ)/(1−δ) is algebraically equivalent to κ_p<=(sqrtκ+1)/(sqrtκ−1); for κ=1 the frontier is δ<=1 automatically. Independently checked the rational example A=diag(9,1), B=[[1/9,−1/6],[-1/6,1]], C eigenvalues 1/2 and 3/2, T=[[0,3/2],[1/6,0]], singular values 3/2 and 1/6. Does not claim numerical residual gap stability.

## originality

PASS

Classical spectral equivalence and energy-norm Richardson convergence are covered. A tight Euclidean RESIDUAL amplification depending simultaneously on δ and κ₂(A), with an attained 2×2 SPD nonnormal similarity and exact monotonicity frontier, was not located in directly relevant numerical analysis literature or published related findings. This is a distinct norm and quantifier from energy-norm contraction and unpreconditioned SPD Richardson step-size safety. The similarity bound itself is textbook; novelty is restricted to its sharp worst-case application and safety distinction.

## value

PASS

An SPD preconditioner can give strongly contracting preconditioned residuals yet transiently increase the ordinary stopping-test Euclidean residual. The exact δ sqrtκ frontier gives a usable, parameter-sharp yes/no condition, with the smallest possible two-dimensional witness, for a common stationary correction. This natural stability-boundary diagnostic is more than a sign/type check, despite elementary norm algebra; it does not pretend to be a new Richardson convergence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
