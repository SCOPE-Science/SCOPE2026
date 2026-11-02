# Complete weighted-Ising criterion for exact protection of every collective spin singlet

## Finding

**Theorem (complete graph-and-field classification).** Let \(N=2n\ge2\) qubits have the Hamiltonian
\[
H=\sum_{1\le i<j\le N}J_{ij}Z_iZ_j+\sum_{i=1}^N h_iX_i,
\]
where the real, symmetric edge couplings \(J_{ij}=J_{ji}\) are otherwise arbitrary, and \(X_i,Z_i\) are Pauli operators. Define \(S_\pm=\sum_i(X_i\pm iY_i)/2\) and the total-spin singlet subspace \(\mathcal S=\ker S_+\cap\ker S_-\). Then the **entire** space \(\mathcal S\) is invariant under \(H\) if and only if
\[
h_1=\cdots=h_N,\qquad J_{ij}=a_i+a_j\quad(i\ne j)
\]
for some real vertex weights \(a_1,\ldots,a_N\). In that case
\[
H\big|_{\mathcal S}=-\sum_{i=1}^N a_i\,I_{\mathcal S},\qquad
\dim\mathcal S=\frac1{n+1}\binom{2n}{n}.
\]
The interaction condition is vacuous for \(N=2\): every single edge weight can be represented by vertex weights.

Consequently, for a Lindblad evolution whose only jumps are proportional to the collective \(S_-\) and \(S_+\) (with arbitrary nonnegative rates), every density operator supported on \(\mathcal S\) is an **exact stationary, decoherence-free state** precisely under this criterion. The equivalence is for Hamiltonian invariance of the entire collective singlet space, not merely a single protected vector. A collective \(S_z\) dephasing jump would also vanish there, but local bath jumps are not covered.

A nonhomogeneous *star* gives a sparse constructive example: \(J_{1j}=g\ne0\) for all \(j\ge2\), all other couplings zero, and uniform transverse field. Set \(a_1=g\), \(a_2=\cdots=a_N=0\). Every one of the \(C_n\) singlets is an eigenstate with energy \(-g\), for arbitrarily large even \(N\). Thus exact protection does not require the all-to-all uniform Ising graph.

**Exact dimer diagnostic.** For any perfect matching \(M=\{(i_p,j_p):1\le p\le n\}\) of the labels, let \(|s_M\rangle\) be the product of the normalized antisymmetric two-spin singlets on its pairs. Define the four-index alternating coupling difference
\[
Q_{pq}=J_{i_pi_q}-J_{i_pj_q}-J_{j_pi_q}+J_{j_pj_q},\quad p<q.
\]
For *arbitrary* real edge couplings and transverse fields,
\[
\boxed{\operatorname{Var}_{s_M}(H)=\sum_{p<q}Q_{pq}^{2}+\sum_{p=1}^n(h_{i_p}-h_{j_p})^2.}
\]
This is an **energy-variance** identity, not an equality with the norm of leakage outside the *whole* singlet space. The full collective singlet space is protected if and only if this nonnegative variance vanishes for **every** perfect matching. Individual pair singlets form convenient diagnostic probes; no assertion that they are an orthogonal family is needed.

## Assumptions and scope

There are exactly \(N=2n\) spin-\(1/2\) sites with \(n\ge1\); all pairwise Ising interactions and all on-site transverse fields are real and time independent. The bath is globally collective, with jumps \(S_-\) and \(S_+\). There are no individual lowering, raising, or dephasing operators and no other Hamiltonian terms. Invariance refers to all pure states in \(\mathcal S\), equivalently all supported density operators. The conclusion is independent of the nonnegative collective-jump rates because both jumps annihilate \(\mathcal S\).

For \(N=2\), \(J_{12}=a_1+a_2\) has nonunique representations, but \(-a_1-a_2=-J_{12}\) is representation independent. For \(N\ge4\), the additive representation is unique. The Catalan multiplicity and singlet identification are established prior facts, not claimed discoveries.

## Proof

