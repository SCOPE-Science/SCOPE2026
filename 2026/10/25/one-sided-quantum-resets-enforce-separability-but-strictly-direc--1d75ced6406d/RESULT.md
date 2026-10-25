# One-sided quantum resets enforce separability but strictly directional discord in an Ising dimer

## Finding

For a coherently coupled Ising qubit pair, a Poisson reset that erases **only the first qubit** produces a unique, full-rank stationary state that is separable and classical when measuring the *unreset second qubit*, yet has strictly positive quantum discord when measuring the *reset first qubit*. This holds for all nonzero Ising coupling and both nonzero local transverse drives, at every finite positive reset rate. In particular, global resetting and selective local resetting need not have the same entangling ability.

Let the physical coupling and drives be real numbers \(J,\Omega_1,\Omega_2\ne0\), let \(r>0\), and write \(X,Y,Z\) for the Pauli matrices and \(I\) for the identity. Set
\[
\Delta=(r^2+\Omega_1^2)(r^2+\Omega_2^2)+4J^2r^2,
\quad
u=\frac{\Omega_1 r(r^2+\Omega_2^2)}{\Delta},\quad
v=-\frac{r^2(r^2+\Omega_2^2+4J^2)}{\Delta},
\]
\[
s=-\frac{2J\Omega_1\Omega_2 r}{\Delta},\qquad
t=\frac{2J\Omega_1r^2}{\Delta}.
\]
The **sole** stationary density matrix is
\[
\boxed{\rho_*=\tfrac14\big(I\otimes I+uY\otimes I+vZ\otimes I+sX\otimes Y+tX\otimes Z\big).}
\]
Put \(m=(s^2+t^2)^{1/2}>0\), \(B=(sY+tZ)/m\), \(b=(u^2+v^2)^{1/2}>0\), and \(k=(b^2+m^2)^{1/2}\). The exact spectrum of \(\rho_*\) is \((1+k)/4\) twice and \((1-k)/4\) twice, with
\[
1-k^2=\frac{\Omega_1^2(r^2+\Omega_2^2)}{\Delta}>0.
\]
Its correlations obey: entanglement \(=0\); discord under projective measurements of qubit 2 \(=0\); discord under projective measurements of qubit 1 \(>0\); and
\[
I(1:2)=h\!\left(\frac{1+b}{2}\right)-h\!\left(\frac{1+k}{2}\right)>0,
\quad h(z)=-z\log z-(1-z)\log(1-z).
\]
This last expression uses natural logarithms and is the ordinary quantum mutual information.

## Assumptions and scope

The time-homogeneous two-qubit state evolves under the trace-preserving generator
\[
\mathcal L(\rho)=-i[H,\rho]+r\big(\lvert\downarrow\rangle\langle\downarrow\rvert\otimes\operatorname{tr}_1\rho-\rho\big),
\qquad
H=-JZ\otimes Z+\frac{\Omega_1}{2}X\otimes I+\frac{\Omega_2}{2}I\otimes X,
\]
where \(Z\lvert\downarrow\rangle=-\lvert\downarrow\rangle\). Each reset replaces only qubit 1 by its down state **without disturbing the marginal of qubit 2**. All amplitudes are finite and real; \(J\Omega_1\Omega_2\ne0\) and \(r>0\). Discord is the conventional entropy-based one-sided discord, vanishing precisely for states unchanged by a rank-one local projective dephasing on the measured qubit. No initial-state restriction is needed for the stationary classification.

## Proof

**1. Exact invariant-coefficient equations.** The real four-dimensional affine subspace spanned by \(I\otimes I,Y\otimes I,Z\otimes I,X\otimes Y,X\otimes Z\) is invariant under \(\mathcal L\). Its coefficients satisfy
\[
\dot u=-\Omega_1v-2Jt-ru,\qquad
\dot v=\Omega_1u-r(v+1),
\]
\[
\dot s=-\Omega_2t-rs,\qquad
\dot t=2Ju+\Omega_2s-rt.
\]
Setting their derivatives to zero gives successively \(s=-\Omega_2t/r\), \(t=2Jru/(r^2+\Omega_2^2)\), \(v=\Omega_1u/r-1\), and the displayed unique values of \(u,v,s,t\). Therefore the displayed \(\rho_*\) is stationary.

**2. Strict positivity and stationarity uniqueness.** The four traceless Hermitian Pauli strings in \(\rho_*\) anticommute pairwise and square to \(I\otimes I\). Their weighted sum squares to \(k^2 I\otimes I\), giving the doubled eigenvalues. Direct simplification gives \(1-k^2=\Omega_1^2(r^2+\Omega_2^2)/\Delta>0\). Hence \(\rho_*\) is a faithful density matrix, not merely a formal fixed point.

