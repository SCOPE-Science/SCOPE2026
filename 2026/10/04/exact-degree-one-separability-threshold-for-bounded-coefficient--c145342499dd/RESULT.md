# Exact degree-one separability threshold for bounded-coefficient Pauli Gibbs states

## Finding
Let a finite Pauli Hamiltonian be written as
\[
H=\sum_i J_iP_i,
\]
where each \(P_i\) is a nonidentity Hermitian Pauli string, \(|J_i|\le J\), and the term-overlap graph joins two terms exactly when their supports share a qubit. If this graph has maximum degree at most one, then the exact universal full-separability threshold is
\[
\beta J\le z_1^*:=\operatorname{arctanh}(\sqrt2-1)=\frac12\log(1+\sqrt2)\approx0.4406867935.
\]
At and below this threshold every Gibbs state is a convex mixture of product Pauli eigenstates. Above it, the two-qubit commuting Hamiltonian
\[
H_*=-J(X\otimes X+Z\otimes Z)
\]
already has an entangled Gibbs state. Hence degree one has a finite sharp boundary distinct from the \(\Delta\ge2\) tree-recursion regime.

## Assumptions and scope
The statement uses the same term-overlap graph and coefficient cap as arXiv:2609.30149v1. Zero-coefficient terms may be discarded. A two-term component whose Pauli strings are proportional is treated as an effective one-string Hamiltonian and is separable at every temperature. The claim concerns finite systems and full separability across the physical qubits; it does not address the sampling complexity of an explicit decomposition.

## Proof
Because the term-overlap graph has maximum degree at most one, every connected component contains either one term or two terms. Distinct connected components act on disjoint sets of physical qubits, so the Gibbs state tensor-factorizes across those components. It therefore suffices to prove full separability for every one- and two-term component.

First use the following elementary Pauli-mixture lemma. For any nonidentity Hermitian Pauli string \(R\),
\[
\tau_R^{\pm}:=2^{-n}(I\pm R)
\]
is fully separable: choose local eigenbases for the nonidentity one-qubit Paulis in \(R\), and average uniformly over product eigenvectors whose eigenvalue parity is \(\pm1\); identity factors may be averaged in any local basis. Consequently,
\[
2^{-n}\!\left(I+\sum_k c_kR_k\right)
\]
is fully separable whenever the \(R_k\) are nonidentity Hermitian Pauli strings and \(\sum_k|c_k|\le1\), since it is the convex combination of the maximally mixed state and the corresponding \(\tau_{R_k}^{\operatorname{sgn}(c_k)}\).

For a one-term component \(H=aP\),
\[
\rho_\beta=2^{-n}\bigl(I-\tanh(\beta a)P\bigr),
\]
so the lemma gives separability for every \(\beta\).

Now consider a genuine two-term component \(H=aP+bQ\) with \(|a|,|b|\le J\). Hermitian Pauli strings either commute or anticommute. If \(P\) and \(Q\) are proportional, the Hamiltonian reduces to one Pauli string and is already covered. Otherwise, when they commute, \(PQ\) is again a nonidentity Hermitian Pauli string and
\[
\rho_\beta=2^{-n}(I-t_aP)(I-t_bQ),\qquad t_a=\tanh(\beta a),\quad t_b=\tanh(\beta b).
\]
Let \(t=\tanh(\beta J)\). The sum of the absolute nonidentity Pauli coefficients is at most
\[
|t_a|+|t_b|+|t_at_b|\le2t+t^2.
\]
At \(\beta J\le z_1^*\), one has \(t\le\sqrt2-1\), and
\[
2(\sqrt2-1)+(\sqrt2-1)^2=1.
\]
The Pauli-mixture lemma therefore proves full separability for every commuting two-term component.

