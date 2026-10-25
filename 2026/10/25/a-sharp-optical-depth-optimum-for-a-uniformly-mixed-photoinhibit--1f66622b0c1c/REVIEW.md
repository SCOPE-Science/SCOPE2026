# Mathematical review

## Correctness

**PASS.** The exact Beer-depth integral follows by substituting exponentially declining dimensionless irradiance in Steele's light response. The derivative's sign is governed by a running-mean comparison. Its derivative changes sign only at \(t=\log q\), yielding the unique optimizer for \(q>1\) and the strict zero-optimum regime for \(q\le1\). At the root, both partial derivatives of the implicit equation have definite signs, proving strict monotonicity. Uniform Taylor expansion and the implicit-function theorem give the onset coefficient \(3/2\), while the boundary-irradiance equation gives the \(\log q+\log\log q\) scale. Direct quadrature and sign tests in `verify.py` reproduce these formulas; finite checks do not certify the infinite theorem.

## Originality

**PASS, with residual literature risk.** Steele (1962) provides the photoinhibition relation, not this attenuation optimizer. Bannister (1974, equation (20)) provides a closely related integrated-production formula, so the formula alone is not novel and has not been claimed as such. His inspected analytic discussion does not state the exact optimization boundary, its strict all-parameter monotonicity, or the two asymptotic laws. Walsby (1997) addresses numerical time-and-depth integration under complex conditions. The close Idso–Foster (1975) full text and Murphy (1962) full text were inaccessible; their abstracts cannot justify exclusion of stronger results. No identified published mathematical record explicitly covers the full claim, but the unresolved primary comparisons and possible general unimodal-running-mean theorem are real residual risks; no historical uniqueness is certified.

## Mathematical value

**PASS.** A finite, fixed-depth system is not optimized by maximizing total light penetration when the response curve inhibits production at high irradiance. The exact critical surface-light threshold, a unique interior optimum, globally monotone optimizer, and nontrivial double-logarithmic intense-light law give a complete and reproducible dimensionless design classification. These answer an ecologically motivated conditional question rather than choosing an arbitrary finite sample. The result is limited to frozen physiology, an externally variable attenuation coefficient, uniform depth biomass and a fixed instantaneous objective; it does not claim broad ecosystem management optimality.

## References and unresolved risks

Closest fully inspected works: Steele (1962), Bannister (1974), Walsby (1997). Closest unresolved full-text sources: Idso–Foster (1975), Murphy (1962). The latter literature may contain an implied comparison; stronger general averaging theory may imply the mathematical core. No external mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
