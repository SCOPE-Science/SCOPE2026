# Review of sharp Hilbert distortion for clique-joined rook graphs

## Correctness — PASS

The argument has two independent universal inequalities: the Hilbert four-point quadrilateral identity on every rook rectangle gives squared distortion at least \(2\), and the exact centroid variance identity combined with the average squared edge and diagonal bounds gives the second rational lower bound \(L_{m,n,h}\). Neither step assumes an equivariant embedding, fixed dimension, or positive-definite numerical approximation. Three orthogonal centered regular simplices construct matching embeddings in both regimes. Equality cases in every nonnegative inequality recover the claimed complete rigidity classification for \(L\ge2\); a perpendicular translation exhibits distinct optimizers for \(L<2\). The exact-arithmetic checker verifies all pairwise constraints for 224 triples and 20 alternative balanced configurations, with 154006 exact rational pair checks. Finite checks are corroboration, not the infinite proof.

## Originality — PASS (historical priority qualified)

Vallentin's Hamming-graph theorem (arXiv:math/0509716, §4.1) determines the core's squared distortion \(2\) but is about distance-regular graphs and lacks the joined clique's cross-centroid obstruction. Cioabă–Gupta–Ihringer–Kurihara (arXiv:2109.09708, Introduction and §5) likewise studies distance-regular embeddings; the present graph is irregular since hub degree exceeds core degree by \((m-1)(n-1)\). Cardoso–Díaz–Rojo (DOI:10.1016/j.laa.2018.08.024) studies graph-join **distance spectra**, which do not directly give the present nonlinear least-distortion optimization or rigidity regimes. Targeted searches for rook graph join, universal-clique Hamming metric, Euclidean distortion, equivalent forms and tables, plus comparisons with accessible related mathematical records, found no covering theorem. Prior work on related Banach-space distortions and graph complexes studies different invariants. This is a qualified originality assessment; older equivalent work under other spectral/SDP terminology and the uninspected full body of a less directly relevant join-spectrum paper remain risks.

## Mathematical value — PASS

This is an exact three-integer-parameter classification of a natural graph operation applied to two-coordinate Hamming graphs, with a sharp phase boundary \((h-1)/(2h)=1/m+1/n\). Beyond the boundary, the join produces strictly more Hilbert distortion than the rook graph alone; in the balanced large-size limit the distortion approaches \(\sqrt{5/2}\). The proof also distinguishes asymmetric rigidity from a balanced interval of optimizers, with full affine dimensions at and above the boundary. These structural effects are not supplied by the previously known Hamming core distortion. The claim does not extend to higher Hamming dimensions, arbitrary edge weights, or other target spaces.

Self-review: passed. Independent audit: not yet performed.
