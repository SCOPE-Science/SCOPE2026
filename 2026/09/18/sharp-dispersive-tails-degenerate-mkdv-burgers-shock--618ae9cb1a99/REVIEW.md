# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The argument starts from the source profile equation
\[
(U-s)^2(U+2s)=\mu U'-\kappa U''
\]
and treats the two spatial ends separately. At the upstream state, linearization gives the exact characteristic polynomial \(\kappa\lambda^2-\mu\lambda+9s^2\). In the strict monotone regime its two roots are positive and distinct. The source derivative estimate, after the standard \(\mu\)-scaling, bounds the normalized logarithmic slope by a quantity tending to 18; the fast root is strictly larger than 18, so the heteroclinic cannot approach solely along the fast eigendirection. This selects the slow root and yields the sharp exponential rate.

At the monotonicity boundary the characteristic polynomial has a repeated root and the profile equation factors as \(\kappa(D-\Lambda_c)^2q=q^2(6s-q)\). The transformed amplitude \(r=e^{-\Lambda_c\xi}q\) satisfies \(r''>0\), while the source derivative inequality gives \(r'<0\). The ordinary Jordan asymptotic therefore cannot have vanishing generalized-eigenvector coefficient: if it did, \(r'\to0\) at the upstream end, and integration of \(r''>0\) would force \(r'>0\). This establishes the factor \((-\xi)e^{\Lambda_c\xi}\) with positive amplitude.

At the downstream contact state, writing \(y=s-U\) and \(v=U'\) gives the exact scalar center-manifold equation \(\kappa v v_y+\mu v=3sy^2-y^3\). Coefficient matching yields \(v=(3s/\mu)y^2-(\mu^2+18\kappa s^2)\mu^{-3}y^3+O(y^4)\). For \(X=1/y\), one then obtains \(X'=3s/\mu-(1/\mu+18\kappa s^2/\mu^3)X^{-1}+O(X^{-2})\), and one iteration followed by integration produces the stated logarithmic term. Translating \(\xi\) changes only the constant term, not the logarithmic coefficient.

The algebraic coefficients, upstream roots and critical factorization were independently re-derived within the review and checked by the accompanying symbolic script. Useful sign and limiting checks also pass: as \(\kappa\downarrow0\), the upstream rate tends to \(9s^2/\mu\), while the reciprocal-tail logarithmic coefficient reduces to the purely viscous value \(1/(3s)\); at \(36\kappa s^2=\mu^2\), the two upstream roots coalesce at \(18s^2/\mu\). The symbolic computation is supportive evidence only and is not independent validation.

## Originality

**PASS, to the best of our knowledge.** The full HTML of arXiv:2609.20591v1 was inspected, including Theorem 2.1, the integrated travelling-wave equation and the phase-plane discussion. The source proves dispersion-uniform two-sided bounds and states that the shock has the same exponential/algebraic decay scales as the purely viscous profile. It does not state the exact dispersion-dependent upstream root, the polynomial-times-exponential critical tail, the downstream logarithmic correction, or the translation-invariant recovery formulas for \(\kappa\).

Searches covered the exact source title and arXiv identifier together with terms such as sharp asymptotics, logarithmic tail/correction, degenerate shock, repeated spatial root, Jordan tail, contact tail, and modified KdV-Burgers travelling wave. Repository searches by the source identifier and equivalent mathematical terminology found no existing SCOPE record. No source-specific correction or comment containing these conclusions was located.

The closest older reference is Jacobs–McKinney–Shearer, *Travelling wave solutions of the modified Korteweg-de Vries-Burgers equation*, J. Differential Equations 116 (1995), 448–467. Its full text was not inspected, so it is the principal residual originality risk: an equivalent endpoint expansion could conceivably appear there under different terminology. Later accessible sources were also checked for context. Dodd (2007) describes the Jacobs–McKinney–Shearer work as a classification of mKdV-Burgers travelling waves and focuses on explicit undercompressive profiles and their spectral stability; El–Hoefer–Shearer (2017) surveys diffusive-dispersive shock classification. No inspected source exposed the degenerate Oleinik logarithmic contact-tail expansion or the critical Jordan asymptotic stated here.

The originality claim therefore excludes the travelling-wave reduction, phase-plane classification, characteristic-root calculation as a general technique, Jordan-block asymptotics, center-manifold expansions, and all existence/monotonicity results from the source paper. It is restricted to the source-specific sharp tail theorem and its translation-invariant dispersion fingerprints, with the strongest novelty weight placed on the downstream logarithmic coefficient and the critical-threshold tail.

## Value

**PASS.** The result separates coarse decay scale from sharp asymptotic structure in a profile that is central to the source stability theorem. The source estimates are deliberately uniform in dispersion, whereas the exact upstream exponent varies substantially across the monotone regime and the boundary develops a distinct Jordan factor. At the contact end, dispersion first appears in a universal logarithmic correction rather than in the leading \(1/\xi\) term. This identifies precisely where dispersive information is hidden by the uniform bounds and supplies two translation-invariant ways to recover \(\kappa\) from a profile tail.

## Limitations

The theorem concerns only the monotone degenerate Oleinik shock joining \(-2s\) to \(s\) for \(36\kappa s^2\le\mu^2\). It does not cover oscillatory profiles beyond the monotone regime, nondegenerate or undercompressive shocks, or nonlinear convergence rates of time-dependent solutions toward the profile. The amplitudes and constant terms in the tail expansions depend on translation. The 1995 Jacobs–McKinney–Shearer full text remains the most important unresolved literature-access risk for originality.
