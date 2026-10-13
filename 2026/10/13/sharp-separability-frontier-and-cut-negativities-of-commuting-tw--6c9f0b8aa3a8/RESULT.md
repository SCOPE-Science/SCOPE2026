# Sharp separability frontier and cut negativities of commuting two-local Pauli Gibbs states

## Finding
For any finite number of qubits and any pairwise commuting Hamiltonian formed from distinct nonidentity Pauli strings of weight at most two, all thermal entanglement is confined to a matching of independent two-qubit Bell-diagonal sectors. This yields an exact test for full separability and an exact expression for logarithmic negativity across **every** bipartition.

In particular, fix an interaction coefficient bound \(J>0\), and allow any number of terms with \(|h_j|\le J\). If the term-overlap graph is required to have maximum degree at most any fixed \(\Delta\ge2\), then the largest universally separable inverse-temperature interval is exactly
\[
0\le\beta J\le\frac{\log3}{4}.
\]
The bound is attained by a two-qubit three-term commuting Heisenberg dimer. For every \(\beta J>(\log3)/4\), an admissible two-qubit example is entangled. No system-size dependence or dependence on \(\Delta\ge2\) remains.

More precisely, after one-qubit Clifford transformations and a permutation of sites, every Hamiltonian in the stated class decomposes into a diagonal classical Pauli Hamiltonian on some sites, together with pairwise disjoint Bell dimers
\[
H_e=a_e X\otimes X+b_e Y\otimes Y+c_e Z\otimes Z.
\]
For each such dimer let \(p_e\) denote the largest of its four Gibbs probabilities in the Bell basis. The global thermal state is fully separable **if and only if** \(p_e\le1/2\) for every dimer. If \(A\) is any subset of physical qubits, its logarithmic negativity across \(A\mid A^c\) is exactly
\[
E_N(A)=\sum_{e\,\mathrm{crosses}\,A\mid A^c}\log_2\max\{1,2p_e\}.
\]

## Assumptions and scope
Let \(n\ge2\), and let \(P_1,\ldots,P_m\) be pairwise distinct nonidentity Hermitian Pauli strings on \((\mathbb C^2)^{\otimes n}\), each of support size one or two. Assume \([P_j,P_k]=0\) for every pair and \(H=\sum_{j=1}^{m}h_jP_j\), where every \(h_j\in\mathbb R\) satisfies \(|h_j|\le J\). Identity terms are irrelevant constants and are omitted; equal strings have been collected **before** imposing the coefficient bound. The Gibbs state is \(\rho_\beta=e^{-\beta H}/\operatorname{Tr}e^{-\beta H}\) for \(\beta\ge0\).

The term-overlap graph has one vertex per nonzero term, with two vertices adjacent when their Pauli supports intersect, regardless of whether the operators commute. The universal-threshold assertion considers every such Hamiltonian with maximum overlap degree at most a prescribed integer \(\Delta\ge2\); the structural and cut-negativity identities need no degree bound. Full separability means a convex combination of tensor products of single-qubit states. For a bipartition, \(E_N(A)=\log_2\|\rho_\beta^{T_{A^c}}\|_1\).

## Proof
**1. A two-local commutation rigidity lemma.** Suppose commuting strings \(P,Q\) use different nonidentity Pauli axes on qubit \(v\). Their local factors anticommute on \(v\). For the complete strings to commute they must anticommute at a second qubit \(w\). Since both have weight at most two, both supports are exactly \(\{v,w\}\), and their local axes differ at each endpoint. Any other commuting Pauli string touching \(v\), but not \(w\), would have to commute at \(v\) with two independent Pauli axes, which no nonidentity Pauli does. An additional term supported on \(\{v,w\}\) must lie in the four-element Pauli centralizer of \(P,Q\), namely the identity and their two generators and product, up to scalar phases.

Single-qubit Clifford conjugations therefore identify each such isolated pair with the span of \(I\), \(X\otimes X\), \(Y\otimes Y\), and \(Z\otimes Z\). Different isolated pairs are disjoint. On every remaining qubit all incident Pauli factors have the same axis; one local Clifford converts them to \(Z\). All remaining terms are diagonal in the resulting product basis. Hence the asserted decomposition holds for **all** commuting weight-at-most-two qubit Pauli Hamiltonians, irrespective of system size or overlap degree.

**2. Thermal factors and exact cut negativity.** Exponentiating this tensor-factor decomposition gives one classical diagonal Gibbs factor and independent dimer factors. Each dimer is diagonal in the Bell basis because its three displayed two-qubit Paulis commute. The allowed simultaneous eigenvalue signs are precisely
\[
(s_x,s_y,s_z)\in\{\pm1\}^3,\qquad s_xs_ys_z=-1,
\]
with energies \(E_s=a_es_x+b_es_y+c_es_z\) and probabilities \(q_s=e^{-\beta E_s}/\sum_ue^{-\beta E_u}\). The partial transpose of a Bell-diagonal two-qubit state has eigenvalues \(\{1/2-q_s\}_s\). Thus it has positive partial transpose precisely when \(p_e=\max_s q_s\le1/2\). The two-qubit positive-partial-transpose criterion is sufficient for separability. The classical factor is explicitly a mixture of product-axis projectors. Taking partial traces back onto each isolated pair shows that if any dimer is entangled, the global state is not fully separable. This proves the exact full-separability test.

For a given cut, dimers wholly on either side have partial-transpose trace norm one. A crossing dimer has partial-transpose trace norm \(\max\{1,2p_e\}\), because there can be at most one negative eigenvalue \(1/2-q_s\). The classical factor stays positive under transpose in its product eigenbasis. Multiplicativity of the trace norm under tensor products and invariance under one-qubit unitaries prove the displayed logarithmic-negativity formula for **every** cut, including cuts of size one and the endpoints \(\beta=0\) and \(\beta\to\infty\).

