# Scientific review: two-successor FIK chain normal forms

## Correctness — PASS

The underlying relation is fixed on the labeled \(n\)-element chain and is forward confluent exactly when its nonempty rows form a final segment and their maxima increase weakly. The global FIK box on an upset depends only on the suffix minimum of all target worlds, while the local diamond depends only on each row maximum. These are complete and recoverable invariants for **pointwise formula equivalence under fixed upward-closed valuations**. Every admissible invariant pair is realized by rows containing just the suffix minimum and the row maximum; the former are weakly increasing, making the construction valid. The number of pairs is the classical count of plane partitions in a \(2\times r\times(n-1)\) box, with the displayed factorial product. The single-successor spectrum follows by setting the two thresholds equal. Exhaustive checks directly tested all 66,066 relations on chains through four worlds, and separately enumerated all legal pairs through six worlds. The experiments are corroboration, not a proof of the general statement.

## Originality — PASS, with bounded search confidence

The 2023 FIK source [1] introduces the semantic condition and proves logical properties, but the inspected complete text contains no finite-chain operator quotient, two-successor representative, or plane-partition classification. The 2024 LIK source [2] uses both forward and downward confluence and a local box, so its relational class and forcing semantics are different and do not imply this count. The classical plane-partition product [3] counts arrays, not FIK operator pairs. A prior raw forward-confluent-relation count distinguishes all accessibility relations and is strictly finer: for four worlds there are 13,377 raw relations but only 726 modal operator pairs, so it does not subsume the quotient theorem. Four targeted semantic-index searches and focused public-text searches under the FIK, modal-equivalence, normal-form, plane-partition, and branching synonyms located no equivalent result. General duality folklore, uncatalogued notes, or independently noticed specializations remain originality risks; searching cannot certify priority.

## Value — PASS

The result replaces an exponentially larger relational search space by an exact classification of the **induced semantic operations**, which are what FIK formulas can observe. The existence and sharpness of a two-successor normal form is a structurally motivated expressiveness statement; it is not a re-expression of the raw frame count. The MacMahon product gives a complete natural exact invariant for every chain size, while the central-binomial partial-function count pinpoints the precise obstruction to removing modal branching. This is a finite-chain theorem, not a claim about general preorders or validity-equivalence of arbitrary frames.

## Limitations

The order must be a fixed labeled chain, the box clause must quantify over all higher worlds, and equivalence is pointwise with corresponding worlds and valuations. No expert independent audit or exhaustive search of unpublished literature has occurred.

Self-review: passed. Independent audit: not yet performed.
