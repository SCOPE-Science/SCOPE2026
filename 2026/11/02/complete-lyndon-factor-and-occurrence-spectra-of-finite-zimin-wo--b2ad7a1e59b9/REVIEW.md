# Review of the complete Zimin Lyndon-factor classification

## Correctness — PASS

The argument is valid for every finite rank at the exact ordered alphabet stated. It first derives the ruler representation and the alternating-minimum-letter desubstitution. Every nonsingleton Lyndon factor must start at the odd-position minimal letter and end at an even-position larger letter; the length-two substitution then reduces its Lyndon suffix test precisely to that of a lower-rank factor. The recursive classification has an explicit base case and terminates. Each occurrence of \(a_j\) is the center of a copy of \(Z_j\), making exactly the \(j\) listed suffix lengths available at that endpoint. This separately proves the stated multiplicities and sums; no finite enumeration is substituted for induction.

The standalone checker exhaustively compared every Lyndon factor at every endpoint for ranks 1–9, and additionally used a cyclic-rotation definition on the predicted factors for ranks 1–6. It checked distinct-factor sets, counts by length and endpoint, and total occurrence sums. All checks passed. Potential normalization pitfalls (the empty word, one-based indexing, alphabet order, distinct-versus-occurrence counting) are resolved explicitly in `RESULT.md`.

## Originality — PASS, with priority qualification

The closest known coverage is Badkobeh and Crochemore, *Left Lyndon tree construction*, arXiv:2011.12742, Section 5 (2020), which explicitly identifies **half Zimin words** as Lyndon. The special cases \(Z_{i-1}a_i\) therefore predate this report. That observation does not classify all off-diagonal words \(Z_{i-1}a_j\) for \(j>i\), exclude other factors, or determine every endpoint's Lyndon suffix profile and both multiplicity spectra. It is cited rather than presented as new.

Goc, Saari, and Shallit, arXiv:1207.5124 (2012), show \(k\)-regularity of Lyndon complexity of automatic sequences and compute specific binary spectra, including the Thue–Morse word. Their fixed-alphabet automatic setting does not imply the rank-dependent Zimin result. Głowinski and Rytter, arXiv:1307.1560 (2013), give a Zimin factor-membership criterion but no Lyndon-spectrum theorem; membership alone does not furnish the explicit comprehensive classification or occurrence counts. Rytter and Shur, arXiv:1409.8235 (2014), analyze pattern embeddings and Zimin type, a different problem. Glen, Simpson, and Smyth, arXiv:1701.00928 (2017), determine generic maximum and expectation properties of Lyndon factors and particular Christoffel counts, not the Zimin endpoint or occurrence spectrum.

The indexed research-record comparisons and available historical ledger claims showed no statement that covers or implies this complete theorem. In particular the previous Zimin anti-dictionary and palindrome-factorization results concern different invariants, and the previously recorded binary weight-three Lyndon spectra concern different words. Searches are not proof of historical uniqueness; ruler-sequence terminology and unindexed material remain residual priority risks.

## Value — PASS

Zimin words have \(2^n-1\) positions and are canonical unavoidable-pattern objects. The result identifies their entire set of Lyndon factors with only \(n(n+1)/2\) descriptions and yields a lacunary exact length spectrum, a pointwise suffix-profile classification, and an explicit total number of occurrences. This is a natural complete classification of a significant string invariant rather than an arbitrary finite table or a renamed instance of an existing binary result. Its positional form also gives an exact compact representation of the Lyndon-ending signatures of exponentially long words.

## Sources and limits

Material read includes full accessible text of arXiv:1207.5124 (Section 3), arXiv:1307.1560 (Sections 1–2), arXiv:1409.8235 (Sections 1–2), and arXiv:2011.12742 (Sections 1, 5, and 6), and arXiv:1701.00928 (abstract, introduction). The closest 2020 source was inspected in its accessible arXiv PDF, especially the note on half Zimin words. No claim is made that the prior half-Zimin Lyndon examples are original, or that historical priority has been exhaustively established. The finite checker only covers ranks up to nine. No independent scientific audit has occurred.

Self-review: passed. Independent audit: not yet performed.
