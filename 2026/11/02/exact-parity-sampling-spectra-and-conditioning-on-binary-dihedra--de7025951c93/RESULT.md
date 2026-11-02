# Exact parity sampling spectra and conditioning on binary-dihedral spherical configurations

## Finding

For every integer \(m\ge2\), let \(N=2m\) and put
\[
X_m=\left\{(\cos(\pi j/m),\sin(\pi j/m),0,0),\ (0,0,\cos(\pi j/m),\sin(\pi j/m)):0\le j<N\right\}\subset S^3.
\]
The \(4m\) points form the binary-dihedral (dicyclic) subgroup of unit quaternions and consist of two mutually orthogonal regular \(N\)-gons on great circles. For every integer \(\ell\ge0\), form the \(4m\)-by-\(4m\) Gram matrix
\[
K_\ell(x,y)=U_\ell(\langle x,y\rangle),
\qquad U_\ell(\cos\theta)=\sum_{r=0}^{\ell}e^{i(\ell-2r)\theta},
\]
with \(U_\ell\) the Chebyshev polynomial of the second kind. Define the residue counts, for \(0\le j<N\), by
\[
c_j=c_j(m,\ell)=\#\{r\in\{0,\ldots,\ell\}:\ell-2r\equiv j\pmod N\}.
\]
Writing \(v^{[h]}\) for an eigenvalue \(v\) of multiplicity \(h\), **the complete spectra, including all zeros**, are
\[
\operatorname{spec}(K_\ell)=
\begin{cases}
\displaystyle\bigsqcup_{j=0}^{N-1}\{(Nc_j)^{[2]}\},&\ell\ \text{odd},\\[5pt]
\displaystyle\{N(c_0+1),N(c_0-1)\}\sqcup\bigsqcup_{j=1}^{N-1}\{(Nc_j)^{[2]}\},&\ell\ \text{even}.
\end{cases}
\]
In even degree, \(c_0=2\lfloor\ell/N\rfloor+1\). The rank of the evaluation map from exact-degree spherical harmonics is
\[
\operatorname{rank}K_\ell=
\begin{cases}
2\min(\ell+1,m),&\ell\ \text{odd},\\
2\min(\ell+1,m)-1,&\ell<N\ \text{even},\\
2m,&\ell\ge N\ \text{even}.
\end{cases}
\]
Thus evaluation surjects onto all values compatible with antipodal parity \(f(-x)=(-1)^\ell f(x)\) precisely when \(\ell+1\ge m\) in odd degree, or \(\ell\ge2m\) in even degree.

Let \(\kappa_\ell^2\) denote the largest positive Gram eigenvalue divided by the smallest positive one (equivalently, the squared condition number of evaluation after discarding its kernel). Then the **sharp all-degree formula** is
\[
\kappa_\ell^2=
\begin{cases}
1,&\ell\ \text{odd},\quad \ell+1\le m\ \text{or}\ m\mid(\ell+1),\\
(q+1)/q,&\ell\ \text{odd},\quad \ell+1>m,\ m\nmid(\ell+1),\quad q=\lfloor(\ell+1)/m\rfloor,\\
1,&\ell\in\{0,2m-2\},\\
2,&0<\ell<2m-2,\quad\ell\ \text{even},\\
(s+1)/s,&\ell\ge2m,\quad\ell\ \text{even},\quad s=\lfloor\ell/(2m)\rfloor.
\end{cases}
\]
In particular the even degrees exhibit one isolated nonconstant tight degree, \(\ell=2m-2\), followed immediately by a loss of tightness at \(\ell=2m\). For odd degrees, the infinite exact-tightness progression is \(m\mid(\ell+1)\), subject to odd parity. Finally, if \(J\) is the permutation matrix \(J_{x,y}=\mathbf1_{\{y=-x\}}\), then the exact matrix translation identity is
\[
\boxed{K_{\ell+4m}=K_\ell+4m\bigl(I+(-1)^\ell J\bigr)}.
\]

## Assumptions and scope

The integer \(m\) is at least two, and the harmonic degree \(\ell\) is any nonnegative integer. The normalized sphere measure is the probability Haar measure on \(S^3\). The degree-\(\ell\) harmonic space has dimension \((\ell+1)^2\), and its reproducing kernel is \((\ell+1)U_\ell(\langle x,y\rangle)\). Hence \(K_\ell\) is positive semidefinite and differs from the physical evaluation Gram matrix only by the positive scalar \(\ell+1\). All ranks and condition-number ratios are exactly those of harmonic restriction. The antipodal-compatible sample-value space has dimension \(2m\), not \(4m\); zeros forced by parity are always counted in the displayed complete spectrum.

