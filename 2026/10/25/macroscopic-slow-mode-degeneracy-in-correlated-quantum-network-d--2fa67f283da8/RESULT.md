# Macroscopic slow-mode degeneracy in correlated quantum-network dissipation

## Finding
For every even number of sites \(N=2m\geq6\), the balanced two-community latent-variable exchange network described below has a slowest nonstationary Liouvillian eigenvalue
\[
-\gamma=-J^2\Delta t\,\xi(1-\xi)(N-2)(1-\kappa^2)
\]
with **exact geometric and algebraic multiplicity** \(\binom{N-2}{2}\), whenever \(0<\kappa<1\). Every eigenvalue other than zero has real part at most \(-\gamma\), and there are no additional eigenvalues on that real-part boundary. At the exceptional size \(N=4\), the multiplicity is \(3\), rather than \(\binom{2}{2}=1\). At zero correlation, \(\kappa=0\), the multiplicity is \(\binom{N-1}{2}\) for every even \(N\geq4\). In particular, the introduction of any nonzero community correlation removes exactly \(N-2\) independent slow modes for \(N\geq6\), while leaving the three slow modes intact for \(N=4\).

## Assumptions and scope
Consider the single-excitation Hilbert space \(\mathbb C^N\), with \(N=2m\geq4\). Partition the sites into equal communities; write \(\mathbf u=(1,\ldots,1)^T\) and \(\mathbf s=(1,\ldots,1,-1,\ldots,-1)^T\), with \(m\) entries of each sign. Put \(S=\mathbf u\mathbf u^T-I_N\), \(Q=\mathbf s\mathbf s^T-I_N\), and \(V_{ij}=|i\rangle\langle j|+|j\rangle\langle i|\) for each \(i<j\). For any Hermitian \(A\), set \(\mathcal D[A](X)=AXA-\tfrac12(A^2X+XA^2)\). Fix nonzero real \(J\), positive \(\Delta t\), edge marginal \(\xi=1/2\), and \(0\leq\kappa<1\). Define
\[
\mathcal L_\kappa(X)=-i[J\xi S,X]+a\sum_{i<j}\mathcal D[V_{ij}](X)+b\mathcal D[Q](X),
\]
where \(a=J^2\Delta t\,\xi(1-\xi)(1-\kappa^2)>0\) and \(b=J^2\Delta t\,\xi(1-\xi)\kappa^2\). This is the **leading-order effective continuous-time generator** induced by the source's positive-semidefinite latent-variable covariance \(\xi(1-\xi)[(1-\kappa^2)I+\kappa^2\mathbf q\mathbf q^T]\), with edge sign \(q_{ij}=s_is_j\). The exact finite-switching-time random-unitary channel is not asserted to have the same multiplicities.

For \(0<\kappa<1\) the full slow eigenspace, over \(\mathbb C\), is precisely
\[
\mathscr E_\kappa=\{X:X^T=X,\ X_{ii}=0,\ X\mathbf u\in\mathbb C\mathbf u,\ X\mathbf s\in\mathbb C\mathbf s\}.
\]
For \(\kappa=0\) delete the condition involving \(\mathbf s\). Matrices in these spaces are automatically traceless. Their Hermitian real-symmetric members are independent physical slow observables; sufficiently small perturbations of \(I_N/N\) along any such member are valid quantum states.

## Proof
**1. The independent-edge dissipation has an exactly located bottom eigenspace.** Set \(\mathfrak D=\sum_{i<j}\mathcal D[V_{ij}]\). In Hilbert–Schmidt geometry the matrix space splits orthogonally into scalar multiples of \(I_N\), traceless diagonal matrices, skew-symmetric zero-diagonal matrices, and symmetric zero-diagonal matrices, also for complex coefficients. Direct multiplication uses \(\sum V_{ij}^2=(N-1)I_N\). On these four spaces, respectively, \(\mathfrak D\) acts by the real scalars \(0,-N,-N,-(N-2)\). Hence on every traceless \(X\),
\[
\operatorname{Re}\langle X,\mathcal L_\kappa X\rangle_{HS}\le -a(N-2)\|X\|_{HS}^2.
\]
Indeed the Hamiltonian commutator is skew-adjoint, while \(\langle X,\mathcal D[Q]X\rangle=-\frac12\|[Q,X]\|_{HS}^2\le0\). Any nonzero eigenoperator is traceless because the generator is trace preserving, so every nonzero eigenvalue has real part no larger than \(-a(N-2)\). This establishes an upper bound on the spectral abscissa in the traceless sector, not by itself an existence statement.

