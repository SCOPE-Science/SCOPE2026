# Review of extremizer rigidity for two-distance codes

## Correctness (C): PASS

The statement quantifies over every labeled alphabet of size \(3\) or \(4\), every \(n\ge17\), and unrestricted (not necessarily linear) codes with nonzero pairwise Hamming distances in \(\{2,4\}\). The proof uses the strict cases of the *publicly available* Section 7 bound in arXiv:2610.30615v1, then derives equality in both estimates of Lemma 6.1. The deficit formula in its Eq. (5) forces all external pairs, and the one-coordinate synchronization lemma forces all letters. Explicit disjoint pairs determine the unique center and justify the count \((q(q-1))^n\). At \(n=17\), the six alternative upper bounds are at least 10 below the optimum; their gaps increase thereafter. The two standalone programs replay finite sanity checks; the all-length conclusion follows from the argument, not from a finite extrapolation.

## Originality (O): PASS, qualified

The nearest source is Lin–Djaljapayan–Yu (2026), arXiv:2610.30615v1, sections 2, 6, 7 and 9, which proves the optimal *cardinality* and displays the standard construction. It does not assert that every optimal code is isometric to it or count distinct labeled maximizers. The new implication extracts equality in both layer bounds, proves simultaneous synchronization of all supports, identifies a unique center, and counts every labeled equality case. Their companion arXiv:2610.30613v1 is restricted to \(q\ge5\); the binary precursor arXiv:2210.07496 addresses maximum size, not this ternary/quaternary equality classification. Searches for equivalent isometry-orbit classifications and exact codebook counts revealed no covering theorem; this is not a proof of global priority. The principal residual risk is that the equality classification may already have been recognized implicitly or recorded in unindexed work.

## Value (V): PASS

Knowing only the maximum size does not tell whether extremizers are structurally rigid or how many different labeled codebooks attain it. This result settles those natural questions simultaneously for every alphabet of size three or four at all lengths \(n\ge17\), by a nontrivial equality-case analysis of intersecting support configurations. It identifies one isometry class, forbids use of three or four different symbols at any fixed coordinate, and gives an exact exponentially large enumeration. These are structural consequences of extremality, rather than a restatement of the existing cardinality bound.

## Scientific dependencies and limits

The structural estimates in arXiv:2610.30615v1 are accepted as proved published premises. No attempt is made to independently reprove the underlying combinatorial intersection inequalities. The analysis does not classify maximizers at \(n\le16\) or alphabets of size at least five. The finite checks confirm construction validity, parameter injectivity in sample dimensions, and the arithmetic of the strict bounds; they cannot certify uniqueness of *arbitrary* large codes without the proof. Independently checking the source inequalities and previously uncatalogued equality-case work remains appropriate.

Self-review: passed. Independent audit: not yet performed.
