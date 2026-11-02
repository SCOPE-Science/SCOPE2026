# Bonded double-apex antiferromagnetic rings: an exact first-order conical transition

## Finding

For every odd integer \(n\ge5\), the classical antiferromagnetic Heisenberg ring with two equivalent, mutually coupled apex spins has an exactly determined zero-temperature phase diagram. Define
\[
 c=-\cos(\pi/n),\quad a=J(1-c)=J(1+\cos(\pi/n)),\quad K_{\mathrm c}=\sqrt{2aL/n}.
\]
For exchange constants \(J,K,L>0\) satisfying \(0<L<na/2\), the ground energy is
\[
 E_{\min}(K)=\begin{cases}
 nJc-L,&0<K\le K_{\mathrm c},\\
 nJc-nK^2/a+L,&K_{\mathrm c}\le K\le a,\\
 n(J-2K)+L,&K\ge a.
 \end{cases}
\]
The formulas agree at both joining points. As \(K\) passes through \(K_{\mathrm c}\), the magnitudes of the normalized ring magnetization and the sum of the two apex spins jump, respectively, from \(0\) and \(0\) to \(K_{\mathrm c}/a\) and \(2\). In particular the apex correlation jumps from \(-1\) to \(+1\). At the transition itself an entire interval of exact ground-state order parameters coexists. In the intermediate regime \(K_{\mathrm c}<K<a\), all ground states have conical rings and nonzero oriented apex–rim chirality; the two chiralities have equal ground energy.

## Assumptions and scope

There are \(n\) classical spins \(\mathbf s_j\in\mathbb R^3\) of unit length, indexed cyclically by \(j\in\{0,\ldots,n-1\}\), and two unit apex spins \(\mathbf h_+,\mathbf h_-\). The energy is
\[
 H=J\sum_{j=0}^{n-1}\mathbf s_j\cdot\mathbf s_{j+1}
 +K(\mathbf h_++\mathbf h_-)\cdot\sum_{j=0}^{n-1}\mathbf s_j
 +L\mathbf h_+\cdot\mathbf h_-.
\]
The graph is the join of a cycle with a bonded two-site apex pair. All \(n\) rim bonds have coupling \(J\), all \(2n\) spokes have coupling \(K\), and the apex-pair bond has coupling \(L\). We require \(J,K,L>0\), \(n\ge5\) odd, and \(2L<na\). The system is an equilibrium classical unit-vector model; this statement makes no finite-temperature or quantum-spin claim.

Write \(\mathbf M=\sum_j\mathbf s_j\), \(m=|\mathbf M|/n\), and \(s=|\mathbf h_++\mathbf h_-|\). Thus \(0\le m\le1\) and \(0\le s\le2\). The exact order parameters for every ground state are:

- \(0<K<K_{\mathrm c}\): \(m=s=0\). The rim forms a planar maximally twisted antiferromagnetic spiral, while the apex spins are antiparallel and otherwise unconstrained.
- \(K=K_{\mathrm c}\): \(0\le s\le2\) and \(m=K_{\mathrm c}s/(2a)\). This is a continuum of coexisting ground states.
- \(K_{\mathrm c}<K<a\): \(s=2\), \(m=K/a\). The apex spins coincide and point opposite the rim magnetization; the rim is a noncoplanar cone with either handedness.
- \(K\ge a\): \(s=2\), \(m=1\). All rim spins coincide and the two apex spins point oppositely.

In all states with \(ms>0\), the apex resultant points strictly antiparallel to \(\mathbf M\). At \(m=s=0\), its direction is immaterial. For a maximally twisted cone, let \(q=(n-1)\pi/n\). One choice is
\[
 \mathbf s_j=(\sqrt{1-m^2}\cos(jq),\,\sqrt{1-m^2}\sin(jq),\,m),
 \quad \mathbf h_++\mathbf h_-=-s\mathbf e_z.
\]
Any \(s\in[0,2]\) is realized by two unit vectors whose sum equals \(-s\mathbf e_z\). The opposite winding replaces \(q\) by \(-q\).

Define the local, oriented observable
\[
 \Xi_j=(\mathbf h_++\mathbf h_-)\cdot(\mathbf s_j\times\mathbf s_{j+1}).
\]
For every intermediate-regime ground state, \(\Xi_j\) is independent of \(j\) and the two possible values are
\[
 \Xi_j=\pm 2\bigl(1-K^2/a^2\bigr)\sin(\pi/n).
\]
It vanishes on both open extreme regimes; at the coexistence point it varies with the ground state rather than taking a unique value. The two signs are interchanged by spatial reflection, not by proper global rotations.

