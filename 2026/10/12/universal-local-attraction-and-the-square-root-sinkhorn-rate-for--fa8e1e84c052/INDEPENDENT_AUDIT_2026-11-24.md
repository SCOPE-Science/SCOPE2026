# Independent mathematical audit

## correctness

PASS

The cumulative-factor update cancels the old row scaling and gives y=(q^k)^2/q^{k−1}, p_new=r/(My) and q_new=S_M(y); reconstruction from y is gauge invariant and exactly column feasible. In c-centered logarithmic coordinates the one-step derivative is J=D_c^−1 PᵀD_r^−1 P, self-adjoint in the c inner product and similar to WᵀW. It is nonnegative and stochastic; positivity makes the Perron eigenvalue 1 simple. The centered derivative has top eigenvalue s₂², with singular values read as square roots of eigenvalues of WᵀW (including zeros for wide W, and s₂=0 for the empty projective space). Each projective two-state block has polynomial λ²−2σλ+σ, where σ is a centered eigenvalue of J. This yields modulus √σ, also covering the zero nilpotent block. An equivalent norm and a sufficiently small invariant ball give every rate ρ∈(s₂,1). The reconstructed output differential is P_ij[(Jh)_j−(Ah)_i]; for a nonconstant top mode with σ>0 it cannot vanish, and its extrapolation multiplier 2λ−1 is nonzero. Complexifying a real uniform derivative bound therefore proves output and state sharpness. Rank-one M gives a constant projective map; the symmetric two-by-two family gives the advertised limiting rates. An independent exact test uses a positive rank-two 2×3 coupling, finds centered eigenvalues 0 and 19/504, and checks reconstruction, nonzero output differential and first-order response.

## originality

PASS

The recurrence itself and the standard Sinkhorn s₂² baseline are prior. The supported distinct finding is the all-positive-data BDRS local spectral radius s₂, with sharpness for reconstructed couplings and a quantitative distinction from both the sufficient global contraction condition and genuine overrelaxed Sinkhorn. General Euclidean DR angle theory supplies an analogous spectral mechanism, not a theorem for this nonlinear entropy-Bregman recurrence and its observed couplings. The closest inspected algorithmic and catalogue comparisons do not establish the stated result.

## value

PASS

The theorem resolves a natural local question for an established scaling method with genuine global counterexamples: every positive-data optimum is locally stable, yet stability can be arbitrarily slow. The exact exponent shows that this momentum is locally slower than ordinary Sinkhorn on non-rank-one instances, and the visibility check makes that conclusion applicable to the actual coupling rather than only to internal scaling coordinates. This separates local rate, global guarantees and algorithmic acceleration in a useful way.

The dated certificate retains the supplied scientific assessment, sources and limitations.
