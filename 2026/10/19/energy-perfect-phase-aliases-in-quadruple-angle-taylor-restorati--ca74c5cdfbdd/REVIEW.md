# Scientific review: energy-perfect quadrupling aliases

## Correctness — PASS

The recurrence for normalized oscillator cosine and sinc yields exactly \(D_{j+1}=4C_j^2D_j\) by expansion. Chebyshev composition follows from \(T_2(t)=2t^2-1\). Inverting the cosine Taylor seed near zero constructs a unique small positive \(x_s\) at every sufficiently large scale, and the odd resonant index makes \(C_{s-1}=0\), forcing the computed rotation to be \(-I_2\). Taylor inversion gives the signed asymptotic phase discrepancy of \(\pi\); the exact rotation therefore tends to \(I_2\). The omitted Taylor remainders establish vanishing seed errors. For \(m=1\) the factorization of \(D_0\) and all simple Chebyshev zeros yield a complete distinct-positive-root enumeration. Algebraicity of the inputs and transcendence of \(\pi\) exclude true-phase coincidence. The embedded checker passed 11,669 deterministic assertions, corroborating but not replacing the proof.

## Originality — PASS, with explicitly retained risk

The precise comparison is with the error-controlled Taylor/quadrupling algorithm of Li–Wang–Zhang (arXiv:2406.06008v1, Sections 1–3), the trigonometric Taylor/Chebyshev recovery algorithm of Al-Mohy (arXiv:1708.08360v1, Sections 1–3), and the older ARKN/ERKN implementation by Shi–Wu–Liu (DOI:10.1016/j.apnum.2019.12.014, abstract and citation only). The first two sources already establish the recurrences, Chebyshev recovery and forward-error safeguards. They do not in inspected material state the exact energy-defect product, the \(2^s\) positive false-certificate census, or the deliberately overscaled all-degree maximal-error construction. The earlier Shi–Wu–Liu full text was not inspected, so an equivalent specialized result there or in unindexed literature remains possible. Existing general statements that energy does not imply phase accuracy are strictly weaker than the new specific quantitative classification and asymptotic construction. Related indexed statements on energy-projected Runge–Kutta oscillators concern different algorithms and do not imply this result.

## Value — PASS

The precise scientific gap is whether a zero normalized oscillator energy defect can certify correct matrix-function phase after a Taylor/quadruple restoration. The full degree-one root census shows not just an isolated failure but every exact false certificate; the all-degree scaling construction proves that an arbitrarily small seed error may coexist with the largest possible recovered-phase error. This motivates distinguishing energy diagnostics from rigorous propagated forward-error bounds when using oscillatory matrix functions. It is a theoretical stress test of freely chosen parameters, not evidence that a well-controlled implementation fails in normal operation.

## Boundaries and outstanding risks

All recurrences are in exact arithmetic. The upper-end error is asymptotic and fixed-degree scaling is deliberately excessive. The forward-error-controlled choice in the motivating method is not accused of producing this sequence. The inaccessible full text of the cited older ARKN/ERKN paper is an originality residual risk; no independent priority audit was performed.

Self-review: passed. Independent audit: not yet performed.
