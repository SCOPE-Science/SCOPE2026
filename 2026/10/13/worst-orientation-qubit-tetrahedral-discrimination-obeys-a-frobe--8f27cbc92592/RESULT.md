# Worst-orientation qubit tetrahedral discrimination obeys a Frobenius-norm law

## Finding
Let \(\Phi\) be any qubit quantum channel, represented on Bloch vectors by the real affine map \(r\mapsto Tr+t\), where \(T\in\mathbb R^{3\times3}\). Let \(v_1=(1,1,1)/\sqrt3\), \(v_2=(1,-1,-1)/\sqrt3\), \(v_3=(-1,1,-1)/\sqrt3\), and \(v_4=(-1,-1,1)/\sqrt3\). For \(R\in SO(3)\), write \(\rho_j(R)=(I+(Rv_j)\cdot\sigma)/2\). The four input states have equal prior probabilities. If \(P_{\rm guess}(R)\) is the largest correct-identification probability over all four-outcome POVMs on the channel output, then
\[
\boxed{\min_{R\in SO(3)}P_{\rm guess}(R)=\frac14\left(1+\frac{\|T\|_{\rm F}}{\sqrt3}\right).}
\]
The translation \(t\) does not affect this worst-orientation value. An attaining orientation is any \(R\in SO(3)\) for which \(R^TT^TTR\) is diagonal. If \(\|T\|_{\rm F}>0\), these and only these orientations attain the minimum; if \(T^TT\) has distinct eigenvalues, there are exactly 24 such proper rotations of the labeled tetrahedral frame.

## Assumptions and scope
All calculations use trace-one qubit density matrices \(\rho=(I+r\cdot\sigma)/2\) with the three Pauli matrices \(\sigma\). A quantum channel is completely positive and trace preserving; its Bloch representation is affine and sends the unit ball into itself. Each of the four input states is used with prior probability \(1/4\). The same freely chosen input unitary realizes each proper rotation \(R\). After that rotation and the known channel, the decoder may optimize an arbitrary POVM. The displayed minimum is the **worst** over encoding orientations, not the best encoding fidelity. No ancilla or multiple channel uses are included. The Frobenius norm is \(\|T\|_{\rm F}=\sqrt{\operatorname{tr}(T^TT)}\).

## Proof
Write \(y_j=TRv_j\) and \(x_j=t+y_j\). The qubit ensemble consists of \(\tau_j=(I+x_j\cdot\sigma)/2\). Minimum-error discrimination has the finite-dimensional dual optimization \(P_{\rm guess}(R)=\min\{\operatorname{tr}H:H\ge\tau_j/4\text{ for all }j\}\). Parametrize a Hermitian dual variable by \(H=((1+s)I+c\cdot\sigma)/8\). Its four semidefinite inequalities are equivalent, using the eigenvalues of a Bloch-form Hermitian matrix, to \(s\ge\|c-x_j\|\) for every \(j\). Its trace is \((1+s)/4\). Thus
\[
P_{\rm guess}(R)=\frac{1+\mathcal R(x_1,x_2,x_3,x_4)}4,
\]
where \(\mathcal R\) is the radius of the smallest Euclidean enclosing ball of the four output Bloch vectors. This is the standard qubit geometric discrimination reduction; the contribution below is its exact optimization over all input orientations.

The regular tetrahedron satisfies
\[
\sum_{j=1}^4v_j=0,\qquad\frac14\sum_{j=1}^4v_jv_j^T=\frac13I_3.
\]
Consequently \(\sum_jy_j=0\) and, for every candidate enclosing center \(c\in\mathbb R^3\),
\[
\frac14\sum_{j=1}^4\|x_j-c\|^2
=\frac{\operatorname{tr}(T^TT)}3+\|t-c\|^2.
\]
Every enclosing ball has radius at least \(\alpha=\|T\|_{\rm F}/\sqrt3\); therefore \(P_{\rm guess}(R)\ge(1+\alpha)/4\) uniformly over \(R\).

