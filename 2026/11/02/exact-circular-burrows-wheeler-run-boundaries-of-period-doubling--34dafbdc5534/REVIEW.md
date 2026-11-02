# Scientific review: circular Burrows–Wheeler boundaries of period-doubling words

## Correctness (PASS)
The claim fixes the substitution, complete dyadic iterates, circular lexicographic transform and linear notion of runs. The proof first proves primitiveness from odd symbol count, avoiding tied rotations. A parity decomposition classifies length-three factors and forces every long circular bispecial factor to be \(\mu(v)0\). This gives a complete recursive bispecial set. Every BWT boundary is associated with exactly one lexicographic cut at a right-special factor; comparing predecessor symbols filters those cuts. Order reversal under substitution transfers the cut indicator, and direct contexts at \(\epsilon\), \(0\), \(00\) prove which new cuts are active. There are exactly \(2k-3\), giving \(2k-2\) runs. Direct checks agree through rank \(14\), with independent sorting through rank \(9\). The proof, not the finite checks, establishes all ranks.

## Originality (PASS, with priority risk)
The inspected BWT morphism survey of Brlek et al. (2019) treats different named morphic families. Frosini et al. (2022) establish logarithmic BWT-run mechanisms but not the explicit period-doubling two-family boundary cut set. The full available article by Fici et al. (2025) includes a period-doubling *morphism* in a worst-case transformation-sensitivity question, which neither fixes the input to its dyadic iterates nor gives their circular BWT. The accessible Currie et al. (2013) study lexicographic infinite shift extremals, not sorted finite circular rotation cuts. No inspected result, direct table or abstract implies the exact theorem. Literature coverage is necessarily nonexhaustive, especially for unindexed prior computations and alternate definitions of BWT.

## Value (PASS)
The number of BWT runs is a natural compressed-index complexity measure. This theorem identifies **every changing predecessor cut**, not just a growth bound or empirical sequence. Its canonical bispecial-factor certificate isolates the structural source of each run and yields an exact logarithmic law in a classical primitive automatic-word family. It applies at all dyadic ranks and does not merely restate general \(O(\log N)\) bounds or existing factor-count formulas.

## Checked sources and limits
Full available primary texts inspected: Burrows–Wheeler (1994), Currie et al. (2013), Brlek et al. (2019), Frosini et al. (2022), and Fici et al. (2025). Original published terminology, circular-versus-sentinel BWT, and uniform versus existential bounds were compared. Remaining scientific scope excludes arbitrary prefixes or terminated transforms; historical-priority uncertainty and independent verification remain.

Self-review: passed. Independent audit: not yet performed.
