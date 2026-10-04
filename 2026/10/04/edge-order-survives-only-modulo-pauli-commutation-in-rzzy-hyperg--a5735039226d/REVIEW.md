# Scientific review: Edge order survives only modulo Pauli commutation in RZZY hypergraph states

## Correctness

PASS. The proof reduces the question to Pauli-string commutation. Two RZZY generators differ locally only by possible \(Y/Z\) role mismatches, so the total commutation sign is exactly the parity of those mismatches. The two star families have zero mismatches for every pair, hence all their edge rotations commute. The two-edge chain example has exactly one mismatch and therefore anticommutes; direct expansion gives the stated overlap formula. No infinite claim is inferred from the numerical checker.

## Originality

PASS. The primary 2026 source explicitly motivates the construction by the existence of noncommuting adjacent-edge permutations and describes a one-to-one encoding of edge-ordered weighted hypergraphs. Its own star formulas yield pairwise commuting generators, but the inspected source does not identify that all star orderings collapse to one state or formulate the general role-mismatch parity quotient. Targeted semantic and web searches found general Pauli-commutation/circuit-optimization literature but no prior statement of this correction for the RZZY hypergraph construction.

## Value

PASS. Edge order is a defining datum of the proposed representation. Showing that two entire advertised star subclasses erase that datum is a structural correction, not a cosmetic normalization issue. The parity criterion also identifies exactly which local edge interactions can carry order information and supplies the appropriate commutation quotient that any reconstruction or graph-inference use must respect.

## Closest literature and limitations

The closest source is arXiv:2609.30399v1 itself, which defines the RZZY generators and the star and chain families. arXiv:2305.10966 treats commuting Pauli rotations as a circuit-optimization resource but does not analyze edge-ordered hypergraph injectivity. The present result does not claim that the commutation quotient is a complete classification of all state-level degeneracies; special weights and global phases can create additional identifications.

Same-model review: passed. Independent audit: not yet performed.
