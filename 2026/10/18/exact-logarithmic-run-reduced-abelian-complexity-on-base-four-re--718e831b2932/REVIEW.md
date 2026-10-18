# Scientific review: run-reduced period-doubling spectra

## Correctness
**PASS.** The theorem includes both the exact reduced-Parikh class set and its logarithmic envelope. The proof establishes the prefix-zero/digit-sum identity from the primitive substitution, proves sharp base-four carry inequalities *with endpoint-letter equality conditions*, uses recurrent sliding windows to produce every intermediate zero count and both boundary letters, and transfers the resulting factor spectra via reversal closure. The independently executable checker confirms literal run-reduction counts and complete finite-prefix spectra at the first seven repunit scales. The checks do not replace the infinite argument.

## Originality
**PASS relative to the examined evidence.** Campbell–Currie–Rampersad define the new equivalence and derive results for paperfolding and Thue–Morse, but not this period-doubling profile (arXiv:2509.16034, especially Section 2.2). Parreau–Rigo–Rowland–Vandomme treat the finer two-Abelian and two-block-coding statistics of period doubling; their Theorem 21 controls the *number* of block-coding Abelian types, not the present run-collapse class set (arXiv:1405.3532, Sections 4–5). Machacek treats a different orbit complexity of a ternary word in terms of the ordinary Abelian complexity of period doubling (arXiv:2509.26613, Section 5). Searches of relevant published records for base-four repunits, period-doubling run collapse, and reduced Abelian complexity did not show coverage. The most important residual risk is an unlocated earlier transformation of two-block Abelian spectra implying the same exact subsequence.

## Value
**PASS.** The exact class classification at all repunit scales is a motivated, unbounded infinite computation of a recently introduced invariant for a classical fixed point. It proves that, unlike the bounded eventually periodic reduced-Abelian complexity of paperfolding, period doubling has a logarithmically growing upper envelope. The arithmetic source of the growth—the alternating binary digit sum together with a sharp base-four carry bound—may inform the full-profile problem. The result is more than a numerical list, routine substitution, or general upper bound.

## Limitations and validation status
The overall sequence has not been classified exactly, and no sharp global asymptotic constant is established. The correctness proof is self-contained; finite computation provides corroboration. Closest full-text sources and unresolved priority risks are identified above. The result has not received independent external scientific audit.

Self-review: passed. Independent audit: not yet performed.
