# Open-boundary twist convergence for primitive SU(2)-symmetric matrix product states

## Finding

For every fixed-bond-dimension, one-site translation-invariant, exactly \(SU(2)\)-covariant matrix-product-state tensor with a primitive normalized transfer matrix and fixed open-boundary vectors whose leading norm-transfer coefficient is nonzero, the normalized expectation of the squared twist operator
\[
U_L^2=\exp\!\left[\frac{4\pi i}{L}\sum_{j=1}^{L}jS_j^z\right]
\]
satisfies
\[
\langle U_L^2\rangle=1+O(L^{-1})\qquad (L\to\infty).
\]
The implicit constant may depend on the tensor and the fixed boundary vectors.

## Assumptions and scope

Let \(A^m\in\mathbb C^{D\times D}\) be a fixed one-site MPS tensor for a finite-dimensional integer-spin on-site representation, with physical basis index \(m\). Assume exact covariance under rotations about the \(z\)-axis:
\[
\sum_n [e^{i\theta S^z}]_{mn}A^n
=V_\theta A^mV_\theta^{-1},\qquad V_\theta=e^{i\theta G},
\]
where \(V_\theta\) is the virtual representation induced by the physical \(SU(2)\) symmetry. In particular, \(V_{4\pi}=I\). Assume the normalized transfer matrix
\[
T_0=\sum_m\overline{A^m}\otimes A^m
\]
has a simple eigenvalue \(1\), with every other eigenvalue strictly inside the unit disk. Its normalized fixed point is full rank. The open-boundary state is
\[
|\Psi_L\rangle=\sum_{m_1,\ldots,m_L}
\ell^\dagger A^{m_1}\cdots A^{m_L}r\,|m_1,\ldots,m_L\rangle,
\]
with fixed boundary vectors \(\ell,r\), and the leading coefficient of its norm contraction is assumed nonzero. The expectation is normalized by \(\langle\Psi_L|\Psi_L\rangle\).

This is a statement about primitive, finite-bond-dimension symmetric MPS tensors and fixed open boundaries. It does not assert the same conclusion for every ground state of every gapped open spin chain.

## Proof

Put \(\delta=4\pi/L\) and \(\theta_j=j\delta\). By the covariance equation, the physical rotation at site \(j\) can be moved to virtual indices. Adjacent virtual rotations cancel except for the increment \(V_{\theta_j}^{-1}V_{\theta_{j+1}}=V_\delta\); the endpoint at \(\theta_L=4\pi\) is the identity. Consequently the twisted overlap is represented by a boundary contraction of the constant twisted transfer matrix
\[
T_\delta=\sum_m\overline{A^m}\otimes V_\delta A^m,
\]
up to boundary factors analytic in \(\delta\) and equal to their untwisted values at \(\delta=0\). The norm uses \(T_0\).

Because the eigenvalue \(1\) of \(T_0\) is simple, analytic matrix perturbation gives a unique eigenvalue \(\lambda(\delta)\) near \(1\), with \(\lambda(0)=1\). In canonical transfer-matrix normalization, its first derivative is
\[
\lambda'(0)=i\,\operatorname{Tr}(\rho G),
\]
where \(\rho\) is the normalized virtual fixed point. Covariance of \(T_0\) and uniqueness of \(\rho\) imply that \(\rho\) commutes with the virtual \(SU(2)\) representation. Thus \(\rho\) is scalar on each irreducible spin block, while the generator \(G\) is traceless on each such block. Hence \(\operatorname{Tr}(\rho G)=0\), so
\[
\lambda(\delta)=1+O(\delta^2).
\]

The remaining transfer spectrum stays uniformly inside a circle of radius \(\kappa<1\) for sufficiently small \(\delta\). The leading boundary coefficient is analytic and nonzero at \(\delta=0\), so its ratio to the untwisted coefficient is \(1+O(\delta)\). Therefore the normalized overlap is
\[
\frac{\langle\Psi_L|U_L^2|\Psi_L\rangle}
{\langle\Psi_L|\Psi_L\rangle}
= \bigl(1+O(\delta)\bigr)\lambda(\delta)^L+O(\kappa^L).
\]
Since \(\lambda(\delta)^L=1+O(L\delta^2)\) and \(\delta=4\pi/L\), the right-hand side is \(1+O(L^{-1})\). This proves the claim.

## Verification

The critical cancellation is the vanishing of the first-order transfer-eigenvalue shift, \(\operatorname{Tr}(\rho G)=0\), forced by \(SU(2)\) invariance; without it, the factor \(\lambda(4\pi/L)^L\) need not approach \(1\). The simple dominant eigenvalue and the nonzero boundary coefficient are needed to control the transfer asymptotics and the normalization. The proof establishes the \(O(L^{-1})\) rate but does not determine its coefficient. No finite-size computation is used as a substitute for the asymptotic argument.

## Relationship to prior work

Su, Yao, and Furusaki prove the squared-twist criterion for gapped \(SO(3)\)-symmetric chains with periodic boundary conditions and give explicit open-boundary calculations for the Majumdar–Ghosh and AKLT states. Their discussion identifies a rigorous open-boundary argument for a broader class as an open direction. The present statement is narrower than such a general Hamiltonian theorem: it covers primitive, finite-bond-dimension symmetric MPS tensors with fixed boundaries, and its proof uses the MPS transfer matrix rather than a spectral-gap argument for arbitrary Hamiltonians.

Pérez-García, Verstraete, Wolf, and Cirac develop the canonical and transfer-matrix formalism for MPS, including open-boundary representations and parent Hamiltonians. That formalism is background for the proof; the claim here is the slow-twist \(O(L^{-1})\) asymptotic under the stated open-boundary assumptions.

## Limitations

The estimate is not uniform over families of tensors or boundary vectors. It does not cover nonprimitive transfer matrices, noninjective symmetry-breaking MPS, boundary data whose leading norm-transfer coefficient vanishes, tensors with only a smaller symmetry group, or arbitrary open-boundary ground states not represented by the specified exact MPS class. It supplies no explicit \(L^{-1}\) coefficient and does not prove a converse gap diagnostic.

## References

1. H. Su, Y. Yao, and A. Furusaki, “Identification of gapless phases by squaring a twist operator,” arXiv:2506.02496v1 (first public version, 2025-06-03); see the squared-twist theorem, the open-boundary discussion, and the supplementary Majumdar–Ghosh and AKLT calculations. https://arxiv.org/abs/2506.02496
2. D. Pérez-García, F. Verstraete, M. M. Wolf, and J. I. Cirac, “Matrix Product State Representations,” arXiv:quant-ph/0608197v2 (2007); see the MPS transfer-matrix, canonical-form, and open-boundary sections. https://arxiv.org/abs/quant-ph/0608197