If \(P\) and \(Q\) anticommute, set \(r=\sqrt{a^2+b^2}\). Since \((aP+bQ)^2=r^2I\),
\[
\rho_\beta=2^{-n}\!\left[I-\frac{\tanh(\beta r)}{r}(aP+bQ)\right].
\]
The absolute Pauli-coefficient sum is
\[
\frac{\tanh(\beta r)}{r}(|a|+|b|)\le\beta(|a|+|b|)\le2\beta J.
\]
At the proposed threshold,
\[
2z_1^*=\log(1+\sqrt2)<1,
\]
so the same lemma proves full separability for every anticommuting two-term component. Tensoring the component decompositions gives a fully separable Gibbs state for the entire Hamiltonian.

It remains to prove sharpness. For
\[
H_*=-J(X\otimes X+Z\otimes Z),\qquad t=\tanh(\beta J),
\]
the two Pauli terms commute and overlap, so the term-overlap graph is a single edge. The Gibbs state is
\[
\rho_*=\frac14\bigl(I+tX\otimes X+tZ\otimes Z-t^2Y\otimes Y\bigr).
\]
Partially transposing the second qubit flips the sign of the \(Y\)-term, giving
\[
\rho_*^{T_2}=\frac14\bigl(I+tX\otimes X+tZ\otimes Z+t^2Y\otimes Y\bigr).
\]
In the Bell basis its eigenvalues are
\[
\frac{1+2t-t^2}{4},\qquad \frac{1+t^2}{4},\qquad \frac{1+t^2}{4},\qquad \frac{1-2t-t^2}{4}.
\]
The last eigenvalue is negative exactly when \(t>\sqrt2-1\), equivalently when \(\beta J>z_1^*\). A separable state cannot have a negative partial transpose, so \(\rho_*\) is entangled above the threshold. The lower-bound proof already includes equality, completing the exact threshold.

## Verification
The included checker evaluates the closed-form constant, verifies the identity \(2t+t^2=1\) at \(t=\sqrt2-1\), tests the commuting and anticommuting coefficient bounds throughout the coefficient box, and checks the sign change of the explicit witness's smallest partial-transpose eigenvalue on both sides of the threshold. These computations are consistency checks; the proof above is analytic and does not depend on finite sampling.

## Relationship to prior work
arXiv:2609.30149v1 proves an exact universal threshold for maximum term-overlap degree \(\Delta\ge2\), and its theorem explicitly excludes degree one. Its weighted corollary applies more generally but, for degree one and \(|J_i|\le J\), gives only the sufficient condition \(\beta J\le1/(4e)\), not the sharp boundary above. Earlier high-temperature separability results of Bakshi, Liu, Moitra, and Tang and of Putterman, Zlokapa, and Cotler provide constant-temperature or degree-scaled sufficient bounds rather than this exact degree-one completion.

The distinction is structural: maximum degree zero has no entangling transition at any finite temperature because all Hamiltonian terms have disjoint supports, while maximum degree one already admits the single-edge witness above and therefore has the finite threshold \(z_1^*\). Targeted searches did not locate a prior theorem stating this universal degree-one boundary. The exact thermal threshold of particular two-qubit models may have appeared elsewhere; originality here is the universal maximum-overlap-degree-one theorem and its match to the omitted boundary of arXiv:2609.30149v1.

## Limitations
The theorem is specific to the coefficient cap \(|J_i|\le J\) and maximum term-overlap degree at most one. It does not supply an optimal weighted analogue for unequal coefficients, an efficient sampler, or a new result for \(\Delta\ge2\). The literature search cannot exclude a differently phrased older observation, especially for the particular two-qubit witness, so priority is asserted only for the universal degree-one completion found by the stated searches.

## References
1. B. T. Kiani, “Sharp universal death of entanglement threshold for Pauli Hamiltonians,” arXiv:2609.30149v1, first public 2026-09-24.
2. A. Bakshi, A. Liu, A. Moitra, and E. Tang, “High-Temperature Gibbs States are Unentangled and Efficiently Preparable,” arXiv:2403.16850.
3. H. Putterman, A. Zlokapa, and J. Cotler, “When quantum thermal states look classical,” arXiv:2607.28536v1.
