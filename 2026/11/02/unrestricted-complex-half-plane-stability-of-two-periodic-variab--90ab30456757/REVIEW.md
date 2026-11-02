# Scientific review

## Correctness — PASS

The two-step recurrence and period matrix are reconstructed from the stated standard variable-step BDF2 coefficients. Symbolic multiplication proves the monodromy determinant and trace; the Schur–Cohn criterion is reduced to an explicit sum-of-nonnegative-terms certificate \(FG>0\) for all \(\operatorname{Re}z\ge0\), \(z\ne0\) and \(r>0\). The zero-frequency semisimplicity and both asymptotic limits follow by factoring the polynomial. The proof is complete for precisely alternating steps and the scalar constant-coefficient equation, not for arbitrary meshes.

## Originality — PASS within inspected evidence

The source introduces an adaptive SSAV-vBDF2 method and uses the classical ratio restriction in convergence analysis. Li–Liao prove arbitrary-grid stability in a different small-maximum-step perturbation sense; Akrivis and coauthors obtain bounded-ratio parabolic estimates. Neither inspected full text states the unconditional complex-half-plane two-period Floquet law or its singular Crank–Nicolson limit. The earlier Bourgault–Garon deferred-correction article could not be fully inspected and remains a concrete priority risk; the accessible abstract does not decisively imply the present result. No exhaustive uniqueness claim or independent literature certification is made.

## Mathematical value — PASS

The exact product stability theorem reveals a nontrivial and natural structural exception to a familiar general-grid ratio restriction, relevant to the stability assessment of strongly oscillating adaptive step sequences. Its complex Schur factorization supplies an infinite-parameter proof and its Crank–Nicolson singular limit distinguishes strict per-ratio damping from uniform damping, a numerically meaningful boundary. It is not merely a renamed constant-step theorem.

## Limits and closest sources

The claim does not apply to arbitrary variable meshes, the nonlinear auxiliary variable coupling, or global adaptive error constants. Closest inspected scientific literature: Shergill–Williams arXiv:2610.30454v1, Li–Liao arXiv:2201.00527v1, Akrivis et al. doi:10.1007/s10543-024-01007-y; Bourgault–Garon doi:10.1007/s10543-022-00931-1 abstract only. Independent audit and exhaustive historical-priority confirmation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