## Proof

**1. Sharp ring energy at prescribed magnetization.** Define \(c=\min_{1\le k<n}\cos(2\pi k/n)=-\cos(\pi/n)\). The discrete Fourier basis diagonalizes the cyclic quadratic form \(\sum_j\mathbf s_j\cdot\mathbf s_{j+1}\); its zero-mode eigenvalue is \(1\) and each nonzero Fourier-mode eigenvalue is at least \(c\). Parseval and the unit-length condition give
\[
 \sum_j\mathbf s_j\cdot\mathbf s_{j+1}\ge
 c\sum_j|\mathbf s_j|^2+(1-c)\frac{|\mathbf M|^2}{n}
 =nc+n(1-c)m^2.
\]
For every \(0\le m\le1\), equality is attained by the cone displayed above, whose winding belongs to the two lowest nonzero Fourier modes. Consequently the bound is the exact minimum over all three-dimensional rim configurations having prescribed \(m\).

For completeness, the cone also describes every equality case when \(0\le m<1\), up to global orthogonal transformations and reversing winding. Equality confines the Fourier support to the constant mode and the modes \(k=(n\pm1)/2\). Thus \(\mathbf s_j=\mathbf u+\mathbf A\cos(jq)+\mathbf B\sin(jq)\), where \(|\mathbf u|=m\). Since \(n\ge5\) is odd, the Fourier harmonics \(0,\pm q,\pm2q\) are distinct modulo \(2\pi\). Requiring \(|\mathbf s_j|^2=1\) at all sites forces \(\mathbf u\perp\mathbf A,\mathbf B\), \(\mathbf A\perp\mathbf B\), and \(|\mathbf A|=|\mathbf B|=\sqrt{1-m^2}\). The case \(m=1\) is uniform.

**2. Exact apex reduction.** Every pair of unit apex spins with resultant length \(s\in[0,2]\) has pair correlation \(\mathbf h_+\cdot\mathbf h_-=s^2/2-1\), and all \(s\) in this interval are realizable. For fixed \(m,s\), the spoke interaction is bounded below by \(-nKms\), with equality whenever the apex resultant points antiparallel to \(\mathbf M\). Combining this observation with Step 1 gives the exact, jointly attainable reduction
\[
 \min H=\min_{0\le m\le1,\,0\le s\le2}
 \left\{nJc+nam^2-nKms+L\left(\frac{s^2}{2}-1\right)\right\}.
\]
This is not merely a variational ansatz: each point of the displayed rectangle can be realized by an exact rim cone and an apex pair.

**3. Full constrained minimization and boundaries.** For \(K\le a\), the minimizing \(m\), at fixed \(s\), is \(m=Ks/(2a)\le1\). Substitution gives
\[
 nJc-L+\left(\frac L2-\frac{nK^2}{4a}\right)s^2.
\]
The coefficient is positive for \(K<K_{\mathrm c}\), zero at \(K=K_{\mathrm c}\), and negative for \(K_{\mathrm c}<K\le a\). This proves the first two branches and the entire coexistence interval. Since \(2L<na\), the critical value lies strictly below \(a\).

For \(K>a\), the optimal \(m\) at fixed \(s\) is \(\min\{Ks/(2a),1\}\). For \(0\le s\le 2a/K\), the optimized energy decreases strictly in \(s\), since the quadratic coefficient is then negative. For \(2a/K\le s\le2\), it has derivative \(Ls-nK<0\), using \(2L<na<nK\). Hence the unique optimum has \(s=2\), \(m=1\), proving the third branch and the boundary \(K=a\). The three branches join continuously as energies. Their one-sided derivatives at \(K_{\mathrm c}\) are \(0\) and \(-2nK_{\mathrm c}/a\), which differ, so the transition is first order. Every asserted order parameter and its exclusivity follows from the strict cases of the scalar minimization.

**4. Chirality and handedness.** In a cone of magnetization \(m\), the component of \(\mathbf s_j\times\mathbf s_{j+1}\) along the cone axis equals \(\pm(1-m^2)\sin(\pi/n)\). At the intermediate-regime optimum, the apex resultant has length \(2\) and points along the opposite cone axis. This yields \(\Xi_j=\pm2(1-K^2/a^2)\sin(\pi/n)\). The magnitude is strictly positive for \(K_{\mathrm c}<K<a\). Both windings attain the same energy, proving the paired chiral degeneracy.

