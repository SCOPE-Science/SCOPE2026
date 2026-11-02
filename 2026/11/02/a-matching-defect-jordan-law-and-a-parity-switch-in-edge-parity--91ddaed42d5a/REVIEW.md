# Scientific review: a matching-defect Jordan law and a parity switch in edge-parity networks

## Correctness

**PASS.** The update matrix equals the characteristic-two incidence Gram matrix \(B^{\mathsf T}B\). Connectivity gives \(\operatorname{im}B=\{z:\sum z_i=0\}\) and \(\ker B^{\mathsf T}=\langle\mathbf1\rangle\). Removing a matching leaves on the even-coordinate subspace either a coordinate-swap involution (odd root order) or disjoint nilpotent all-ones two-by-two blocks (even root order). The proof computes the ranks from these blocks, derives both Jordan forms, and obtains first-entry populations by counting kernels. Direct binary tests cover all parameter pairs through order 16 at the matrix level and 3,995,516 initial states in a separate edge-wise enumeration through order 7. These finite tests corroborate, rather than replace, the proof for every order and every characteristic-two field.

## Originality

**PASS, subject to historical-priority limitations.** The incidence identity, general linear-basin formula, and ordinary real ranks of line graphs are previously known and are not presented as new. Davis–Domke–Garner (2004) inspect complete graphs and cocktail-party graphs over the real numbers, not their characteristic-two Jordan decompositions. Ciandrini et al. (2008) discuss general XOR network dynamics but do not calculate this matching-defect phase diagram. Abudayah–Alomari–Sander (2022) establish matrix identities for mixed graphs but not orbit classifications. Prior edge-XOR work on hypercube, tree, and Hamming-product line graphs treats different root families; a few degenerate small graphs are shared but do not cover the parameter-uniform theorem. Direct searches for finite-field matching-deletion line-graph recurrences and stronger universal coverage did not locate an equivalent explicit result. The residual risk is an equivalent unindexed spectral or algebraic classification.

## Value

**PASS.** Deleting a matching is a canonical one-parameter perturbation of a complete graph. This single family exhibits an exact even–odd transition between global extinction and nontrivial recurrent oscillations, with the entire Jordan structure and all attraction-basin and first-entry counts explicit. The rank response to the final missing edge differs by the parity of half the graph order; it is a structural boundary effect not captured by the usual real adjacency-rank treatment. Exact resolution of this natural infinite-family invariant may be useful for comparing discrete feedback and finite-field spectral response across graph perturbations.

## Scope and remaining risks

The claim is confined to loopless synchronous updates of edge states over characteristic-two fields and deletion of pairwise-disjoint root edges. General incidence formulas and previously known special cases are excluded from priority. Independent validation and exhaustive historical-priority coverage have not occurred. The publisher PDF was examined at relevant sections and other selected pages, not word-for-word across every page; its stated method concerns ordinary real adjacency spectra.

Self-review: passed. Independent audit: not yet performed.
