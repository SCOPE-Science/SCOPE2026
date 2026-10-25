# Scientific review

## Correctness — PASS
The proof separates the noncomputational infinite progression \(945+99225t\), justified by the standard coprime-multiplication lemma, from two finite exhaustive certificates. The practical residue representatives yield an effective global bound \(41236217\). The exact Python and C++ verifiers establish the finite coverage and the sharp obstruction at \(19067\), including a complete \(720\)-exception census. Both programs were executed successfully. Prime-factor practicality was cross-checked against direct divisor subsets for small integers. The computed certificate is not represented as an infinite proof by itself.

## Originality — PASS within inspected evidence
The closest primary source, Somu–Kukla–Tran, arXiv:2310.14149v2, proves qualitative co-finiteness for Zumkeller-plus-practical sums without an effective conductor. Its numerical largest exception \(32761\) concerns two Zumkeller summands and does not imply this claim. Mahanta–Saikia–Yaqubi (2020) concerns divisor and layering structure, not the exact mixed sumset conductor. Searches for `19067`, `720`, `Zumkeller + practical`, and corresponding sumset aliases in web literature and published mathematical records returned no exact prior result. A specialized unindexed census remains a residual risk.

## Value — PASS
The result determines a natural least eventual threshold for the specific additive representation whose eventual existence was established but left ineffective in 2023. It also counts and provides all exceptional integers, and supplies a finite, independently replayable boundary certificate. The distinction between the mixed sumset and the two-Zumkeller sumset is mathematically essential; the conductor is not a routine restatement of a known table.

## Limitations
The proof relies on deterministic finite computation over a sizeable interval, requires a C++17 compiler and memory for a sieve through \(42000000\), and does not classify representation multiplicities. Prior unindexed computations may exist.

Self-review: passed. Independent audit: not yet performed.
