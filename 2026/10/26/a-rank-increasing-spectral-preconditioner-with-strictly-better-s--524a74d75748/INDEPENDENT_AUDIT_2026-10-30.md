# Independent mathematical audit

## correctness

PASS

Orthogonal right residuals have rank1 norm r and rank2 norm tau=sqrt((r²+1)/2)<r; Frobenius improves too. Exact surrogate right singular vectors give P1=diag(r,1,1), P2=diag(r²,1,1)+(tau-1)vv^T. A P1^-1 has condition r. For P2 the nontrivial squared singular eigenvalues solve z²-Tz+D=0 with T=(r²+3)/2, D=2r²/(r²+1); 1-T+D=-(r²-1)²/[2(r²+1)]<0 proves lambda_-<1<lambda_+. Identity T²-D(r+1/r)²=(r²-1)²/4>0 gives kappa2>r; T~r²/2, D->2 gives kappa2~r²/(2sqrt2). Independent symbolic Gram identities and ten matrix-SVD parameter checks agree. The claim is not a CUR sampler output or a solver iteration theorem.

## originality

PASS

The Huh–Cartis–Nakatsukasa April 2026 paper already defines the spectral right preconditioner and warns of over-preconditioning and damaged spectral separation. Its explicit Theorem4.1 requires mu>0 and error norm below mu; neither hypothesis applies to this mu=0 family. The present construction is a sharp quantified counterexample in nested right projections, not the pre-existing conditional bound or CUR algorithm. Kahl–Rittich deflation concerns another operator. Residual risk: analogous inexact spectral-preconditioner perturbation examples under other terminology. The independently inspected Kahl–Rittich full PDF explicitly notes inexact deflation can worsen condition number, so qualitative deterioration is not claimed novel; its Theorem 3.6 and section 6 use a different operator and do not give this exact all-r error-improving family.

## value

PASS

Rank-adaptive spectral preconditioning is often driven by improved surrogate error; this infinite-parameter SPD construction rigorously separates that signal from conditioning, with an unbounded quantitative penalty. The finite matrix size is motivated as a minimal counterexample, not an arbitrary unmotivated slice; no claim about real CUR sampling or Krylov iteration count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
