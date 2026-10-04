# Review

## Correctness
**PASS.** Equality of all STFT magnitudes gives equality of squared magnitudes. For the two-point window, each frequency slice has only character coefficients at \(0\), \(a\), and \(-a\); the assumption that the step order is at least \(4\) makes these distinct, so the adjacent squared-magnitude sum and complex edge product are exactly recoverable. On full support, quotient variables satisfy a forced alternating recurrence. The remaining recovered sum reduces to one factored scalar equation, yielding either unimodular cycle scaling or the stated two-level parity swap. The converse is checked directly by preservation of the recovered coefficients. The bundled exact verifier independently checks the coefficient identities and both branches throughout a broad finite range.

## Originality
**PASS.** The closest archive-era paper, Bojarovska--Flinth, gives sufficient ambiguity nonvanishing conditions; its nonvanishing-signal criterion is inapplicable to this equal two-point window at even step order because the zero-shift ambiguity vanishes at a half-cycle character. Jaganathan--Eldar--Hassibi establish almost-all uniqueness for overlapping short windows, which permits a measure-zero exceptional set but does not identify it. Bartusel's later exact short-window theory explicitly treats ambiguity zeros but its complete finite-dimensional statements concern separated signals, while it cites the almost-all nonvanishing theorem rather than classifying the exceptional full-support fibers. Targeted published-finding corpus searches for the exact two-point, alternating-magnitude, and full-support fiber formulations returned no scientifically equivalent result. The own-ledger overlaps concern support size/minimization for the same two-point window and a generic-window theorem for two-sparse signals; neither implies a phaseless full-support fiber classification.

## Value
**PASS.** The theorem converts an almost-sure statement into an exact boundary description for the simplest short window precisely where the standard ambiguity-nonvanishing sufficient condition fails. It explains the even-cycle obstruction structurally, identifies every exceptional full-support signal rather than merely exhibiting examples, and gives the entire measurement fiber, including disconnected-step cycles. This is a natural sharp phase-retrieval fact rather than a parameter increment or table recomputation.

## Closest literature and limitations
The closest literature is Bojarovska--Flinth (2015/2016), Jaganathan--Eldar--Hassibi (2015/2016), and Bartusel (2023). The result is restricted to full support and even step order at least \(4\); the order-two aliasing case and zero-containing signals remain outside the theorem. A differently phrased or poorly indexed prior classification remains a residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
