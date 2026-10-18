# Dephasing-induced switching threshold for bright-state absorption on complete bipartite quantum networks

## Finding

Let \(m\ge2\), \(n\ge1\), and let \(K_{m,n}\) have a monitored part \(A\) of size \(m\) and an unmonitored part \(B\) of size \(n\). Its single-excitation adjacency Hamiltonian has hopping strength \(J>0\). Every site of \(A\) irreversibly loses excitation at rate \(\kappa>0\), and every site has homogeneous projector dephasing rate \(\gamma\ge0\). Start from any unit-trace density matrix \(\rho_0\) supported on \(B\). Define the bright overlap
\[
s=\sum_{b,b'\in B}(\rho_0)_{bb'}=n\langle b_+|\rho_0|b_+\rangle\in[0,n],\qquad |b_+\rangle=n^{-1/2}\sum_{b\in B}|b\rangle.
\]

**Exact mean-time law.** For every \(\gamma>0\), absorption occurs with probability one and the mean time is
\[
T_\gamma=\frac{m+n}{m\kappa}+\frac{n(m-1)}{m(\kappa+\gamma)}+\frac{n-s}{\gamma}+\frac{\kappa/2+\gamma}{2mJ^2}.
\tag{1}
\]
For \(s<n\), zero dephasing leaves a nonzero dark component, so the unconditional mean absorption time is infinite. The unique minimizer over positive dephasing rates is the unique positive solution of
\[
\frac1{2mJ^2}=\frac{n(m-1)}{m(\kappa+\gamma)^2}+\frac{n-s}{\gamma^2}.
\tag{2}
\]

**Coherent-launch switching threshold.** When \(s=n\), the initial state is necessarily \(|b_+\rangle\langle b_+|\). The zero-dephasing mean is finite and equals
\[
T_0=\frac2\kappa+\frac\kappa{4mnJ^2}.
\tag{3}
\]
A strictly positive dephasing rate gives a *strictly smaller* mean than \(T_0\) if and only if \(m>n\) and
\[
0<\frac\kappa{J\sqrt{2n(m-1)}}<x_c(m,n),\qquad
x_c(m,n)=\frac{2n-\sqrt{4n^2-2(n+1)(m-n)/(m-1)}}{n+1}.
\tag{4}
\]
In this parameter regime the **unique global** minimizing rate, allowing \(\gamma=0\), is
\[
\gamma_*=J\sqrt{2n(m-1)}-\kappa>0.
\tag{5}
\]
When \(m>n\ge2\) and equality holds in (4), the two distinct rates \(0\) and \(\gamma_*\) are tied global minimizers. In every other case not satisfying the strict or equality condition, zero dephasing is the unique global minimizer. In particular, for \(n=1\), \(x_c(m,1)=1\), and the equality case has \(\gamma_*=0\), not two distinct rates.

Thus even a fully coherent, initially bright excitation can benefit from environmental dephasing when the absorbing part is larger than the launching part and the loss rate lies below an exact, dimension-dependent boundary. Equal or smaller absorbing parts never exhibit that improvement for this bright preparation.

## Assumptions and scope

The Hilbert space is \(\mathbb C^{m+n}\), with canonical site basis. Write \(\Pi_A=\sum_{a\in A}|a\rangle\langle a|\) and
\[
H=J\sum_{a\in A,b\in B}\bigl(|a\rangle\langle b|+|b\rangle\langle a|\bigr).
\]
We use the unnormalized no-jump density matrix on the surviving sites, evolving through
\[
\dot\rho=-i[H,\rho]-\gamma\bigl(\rho-\operatorname{diag}\rho\bigr)-\frac\kappa2\{\Pi_A,\rho\}.
\tag{6}
\]
A monitored-site population therefore decays at rate \(\kappa\), and each offdiagonal coherence dephases at rate \(\gamma\). No other decay or onsite energies are present. The survival probability is \(S(t)=\operatorname{Tr}\rho(t)\), and \(T=\int_0^\infty S(t)\,dt\), interpreted as \(+\infty\) when survival has a nonzero limit. The result is for finite nonempty parts, uniform cross-part hopping and loss, and homogeneous site-projector dephasing. Rates are not optimized jointly: \(\kappa\) and \(J\) are held fixed while \(\gamma\) varies.

