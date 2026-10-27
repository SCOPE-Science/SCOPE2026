# Scientific review: complete binary Gabidulin subcode census

## Correctness (C): PASS

The critical nonstandard fact follows from an exact field equation: \(L_{a,b}(x)=ax+bx^2\) has full binary rank precisely when exactly one coefficient is nonzero, whereas a nonzero mixed pair has kernel \(\{0,a/b\}\) and rank one less than full. This holds for every \(m\ge2\), and also makes the coefficient map injective. The full-rank-only subspaces are contained in one of the two coefficient axes because the sum of an element from each axis is a rank-deficient mixed word. This establishes the subcode-distance threshold. The quotient-and-graph bijection proves the exact Gaussian-binomial census, including the feasibility conditions and all quantifiers. Counting larger subspaces containing either full-rank axis proves the exact codimension probability with no overlap because no proper subcode contains both axes.

The extracted standalone verifier directly constructs the relevant matrices and checks every hyperplane through extension degree five. It separately enumerates every subcode through degree four (including \(417199\) subcodes for degree four) and checks complete rank spectra directly through degree three. The executable ends with `VERIFY_OK`. These checks corroborate the proof but do not replace its all-degree argument.

## Originality (O): PASS, qualified by the stated residual risk

The closest first-public 2026 source, Alfarano–Pratihar–Vinçotte [1], contains a general bound and a degree-three example where an exceptional subcode distance survives or falls. It does not identify all preserving hyperplanes or their proportions, let alone all rank spectra and the complete joint subcode census. The 2025 definition/structure paper [2] computes the parent code invariants, not this Grassmannian distribution. The 2006 subspace-subcode article [3] considers coordinate-alphabet restrictions, not arbitrary binary subcodes, so its stated construction does not imply the joint formula. Searches for coefficient-axis aliases, rank-enumerator profiles, subcode distances, and the exact \(2/(2^m+1)\) probability did not find equivalent coverage. Closely ranked mathematical records concerned other codes or Hamming-support distributions, and do not imply this claim.

The combinatorial graph count itself is elementary finite geometry and not claimed as an independent new counting principle. Possible unindexed or implicit prior coverage remains a real originality risk; search failure is not a uniqueness theorem.

## Value (V): PASS

The source [1] explicitly leaves frequencies of exceptional subcode-distance drops as a question. The result solves a natural complete binary degree-two specialization, supplies not just the probability but the whole rank-spectrum and code-distance distribution for *every* subcode dimension, and exhibits the exponential rarity of keeping the exceptional best distance under random one-dimensional removal. These are intrinsic coding invariants relevant to understanding structural loss under removal. The claim has a motivated infinite family and an exact classification, not an arbitrary finite slice. No computational security, decoding gain, or higher-degree generalization is inferred.

## Closest references and limits

[1] G. N. Alfarano, R. Pratihar, A. Vinçotte, arXiv:2610.03460, Sections 2.4, 4, 5–6.
[2] E. Camps-Moreno, E. Gorla, H. H. López, arXiv:2509.16424, Sections 2–3.
[3] E. M. Gabidulin, P. Loidreau, arXiv:cs/0607108, Sections 1–2.

The theorem applies only to the binary square degree-two family. No result is asserted for additive outside-code perturbations. Publication-priority verification beyond inspected sources is incomplete, and independent validation remains unperformed.

Self-review: passed. Independent audit: not yet performed.
