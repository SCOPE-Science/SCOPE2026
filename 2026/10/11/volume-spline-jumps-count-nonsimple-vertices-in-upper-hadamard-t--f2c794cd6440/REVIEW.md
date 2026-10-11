# Same-model review

## Correctness
PASS. The proof starts from the published upper-regime affine chart, in which the polytope is a cube with \(d+1\) pairwise disjoint corner caps. Inclusion-exclusion gives the exact cap volume, and differentiating the resulting positive-part spline gives the stated jump. Independently, Hamming-layer and edge counts give the complete vertex profile. At resonance the published tangent cone has \(d+1\) irredundant facets; its extreme rays give degree \((j+1)(d-j)\). The two independent exact counts coincide as claimed. No finite enumeration is used to establish the universal theorem.

## Originality
PASS. The closest source, arXiv:2609.32950v1, contains the separated-corner representation, resonance set, and local nonsimple cone, but not the volume spline, full vertex-count profile, resonance degree, or jump-count identity. The direct Santos predecessor contains the Hadamard/Hamming geometry but not these truncation formulas. Targeted searches using the family name, resonance ratios, volume-spline aliases, vertex counts, and derivative-jump wording found no checked source covering the complete statement. The classical one-cap inclusion-exclusion formula is explicitly treated as background rather than as original content.

Residual originality risk remains that a general polyhedral-spline treatment not indexed under Hadamard terminology could imply part of the theorem. No checked comparison produced such a covering result.

## Value
PASS. The theorem identifies every upper smoothness resonance simultaneously by an analytic singularity and by an exact combinatorial singularity count, with the striking equality
\[
\left|[V^{(d)}]_{m_j}\right|=(d+1)\binom{d}{j}.
\]
It also gives the complete upper-regime vertex-count phase diagram and the exact degree of each nonsimple resonance vertex. These are natural invariants of the same family for which smoothness and normality are being studied and expose structure not visible from the smooth/non-smooth dichotomy alone.

## Closest literature and limitations
The lead 2026 paper proves the separated-corner geometry and smoothness classification used as premises. Santos's 2007 report is the direct constructional predecessor. The present theorem is restricted to the strict separated upper regime and does not claim lower-regime formulas, normality consequences, or Ehrhart consequences. The originality assessment is limited to the checked literature and indexed comparisons.

Same-model review: passed. Independent audit: not yet performed.