## Proof

**1. Strict decay for positive dephasing.** Regard (6) as a linear map \(\mathcal L\) on all complex site matrices, with Hilbert--Schmidt inner product. Its Hamiltonian commutator is skew-adjoint and
\[
\operatorname{Re}\langle X,\mathcal LX\rangle
=-\gamma\sum_{i\ne j}|X_{ij}|^2
-\frac\kappa2\sum_{i,j}\bigl({\bf1}_{i\in A}+{\bf1}_{j\in A}\bigr)|X_{ij}|^2.
\tag{7}
\]
Every eigenvalue therefore has nonpositive real part. Equality for an eigenmatrix when \(\gamma,\kappa>0\) requires \(X\) to be diagonal and supported entirely on \(B\). But the \(A\)-\(B\) block of \(-i[H,X]\) then has entries \(-iJX_{bb}\) for all \(a,b\), which vanish only when \(X=0\). Consequently every eigenvalue has strictly negative real part, and \(\rho(t)\to0\) exponentially (possibly with polynomial Jordan prefactors). In particular, all five scalar observables below are integrable and total absorption is certain.

**2. Exact five-variable closure.** Set
\[
P_A=\sum_{a\in A}\rho_{aa},\quad P_B=\sum_{b\in B}\rho_{bb},\quad
Q_A=\sum_{a\ne a'}\rho_{aa'},\quad Q_B=\sum_{b\ne b'}\rho_{bb'},\quad
Y=2J\operatorname{Im}\sum_{a\in A,b\in B}\rho_{ab}.
\]
The quantities \(Q_A\) and \(Q_B\) are real by Hermiticity. Directly summing the entries of (6) gives the closed *exact* linear system
\[
\begin{aligned}
\dot P_A&=-Y-\kappa P_A,&\dot P_B&=Y,\\
\dot Q_A&=-(m-1)Y-(\kappa+\gamma)Q_A,&
\dot Q_B&=(n-1)Y-\gamma Q_B,\\
\dot Y&=2J^2\bigl[n(P_A+Q_A)-m(P_B+Q_B)\bigr]-(\kappa/2+\gamma)Y.
\end{aligned}
\tag{8}
\]
Initially \(P_A=Q_A=Y=0\), \(P_B=1\), and \(Q_B=s-1\). Integrating (8) over \([0,\infty)\), using the vanishing terminal values, yields
\[
\int Y=-1,\quad \int P_A=\frac1\kappa,\quad
\int Q_A=\frac{m-1}{\kappa+\gamma},\quad
\int Q_B=\frac{s-n}{\gamma}.
\tag{9}
\]
The final equation of (8) gives
\[
\int P_B=\frac n m\left(\frac1\kappa+\frac{m-1}{\kappa+\gamma}\right)
+\frac{n-s}{\gamma}+\frac{\kappa/2+\gamma}{2mJ^2}.
\tag{10}
\]
Adding \(\int P_A\) proves (1) without any assumption on individual phases or purity of \(\rho_0\).

**3. General initial states and the zero-noise boundary.** Because \(m\ge2\), differentiation of (1) twice shows strict convexity in \(\gamma>0\):
\[
T''_\gamma=\frac{2n(m-1)}{m(\kappa+\gamma)^3}+\frac{2(n-s)}{\gamma^3}>0.
\]
For \(s<n\), the derivative tends to \(-\infty\) at zero and to \(1/(2mJ^2)>0\) at infinity, proving (2) and uniqueness. At exactly zero dephasing, the subspace of \(B\)-states orthogonal to \(|b_+\rangle\) is annihilated by both \(H\) and \(\Pi_A\); its initial weight \(1-s/n>0\) never decays. This establishes the infinite mean at \(\gamma=0\).

**4. Bright input and global switching.** For \(s=n\), positivity and unit trace force \(\rho_0=|b_+\rangle\langle b_+|\). With \(\gamma=0\), only the normalized uniform states \(|a_+\rangle\), \(|b_+\rangle\) participate. Their Hamiltonian coupling is \(J\sqrt{mn}\), and only \(|a_+\rangle\) has loss \(\kappa\). Integrating the resulting two-state population and coherence equations gives (3).