1. **Paired singlet basis probes and magnetization.** For a fixed matching \(M\), choose an ordering of its pairs. In pair \(p\), the normalized state is \((|\uparrow_{i_p}\downarrow_{j_p}\rangle-|\downarrow_{i_p}\uparrow_{j_p}\rangle)/\sqrt2\). Their tensor product \(|s_M\rangle\) belongs to \(\mathcal S\). It is supported in the computational configurations with opposite spins on each matched pair, all of which have zero total \(Z\)-magnetization. The \(ZZ\) term preserves this magnetization, while every one-spin \(X_i\) flips it to \(+2\) or \(-2\). If \(H\mathcal S\subseteq\mathcal S\), the \(X\)-part separately annihilates \(|s_M\rangle\). Across matched pairs these one-flip outputs are mutually orthogonal; within pair \((i_p,j_p)\) their sum is \((h_{i_p}-h_{j_p})(|\downarrow\downarrow\rangle-|\uparrow\uparrow\rangle)/\sqrt2\). Hence \(h_{i_p}=h_{j_p}\) for all pairs of every matching. Any two indices can be paired in some matching, so all fields are equal.

2. **A one-dimensional intersection.** Write \(V_M\) for the coordinate span of the \(2^n\) computational states with spins opposite within every pair of \(M\). The \(ZZ\)-term acts diagonally and maps \(V_M\) to itself. Furthermore \(\mathcal S\cap V_M=\mathbb C|s_M\rangle\). To see this, impose \(S_+|\psi\rangle=0\) on a generic \(|\psi\rangle\in V_M\). For each pair, the amplitude at a configuration with that pair \(\uparrow\uparrow\) is the sum of the two coefficients of the corresponding opposite-spin configurations. Different pairs give distinct raised-spin support patterns, so these sums must separately vanish. Coefficients must change sign when any single pair is reversed. This determines all \(2^n\) coefficients up to one scalar, giving \(|s_M\rangle\). Thus invariance forces the diagonal Ising term to act as a scalar on each \(|s_M\rangle\).

3. **Exact Walsh expansion and variance.** Assign independent Rademacher variables \(\xi_p\in\{-1,+1\}\) to the two possible opposite-spin configurations in pair \(p\). The diagonal Ising energy on \(V_M\) is exactly
\[
E_M(\boldsymbol\xi)=-\sum_{p=1}^n J_{i_pj_p}+\sum_{p<q}Q_{pq}\xi_p\xi_q.
\]
The squared amplitudes of \(|s_M\rangle\) form the uniform measure on these \(2^n\) configurations. Distinct Walsh products \(\xi_p\xi_q\) are orthogonal, so \(\operatorname{Var}_{s_M}(H_{ZZ})=\sum_{p<q}Q_{pq}^2\). The one-spin transverse outputs are orthogonal to the entire zero-magnetization sector and have total squared norm \(\sum_p(h_{i_p}-h_{j_p})^2\). Their expectation vanishes, as do the mixed expectations with \(H_{ZZ}\). This proves the displayed full energy-variance identity. In particular, \(H_{ZZ}|s_M\rangle\) is proportional to \(|s_M\rangle\) if and only if all \(Q_{pq}=0\).

4. **From matchings to a complete graph condition.** Any four distinct labels can be placed into two pairs of a perfect matching, so invariance imposes
\[
J_{ik}-J_{il}-J_{jk}+J_{jl}=0\quad\text{for all pairwise distinct }i,j,k,l.
\]
For \(N\ge4\), fix labels \(1,2\). The identity with \((i,j)=(1,2)\) shows \(d:=J_{1k}-J_{2k}\) is constant over \(k\ge3\). Set \(a_1=(J_{12}+d)/2\), \(a_2=(J_{12}-d)/2\), and \(a_k=J_{1k}-a_1\) for \(k\ge3\). Then \(J_{1k}=a_1+a_k\) and \(J_{2k}=a_2+a_k\). The identity with pairs \((1,k),(2,l)\) gives \(J_{kl}=J_{1l}+J_{2k}-J_{12}=a_k+a_l\) for all distinct \(k,l\ge3\). The \(N=4\) case is included; for \(N=2\), choose any \(a_1+a_2=J_{12}\). This establishes necessity of additive edge weights.

