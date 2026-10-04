# Review: Exact singularity criterion for three-point principal Fourier minors

## Correctness
**PASS.** After translation to \(K=\{0,a,b\}\), the determinant is exactly
\[
(\omega^{a^2}-1)(\omega^{b^2}-1)-(\omega^{ab}-1)^2.
\]
The proof separates \(N\mid ab\) from \(N\nmid ab\). In the first case, vanishing is exactly \(N\mid a^2\) or \(N\mid b^2\). In the second, the phase identity forces \(N\mid(b-a)^2\), after which the determinant factors as \(-X(R-1)^2\), giving exactly \(N\mid a(b-a)\). No implication is inferred from finite testing. The order-coset and valuation formulations follow algebraically from the same divisibilities. The packaged exact verifier independently checks all normalized triples for \(3\le N\le120\).

Risk: the only mathematical risk identified is an algebraic transcription error; replay of the exact cyclotomic verifier and direct reconstruction of the factorization found none.

## Originality
**PASS.** Tao and Frenkel cover prime-order all-minor nonvanishing. Caragea--Lee is the closest inspected source: it proves nonvanishing of all \(3\times3\) principal minors for square-free \(N\), and existence of zero principal minors for nonsquare-free \(N\). Its \(3\times3\) proof contains the same initial determinant identity and a necessary square-divisibility step, but the inspected theorem and proof do not state the exact local iff condition for each triple, the cross-divisibility condition, or the additive-order/coset characterization. Searches for those equivalent formulations did not locate a matching statement.

Risk: a local classification may exist under different terminology or outside the inspected indexed literature. This residual risk does not create an unresolved implication from a known stronger result.

## Value
**PASS.** The result closes a natural local classification problem left open by the global square-free/nonsquare-free dichotomy: it tells exactly which individual three-point principal Fourier submatrices fail, not merely whether some failure exists. The additive-order formulation exposes the square-divisor mechanism geometrically and gives an immediate arithmetic filter for singular triples. It also explains why nonsquare-free moduli can contain many nonsingular triples even though a singular triple exists globally.

Risk: the result is intentionally limited to order three and does not address the harder larger-minor problem.

Same-model review: passed. Independent audit: not yet performed.
