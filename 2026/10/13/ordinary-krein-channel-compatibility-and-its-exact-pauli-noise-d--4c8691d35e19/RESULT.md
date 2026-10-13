# Ordinary/Krein channel compatibility and its exact Pauli-noise distance
## Finding
Let \(\mathcal H_A\) and \(\mathcal H_B\) be finite-dimensional complex Hilbert spaces. Let \(J_A\) and \(J_B\) be self-adjoint unitaries, so that
\[
J_A^2=I_A,\qquad J_B^2=I_B.
\]
Following the complete \(J\)-positivity convention for linear maps in Heo's work, a map
\[
\Phi:\mathcal B(\mathcal H_A)\longrightarrow\mathcal B(\mathcal H_B)
\]
is completely \((J_A,J_B)\)-positive if
\[
\Xi_\Phi(X)=J_B\Phi(J_AX)
\]
is ordinarily completely positive. There is no trace-preservation requirement in this definition.

**Compatibility theorem.** The following conditions on \(\Phi\) are equivalent:

1. \(\Phi\) is both ordinarily completely positive and completely \((J_A,J_B)\)-positive.
2. \(\Phi\) is ordinarily completely positive and obeys the strong intertwining identity
   \[
   \Phi(J_AX)=J_B\Phi(X)\quad\text{for every }X.
   \]
3. \(\Phi\) has an ordinary Kraus representation
   \[
   \Phi(X)=\sum_\alpha K_\alpha X K_\alpha^\dagger,
   \qquad J_BK_\alpha=K_\alpha J_A\quad\text{for every }\alpha.
   \]
Equivalently, its ordinary Choi matrix is positive semidefinite and supported on the \(+1\) eigenspace of
\[
\Gamma=J_A^{\mathsf T}\otimes J_B.
\]
In particular, for every trace-preserving compatible map and every density operator \(\rho\), the fundamental-sector populations are conserved:
\[
\operatorname{Tr}\!\left[P_B^\pm\Phi(\rho)\right]
=\operatorname{Tr}\!\left[P_A^\pm\rho\right],
\qquad P_A^\pm=\frac{I_A\pm J_A}{2},\quad
P_B^\pm=\frac{I_B\pm J_B}{2}.
\]

**Qubit classification.** Fix \(J_A=J_B=Z=\operatorname{diag}(1,-1)\). All ordinary CPTP maps that are also \(J\)-completely positive are exactly
\[
\boxed{
\Phi_c\!\begin{pmatrix}a&b\\d&e\end{pmatrix}
=\begin{pmatrix}a&cb\\\overline c d&e\end{pmatrix},
\qquad |c|\le1.
}
\]
Thus the compatible physical qubit channels form the closed phase-damping disk; no population transfer is possible, while coherences may be attenuated and phase rotated.

**Sharp Pauli-noise separation.** For any Pauli probabilities
\[
q_I,q_X,q_Y,q_Z\ge0,\qquad q_I+q_X+q_Y+q_Z=1,
\]
write
\[
\mathcal P=q_I\operatorname{id}
+q_X\operatorname{Ad}_X
+q_Y\operatorname{Ad}_Y
+q_Z\operatorname{Ad}_Z,
\quad\operatorname{Ad}_U(\rho)=U\rho U^\dagger.
\]
In the *unhalved* diamond norm, the exact distance to the compatible physical class is
\[
\boxed{
\inf_{|c|\le1}\|\mathcal P-\Phi_c\|_\diamond
=2(q_X+q_Y).
}
\]
One optimal compatible channel is
\[
\Phi_*=(q_I+q_X)\operatorname{id}+(q_Z+q_Y)\operatorname{Ad}_Z.
\]
In particular, when
\[
\mathcal D_p(\rho)=(1-p)\rho+p\operatorname{Tr}(\rho)I/2,
\qquad 0\le p\le1,
\]
its Pauli probabilities are \(q_X=q_Y=q_Z=p/4\), so the exact distance is \(p\). With the alternative half-diamond-distance convention, every displayed diamond distance is divided by two.

## Assumptions and scope
The operator \(J\) is a fixed self-adjoint involution; changing the fundamental symmetry changes the compatible channel class. Ordinary completely positive maps are in the Schrödinger-picture convention \(\Phi(X)=\sum KXK^\dagger\). The general equivalence allows different finite input and output dimensions and does not require trace preservation. The population identity and qubit/Pauli results explicitly require ordinary trace preservation.