## Verification

The accompanying stand-alone `check_two_hub.py` implements the original spin Hamiltonian rather than only the reduced scalar formula. It independently checks constructed conical witnesses, 3,360 random-spin global lower-bound tests (plus other checks), constrained two-parameter optimization, a continuum of critical coexistence witnesses, exact apex-pair correlations, chiral plaquette values, and five full-coordinate nonlinear spin optimizations. On the supplied numerical test environment it passed 3,901 assertions, with maximum absolute witness-energy discrepancy \(1.43\times10^{-14}\). Run `python check_two_hub.py` with NumPy and SciPy installed. These finite checks are corroboration of, not substitutes for, the all-\(n\) proof above.

As an example, for \(n=5\), \(J=L=1\) one has \(a=1+\cos(\pi/5)\) and \(K_{\mathrm c}\simeq0.85065080835\). The rim magnetization jumps from zero to approximately \(0.47022820183\), and the chirality magnitude immediately above the transition approaches approximately \(0.91563474760\).

## Relationship to prior work

The exact fixed-magnetization parabola for an isolated odd spin ring is **already published** as Eq. (79) of Schmidt and Luban (2002), after accounting for their convention of counting bonds twice; their Sec. 6.3.3 also solves a one-apex pentagonal star. Neither ingredient is claimed as new. Sklan and Henley (2012) characterize conical spin states on an octahedral lattice and discuss Fourier/Luttinger–Tisza bounds. Jeevanesan and Orth (2014) give rich planar and nonplanar phases for the coupled triangular–honeycomb windmill lattice. Grajek and collaborators (2018) explicitly discuss odd uncentered rings and **one-apex centered rings with an even number of rim spins**, not the bonded two-apex odd ring here. Florek and collaborators (2020) analyze a single-center classical wheel using the Lagrange variety; their Hamiltonian (10) has one apex, not an apex pair with an independent antiferromagnetic apex bond.

The present classification concerns the additional apex–apex frustration and the exact discontinuous alignment transition in a finite odd-rim two-apex graph. A pre-existing general theory of symmetric spin matrices could offer another derivation; its existence would not alone establish that this specific phase diagram is unreported. Historical-priority verification is therefore qualified to the primary material actually examined, not an assertion of universal uniqueness.

## Limitations

The exact result assumes homogeneous isotropic bilinear exchange, a bonded equivalent pair of unit apex spins, positive couplings, and odd rim size at least five, with \(2L<na\). The phase diagram outside that strict parameter domain, thermal or quantum fluctuations, anisotropic axes, heterogeneous spokes/rim bonds, and dynamical stability are not determined here. The result does not imply that the material experiment realizes these couplings. Independent scientific audit has not been performed.

## References

1. H.-J. Schmidt and M. Luban, *Classical ground states of symmetric Heisenberg spin systems* (2002 preprint; 2003 journal), https://arxiv.org/abs/cond-mat/0209157 ; https://doi.org/10.1088/0305-4470/36/23/306 . Earliest public preprint: 2002-09-06 UTC. Exact ring fixed-magnetization energy is their Eq. (79), and a one-apex odd pentagonal star occurs in Sec. 6.3.3.
2. S. R. Sklan and C. L. Henley, *Nonplanar ground states of frustrated antiferromagnets on an octahedral lattice* (2012 preprint; published 2013), https://arxiv.org/abs/1209.1381 . Earliest public preprint: 2012-09-06 UTC.
3. B. Jeevanesan and P. P. Orth, *Classical ground states of Heisenberg and XY antiferromagnets on the windmill lattice* (2014), https://arxiv.org/abs/1409.1618 ; https://doi.org/10.1103/PhysRevB.90.144435 .
4. M. Grajek, T. Kopyciuk, W. Florek, A. Marlewski, *Collinear and Non-Collinear Configurations in Classical Geometrically Frustrated Ring-Shaped Systems* (2018), https://pdfs.semanticscholar.org/3f22/35011bc1727442e3d0ced9d7401299924e6a.pdf .
5. W. Florek, A. Marlewski, G. Kamieniarz, M. Antkowiak, *The Lagrange variety approach applied to frustrated classical wheels* (2020), https://doi.org/10.17586/2220-8054-2020-11-1-30-35 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=nano&option_lang=eng&paperid=495&what=fullt .
