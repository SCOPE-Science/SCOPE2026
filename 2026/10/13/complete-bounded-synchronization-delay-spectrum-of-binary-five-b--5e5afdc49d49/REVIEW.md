# Scientific review

## Correctness — PASS

The claim specifies the binary alphabet, exactly five positions per word, a six-word codebook, the universal prefix-code synchronization condition and the precise meaning of a complete false-framed word. The primitive-necklace argument excludes periodic words and two cyclic conjugates and yields an exhaustive \(5^6=15625\) parameterization. For each offset, a false parse of \(d\) words is equivalent to a directed walk of \(d\) edges, and directed cycles are exactly unbounded false parses. The two standalone integer-exact programs separately compute the full distribution. The complete CSVs agree byte-for-byte, and symmetry-orbit totals reproduce the unquotiented counts. The result makes no extrapolation to arbitrary block lengths.

## Originality — PASS, with residual risk

Classical work establishes the six-word upper bound and a Lyndon construction, and the delay-one comma-free optimum and its \(86\) labeled realizations were already classified. Those pieces are not claimed as novel. Direct comparisons with Cummings (1987, 1988, 1998) and Vohl–Quimper–Dubé (2016) found capacity bounds, special constructions and a different synchronization-control insertion problem, rather than the exact combined finite delay census \(5546,3116,456\) or the \(2293\) new symmetry classes. The inaccessible complete text of Golomb–Gordon (1965) and specialist later publications leaves a nonzero risk of unindexed enumeration or mismatched definitions, but the inspected statements do not imply the claimed census.

## Value — PASS

At a fixed optimal information alphabet size, a communication designer must distinguish immediately self-framing codes from codes permitting one, two or three successive false-framed words. The full natural equality-case enumeration quantifies that tradeoff and reveals thousands of optimizers unavailable under comma-freedom, together with their exact symmetry variety. This is a complete classification of a motivated finite optimum family rather than an arbitrary parameter change.

## Closest literature and limits

See Golomb–Gordon (1965), Cummings (1987, 1988, 1998) and Vohl–Quimper–Dubé (2016), with exact source identifiers in RESULT.md. A full re-evaluation of archival sources not available online may still be useful. The claim concerns uncorrupted streams and counts false-framed *blocks*, not elapsed raw bits. Independent verification was not performed.

Self-review: passed. Independent audit: not yet performed.
