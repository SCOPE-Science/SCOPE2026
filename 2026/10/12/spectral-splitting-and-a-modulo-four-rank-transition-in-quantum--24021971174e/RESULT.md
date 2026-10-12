# Spectral splitting and a modulo-four rank transition in quantum mixing on sunlet graphs

## Finding

For an integer \(n\geq 3\), let \(L_n=C_n\circ K_1\) be the **sunlet graph**: a simple \(n\)-cycle with one private pendant leaf attached to each cycle vertex. The adjacency matrix, with cycle vertices first and leaves second, is
\[
H_n=\begin{pmatrix}A(C_n)&I_n\\I_n&0\end{pmatrix}.
\]
For a real symmetric matrix \(B\), set \(\widehat M(B)=\lim_{T\to\infty}T^{-1}\int_0^T e^{itB}\circ e^{-itB}\,dt\), where \(\circ\) is the entrywise product. Then the exact rank for every \(n\geq3\) is
\[
\boxed{\operatorname{rank}\widehat M(H_n)=
\begin{cases}
2n,&n\text{ odd},\\
n,&n\equiv2\pmod4,\\
n-1,&n\equiv0\pmod4.
\end{cases}}
\]
Thus odd sunlets have strictly positive-definite average mixing, whereas even sunlets lose at least half their spectral modes, with **one additional null direction precisely at multiples of four**. For example, the sixteen-vertex sunlet \(L_8\) has rank \(7\).

The proof also gives the entire Fourier-indexed spectrum: define \(\lambda_j=2\cos(2\pi j/n)\) and \(w_j=\lambda_j^2/(\lambda_j^2+4)\). The spectrum of \(\widehat M(H_n)\), counting multiplicities, is the union of the spectra of the two \(n\times n\) matrices \(R_n\) and \(S_n\) defined below. If \(n\) is odd, the eigenvalues of \(R_n\) are \(1\) once and \(1/n\) repeated \(n-1\) times; the indexed eigenvalues of \(S_n\), on Fourier frequency \(k\), are
\[
\sigma_0=\frac{w_0+2\sum_{j=1}^{(n-1)/2}w_j}{n},\qquad
\sigma_{2j}=\sigma_{-2j}=\frac{w_j}{n}
\quad (1\le j\le(n-1)/2).
\]
Subscripts are interpreted modulo \(n\), so this specifies each Fourier frequency exactly once. If \(n=2m\) is even, the eigenvalues of \(R_n\) are \(1\) once, \(2/n\) repeated \(m-1\) times, and \(0\) repeated \(m\) times. The indexed eigenvalues of \(S_n\) are
\[
\sigma_0=\frac{w_0+w_m+2\sum_{j=1}^{m-1}w_j}{n},\qquad
\sigma_{2j}=\frac{2w_j}{n}\ (1\le j<m),\qquad
\sigma_k=0\ (k\text{ odd}).
\]
The complete spectrum is understood as a multiset: repeated numerical values are combined with their Fourier multiplicities.

## Assumptions and scope

The graph is finite, undirected, unweighted, and loopless. The evolution uses the ordinary adjacency Hamiltonian and the conventional uniform-in-time Cesàro average, not Laplacian evolution or an optimized observation-time distribution. The cycle has \(n\ge3\) vertices, and each cycle vertex has exactly one private leaf. The ambient field is \(\mathbb C\), but all average mixing matrices are real symmetric positive semidefinite. No genericity or simple-spectrum assumption is imposed.

## Proof

**1. A corona spectral-splitting lemma.** More generally let \(A\) be any real symmetric \(n\times n\) matrix, with distinct spectral values \(\lambda\) and orthogonal projectors \(E_\lambda\). Put \(H=\left(\begin{smallmatrix}A&I\\I&0\end{smallmatrix}\right)\). On the \(\lambda\)-eigenspace of \(A\), the two-dimensional fibre matrix is \(B_\lambda=\left(\begin{smallmatrix}\lambda&1\\1&0\end{smallmatrix}\right)\); its two distinct eigenvalues are \(\rho_{\lambda,\pm}=(\lambda\pm\sqrt{\lambda^2+4})/2\). For each fixed sign, \(\lambda\mapsto\rho_{\lambda,\pm}\) is strictly increasing. The positive and negative branches never intersect, so the distinct spectral projectors of \(H\) are exactly \(E_\lambda\otimes Q_{\lambda,+}\) and \(E_\lambda\otimes Q_{\lambda,-}\), where \(Q_{\lambda,\pm}\) project onto the two eigenvectors of \(B_\lambda\).

Let \(P_\pm=\frac12\left(\begin{smallmatrix}1&\pm1\\\pm1&1\end{smallmatrix}\right)\). Direct calculation using \(\Delta_\lambda=\sqrt{\lambda^2+4}\) and \(Q_{\lambda,+}=\frac12\left(\begin{smallmatrix}1+\lambda/\Delta_\lambda&2/\Delta_\lambda\\2/\Delta_\lambda&1-\lambda/\Delta_\lambda\end{smallmatrix}\right)\), with \(Q_{\lambda,-}=I-Q_{\lambda,+}\), gives the **Schur-square identity**
\[
Q_{\lambda,+}\circ Q_{\lambda,+}+Q_{\lambda,-}\circ Q_{\lambda,-}
=P_++\frac{\lambda^2}{\lambda^2+4}P_-.
\]
For every real symmetric Hamiltonian, \(\widehat M(B)=\sum_E E\circ E\), the sum ranging over its distinct orthogonal spectral projectors. Thus, with
\[
R=\sum_\lambda E_\lambda\circ E_\lambda=\widehat M(A),\qquad
S=\sum_\lambda\frac{\lambda^2}{\lambda^2+4}(E_\lambda\circ E_\lambda),
\]
we have the exact identity
\[
\boxed{\widehat M(H)=R\otimes P_++S\otimes P_-.}
\]
The tensor notation uses the interleaved order (base vertex, attached leaf); in the base-first order of the statement it is the block matrix \(\frac12\left(\begin{smallmatrix}R+S&R-S\\R-S&R+S\end{smallmatrix}\right)\). Since the two fibre projectors are orthogonal, \(\operatorname{rank}\widehat M(H)=\operatorname{rank}R+\operatorname{rank}S\). This identity holds even when \(A\) has repeated or zero eigenvalues.

