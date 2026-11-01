# Review of the vertex-deleted cube theorem

## Correctness: PASS

For every integer \(d\ge2\) and finite field of characteristic two, the square of the complete cube adjacency matrix is \((d\bmod2)I\). Its shifted square-zero map has rank exactly half the vertices by a two-coordinate-block argument. Compressing away one vertex preserves that rank: the kernel contains a vector with nonzero deleted coordinate and the image contains no deleted-coordinate basis vector. The resulting compression rank and exact identity \(B^2=\varepsilon I+ww^{\mathsf T}\) force the stated even and odd Jordan decompositions. Counted kernels, invariant periodic subspaces and preimage fibers yield every transient and orbit formula without extrapolating finite data. Independently rerun `verify.py` exactly reproduced `verification_output.txt` and checked 51,352 configurations. No mathematical step relies on finite computation for all dimensions.

## Originality: PASS, with residual risk

The closest primary paper, Kim–Reiner–Schoenzeit (arXiv:2608.27887), explicitly studies the singly punctured cube as a real-spectral subgraph; its eigenvalue/eigenspace results over \(\mathbb R\) cannot determine the characteristic-two Jordan block sizes or dynamical first-entry populations. Sutner (2001) develops nilpotent/regular methods for one-dimensional finite additive automata, not vertex-deleted Boolean cubes. Li–Wang–Zhang (arXiv:2410.09833) assumes Eulerian/uniform degree parity; the punctured cube has mixed vertex-degree parities. Search comparisons included other vertex-deleted cubes, distance-two cube parity automata, feedback and edge-defect hypercubes and exact-table aliases. No checked result proves the exact claim or dominates it; an unindexed equivalent remains possible. The 1996 finite-field automaton paper was examined at bibliographic and abstract level, not falsely treated as a full-text exclusion.

## Value: PASS

Removing a single vertex from a maximally symmetric linear network alters the maximal nilpotent chain from two to three in even dimension, and creates a transient line in the otherwise reversible odd-dimensional dynamics. The theorem identifies the exact Jordan mechanism and the complete population of fixed, two-cycle and transient configurations for every dimension and finite characteristic-two field. This is a natural network-failure invariant that distinguishes vertex removal from previously studied edge removal and feedback changes, not an arbitrary numerical slice.

## Remaining limitations

No independent review or exhaustive historical priority claim is made. The comparison to real-spectral punctured-cube results is based on the accessible full paper, with finite-field transfer checked as a matter of actual statement implication, not keyword disagreement. The code confirms finite dimensions; the algebraic proof establishes the infinite claim.

Self-review: passed. Independent audit: not yet performed.