For uniqueness, use the legitimate Lindblad jump operators \(L_0=\sqrt r\lvert\downarrow\rangle\langle\uparrow\rvert\otimes I\) and \(L_1=\sqrt r\lvert\downarrow\rangle\langle\downarrow\rvert\otimes I\). If \(A\) lies in the kernel of the adjoint generator \(\mathcal L^\dagger\), the standard dissipative carré-du-champ identity is
\[
\mathcal L^\dagger(A^\dagger A)-\mathcal L^\dagger(A^\dagger)A-A^\dagger\mathcal L^\dagger(A)
=\sum_{j=0}^1[L_j,A]^\dagger[L_j,A].
\]
Taking its expectation against faithful \(\rho_*\), the left side has trace zero because \(\mathcal L(\rho_*)=0\) and \(A,A^\dagger\) are fixed. Positivity then forces \([L_j,A]=0\). The same argument for \(A^\dagger\) forces \([L_j^\dagger,A]=0\). The joint commutant of these first-qubit matrix units has precisely the form \(A=I\otimes C\). For such \(A\), the adjoint reset term vanishes; \([H,I\otimes C]=0\) requires simultaneously \([Z,C]=[X,C]=0\) since \(J\Omega_2\ne0\). Thus \(C\) is scalar. The adjoint kernel is one-dimensional; by equality of kernel dimensions for a finite square map and its adjoint, the stationary kernel is one-dimensional. Its normalized positive member is \(\rho_*\), proving uniqueness for the full sixteen-real-dimensional state space.

**3. Separable yet asymmetric correlations.** Define \(\Pi_\eta=(I+\eta B)/2\) for \(\eta=\pm1\). Since \(B^2=I\), these are orthogonal rank-one projectors and the exact identity
\[
\rho_*=\frac12\sum_{\eta=\pm1}
\left[\frac{I+uY+vZ+\eta mX}{2}\right]\otimes\Pi_\eta
\]
holds. The two qubit-1 factors are density matrices because their Bloch length is \(k<1\). Thus \(\rho_*\) is explicitly separable and remains unchanged by projective measurement \(\{\Pi_+,\Pi_-\}\) on the *second* qubit. Accordingly concurrence, negativity, and second-side discord all vanish.

On the first qubit, a rank-one local projective measurement preserving the state would imply \([\rho_*,(\boldsymbol n\cdot\boldsymbol\sigma)\otimes I]=0\) for a unit real vector \(\boldsymbol n\). Comparing independent second-qubit operators, the nonzero \(sY+tZ\) forces \(\boldsymbol n\) parallel to the \(X\) axis, whereas the nonzero first-qubit Bloch vector \(uY+vZ\) forces \(\boldsymbol n\) parallel to a perpendicular \(YZ\) direction. This is impossible. Hence first-side discord is strictly positive. Finally the second marginal is \(I/2\), the first marginal has Bloch length \(b\), and the full state has double spectrum determined by \(k>b\), giving the displayed strictly positive mutual information formula.

## Verification

The standalone program `one_sided_reset_verify.py` uses NumPy and SciPy to assemble the full \(16\times16\) Lindblad superoperator independently from matrix units, solve its normalized kernel, and compare it with the closed form. It passed 256 deterministic randomly selected nonzero parameter tuples, checking stationarity, uniqueness by full-matrix rank, full-rank spectrum, positivity under partial transpose, two-sided commutator tests, and the exact positivity identity. Execute `python one_sided_reset_verify.py` in an environment with NumPy and SciPy. Numerical tests are corroboration, not an infinite-parameter proof.

## Relationship to prior work

Kulkarni and Majumdar study the same basic interacting Ising dimer **with joint resetting of both spins to the initial product state**; their full-system reset can generate stationary entanglement [1]. Here the first-spin-only marginal-preserving reset is a different quantum channel and yields an exactly separable, strictly one-way-discordant stationary state. Magoni et al. investigate correlations from global resetting in a **noninteracting** spin ensemble [2], while Wald et al. analyze **discrete-time** resetting and few-qubit correlations [3]. The local-measurement criterion for vanishing quantum discord is standard [4]. The novelty assessed here is the complete selective-reset steady-state classification and its all-parameter discord directionality, **not** those prior mechanisms or general discord criteria.

## Limitations

The result is restricted to the specified transverse-field Ising Hamiltonian, selective first-qubit erasure, and strictly nonzero \(J,\Omega_1,\Omega_2\). Singular parameter limits can have qualitatively different fixed-point structure and are not covered by the strict-discord statement. The theorem concerns mathematical stationary states, not experimental reset fidelity, dynamical rates of approach, or bath-induced thermalization. The cited literature does not exclude equivalent statements in unindexed or inaccessible sources; mathematical originality still merits independent assessment.

## References

[1] M. Kulkarni and S. N. Majumdar, *Generating Entanglement by Quantum Resetting*, arXiv:2307.07485 (first public version 2023-07-14), https://arxiv.org/abs/2307.07485.

[2] M. Magoni, F. Carollo, G. Perfetto and I. Lesanovsky, *Emergent quantum correlations and collective behavior in non-interacting quantum systems subject to stochastic resetting*, arXiv:2202.12655, https://arxiv.org/abs/2202.12655.

[3] S. Wald, L. H. Yao, T. Platini, C. Hooley and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497, https://arxiv.org/abs/2410.11497.

[4] B. Dakić, V. Vedral and Č. Brukner, *Necessary and sufficient condition for non-zero quantum discord*, arXiv:1004.0190, https://arxiv.org/abs/1004.0190.
