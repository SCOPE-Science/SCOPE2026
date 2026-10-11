# Sharp spectral-demixed two-sensor frame bounds on finite cycles — scientific review

## Correctness — PASS

The statement is for normalized undirected cycles and the deliberately specified **demixed** output norm. Direct Fourier diagonalization yields one \(1\)-dimensional block with Gram eigenvalue \(2/N\) and \(K\) independent \(2\)-dimensional blocks with eigenvalues \((2/N)(1\pm|\cos(2\pi ks/N)|)\). This proves the claimed optimal frame bounds for every fixed sensor separation. The finite-circle pigeonhole upper bound and the explicit residue \(u=q\) give the exact best spacing \(q/M\) for every allowed integer \(N,K\). Equality on a divisible circle forces the \(K+1\) residues to be equally spaced, proving the totient count. The \(K+1\) Laplacian eigenvalues are pairwise distinct, so a genuine Vandermonde matrix recovers the demixed data from \(K+1\) time samples at each vertex. A direct supplementary computation checks the all-parameter formulas through \(N=120\), including two-by-two Gramian eigenvalues. No numerical approximation is used as an infinite-domain proof.

## Originality — PASS, with literature-access risk

The Sept. 21, 2026 graph-Paley–Wiener preprint provides current finite-graph dynamical-frame motivation, but the publicly retrievable abstract discusses path-graph numerical studies rather than a two-sensor closed-form cycle optimum. Its complete manuscript could not be accessed, so overlap beyond the abstract remains unresolved. Yang, Yang and Huang's 2021 author-posted full text provides a relevant original study of graph-node selection, frame-based reconstruction and a size-1000 undirected ring-graph numerical experiment; those materially reviewed sections provide neither the formula \(q=\lfloor M/(K+1)\rfloor\) nor the exact optimal separation count. Aldroubi et al. (2024) present general noisy space–time sensor recovery conditions, not an accessible explicit all-order optimal cycle-frame profile. Relevant published mathematical records for angular spacing, finite cyclic sampling and Fourier frame problems were compared by implication. The finite-pigeonhole and Fourier-diagonalization ingredients are classical; originality is claimed only for the combined all-parameter **demixed spectral frame design theorem**, not for those ingredients individually. Residual risk: an unindexed specialized cycle result or unavailable full manuscript might entail it.

## Value — PASS

The low-pass spaces \(H_K\) on \(C_N\) are natural, and sensor separation is a concrete design choice in dynamical graph recovery. A complete sharp frame-bound optimization quantifies worst-case recovery sensitivity across every cycle size and every strict low-pass cutoff, including parity-dependent lattice losses and the rigid arithmetic classification of all optimal placements on divisible grids. It improves a qualitative recoverability statement by giving exact conditioning and realization rather than optimizing an artificial subfamily. The crucial distinction from **raw** time-trajectory conditioning is explicit: Vandermonde demixing can be ill-conditioned and is not optimized by this theorem.

## References and limitations

- Bulai, Cabrelli, Cordero, Molter and Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472, first posted 21 September 2026. Abstract and date checked; complete manuscript inaccessible.
- Yang, Yang and Huang, *An Orthogonal Partition Selection Strategy for the Sampling of Graph Signals with Successive Local Aggregations*, Signal Processing 188 (2021), 108211, doi:10.1016/j.sigpro.2021.108211. Original author's full text inspected, including theory and ring numerical experiments.
- Aldroubi et al., *Reconstructing Graph Signals from Noisy Dynamical Samples*, arXiv:2411.12670. Abstract checked; complete text not obtained.

Same-model review: passed. Independent audit: not yet performed.
