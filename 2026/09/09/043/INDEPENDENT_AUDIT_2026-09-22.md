# Independent audit — 2026-09-26

Record: `2026/09/09/043`. Verdict: **correctness PASS; originality PASS (selected patterns); scientific value PASS (bounded).** Disposition: retain accepted.

## Correctness
For each of six asserted vacuous cells, the given extremal-occurrence replacement is a valid occurrence of the same classical base: M0/M1 replace the first entry by an earlier entry of lower/intermediate value, M2/M6 replace it by an interior entry with later first index while fixing the second, M3 replaces the third by an earlier interior entry, and M5 replaces the first by the earlier intermediate entry. The well-ordering/lexicographic extremum then yields an empty selected cell. This is an all-n argument, distinct from table matching. I independently enumerated all permutations of lengths 4–7 with a separate open-rectangle incidence test: rows at n=7 were [2762,2762,2762,2762,3060,2761,2761,2958], matching the eight asserted values; at n=5, M4/M7 each give 104 versus the 2143 classical 103. The listed S5 witnesses have the indicated unique blocked occurrence. The n=10 values rely on the package's two C enumeration paths and cross-check, rather than this third enumerator; classical rows agree with OEIS A061552 and A005802.

## Prior work and originality
The Shading Lemma framework (Hilmarsson et al. 2014; generalization in *Coincidence among families of mesh patterns*, arXiv:1412.0703) precedes this elementary replacement proof. Zhang and Zhao, arXiv:2607.04111, close length-two mesh Wilf classification at 46 classes; this does not classify these length-four examples. Credit is limited to the selected eight shadings, their explicit pairwise comparisons and bounded M4/M7 counts, not to a general classification of all single-cell length-four meshes.

## Scientific value and limits
The all-n collapse supplies precise examples and the finite table gives search data for two genuinely different shaded patterns. The 1.827699 ratio at n=10 says nothing about growth constants; no completeness of the chosen window or transfer-matrix certification is proved.

Sources: RESULT.md, output/artifacts/vacuity.py, enumA.c, enumB.c and verify.py; https://arxiv.org/abs/1409.3165; https://arxiv.org/abs/1412.0703; https://arxiv.org/abs/2607.04111; https://oeis.org/A061552; https://oeis.org/A005802.
