# Review of the three-absorber hypercube theorem

## Correctness: PASS
The proof uses the complete Walsh eigenspace decomposition of the hypercube adjacency matrix. For each interior Hamming weight, the restriction to three traps has rank two exactly when two traps are antipodal and otherwise has rank three. The non-antipodal implication follows from a coordinate-swap argument over the two-dimensional binary vector space, not from numerical enumeration. The positivity of all absorption strengths guarantees strict decay on the resulting bright subspace. Both endpoint eigenspaces contribute rank one. Together these statements establish the formula for every integer \(d\ge2\). The finite exact rank checks reproduce the claimed values in independent spectral and Krylov constructions, but are corroboration only.

## Originality: PASS relative to available inspected sources
Bernasconi–Godsil–Severini (arXiv:0808.0510) already imply special antipodal symmetry and transfer on cubelike graphs; the antipodal proportionality itself is therefore not asserted original. Novo–Mohseni–Omar (arXiv:1312.6989) and Novo et al. (arXiv:1412.7209) treat single-site trapping and spectral/Krylov reductions. Their inspected texts do not state the complete three-absorber placement dichotomy or its \(3d-1\) non-antipodal rank. Earlier two-trap formulas and generic spectral rank criteria likewise do not directly state the new all-triple classification, although a broad graph observability theorem could imply it. The assessment is based on explicit implication comparisons and is not a priority certificate. Later related work on projective detection and general graph transport remains a residual literature risk.

## Mathematical value: PASS
Three sites are the smallest trap arrangement in which the spectral constraints can exhibit a rank-three versus rank-two phase change across every interior Walsh shell. The result completely classifies this natural physical invariant for all three-site placements, including independence from site loss rates, a particularly sharp three-cube full-versus-partial absorption example, and the exact frequency of the exceptional configurations. It answers more than a single isolated numerical example.

## Limits and literature risk
The theorem does not cover unequal hopping weights, more than three traps or detailed source-resolved absorption dynamics. A general previously published observability-rank theorem may cover the result after nontrivial specialization. The one-sink and antipodal structure are known and expressly excluded from the claim of originality. Finite computational checks do not establish the all-dimensional result.

Self-review: passed. Independent audit: not yet performed.
