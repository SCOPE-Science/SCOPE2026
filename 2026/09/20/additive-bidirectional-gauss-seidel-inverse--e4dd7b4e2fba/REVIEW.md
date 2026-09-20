# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The central factorization follows by multiplying the proposed inverse on both sides by the forward triangular factor. After block-diagonal scaling it is a congruence of \(I-C^TC\), giving the exact positive-definiteness threshold \(\|C\|_2<1\). Under this threshold, the inverse formula yields \(\widetilde B^{-1}-H\succeq0\), which places the preconditioned spectrum in \((0,1]\). The exact identity
\[
\widetilde BH-I=-XCC^T-X^TC^TC,
\qquad X=(I+C)^{-1},
\]
gives the stated \(2\delta^2/(1-\delta)\) norm bound and the condition-number estimate for \(\delta<1/2\). The affine-family uniqueness calculation is a direct first-order expansion. The two-block spectrum follows by \(C^2=0\). The rational 3-by-3 example has positive leading principal minors for \(A\) but \(\det B<0\), so it correctly separates SPD of \(A\) from SPD of the additive inverse.

Independent numerical checks in the accompanying compact artifact reproduce the factorization and error identity to floating-point precision, verify inverse dominance and the spectral bounds for a deterministic weak-coupling example, evaluate the rational counterexample, and confirm the two-block identity.

## Originality

**PASS, to the best of our knowledge, with residual literature risk.** Classical forward, backward and symmetric Gauss-Seidel, SSOR, extrapolated Gauss-Seidel, additive/multiplicative splitting theory, and parallel variants are longstanding. The search therefore targeted both terminology and algebraic equivalents rather than the proposed name alone.

The checked literature includes Koliha's 1972 treatment of accelerated stationary methods, the abstract-level statements of Evans--Li--Xue (1987) on extrapolated GS and Evans--Li (1988) on a symmetric extrapolated method, Bai's 2003 additive/multiplicative splitting framework, standard modern preconditioner surveys, and recent additive/multiplicative smoother work. Standard symmetric Gauss-Seidel is the multiplicative inverse \((D+L^T)^{-1}D(D+L)^{-1}\), not the diagonal-corrected additive inverse studied here.

Targeted searches did not locate the conjunction of (i) \((D+L)^{-1}+(D+L^T)^{-1}-D^{-1}\), (ii) the congruence factorization through \(D-L^TD^{-1}L\), (iii) the iff SPD threshold \(\|D^{-1/2}LD^{-1/2}\|_2<1\), (iv) an SPD-system counterexample beyond that threshold, and (v) the quadratic weak-coupling spectral bound. No novelty is claimed for generic extrapolation, additive splitting, polynomial preconditioning, or forward/backward symmetrization itself.

The full texts of Evans--Li--Xue (1987), Evans--Li (1988), and Bai (2003) were not inspected end-to-end; these are the most plausible sources that could contain an equivalent construction or a stronger theorem. Only abstract-level information was inspected for Saye (2026). These limitations leave a real but presently unresolved originality risk.

## Value

**PASS.** The result identifies a simple additive alternative to the usual multiplicative symmetric Gauss-Seidel inverse and gives a complete safety boundary rather than an unconditional heuristic. The same algebra explains both its attraction and its failure mode: subtracting the diagonal inverse uniquely cancels first-order coupling error in the natural symmetric affine family, giving quadratic weak-coupling clustering, but the correction can cross an exact positivity threshold. The explicit counterexample prevents unsafe use based only on SPD of the original system. The two-block corollary gives an exactly solvable regime in which the method has no extra positivity restriction and its spectrum is determined directly by singular values of the off-diagonal coupling.

## Scientific limitations

- Finite-dimensional real SPD setting with a fixed SPD block diagonal split.
- Positive definiteness of the proposed inverse requires the stated spectral-norm certificate; the original matrix being SPD is insufficient.
- The condition-number bound is worst-case and weak-coupling; it is not a practical performance guarantee.
- No floating-point stability, communication, scalability, or performance theorem is established.
- Standard SGS is unconditionally SPD for SPD block diagonal \(D\), so the additive construction is not a universal replacement.
- The most relevant inaccessible historical sources listed above could reduce or eliminate the originality claim if they contain an equivalent formula and analysis.
