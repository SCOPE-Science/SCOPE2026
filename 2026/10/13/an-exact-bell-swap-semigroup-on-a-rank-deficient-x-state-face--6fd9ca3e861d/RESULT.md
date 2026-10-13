# An exact Bell-swap semigroup on a rank-deficient X-state face
## Finding
Let \(L\ge 1\). For each \(k=1,\ldots,L\), let the \(k\)-th oriented two-qubit link, in the basis \((|00\rangle,|01\rangle,|10\rangle,|11\rangle)\), be
\[
\rho_k=
\begin{pmatrix}
a_k&0&0&w_k\\
0&0&0&0\\
0&0&c_k&0\\
\overline{w_k}&0&0&d_k
\end{pmatrix},
\]
where \(a_k,c_k,d_k\ge 0\), \(a_k+c_k+d_k=1\), and \(|w_k|^2\le a_kd_k\). Arrange the links in an oriented chain and, at each intermediate node, project the right qubit of the left link and the left qubit of the right link onto \(|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2\), postselecting this outcome at every swap.

Define
\[
T_k=\begin{pmatrix}a_k&c_k\\0&d_k\end{pmatrix},
\qquad
T_L\cdots T_1=
\begin{pmatrix}A_L&C_L\\0&D_L\end{pmatrix},
\qquad
W_L=\prod_{k=1}^L w_k.
\]
Then the unnormalized end-to-end state is exactly
\[
\widetilde\rho_L=2^{1-L}
\begin{pmatrix}
A_L&0&0&W_L\\
0&0&0&0\\
0&0&C_L&0\\
\overline{W_L}&0&0&D_L
\end{pmatrix}.
\]
Its branch probability is
\[
p_L=2^{1-L}Z_L,
\qquad Z_L=A_L+C_L+D_L,
\]
and the normalized end state has concurrence
\[
\mathcal C_L=\frac{2|W_L|}{Z_L}.
\]
Consequently, if every link is entangled, equivalently \(w_k\ne0\) on this face, then \(p_L>0\) and \(\mathcal C_L>0\) for every finite \(L\). Thus this entire heterogeneous rank-deficient face has an infinite postselected entanglement horizon along the repeated \(|\Phi^+\rangle\) branch.

For identical links \((a,c,d,w)\),
\[
A_L=a^L,\qquad D_L=d^L,\qquad
C_L=c\sum_{j=0}^{L-1}a^{L-1-j}d^j,
\qquad W_L=w^L.
\]
The rank-three family in Trinh et al. is recovered by
\[
a=\frac12,\qquad c=\frac{1-s}{2},\qquad d=\frac{s}{2},\qquad w=\frac{\kappa\sqrt{s}}2.
\]
For this specialization the normalized output is exactly \(\rho_{s^L,\kappa^L}\), and \(\mathcal C_L=(\kappa\sqrt{s})^L\).

## Assumptions and scope
The theorem concerns finite chains of independent two-qubit density operators on the displayed face, with the link orientation fixed as stated. The positivity condition \(|w_k|^2\le a_kd_k\) is both necessary and sufficient for positivity of the nontrivial \((|00\rangle,|11\rangle)\) block together with the nonnegative population \(c_k\). The zero \(|01\rangle\) population makes every such link rank at most three. When \(w_k\ne0\), positivity forces \(a_kd_k>0\), so the successful branch has nonzero probability.

Only the repeated \(|\Phi^+\rangle\) branch is asserted. The result does not claim that every Bell outcome, every adaptive strategy, or an outcome-averaged state remains entangled. It also does not classify all rank-deficient two-qubit states.

