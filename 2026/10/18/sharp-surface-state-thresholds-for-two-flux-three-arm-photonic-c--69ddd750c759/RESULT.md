# Sharp surface-state thresholds for two-flux three-arm photonic cages

## Finding

The open-ended three-arm (theta) tight-binding lattice of Brosco–Pilozzi–Conti has an exact surface-mode existence criterion in *both* finite and semi-infinite geometries, uniformly in two magnetic fluxes and four positive hopping strengths. Define
\[
 u=J_1^2+2J_{t1}^2,\quad v=J_2^2+2J_{t2}^2,\quad
 q=J_1J_2+J_{t1}J_{t2}(e^{-i\phi_1}+e^{i\phi_2}),\quad c=|q|.
\]
Then \(u,v>0\) and \(0\le c^2\le uv\). The squared-energy bulk interval is \([u+v-2c,u+v+2c]\), in addition to zero-energy flat bands.

For a chain terminated on the left at a hub, a localized *nonzero* semi-infinite surface pair exists **if and only if** \(c<v\) and \(u>c^2/v\); its exact eigenenergies are
\[
 E_{\mathrm{surf}}^\pm=\pm\sqrt{u-c^2/v}.
\]
The corresponding hub amplitudes decay geometrically as \((-\overline q/v)^n\). If \(c<v\) but \(u=c^2/v\), the pair collapses to one additional hub-supported zero eigenvector; it must not be counted as two nonzero surface states. If \(c\ge v\), there is no additional localized hub eigenmode outside the flat-band zero eigenspace. For \(c<v\), the squared-energy separation from the bottom dispersive edge is exactly \((v-c)^2/v\).

For the **finite** left-terminated model with exactly \(N\ge2\) hubs and \(3N\) arm sites, and \(c>0\), there is exactly one positive squared eigenvalue **strictly below the infinite-volume bulk lower edge** if and only if
\[
 \boxed{v>c\left(1+\frac1N\right).}
\]
At equality the eigenvalue is at the edge; below that inequality there is none. There are exactly \(2N\) zero eigenvalues, and each positive squared eigenvalue yields one positive and one negative energy. When \(c=0\), the nonzero energies are \(\pm\sqrt u\) (once each) and \(\pm\sqrt{u+v}\) (each with multiplicity \(N-1\)), with \(2N\) zero modes.

For all four hoppings equal to \(J>0\) and equal fluxes \(\phi_1=\phi_2=\phi\in[0,\pi]\), the finite detached pair exists exactly when \(\phi>\phi_N=\arccos(1-3/[2(N+1)])\). As \(N\to\infty\), \(\phi_N\sim\sqrt{3/(N+1)}\). At the complete-caging flux \(\phi=2\pi/3\), the surface pair is \(\pm\sqrt3J\) and the remaining dispersive energies are \(\pm\sqrt6J\). On the semi-infinite lattice, as \(\phi\downarrow0\), the hub localization length is asymptotic to \(3/\phi^2\) unit cells, while the positive-energy surface-to-bulk separation is
\[
 E_{\mathrm{bulk},\min}-E_{\mathrm{surf}}
 =\frac{J}{6\sqrt2}\,\phi^3+O(\phi^5).
\]
Thus the zero-flux surface state emerges with an explicitly divergent length and a *cubic* energy separation, although its squared-energy separation is quartic in flux.

## Assumptions and scope

All four hoppings \(J_1,J_2,J_{t1},J_{t2}\) are strictly positive real numbers and both fluxes are arbitrary real phases modulo \(2\pi\). Write the one-particle chiral Hamiltonian as
\[
 H=\begin{pmatrix}0&T\\T^*&0\end{pmatrix},\qquad
 (Ty)_n=t\cdot y_n+s\cdot y_{n-1},
\]
where \(t=(J_1,J_{t1}e^{-i\phi_1},J_{t1}e^{i\phi_2})\), \(s=(J_2,J_{t2},J_{t2})\), and the second term is absent at \(n=0\). For a finite chain \(n\in\{0,\dots,N-1\}\) and \(y_{-1}=0\); for the half-line \(n\in\mathbb N_0\) and \(y_{-1}=0\). The adjoint is taken in the standard complex Hilbert space. Here \(\cdot\) denotes an ordinary row-by-column product, so \(q=t\cdot\overline s\).

