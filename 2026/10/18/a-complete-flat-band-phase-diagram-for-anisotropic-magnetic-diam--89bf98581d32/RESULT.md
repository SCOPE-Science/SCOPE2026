# A complete flat-band phase diagram for anisotropic magnetic diamond chains

## Finding
An infinite magnetic diamond (rhombic) tight-binding chain can have exactly zero, one, or three distinct flat-band energies, but never exactly two. The classification below covers four arbitrary positive hopping magnitudes, three arbitrary real periodic site potentials, and every magnetic flux. It also determines the minimum span of compactly supported flat-band states: one or two consecutive unit cells.

The three-flat-band regime is a generalized Aharonov–Bohm cage: the two products of arm hoppings must agree and the flux must be half a flux quantum, while the common side-site potential and central potential remain arbitrary. A *second*, inequivalent one-flat-band regime exists for unequal side-site potentials, with explicit tuning and only zero or half flux.

## Assumptions and scope
Each cell is indexed by \(j\in\mathbb Z\) and contains a central site \(S_j\), upper side site \(U_j\), and lower side site \(D_j\). Its four hopping magnitudes are \(a,b,c,d>0\). Onsite energies are \(u\) on central sites, \(v\) on upper sites, and \(w\) on lower sites. One bond per diamond carries phase \(e^{i\phi}\), with \(\phi\) defined modulo \(2\pi\). There are no direct bonds between side sites and no other interactions. The resulting infinite Hamiltonian on \(\ell^2(\mathbb Z;\mathbb C^3)\) is self-adjoint and bounded.

The Bloch Hamiltonian in the cell convention \(z=e^{ik}\), \(|z|=1\), is
\[
H(z)=\begin{pmatrix}
u&a+bz&c+d e^{i\phi}z\\
a+bz^{-1}&v&0\\
c+d e^{-i\phi}z^{-1}&0&w
\end{pmatrix}.
\]
A *flat-band energy* is a real \(E\) such that \(\det(H(z)-EI_3)=0\) for every \(|z|=1\). Distinct flat-band energies are counted without multiplying by the infinitely many translated states. A state occupies one (respectively two) cells if its site amplitudes vanish outside one (respectively two consecutive) triples \((S_j,U_j,D_j)\).

Set \(A=a^2+b^2\), \(B=c^2+d^2\), \(C=ab\), \(D=cd\). All four are strictly positive.

**Classification.** If \(v=w\), \(E=v\) is flat for all hoppings and flux. The chain has three flat energies if and only if \(\phi\equiv\pi\pmod{2\pi}\) and \(C=D\); the other two flat energies then are
\[
E_\pm=\frac{u+v\pm\sqrt{(u-v)^2+4(A+B)}}2.
\]
Outside this regime it has exactly the single flat energy \(v\).

If \(v\ne w\), one flat energy occurs precisely under all three conditions
\[
\phi\equiv0\text{ or }\pi\pmod{2\pi},\qquad
C+sD\ne0,\qquad
u=E_*+\frac{A}{v-E_*}+\frac{B}{w-E_*},
\]
where \(s=\cos\phi\in\{1,-1\}\) and
\[
E_* =\frac{Cw+sDv}{C+sD}.
\]
If any condition fails, there is no flat band. The denominators are nonzero automatically under the displayed assumptions: \(E_*\notin\{v,w\}\). Thus two distinct flat-band energies never occur.

Every listed flat energy admits a nonzero eigenfunction supported on at most two consecutive unit cells. A one-cell eigenfunction exists precisely for the branch \(v=w\), \(\phi\equiv0\pmod{2\pi}\), \(ad=bc\). In all other cases the two-cell upper bound is sharp.

