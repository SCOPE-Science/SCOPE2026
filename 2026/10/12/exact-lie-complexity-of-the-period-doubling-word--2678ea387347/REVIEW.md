# Self-review

## Correctness
PASS. The proof is self-contained from the period-doubling substitution. Every \(1\) in the fixed point occurs at an odd global position, and a short substitution argument excludes \(0000\). These facts give a unique desubstitution of any qualifying even-length circular class after at most one rotation.

The map
\[
[u]_C\longmapsto[\delta(u)]_C
\]
is proved to be a bijection on qualifying classes. Even rotations are direct morphic images; odd rotations are realized by starting one symbol inside an occurrence of an image. Conversely, qualifying image rotations with a \(1\) are forced to occur at the aligned parity and therefore desubstitute. The only possible odd-shift collapse would force an all-zero image, which cannot occur for length at least four.

At odd length at least five, a qualifying circular word needs at least two \(1\)'s. A cyclic cut separating two \(1\)'s changes the relative parity of exactly the wrapped group because the length is odd, contradicting the one-parity property of every period-doubling factor. Direct base cases at lengths \(1\) and \(3\) finish the proof.

The standalone verifier independently enumerates factor sets and cyclic classes through length \(192\), checks the doubling law through half-length \(96\), and confirms the structural forbidden factors.

## Originality
PASS. Bell and Shallit's primary paper introduces ordinary Lie complexity and computes closed formulas for several classical automatic words, but the inspected examples do not include period-doubling. The later extension paper by Li likewise contains no period-doubling occurrence. Older work on cyclic complexity explicitly treats period-doubling, but its quantifier is weaker: one conjugate need occur rather than all of them.

Targeted exact-formula, invariant-name, conjugacy, automaticity, and dyadic-support searches found no covering ordinary Lie-complexity formula. Current and prior research ledgers contain other period-doubling invariants but no Lie-complexity statement. Residual risk remains for an unindexed Walnut computation or note.

## Value
PASS. This completes a natural missing classical example for an invariant introduced to study exactly this kind of conjugacy closure. The theorem is stronger than a finite automatic output table: it identifies the two qualifying conjugacy classes at every nonzero length and explains the support by a morphic bijection plus a sharp odd-length obstruction.

Self-review: passed. Independent audit: not yet performed.