The finite termination contains the three arms attached to the last hub, but does **not** include an extra right terminal hub; a different termination may have a different spectrum. The bulk bands refer to the translation-invariant full-line operator. The terms *surface pair* and *detached* concern nonzero energies and the lower edge of the nonzero squared-energy dispersive band; they do not exclude the pre-existing zero flat-band states.

## Proof

**1. Bright-sector reduction.** Direct multiplication gives
\[
 TT^*=\begin{pmatrix}
 u&q&0&\cdots\\ \overline q&u+v&q&\ddots\\0&\overline q&u+v&\ddots\\\vdots&\ddots&\ddots&\ddots
 \end{pmatrix}
 =:B.
\]
This holds for the finite and half-infinite operators. A diagonal unitary makes the off-diagonal entries real and equal to \(c\). On the full line, Fourier transformation gives the bright squared bands \(u+v+2c\cos k\); its chiral square roots are the two nonzero dispersive bands, and vectors in \(\ker T\) give zero flat bands. Every row of finite \(T\) has a private block of three columns belonging to that row, and the first row is nonzero; successively eliminating rows shows \(T\) has full row rank \(N\). Consequently \(\dim\ker T=3N-N=2N\), and \(B_N=TT^*\) is positive definite. Its eigenvalues yield exactly all nonzero eigenvalues of \(H_N\), in opposite-sign pairs.

**2. Half-line surface criterion.** For \(q\ne0\), an eigenvector of \(B\) with square-summable hub amplitudes below the lower band edge must have \(x_n=r^n x_0\), where \(|r|<1\), by the constant-coefficient interior recurrence; the other characteristic root has modulus exceeding one. The boundary equation is \(\mu=u+qr\), and the interior equation is \(\mu=u+v+qr+\overline q/r\). Subtracting gives \(r=-\overline q/v\), so
\[
 |r|=c/v,\qquad \mu=u-c^2/v.
\]
It follows that such a solution exists precisely when \(c<v\), and its energy is nonzero precisely when \(\mu>0\). By Cauchy–Schwarz, \(\mu\ge0\). If \(\mu=0\) then \(T^*x=0\), and \((x,0)\) is a single additional hub-supported eigenstate of \(H\) at zero. If \(\mu>0\), its two chiral partners are \((x,\pm T^*x/\sqrt\mu)\), normalized by \(1/\sqrt2\) when \(\|x\|=1\). For \(q=0\), \(B\) is diagonal with first entry \(u\) and all later entries \(u+v\); the same formula applies with \(r=0\). At \(c=v\), the formal geometric root has unit modulus, hence no bound state. For \(c>v\), it grows. The boundary is a rank-one negative perturbation of the constant Jacobi matrix, which can produce at most one bound squared eigenvalue below its band, and no eigenvalue above its upper band. Finally,
\[
 (u+v-2c)-(u-c^2/v)=(v-c)^2/v.
\]
Thus every case of the claimed surface classification is accounted for, including the zero-energy exceptional case and complete caging.

**3. Finite threshold, including strict boundary.** For \(c>0\), gauge-transform \(B_N=B_{0,N}-v|e_0\rangle\langle e_0|\), with \(B_{0,N}\) the \(N\)-site uniform tridiagonal matrix with diagonal \(d=u+v\) and off-diagonal \(c\). The lowest eigenvalue of \(B_{0,N}\) is strictly greater than \(d-2c\). For any \(z\le d-2c\), the finite-dimensional rank-one determinant lemma gives
\[
 \det(B_N-z)=\det(B_{0,N}-z)\bigl(1-vG_N(z)\bigr),
 \quad G_N(z)=\langle e_0,(B_{0,N}-z)^{-1}e_0\rangle.
\]
Here \(G_N\) is strictly increasing as \(z\) increases below the uniform matrix spectrum, with limit zero as \(z\to-\infty\). At \(z=d-2c\), the resolvent is \(c^{-1}\) times the inverse of the positive definite tridiagonal matrix with diagonal \(2\) and off-diagonal \(1\). Conjugating by alternating signs converts it to the path Dirichlet Laplacian, whose endpoint inverse diagonal entry is \(N/(N+1)\). Thus
\[
 G_N(d-2c)=\frac{N}{c(N+1)}.
\]
The secular factor has a unique root **strictly** below \(d-2c\) exactly when \(vG_N(d-2c)>1\), equivalent to \(v>c(1+1/N)\); equality places the root at the edge. Interlacing, or the rank-one secular equation, excludes a second detached squared eigenvalue. At \(c=0\), direct diagonalization gives one squared eigenvalue \(u\) and \(N-1\) at \(u+v\). This proves the full finite-volume assertion.

