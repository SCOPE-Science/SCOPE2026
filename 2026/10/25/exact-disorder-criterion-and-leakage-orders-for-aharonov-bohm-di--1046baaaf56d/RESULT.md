# Exact disorder criterion and leakage orders for Aharonov–Bohm diamond cages

## Finding

Consider a two-sided diamond chain with one hub \(A_j\) and two arm sites \(U_j,V_j\) in each bond cell. Every hub is connected to both arms of its neighboring cells, with arbitrary bounded nonzero complex hopping amplitudes and arbitrary bounded real site energies. **Complete one-cage confinement from every hub is equivalent to two local identities on every diamond:** the two arm energies coincide and the two coherent two-step paths between consecutive hubs cancel exactly.

For bond cell \(j\), write the hopping vectors from its left and right hubs as \(\ell_j,r_j\in\mathbb C^2\), and arm energies as \(\epsilon_{U,j},\epsilon_{V,j}\). The necessary and sufficient identities are
\[
\epsilon_{U,j}=\epsilon_{V,j},\qquad r_j^\dagger\ell_j=0\quad\text{for every }j\in\mathbb Z.
\]
Under these identities the full Hamiltonian is unitarily equivalent to an **orthogonal direct sum of independent three-site Jacobi matrices**. Therefore it has a complete orthonormal basis of compactly supported eigenvectors even if all other permitted parameters vary arbitrarily from cell to cell. The two-path condition amounts to equal magnitudes and a relative phase of \(\pi\) for the two gauge-invariant path contributions.

The first nonzero short-time probability for escape from hub \(A_j\) directly to hub \(A_{j+1}\) distinguishes two mechanisms. A failure of path cancellation gives an order-\(t^4\) probability. Exact path cancellation with unequal arm energies gives an order-\(t^6\) probability. When both equalities hold, that probability vanishes for all times.

## Assumptions and scope

Let \(\mathcal H=\ell^2(\mathbb Z;\mathbb C^3)\) have orthonormal basis vectors \(|A_j\rangle,|U_j\rangle,|V_j\rangle\) for \(j\in\mathbb Z\). The arm pair in cell \(j\) is denoted \(w_j=(U_j,V_j)\). Real sequences \(v_j,\epsilon_{U,j},\epsilon_{V,j}\) and complex vectors \(\ell_j=(\ell_{U,j},\ell_{V,j})^T\), \(r_j=(r_{U,j},r_{V,j})^T\) are uniformly bounded. All four components of \(\ell_j,r_j\) are required to be nonzero at every cell. We do not demand uniform positive lower bounds, translation symmetry, an infinite-volume gap, or a probability distribution for disorder.

The bounded self-adjoint tight-binding Hamiltonian \(H\) is fixed by
\[
\begin{aligned}
(H\psi)_{A_j}&=v_j\psi_{A_j}+\ell_j^\dagger\psi_{w_j}+r_{j-1}^\dagger\psi_{w_{j-1}},\\
(H\psi)_{w_j}&=E_j\psi_{w_j}+\ell_j\psi_{A_j}+r_j\psi_{A_{j+1}},\\
E_j&=\operatorname{diag}(\epsilon_{U,j},\epsilon_{V,j}).
\end{aligned}
\]
No direct hub-to-hub or arm-to-arm hopping is allowed. Define **one-cage confinement from every hub** to mean that for every \(j\in\mathbb Z\) and every \(t\in\mathbb R\), the vector \(e^{-itH}|A_j\rangle\) belongs to the five-site span of \(A_j,U_{j-1},V_{j-1},U_j,V_j\).

Define the two-step path sum and energy-weighted sum
\[
S_j=\overline{r_{U,j}}\ell_{U,j}+\overline{r_{V,j}}\ell_{V,j},\qquad
T_j=\epsilon_{U,j}\overline{r_{U,j}}\ell_{U,j}+\epsilon_{V,j}\overline{r_{V,j}}\ell_{V,j}.
\]
The conclusions apply to every sequence obeying these assumptions, including arbitrarily strong but bounded spatial variation.

## Proof

