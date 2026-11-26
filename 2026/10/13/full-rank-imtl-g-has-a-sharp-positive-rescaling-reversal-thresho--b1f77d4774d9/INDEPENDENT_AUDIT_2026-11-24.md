# Independent mathematical audit

## correctness

PASS

Reconstruct the normalized method with U the matrix of unit-gradient columns, B=UᵀU, and n_i=||g_i||. Full column rank makes B positive definite. The equal-projection equations are B diag(n_i k_i) α'=C'1, before imposing the sum-one condition. Thus every equal-projection coefficient vector at the new scale is a scalar multiple of (α_i/k_i)_i, since the original C is nonzero (otherwise α=0). The normalization gives the unique multiplier 1/D when D=Σα_i/k_i≠0; at D=0 there is no sum-one solution, not just a numerical failure. Nonnegative weights force D>0; one negative α_j gives the strictly increasing D(k)=1−α_j+α_j/k with the stated unique root and opposite signs on either side. In the example det(U)=r²(r−1) with r=1/√2 and the scaled gradient determinant is k times this. The displayed coefficients sum to one and give (0,0,r) and common projection 1/2. The third-scale denominator is 2+√2−(1+√2)/k, with simple zero at r and negative sign below r. Each scaled objective's derivative along −g' is −k_i n_i/(2D)>0 there. This is an algebraic reconstruction (replay via the Gram equation and these exact identities), not execution of the uploaded checker. It proves an instantaneous statement for the sum-one normalization, not a training trajectory.

## originality

PASS

The multiplier itself and the threshold algebra conditional on a negative coefficient are direct consequences of known scaling formulas, not a separate originality claim. The supported contribution is the admissible full-rank three-task witness to a positive-scale singularity and an actual orientation reversal with all tasks in first-order ascent. The strongest inspected literature reproduces the normalization and even considers conflict, but supplies a rank-deficient example, not this full-rank boundary and reversal.

## value

PASS

Positive changes of objective units are a central invariance test for a multi-task aggregator. A legal full-rank example distinguishes preservation of a line from preservation of a directed descent step: a finite singularity is followed by ascent for every task, with the exact scale separating those regimes. This supplies a concrete diagnostic for normalization design without claiming instability of a whole training run.

The dated certificate retains the supplied scientific assessment, sources and limitations.
