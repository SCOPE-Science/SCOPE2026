# Scientific review — Loewy filtration and nilpotent cutoffs

## Correctness: PASS
The proof specifies the endomorphism ring of \(C_{p^a}\oplus C_{p^b}\) and proves that for unequal exponents its radical is the kernel of diagonal reduction to \(\mathbb F_p\times\mathbb F_p\). The radical powers are exactly given by minimum-weight walks for the valuation matrix \(\begin{psmallmatrix}1&0\\b-a&1\end{psmallmatrix}\); single-corner products attain the bounds, proving equality, not just containment. The resulting two valuation regimes determine each quotient order and nilpotency cutoff. The equal-exponent case is treated separately. Finite ring enumeration supports every formula in the checked cases but cannot prove the universal statements.

## Originality: PASS within the evidence examined
Mader (2012) supplies the underlying matrix normal form; Keef (2024) studies general Jacobson-radical structure; Senden (2023) studies Reidemeister fixed-point spectra. The accessible inspected portions do not give this full two-cyclic radical-power and nilpotent-element profile. Searches targeted the exact ideals, equivalent Loewy layer counts, nilpotency cutoffs, and larger endomorphism-ring structure. The 2003 Krylov–Mikhalev–Tuganbaev chapter on radicals is an important **unresolved** source, not a verified noncoverage. Absolute novelty is not certified.

## Value: PASS
The result determines all powers of a canonical radical and all their sizes, uniformly in the prime and both cyclic exponents. Its adjacent-exponent versus separated-exponent change distinguishes two natural Loewy regimes, and the equal-summand case distinguishes radical nilpotency from individual-element nilpotency. These are nontrivial structural and arithmetic invariants.

## Scope and limitations
The classification covers exactly two cyclic primary summands, not arbitrary finite abelian groups. It is not an element-by-element conjugacy classification. A relevant older chapter could overlap, and independent external review remains outstanding. Reproduce the finite checks with `python3 checker.py`.

Self-review: passed. Independent audit: not yet performed.