**2. Equality characterizes all boundary eigenoperators.** If \(0<\kappa<1\), then \(a,b>0\). Equality forces \(X^T=X\), \(X_{ii}=0\), and \([Q,X]=0\). Since \(Q=\mathbf s\mathbf s^T-I_N\), the final relation is equivalent, for symmetric \(X\), to \(X\mathbf s\in\mathbb C\mathbf s\). On this equality subspace the eigenvalue equation reduces to \(-i[J\xi S,X]=i\omega X\), for real \(\omega\). Its left-hand side is skew-symmetric under ordinary transposition, while its right-hand side is symmetric. Both therefore vanish, so \(\omega=0\) and \([S,X]=0\). Because \(S=\mathbf u\mathbf u^T-I_N\), this is equivalent to \(X\mathbf u\in\mathbb C\mathbf u\). Conversely, each matrix satisfying these conditions is annihilated by the \(Q\) dissipator and the Hamiltonian commutator and satisfies \(\mathfrak D X=-(N-2)X\), so it is an eigenoperator with eigenvalue \(-a(N-2)\). This proves exactness of the whole boundary eigenspace and the spectral gap. With \(\kappa=0\) the \(Q\) condition is absent; the same argument gives the stated larger space. The uniform Hilbert–Schmidt estimate \(\|e^{t\mathcal L_\kappa}X\|_{HS}\le e^{-a(N-2)t}\|X\|_{HS}\) on traceless matrices excludes Jordan blocks at the boundary: a nontrivial Jordan chain would produce polynomially enhanced norm there. Thus algebraic and geometric multiplicities coincide.

**3. Exact dimension count and four-site exception.** Write a symmetric zero-diagonal matrix in community blocks \(X=\begin{psmallmatrix}A&C\\C^T&B\end{psmallmatrix}\). The two constant-vector requirements mean that \(A\) and \(B\) have constant row sums equal to each other, and \(C\) has equal constant row and column sums. If \(m\ge3\), the space of symmetric zero-diagonal \(m\times m\) matrices with constant row sums has dimension \((m-1)(m-2)/2\): the unsigned incidence matrix of the complete graph has rank \(m\), since any vector orthogonal to all columns obeys \(z_i+z_j=0\) for all pairs and therefore vanishes. Requiring the two within-community row-sum values to coincide removes one dimension. The cross-block matrices \(C\) with constant row and column sums form a space of dimension \((m-1)^2+1\). Adding gives \((m-1)(2m-3)=\binom{N-2}{2}\). For \(m=2\), each symmetric zero-diagonal \(2\times2\) matrix already has uniform row sums; equality between the two block sums leaves one freedom, while \(C\) has two freedoms, totaling three. At \(\kappa=0\), the single condition of constant total row sums has \(N-1\) independent constraints on the \(\binom N2\) offdiagonal variables, because the unsigned complete-graph incidence matrix has full rank for \(N\ge3\). Therefore \(\dim\mathscr E_0=\binom N2-(N-1)=\binom{N-1}{2}\).

## Verification
The accompanying `artifacts/verify.py` independently constructs the \(N^2\times N^2\) Lindblad matrix from matrix units and compares its eigenvalues to the claimed gap and multiplicity at \(N=4,6,8\) and \(\kappa=0,1/2,9/10\). It also tests the constructed eigenoperators and the eigenspace's linear constraints. These finite-dimensional tests corroborate, but do not replace, the all-even-\(N\) algebraic proof. Reproduce with `python -m pip install -r artifacts/requirements.txt` followed by `python artifacts/verify.py`.

## Relationship to prior work
Nourmandipour and Mancini [1], especially Sec. V, Appendix C.1, and Eqs. (31)–(32), (A71), (A83)–(A95), construct this latent-variable ensemble and one explicit slow eigenoperator. They give its decay rate, while expressly distinguishing it from an analytical proof that no slower mode exists. They also analyze the **different** fully correlated endpoint \(\kappa=1\), including the stationary-kernel dimension. The new point here is the full finite-correlation **slow-band multiplicity**, its complete operator characterization, and the singular four-site exception. The independent-edge dissipative spectrum is elementary and established in related edge-noise literature; by itself it does not determine which of its degenerate modes survive the additional correlated jump and coherent Hamiltonian. Farooq and Mancini [2] address random graph evolution and correlations but not this eigenspace classification. More general open-system invariant-algebra results may offer alternative derivations; no literature-wide priority claim is made.

## Limitations
This statement is exact for the specified finite-dimensional **leading-order effective generator**, not for finite-time switching channels, unequal communities, incomplete edge sets, or the rank-one endpoint \(\kappa=1\). The correlation parameter approaches one only from below; setting \(\kappa=1\) changes the dissipative kernel discontinuously. Nothing is claimed about nonlinear dynamics outside the single-excitation sector. Although numerical spectrum checks cover three network sizes, only the direct linear-algebra proof supports the unrestricted even-size theorem. Independent expert review and exhaustive priority verification have not been performed.

## References
[1] A. Nourmandipour and S. Mancini, *Emergent Dissipation from Fluctuating Quantum-Network Topology*, arXiv:2610.03194v1 (first publicly submitted 2026-10-02), https://arxiv.org/abs/2610.03194.

[2] U. Farooq and S. Mancini, *Information Dissipation in Random Quantum Networks* (2014), arXiv:1404.0508, https://arxiv.org/abs/1404.0508. (Historical context only.)
