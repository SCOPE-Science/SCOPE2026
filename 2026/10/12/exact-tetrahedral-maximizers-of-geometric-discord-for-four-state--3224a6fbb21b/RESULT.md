# Exact tetrahedral maximizers of geometric discord for four-state qubit QRAC ensembles
## Finding
For four equally likely pure qubit encodings \(\rho_a\), indexed by \(a\in\{00,01,10,11\}\), let \(r_a\in\mathbb S^2\) be their Bloch vectors and consider the classical--quantum state
\[
\rho=\frac14\sum_a \rho_a\otimes |a\rangle\langle a|.
\]
For Hilbert--Schmidt geometric discord measured on the qubit subsystem, in the normalization used by Yao et al., define the \(3\times3\) matrix \(G\) appearing in the standard qubit--qudit formula. Then
\[
G=\frac14\sum_a r_a r_a^{\mathsf T},
\qquad
D_G=\frac18\left(1-\lambda_{\max}(G)\right).
\]
Consequently
\[
D_G\le \frac1{12}.
\]
The bound is attained, and equality holds exactly when
\[
\sum_a r_a r_a^{\mathsf T}=\frac43 I_3.
\]
Equivalently, the four Bloch vectors are a unit-norm tight frame in \(\mathbb R^3\). For four unit vectors in three dimensions this is equivalent to a signed regular tetrahedron: after independently replacing any subset of the \(r_a\) by their antipodes, the resulting four vectors are the vertices of a regular tetrahedron.

This also gives an exact operational separation from optimal \(2\to1\) QRAC coding. For every geometric-discord maximizer, the best uniform-average two-bit recovery success is at most
\[
P_{\mathrm{av}}\le \frac12+\frac1{2\sqrt3},
\]
and equality occurs for an unflipped regular tetrahedron with a suitable labeling. Since
\[
\frac12+\frac1{2\sqrt3}<\frac12+\frac1{2\sqrt2},
\]
no geometric-discord maximizer can be an optimal \(2\to1\) QRAC.

## Assumptions and scope
The four encoding states are pure qubit states with equal prior probability \(1/4\), exactly the four-state ensemble used in the cited \(2\to1\) QRAC analysis. Geometric discord is the squared Hilbert--Schmidt distance to the zero-discord set, measured on the qubit subsystem, with the normalization in which the cited paper writes \(D_G=\frac18(1-\lambda_{\max}(G))\) for this \(2\otimes4\) state. The QRAC comparison uses uniform inputs and optimizes over binary qubit measurements for the fixed four encodings.

The result does not assert that Hilbert--Schmidt geometric discord is a monotone under arbitrary local operations, and it does not address mixed encoding states, nonuniform priors, or other QRAC dimensions.

## Proof
Choose any orthonormal basis \(W_1,W_2,W_3\) of the diagonal traceless Hermitian \(4\times4\) matrices, normalized by \(\operatorname{Tr}(W_jW_k)=2\delta_{jk}\), and write \(w_{j,a}\) for the \(a\)-th diagonal entry of \(W_j\). Completeness in the three-dimensional traceless diagonal subspace gives
\[
\sum_{j=1}^3 w_{j,a}w_{j,b}=2\left(\delta_{ab}-\frac14\right).
\]
Let \(S=\sum_a r_a\). In the qubit--qudit Bloch normalization used in the source,
\[
x=\frac14S,
\qquad
T_{ij}=\frac12\sum_a r_{a,i}w_{j,a}.
\]
Therefore
\[
TT^{\mathsf T}
 =\frac12\sum_a r_ar_a^{\mathsf T}-\frac18SS^{\mathsf T}.
\]
For qubit dimension \(m=2\) and classical-register dimension \(n=4\), the matrix entering geometric discord is \(G=xx^{\mathsf T}+\frac12TT^{\mathsf T}\). The two rank-one terms cancel, leaving
\[
G=\frac14\sum_a r_ar_a^{\mathsf T}.
\]
Because every \(r_a\) has unit norm, \(\operatorname{Tr}G=1\). Hence \(\lambda_{\max}(G)\ge1/3\), and the exact qubit--qudit formula yields \(D_G\le1/12\). Equality occurs if and only if all three eigenvalues of \(G\) are \(1/3\), equivalently \(\sum_a r_ar_a^{\mathsf T}=\frac43I_3\).

