# Scientific review

## Correctness
**PASS.** The claimed object is the basin of \(1\) under the base-three square-digit map. The finite orbit reduction follows from \(S(n)\le4d<n\) for numbers with \(d\ge4\) ternary digits and the full computation on \([1,26]\). The coefficients of \((1+z+z^4)^{m-1}\) enumerate all suffixes without omission, and summing the two possible leading-digit contributions counts every element of each exact shell once. Exact-integer cross multiplication establishes the contrasting densities; direct small-shell enumeration independently tests the recurrence. The published Theorem 4.1 of Gilmer applies because the explicit three bounds (B) are certified at both tested lengths, and the correction factor is greater than \(1-10^{-6}\). The final upper-versus-lower deduction is mathematically valid. Risks: the infinite transfer is a cited external theorem, not a new proof; the checker alone certifies only the finite input.

## Originality
**PASS, with stated literature risk.** The exact theorem is not the decimal nonexistence result of Gilmer [1]: changing the base is not itself a proof, since the attracting cycles and shell statistics change. Gilmer's transferable general theorem is credited, and the new contribution is the two exact ternary numerical certificates and their certified implications. Grundman and Teeple [2] prove ternary progression and parity statements, neither of which entails nonexistence of density. Searches for base-three happiness, upper/lower densities, equivalent basin formulations, and the two distinctive numerical bounds found no documented equivalent. A 2022 survey [3] was obtainable only as an abstract; its unexamined full text remains a residual originality risk.

## Value
**PASS.** Natural-density existence is a classical motivating question for digit-square dynamics. This theorem provides a complete yes/no answer for the smallest nontrivial odd base and a quantitatively strong separation. The two shell calculations are not arbitrary table entries: they are explicit witnesses satisfying a preexisting analytic transfer criterion for an infinite asymptotic property. Exact sharp densities remain open.

## Closest sources and remaining limits
[1] Justin Gilmer, *On the Density of Happy Numbers*, arXiv:1110.3836, Theorem 4.1 and Sections 2 and 5; full text inspected. [2] Grundman–Teeple, *Sequences of Generalized Happy Numbers with Small Bases*, JIS 2007, full text inspected. [3] Grundman–Hall-Seelig, *Happy Numbers, Happy Functions, and Their Variations: A Survey*, DOI:10.1007/s44007-021-00010-x, abstract only; full-text equivalence cannot be excluded. The proof does not find exact extrema, does not address all bases, and has not undergone independent validation.

Self-review: passed. Independent audit: not yet performed.