The notion of complete \(J\)-positivity used here is exactly the source's *left-multiplication* convention \(X\mapsto J_B\Phi(J_AX)\), not a stronger or weaker definition based on conjugation by \(J\). The theorem does not assert that every quantum \(J\)-channel is an ordinary physical quantum channel: it classifies their intersection.

## Proof
Fix orthonormal bases and let \(C_\Phi\) be the ordinary, unnormalized Choi matrix
\[
C_\Phi=\sum_{i,j}|i\rangle\langle j|\otimes\Phi(|i\rangle\langle j|).
\]
Put \(\Gamma=J_A^{\mathsf T}\otimes J_B\). A direct expansion of the source's twisting definition gives
\[
C_{\Xi_\Phi}=\Gamma C_\Phi.
\]
Both \(J_A^{\mathsf T}\) and \(J_B\) are Hermitian involutions, so \(\Gamma\) is a Hermitian involution.

Suppose \(\Phi\) is both ordinary CP and \(J\)-CP. By the Choi theorem,
\[
C_\Phi\succeq0,\qquad \Gamma C_\Phi\succeq0.
\]
The second matrix is Hermitian, and hence
\[
\Gamma C_\Phi=(\Gamma C_\Phi)^\dagger=C_\Phi\Gamma.
\]
Thus \(C_\Phi\) commutes with \(\Gamma\). Its restriction to the \(-1\) eigenspace of \(\Gamma\) is simultaneously positive semidefinite and, after multiplication by \(\Gamma\), negative semidefinite. It therefore vanishes. Hence
\[
\Gamma C_\Phi=C_\Phi,
\qquad
C_\Phi=P_+C_\Phi P_+,
\quad P_+=\frac{I+\Gamma}{2}.
\]
Because the Choi correspondence is injective, \(C_{\Xi_\Phi}=C_\Phi\) implies \(\Xi_\Phi=\Phi\), which is exactly
\[
\Phi(J_AX)=J_B\Phi(X).
\]
Conversely, if \(\Phi\) is ordinarily CP and this intertwining identity holds, then \(\Xi_\Phi=\Phi\) is CP, so \(\Phi\) is \(J\)-CP. This proves the first two conditions are equivalent.

Diagonalizing the positive Choi matrix yields Kraus vectors \(|K_\alpha\rangle\rangle\) lying in the support of \(C_\Phi\). With the input-first vectorization convention,
\[
\Gamma|K\rangle\rangle
=|J_BKJ_A\rangle\rangle.
\]
Thus every Kraus vector in the \(+1\) eigenspace satisfies \(J_BK_\alpha J_A=K_\alpha\), or equivalently \(J_BK_\alpha=K_\alpha J_A\). Conversely, intertwining Kraus operators produce Choi vectors in the \(+1\) eigenspace and hence both positivity properties. This proves the third condition.

For trace-preserving \(\Phi\), the Kraus normalization is \(\sum_\alpha K_\alpha^\dagger K_\alpha=I_A\). Intertwining gives
\[
P_B^\pm K_\alpha=K_\alpha P_A^\pm,
\]
and therefore
\[
\sum_\alpha K_\alpha^\dagger P_B^\pm K_\alpha
=P_A^\pm\!\left(\sum_\alpha K_\alpha^\dagger K_\alpha\right)P_A^\pm=P_A^\pm.
\]
Tracing against any \(\rho\) proves exact sector-population conservation.

In the qubit case \(J_A=J_B=Z\), the matrix equation \(ZK=KZ\) says precisely that every Kraus operator is diagonal. Thus \(|0\rangle\langle0|\) and \(|1\rangle\langle1|\) are fixed, and \(|0\rangle\langle1|\) is multiplied by some complex \(c\). Trace preservation and Cauchy--Schwarz for the two diagonal Kraus coefficient columns give \(|c|\le1\). Conversely, every \(|c|\le1\) is achieved by the diagonal Kraus operators
\[
K_0=\operatorname{diag}(1,\overline c),
\qquad
K_1=\operatorname{diag}(0,\sqrt{1-|c|^2}),
\]
which are normalized and intertwine with \(Z\). This proves the disk classification.