**3. Uniform upper bound on Bell concentration.** For two different allowed Bell sign triples, exactly two signs differ. Consequently every pair of dimer energies differs in magnitude by at most \(4J\). If \(E_*\) is a minimum energy, each of the other three energy differences satisfies \(0\le E_s-E_*\le4J\). At every \(\beta\ge0\),
\[
p_e=\left(1+\sum_{s\ne*}e^{-\beta(E_s-E_*)}\right)^{-1}
\le\frac{1}{1+3e^{-4\beta J}}.
\]
If the minimum is degenerate, choose any minimum; the same inequality applies and the displayed expression still equals the largest Boltzmann probability. When \(4\beta J\le\log3\), this upper bound is at most \(1/2\). Step 2 then gives full separability independently of the number of qubits and of \(\Delta\).

**4. Sharpness at overlap degree two.** On two qubits take \(H=J(X\otimes X+Y\otimes Y+Z\otimes Z)\). These three distinct weight-two terms commute and their term-overlap graph is a triangle of maximum degree two. The antisymmetric Bell state has energy \(-3J\); the other three Bell states have energy \(+J\). Therefore
\[
p_{\max}=\frac{1}{1+3e^{-4\beta J}}.
\]
It exceeds \(1/2\) precisely when \(4\beta J>\log3\). The negative partial-transpose eigenvalue then proves entanglement. The same witness lies in every class with \(\Delta\ge2\), completing the universal necessity and sufficiency claim.

## Verification
The analytic proof establishes all dimensions and real coefficients. The accompanying standalone program `verify.py` enumerates 9,957 commuting subsets of one- and two-qubit Pauli terms on three and four sites (within documented subset-size limits), checking the isolated-pair rigidity assertion. It also compares full two-qubit Gibbs matrices with their partial transposes in 6,600 samples, and tests 3,960 explicit bipartition partial-transpose trace norms against the sum-of-dimers formula for four- and five-qubit examples. Its expected final output begins `VERIFY_OK`. Run with `python3 verify.py` in an environment providing NumPy as specified in `requirements.txt`.

The enumerations and floating-point tests are **finite corroboration**, not a proof for unbounded \(n\). Universal statements follow from the exact support argument, the four-dimensional Bell spectrum, and the sharp explicit witness.

## Relationship to prior work
Kiani, *Sharp universal death of entanglement threshold for Pauli Hamiltonians* (arXiv:2609.30149v1, first public September 24, 2026 UTC), proves a sharp bound for **unrestricted term locality** at each bounded overlap degree, using a larger-support commuting tree construction for sharpness. At overlap degree two its universal sufficient threshold is \((\log2)/4\), strictly less than the present \((\log3)/4\). That result does not imply a matching upper bound within the commuting, two-local subclass. Its highly relevant full manuscript was not available for direct inspection in this comparison, so possible implicit specialization remains a residual originality risk.

Marvian and Lidar, *Quantum error suppression with commuting Hamiltonians: Two local is too local* (arXiv:1410.5487, 2014), establish short-range structure for ground spaces of commuting two-local Hamiltonians. Their ground-space/noise statement does not determine finite-temperature Bell-sector populations, exact many-qubit cut negativities, or the sharp universal inverse-temperature frontier. Bouland, Mancinska, and Zhang, *Complexity Classification of Two-Qubit Commuting Hamiltonians* (public full text at Stanford), address computational sampling power of a single two-qubit interaction applied throughout a register, not finite-temperature separability of arbitrary commuting Pauli sums. The Bell-state partial-transpose criterion itself is classical work of the Horodecki family and is used here rather than claimed as new.

A degree-at-most-one **two-term** overlap case admits a separate sharper threshold; that earlier regime and its thermodynamic criteria are not claimed anew. The present frontier is caused by the first allowed three-term Bell dimer, appearing at degree two.

## Limitations
The statement does not cover noncommuting Hamiltonians, terms of support at least three, higher local dimension, non-Pauli two-body interactions, or fixed ensembles whose coefficient sum is not bounded after identical terms are collected. It classifies a deliberately restricted but natural physical family; it does not imply the universal high-temperature threshold for unrestricted Pauli Hamiltonians can be raised. The quantitative logarithmic-negativity law gives no corresponding claim about distillable entanglement rates under arbitrary LOCC. Prior exact computations of a single Heisenberg dimer and implicit many-body corollaries are potential priority risks; the main comparison source's complete text could not be inspected.

## References
1. B. T. Kiani, *Sharp universal death of entanglement threshold for Pauli Hamiltonians*, arXiv:2609.30149v1 (2026), https://arxiv.org/abs/2609.30149.
2. I. Marvian and D. A. Lidar, *Quantum error suppression with commuting Hamiltonians: Two local is too local*, arXiv:1410.5487 (2014), https://arxiv.org/abs/1410.5487.
3. A. Bouland, L. Mancinska, and X. Zhang, *Complexity Classification of Two-Qubit Commuting Hamiltonians*, https://theory.stanford.edu/~abouland/Papers/commuting_hamiltonians.pdf.
4. M. Horodecki, P. Horodecki, and R. Horodecki, *Separability of mixed states: necessary and sufficient conditions*, Physics Letters A **223** (1996), 1–8, DOI:10.1016/S0375-9601(96)00706-2.
5. R. Horodecki and M. Horodecki, *Information-theoretic aspects of inseparability of mixed states*, Physical Review A **54** (1996), 1838, DOI:10.1103/PhysRevA.54.1838.
