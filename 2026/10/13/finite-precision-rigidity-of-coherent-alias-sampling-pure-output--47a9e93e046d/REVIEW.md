# Independent mathematical audit

## correctness

PASS

At the stated circuit cut, equal retained-register tuples determine all cross terms of the partial trace. Swap terms have distinct original address/random pairs in the retained tuple and produce the diagonal positive weights d_j; keep terms group by (alias, threshold, random), yielding t copies of the indicated rank-one outer product. The trace is one. Positive d_j force every alias basis vector into the support, so rank one requires a single alias c and zero keep weight off c; these conditions suffice. Uniformity is positive flow balance, which forces surjectivity, hence permutation, then equality of thresholds along cycles. Those fibers are singletons, giving I/L. Its spectrum and its difference from the uniform pure projector give the claimed entropy, squared fidelity convention and trace distance; the general positive-target formula is the expectation of the same Gram sum. A full-keep representation is genuinely different: with all t_j=B and all aliases equal the trimmed register is pure uniform. The symbolic argument covers every legal table and does not rely on the small-case checker.

## originality

PASS

The prior retained-state and distribution equations are substantial antecedents, and neither retained garbage itself nor computing a partial trace is the distinct claim. The surviving contribution is the two exact all-table rigidity classifications for the strict finite-bit implementation; no covering classification was established in the checked evidence.

## value

PASS

This is an implementation-specific structural obstruction, not just an example of dirty ancillas. No legal uniform table can improve the reduced state's pure-target fidelity by varying alias or thresholds; the exact obstruction scales as 1/L with n bits of entanglement. Together with the complete pure boundary it gives a useful diagnostic for when classical sampling guarantees cannot be read as clean-state guarantees, without making an unwarranted claim about jointly uncomputed oracles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
