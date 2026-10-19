# Review of the letter-dilation BWT run-head theorem

## Correctness

**PASS.** The proof classifies every cyclic rotation uniquely by the containing circular maximal run and the remaining length of its first constant-symbol block. Comparisons split into lower-following and higher-following rows. Fixed-length ties are ordered by post-run cyclic continuations; the order is invariant under positive symbolwise powers. Exactly one predecessor of each maximal run can differ from the starting character, generating a fixed exceptional block at each multiple of the dilation exponent. Every intervening filler has positive length when all exponents are at least two, giving equality of run-label sequences. The proof treats periodic ties, circular boundaries, multi-symbol alphabets, and monochromatic words. Direct-sorting and independent suffix-doubling computational checks corroborate the whole BWT formula on the stated finite ranges. No infinite assertion depends on finite testing.

## Originality

**PASS against the inspected sources and retrieved records, with residual uncertainty.** The 1994 original BWT report defines cyclic sorting but does not analyze letter-exponent rigidity. Mantaci et al. (2017), especially Proposition 3.9, prove nondecrease under a one-letter expansion, not equality after all letters have been duplicated; their global twofold bound is likewise insufficient. Frosini et al. (2022) establish asymptotic estimates for finite iterates of morphisms, not an exact all-parent all-alphabet run-head formula. Published-record queries for letter dilations, stuttering morphisms, and run-length invariance and comparisons to accessible related exact BWT findings disclosed no equivalent statement. A differently named or unindexed earlier characterization could still exist; this is not an independence certification.

## Mathematical value

**PASS.** BWT run count is a standard invariant of run-length compressed indexing. The theorem supplies a natural complete structural classification of how this invariant—and the stronger ordered run-head word—behaves under a broad family of input morphisms. The independent exponent parameters, all finite ordered alphabets, nonprimitive inputs, exact decomposition, and sharp threshold give content beyond the known monotonicity and rough bounds. It is neither a finite census nor a parameter substitution into a known identity.

## Scientific scope and risks

The result concerns the sentinel-free cyclic transform, not suffix-BWT or bijective variants. Source comparison was based on the complete publicly accessible 1994 report, the 2017 lawful full postprint (including its expansion proposition), the 2022 full arXiv manuscript, published bibliographic searches, and the directly compared accessible related claims. Residual originality risk is chiefly an unindexed equivalent formulation; no claim of independent review or exhaustive literature coverage is made.

Self-review: passed. Independent audit: not yet performed.
