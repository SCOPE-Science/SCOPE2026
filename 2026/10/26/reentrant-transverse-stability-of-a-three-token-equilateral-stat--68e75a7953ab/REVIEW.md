# Scientific review

**Correctness — PASS.** The three-token map is smooth and globally defined for \(0<h<1\). The regular-triangle softmax derivative yields a neutral common-rotation eigenvalue and precisely two identical shape eigenvalues \(\lambda=(1-hL)/(1-hK)\). Their modulus is controlled exactly by \(hS(\beta)-2\). A derivative sign analysis yields one strict maximum and the two claimed crossings. An independent numerical derivative checker compares the actual nonlinear map to the computed full shape spectrum. At \(\lambda=-1\), no nonlinear stability verdict is asserted.

**Originality — PASS under examined evidence.** Altafini (arXiv:2610.13518v1) studies full attention with a positive dominant value eigenvalue, which the chosen negative scalar value violates. Gao, Yang and Chen (arXiv:2609.28448v1) analyze a closely related repulsive polygon setting but explicitly remove self-edges. That model differs dynamically and does not imply the reentrant full-self-edge three-token theorem. Six focused mathematical-record searches and claim-based historical deduplication found no explicit covering theorem. Historical-priority uncertainty persists under different naming conventions; search absence alone is not novelty proof.

**Value — PASS.** The smallest noncollinear full-attention configuration exhibits a genuine sharp stability-loss-then-restoration window in softmax sharpness at fixed residual step. The result identifies two critical values and an exact step boundary through a global one-variable calculation, furnishing a natural local dynamical phase diagram.

**Closest literature and limitations.** The two named arXiv papers are the primary comparators. The theorem is restricted to three planar unit tokens with full unmasked softmax, negative scalar value and \(0<h<1\). It gives transverse linear stability, not global convergence or nonlinear bifurcation type at the critical points. Residual equivalent-formulation priority risk remains.

Self-review: passed. Independent audit: not yet performed.