**4. Equal-hopping flux scale.** With all hoppings equal \(J\) and equal phase \(\phi\), we have \(u=v=3J^2\) and \(c=J^2|1+2\cos\phi|\). For \(0\le\phi\le\pi\), the inequality \(c<3J^2N/(N+1)\) reduces to \(\phi>\phi_N\): after \(\phi=2\pi/3\), the absolute value rises only to \(J^2\), below the threshold for all \(N\ge2\). Expanding \(\arccos(1-z)\) gives \(\phi_N\sim\sqrt{3/(N+1)}\). Near zero, \(c/J^2=3-\phi^2+\phi^4/12+O(\phi^6)\). Hence \(\log(v/c)=\phi^2/3+O(\phi^4)\), proving the length law. Direct algebra gives the exact squared-energy gap \((v-c)^2/v\). Since both positive energies are asymptotic to \(\sqrt2 J\,\phi\), division by their sum yields
\[
 \sqrt{6J^2-2c}-\sqrt{3J^2-c^2/(3J^2)}
 =\frac{J}{6\sqrt2}\phi^3+O(\phi^5),
\]
which finishes the proof.

## Verification

The standalone program `checks/verify.py` constructs the independent physical hub-to-arm coupling matrix for \(N=2,\ldots,16\), forms \(TT^*\) directly, and compares its spectrum with the derived tridiagonal matrix and strict finite-threshold rule. For \(N\le8\) it also diagonalizes the full \(4N\)-vertex chiral Hamiltonian and checks the complete eigenvalue list. It tests 2310 parameter/size instances, including complex phase choices, caging points, parallel couplings, and flux values on either side of the finite threshold; the asymptotic cubic coefficient is tested separately. The program requires Python 3.9+ and NumPy and runs with `python3 checks/verify.py` from this package. These finite checks are supporting evidence; all-size and half-line conclusions follow from the preceding exact argument.

## Relationship to prior work

Brosco, Pilozzi, and Conti introduced this exact two-flux three-arm lattice, found its Bloch dispersions and phase-controlled complete caging, and examined finite wavepacket propagation [1]. Their bulk formulas agree with the squared bands stated here. The new result concerns **open-boundary** spectral existence, finite-length threshold and small-flux critical energy/length laws, none of which is supplied by those bulk formulas alone. Kremer et al. [2] and Mukherjee et al. [3] establish boundary states of special *two-arm* rhombic Aharonov–Bohm cages; their known special-case boundary eigenenergies are not claimed as new here. The present result instead gives sharp inequalities for the general *three-arm* model with two independent fluxes and unequal hoppings, including the singular zero-energy exception. Generic rank-one Jacobi spectral theory underlies the proof but does not itself tabulate this physical flux-phase threshold or its cubic near-zero scaling.

## Limitations

Only one left-hub-terminated chain is classified; adding a terminal hub, choosing other boundary cuts, spatial disorder, interactions, or gain/loss changes the model. A squared-energy eigenvalue below the dispersive interval is not necessarily separated from the existing zero-energy flat band when the surface energy tends to zero. The semi-infinite surface eigenvector has algebraic and spectral multiplicity one per nonzero sign; at \(\mu=0\) there is one additional hub-type zero mode rather than a nonzero pair. The numerical tests are finite and do not replace the analytic proof. Independent external priority and correctness assessment has not been performed.

## References

[1] V. Brosco, L. Pilozzi, C. Conti, *Two-flux tunable Aharonov-Bohm caging in a photonic lattice*, arXiv:2102.06682v1 (first public 2021-02-12); published as *Two-flux tunable Aharonov-Bohm effect in a photonic lattice*, Physical Review B **104**, 024306 (2021), DOI:10.1103/PhysRevB.104.024306.

[2] M. Kremer et al., *Non-quantized square-root topological insulators: a realization in photonic Aharonov-Bohm cages*, arXiv:1805.05209 (2018), including supplemental edge-state analysis.

[3] S. Mukherjee et al., *Experimental observation of Aharonov-Bohm cages in photonic lattices*, arXiv:1805.03564 (2018), including its boundary-mode discussion.
