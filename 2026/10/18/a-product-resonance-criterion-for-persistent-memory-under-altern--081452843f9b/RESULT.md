# A product-resonance criterion for persistent memory under alternating site dephasing

## Finding

A weighted periodic bipartite quantum walk can retain its initial-state memory under strictly positive site dephasing on *every vertex of one sublattice*. The obstruction is an exact cyclic product resonance. Fix an integer \(n\ge3\), positive real hoppings \(a_j,b_j>0\) for \(j\in\mathbb Z/n\mathbb Z\), and any dephasing rate \(\gamma>0\). With Hamiltonian and dephasing as defined below, put \(A=\prod_{j=0}^{n-1}a_j\) and \(B_*=\prod_{j=0}^{n-1}b_j\). Then the dynamics converges for **every** initial density matrix, and its limiting state is maximally mixed unless \(n\) is even and \(A=B_*\).

On that resonant locus, let \(d\) be the normalized vector supported on the unmonitored sites with amplitudes satisfying \(a_jd_j+b_jd_{j-1}=0\), and put \(D=|d\rangle\langle d|\). If \(p=\langle d|\rho(0)|d\rangle\), then
\[
\lim_{t\to\infty}\rho(t)=pD+\frac{1-p}{2n-1}(I_{2n}-D).
\]
Away from resonance, \(\lim_{t\to\infty}\rho(t)=I_{2n}/(2n)\). Thus the fixed-point algebra changes dimension exactly from one to two on the product-resonant even cycles. Both conclusions hold for every \(\gamma>0\); no convergence-rate uniformity as \(\gamma\downarrow0\) is asserted.

Furthermore, there are strictly positive resonant hoppings with a localized dark state. For \(n=2m\ge4\) and any fixed \(0<q<1\), choose \(a_j=1\), \(b_0=q^{-1}\), \(b_j=q\) for \(1\le j\le m\), and \(b_j=q^{-1}\) for \(m+1\le j<2m\). Starting at the unmonitored site \(O_0\), the limiting return probability tends, along even \(n\to\infty\), to
\[
\left(\frac{1-q^2}{1+q^2}\right)^2>0.
\]
If even one hopping is detuned so that the product equality fails, the long-time return probability at every finite \(n\) becomes exactly \(1/(2n)\), hence vanishes with increasing \(n\). The order of limits is time first, then size; generic detuning destroys the resonance.

## Assumptions and scope

The single-particle Hilbert space is \(\mathbb C^{2n}\), with orthonormal basis \(|E_j\rangle,|O_j\rangle\), indexed modulo \(n\). The Hamiltonian has two real positive bonds incident to each monitored vertex:
\[
H=\sum_{j=0}^{n-1}\big[a_j(|E_j\rangle\langle O_j|+|O_j\rangle\langle E_j|)+b_j(|E_j\rangle\langle O_{j-1}|+|O_{j-1}\rangle\langle E_j|)\big].
\]
Only the \(E\)-sublattice is dephased. Let \(P_j=|E_j\rangle\langle E_j|\), and for any operator \(X\) define
\[
\mathcal L(X)=-i[H,X]+\gamma\sum_{j=0}^{n-1}\left(P_jXP_j-\tfrac12(P_jX+XP_j)\right).
\]
There is no decay, no absorption, no reset, no onsite energy, and no dephasing on \(O\). The initial state is an arbitrary positive semidefinite trace-one operator. The result is finite-size exact for all \(n\ge3\), with a separately identified even-size localization limit.

## Proof

**1. Dissipation and the peripheral spectrum.** For the Hilbert–Schmidt inner product, direct expansion of each orthogonal projector gives the exact identity, for every complex operator \(X\),
\[
\operatorname{Re}\operatorname{Tr}(X^\dagger\mathcal L X)=-\frac\gamma2\sum_j\|[P_j,X]\|_{\mathrm{HS}}^2.
\]
Hence every stationary eigenoperator and every purely imaginary eigenoperator of \(\mathcal L\) commutes with each \(P_j\). For such an operator, the dissipator vanishes. Writing the basis with \(E\) first, \(O\) second, every commuting operator has the block form \(X=\operatorname{diag}(C,Y)\), where \(C\) is diagonal and \(Y\) is unrestricted. Since \(H\) is off-diagonal, \([H,X]\) has only off-diagonal blocks. Thus \(\mathcal L X=i\omega X\) with real \(\omega\ne0\) implies \(X=0\). There are no nonzero-frequency peripheral modes. The Hilbert–Schmidt norm of \(e^{t\mathcal L}X\) is nonincreasing by the same identity, so eigenvalues on the imaginary axis cannot carry nontrivial Jordan blocks. As the space is finite dimensional, the semigroup converges to the projection onto its zero eigenspace.

**2. Exact zero-eigenspace classification.** Put
\[
H=\begin{pmatrix}0&T\\T^\mathsf{T}&0\end{pmatrix},\qquad T_{j,j}=a_j,\qquad T_{j,j-1}=b_j,
\]
with all other entries zero. Commutation of \(X=\operatorname{diag}(C,Y)\) with \(H\) is equivalent to \(TY=CT\) and \(YT^\mathsf{T}=T^\mathsf{T}C\). Multiplying yields \([C,TT^\mathsf{T}]=0\). For every adjacent pair \(j,j+1\) the corresponding off-diagonal element of \(TT^\mathsf{T}\) is \(a_jb_{j+1}>0\). These entries form a connected cycle; because \(C\) is diagonal, the commutator vanishes only when \(C=cI_n\). Consequently, setting \(W=Y-cI_n\), one has \(TW=0\) and \(WT^\mathsf{T}=0\).

