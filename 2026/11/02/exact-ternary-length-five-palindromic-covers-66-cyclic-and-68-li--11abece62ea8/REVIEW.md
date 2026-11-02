# Scientific review: exact ternary length-five palindrome covers

## Correctness — PASS

The claim explicitly fixes the alphabet, contiguous-factor semantics, cyclic wrapping, and allowance of repeated targets. Selecting one instance per palindrome yields a permutation of target starts and a rigorous minimum-gap bound; the added dummy vertex handles linear endpoint cost. For each of 702 cyclic and 756 linear arcs, a machine-readable half-integral degree-and-cut dual inequality is verified using integer arithmetic. The dual sums are exactly 66 and 68. Independently checked word constructions attain those bounds and contain all 27 targets. The verifier does not rely on a solver's status or extrapolation of experiments. Remaining technical risk is ordinary software or transcription error, mitigated by small exact certificates, source-visible code, and full edge enumeration.

## Originality — PASS, qualified

The closely relevant full-text paper by Chen, Kitaev, and Sun (arXiv:1908.01116) concerns universal cycles/words and principally deletions of at most two words, not the length optimization of the 27 ordinary ternary palindromes. OEIS A330022 treats binary linear palindrome superstrings; its Hamiltonian formulation is acknowledged as prior methodology. Simpson (2014) bounds counts of distinct palindromes in circular words across lengths and does not imply either exact minimum. Shortest-superstring approximation bounds do not imply these two numerical equalities. Separate earlier results for all-alphabet length-three and length-four palindrome covers likewise do not imply length five. Targeted comparisons of palindrome-superstring, cyclic-versus-linear, and overlap formulations have not located an exact equivalent or a stronger theorem covering the precise instance. Residual risk: an unindexed computational table or equivalent superstring result may already have the same values; failure to locate one does not prove first discovery.

## Value — PASS

All 27 five-letter ternary ordinary palindromes form a canonical finite family, not an arbitrary chosen subset. The exact shortest circular and linear lengths distinguish two natural universal-word models, identify a nontrivial two-character boundary advantage, and provide short reproducible lower-bound certificates as benchmarks for constrained superstring algorithms. Both settings are solved, not only bounded or experimentally approximated. The values do not imply a general alphabet-length theorem; such a theorem is not required for the value of these natural finite optima.

## Closest sources and scientific limitations

- Chen, Kitaev, and Sun, arXiv:1908.01116: universal cycles/words of restricted collections, different deletion scope.
- OEIS A330022: binary linear palindrome superstrings and Hamiltonian-overlap methodology, different alphabet and no cyclic minimum.
- Simpson, DOI 10.1016/j.tcs.2014.07.012: global palindrome diversity in circular words, not exact fixed-length cover minima.
- Teng and Yao, DOI 10.1137/S0097539794286125: general approximation context, not an exact solution of the present instance.

Self-review: passed. Independent audit: not yet performed.