## Proof
Write \(f(z)=a+bz\) and \(g(z)=c+d e^{i\phi}z\). For real \(E\) and \(|z|=1\), the determinant expansion gives
\[
\begin{aligned}
\det(H(z)-EI_3)
&=p_0(E)+p_+(E)z+p_-(E)z^{-1},\\
p_0(E)&=(u-E)(v-E)(w-E)-A(w-E)-B(v-E),\\
p_+(E)&=-C(w-E)-D e^{i\phi}(v-E),\\
p_-(E)&=\overline{p_+(E)}.
\end{aligned}
\]
The matrix determinant vanishes identically on the unit circle if and only if \(p_0(E)=p_+(E)=0\). This is because distinct Laurent monomials are linearly independent on the circle.

If \(v=w\), \(p_+(E)=-(v-E)(C+D e^{i\phi})\). It always vanishes at \(E=v\), and \(p_0(v)=0\) as well. Since \(C,D>0\), the complex number \(C+D e^{i\phi}\) vanishes if and only if \(C=D\) and \(e^{i\phi}=-1\). Without this exceptional cancellation, \(p_+\) vanishes at no other energy. With it, the determinant reduces to
\[
(v-E)\big((u-E)(v-E)-A-B\big).
\]
The two roots of the quadratic factor are \(E_\pm\) as stated, and are distinct from each other and from \(v\), because \(A+B>0\). This proves the complete equal-side-potential case.

If \(v\ne w\), the coefficient condition is
\[
C(w-E)+D e^{i\phi}(v-E)=0.
\]
An admissible \(E\) cannot equal \(v\) or \(w\), because \(C,D>0\) and \(v\ne w\). Hence the ratio \((w-E)/(v-E)\) is a nonzero *real* number, so \(e^{i\phi}\) must be real: precisely \(0\) or \(\pi\) flux. With \(s=e^{i\phi}=\pm1\), the coefficient equation is \((C+sD)E=Cw+sDv\). If \(C+sD=0\), it would force \(C(w-v)=0\), impossible; otherwise it has exactly the solution \(E_*\). Dividing \(p_0(E_*)=0\) by the nonzero product \((v-E_*)(w-E_*)\) yields exactly the stated equation for \(u\). The converse follows by substituting these conditions back into every Laurent coefficient. This proves exhaustiveness and the zero/one/three count.

To construct finitely supported eigenstates, observe that a nonzero Bloch eigenvector whose components are Laurent polynomials is the Fourier transform of a finitely supported lattice eigenfunction. For \(v=w\) and \(E=v\), the polynomial vector
\[
\psi_v(z)=\big(0,-g(z),f(z)\big)^T
\]
lies in \(\ker(H(z)-vI_3)\) for every \(z\), and only the powers \(z^0,z^1\) occur. For \(v\ne w\), on the tuned branch, the polynomial vector
\[
\psi_*(z)=\big((v-E_*)(w-E_*),
-(w-E_*)\overline{f(z)},
-(v-E_*)\overline{g(z)}\big)^T
\]
vanishes under \(H(z)-E_*I_3\); the side equations cancel individually, and the central equation is the vanishing determinant. Here complex conjugation denotes the restriction to \(|z|=1\), hence the side components are Laurent polynomials in \(z^{-1}\). For the other two flat energies \(E_\pm\) in the all-flat case, use
\[
\psi_\pm(z)=\big(v-E_\pm,-\overline{f(z)},-\overline{g(z)}\big)^T.
\]
The side equations again cancel, and the central equation follows from \(|f(z)|^2+|g(z)|^2=A+B\), which holds exactly in the all-flat regime. Every vector displayed is nonzero as a Laurent-polynomial vector; its support lies in at most two consecutive cells.

For sharpness, suppose a one-cell eigenfunction existed at some real energy \(E\). Its Bloch transform would be a constant nonzero vector \((S,U,D)^T\). In the lower two Bloch eigenvalue equations, the \(z^{-1}\) coefficients are \(bS\) and \(d e^{-i\phi}S\), so \(S=0\) because \(b,d>0\). Then \((v-E)U=(w-E)D=0\). The central Bloch equation reads \((a+bz)U+(c+d e^{i\phi}z)D=0\) for every \(z\). Neither \(U\) nor \(D\) can vanish separately, so \(v=w=E\), and the two scalar conditions for the coefficients are \(aU+cD=0\) and \(bU+d e^{i\phi}D=0\). Their nonzero solution exists precisely when \(ad e^{i\phi}=bc\). Positivity forces \(e^{i\phi}=1\) and \(ad=bc\). Conversely, in that case the constant vector \((0,c,-a)^T\) is a valid one-cell eigenvector. This proves the exact one-versus-two-cell criterion.