## Proof

**Step 1: two-circle block structure.** Order the points with the first great-circle polygon before the second. Within either polygon, the inner product of vertices separated by \(h\) steps is \(\cos(2\pi h/N)\). The polygons lie in orthogonal coordinate planes, so their cross-circle inner products are all zero. Consequently
\[
K_\ell=\begin{pmatrix}C_\ell&\varepsilon_\ell\mathbf1\mathbf1^T\\\varepsilon_\ell\mathbf1\mathbf1^T&C_\ell\end{pmatrix},\quad
(C_\ell)_{a,b}=U_\ell\bigl(\cos(2\pi(a-b)/N)\bigr),\quad
\varepsilon_\ell=U_\ell(0).
\]
The recurrence \(U_0=1\), \(U_1(t)=2t\), \(U_{\ell+1}(t)=2tU_\ell(t)-U_{\ell-1}(t)\) gives \(\varepsilon_\ell=0\) when \(\ell\) is odd and \(\varepsilon_\ell=(-1)^{\ell/2}\) when \(\ell\) is even.

**Step 2: full Fourier diagonalization.** The character sum
\[
U_\ell(\cos\theta)=\sum_{r=0}^{\ell}e^{i(\ell-2r)\theta}
\]
shows that the \(N\)-point discrete Fourier transform of each circulant block has exact eigenvalues \(Nc_j\), with multiplicity one at each Fourier index \(j\). Every nonconstant Fourier mode annihilates \(\mathbf1\mathbf1^T\), hence occurs twice in \(K_\ell\). The constant Fourier index instead contributes the two-by-two matrix \(N\begin{psmallmatrix}c_0&\varepsilon_\ell\\\varepsilon_\ell&c_0\end{psmallmatrix}\). Its two eigenvalues are \(N(c_0\pm1)\) in even degree; in odd degree both are \(Nc_0\), necessarily zero because no even Fourier index occurs. This proves the displayed all-degree spectral decomposition without omitting the nullspaces.

**Step 3: parity counts and rank.** In odd degree all \(\ell+1\) character exponents \(\ell,\ell-2,\ldots,-\ell\) are odd. Modulo \(N=2m\), stepping by two visits the \(m\) odd residues cyclically, giving counts differing by at most one. Their nonzero count is \(\min(\ell+1,m)\), each contributing a double eigenvalue. This proves the odd-rank formula. In even degree, the same arithmetic visits only even residues and includes zero. The zero residue occurs \(2\lfloor\ell/N\rfloor+1\) times. When \(\ell<N\), it occurs once, and its two-dimensional constant block has rank one; the remaining \(\min(\ell+1,m)-1\) occupied nonzero residues contribute two dimensions each. When \(\ell\ge N\), the zero-residue count is at least three, both constant eigenvalues are positive, and every even residue is occupied, giving rank \(2m\). Rank equals evaluation range dimension because the Gram is the harmonic evaluation operator multiplied by its adjoint. Antipodal parity forces the image into the \(2m\)-dimensional parity-compatible space, proving the stated exact interpolation thresholds.

**Step 4: sharp conditioning.** For odd degree the positive residue counts equal either \(q\) or \(q+1\), where \(q=\lfloor(\ell+1)/m\rfloor\), unless \(\ell+1<m\), in which case every occupied residue has count one. The counts are equal on all occupied residues if and only if \(\ell+1\le m\) or \(m\mid(\ell+1)\). Otherwise their exact largest-to-smallest ratio is \((q+1)/q\).

For even \(0\le\ell<N\), the zero-index constant block has one positive eigenvalue \(2N\). At \(\ell=0\), this is the only positive eigenvalue. At \(\ell=N-2\), the \(\ell+1=N-1\) exponents visit zero once and every other even residue twice, so every positive eigenvalue equals \(2N\). At all other positive even degrees below \(N-2\), some occupied nonzero even residue has count one (and no count exceeds two), yielding both \(N\) and \(2N\) and ratio two. For even \(\ell\ge N\), put \(s=\lfloor\ell/N\rfloor\ge1\); the zero residue has count \(2s+1\), giving constant-sector eigenvalues \(2Ns\) and \(2N(s+1)\). Every other even-residue count is either \(2s\) or \(2s+2\), so all other positive eigenvalues lie between those constant-sector extremes. The exact ratio is \((s+1)/s\). These cases exhaust all degrees and prove each sharp equality classification.

