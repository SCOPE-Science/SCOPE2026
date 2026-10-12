# A minimal exact uphill direction for termwise Hamiltonian-pool OVQITE
## Finding
Consider the exact operator-projected variational quantum imaginary-time evolution (OVQITE) equations with a termwise Hamiltonian pool \(S_H=\{O_k\}\), Hamiltonian \(H=\sum_k c_kO_k\), Jacobian \(J\), imaginary-time velocity vector \(v\), and regularized update
\[
(J^{\mathsf T}J+\lambda I)\dot\theta=J^{\mathsf T}v,
\qquad \lambda\ge0.
\]
There is a one-qubit, one-parameter, two-term instance for which the exact update is strictly uphill for every \(\lambda\ge0\). Take
\[
H=Y+Z,
\qquad
r=\frac{(-1,-2,-1)}{\sqrt6},
\qquad
n=\frac{(2,1,-4)}{\sqrt{21}},
\]
where \(r\) is the Bloch vector of the current pure state and the local ansatz is \(U_\theta=\exp[-i\theta(n\cdot\sigma)/2]\). At \(\theta=0\), the exact directional energy derivative of the OVQITE update is
\[
s_E=\frac{1}{5+14\lambda}>0.
\]
Thus every sufficiently small positive parameter step raises the exact energy, although exact imaginary-time evolution lowers it at rate \(-1\) at the same state.

Moreover, two nonconstant Hamiltonian-pool terms are minimal for strict uphill motion. If the pool has one term, \(H=cO\), then every exact Tikhonov-regularized least-squares direction has \(s_E\le0\); the same holds at \(\lambda=0\) for any least-squares solution.

## Assumptions and scope
The equations are the exact, untruncated OVQITE equations reviewed and used as the update rule in arXiv:2610.01954v1. No sampling noise, Majorana-propagation truncation, finite-difference error, or approximate linear solve is present. The claim concerns the local continuous direction selected by the least-squares normal equations. Strict positivity of \(s_E\) implies an energy increase for every sufficiently small positive step by differentiability.

The qubit algebra embeds in a fixed-parity sector of two fermionic modes. For Majoranas \(m_1,m_2,m_3,m_4\), set \(A=i m_1m_2\), \(B=i m_2m_3\), and \(C=i m_1m_3\). These are even quadratic Hermitian Majorana monomials and obey \(A^2=B^2=C^2=I\) together with \(AB=iC\), \(BC=iA\), and \(CA=iB\). On either parity sector they therefore realize a Pauli triple, so the two Hamiltonian terms may be taken as \(B\) and \(C\). A fixed Gaussian conjugation rotates a single bilinear generator to the axis \(n\), so the one-parameter local family can be implemented by fixed quadratic-Majorana rotations surrounding one variable quadratic-Majorana rotation. This connects the obstruction directly to the length-two fermionic operator algebra used by VIME, but no claim is made about a particular molecular instance or about the source's compressed-tUPS parameterization.

