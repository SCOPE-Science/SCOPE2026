# Independent Audit — 2026-09-29

**Record:** `2026/09/19/accelerated-filtration-entropy-growth-obstruction--f6a5a54dee7a`  
**Title:** Accelerated filtrations break entropy-growth detection  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The prescribed-entropy construction is correct: f_λ(n)=n+⌊e^{λn}−1⌋ is strictly increasing and superadditive, so degree cutoffs define a filtration, and the exact layer difference has logarithmic rate λ. The e^{n²} variant gives +∞ and the standard degree filtration gives 0. The universal-quantifier repair is also valid: if an affine algebra has exponential growth, zero entropy for any exhaustive finite-dimensional filtration would force subexponential cumulative dimensions and contradict containment of a finite generating space; conversely positive entropy of a standard filtration forces positive exponential rate because its cumulative dimensions are submultiplicative and hence have a limiting root rate.
- **Originality — PASS:** The 2024 defining paper already proves filtration dependence under linear reindexing and explicitly suggests—but does not establish—zero-entropy invariance. The September 2026 Schwarz–Sebandal paper still advertises the unrestricted entropy-to-growth framework. Searches did not locate the exact full spectrum [0,∞] on k[x], the nonlinear acceleration counterexample, or the “positive for every filtration” characterization before this record. The later same-day universal-acceleration record does not predate this one.
- **Scientific value — PASS:** A one-variable polynomial algebra realizes every extended nonnegative entropy while retaining intrinsic linear growth, directly exposing the missing hypothesis in a current preprint. The every-filtration equivalence is a sharp corrected intrinsic statement, and the linear-control condition explains when the intended one-filtration implication is safe.

## Independent checks

- Reproved superadditivity of f_λ including the floor inequality and squeezed the exact layer dimensions to rate λ.
- Checked the e^{n²} infinite-entropy variant and the [0,∞] spectrum claim.
- Re-derived both directions of the every-filtration/exponential-growth equivalence.
- Checked the linear-control repair against a standard generating filtration and confirmed the 2024 paper’s linear-reindexing prior art.

## Literature and evidence

- Bock et al., Algebraic Entropy of Path Algebras and Leavitt Path Algebras of Finite Graphs — Open full text states the filtration definition, proves linear reindexing multiplies entropy, and remarks that zero entropy might appear filtration-independent.
- Schwarz–Sebandal, Growth functions of algebras and an application to Leavitt path algebras — Current motivating preprint presents the broad growth/entropy framework that the nonlinear accelerated filtration separates from intrinsic growth.

## Limitations

- Concerns the specific filtered algebraic entropy of Bock et al.; not other notions called algebraic entropy.
- Does not challenge statements restricted to standard/natural filtrations or the standard-filtration Leavitt-path application.
- The primary Krause–Lenagan book proposition was not independently inspected; the counterexample and corrected theorem do not depend on that bibliographic point.

**Independent-audit disposition:** passed.