It remains to classify equality. Let \(R\) be the \(3\times4\) matrix whose columns are the four \(r_a\). Equality says \(RR^{\mathsf T}=\frac43I_3\). Thus the Gram matrix \(H=R^{\mathsf T}R\) has rank three, its three nonzero eigenvalues are \(4/3\), and its diagonal entries are all one. Consequently \(P=\frac34H\) is a rank-three orthogonal projection with diagonal entries \(3/4\). Its rank-one complement is \(I_4-P=uu^{\mathsf T}\), and the diagonal condition forces \(|u_a|=1/2\). Writing \(u_a=s_a/2\) with \(s_a\in\{-1,1\}\), one obtains
\[
H_{ab}=-\frac13s_as_b\quad(a\ne b).
\]
After the antipodal replacements \(r_a\mapsto s_ar_a\), all six pairwise inner products equal \(-1/3\), exactly the Gram matrix of a regular tetrahedron. The converse is immediate because signs do not change \(r_ar_a^{\mathsf T}\).

For the QRAC comparison, put the labels in the order \(00,01,10,11\) and define the two Walsh sign vectors
\[
w_1=(1,1,-1,-1)^{\mathsf T},\qquad
w_2=(1,-1,1,-1)^{\mathsf T}.
\]
For fixed qubit encodings, optimizing each binary measurement gives
\[
P_{\mathrm{av}}=\frac12+\frac1{16}\left(\|Rw_1\|+\|Rw_2\|\right).
\]
At a discord maximizer, the Gram form above gives
\[
\|Rw_j\|^2
=w_j^{\mathsf T}Hw_j
=\frac{16}3-\frac13(w_j^{\mathsf T}s)^2
\le\frac{16}3,
\]
so \(P_{\mathrm{av}}\le\frac12+\frac1{2\sqrt3}\). Choosing \(s=(1,1,1,1)^{\mathsf T}\) makes both displayed inner products vanish and attains the bound. The standard optimal \(2\to1\) QRAC value is \(\frac12+\frac1{2\sqrt2}\), which is strictly larger.

## Verification
The identity for \(G\), the equality characterization, and the QRAC ceiling are analytic. The bundled `verify.py` uses exact rational arithmetic for the regular-tetrahedron second moment, the signed-tetrahedron Gram formula, and all sixteen sign choices; it verifies the maximum Walsh-sum squared norm \(16/3\), the discord value \(1/12\), and the strict algebraic comparison with the optimal \(2\to1\) QRAC value. It prints `VERIFY_OK` on success.

The finite enumeration over sixteen signs is only a replay of the already-proved equality-classification parameter \(s\in\{-1,1\}^4\); it is not used as a substitute for an infinite-state-space proof.

## Relationship to prior work
Yao et al. derive the geometric-discord matrix \(G\), prove the general eigenvalue bound \(D_G\le1/12\), and then state that arbitrary Bloch-sphere encodings are technically difficult; their Appendix reports numerical simulations whose discord values approach \(1/12\). They also report numerically that maximal geometric discord does not coincide with optimal \(2\to1\) QRAC. The present result closes that specific analytic gap: it identifies \(G\) as the second-moment frame operator of the four Bloch vectors, proves exact attainability, classifies every maximizer, and gives an exact QRAC-performance ceiling for those maximizers.

Mančinska and Storgaard later develop Bloch-space geometry for QRAC success-probability bounds and characterize optimality conditions for QRAC constructions. Their paper does not discuss geometric discord, and its statements do not imply the frame-operator identity, the signed-tetrahedron discord maximizers, or the \(1/2+1/(2\sqrt3)\) ceiling restricted to maximal-discord encodings.

## Limitations
The theorem is specific to equal-prior pure four-state qubit encodings and to squared Hilbert--Schmidt geometric discord. The literature search found no implication-equivalent statement in the inspected sources or semantic database, but absence from those searches is not a proof of global bibliographic uniqueness. The source itself notes known interpretational limitations of Hilbert--Schmidt geometric discord, so the result is a precise geometric and QRAC-comparison theorem rather than a universal resource-theoretic claim.

## References
1. Y. Yao et al., “Quantum discord in quantum random access codes and its connection with dimension witness,” arXiv:1207.1275; Phys. Rev. A 86, 062310 (2012), DOI 10.1103/PhysRevA.86.062310.
2. L. Mančinska and S. A. L. Storgaard, “The geometry of Bloch space in the context of quantum random access codes,” arXiv:2106.00155; Quantum Information Processing 21, 143 (2022), DOI 10.1007/s11128-022-03470-4.
3. AMS, Mathematics Subject Classification 2020, entry 81P43: Quantum discord.