**2. Fourier projectors for cycles.** Identify the cycle vertices with \(\mathbb Z/n\mathbb Z\), set \(\omega=e^{2\pi i/n}\), and put \((F_j)_{uv}=n^{-1}\omega^{j(u-v)}\). These are mutually orthogonal rank-one Fourier projectors, and \(F_j\circ F_k=n^{-1}F_{j+k}\). The real adjacency eigenvalue at frequency \(j\) is \(\lambda_j=2\cos(2\pi j/n)\). The **distinct** real spectral projectors of \(A(C_n)\) are \(F_0\), the pairs \(F_j+F_{-j}\) for \(1\le j<n/2\), and, when \(n\) is even, \(F_{n/2}\). These have Schur squares \(n^{-1}F_0\) for each singleton and \(n^{-1}(F_{2j}+F_{-2j}+2F_0)\) for each pair.

Consequently \(R_n\) and \(S_n\) are diagonal in the Fourier basis. Summing the above Schur squares unweighted or weighted by \(w_j\), respectively, gives exactly the indexed eigenvalues stated under Finding. In particular the known cycle formula is recovered: for odd \(n\), \(R_n=n^{-1}I+(n-1)n^{-2}J\); for even \(n=2m\), \(R_n=n^{-1}(I+T^m)+(n-2)n^{-2}J\), where \(T\) is the one-step cyclic permutation matrix.

**3. Exact positivity and the isolated zero mode.** Since \(w_j\ge0\), every nonzero Fourier coefficient listed for \(S_n\) is positive unless \(\lambda_j=0\). For odd \(n\), no \(\lambda_j\) is zero: \(\cos(2\pi j/n)=0\) would require \(4\mid n\). Thus \(R_n\) and \(S_n\) are both positive definite and the sunlet rank is \(2n\).

For even \(n=2m\), the unweighted matrix \(R_n\) is positive on exactly the \(m\) even Fourier frequencies, hence has rank \(m\). The weighted matrix \(S_n\) vanishes on all \(m\) odd frequencies. Its zero-frequency coefficient is positive because \(w_0=1/2\); at a nonzero even frequency \(2j\) the coefficient is \(2w_j/n\). The equation \(w_j=0\) has a solution with \(1\le j<m\) **if and only if** \(4\mid n\), and then uniquely at \(j=n/4\), corresponding to Fourier frequency \(n/2\). Hence \(\operatorname{rank}S_n=m\) when \(n\equiv2\pmod4\) and \(m-1\) when \(4\mid n\). Adding the two sector ranks proves the claimed formula for every \(n\ge3\).

## Verification

Run `python verify.py` with Python 3 and NumPy. The executable checks exact rational Fourier coefficient identities for cycle orders \(4,6,8,12\) and independently computes the full \(2n\times2n\) sunlet spectral-projector average-mixing matrices for every integer \(3\le n\le24\). The recorded replay result is:

`VERIFY_OK exact_cycle_orders=4,6,8,12 independent_matrix_orders=3..24 fourier_modes=30 max_matrix_error=9.645e-16 mod4_boundary_8=7/16`

The rational frequency checks use exact squared cycle eigenvalues and rational arithmetic; the matrix calculations use floating-point diagonalization and check the independent block decomposition and ranks. The unrestricted theorem follows from the exact symbolic proof above, not from finite tests.

## Relationship to prior work

Godsil, *Average mixing of continuous quantum walks* (arXiv:1103.2578), derives the cycle average mixing matrix \(R_n\) in Lemma 6.1. Ackelsberg and coauthors, *Quantum State Transfer in Coronas* (arXiv:1605.05260), obtain spectral eigenprojectors for graph coronas (Proposition 3.2) in a study of state transfer, not of Cesàro mixing rank. The projector-sum approach to average mixing is developed in Godsil (2011), Coutinho–Godsil–Guo–Zhan (2017), and Coutinho and coauthors (2022). The contribution here is the combined **two-sector average-mixing identity, full Fourier-indexed sunlet spectrum and sharp modulo-four rank transition**, including the extra defect caused by an adjacency zero mode. None of these cited results is represented as independently proving this particular rank classification.

## Limitations

The theorem addresses exactly one pendant leaf per cycle vertex, with uniform unweighted coupling. It does not claim a graph-independent full-rank result for arbitrary coronas, nor does it address variable pendant couplings, partial leaf decorations, or other quantum-walk Hamiltonians. The source literature contains general spectral tools that may permit the result to be recovered through another unlocated formulation; the literature comparison is not an independent originality certification. The finite numerical checks do not establish the infinite statement.

## References

1. G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier, R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first public 2022-08-18); DOI:10.1137/22M1521262. Primary MSC2020 81P68.
2. C. Godsil, *Average mixing of continuous quantum walks*, arXiv:1103.2578, especially Lemma 6.1 and the cycle Fourier decomposition.
3. E. Ackelsberg, Z. Brehm, A. Chan, J. Mundinger, C. Tamon, *Quantum State Transfer in Coronas*, arXiv:1605.05260, especially Proposition 3.2.
4. G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591.
5. C. Godsil, K. Guo, J. Sinkovic, *Average mixing matrix of trees*, arXiv:1709.07907.
