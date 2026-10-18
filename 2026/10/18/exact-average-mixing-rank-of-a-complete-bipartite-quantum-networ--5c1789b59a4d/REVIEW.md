# Scientific review: one defective bond in a complete bipartite quantum network

## Correctness — PASS

The claim covers all integer part sizes \(a,b\ge2\) and all nonnegative real bond weights \(g\). The proof uses the exact spectral compression characterization \(x^{\mathsf T}\widehat Mx=\sum_\lambda\|E_\lambda\operatorname{diag}(x)E_\lambda\|_F^2\). A four-cell decomposition isolates two dark zero-energy spaces and a four-dimensional singular-value block. For \(g\ne1\), the block has four distinct nonzero eigenvalues. The dark constraints and two bright constraints are shown explicitly to have constant ranks, with exceptional values determined solely by part sizes. The special case \(g=1\) is derived separately. Exact rational commutant calculations for 180 parameter triples and independent grouped-spectral computations for 288 profiles reproduce the predicted rank. These finite calculations are corroborative, not an infinite proof.

## Originality — PASS, with qualifications

The closest general prior theorem is the diagonal-commutant correspondence of Coutinho–Godsil–Guo–Zhan (arXiv:1709.03591), but it does not state the weighted one-edge biclique rank law. Godsil–Guo–Kempton–Lippner (arXiv:1710.02181) analyze edge perturbations of strongly regular graphs, overlapping the balanced biclique Hamiltonian, yet their studied outcomes are strong cospectrality, spectral polynomials and state transfer, not average-mixing rank. The general exact average-mixing algorithm in Coutinho et al. (arXiv:2208.08971) does not deliver this explicit family classification. Carlson et al. (arXiv:quant-ph/0608044) address instantaneous universal mixing across variable weights and average uniformity, rather than this fixed-one-bond Cesàro rank. The recent survey on average-mixing questions (doi:10.1515/spma-2024-0025) also does not record this classification in its inspected discussion. Literature search does not certify global novelty; unlocated equivalent singular-space theorems remain a risk.

## Value — PASS

A local bond defect is a standard physical perturbation of coherent transport networks. The result provides the exact response of a global long-time observable to an arbitrarily small defect, distinguishing balanced from unbalanced networks and exposing a three-mode loss on the smallest balanced nontrivial example. Its strength-independence is an exact structural fact, not a numerical fit. The unrestricted two-parameter family and explicit sharp full-rank boundary are useful for designing networks robust to a single coupling error.

## Scope and risks

The source date used for this mathematical-physics direction is the 2022-08-18 first public version of arXiv:2208.08971, with primary MSC 81P68. The theorem concerns nonnegative single-edge weights only. It does not address signed couplings, multiple defects, finite-time mixing rates or optimized observation-time distributions. A more specialized, unlocated published theorem could imply the formula; no claim of universally verified publication priority or independent external validation is made.

Self-review: passed. Independent audit: not yet performed.