## Verification
The companion self-contained Python program `verify.py` computes the \(3\times3\) Bloch determinant via the permutation formula, independently of the claimed Laurent coefficients. It checks 450 general parameter profiles, 200 analytically tuned unequal-side-potential profiles, and 200 equal-side-potential/all-flat profiles, comparing 29,250 sampled complex determinants. It separately verifies 15 exact rational tuned identities, with a fixed deterministic seed. Executing `python3 verify.py` prints:

```text
VERIFY_OK coefficient_profiles= 850 direct_determinants= 29250 exact_tuned= 15
```

All-order validity follows from the Laurent coefficient proof, not from finite tests.

## Relationship to prior work
Sabri and Youssef [1] establish general Laurent-polynomial criteria, compact-localization facts, and semialgebraic flat-band parameter loci for periodic graph operators, and explicitly leave broad potential-locus classification problems open for cells of size at least three. Their results justify the algebraic approach but do not give this four-positive-hopping/three-potential/flux *complete explicit* diamond-chain classification or the precise one-versus-two-cell threshold.

Xia and coauthors [2] analyze the same three-site rhombic motif with equal nearest-neighbor hopping magnitudes and selected symmetric/antisymmetric side-site detunings. Their symmetry-protected and centrally detuned flat-band special cases are **antecedents**, not claimed as new in isolation. Their main strain parameter also introduces a side-to-side next-nearest-neighbor hopping, absent from the present model. Danieli and coauthors [3] explain the conventional zero-energy rhombic flat band, the half-flux three-band cage for equal couplings, and general compact-localized-state construction techniques. These known symmetric cases are included but not relabeled as discoveries.

Marques and coauthors [4] give exact conventional-flux Bloch energies and two-cell localized vectors for an equal-hopping clean diamond chain, then study *local impurity* potentials on open chains. Their Section III and conclusions do not give a uniform asymmetric-positive-hopping flat-band locus under arbitrary periodic onsite potentials, nor the sharp single-cell criterion. The present result is an explicit simultaneous *parameter classification* under the stated model rather than a new general criterion for all periodic graphs.

## Limitations
All four hopping magnitudes must be strictly positive; removing an edge changes the classification. The sites form a translationally invariant infinite chain, and the potentials are constant from cell to cell. Interactions, random potentials, direct side-to-side hoppings, defects and other lattices are excluded. Bloch eigenfunctions at band touchings need not be continuous in a chosen normalized gauge, but the displayed Laurent-polynomial compact states are valid. No completeness of translated compact states as a basis is claimed. Although the stated full parameter classification was not located in the inspected primary sources, a still-unidentified broader result or alternative parametrization might imply it; no independent novelty verification is asserted.

## References
1. M. Sabri and P. Youssef, *Flat bands of periodic graphs*, arXiv:2304.06465 (first posted 13 April 2023), https://arxiv.org/abs/2304.06465.
2. S. Xia et al., *Band evolution and Landau–Zener Bloch oscillations in strained photonic rhombic lattices*, *Optics Express* **29** (2021), 37503–37514, https://doi.org/10.1364/OE.441554.
3. C. Danieli et al., *Flat band fine-tuning and its photonic applications*, *Nanophotonics* (2024), https://doi.org/10.1515/nanoph-2024-0135.
4. A. M. Marques et al., *Impurity flat band states in the diamond chain*, arXiv:2407.14405v1 (19 July 2024), subsequently *Communications Physics* **7** (2024), 387, https://arxiv.org/abs/2407.14405.
