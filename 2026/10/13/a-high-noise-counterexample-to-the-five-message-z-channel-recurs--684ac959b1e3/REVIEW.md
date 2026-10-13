# Self-review

## Correctness — PASS
The channel orientation, uniform message distribution, published column order, and maximum-likelihood criterion are explicit. For every output, a minimum-weight containing codeword is the ML choice when \(0<p<1\). Exact partitions of outputs produce both full-probability polynomials, whose difference factors as \(p^2(1-p)^2(1+p)(2p^3+p-1)\). The strictly increasing cubic yields one transition and strict improvement over a nonempty open interval. Exact independent enumeration of all \(256\) outputs, integer polynomial coefficients, and rational-likelihood evaluations agree. No global optimum or other length is asserted.

## Originality — PASS
The inspected 2011 source explicitly proposes the affected five-message length-eight code as a conjectural optimum, and its 2013 full-length successor reproduces that precise starting codebook. Neither source states the alternative or the high-flip probability obstruction. The closest work on binary asymmetric minimum-distance codes concerns a different objective; papers on the binary erasure and symmetric channels concern different channels. Targeted literature and mathematical record searches found no equivalent exact inequality, but an obscure or unindexed prior counterexample remains a residual risk. The comparison refutes a conjecture, not a published theorem.

## Value — PASS
This is a motivated challenge to a specific prominent small-blocklength optimality conjecture at its prescribed even-length base case, not an arbitrary parameter slice. The obstruction holds on the entire open interval above an exact algebraic threshold and arises inside the same weak-flip column family, pinpointing the multiplicity choice as the issue. It gives a precise correction target for finite-blocklength Z-channel design without claiming that the alternative achieves the global optimum.

Self-review: passed. Independent audit: not yet performed.
