# Independent audit — SCOPE-20260918-40d4eb3f4497

Audit date (UTC): 2026-10-01

## Final claim

In the three-oscillator straight-isochrone Stuart--Landau setting of Muolo--Nakao--Bick, the displayed globally phase-equivariant cubic counterterm contributes exactly the negative of the complete order-\(\varepsilon^2\) phase term, so the phase dynamics equal the first-order model through order \(\varepsilon^2\).

## Correctness

**PASS** — The tangent projection was independently re-derived: a resonant cubic monomial contributes \(a\,\mathrm{Im}(C e^{i(\theta_p+\theta_q-\theta_r-\theta_i)})\) on the radius-\(\sqrt a\) torus, and an order-\(\varepsilon^2\) physical term needs only this zeroth-order evaluation. Term-by-term substitution of the proposed counterterm reproduces the seven harmonic groups of the source second-order expression with opposite sign. A fresh randomized check over 1,000 parameter/phase draws and all three components gave maximum absolute residual below \(3\times10^{-15}\). The source full HTML was inspected: it explicitly asserts compensation is necessarily partial, while its general cubic formula permits the omitted pairwise choice yielding the second harmonic.

## Originality

**PASS** — The primary source enumerates two nonlinear pairwise cases and states that its engineered compensation is necessarily partial. Its own general resonant cubic formula allows the additional case with both unconjugated indices equal to the other oscillator and the conjugated index equal to the receiving oscillator; that case yields the required pairwise second harmonic. General synchronization-engineering papers establish harmonic shaping broadly but do not give this source-specific complete second-order counterterm. No prior exact counterterm for this displayed second-order triad formula was located.

### Equivalent formulations

Aliases, parameter normalizations, and source-specific formulations were compared by implication rather than by title similarity. Exact-title, exact-claim, alias, and primary-literature searches found no equivalent stronger statement beyond the qualifications below.

### Broader coverage

The closest general results and source theorems were inspected directly. General machinery that is prior art is excluded from the novelty claim; none of the inspected broader statements implies the final claim at the stated strength.

### Exact database or table

Finite computations and tables were treated as corroborative evidence only. They were not used to infer an infinite theorem or to establish novelty.

### Claim versus prior implication

The primary source enumerates two nonlinear pairwise cases and states that its engineered compensation is necessarily partial. Its own general resonant cubic formula allows the additional case with both unconjugated indices equal to the other oscillator and the conjugated index equal to the receiving oscillator; that case yields the required pairwise second harmonic. General synchronization-engineering papers establish harmonic shaping broadly but do not give this source-specific complete second-order counterterm. No prior exact counterterm for this displayed second-order triad formula was located.

## Value

**PASS** — The result corrects a concrete structural limitation claimed in a current phase-reduction paper and gives an explicit physical control direction that removes every second-order term in its benchmark triad. This is more than a generic observation that nonlinear feedback can shape harmonics, while remaining explicitly perturbative and source-specific.

## Sources inspected

- Physical and emergent nonpairwise interactions in oscillator networks — https://arxiv.org/html/2609.20632v1 — NOT_COVERING and directly motivates the correction: the paper claims partial cancellation and its two-case pairwise enumeration omits the second-harmonic case allowed by its own general cubic formula.
- Synchronization engineering: theoretical framework and application to dynamical clustering — https://doi.org/10.1063/1.2927531 — BACKGROUND: establishes nonlinear feedback for interaction-function design but does not imply the source-specific counterterm coefficients.
- Synchronization engineering: tuning the phase relationship between dissimilar oscillators using nonlinear feedback — https://doi.org/10.1098/rsta.2010.0032 — BACKGROUND: demonstrates phase-interaction engineering, not this second-order triad cancellation identity.

## Residual risks and limitations

- The statement is perturbative through order epsilon squared and does not bound the cubic-order remainder or establish laboratory realizability.
- The originality claim is restricted to the explicit source-specific counterterm and omitted resonant direction; general harmonic engineering is prior art.

## Disposition

**PASSED**
