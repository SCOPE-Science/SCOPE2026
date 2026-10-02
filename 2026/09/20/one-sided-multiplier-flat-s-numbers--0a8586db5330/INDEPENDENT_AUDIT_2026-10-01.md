# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-0a8586db5330`

## Correctness — PASS

The rank-one witness argument is valid on every normalized symmetrically normed Banach ideal of compact operators. An essential spectral tail of one coefficient supplies an infinite-dimensional Hilbert subspace on which that coefficient is uniformly bounded below, while a near-norming vector for the other coefficient gives a rank-one column or row subspace. The input and output witnesses are contractively complemented. This yields the approximation, Bernstein, Gelfand, and Kolmogorov lower bounds and the strict-singularity-distance bounds. If one coefficient is compact, finite-rank approximation on both sides gives the matching compact-distance upper bound and the common asymptotic s-number limit. For one-sided multiplication, the lower bound equals the operator norm, forcing every one of the four s-numbers and all three ideal distances to be exactly flat.

### Correctness sources

- assigned RESULT.md
- Lindström–Saksman–Tylli 2005 full primary paper
- current published elementary-operator rank-one witness theorem

### Correctness risks

- For two noncompact coefficients the displayed essential-norm quantity is only a universal lower bound.
- The theorem is for Banach norm ideals, not quasi-Banach Schatten classes below one.

## Originality — PASS

Qualitative compactness and strict-singularity results are prior and are excluded from novelty. A highly relevant current theorem proves that every noncompact finite elementary operator is bounded below on some complemented rank-one Hilbertian subspace, so the existence of some positive lower witness is now covered. That theorem does not determine the witness constant in terms of coefficient norm and essential norm and does not imply the audited exact one-sided all-index profile, exact distances, or one-compact-factor asymptotics. The 2005 primary paper treats strict singularity/cosingularity of multiplication on full operator spaces and analogous qualitative restrictions, not these exact s-number constants.

### equivalent_formulations

Searches:
- Resultary query: flat classical s-number profiles one-sided multiplication symmetrically normed Banach ideals compact strictly singular approximation Bernstein Gelfand Kolmogorov
- Lindström–Saksman–Tylli 2005 full paper
- current SCOPE result strictly-singular-elementary-operators-are-compact

Evidence:
- The current elementary-operator theorem covers qualitative compact=FSS=SS and existence of a rank-one witness with unspecified constant.
- The audited theorem fixes exact constants and all four classical s-number profiles for one-sided multiplication.

Reasoning:
Equivalent formulations through s-number flatness, essential-norm lower bounds, distances to compact/FSS/SS, and rank-one complemented witnesses were compared.

### broader_coverage

Searches:
- current SCOPE finite-elementary-operator theorem
- Mathieu–Tradacete 2020
- Fialkow–Loebl elementary-operator literature

Evidence:
- The current broader class theorem is qualitatively stronger in operator class but quantitatively weaker: it gives some witness constant rather than the audited sharp coefficient-dependent floor.
- The older literature is centered on compactness, strict singularity, or mappings into ideals.

Reasoning:
Broader operator-class coverage does not mechanically supply the numerical s-number profile.

### exact_database_or_table

Searches:
- current Resultary operator-ideal records
- classical s-number literature searches

Evidence:
- No exact table/database gives these all-index constants for the stated multiplier class.

Reasoning:
The invariants are operator-theoretic formulas, not database values.

### claim_vs_prior_implication

Searches:
- qualitative noncompact witness theorem versus exact one-sided profile
- compactness criteria versus exact metric distances

Evidence:
- Knowing only that a noncompact multiplier is bounded below somewhere yields an unspecified positive Bernstein lower bound, not equality of four s-number sequences with the operator norm.
- Compactness equivalence does not determine distance to compact/FSS/SS or the compact-factor asymptotic constants.

Reasoning:
The quantitative final claim survives the located qualitative coverage.

### source_inspections

- **Strictly Singular and Cosingular Multiplications** — https://doi.org/10.4153/CJM-2005-050-7. Trigger: Primary prior art for strict singularity of multiplication operators. Material read: Complete thirty-page Cambridge PDF, including the basic facts and examples for multiplication and compact-operator restrictions. Method: Primary full-text statement comparison. Assessment: Qualitative prior art, not quantitative coverage. Evidence: The paper studies strict singularity/cosingularity on full operator spaces and related restrictions without the audited four-s-number formulas.
- **Strict singularity collapses to compactness for finite elementary operators on norm ideals** — https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-strictly-singular-elementary-operators-are-compact--47524bf7e824. Trigger: Highly relevant current broader-class theorem. Material read: Complete published RESULT.md. Method: Full theorem and proof implication comparison. Assessment: PARTIAL COVERAGE only. Evidence: It proves qualitative collapse and existence of a complemented rank-one lower witness with some constant, but not the exact coefficient-norm floors or all-index flat profiles.
- **Strictly singular multiplication operators on L(X)** — https://doi.org/10.1007/s11856-020-1985-0. Trigger: Modern neighboring strict-singularity literature. Material read: Accessible bibliographic/theorem scope. Method: Scope comparison. Assessment: Not covering the exact norm-ideal s-number formulas. Evidence: Its ambient object is multiplication on full operator algebras for Banach spaces.

### checked_sources

- Lindström–Saksman–Tylli 2005 full PDF
- current Resultary exact s-number search
- current finite-elementary-operator theorem
- Mathieu–Tradacete 2020
- assigned RESULT.md

### residual_risks

- Older elementary-operator and norm-ideal literature is extensive; an exact s-number identity under older terminology remains possible.
- The 1984 Fialkow–Loebl paper was not exhaustively read in this run.

## Scientific value — PASS

The all-index equality of four classical s-number scales and exact distances to three operator ideals is a natural quantitative invariant, not merely a compactness test. The theorem gives sharp information uniformly across all normalized symmetric Banach norm ideals and a reusable coefficient-dependent lower floor for two-sided multiplication.

### Value sources

- audited quantitative theorem
- qualitative finite-elementary-operator rank-one witness theorem
- classical multiplication compactness literature

### Value risks

- The qualitative compactness/strict-singularity equivalence itself is not claimed as new.

## Limitations

- The exact flatness theorem is for one-sided multipliers on normalized symmetrically normed Banach ideals.
- For two noncompact coefficients only a lower bound is claimed.
- Quasi-Banach ideals and infinite elementary sums are outside scope.
- Originality is best-of-knowledge for the quantitative formulas.

## Disposition

**PASSED**
