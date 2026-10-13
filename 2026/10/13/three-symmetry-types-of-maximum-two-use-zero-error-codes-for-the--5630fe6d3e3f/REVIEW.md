# Self-review

## Correctness
**PASS.** The finite claim is verified in two independent ways. A row-state transfer computation reconstructs the complete independence polynomial of \(C_7\boxtimes C_7\), giving maximum \(10\) and exactly \(980\) maxima. A separate branch-and-bound search finds all \(200\) maxima through \(00\), whose translation closure is exactly the same \(980\)-set census and satisfies the incidence identity \(980\cdot10=200\cdot49\). Exhaustive action by the explicit order-\(392\) natural symmetry group then gives three orbits of sizes \(392,392,196\), with stabilizers \(1,1,2\). The proposed fingerprints and coordinate multiplicity profiles are checked on every maximum.

Risk: the equality classification is finite and computational, but the full standard-library verifier is supplied and independently reconstructs the extremal census before performing the orbit calculation.

## Originality
**PASS.** Hales proves the classical size-\(10\) optimum for the strong square of the \(7\)-cycle, while a recent transfer-operator paper publishes the complete independence polynomial and the count \(980\). The latter compresses the \(29\) single-cycle row states by dihedral symmetry, not the \(980\) maximum two-dimensional codes. Full-text comparison and exact-parameter searches found no source stating or implying the three natural-symmetry orbits or their \((u,v)\) fingerprints.

Risk: an obscure or unindexed historical equality-case classification may remain undiscovered; the claim is restricted to the explicitly defined natural group.

## Value
**PASS.** This is a complete equality-case classification for a classical zero-error benchmark. It upgrades a known optimum and a recently published raw count into a compact structural statement: exactly three extremal symmetry types, one with a nontrivial stabilizer, distinguished by a two-number distance invariant. The result is directly usable as benchmark data for symmetry-aware searches in higher strong powers.

Self-review: passed. Independent audit: not yet performed.