For the diamond-norm bound let \(t=q_X+q_Y\). Every compatible \(\Phi_c\) fixes \(|0\rangle\langle0|\), whereas
\[
\mathcal P(|0\rangle\langle0|)
=(1-t)|0\rangle\langle0|+t|1\rangle\langle1|.
\]
Testing the diamond norm on this unentangled density matrix gives
\[
\|\mathcal P-\Phi_c\|_\diamond\ge
\|t(|1\rangle\langle1|-|0\rangle\langle0|)\|_1=2t.
\]
Now \(\Phi_*=(q_I+q_X)\operatorname{id}+(q_Z+q_Y)\operatorname{Ad}_Z\) is a CPTP mixture of commuting diagonal unitaries, so it is compatible. Direct subtraction gives
\[
\mathcal P-\Phi_*
=q_X(\operatorname{Ad}_X-\operatorname{id})
+q_Y(\operatorname{Ad}_Y-\operatorname{Ad}_Z).
\]
Each difference of two channels has diamond norm at most two. The triangle inequality therefore yields \(\|\mathcal P-\Phi_*\|_\diamond\le2t\). With the lower bound, this proves the exact minimum. The depolarizing specialization is immediate.

## Verification
The compatibility theorem uses an exact equality of two Choi matrices and positivity of a Hermitian involution times a positive matrix. The Pauli minimum follows from a single computational-basis witness and a matching explicit compatible channel; there is no numerical minimization or finite extrapolation.

The standalone checker constructs ordinary and twisted Choi matrices for representative complex qubit coherence factors, verifies their positive support and Kraus normalization, checks incompatibility of a bit-flip unitary, and verifies the exact matching Pauli-channel upper/lower witnesses for rational parameter choices. The full finite-dimensional theorem is proved symbolically above rather than inferred from these tests.

## Relationship to prior work
Heo's 2026 article establishes the correspondence between complete \(J\)-positivity and complete positivity of a twisted map, and gives a sufficient condition: if \(\Phi(J_AX)=J_B\Phi(X)\), then ordinary and \(J\)-complete positivity coincide. Its Remark 2.8 gives Choi and twisted-positivity characterizations. The present result supplies the missing *necessity* when a map satisfies both positivity notions, in the stronger form of an exact support/Kraus classification, and quantifies how far a generic physical Pauli channel lies from that intersection.

Heo's earlier *Quantum J-channels on Krein spaces* develops \(J\)-Kraus and \(J\)-Choi theory, gives examples of qubit indefinite symmetries, and investigates entanglement breaking and \(J\)-separability. Felipe-Sosa and Felipe introduce the \(J\)-state and \(J\)-channel framework. Those sources supply indispensable definitions and representation results, but do not give the simultaneous ordinary/\(J\)-complete-positivity cone, the qubit phase-damping disk as that intersection, or its sharp Pauli diamond-distance law.

The Pauli-channel metric calculation uses the standard operational diamond norm of channel discrimination. Its role here is specific to the new compatibility class rather than a claim to a new general theory of diamond norms.

## Limitations
The theorem is finite dimensional, with fixed fundamental symmetries. The qubit disk and the sharp metric are specifically for equal input/output qubit symmetry \(Z\) and for Pauli-diagonal noise; no formula is claimed for arbitrary coherent, non-Pauli channels or for general higher-dimensional distances. The physical trace-preserving intersection should not be confused with the larger class of \(J\)-channels, which need not be ordinary completely positive. The distance uses the unhalved diamond-norm convention.

A related result might appear in literature under symmetry-preserving quantum operations or superselection rules rather than \(J\)-positive maps, despite the source- and alias-specific comparisons.

## References
1. J. Heo, *Completely J-positive (bi-)linear maps on Krein spaces and their Choi J-matrices*, Filomat 40(4), 1449–1462 (2026), DOI 10.2298/FIL2604449H, first public 2026-02-09.
2. J. Heo, *Quantum J-channels on Krein spaces*, Quantum Information Processing 22, Article 16 (2023), DOI 10.1007/s11128-022-03771-8 (online 2022-12-12).
3. R. Felipe-Sosa and R. Felipe, *J-states and quantum channels between indefinite metric spaces*, arXiv:2009.07759v3 (2021), later published in Quantum Information Processing 21 (2022).
