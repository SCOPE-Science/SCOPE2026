# Independent mathematical audit

## correctness

PASS

Exact Gram for rows r1=(1,0,0), r2=(t,s,0), r3=(t,0,s) is [[1,t,t],[t,1,t²],[t,t²,1]], determinant d², d=1-t². Exact Schur pivots give det normalized Gram H=1, with class (trace, inverse trace): A=(T,T), B=(T,T-y²/d), C=(T+y²/[d(1+y)],T-y²/d), y=t², T=1+2/d. Thus positive-eigenvalue cubic polynomials obey chi_B=chi_A-(y²/d)z and chi_C=chi_B-y² z²/[d(1+y)], so largest roots strictly increase A<B<C. Saddle spectrum lambda±=(1±sqrt(1+4mu))/2 proves strict spectral-radius classes, d*mu_A->2, d*mu_C->5/2 gives ratio sqrt(5)/2. For two unit constraints reversed pivots have same trace/determinant. Independently reproduced all trace identities with symbolic exact algebra; finite tests not proof of open-interval classification.

## originality

PASS

The Bergamaschi 2026 primary text establishes exact forward Schur pivots and symmetric preconditioning, not a cross-permutation spectral-radius theorem. Wang 2024 uses an approximate triangular preconditioner in a different boundary-control model; published broader saddle-point preconditioner results may contain an equivalent ordering lemma.

## value

PASS

Identifies the smallest number of scalar constraints where order matters and a sharp, strictly worse least-correlation heuristic for a natural sequential preconditioner, including a limiting penalty; no claim about solver runtime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
