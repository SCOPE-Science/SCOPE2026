# Scientific review: one-bond-defect quantum-ring average mixing

## Correctness — PASS

The assertion is an exact theorem for each integer \(n\ge3\) and real \(g\ge0\). For nonunit links, an explicit two-boundary Chebyshev recurrence proves spectral simplicity: a two-dimensional eigenspace would force \(g^2=1\). Reflection parity gives an upper rank bound \(q=\lceil n/2\rceil\). Counting closed walks shorter than the circumference yields the exact moment determinant \((-1)^{q-1}(g^2-1)^{q-1}\), proving the matching lower rank bound for every \(g\ne1\). Projector square Gram factorization identifies the *entire* kernel. Godsil's explicit unperturbed-cycle formulas are cited for \(g=1\) and yield the stated parity-dependent rank and kernel. The severed-link value \(g=0\) is included, and the two-vertex multigraph is explicitly excluded. The finite exact-arithmetic and numerical checks support the proof but are not mistaken for infinite verification.

## Originality — PASS, with stated residual risk

Godsil's 2011 sections on paths and cycles already give the endpoint \(g=0\) and \(g=1\) cases, which are credited. Adamczak et al. (2007) concern unperturbed circulants; nonunit bond weights destroy circulancy. Coutinho, Godsil, Guo, and Zhan (2018) give an encompassing *method* for quantum average-mixing rank, but the inspected sections do not entail the exact defect-parameter rank and kernel without the new walk-counting witness. Godsil, Guo, Kempton, and Lippner (2017) study perturbed-edge state transfer of strongly regular graphs, which neither treats arbitrary cycles nor classifies their Cesàro ranks. Li and Wang (2015) treat defects on the infinite line rather than finite rings. The qualifying 2022 article develops general exact spectral methods but does not derive this parameter-uniform bond theorem. Source-by-source implication comparisons and potential broader reductions are recorded in `AUDIT.json`.

No matching bond-rank assertion was identified in the searchable mathematical-results index or the examined primary papers. Lack of a hit is not proof of global priority. The main residual risk is an unlocated general theorem about cyclic Jacobi eigenvector intensities that subsumes this result. Claims about unweighted-cycle or severed-link values are not presented as newly established.

## Value — PASS

The weak-link ring is a natural finite coherent-transport model. Altering a single edge by arbitrarily little breaks translation degeneracies but retains a bond reflection. The theorem exactly quantifies how this changes the *dimension and full nullspace* of stationary time-averaged transport: a discontinuous rank fall for odd rings and a replacement of the unobservable contrast modes for even rings. The determinant identifies the only transition parameter for every ring length and offers a reusable closed-walk method; this is more than a textbook application or a selected finite computation.

## Boundaries and evidence

Primary comparison material includes Godsil (arXiv:1103.2578, Sections 4, 6), Adamczak et al. (arXiv:0708.2096, cycle/circulant theorems), Coutinho et al. (arXiv:1709.03591, Sections 3–5), Godsil et al. (arXiv:1710.02181, edge perturbation and transfer results), Li–Wang (arXiv:1502.04289, infinite-line defect), and Coutinho et al. (arXiv:2208.08971v1, exact average methods). See `VERIFICATION.md` and the executable `verify.py`. General multiple-edge disorder, magnetic flux, time-dependent quantities and finite-time mixing are unproved here. Independent review is still required for publication-level confidence.

Self-review: passed. Independent audit: not yet performed.
