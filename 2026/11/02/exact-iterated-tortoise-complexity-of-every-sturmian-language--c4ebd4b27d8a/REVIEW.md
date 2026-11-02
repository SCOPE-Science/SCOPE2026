# Scientific review: iterated tortoise complexity of Sturmian languages

## Correctness
**PASS.** The asserted identity holds simultaneously for all irrational slopes in the unit interval, all positive iterations, and all positive factor lengths. The proof derives the complete Sturmian factor set as a phase partition with exactly one coordinate jump per discontinuity, proves that each jump changes either \(u01v\) to \(u10v\) or the last letter \(u0\) to \(u1\), and computes exactly which jumps survive the \(k\)-fold deletion-and-append operation. Strict lexicographic increase at every surviving jump excludes all nonlocal duplicate images. The Abelian threshold follows from the two possible counts of ones. Standalone independent finite checks support, but do not replace, these arguments; rational experiments do not prove an irrational theorem.

## Originality
**PASS, with residual priority uncertainty.** Campbell–Rampersad, arXiv:2604.25811, Definitions 1–2 and Sections 3–7, defines this equivalence, treats paperfolding and Thue–Morse, proves only a general one-iteration constant-deficit bound under relevant low-complexity hypotheses, and asks about Sturmian versions. It does not give the formula as a function of arbitrary irrational slope, iteration count, and factor length. Defant–Kravitz, arXiv:1809.09158, defines the map for finite words, but not the infinite Sturmian enumerator. Searches for Sturmian tortoise complexity, rotation formulas, and equivalent iterated maps did not reveal a stronger covering theorem. A previously known restricted-slope single-iteration special case is not counted as a new separate finding; the all-slope/all-iteration formula and exact stabilization threshold are the contribution. Unindexed or implicit prior derivations remain possible; search absence alone proves no novelty.

## Value
**PASS.** The April 2026 motivating article expressly asks how tortoise complexity should be applied to Sturmian sequences. The result gives an exact unbounded two-parameter classification, not an arbitrary finite sample or a restatement of the known factor complexity. It precisely measures the trade-off between factor length, frequency and the number of tortoise passes, and identifies a sharp Abelian-agreement transition for every irrational slope.

## Scope and risks
There is no proof for non-Sturmian words or larger alphabets. The result does not classify fiber sizes. The computational checks are finite and use rational analogues for the phase claim; the irrational conclusion is proved symbolically. The main remaining risk is unindexed or implicit published coverage, not an unresolved proof step. Independent mathematical review is not available.

Self-review: passed. Independent audit: not yet performed.
