# An endpoint cluster measurement increases a proposed pairwise mutual-information entanglement quantity
## Finding
For the four-qubit linear cluster state
\[
|C_4\rangle=CZ_{12}CZ_{23}CZ_{34}|+\rangle^{\otimes 4},
\]
consider the Paz-Silva--Reina probe
\[
\mathcal{F}r(i,j)=\frac12\bigl(S(\rho_i)+S(\rho_j)-S(\rho_{ij})\bigr)=\frac12 I(i:j)
\]
and its four-qubit arithmetic aggregate
\[
\mathcal M_{\mathcal{F}r}=\frac{2}{\binom42}\sum_{i<j}\mathcal{F}r(i,j)=\frac16\sum_{i<j}I(i:j).
\]
Then
\[
\mathcal M_{\mathcal{F}r}(|C_4\rangle)=\frac13.
\]
A computational-basis measurement of endpoint qubit \(1\) is a local operation. For either measurement outcome, the conditional pure state is a product of the measured endpoint with a three-qubit path graph state on qubits \(2,3,4\), up to a local Pauli correction, and
\[
\mathcal M_{\mathcal{F}r}=\frac12.
\]
Thus the average postmeasurement value is \(1/2>1/3\), with exact gap \(1/6\) and ratio \(3/2\). Consequently this pairwise mutual-information arithmetic quantity is not an LOCC entanglement monotone, already on pure four-qubit states.

## Assumptions and scope
All logarithms in the von Neumann entropy are base two. The claim concerns the arithmetic quantity built from the mutual-information probe in Eqs. (11)--(12) of Paz-Silva and Reina, not their quasi-concurrence probe, not their geometric aggregate, and not later total-correlation constructions. The local protocol is the standard selective projective measurement of qubit \(1\) in the computational basis, with the measurement outcome retained. Average LOCC monotonicity would require the initial value to be at least the probability-weighted average of the conditional values.

The four-qubit graph is the path \(1-2-3-4\). Its stabilizer generators are
\[
K_1=X_1Z_2,\qquad K_2=Z_1X_2Z_3,\qquad K_3=Z_2X_3Z_4,\qquad K_4=Z_3X_4.
\]

## Proof
For a graph state and a subsystem \(A\), the reduced state is the uniform sum of those stabilizers whose support is contained in \(A\). This follows directly by tracing the stabilizer expansion \(|C_4\rangle\langle C_4|=2^{-4}\sum_{g\in\mathcal S}g\).

Every one-qubit reduced state is maximally mixed, so \(S(\rho_i)=1\). On the pair \(\{1,2\}\), the only nonidentity stabilizer supported inside the pair is \(K_1\); hence
\[
\rho_{12}=\frac14(I+X_1Z_2),
\]
whose spectrum is \(\{1/2,1/2,0,0\}\), so \(S(\rho_{12})=1\) and \(I(1:2)=1\). Likewise \(K_4\) gives \(I(3:4)=1\). For each of the other four pairs there is no nonidentity stabilizer with support contained in that pair, so the reduced state is \(I/4\), its entropy is \(2\), and the pairwise mutual information is zero. Therefore
\[
\sum_{i<j}I(i:j)=2,
\qquad
\mathcal M_{\mathcal{F}r}(|C_4\rangle)=\frac16\cdot2=\frac13.
\]

Now measure qubit \(1\) in the \(Z\) basis. Each outcome has probability \(1/2\). Deleting the measured endpoint from a graph state leaves the path graph on \(2-3-4\), with at most a local \(Z_2\) byproduct depending on the outcome. Local Pauli operators do not change entropies or mutual informations. Qubit \(1\) is pure and product with the remaining three qubits, so every pair involving qubit \(1\) has mutual information zero.

For the three-qubit path, take generators
\[
L_2=X_2Z_3,\qquad L_3=Z_2X_3Z_4,\qquad L_4=Z_3X_4.
\]
The pair \(\{2,3\}\) contains \(L_2\), the pair \(\{3,4\}\) contains \(L_4\), and the pair \(\{2,4\}\) contains \(L_2L_4=X_2X_4\). In each case the pair reduced state has spectrum \(\{1/2,1/2,0,0\}\), while both one-qubit marginals are maximally mixed. Hence
\[
I(2:3)=I(2:4)=I(3:4)=1.
\]
Thus, for either measurement branch,
\[
\sum_{i<j}I(i:j)=3,
\qquad
\mathcal M_{\mathcal{F}r}=\frac16\cdot3=\frac12.
\]
Because both outcomes give the same value, the probability-weighted postmeasurement average is \(1/2\). This is strictly larger than the initial \(1/3\), proving failure of average LOCC monotonicity.

## Verification
The standalone script `verify_cluster_counterexample.py` reconstructs the four-qubit cluster density matrix with exact rational entries, takes exact partial traces, diagonalizes the one- and two-qubit reduced matrices symbolically, and repeats the calculation for both endpoint-measurement outcomes. It verifies the initial six mutual informations \(\{1,1,0,0,0,0\}\), the conditional six mutual informations \(\{1,1,1,0,0,0\}\), and prints

`VERIFY_OK initial_M=1/3 branch_M=1/2 average_post=1/2 gap=1/6 ratio=3/2`

The finite computation is a replay of the exact reduced-state calculation; the proof above supplies the dimension-specific analytic reason for every spectrum.

## Relationship to prior work
Paz-Silva and Reina define \(\mathcal{F}r\) as one half of the pairwise von Neumann mutual information and define the normalized arithmetic average over all pairs in Eqs. (11)--(12) of arXiv:quant-ph/0603102. For four qubits their normalization is \(2\), giving exactly the functional used here. The paper presents the arithmetic construction as an entanglement measure. Their follow-up arXiv:quant-ph/0610017 reports that LOCC nonincrease is established for registers up to three parties and says numerical calculations support LOCC nonincrease beyond that range. The explicit four-qubit cluster protocol above gives the opposite conclusion for the mutual-information arithmetic instance.

Targeted searches for the defining title, the follow-up title, the exact probe, pairwise mutual information on cluster states, and LOCC monotonicity did not locate a published statement implying this exact four-qubit counterexample. A later paper by the same authors, arXiv:quant-ph/0702177, develops a different total-correlation construction and is not used as evidence that the earlier pairwise arithmetic functional is monotone.

## Limitations
The result is an exact counterexample to one specified arithmetic functional. It does not address the quasi-concurrence probe, the geometric average, later repaired or total-correlation measures, mixed-state convex-roof behavior beyond what follows from the pure-state counterexample, or optimality of the numerical gap among all four-qubit states and local protocols. No claim is made that every pairwise-correlation aggregate must fail LOCC monotonicity.

## References
1. G. A. Paz-Silva and J. H. Reina, “Geometric multipartite entanglement measures,” arXiv:quant-ph/0603102, first public 11 March 2006; Physics Letters A 365, 64--69 (2007), DOI: 10.1016/j.physleta.2006.12.065.
2. G. A. Paz-Silva and J. H. Reina, “A pairwise additive strategy for quantifying multipartite entanglement,” arXiv:quant-ph/0610017, first public 3 October 2006.
3. G. A. Paz-Silva and J. H. Reina, “Total correlations as fully additive entanglement monotones,” arXiv:quant-ph/0702177; Journal of Physics A 42, 055306 (2009), DOI: 10.1088/1751-8113/42/5/055306.
