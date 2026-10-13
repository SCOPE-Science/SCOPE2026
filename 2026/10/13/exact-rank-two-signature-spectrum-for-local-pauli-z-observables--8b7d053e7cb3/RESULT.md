# Exact rank-two signature spectrum for local Pauli \(Z\) observables
## Finding
Let \(n\ge 2\), let \(Z_i\) denote Pauli \(Z\) on qubit \(i\), and let \(\Lambda_2(Z_1,\ldots,Z_n)\) be the joint rank-two numerical range: \(\lambda\in\mathbb R^n\) belongs to it when a rank-two projector \(P\) satisfies \(PZ_iP=\lambda_iP\) for every \(i\). Then every attainable vector obeys
\[
\sum_{i=1}^n \lambda_i^2\le n-2.
\]
Moreover the rank-two signature spectrum, the set of Euclidean norms of attainable compression vectors, is exactly
\[
\Sigma_2(Z_1,\ldots,Z_n)=[0,\sqrt{n-2}].
\]
The upper bound follows from an exterior-square identity: for an orthonormal code basis \(\psi_0,\psi_1\), write \(\psi_0\wedge\psi_1=\sum_{x<y}p_{xy}|x\wedge y\rangle\). Scalar compression gives \(\lambda_i^2=\sum_{x<y}|p_{xy}|^2(-1)^{x_i+y_i}\); summing over \(i\) yields the convex average \(\sum_{x<y}|p_{xy}|^2(n-2d_H(x,y))\le n-2\). Equality in this bound occurs exactly when every pair \(x,y\) carrying nonzero Pluecker weight has Hamming distance one. Sharpness of every radius is obtained by fixing \(n-2\) one-qubit factors with arbitrary \(Z\)-expectations and using on the final two qubits the Bell subspace \(\operatorname{span}\{|\Phi^+\rangle,|\Psi^+\rangle\}\), on which both local \(Z\) observables have zero compression.

## Assumptions and scope
For \(n\ge 2\), work on \(\mathcal H_n=(\mathbb C^2)^{\otimes n}\). For each \(i\), \(Z_i\) is the usual Pauli \(Z\) on qubit \(i\) and identity elsewhere. The joint rank-two numerical range is
\[
\Lambda_2(Z_1,\ldots,Z_n)=\{{\lambda\in\mathbb R^n: \exists P,\;P=P^*=P^2,\;\operatorname{{rank}}P=2,\;PZ_iP=\lambda_iP\;\forall i\}}.
\]
Its signature spectrum is \(\Sigma_2=\{{\|\lambda\|_2:\lambda\in\Lambda_2\}}\). No claim is made here about the complete vector set \(\Lambda_2\) for general \(n\), only its exact Euclidean-norm image and the stated universal quadratic bound.

## Proof
Let \(\psi_0,\psi_1\) be an orthonormal basis of the range of a projector \(P\) realizing \(\lambda\). Set \(w=\psi_0\wedge\psi_1\), a unit vector in \(\bigwedge^2\mathcal H_n\). In the computational basis write
\[
w=\sum_{{x<y}}p_{{xy}}|x\wedge y\rangle,
\qquad \sum_{{x<y}}|p_{{xy}}|^2=1,
\]
where \(x,y\in\{{0,1\}}^n\) and the order is arbitrary but fixed.

For any operator \(A\), the exterior-square identity gives
\[
\langle w,(\bigwedge^2 A)w\rangle
=\det\big(\langle\psi_a,A\psi_b\rangle\big)_{{a,b=0}}^1.
\]
Applying this to \(A=Z_i\) and using \(PZ_iP=\lambda_iP\) yields
\[
\lambda_i^2=\langle w,(\bigwedge^2 Z_i)w\rangle.
\]
Because \(Z_i|x\rangle=(-1)^{{x_i}}|x\rangle\), the wedge basis diagonalizes \(\bigwedge^2 Z_i\), so
\[
\lambda_i^2=\sum_{{x<y}}|p_{{xy}}|^2(-1)^{{x_i+y_i}}.
\]
Summing over \(i\) gives
\[
\sum_{{i=1}}^n\lambda_i^2
=\sum_{{x<y}}|p_{{xy}}|^2\sum_{{i=1}}^n(-1)^{{x_i+y_i}}
=\sum_{{x<y}}|p_{{xy}}|^2\bigl(n-2d_H(x,y)\bigr).
\]
Every pair in the wedge expansion has \(x\ne y\), hence \(d_H(x,y)\ge1\), proving \(\sum_i\lambda_i^2\le n-2\). Since the weights are nonnegative and sum to one, equality holds exactly when every pair with \(p_{{xy}}\ne0\) has \(d_H(x,y)=1\).