**1. Necessary conditions from two time derivatives.** If one-cage confinement holds from hub \(A_j\), then \(\langle A_{j+1},e^{-itH}A_j\rangle=0\) for every \(t\). Since \(H\) is bounded, its exponential is an entire operator-valued function, and all matrix-power coefficients vanish. Directly summing the only two length-two paths gives
\[
\langle A_{j+1},H^2A_j\rangle=S_j.
\]
Every length-three walk from \(A_j\) to \(A_{j+1}\) inserts precisely one diagonal waiting step at the initial hub, terminal hub, or one arm. Hence
\[
\langle A_{j+1},H^3A_j\rangle=(v_j+v_{j+1})S_j+T_j.
\]
Confinement implies \(S_j=T_j=0\). Put \(u_j=\overline{r_{U,j}}\ell_{U,j}\). The nonzero-coupling hypothesis yields \(u_j\ne0\); when \(S_j=0\), the other path contribution is \(-u_j\), so
\[
T_j=u_j(\epsilon_{U,j}-\epsilon_{V,j}).
\]
Thus both arm energies are equal. Repeating for every \(j\) proves necessity. Notice that necessity relies on confinement for **all times**, not only on one or finitely many observed times.

**2. Sufficiency and exact block structure.** Suppose both identities hold for every cell, writing \(\epsilon_j=\epsilon_{U,j}=\epsilon_{V,j}\). The orthogonal vectors \(\ell_j/\|\ell_j\|\) and \(r_j/\|r_j\|\) form an orthonormal basis of the cell's arm space \(\mathbb C^2\). Because \(E_j=\epsilon_j I_2\), it does not mix these basis directions. Form the mutually orthogonal invariant spaces
\[
\mathcal K_j=\operatorname{span}\left\{\frac{r_{j-1}}{\|r_{j-1}\|}\text{ at }w_{j-1},\;|A_j\rangle,\;\frac{\ell_j}{\|\ell_j\|}\text{ at }w_j\right\}.
\]
The spaces partition the original hub-and-arm basis, and the action of \(H\) on \(\mathcal K_j\), in the displayed order, is exactly
\[
J_j=\begin{pmatrix}
\epsilon_{j-1}&\|r_{j-1}\|&0\\
\|r_{j-1}\|&v_j&\|\ell_j\|\\
0&\|\ell_j\|&\epsilon_j
\end{pmatrix}.
\]
Therefore \(H\simeq\bigoplus_{j\in\mathbb Z}J_j\), and every hub evolves entirely inside its single space \(\mathcal K_j\). Every \(J_j\) is an irreducible real symmetric three-diagonal matrix, since its off-diagonal entries are positive, so it has three simple real eigenvalues. Choosing orthonormal eigenvectors in every block gives a complete orthonormal basis of eigenvectors of \(H\) with support on at most five original sites. It follows that \(H\) has pure-point **spectral type**. Its topological spectrum is the closure of the union of all block eigenvalues; accumulation points in this closure need not themselves be eigenvalues.

**3. Gauge-invariant balance.** Each path contribution \(\overline{r_{U,j}}\ell_{U,j}\) or \(\overline{r_{V,j}}\ell_{V,j}\) is multiplied by the same factor under independent site phase changes. Their relative phase and ratio of magnitudes are therefore gauge invariant. Since both contributions are nonzero, their sum vanishes if and only if their magnitudes match and their relative phase is \(\pi\) modulo \(2\pi\). This formulation permits unequal individual arm-hopping magnitudes, provided the products match.

**4. Sharp initial leakage laws.** The direct transition amplitude \(F_j(t)=\langle A_{j+1},e^{-itH}A_j\rangle\) has vanishing zeroth- and first-order coefficients. The bounded-operator Taylor expansion and Step 1 give
\[
F_j(t)=-\frac{S_j}{2}t^2+\frac{i}{6}\bigl[(v_j+v_{j+1})S_j+T_j\bigr]t^3+O(t^4).
\]
If \(S_j\ne0\), squaring its modulus yields
\[
|F_j(t)|^2=\frac{|S_j|^2}{4}t^4+O(t^5).
\]
If \(S_j=0\) but \(\epsilon_{U,j}\ne\epsilon_{V,j}\), then \(T_j=u_j(\epsilon_{U,j}-\epsilon_{V,j})\ne0\), and
\[
|F_j(t)|^2=\frac{|u_j|^2|\epsilon_{U,j}-\epsilon_{V,j}|^2}{36}t^6+O(t^7).
\]
If both conditions are satisfied, the invariant-block decomposition shows \(F_j(t)\equiv0\). Conversely, the first two nonzero Taylor coefficients exclude persistent zero amplitude when either condition fails. The proof is global in the cell index and in the strength of the bounded parameters.

