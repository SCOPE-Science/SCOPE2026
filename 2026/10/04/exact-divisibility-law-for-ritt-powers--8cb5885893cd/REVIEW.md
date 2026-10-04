# Review: Exact divisibility law for Ritt powers

## Correctness
**PASS.** If one power \(T^N\) is Ritt, then \(T\) is power bounded. Spectral mapping forces every peripheral spectral point of \(T\) to be an \(N\)-th root of unity, so the least common multiple \(d\) of their orders is finite and divides \(N\). For \(S=T^d\) and \(a=N/d\), the polynomial \(Q_a(z)=1+z+\cdots+z^{a-1}\) has no zero on \(\sigma(S)\), hence \(Q_a(S)\) is invertible. Factoring \(I-S^a=(I-S)Q_a(S)\) transfers the Ritt discrete-derivative estimate from \(S^a\) to \(S\). Necessity follows from peripheral spectral mapping, and positive powers preserve the Ritt property.

## Originality
**PASS, with a stated residual literature risk.** The focal 2026 paper provides universal exponents arising from displacement bounds and finite root-of-unity peripheral spectra, but the inspected statements do not classify all Ritt exponents for one fixed operator. The 2022/2025 finite-peripheral-spectrum paper develops Ritt\(_E\) theory and the relevant derivative characterization, but the inspected definitions, Theorem 2.10, and power-related passages do not state the exact set \(d\mathbb N_{\ge1}\). Meaning-based published-record searches for the exact divisibility, least-exponent, root-of-unity, and \(\gcd\) formulations returned no covering result. The remaining risk is an older equivalent lemma under different terminology.

## Value
**PASS.** Badea's work makes the existence and choice of Ritt powers a central structural issue. The present theorem turns existence of one Ritt power into a complete arithmetic classification, identifies a canonical operator-specific Ritt period from the peripheral spectrum, and yields the non-obvious \(\gcd\)-closure consequence. It sharpens a universal-exponent viewpoint to an exact fixed-operator invariant without extra geometric hypotheses.

## Closest literature and limitations
The closest sources are arXiv:2609.27458v1, which studies powers forced to be Ritt from displacement hypotheses, and arXiv:2203.05373v2, which develops Ritt\(_E\) operators for finite peripheral spectra. The theorem assumes existence of a Ritt power, is formulated over complex Banach spaces, and does not optimize quantitative Ritt constants.

Same-model review: passed. Independent audit: not yet performed.