It remains to prove that every radius allowed by the bound occurs. On the final two qubits let
\[
\mathcal B=\operatorname{{span}}\{|\Phi^+\rangle,|\Psi^+\rangle\}.
\]
The compressions of \(Z\otimes I\) and \(I\otimes Z\) to \(\mathcal B\) both vanish. On each of the first \(n-2\) qubits choose a unit vector \(u_i\) with \(\langle u_i|Z|u_i\rangle=t_i\), where \(t_i\in[-1,1]\). The two-dimensional code
\[
\left(\bigotimes_{{i=1}}^{{n-2}}u_i\right)\otimes\mathcal B
\]
therefore has compression vector \( (t_1,\ldots,t_{{n-2}},0,0)\). Thus an embedded cube \([-1,1]^{{n-2}}\times\{{(0,0)\}}\) lies in \(\Lambda_2\), and its Euclidean norms fill every value from \(0\) to \(\sqrt{{n-2}}\). Together with the upper bound this proves \(\Sigma_2=[0,\sqrt{{n-2}}]\).

## Verification
The determinant identity is basis-independent and follows directly from the definition of the exterior-square representation. The computational-basis eigenvalue of \(\bigwedge^2 Z_i\) on \(|x\wedge y\rangle\) is exactly \((-1)^{{x_i+y_i}}\); summing these signs over coordinates gives \(n-2d_H(x,y)\). The Bell-subspace construction can be checked directly: each local \(Z\) maps \(|\Phi^+\rangle\) and \(|\Psi^+\rangle\) into the orthogonal Bell states \(|\Phi^-\rangle\) and \(|\Psi^-\rangle\), so both compressions are zero. For \(n=3\), the formula reduces to \(\Sigma_2=[0,1]\), consistent with the published exact octahedral range.

## Relationship to prior work
Sun, Cao, Poon, and Zeng define the signature spectrum as the Euclidean norm image of a joint higher-rank numerical range and, for the local three-qubit tuple \((Z_1,Z_2,Z_3)\), prove the exact rank-two octahedron. Their appendix gives general diagonal lower and half-space upper bounds but applies them to that three-qubit classification. The present statement supplies an all-\(n\) exact radial theorem for the natural local-\(Z\) family, using an exterior-square/Hamming-distance identity not stated in the inspected source.

Earlier work on Pauli joint higher-rank numerical ranges provides general classification and construction frameworks for Pauli tuples. Those frameworks are relevant background, but the inspected records did not state the all-\(n\) radial formula \(\Sigma_2=[0,\sqrt{{n-2}}]\) or the quadratic bound proved here. A 2025/2026 study of Knill--Laflamme signature vectors develops the norm invariant for full code-error families and exact ranges for selected codes, rather than this local-\(Z\) tuple.

## Limitations
The theorem does not determine the full set \(\Lambda_2(Z_1,\ldots,Z_n)\) for \(n\ge4\), nor does it treat ranks other than two or additional Pauli errors. The equality condition stated for the quadratic bound is a condition on the Pluecker support of a realizing two-plane; no complete classification of equality codes up to local or Clifford equivalence is claimed. A broad 2018 Pauli-classification paper was available through abstract-level material but not inspected in full text, so an equivalent formula hidden there remains a residual literature risk.

## References
1. B. Sun, N. Cao, Y. T. Poon, B. Zeng, “Geometry of Knill–Laflamme Coefficients for Pauli Error Detection,” arXiv:2610.01992v1 (2026).
2. M. Du, C. Zhang, Y. T. Poon, B. Zeng, “Characterizing quantum codes via the coefficients in Knill-Laflamme conditions,” npj Quantum Information 12, 13 (2026), DOI 10.1038/s41534-025-01155-1.
3. S. A. Mousavi, A. Salemi, “Joint higher rank numerical range of Pauli group,” Linear and Multilinear Algebra 63 (2015), 439–454, DOI 10.1080/03081087.2013.872638.
4. H. R. Afshin, M. A. Mehrjoofard, A. Zare Chavoshi, “Pauli group: Classification and joint higher rank numerical range,” Linear Algebra and its Applications 549 (2018), 136–152, DOI 10.1016/j.laa.2018.03.008.