## Verification

The standalone reproducibility program `verify.py` checks the matrix-power formulas symbolically and performs independently constructed finite-periodic-chain comparisons. With seeded complex couplings and nonuniform hub/arm energies it tests 650 exact unitary block decompositions, 650 spectrum comparisons, 650 dynamic confinement tests, 650 deliberately broken path-cancellation cases, 650 deliberately broken arm-energy equality cases, 125 direct short-time matrix-exponential tests, two symbolic identities, and one fixed nonuniform example: 3,378 categorized assertion groups. Run `python3 verify.py` in an environment containing NumPy, SciPy, and SymPy. All tests passed in the prepared reference execution. Finite tests independently detect algebraic or implementation mistakes but are **not** a proof of the theorem on an infinite chain; the complete proof is in the previous section.

## Relationship to prior work

Aharonov–Bohm caging through magnetic interference was established by Vidal, Mosseri, and Douçot (1998). Flach and collaborators (2013) developed detangling rotations for flat-band Fano lattices. Later diamond-chain work explicitly established compact states for symmetric on-site potentials in fixed-hopping models and examined the disruption of caging by generic disorder. General periodic all-bands-flat constructions and the use of local unitary changes of basis are consequently **not** claimed as new.

The contribution here is the joint *if-and-only-if* classification of **every-hub, every-time one-cage confinement** for arbitrary bounded cell-dependent complex hopping amplitudes and real site energies (without Bloch translation invariance), together with its exact inhomogeneous trimer decomposition and the discriminating order-\(t^4\) versus order-\(t^6\) probability laws for the two independent ways confinement can fail. Symmetric on-site disorder in the standard fixed-coupling diamond chain is a known special case. The proof is a direct matrix argument, conceptually related to the known detangling method; an equivalent criterion could appear implicitly elsewhere in the extensive flat-band literature.

## Limitations

The result assumes a noninteracting single-particle, bounded self-adjoint nearest-neighbor diamond Hamiltonian on a two-sided infinite chain with nonzero couplings on all four arms of each diamond. Vanishing hoppings, direct arm-arm or hub-hub couplings, interactions, non-Hermitian gain/loss and infinite-range hopping are excluded. Local caging does not imply a globally flat energy **set** under inhomogeneous disorder: the localized eigenvalues can depend on cell, and their closure can be continuous as a set. The short-time laws concern transition specifically between adjacent hub sites, not total probability outside a multi-cell region. Robustness to statistically independent, unconstrained disorder is not asserted. Priority is subject to comparison with any unlocated equivalent treatment of general correlated hopping disorder.

## References

1. J. Vidal, R. Mosseri, B. Douçot, *Aharonov–Bohm Cages in Two-Dimensional Structures*, arXiv:cond-mat/9806068v1 (public preprint June 5, 1998), https://arxiv.org/abs/cond-mat/9806068.
2. S. Flach, D. Leykam, J. D. Bodyfelt, P. Matthies, A. Desyatnikov, *Detangling flat bands into Fano lattices*, arXiv:1311.5689 (2013), https://arxiv.org/abs/1311.5689.
3. G. Gligorić, D. Leykam, A. Maluckov, *Influence of Different Disorder Types on Aharonov–Bohm Caging in the Diamond Chain*, arXiv:1909.07055 (2019), https://arxiv.org/abs/1909.07055.
4. A. Ahmed, A. Ramachandran, I. Khaymovich, A. Sharma, *Flat-band-based multifractality in the all-bands-flat diamond chain*, arXiv:2205.02859 (2022), https://arxiv.org/abs/2205.02859.
5. C. Danieli, A. Andreanov, T. Mithun, S. Flach, *Nonlinear caging in all-bands-flat lattices*, arXiv:2004.11871 (2020), https://arxiv.org/abs/2004.11871.
6. L. Toikka, A. Andreanov, *Necessary and sufficient conditions for flat bands in M-dimensional N-band lattices*, arXiv:1810.01076 (2018), https://arxiv.org/abs/1810.01076.
7. A. M. Marques, D. Viedma, V. Ahufinger, R. G. Dias, *Impurity flat band states in the diamond chain*, *Communications Physics* 7, 387 (2024), https://doi.org/10.1038/s42005-024-01886-1.
