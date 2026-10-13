# Complete gapped flat-band phase diagram of a weighted triangle-bridge chain

## Finding

For every choice of positive edge weights \(p,q,r,s>0\) and arbitrary real onsite energies \(Q_A,Q_B,Q_C\), define
\[
g=\frac{qr}{p},\qquad
\alpha=Q_A-Q_C+g-\frac{pr}{q},\qquad
\beta=Q_B-Q_C+g-\frac{pq}{r}.
\]
The operator has a flat band **if and only if**
\[
\boxed{\alpha\beta=s^2}.
\]
When this equation holds, exactly one flat band exists, at
\[
\boxed{\lambda=Q_C-\frac{qr}{p}}.
\]
It is spectrally isolated (separated by a positive spectral gap from the other bands), has a one-dimensional Floquet eigenspace at every quasimomentum, and its global eigenspace is spanned by translates of a two-cell compactly supported eigenfunction. The admissible potentials form a smooth quadric with two connected components: for \(\alpha>0\) the flat band is the strictly lowest band, whereas for \(\alpha<0\) it is the strictly middle band. It is never the top band.

For equal unit hoppings, the criterion takes the particularly simple nonlinear form
\[
\boxed{(Q_A-Q_C)(Q_B-Q_C)=1},\qquad\lambda=Q_C-1.
\]
Thus the unweighted adjacency operator has no flat band at zero potential, but the potentials \((Q_A,Q_B,Q_C)=(1,1,0)\) and \((-1,-1,0)\) create respectively an isolated lowest and an isolated middle flat band, both at energy \(-1\).

## Assumptions and scope

The graph has vertices \(A_n,B_n,C_n\), indexed by \(n\in\mathbb Z\), with four undirected edges per cell: \(A_nB_n\) of weight \(p\), \(B_nC_n\) of weight \(q\), \(C_nA_n\) of weight \(r\), and \(A_nB_{n+1}\) of weight \(s\). The weights are independent of \(n\) and strictly positive. A real onsite potential is constant on each vertex orbit and equals \(Q_A,Q_B,Q_C\) there. The operator is the bounded self-adjoint weighted adjacency operator plus this diagonal potential on \(\ell^2(\mathbb Z;\mathbb C^3)\). A flat band means a real energy that is a Bloch eigenvalue for every \(z\) with \(|z|=1\), equivalently a point-spectrum eigenvalue of the periodic operator.

With the Fourier convention \(\sum_{n\in\mathbb Z}\psi_n z^n\), the Hermitian Bloch matrix is
\[
H(z)=\begin{pmatrix}
Q_A&p+sz&r\\
p+sz^{-1}&Q_B&q\\
r&q&Q_C
\end{pmatrix},\qquad |z|=1.
\]

## Proof

Put \(x_A=Q_A-E\), \(x_B=Q_B-E\), \(x_C=Q_C-E\). Direct determinant expansion gives the exact Laurent identity
\[
\begin{aligned}
\det(H(z)-EI)={}&x_Ax_Bx_C-q^2x_A-r^2x_B-(p^2+s^2)x_C+2pqr\\
&+s(qr-px_C)(z+z^{-1}).
\end{aligned}
\]
If \(E\) is a flat energy, the coefficient of \(z\) must vanish. Since \(s,p>0\), this forces \(x_C=qr/p=g\) and therefore \(E=\lambda=Q_C-g\). In particular no second flat energy is possible.

At this forced energy, eliminate the \(C\)-coordinate by a Schur complement. Because \(g>0\) and \(rq/g=p\), this Schur complement is exactly
\[
S(z)=\begin{pmatrix}\alpha&sz\\sz^{-1}&\beta\end{pmatrix}.
\]
Consequently
\[
\det(H(z)-\lambda I)=g\det S(z)=g(\alpha\beta-s^2).
\]
Thus the displayed quadric is simultaneously necessary and sufficient for a flat band, without excluding any positive-weight or real-potential case.

On the quadric, \(\alpha\beta=s^2>0\), so neither \(\alpha\) nor \(\beta\) vanishes and they have the same sign. The matrix \(S(z)\) has rank one for every \(|z|=1\); its nonzero eigenvalue has the sign of \(\alpha\). The Schur-complement inertia theorem, using the positive pivot \(g\), now shows that \(H(z)-\lambda I\) has inertia \((2,0,1)\) for \(\alpha>0\), and \((1,1,1)\) for \(\alpha<0\), in positive/negative/zero order. Thus \(\lambda\) is respectively the simple bottom or simple middle Bloch eigenvalue for every phase. Simplicity and continuous dependence of the three ordered Bloch eigenvalues on the compact unit circle yield a strictly positive separation from the other two spectral bands. The conclusion concerns each fixed admissible parameter set; no parameter-uniform gap lower bound is asserted.