## Proof
For a pure qubit with Bloch vector \(r\), rotation about the unit axis \(n\) gives the tangent \(r'(0)=n\times r\). Here
\[
n\times r=\frac{(-3,2,-1)}{\sqrt{14}}.
\]
Because the Hamiltonian pool is \(\{Y,Z\}\), the Jacobian is therefore
\[
J=\begin{pmatrix}\partial_\theta\langle Y\rangle\\[2pt]\partial_\theta\langle Z\rangle\end{pmatrix}
=\frac1{\sqrt{14}}\begin{pmatrix}2\\-1\end{pmatrix}.
\]
The current energy is \(E=\langle H\rangle=-3/\sqrt6\). Since \(\{Y,Y\}=\{Z,Z\}=2I\) and \(\{Y,Z\}=0\), the exact imaginary-time velocity formula
\[
v(O)=-\langle\{H,O\}\rangle+2E\langle O\rangle
\]
gives
\[
v_Y=-2+2E r_y=0,
\qquad
v_Z=-2+2E r_z=-1.
\]
Hence
\[
J^{\mathsf T}J=\frac5{14},
\qquad
J^{\mathsf T}v=\frac1{\sqrt{14}},
\qquad
\dot\theta=\frac{1/\sqrt{14}}{5/14+\lambda}.
\]
Because the Hamiltonian coefficients are \(c=(1,1)\),
\[
s_E=c^{\mathsf T}J\dot\theta
=\frac1{\sqrt{14}}\dot\theta
=\frac1{5+14\lambda}>0.
\]
On the other hand, \(H^2=2I\), so \(\operatorname{Var}(H)=2-E^2=1/2\), and exact imaginary-time evolution obeys
\[
\frac{d}{d\tau}\langle H\rangle=-2\operatorname{Var}(H)=-1.
\]
Thus the least-squares projection reverses the energy sign in this exact instance.

For minimality, suppose instead \(H=cO\) and write the single Jacobian row as \(j\). For \(\lambda>0\), the regularized solution satisfies
\[
j\dot\theta=\frac{\lVert j\rVert^2}{\lVert j\rVert^2+\lambda}v_O.
\]
Therefore
\[
s_E=c\,j\dot\theta
=\frac{\lVert j\rVert^2}{\lVert j\rVert^2+\lambda}v_H\le0,
\]
because \(v_H=-2\operatorname{Var}(H)\le0\). At \(\lambda=0\), if \(j=0\) then \(s_E=0\); if \(j\ne0\), every least-squares solution has \(j\dot\theta=v_O\), again giving \(s_E=v_H\le0\). Thus one nonconstant Hamiltonian term cannot produce strict uphill motion.

## Verification
The exact identities above were independently replayed by `artifacts/verify.py`. The script checks the normalized Bloch and rotation axes, the cross product, the two velocity components, \(J^{\mathsf T}J=5/14\), the sign of \(J^{\mathsf T}v\), the closed form \(s_E=1/(5+14\lambda)\), and the exact imaginary-time energy rate \(-1\). The script is corroborative; the proof is the symbolic derivation above.

## Relationship to prior work
Santona et al. (arXiv:2610.01954v1) define the termwise Hamiltonian pool, the regularized OVQITE normal equations, and the directional derivative \(s_E\). They explicitly state that \(J\dot\theta\) need not reproduce \(v\), so their VIME implementation tests whether \(s_E<0\) before stepping; their reported calculations can increase energy when this check fails. The present result isolates an exact smallest obstruction: even with exact observables and exact derivatives, two Hamiltonian terms already suffice for \(s_E>0\) for every regularization strength \(\lambda\ge0\).

The original OVQITE paper, arXiv:2409.12018v1, requires the Hamiltonian to lie in the span of the chosen operator set and studies Hamiltonian-derived operator pools. Its inspected text does not state an exact noise-free uphill example or a minimal term-count boundary. The one-term descent statement proved here is therefore used as a mathematical boundary of the present claim, not as an attribution to that paper.

## Limitations
The theorem is local and does not claim that VIME typically moves uphill, that Armijo-accepted VIME steps can increase energy, or that the source's molecular benchmarks are affected by this exact example. It does not quantify how often the obstruction occurs, nor does it establish a converse criterion for general pools. The two-mode fermionic embedding concerns the operator algebra and Gaussian accessibility; it is not asserted to be an end-to-end instance of a particular molecular c-tUPS calculation.

## References
1. F. Santona, M. G. Algaba, A. A. Anuar, A. M. Wernbacher, P. Sharma, and F. Šimkovic, *Hardware-Efficient Ground-State Preparation using Variational Imaginary-Time Majorana Evolution*, arXiv:2610.01954v1 (first public 2026-10-01).
2. A. A. Anuar, F. Jamet, F. Gironella, F. Šimkovic IV, and R. Rossi, *Operator-Projected Variational Quantum Imaginary Time Evolution*, arXiv:2409.12018v1; Journal of Physics A 59, 245301 (2026), DOI 10.1088/1751-8121/ae767d.