5. **Sufficiency, eigenvalue, and open-system dynamics.** If \(J_{ij}=a_i+a_j\), then as operator identities,
\[
\sum_{i<j}(a_i+a_j)Z_iZ_j=\left(\sum_i a_iZ_i\right)\left(\sum_iZ_i\right)-\sum_i a_i.
\]
Every singlet is annihilated by \(\sum_iZ_i\) and \(\sum_iX_i=S_++S_-\). Consequently \(H|_{\mathcal S}=-(\sum_i a_i)I\), proving sufficiency and stationary unitary action. Both collective Lindblad jump operators annihilate the singlet space and their number operators do too, so their dissipators vanish on all densities supported there. Conversely, noninvariance of \(H\) prevents the entire singlet space from being Hamiltonian-protected. The Catalan dimension is the standard multiplicity of total spin zero: \(\binom{2n}{n}-\binom{2n}{n-1}=C_n\).

This completes the all-even-size classification. No finite enumeration enters the infinite-family proof.

## Verification

The accompanying \(\texttt{verify.py}\) implements an independent computational-basis matrix Hamiltonian and independently forms the total-spin-zero projector as the kernel of the raising operator on the zero-magnetization sector. It checks the Catalan dimensions, eigenblocks of heterogeneous additive and sparse-star families, exact dimer energy variances for arbitrary edge/field arrays, and leakage when interactions/fields violate the criterion for \(N=2,4,6,8\). It returned **PASS 435 finite independent checks** using NumPy. Run \(\texttt{python verify.py}\) with \(\texttt{numpy>=1.24}\). These are finite cross-checks, not the proof for all even \(N\).

## Relationship to prior work

Khoudiri *et al.* (first public 2026-08-10, arXiv:2608.09693), Sec. III A and Appendix A, identify the collective dark subspace with total-spin singlets and establish its Catalan dimension. Their Eq. (21) states the general projector invariance test; Fig. 1 and surrounding text report noninvariance for their particular homogeneous short-range Ising batteries for \(N\ge4\). The new statement **solves** that test explicitly over all real complete-graph edge parameters and site-dependent transverse fields, giving a necessary-and-sufficient graph family, sparse star examples, and an exact matching-wise energy-variance diagnostic. It does not claim discovery of the Lindblad dark-state condition or Catalan counting.

Kempe–Bacon–Lidar–Whaley (arXiv:quant-ph/0004064) establish general decoherence-free stabilizer and Hamiltonian-preservation frameworks and study exchange control. Jiang *et al.* (arXiv:0811.3049) study four-spin singlet encodings in optical superlattices and Ising couplings for gates. These provide relevant broader context but the inspected portions do not state the complete arbitrary-weight \(ZZ\)-graph classification. The graph identity and dimer variance remain directly reconstructible from the proof. No claim of a complete literature-wide uniqueness or independent priority audit is made.

## Limitations

The protection is exact only for perfectly collective jump operators and for the specified static pairwise \(ZZ\) and on-site \(X\) Hamiltonian. Noncollective dissipation, extra local longitudinal fields, uncontrolled exchange terms, odd system size, and finite errors in the additive parameter relation require separate analysis. A vanishing mean singlet leakage measure for a single vector is insufficient to certify preservation of the **whole** singlet sector. The variance formula is not itself a universal rate of Lindblad decoherence or a literal projector-leakage norm. While the interaction classification is proved, broader preexisting DFS representation-theoretic results may contain general principles from which it could be rederived; full independent novelty validation has not been performed.

## References

1. A. Khoudiri, A. Ullah, A. El Allati, and Ö. E. Müstecaplıoğlu, *Collective-dissipation-induced dark and metastable-like states for enhanced quantum battery performance*, arXiv:2608.09693 (first public 2026-08-10), https://arxiv.org/abs/2608.09693.
2. J. Kempe, D. Bacon, D. A. Lidar, and K. B. Whaley, *Theory of Decoherence-Free Fault-Tolerant Universal Quantum Computation*, arXiv:quant-ph/0004064 (2000), https://arxiv.org/abs/quant-ph/0004064.
3. L. Jiang, A. M. Rey, O. Romero-Isart, J. J. García-Ripoll, A. Sanpera, and M. D. Lukin, *Preparation of Decoherence Free Cluster States with Optical Superlattices*, arXiv:0811.3049 (2008), https://arxiv.org/abs/0811.3049.
4. H. Weisbrich, C. Saussol, W. Belzig, and G. Rastelli, *Decoherence in the quantum Ising model with transverse dissipative interaction in the strong coupling regime*, arXiv:1804.07559 (2018), https://arxiv.org/abs/1804.07559.