**Step 5: spectral translation as a matrix identity.** Replace \(\ell\) with \(\ell+2N=\ell+4m\). In the character sum, the added \(2N\) exponents comprise exactly four complete tours of the \(m\) allowed parity residues. Thus every occupied-parity Fourier eigenvalue of the circulant block increases by \(4N=8m\), while the forbidden-parity modes remain zero. The cross-circle coefficient is unchanged because \(U_{\ell+4m}(0)=U_\ell(0)\). The circulant difference is therefore the matrix \(2N(I+(-1)^\ell J_N)\), where \(J_N\) exchanges antipodal vertices within each polygon: its Fourier eigenvalues are \(4N\) on the allowed parity and zero otherwise. Assembling both diagonal blocks, while the cross-circle blocks cancel, proves \(K_{\ell+4m}-K_\ell=2N(I+(-1)^\ell J)=4m(I+(-1)^\ell J)\). This completes the proof.

## Verification

The standalone standard-library script `artifacts/verify.py` tests the exact residue-count spectra, ranks, and sharp condition-number formulas for \(m=2,\ldots,48\) and \(\ell=0,\ldots,179\), totaling 8,460 cases. It separately constructs actual sample coordinates, Chebyshev Gram blocks, their Fourier eigenvalues, and matrix translation identities for selected \(m\) and \(\ell\). Invoke `python3 artifacts/verify.py` in the directory containing this result; the expected terminal markers are `EXACT_SPECTRAL_CHECKS_OK 8460` and `DIRECT_BLOCK_AND_SHIFT_CHECKS_OK 114`. The proof above, not finite testing, establishes the infinite-family assertions.

## Relationship to prior work

The spherical-harmonic basis, two Hopf-coordinate great circles, and binary-dihedral/prism-space group actions are classical. Lehoucq--Uzan--Weeks (2002), especially Sections 2 and 10, give explicit Laplace eigenmodes of prism quotients \(S^3/D_m^*\), not spectra of the **discrete evaluation map on all \(4m\) group points**. Rossmann (2003) studies the ADE character correspondence for finite subgroups of \(SU(2)\). Weeks (2005), Section 13, supplies a second explicit prism-space invariant-harmonic construction. These results justify the underlying object and representation setting; none of their inspected theorems states the two-circle sample Gram spectrum, the exact parity-compatible interpolation cutoffs, or the all-degree sharp conditioning/tightness and translation classifications. Unlike the invariant-mode problem on the quotient, sampling on the group configuration interrogates every finite-group representation sector, not only the invariant sector. The result makes no claim to rediscover the known quotient eigenmodes or the finite-cyclic DFT.

## Limitations

This concerns exact-degree scalar spherical harmonics on \(S^3\) and their restriction to precisely two orthogonal congruent regular polygons, not low-pass bands, general spherical designs, or arbitrary polyhedral groups. All tightness and condition numbers refer to the nonzero singular values and to the specified uniform weighting. The inherent antipodal kernel makes the full \(4m\)-point evaluation non-surjective in every degree. The proof uses standard finite Fourier diagonalization; the claim of originality is for the combined all-degree sharp classification, not the DFT identity. Closely related older sampling/representation results could express an equivalent classification under different terminology. Numerical tests do not establish historical novelty or independently validate the infinite proof.

## References

1. R. Lehoucq, J.-P. Uzan and J. Weeks, *Eigenmodes of Lens and Prism Spaces*, arXiv:math/0202072v1 (2002-02-08), especially Sections 2 and 10. https://arxiv.org/abs/math/0202072 .
2. W. Rossmann, *McKay's correspondence and characters of finite subgroups of SU(2)*, arXiv:math/0307121v1 (2003-07-09), especially Sections 1--3. https://arxiv.org/abs/math/0307121 .
3. J. R. Weeks, *Exact Polynomial Eigenmodes for Homogeneous Spherical 3-Manifolds*, arXiv:math/0502566v1 (2005-02-27), especially Section 13. https://arxiv.org/abs/math/0502566 .
