# Review: square-zero regular-rank spectra

## Correctness (C): PASS

The algebra decomposition follows from the odd-order cyclic factor and reciprocal involution orbits. In the self-reciprocal case, the fixed length-four ring is exhibited explicitly by an invariant uniformizer and standard quadratic Galois descent; dimensions sum to \(8m\). The \(D_8\) factor is enumerated by exact coefficient equations for \(x^2=0\). The matrix-block polynomial follows from an exhaustive three-way reduction-valuation split and a Smith-pivot calculation over \(\mathbb F_Q[t]/t^4\), including the rank-six/rank-eight distinction for matrices of valuation one. Multiplication ranks add in product algebras; field extension ranks scale by degree. Computations exhaust \(D_8\) and \(D_{24}\) over \(\mathbb F_2\), \(D_8\) over \(\mathbb F_4\), and the local matrix block over \(\mathbb F_2\). The general claim is supported by the proof, not extrapolation from these checks.

## Originality (O): PASS, subject to historical priority uncertainty

The exact prior full-text comparison is Cao et al., arXiv:1902.07533: that paper decomposes the same binary dihedral group-algebra ambient module and enumerates distinct *self-dual left ideals*, not square-zero algebra elements refined by the rank of multiplication. The 2014 Brochero Martínez paper treats semisimple rotation order, whereas \(4m\) is divisible by two here. The close earlier square-zero census for \(\mathbb F_q[D_8]\) gives the total count but not the rank polynomial or all \(m\); the length-two chain-ring square-zero Smith enumeration does not give the needed length-four matrix fibers. The paper of Carnevale–Shechter–Voll counts traceless matrices without imposing square zero, so its image zeta functions cannot be substituted for the complete square-zero distribution. No directly covering indexed research record was found in actual searches. Unlocated rank-enumeration literature or an implicit combination of broader code and matrix enumeration results is a residual risk. Absence of a match is not proof of absolute novelty.

## Value (V): PASS

The rank distribution is a natural complete invariant of square-zero multiplication differentials on the regular module of a canonical infinite family of modular group algebras. Unlike a single table, the factorization handles all finite characteristic-two fields and every odd \(m\), including the maximal-rank (acyclic) count and every intermediate rank multiplicity. The repeated-root local factor is essential and the result provides multiplicities of generators, not merely existence or dimension of their associated dihedral codes. It is a directly reproducible finite-field enumerative theorem with potential application to regular-module homology and group-code generation.

## Limits and nearest literature

Brochero Martínez (arXiv:1405.3716) supplies reciprocal character context but excludes this modular even-order case. Cao–Cao–Fu–Gao (arXiv:1902.07533) supplies the exact dihedral code framework and distinguishes classification of self-dual left ideals from counting square-zero generators. Carnevale–Shechter–Voll (arXiv:1709.02717) concerns all traceless matrices, a different census. Earlier related square-zero characterizations in length-two chain rings and the order-eight case may provide ingredients but do not imply the complete formula without additional local analysis. Independent verification and an exhaustive historical publication-priority search are not claimed.

Self-review: passed. Independent audit: not yet performed.
