# Self-review

## Correctness — PASS
The source premises were independently checked in the primary full text: the curve is \(y^3=x(x^3-1)\), its full automorphism group is \(C_9\), the generator acts by \(x\mapsto\zeta_3x\), \(y\mapsto\zeta_9y\), the line \(z=0\) is the unique undulation line, and the remaining bitangents satisfy the displayed elimination equations. The stabilizer proof is exhaustive because every nontrivial proper subgroup of \(C_9\) is the unique subgroup of order three. The two-torsion proof reconstructs the action on a holomorphic differential basis and obtains the full cyclotomic characteristic polynomial \(\Phi_9\); irreducibility modulo two excludes fixed nonzero two-torsion for every nonidentity power. The attached exact verifier checks the polynomial and finite-field algebra used in the proof.

Risk: the Cayley-octad and Steiner-complex conclusions use the standard genus-three identifications from the cited literature; no explicit octad coordinates are claimed.

## Originality — PASS
Liang states that \(C_9\) acts on its bitangent configuration, but the inspected theorem and proof do not give the orbit decomposition, the \(u=a^3\) orbit labeling, the real-cyclotomic identification, or any Cayley-octad/Steiner-complex orbit profile. Bergvall supplies the general level-two dictionary but does not specialize it to this curve. Exact and alias searches in the research database and the public literature did not locate a statement equivalent to the combined claim. General \(\operatorname{Sp}(6,2)\) tables remain a residual risk for the unlabeled cycle counts, but they do not by themselves identify Liang's explicit \(u\)-fibers with the three bitangent orbits.

Closest literature risk: an older classical theta-characteristic treatment or a finite-group permutation table may encode some or all of the cycle shapes without using modern Picard-quartic terminology.

## Value — PASS
The result turns an explicit bitangent list into the complete level-two symmetry profile of the unique order-nine plane quartic. The key structural link is that the three geometric bitangent orbits are labeled by the real cubic subfield naturally associated with ninth roots of unity, while the same order-nine action is irreducible on two-torsion. This explains, in one statement, the orbit structure of bitangents, even theta characteristics/Cayley octads, and Steiner complexes; it is not an arbitrary numerical slice or a recomputation of a known table.

Self-review: passed. Independent audit: not yet performed.
