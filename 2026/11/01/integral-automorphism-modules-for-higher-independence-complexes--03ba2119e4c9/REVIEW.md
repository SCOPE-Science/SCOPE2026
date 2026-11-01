# Self-review

## Correctness — PASS

The proof gives a complete relative-simplicial chain model. Faces missing one hub comprise a contractible complex because the two possible one-hub cones attach to a leaf simplex along contractible joins. The remaining faces are exactly the oriented hub edge plus at most \(r-2\) leaves. Their relative differential is the augmented leaf-skeleton differential, and the only extra automorphism sign is reversal of the hub pair. The augmented simplex boundary is contraction by the sum-of-coordinates functional, with integral kernel \(\bigwedge^{r-2}W_L\). The long exact sequence gives the canonical integral module and excludes additional degrees and torsion. The boundary cases \(r=1\), \(r=2\), \(r=m+1\) and \(r\ge m+2\) were checked explicitly. The packaged checker passed 128 finite homology cases and 1,050 signed-character cases; those computations are not substituted for the general proof.

## Originality — PASS, with residual risks

Deshpande and Singh's 2020/2021 Theorem 3.10 and Corollary 3.13 already give the exact ordinary sphere-wedge homotopy type of every double star. **That result is prior coverage, and is excluded from the claimed novelty.** Their fully inspected primary text does not give the integral module structure, and its nonequivariant Morse matching does not imply a character formula. Subsequent papers by Abdelmalek et al. (2021), Ghosh and Selvaraja (2025) and Sawant (2026) address shellability and vertex decomposition, not the full automorphism action on integral homology. Targeted searches of mathematical records and literature did not identify an equivalent module theorem. The remaining risk is an unindexed or implicit equivariant version of the earlier Morse matching; independent comparison is still needed.

## Value — PASS

The new object is the natural integral representation of the full graph-automorphism group on the only nonzero homology group, not a recomputation of its rank. For all sizes and thresholds the lattice is a canonical exterior power of the leaf augmentation kernel with a hub-exchange sign. This distinguishes group actions invisible to the known wedge count: for the six-leaf balanced double star at threshold four the hub interchange has trace two and gives \(6\)- versus \(4\)-dimensional rational eigenspaces. The structural chain model and exact character formula supply reusable symmetry information about a natural caterpillar family. The result does not assert any downstream general-tree theorem.

## Closest source and limitations

The closest full-text predecessor is arXiv:2001.05448v2, Theorem 3.10 and Corollary 3.13; it **fully covers** the ordinary homotopy statement but not the integral automorphism module claimed here. arXiv:2605.25150v1 is the recent primary motivation and establishes vertex decomposability of all higher tree-independence complexes. arXiv:2106.10863 and arXiv:2505.06614 contribute shellability/vertex-decomposability context. This work does not claim a full equivariant homotopy equivalence, fixed-point classification, or independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
