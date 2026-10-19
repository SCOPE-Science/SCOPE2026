# Scientific review: Dyadic abelian complexity of the Baum–Sweet word

## Correctness — PASS
The proof fixes the exceptional zeroth symbol and the no-leading-zeros convention. For every dyadic block, accepted nonzero indices imply acceptance of their nonzero binary suffix, giving coordinatewise domination by the initial block. Every length-\(2^m\) window is one suffix of an aligned block and one prefix of the next, so its weight is bounded by the total initial-block weight. Unique tilings by `1` and `00` count that initial weight as \(F_{m+2}\), and the internal `101` of the binary prefixes of a dyadic interval supplies all-zero windows. Sliding by one realizes each intermediate weight. The second generator and exhaustive finite window checks in `verify.py` agree through exponent 11; the argument, not the finite check, proves all exponents.

## Originality — PASS, with residual risk
The 2014 full-text prefix-normal paper defines the extremal-weight framework and studies enumeration of prefix-normal words; it contains no Baum–Sweet calculation. The 2018 full-text study, published in 2021, proves a general relation between Parikh-vector complexity and extremal factor weights (Section 5, Theorem 3), and treats paperfolding, Thue–Morse and Sturmian words, not Baum–Sweet. Parreau et al. (2015) treat 2-abelian regularity for period-doubling and Thue–Morse, not the asserted one-abelian Baum–Sweet values. Searches of available published records and semantic database results did not locate the same Fibonacci dyadic classification. Search failure alone is not evidence of novelty, and an unindexed equivalent calculation or a stronger theorem remains possible.

## Value — PASS
The precise length-\(2^m\) Parikh-spectrum size is a natural jumbled-pattern-reconstruction invariant of an automatic word. Its Fibonacci growth is unbounded and quantitatively different from the bounded abelian spectra of several standard automatic/Sturmian examples. The coordinatewise binary-suffix domination lemma explains why these particular long windows are extremal, so the contribution is not a bare numerical table or an arbitrary finite cutoff. No nondyadic formula is claimed.

## Literature and limitations
Closest relevant full texts: Burcsi–Fici–Lipták–Ruskey–Sawada, arXiv:1404.2824 (2014); Cicalese–Lipták–Rossi, arXiv:1811.06273 (2018 first submission, 2021 final paper), especially Section 5. Relevant context: Parreau–Rigo–Rowland–Vandomme, arXiv:1405.3532 (2014 first submission, 2015 publication); Baum–Sweet, Annals of Mathematics 103 (1976), 593–610. The claim is specific to dyadic lengths; no general-length prefix normality is asserted. It has no independent audit.

Self-review: passed. Independent audit: not yet performed.
