# Same-model review — Pair-residual columns increase for separating hash families

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The construction was checked by a complete case split on how the special columns intersect the target classes.

If special columns occur in at most one target class, projecting them to the single source column can only reduce that class size. Because \(n\ge W\), there are enough unused source columns to pad back to the exact target type before invoking the original SHF.

If special columns occur in at least two target classes, choosing any two such classes reduces their ordinary-column requirements by at least one each. Their ordinary parts are therefore componentwise contained in a pair residual \(T_{ij}\), and there are enough unused ordinary columns to pad to that exact residual type. The bottom ingredient separates the padded residual classes. Distinct new symbols on the special columns are disjoint from the bottom alphabet and from one another, so they cannot create a cross-class collision.

The proof remains valid when a decremented part becomes zero, when more than two target classes contain special columns, and when several special columns occur in the same target class. The alphabet count is \((m-x)+x=m\).

Small explicit instances were also checked directly, including a two-class \(\{2,2\}\) construction and a three-class example; these checks are corroborative only and are not used in the proof.

## Originality

**PASS, to the best of our knowledge.**

The primary starting source was Zaverucha's 2010 Waterloo thesis, Section 3.1.2. The relevant theorem statements and surrounding discussion were inspected directly. The thesis gives:

- a reduced-type one-column construction for two-class SHFs (Theorem 3.13);
- an arbitrary-type one-column construction whose second ingredient retains the full type (Theorem 3.14), explicitly noting that the second ingredient is not of reduced strength;
- the Martirosyan--van Trung perfect-hash columns-increase recurrence with strength reduced by two (Theorem 3.15);
- an arbitrary-type multi-column construction with a full-type auxiliary (Theorem 3.16), followed by the observation that improvements should be possible for some parameters and types.

The same thesis later defines compound SHF types, which supplies standard language for the simultaneous pair-residual requirement used here.

Current-status searches checked exact and synonymous formulations around column increase/columns increase, reduced-strength SHF recurrences, perfect-hash recurrences, compound/distributing hash families, and frameproof-code formulations. Relevant later sources inspected or checked include Bazrafshan--van Trung (2011), Shangguan--Ge (2016), Colbourn--Dougherty--Horsley (2019), Rochanakul (2020), and Wei--Zhang--Ge (2025). No theorem matching the pair-residual arbitrary-type recurrence or the arbitrary-\(x\) reduced two-class specialization was located.

The perfect-hash specialization is known and is explicitly treated as recovery of Martirosyan--van Trung rather than as a new claim. The frameproof lifting is presented as a corollary and is not claimed to have a novel elementary proof.

Residual originality risk remains from differently named, unindexed, or inaccessible literature.

## Value

**PASS.** The theorem resolves a concrete structural deficiency identified in the 2010 source: arbitrary-type column increase can use an auxiliary whose constituent requirements all have total strength \(W-2\), rather than the original strength \(W\). It simultaneously explains why the known perfect-hash and two-class reductions work, extends the two-class reduced recurrence from \(x=2\) to arbitrary admissible \(x\), and yields explicit small-row corollaries such as the logarithmic auxiliary for type \(\{1,1,2\}\).

The contribution is structural rather than a universal parameter-record claim. A pair-residual compound family need not beat a full-type ingredient numerically in every regime.

## Search/access limitations

The originality assessment is literature-based rather than exhaustive. Several broad lines of later SHF, DHF, PHF, and frameproof-code work were checked, but absence from searches does not prove absence from all literature. No inaccessible source produced concrete evidence of coverage; nevertheless, equivalent formulations under other recursive-construction terminology remain the main originality risk.

## Conclusion

Correctness: **PASS**  
Originality: **PASS (to the best of our knowledge)**  
Value: **PASS**

Same-model review: passed. Independent audit: not yet performed.