## Proof
Consider first two links with parameters \((a,c,d,w)\) and \((a',c',d',w')\). Direct contraction of the middle qubits against \(|\Phi^+\rangle\) gives the unnormalized endpoint state
\[
\frac12
\begin{pmatrix}
aa'&0&0&ww'\\
0&0&0&0\\
0&0&a'c+c'd&0\\
\overline{ww'}&0&0&dd'
\end{pmatrix}.
\]
Thus the face is closed under the postselected swap. Its three diagonal parameters compose as
\[
\begin{pmatrix}a'&c'\\0&d'\end{pmatrix}
\begin{pmatrix}a&c\\0&d\end{pmatrix}
=
\begin{pmatrix}a'a&a'c+c'd\\0&d'd\end{pmatrix},
\]
while the corner coherence multiplies as \(w'w\), and one factor \(1/2\) is acquired per Bell projection.

Induction over the \(L-1\) intermediate measurements therefore yields the stated formula with \(T_L\cdots T_1\), \(W_L\), and the common factor \(2^{1-L}\). Taking the trace gives \(p_L=2^{1-L}Z_L\).

After normalization, the end state is again an X state with zero \(|01\rangle\) population. The standard X-state concurrence formula therefore reduces to
\[
\mathcal C_L=2\frac{|W_L|}{Z_L}.
\]
The same conclusion follows directly from the partial transpose. Its only potentially negative block is
\[
\frac1{Z_L}
\begin{pmatrix}0&W_L\\\overline{W_L}&C_L\end{pmatrix},
\]
whose smaller eigenvalue is
\[
\lambda_-=
\frac{C_L-\sqrt{C_L^2+4|W_L|^2}}{2Z_L}.
\]
It is strictly negative exactly when \(W_L\ne0\). Since \(W_L=\prod_k w_k\), all entangled links on this face yield an entangled endpoint for every finite chain length.

For identical links, the formula for \(C_L\) is the upper-right entry of \(T^L\). In the Trinh et al. specialization, \(c=a-d\), so
\[
C_L=a^L-d^L,
\qquad
Z_L=2a^L=2^{1-L}.
\]
Normalizing then gives diagonal entries \(1/2\), \((1-s^L)/2\), \(s^L/2\) and coherence \(\kappa^L\sqrt{s^L}/2\), exactly the published two-parameter family at depth \(L\).

## Verification
The proof is analytic. The accompanying `artifacts/verify.py` independently performs the Bell-state tensor contraction in the computational basis, rather than calling the triangular recurrence, and compares the result with the closed formula for heterogeneous chains of lengths one through three. It also checks positivity of the partial-transpose witness and the exact specialization to the Trinh et al. family at a longer depth. Running the file with the Python standard library returns `VERIFY_OK`.

The finite checks corroborate the algebra but are not used to infer the all-\(L\) theorem; the induction above supplies the infinite family of finite-length cases.

## Relationship to prior work
Trinh et al., arXiv:2609.11021v1, prove that full-rank two-qubit links have a finite entanglement-swapping horizon under arbitrary adaptive postselection, and contrast this with explicit rank-three and rank-two families that retain positive concurrence at every finite depth. Their rank-three example is precisely the specialization displayed above. The present result identifies a substantially larger closed face: arbitrary heterogeneous parameters \((a_k,c_k,d_k,w_k)\) with the same one-dimensional kernel pattern compose by a triangular matrix semigroup and remain entangled on the repeated \(|\Phi^+\rangle\) branch whenever every corner coherence is nonzero.

Muñoz, Grüning, and Roa, arXiv:1311.6784v1 and Phys. Rev. A 89, 064301 (2014), derive the general single-swap output formulas and concurrence thresholds for two X states. Their analysis supplies the natural broader X-state comparison, but it does not state the right-left chain-closed kernel face, the triangular product law for heterogeneous finite chains, or the resulting all-length persistence theorem.

Mondal, Zambare, and Santra, arXiv:2506.22245v1, study multi-parameter network-edge states and end-to-end concurrence statistically, emphasizing that fixed edge concurrence does not determine route quality. Their results concern distributions and averages over broader ensembles rather than the exact postselected branch law on this rank-deficient face.

## Limitations
The theorem gives a sufficient structural mechanism for infinite postselected range, not a necessary characterization of all rank-deficient links that can sustain long-range entanglement. It does not optimize branch probability, compare different Bell outcomes, or address adaptive correction strategies. The success probability may decay exponentially with \(L\), as it does in the published two-parameter example. No claim is made about non-postselected long-range entanglement.

## References
1. X. Du Trinh, N. Pardave, A. Huang, X. Meng, and N. Yu, “Full-Rank Noise Forbids Long-Range Entanglement Swapping,” arXiv:2609.11021v1 (2026).
2. A. Muñoz, G. Grüning, and L. Roa, “Entanglement-swapping for X-states demands threshold values,” arXiv:1311.6784v1; Phys. Rev. A 89, 064301 (2014), doi:10.1103/PhysRevA.89.064301.
3. M. S. Mondal, A. Zambare, and S. Santra, “End-to-end entanglement of quantum network paths with multi-parameter states,” arXiv:2506.22245v1 (2025).
