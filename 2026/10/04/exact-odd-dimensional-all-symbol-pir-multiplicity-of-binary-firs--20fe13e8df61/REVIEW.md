# Same-model review

## Correctness
PASS. With the standard binary first-order Reed–Muller generator \(g_x=(1,x)^T\), a recovery representation of a target column uses an odd number of distinct columns; after minimization, a nontrivial representation has at least three columns. Three-column representations are exactly translates of the nonzero point sets of two-dimensional subspaces. Năstase--Sissokho supplies a partial two-spread of size \((2^m-5)/3\) for odd \(m\). The upper bound is stronger than a locality-three bound: if one more disjoint arbitrary-size recovery set existed, counting would force all sets to have size three, and their associated planes would cover all but one nonzero vector, contradicting the zero XOR of both every plane and the full nonzero vector set.

## Originality
PASS. The 2018 Reed–Muller availability paper proves the even-dimensional exact value but gives only \((2^m-4)/4\) as an odd-dimensional lower bound and explicitly says optimality was not shown. The exact partial-spread theorem is a separate finite-geometry result and does not state the Reed–Muller recovery consequence. The 2026 all-symbol PIR paper explicitly lists Reed–Muller all-symbol recovery properties as an open direction. Focused searches for the exact odd formula, partial-spread formulation, availability aliases, and all-symbol PIR wording did not locate the theorem. A 2025 Reed–Muller recovery-set paper concerns message symbols rather than stored codeword coordinates and therefore does not subsume the claim.

## Value
PASS. This closes an infinite parity gap in a classical Reed–Muller availability problem and simultaneously settles the exact all-symbol PIR multiplicity for every odd-dimensional binary first-order Reed–Muller code, a family explicitly singled out in recent all-symbol PIR work. The result also makes the finite-geometry obstruction transparent and yields a sharp exact formula rather than a marginal numerical improvement.

## Closest literature and limitations
The closest coding-theory source is Baumbaugh et al. (2018), whose Theorem 4.12 gives only an odd-dimensional lower bound and states that optimality was not established. Boruchovsky et al. (2026) supplies the current all-symbol formulation and open family-level direction. Năstase--Sissokho supplies the exact partial-spread ingredient. Ly--Soljanin studies a different target class (message symbols). The theorem here does not address all-symbol batch recovery, nonbinary alphabets, higher-order Reed–Muller codes, or uniqueness of extremal families.

Same-model review: passed. Independent audit: not yet performed.
