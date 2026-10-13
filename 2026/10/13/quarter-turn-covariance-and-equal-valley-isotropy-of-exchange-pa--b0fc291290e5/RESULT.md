# Quarter-turn covariance and equal-valley isotropy of exchange-pair effective masses
## Finding
Let \(R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\) denote a quarter-turn on the quasi-momentum torus. For the square-lattice exchange-interaction Hamiltonian of Bru, de Siqueira Pedra and Ramer dos Santos, assume the interaction data satisfy the quarter-turn symmetry imposed in the source. Let \(E(U,k)\) be the lowest dressed-pair dispersion, for \(U\in[0,\infty]\).

At every \(k\) where \(E(U,\cdot)\) is twice differentiable,
\[
E(U,Rk)=E(U,k),\qquad
\nabla E(U,Rk)=R\nabla E(U,k),\qquad
H_U(Rk)=R H_U(k)R^{\mathsf T},
\]
where \(H_U(k)=\operatorname{Hess}_k E(U,k)\). Wherever \(H_U(k)\) is invertible, the tensor mass \(m_U(k)=H_U(k)^{-1}\) satisfies
\[
m_U(Rk)=R m_U(k)R^{\mathsf T}.
\]

Let \(K_x=[(\pi,0)]\) and \(K_y=[(0,\pi)]\) be the corresponding points of \(\mathbb T^2\). Since \(K_y=RK_x\),
\[
\frac{H_U(K_x)+H_U(K_y)}2
=\frac{\operatorname{tr}H_U(K_x)}2 I_2.
\]
If the two mass tensors exist, then also
\[
\frac{m_U(K_x)+m_U(K_y)}2
=\frac{\operatorname{tr}m_U(K_x)}2 I_2.
\]
Thus an individual valley may have an anisotropic quadratic dispersion or mass tensor, but the equal-weight laboratory-frame average over the quarter-turn-related valley pair is exactly isotropic.

## Assumptions and scope
The statement uses the source model on the square lattice with its quarter-turn-invariant hopping/interaction data. The dispersion must be \(C^2\) at the quasi-momenta where a Hessian is asserted; the tensor-mass statement additionally requires the Hessian to be invertible. The source's regularity results supply the required differentiability under its corresponding smoothness hypotheses on the interaction form factors. The two points \(K_x\) and \(K_y\) are understood as torus classes, so boundary representatives such as \((\pi,0)\) and \((0,-\pi)\) are equivalent.

No assertion is made that a physical state must populate the two valleys equally. The isotropy statement is conditional on equal weights, and it concerns the quadratic laboratory-frame response obtained by averaging the two symmetry-related tensors.

## Proof
Quarter-turn invariance of the full Hamiltonian intertwines the translation fibers: the rotation unitary maps the fiber at \(k\) unitarily onto the fiber at \(Rk\). The lowest spectral value is therefore invariant,
\[
E(U,Rk)=E(U,k).
\]
For finite \(U\) this follows directly from fiber covariance. The hard-core identity follows by passing this equality through the source's \(U\to\infty\) fiber limit.

At a point of differentiability, differentiate \(E(U,Rk)=E(U,k)\). Since \(R\) is orthogonal,
\[
R^{\mathsf T}\nabla E(U,Rk)=\nabla E(U,k),
\]
which is equivalent to \(\nabla E(U,Rk)=R\nabla E(U,k)\). Differentiating once more gives
\[
R^{\mathsf T}H_U(Rk)R=H_U(k),
\]
and hence \(H_U(Rk)=R H_U(k)R^{\mathsf T}\). If \(H_U(k)\) is invertible, inversion preserves orthogonal conjugacy:
\[
H_U(Rk)^{-1}=R H_U(k)^{-1}R^{\mathsf T}.
\]

Finally, every real symmetric matrix \(A=\begin{pmatrix}a&b\\b&c\end{pmatrix}\) obeys
\[
RAR^{\mathsf T}=\begin{pmatrix}c&-b\\-b&a\end{pmatrix},
\qquad
A+RAR^{\mathsf T}=(a+c)I_2=(\operatorname{tr}A)I_2.
\]
Applying this identity first to \(A=H_U(K_x)\) and then, when defined, to \(A=m_U(K_x)\) proves the two equal-valley formulas.

## Verification
The verification is symbolic and does not rely on finite sampling. It checks the chain from global quarter-turn symmetry to unitary fiber covariance, from fiber covariance to invariance of the lowest dispersion, and then uses the ordinary chain rule twice. The only matrix computation needed for isotropy is the displayed exact multiplication for an arbitrary real symmetric \(2\times2\) matrix. The hard-core extension uses the same equality before taking the source's hard-core limit.

The source defines the effective dispersion and its Hessian-based tensor mass and proves the differentiability required under its stated smoothness assumptions. The conclusion is therefore conditional only on those regularity and invertibility hypotheses, not on a numerical approximation to the dispersion.

## Relationship to prior work
Bru, de Siqueira Pedra and Ramer dos Santos establish the square-lattice model, impose quarter-turn symmetry on the interaction data, develop the dressed-pair dispersion, and define the associated tensor mass. Their discussion notes that the rotational hypothesis is used mainly for other technical purposes and for unconventional pairing; the inspected dispersion and mass statements do not formulate the tensor-covariance or equal-valley isotropy identities above.

An earlier isotropic bipolaron--fermion exchange model and a related 2018 doctoral thesis treat the cuprate-motivated momenta near \((\pi,0)\) and \((0,\pi)\) and include special effective-mass calculations. Those calculations are narrower than the present structural statement: the argument above applies directly to the generalized exchange/Hubbard model and permits anisotropic single-valley tensors, while proving exact isotropy only after the symmetry-related pair is averaged with equal weights.

## Limitations
The result does not determine the eigenvalues of either single-valley mass tensor, prove positivity or invertibility of the Hessian, or establish equal valley occupation in a many-body state. It also does not claim that every anisotropy disappears beyond quadratic order. Its content is the exact covariance law and the resulting two-valley quadratic isotropy forced by quarter-turn symmetry.

A residual literature risk is that the same tensor identity may have appeared in older condensed-matter work under valley-symmetry terminology even though no covering statement was found in the inspected primary source, the inspected earlier special-model literature, or targeted searches.

## References
1. J.-B. Bru, W. de Siqueira Pedra, A. Ramer dos Santos, *Scattering and Pairing by Exchange Interactions*, arXiv:2404.15039; first public version 2024-04-23. https://arxiv.org/abs/2404.15039
2. J.-B. Bru, W. de Siqueira Pedra, A. Ramer dos Santos, journal version of the same work, DOI: 10.1017/fms.2025.10083.
3. J.-B. Bru et al., *Isotropic Bipolaron--Fermion Exchange Theory and Unconventional Pairing in Cuprate Superconductors*, Annalen der Physik, DOI: 10.1002/andp.201700235.
4. A. Delgado de Pasquale, doctoral thesis (2018), University of São Paulo repository: https://teses.usp.br/teses/disponiveis/43/43134/tde-03052018-150652/publico/Tesis.pdf
