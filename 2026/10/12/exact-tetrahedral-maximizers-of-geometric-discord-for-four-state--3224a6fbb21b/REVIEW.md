# Self-review

## Correctness
PASS. The second-moment identity for \(G\) follows from the orthogonal projector onto the traceless diagonal subspace of \(4\times4\) Hermitian matrices. The trace-one eigenvalue bound is sharp. Equality is classified without numerical assumptions by the Gram-matrix projection argument, and the QRAC success ceiling follows from exact Walsh-vector quadratic forms. `verify.py` replays the rational identities and all sign choices.

## Originality
PASS. The defining Yao et al. paper gives \(D_G\le1/12\) and numerical searches for arbitrary Bloch-sphere encodings but not exact attainment or a complete equality classification. The later Mančinska--Storgaard Bloch-geometry QRAC paper concerns success-probability bounds and contains no geometric-discord result. Focused semantic literature searches did not locate an implication-equivalent theorem. Residual risk remains for obscure literature using tight-frame terminology without QRAC/discord keywords.

## Value
PASS. The claim resolves a concrete numerical gap in a canonical QRAC/discord model, identifies every maximizer by a standard geometric structure, and proves an exact strict gap between maximum discord and optimal \(2\to1\) QRAC performance. The result is meaningful even without a broader resource-theory claim.

## Closest literature and limitations
The closest source is Yao et al., arXiv:1207.1275, whose Appendix A proves the trace bound and then resorts to simulation. Mančinska and Storgaard, arXiv:2106.00155, provide broader QRAC Bloch-space geometry but do not discuss discord. The theorem is restricted to equal-prior pure qubit encodings and Hilbert--Schmidt geometric discord.

Self-review: passed. Independent audit: not yet performed.
