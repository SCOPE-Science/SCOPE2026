# Independent mathematical audit

## correctness

PASS

Original RESULT.md is FALSE for permitted g<0: normalized input G/sqrt(v) has factor sign(g), absent from its boxed clipped update, momentum, residual and final D. Independent direct matrix recurrence with g=+2 and g=-2 across 17 steps confirms the sign discrepancy. A complete final RESULT.md and SLOGAN.txt restore s=sign(g) in all four signed directions while preserving the squared confidence h_t and RMS formulas. The revised proof reconstructs both row-column factorizations, clipping at d=1, scalar EMA states, exact finite geometric sums including beta3=beta1², epsilon2>0 limit and zero-floor divergence. All assumptions and boundary cases have been checked; g=0 excluded, beta1>0 ensures finite positive h even with epsilon2=0. New signed formulas apply uniformly to positive and negative nonzero g.

## originality

PASS

Prior official CAME article prescribes both EMA factorizations and clipping but does not derive the coupled exact response for a prescribed nonzero scalar gradient times a biregular support. Adafactor supplies only first-stage primitives. The repaired claim corrects a sign quantifier error while retaining the substantive new density-insensitive confidence law.

## value

PASS

Confidence normalization is CAME’s defining modification of Adafactor. Its exact response to a structured constant input reveals a nontrivial distinction: global confidence RMS cannot detect biregular sparsity while active-coordinate magnitudes scale as p^-1/2, and the second regularizer alone controls the limiting response amplitude. This is a motivated analytical limitation and tuning diagnostic for a named optimizer, not a claim about training stability; the sign repair is required to make the meaningful all-g statement correct.

The dated certificate retains the supplied scientific assessment, sources and limitations.
