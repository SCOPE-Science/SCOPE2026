# Review

## Correctness
PASS. The proof reduces the noisy BCABE simplex to four commuting global Pauli strings. The tetrahedral sign vectors give the original eigenvalues \(p_i/4^N\) with multiplicity \(4^N\). Partial transpose flips exactly the global \(Y\)-coefficient once per transposed qubit, so parity alone controls the result. Reflection of the tetrahedron sends vertices to antipodes, yielding the complementary weights \(1/2-p_i\). Summing the unique possible negative eigenspace gives \(\max\{0,w-1/2\}\). The bundled matrix checker agrees for three system sizes and all nontrivial subset-size parities tested.

## Originality
PASS. The 2005 BCABE paper states the noisy family and the threshold \(w>1/2\), but not the full partial-transpose spectrum or negativity. The 2006 generalized-Smolin paper supplies the Pauli representation but contains no inspected negativity or partial-transpose result. The 2008 simplex paper is the closest source: it gives the odd/even partial-transpose geometry and an exact multipartite concurrence-type quantity. Its statement does not provide the four spectral values, their \(4^N\) degeneracy, or the resulting parity-uniform negativity/log-negativity in BCABE barycentric weights. Focused published-finding corpus and web searches did not return a source stating those formulas. Residual risk remains because an unindexed paper could contain the same computation.

## Value
PASS. The source's noisy activation criterion is qualitative. The exact spectrum turns it into a quantitative, cut-by-cut entanglement statement valid for every even system size and reveals a non-obvious compensation: negative eigenvalues shrink exponentially while their degeneracy grows exponentially, leaving total negativity independent of \(N\). It also subsumes the one-versus-three white-noise threshold used in recent Smolin-state experiments as a one-parameter special case.

## Closest literature and limitations
Bandyopadhyay et al. (2005) provide the four-weight noisy BCABE construction and activation threshold. Augusiak--Horodecki (2006) provide the Hilbert--Schmidt generalized-Smolin form. Hiesmayr et al. (2008) provide the closest parity/PPT geometry and a different multipartite entanglement measure. The accepted claim is confined to the complete partial-transpose spectrum and its negativity consequences; it does not claim new construction of the simplex, new activation threshold, or general equivalence between PPT and separability.

Same-model review: passed. Independent audit: not yet performed.
