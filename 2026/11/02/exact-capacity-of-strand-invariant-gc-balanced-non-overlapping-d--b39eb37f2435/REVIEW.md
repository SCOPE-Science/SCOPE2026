# Mathematical review

## Correctness — PASS

The domain is exactly the \(640\) quaternary length-five strings with two or three GC letters. Reverse complementation has no fixed points at odd length and preserves GC content. Direct regeneration gives \(320\) two-member orbits and excludes every internally overlapping orbit, leaving exactly \(120\). The supplied \(12\)-class partition is a clique cover of their incompatibility graph; testing all pairs inside every class bounds each code by \(12\) orbits. A separately checked \(12\)-orbit witness establishes equality, giving \(24\) words. The two included scripts reconstruct all critical claims by different encodings and return `VERIFY_OK` and `CROSSCHECK_OK` with standard-library Python only.

## Originality — PASS, qualified

Full primary-text checks included King's 2003 paper, the 2012 Chee–Kiah–Purkayastha–Wang paper, Blackburn's 2013 paper, the 2015 Yazdi DNA-storage study, and Stanovnik–Moškon–Mraz's 2024 balanced non-overlapping-code paper. Their GC/Hamming-distance, unrestricted synchronization, or balance-only results do not imply the exact optimum with both GC balance and reverse-complement closure. The closest published complete unrestricted length-five result gives \(81\) for the four-letter alphabet and does not resolve the \(24\)-word constrained optimum. Database and literature searches for the joint constraints found no equivalent theorem; an unindexed earlier joint-constraint table remains a residual priority risk, not a proof of absence.

## Value — PASS

Length five is a natural early odd length where all four proper overlap sizes matter, near-half GC means exactly two or three GC positions, and both forward and reverse orientations can be incorporated consistently. Determining the exact feasible capacity \(24\), as opposed to the unrestricted non-overlapping capacity \(81\), supplies a sharp mathematical design benchmark for this natural three-constraint intersection. The result does not pretend to resolve missing biochemical and Hamming-distance requirements.

## Limits and related work

The exactness is finite and certified only at word length five. The cited literature does not prove this joint maximum; more general biochemical constraints or arbitrary lengths are not covered. No independent scientific audit or exhaustive priority determination is asserted.

Self-review: passed. Independent audit: not yet performed.