Expansion of the cyclic bidiagonal determinant gives
\[
\det T=\prod_ja_j-(-1)^n\prod_jb_j.
\]
Since all hoppings are strictly positive, \(T\) is nonsingular for odd \(n\); for even \(n\), singularity is equivalent to \(A=B_*\). If \(T\) is nonsingular, then \(W=0\), so the complete fixed-point algebra is \(\operatorname{span}\{I_{2n}\}\). If \(T\) is singular, each row of \(T d=0\) imposes \(d_j=-(b_j/a_j)d_{j-1}\). No coefficient vanishes and the recurrence determines all amplitudes from one, giving \(\dim\ker T=1\). The two matrix equations for \(W\) imply its image lies in \(\ker T\) and its coimage lies in the same kernel. Hence \(W=t|d\rangle\langle d|\) for a scalar \(t\). The complete fixed-point algebra is \(\operatorname{span}\{I_{2n},D\}\).

**3. Exact long-time state.** The semigroup preserves trace. In the singular case \(HD=DH=P_jD=DP_j=0\), so \(\mathcal L^\dagger(D)=0\) and \(\operatorname{Tr}(D\rho(t))=\operatorname{Tr}(D\rho(0))=p\). Every limiting density matrix is therefore in \(\operatorname{span}\{I,D\}\) with trace one and dark-state weight \(p\); solving these two linear equations gives \(pD+(1-p)(I-D)/(2n-1)\). In the nonsingular case trace alone fixes \(I/(2n)\). This uses no unproved ergodicity assumption.

**4. Localization and discontinuity.** For even \(n=2m\), the specified product-balanced bonds give an unnormalized kernel vector \(d_j=(-1)^jq^{\min(j,2m-j)}\). Its squared norm is \(Z_n=1+2\sum_{k=1}^{m-1}q^{2k}+q^{2m}\). Hence the initial state at \(O_0\) has dark weight \(p_n=1/Z_n\), and its final return probability at \(O_0\) is
\[
R_n=p_n^2+\frac{(1-p_n)^2}{2n-1}.
\]
As \(m\to\infty\), \(Z_n\to(1+q^2)/(1-q^2)\). Thus \(R_n\to((1-q^2)/(1+q^2))^2\). Changing any one hopping without compensating another makes \(\det T\ne0\); Part 3 then gives \(R_n=1/(2n)\).

## Verification

Run \(\texttt{python3 artifacts/check.py}\) with NumPy, SciPy and SymPy. The checker constructs the physical Hamiltonian and Lindblad superoperator directly from the bond data, independently tests the cyclic determinant symbolically for two small sizes and numerically at further sizes, counts numerical zero modes and nonzero-frequency peripheral modes, verifies the dark projector is stationary both in Schrödinger and Heisenberg pictures, checks one directly exponentiated finite-time evolution against the predicted limit, and checks the localized recurrence and normalizations. Explicit samples include odd cycles, generic even cycles, and product-balanced even cycles. This is finite-dimensional diagnostic evidence supporting—but not replacing—the analytical proof valid for every size and positive hopping choice.

## Relationship to prior work

Mohseni et al. [1] and Rebentrost et al. [2] develop coherent-plus-dephasing quantum transport in the Lindblad framework, but not the selective one-sublattice weighted-ring classification. Liu and Balu [3] analyze different graph jump operators of directed-edge transition type, and their regular-graph uniform steady-state conclusion cannot be applied to this projector-dephased model. Medvedyeva, Essler and Prosen [4] treat a uniformly dephased fermionic tight-binding lattice and its many-body Bethe-ansatz spectrum; their sum of jump operators runs over every site, unlike the present half-monitored one-particle sector. Bressanini, Benedetti and Paris [5] likewise use all-site dephasing in their cycle classicalization analysis. All these comparisons concern actual operator assumptions and claimed conclusions, rather than just thematic similarities.

The existence of decoherence-free vectors and the elementary determinant identity individually belong to established algebraic ideas. The specific conjunction claimed here is the **necessary-and-sufficient resonance criterion, complete long-time map for every initial state, and positive thermodynamic return with exact detuning collapse** in an entirely connected and half-dephased family. A complete proof of uniqueness relative to all unindexed literature is not claimed.

## Limitations

The hoppings must be positive real, onsite potentials vanish, and exactly one bipartite sublattice is monitored. Complex Peierls phases or onsite potentials can alter the resonance condition. The equilibrium state is obtained after taking \(t\to\infty\) separately for each finite size; neither uniform spectral-gap estimates nor persistence under small detuning is established. The localized thermodynamic statement is about the diagonal return probability, not ballistic transport or quantum information fidelity at finite times. The cited all-site-dephasing results should not be inferred to cover this different dissipator. No independent external verification has been performed.

## References

[1] M. Mohseni, P. Rebentrost, S. Lloyd, A. Aspuru-Guzik, *Environment-Assisted Quantum Walks in Photosynthetic Energy Transfer*, arXiv:0805.2741v1 (first posted 2008-05-18), https://arxiv.org/abs/0805.2741 .

[2] P. Rebentrost et al., *Environment-Assisted Quantum Transport*, arXiv:0807.0929v1 (2008), https://arxiv.org/abs/0807.0929 .

[3] C. Liu and R. Balu, *Steady states of continuous-time open quantum walks*, arXiv:1604.05652v1 (2016), https://arxiv.org/abs/1604.05652 .

[4] M. V. Medvedyeva, F. H. L. Essler, T. Prosen, *Exact Bethe ansatz spectrum of a tight-binding chain with dephasing noise*, arXiv:1606.09122v1 (2016), https://arxiv.org/abs/1606.09122 .

[5] G. Bressanini, C. Benedetti and M. G. A. Paris, *Decoherence and classicalization of continuous-time quantum walks on graphs* (2022), https://link.springer.com/article/10.1007/s11128-022-03647-x .
