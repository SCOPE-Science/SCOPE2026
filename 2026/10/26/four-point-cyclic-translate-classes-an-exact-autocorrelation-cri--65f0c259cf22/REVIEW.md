# Scientific review

## Correctness — PASS

The stabilizer quotient and the full-branch cardinality bound are proved directly. The central case is aperiodic: positive version space has exactly four distinct hypotheses; depth three requires a balanced second split, equivalent to one nonzero two-point autocorrelation. When that split exists the second-level four cells contain \(2,2,2,n-6\) hypotheses, all at least two, and third queries can separate pairs in each cell. Independent hypothesis-table dynamic programming confirms all \(20{,}293\) four-subsets for cyclic orders eight through twenty, including explicit witness-tree path checks.

## Originality — PASS, with residual priority risk

General Littlestone-dimension closure results in Ghazi–Golowich–Kumar–Manurangsi (2020) are inequalities rather than the exact cyclic-autocorrelation criterion. Aaronson–Ellis–Leader (2020) study union-closed families of cyclic translates; their result does not count adaptive mistake trees. Malliaris–Moran (2021) study stable-class structure and online-learning connections without a four-point cyclic classification. Search comparisons against published four-point difference/Fourier records and existing exact VC/Littlestone records found no statement that entails this trichotomy. Differently named older work remains a priority risk.

## Value — PASS

The theorem classifies the exact online-learning invariant for every four-point cyclic translate family in all cycle lengths at least eight. Periodicity and one nonzero two-point difference multiplicity completely determine rank; the Sidon-versus-progression contrast gives infinite examples with identical hypothesis counts and support sizes but different optimal mistake bounds. This is not merely an instance enumeration.

## Limitations

The proof does not cover supports with other cardinalities or cycles below order eight. Historical priority cannot be fully established by searchable records. Finite computation serves as an independent check rather than proof at unbounded order.

Self-review: passed. Independent audit: not yet performed.
