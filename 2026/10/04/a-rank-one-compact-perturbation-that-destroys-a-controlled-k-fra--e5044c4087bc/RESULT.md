# A rank-one compact perturbation that destroys a controlled \(K\)-frame
## Finding
The compact-perturbation conclusion of Theorem 3.7 in Rajput--Sahu--Mishra is false as stated. Compactness of the difference between synthesis operators does not, by itself, preserve the controlled \(K\)-frame property. The failure occurs already for ordinary Hilbert-space frames, with \(C=K=I\), and with a rank-one perturbation.

Let \(H=\ell^2(\mathbb N)\) with canonical orthonormal basis \((e_n)_{n\ge 1}\). Define
\[
F=(e_1,e_2,e_3,\ldots),
\qquad
G=(e_2,e_2,e_3,e_4,\ldots).
\]
Then \(F\) is a Parseval controlled \(K\)-frame for \(C=K=I\), every vector in \(G\) is nonzero and has norm one, and \(T_F-T_G\) has rank one. Nevertheless \(G\) is not a frame because \(e_1\) is orthogonal to every member of \(G\).

## Assumptions and scope
The example is taken in the scalar Hilbert-space specialization of Hilbert \(C^*\)-modules, so all module-valued inequalities reduce to the ordinary frame inequalities. Set \(C=I\) and \(K=I\). The auxiliary commutation and range hypotheses appearing with the theorem are then automatic.

The conclusion concerns the theorem as printed in the cited article and its arXiv version. It does not assert that no compact perturbation can preserve a controlled \(K\)-frame; rather, it shows that compactness alone is insufficient.

## Proof
Let \((\delta_n)_{n\ge1}\) denote the standard orthonormal basis of the coefficient space \(\ell^2(\mathbb N)\). The synthesis operator of \(F\) is
\[
T_F(c_1,c_2,\ldots)=\sum_{n\ge1}c_ne_n.
\]
For \(G\),
\[
T_G(c_1,c_2,\ldots)=c_1e_2+\sum_{n\ge2}c_ne_n.
\]
Hence
\[
(T_F-T_G)c=c_1(e_1-e_2).
\]
The range of \(T_F-T_G\) is therefore contained in the one-dimensional space \(\operatorname{span}\{e_1-e_2\}\). Thus \(T_F-T_G\) is rank one and, in particular, compact.

On the other hand,
\[
T_G^*e_1=0,
\]
because every member of \(G\) lies in \(\operatorname{span}\{e_n:n\ge2\}\). Therefore
\[
\sum_{n\ge1}|\langle e_1,g_n\rangle|^2=0,
\]
so no positive lower frame bound can hold for \(G\). Thus \(G\) is not a frame, and hence is not an \(I\)-controlled \(I\)-frame.

The perturbation is not merely compact: it is rank one. Equivalently, \(T_G(\delta_1-\delta_2)=0\), so the compact perturbation has destroyed surjectivity of the synthesis operator.

A standard quantitative repair is available in the ordinary Hilbert-frame case. If \(F\) has frame bounds \(A,B\), write \(E=T_F-T_G\). Since \(T_F^*\) is bounded below by \(\sqrt A\),
\[
\|T_G^*f\|
\ge
\|T_F^*f\|-\|E^*f\|
\ge
(\sqrt A-\|E\|)\|f\|.
\]
Therefore, whenever \(\|E\|<\sqrt A\), the sequence \(G\) is a frame with valid lower bound
\[
(\sqrt A-\|E\|)^2.
\]
Similarly,
\[
\|T_G^*f\|\le(\sqrt B+\|E\|)\|f\|,
\]
so \((\sqrt B+\|E\|)^2\) is a valid upper bound.

## Verification
Every step is symbolic. The original sequence is an orthonormal basis, the perturbed sequence misses the direction \(e_1\), and the synthesis-operator difference is explicitly rank one. No finite experiment or numerical approximation is used.

The counterexample also stress-tests possible hidden edge cases: the perturbed atoms are all nonzero and have unit norm; the perturbation has finite rank; and the controlling and target operators are both identities. Thus the failure cannot be attributed to exotic module geometry, zero atoms, or an unbounded perturbation.

## Relationship to prior work
Rajput, Sahu, and Mishra state in Theorem 3.7 that a nonzero sequence remains a controlled \(K\)-frame when the difference of the synthesis operators is compact, under their accompanying range and commutation assumptions. The example above satisfies those assumptions in the scalar specialization but violates the conclusion.

Earlier frame-perturbation results use quantitative hypotheses rather than arbitrary compactness. Christensen--Heil establish stability under suitable perturbation bounds, and Han--Jing--Mohapatra extend perturbation theory to Hilbert \(C^*\)-modules under explicit control conditions. Those results do not imply the compactness-only assertion and are consistent with the rank-one counterexample.

## Limitations
The counterexample disproves compactness-only stability. It does not identify the weakest possible repair in the full Hilbert \(C^*\)-module setting. The displayed small-norm repair is asserted only for the ordinary Hilbert-frame specialization, where the analysis-operator lower bound gives the estimate directly.

A residual literature risk is that an unindexed correction, thesis remark, or informal note may already record this specific failure. No such correction was found in the checked source versions or targeted searches.

## References
1. E. Rajput, N. K. Sahu, V. N. Mishra, *Controlled K-frames in Hilbert C*-modules*, Korean Journal of Mathematics 30 (2022), 91--107. DOI: 10.11568/kjm.2022.30.1.91. Preprint: arXiv:1903.09928.
2. O. Christensen, C. Heil, *Perturbations of Banach Frames and Atomic Decompositions*, Mathematische Nachrichten 185 (1997), 33--47. DOI: 10.1002/mana.3211850104.
3. D. Han, W. Jing, R. N. Mohapatra, *Perturbation of frames and Riesz bases in Hilbert C*-modules*, Linear Algebra and its Applications 431 (2009), 1295--1303. DOI: 10.1016/j.laa.2009.03.025.
