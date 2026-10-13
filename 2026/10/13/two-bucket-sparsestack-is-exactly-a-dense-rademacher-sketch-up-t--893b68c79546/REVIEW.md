# Review of the two-bucket SparseStack Gram-law classification

## Correctness — PASS

For arbitrary integer \(\zeta\ge1\) and \(m\ge2\), the four equally likely one-coordinate signed vectors are carried bijectively by a fixed orthogonal \(2\times2\) Hadamard matrix to all four independent-sign vectors. Independence across all columns and blocks proves the full law, not merely equality of low moments. Orthogonality yields pathwise Gram invariance. For every \(b\ge3\), the two-column collision variable has second and fourth moments \(1/b\), giving the explicitly factored gap \((b-1)(b-2)/(b^3\zeta^3)\) relative to dense independent signs; positivity prevents Gram-law equality. The \(b=1\) and \(m=1\) boundaries are accounted for. Standard-library exact support enumeration and rational identities were replayed on the packaged script. No infinite assertion depends on the finite enumeration.

## Originality — PASS, with residual risk

Compared exact equivalence, orthogonal rotation, Gram moments and the full-width iff claim against the arXiv full text of Jeendgar–Flint–Anzt (Sec. 2.2 and implementation), Camaño–Epperly–Meyer–Tropp (Sec. 3.1 and Appendix B), Chenakkod–Dereziński–Dong (OSNAP main results and moments), Heidary (Secs. 1–2 and 7), and Tikhomirov (intro and Sec. 7.3). These analyze the same signed-hash sampling construction or related general embeddings, but supply high-probability bounds, comparisons with three-point-entry ensembles, or general moments rather than the exact law and iff obstruction here. Searches of the published mathematical-finding index for the Hadamard/Rademacher block equivalence yielded only distinct results, including Haar stochastic subspace descent and unrelated Hadamard frame geometry. General classical fourth-moment algebra is credited, not claimed as a new theorem. Unindexed or differently phrased equivalent constructions remain a legitimate originality risk; this is a self-review, not a proof of absolute novelty.

## Value — PASS

When selecting a fully independent sparse oblivious subspace embedding at a fixed output dimension, a concrete block width determines sparsity and distribution. The classification provides an exact *whole-ensemble* replacement, transferring every Gram-based distortion or joint least-squares statement from iid-sign sketches to a structured family with precisely half as many input contributions. It also shows sharply, by a parameter-explicit fourth-moment invariant, why identical covariance cannot justify the same replacement for any larger block width. This is a natural complete boundary of the SparseStack family rather than an arbitrary numerical slice. It makes no unsupported finite-precision or runtime-speed claims.

## Closest literature and scientific limits

Closest specific source: arXiv:2606.20195v1; closest general theoretical work: arXiv:2508.21189v1 and arXiv:2609.02978v2. Restrictions: real, fully independent, exact arithmetic; no performance, adaptive input, limited-independence, or Gaussian equivalence guarantees. More remote equivalent formulations could remain undiscovered.

Self-review: passed. Independent audit: not yet performed.