Take an orthonormal eigenbasis of the positive semidefinite matrix \(T^TT\), adjusting one vector's sign so the eigenbasis matrix \(R\) has determinant one. Then \(A=R^TT^TTR\) is diagonal. Since each coordinate of every tetrahedral vertex has squared magnitude \(1/3\),
\[
\|TRv_j\|^2=v_j^TAv_j=\frac{\operatorname{tr}A}3=\alpha^2
\]
for all four \(j\). Hence the ball centered at \(t\) with radius \(\alpha\) contains every output Bloch vector and attains the lower bound, proving the formula. For \(\alpha>0\), an explicit attaining measurement is
\[
M_j=\frac14\left(I+\frac{TRv_j}{\alpha}\cdot\sigma\right),\qquad j=1,\ldots,4.
\]
Each effect is positive semidefinite, \(\sum_jM_j=I\), and direct substitution gives \(\tfrac14\sum_j\operatorname{tr}(M_j\tau_j)=(1+\alpha)/4\). For \(\alpha=0\) take \(M_j=I/4\); all outputs are identical.

For necessity, if an orientation attains the lower bound, any minimum enclosing center must equal \(t\), since the averaged squared radius at center \(c\) is \(\alpha^2+\|c-t\|^2\). All four radii must therefore equal \(\alpha\). Writing \(A=(a_{ij})=R^TT^TTR\), equality of the four quantities \(v_j^TAv_j\) gives four equations with the four Walsh sign triples \((s_1s_2,s_1s_3,s_2s_3)\). Subtracting these equations forces \(a_{12}=a_{13}=a_{23}=0\). Conversely diagonality already gave equality. If the three eigenvalues are distinct, there are \(3!\) eigenvector orderings and four sign patterns with positive determinant, hence 24 attaining rotations. This establishes the complete optimizer characterization.

## Verification
Run `python verification/verify.py` with Python 3 and NumPy. It checks the tetrahedral tight-frame identities, diagonal-eigenframe construction, actual qubit POVM positivity and completeness, the attained success probability, and geometric enclosing-ball radii computed independently from all affinely independent support sets. Eight physical channels are checked, with 36 pseudorandom orientations each. Output terminates with `VERIFY_OK channel_cases=8 random_rotations=288 frame_and_POVM=passed geometric_minimax=passed`. The finite checks are corroborative only: the theorem follows from the preceding duality, tight-frame and equality arguments for all CPTP qubit channels.

## Relationship to prior work
Bae and Hwang (arXiv:1204.2313) give the minimum-enclosing-ball formulation of arbitrary fixed qubit-ensemble discrimination, including examples of regular polyhedra. That theorem is used explicitly above and is not claimed as new. The additional quantified question is the exact **minimum over all common tetrahedral orientations** after an arbitrary anisotropic affine qubit channel, with the Frobenius invariant and full equality characterization. Clarke and collaborators describe the ideal tetrahedral detection experiment without this noise-orientation optimization. The literature comparison does not certify priority against every equivalent formulation.

## Limitations
The result concerns single-copy minimum-error discrimination of four equiprobable tetrahedral preparations, with a common input rotation and optimized output POVM. It does not solve best-orientation encoding, unequal priors, collective multi-copy decoding, higher-dimensional SICs, or an unknown channel. The expression for the worst orientation does not quantify a practical receiver constrained to a fixed measurement. Literature expressed in terms of spherical code geometry or channel contractions may contain an equivalent optimization not identified in the available comparisons.

## References
1. J. Bae and W.-Y. Hwang, “Optimal Discrimination of Qubit States – Methods, Solutions, and Properties,” arXiv:1204.2313, first publicly posted 2012-04-11; Phys. Rev. A 87, 012334 (2013).
2. R. B. M. Clarke et al., “Experimental realization of optimal detection strategies for overcomplete states,” Phys. Rev. A 64, 012303 (2001), arXiv:quant-ph/0011032.
