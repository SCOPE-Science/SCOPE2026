# Scientific review

## Correctness — PASS
Exact exhaustive enumeration of all 65,536 possible vertex masks gives 3,054 nonempty faces. The supplied `verify.py` checks the full 13,584-incidence acyclicity certificate of 1,514 sequential Morse matches; every nonstandard integral pivot is actually \(\pm1\). It computes the complete critical integral boundary matrices, their primitive rank-one and rank-four images (including a unimodular determinant \(-1\)), and independent mod-two simplicial ranks. The resulting reduced CW model has a primitive three/four-cell cancellation and four primitive four/five-cell cancellations, giving the **homotopy** wedge rather than merely matching Betti numbers. It verifies a 92-term integral four-cycle and all 384 signed automorphism actions and Lefschetz traces. The precise mathematical limitations are stated in `RESULT.md`.

## Originality — PASS (residual literature-access risk)
The closest complete primary treatment, Deshpande–Singh (arXiv:2001.05448), defines the same higher-independence object but classifies graph families that do not include the four-cube. Its open grid question concerns **nonperiodic** rectangular grid graphs; the four-cube is a periodic grid. Previously indexed ordinary four-cube independence, total cut and edge-matching complexes have different face conditions; neither their numerical results nor their proofs subsume this result. Indexed aliases, character formulas and previously recorded related claims were compared. Salvetti's early d-independent paper was located by DOI but its full text remained inaccessible, so equivalent coverage there or elsewhere is not ruled out. Search absence alone is not a novelty theorem.

## Value — PASS
The four-cube is a canonical symmetric graph. Its first higher-independence complex provides an exact, nonpure and genuinely mixed-dimensional **integral homotopy classification** together with the whole rational hyperoctahedral symmetry character. The distinct invariant dimensions in degrees three and four give meaningful additional structure beyond a face count or a previously known ordinary independence result. The claim is intentionally restricted to this natural graph and one higher-independence index.

## Closest sources and limitations
See Zaker, arXiv:1507.07194 (induced-degree bound, not complex topology); Salvetti, DOI:10.1007/978-3-319-20155-9_22 (abstract only); Deshpande–Singh, arXiv:2001.05448 (full text inspected); and Abdelmalek et al., arXiv:2106.10863 (chordal hypotheses inapplicable). Independent scientific verification has not been performed; an unindexed equivalent result remains possible.

Self-review: passed. Independent audit: not yet performed.