For positive dephasing and \(s=n\), (1) has derivative
\[
T'_\gamma=\frac1{2mJ^2}-\frac{n(m-1)}{m(\kappa+\gamma)^2}.
\tag{11}
\]
Its unique positive stationary minimum exists precisely when \(\kappa<J\sqrt{2n(m-1)}\), and is (5). Otherwise \(T_\gamma\) is increasing for \(\gamma>0\). In the regime with a positive stationary minimum, write \(x=\kappa/(J\sqrt{2n(m-1)})\in(0,1)\). Substitution of (3) and (5) into (1) gives the *exact global comparison*
\[
m\kappa\bigl(T_{\gamma_*}-T_0\bigr)
=n-m+2n(m-1)x-\frac{(m-1)(n+1)}2x^2=:F_{m,n}(x).
\tag{12}
\]
On \((0,1)\), \(F'_{m,n}(x)=(m-1)[2n-(n+1)x]>0\), while
\[
F_{m,n}(0)=n-m,\qquad F_{m,n}(1)=\frac{(n-1)(3m-1)}2.
\]
Hence \(F<0\) occurs precisely when \(m>n\) and \(x<x_c(m,n)\), with the smaller quadratic root (4); for \(n=1\) that root is \(1\). At equality with \(n\ge2\), \(x_c<1\), so the positive optimizer and zero noise tie. At every other parameter value zero dephasing wins uniquely, including the cases with no positive stationary minimum. This proves the full switching statement.

## Verification

The standalone program `verification.py` constructs the *full* Lindblad superoperator (6), solves for the integrated matrix \(-\mathcal L^{-1}\rho_0\), and compares its trace against (1) for complex random positive-semidefinite initial states. It also checks the separate two-level zero-dephasing reduction and the strict/tied global phase comparisons. In one reproducible run with NumPy it completed 124 finite tests, with maximum absolute mean-time discrepancy \(2.49\times10^{-14}\). These are finite consistency checks; the proofs of strict decay, formulas (1)--(5), and the global boundary are analytic above and do not depend on enumeration.

## Relationship to prior work

Razzoli, Paris, and Bordone analyze quantum transport on complete bipartite graphs, but their Section 4.1 uses **one** absorbing vertex, a graph-Laplacian Hamiltonian, and no decoherence. Their reported quantities are coherent absorption efficiencies for selected launches; they do not imply a site-projector-dephased, entire-part absorbing mean-time law or the optimization boundary (4). Alterman, Berman, and Strauch study coherence-sensitive environment-assisted quantum transport on a **fully connected** graph with one trapping site, plus sitewise dephasing; their reduced equations and optimality conditions have a different coupling and loss pattern. Both sources motivate distinguishing coherence effects from noise-assisted transport, but neither inspected model yields the present bipartition-size switching condition as a substitution. The one-absorber star geometry is a degenerate boundary family, not a case of the theorem's \(m\ge2\) collective-loss effect. Broader unpublished or differently formulated equivalent reductions remain possible; no claim of literature-wide uniqueness is made.

## Limitations

The exact result assumes the adjacency rather than degree-Laplacian Hamiltonian; uniform hopping, identical loss on *every* \(A\)-site, uniform site dephasing, and no competing radiative loss. Unequal sink rates, onsite disorder, finite-time success probabilities, and multi-excitation dynamics are not proved. The optimum concerns the **unconditional mean time of eventual absorption**, not a spectral-gap or fixed-time metric. For \(\gamma=0\) the infinite mean for nonbright input comes from a genuine nondecaying component, not numerical slow convergence. Independent verification of originality and correctness has not been performed.

## References

1. L. Razzoli, M. G. A. Paris, and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794v1 (first posted 2020-11-27), especially Section 4.1, Appendix B.1, and Conclusions. https://arxiv.org/abs/2011.13794
2. S. Alterman, J. Berman, and F. W. Strauch, *Optimal Conditions for Environment-Assisted Quantum Transport on the Fully Connected Network*, arXiv:2309.00164v1 (first posted 2023-08-31), especially Sections II--V and Appendix A. https://arxiv.org/abs/2309.00164