An explicit nonvanishing Laurent-polynomial nullvector is
\[
v(z)=\begin{pmatrix}-sz\\\alpha\\(rsz-q\alpha)/g\end{pmatrix}.
\]
Substitution using \(\alpha\beta=s^2\) proves \((H(z)-\lambda I)v(z)=0\). The components contain only the powers \(1,z\), giving a compact eigenfunction supported within two neighboring cells. Since \(\alpha\ne0\), this vector does not vanish at any Bloch phase; the fiber kernel is its span everywhere. Fourier-transforming an arbitrary square-integrable eigenfunction then gives a scalar \(L^2\) multiple of \(v\). Density of trigonometric polynomials in \(L^2\) shows that translates of the compact state span the full flat-band eigenspace.

Finally, the affine change of potential coordinates \((Q_A,Q_B,Q_C)\mapsto(\alpha,\beta,Q_C)\) is invertible. The variety \(\alpha\beta=s^2\) is smooth and has precisely two connected components, corresponding to \(\alpha>0\) and \(\alpha<0\). This proves the complete classification.

## Verification

The accompanying `verify_triangle_bridge.py` checks the full Laurent determinant identity, the Schur-factorized flat-band condition, the displayed nonvanishing Bloch eigenvector, the decisive nonzero principal minor, and four explicit rational test cases with SymPy. Run `python3 verify_triangle_bridge.py` with SymPy installed; expected output begins `VERIFY_OK`. The all-parameter proof is the determinant-Schur-inertia argument above. The four finite test cases establish no all-parameter conclusion by themselves.

## Relationship to prior work

Sabri and Youssef [1] prove a general semialgebraic description of the exceptional onsite-potential set and emphasize the rarity and geometry of flat bands. Their Section 7 examples include affine potential conditions, but not this weighted three-orbit chain's exact nonlinear quadric, two-component classification, or strict spectral ordering. The later general theorem of Faust and Kachkovskiy [2] proves generic absence for fixed connected periodic graphs; its implication is only that exceptional potentials lie in a proper algebraic subset, not the exact defining equation or the existence, simplicity, isolation, and order of the bands exhibited here. The quasi-one-dimensional triangle lattice of Schulze, Bercioux, and Urban [3] uses a two-site Bloch matrix and is not the three-site bridge graph. The diamond-necklace study [4] considers a four-site fundamental cell and a symmetry-generated flat band, not the present nonlinear tuning locus. The familiar general Bloch and compact-localization principles are used rather than claimed as new.

## Limitations

The result concerns this fixed triangle-plus-bridge graph topology, nearest-cell edges, real periodic onsite energies, and strictly positive real hopping weights. It does not classify arbitrary three-site periodic graphs, complex magnetic edge phases, negative or vanishing hoppings, interactions, or nonlinear perturbations. The spectral gaps need not have a uniform positive lower bound as weights and potentials vary. The explicit algebra and examples do not imply that generic absence or the general compact-eigenfunction correspondence was previously unknown. Weakly indexed equivalent calculations for the same motif in alternate tight-binding notation remain a literature risk.

## References

[1] Mostafa Sabri and Pierre Youssef, *Flat bands of periodic graphs*, arXiv:2304.06465 (first public version, 2023-04-13), Sections 1, 2, 7. https://arxiv.org/abs/2304.06465

[2] Matthew Faust and Ilya Kachkovskiy, *Absence of flat bands for discrete periodic graph operators with generic potentials*, arXiv:2509.01927 (2025), Theorem 1.4 and Section 3.4. https://arxiv.org/html/2509.01927v1

[3] Michael Schulze, Dario Bercioux and Daniel F. Urban, *Adiabatic pumping in the quasi-one-dimensional triangle lattice*, arXiv:1208.6113 (2012), two-site Bloch Hamiltonian. https://arxiv.org/abs/1208.6113

[4] *Compact localized boundary states in a quasi-1D electronic diamond-necklace chain*, Quantum Frontiers (2023), DOI:10.1007/s44214-023-00026-0. https://doi.org/10.1007/s44214-023-00026-0
