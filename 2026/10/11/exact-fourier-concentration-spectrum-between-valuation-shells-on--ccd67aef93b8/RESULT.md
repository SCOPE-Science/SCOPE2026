# Exact Fourier concentration spectrum between valuation shells on \(\mathbb Z/p^n\mathbb Z\)

## Finding

For every prime \(p\), integer \(n\ge2\), and indices \(0\le s,t<n\), the Fourier concentration operator between the spatial valuation shell \(X_s\) and frequency valuation shell \(F_t\) of \(G=\mathbb Z/p^n\mathbb Z\) has a completely explicit spectrum. Its only possible eigenvalues strictly between zero and one form a single simple eigenvalue. There is an exact transition at \(s+t=n-1\) between subspaces of perfectly simultaneously localized signals and a rank-one subcritical concentration regime.

Precisely, let \(M=(p-1)p^{n-t-1}=|F_t|\). For \(s+t\le n-2\), the spectrum, with multiplicities, is
\[
1\quad[(p-1)^2p^{n-s-t-2}],\qquad
0\quad[M-(p-1)^2p^{n-s-t-2}].
\]
For \(s+t=n-1\), it is
\[
1\quad[p-2],\qquad 1/p\quad[1],\qquad 0\quad[M-(p-1)].
\]
For \(s+t\ge n\), it is
\[
\beta=\frac{(p-1)^2}{p^{s+t-n+2}}\quad[1],\qquad0\quad[M-1].
\]
Multiplicity zero is omitted where appropriate. In particular, at the threshold \(s+t=n-1\), the prime \(p=2\) loses *all* perfect localization, whereas for \(p\ge3\), there are exactly \(p-2\) independent perfect localizers.

The sharp fraction of \(\ell^2\) energy that a nonzero \(F_t\)-bandlimited signal can place in \(X_s\) equals the largest displayed eigenvalue. The equality cases are exactly its top eigenspace, described explicitly in the proof.

## Assumptions and scope

Equip the cyclic group \(G=\mathbb Z/p^n\mathbb Z\) with counting measure and write \(N=p^n\). Define the nested subgroups \(H_j=p^jG\), with \(H_n=\{0\}\), and set \(X_s=H_s\setminus H_{s+1}\) and \(F_t=H_t\setminus H_{t+1}\). Identify the dual group with \(G\) by the orthonormal Fourier characters \(e_a(x)=N^{-1/2}\exp(2\pi i ax/N)\). Let \(P_t\) be the orthogonal projector onto \(\operatorname{span}\{e_a:a\in F_t\}\), and let \(M_s\) multiply by the indicator \(\mathbf1_{X_s}\).

The operator under study is \(B_{s,t}=P_tM_sP_t\) restricted to \(\operatorname{ran}P_t\). Its eigenvalues are nonnegative and at most one. The theorem addresses **these centered valuation shells**; shifted shells, arbitrary unions, other finite groups, and nonorthogonal masks are not asserted.

## Proof

For any \(a,b\in F_t\), subgroup character orthogonality gives the exact matrix entry
\[
\langle e_a,M_se_b\rangle
=p^{-s}\mathbf1_{p^{n-s}\mid(a-b)}
-p^{-s-1}\mathbf1_{p^{n-s-1}\mid(a-b)}.\tag{1}
\]
Indeed, \(N^{-1}\sum_{x\in H_j}\exp(2\pi i(b-a)x/N)=p^{-j}\mathbf1_{p^{n-j}\mid(a-b)}\). Equation (1) follows from \(\mathbf1_{X_s}=\mathbf1_{H_s}-\mathbf1_{H_{s+1}}\). This identity fixes every normalization.

**Case \(s+t\le n-2\).** For \(a\in F_t\), partition frequencies first by their residues modulo \(p^{n-s-1}\) (coarse classes), then within each coarse class by residues modulo \(p^{n-s}\) (fine classes). Since \(n-s\ge t+2\), there are exactly \((p-1)p^{n-s-t-2}\) coarse classes; each comprises \(p\) fine classes, each of cardinality \(p^s\). In one coarse class, the matrix is
\[
p^{-s}\operatorname{diag}(J_{p^s},\ldots,J_{p^s})-p^{-s-1}J_{p^{s+1}},\tag{2}
\]
where \(J_k\) is the all-ones matrix of order \(k\). It vanishes on vectors of zero sum within every fine class; on normalized class indicators it is \(I_p-p^{-1}J_p\). Consequently each coarse class has eigenvalue one with multiplicity \(p-1\), and all remaining eigenvalues vanish. Summing over coarse classes proves the first formula. The entire energy-maximizing eigenspace consists of frequency coefficient vectors constant in each fine class and having zero sum across the \(p\) fine-class values within each coarse class; independent coarse blocks may be combined freely.

**Case \(s+t=n-1\).** Now there is one coarse class modulo \(p^{n-s-1}=p^t\); the units in \(F_t\) split into \(p-1\) fine classes modulo \(p^{t+1}\), each of cardinality \(p^s\). On the fine-class normalized indicators, (1) is \(I_{p-1}-p^{-1}J_{p-1}\). It has eigenvalue one on the \((p-2)\)-dimensional zero-sum subspace and eigenvalue \(1/p\) on the uniform direction. All within-class zero-sum vectors have eigenvalue zero. This proves the middle line and characterizes equality: if \(p\ge3\), all top eigenvectors have constants on the fine classes with sum zero; if \(p=2\), the top eigenspace is the single all-ones fine-class direction and its eigenvalue is \(1/2\).

**Case \(s+t\ge n\).** Each pair of elements of \(F_t\) has difference divisible by \(p^t\), hence by both \(p^{n-s}\) and \(p^{n-s-1}\). Equation (1) is the rank-one matrix \((p-1)p^{-s-1}J_M\). Its sole positive eigenvalue is
\[
(p-1)p^{-s-1}(p-1)p^{n-t-1}=(p-1)^2/p^{s+t-n+2},
\]
and its eigenspace consists precisely of constant frequency coefficient vectors. This proves the third line, including its range \(0<\beta<1\).

Finally, for \(f\in\operatorname{ran}P_t\), the Rayleigh quotient \(\|\mathbf1_{X_s}f\|_2^2/\|f\|_2^2\) equals \(\langle f,B_{s,t}f\rangle/\|f\|_2^2\). The spectral theorem gives the sharp concentration fraction and equality cases above. Each assertion holds for every prime, scale, and shell index within the stated quantifiers.

## Verification

The companion `verify_shell_spectrum.py` uses exact fractions to assemble (1) over \(p\in\{2,3,5\}\), \(2\le n\le4\), and \(p\in\{2,3\}\), \(n=5\). It independently checks dimension, trace, squared trace, and the proposed annihilating polynomial for matrix orders at most \(36\). It also compares against directly computed unitary DFT restrictions for finite test cases. Run `python3 verify_shell_spectrum.py` with Python 3, NumPy, and SymPy. The actual successful run reports:

`VERIFY_OK exact_case_count=137 exact_matrix_dimensions_sum=4782 dft_cases=96 polynomial_identity_for_m_le_36=PASS trace_trace2=PASS`

These calculations test, but do not replace, the universal symbolic block argument in the proof.

## Relationship to prior work

Finite Fourier time-frequency concentration is a special case of abelian-group time-limited Toeplitz theory (Zhu--Wakin), and ultrametric Fourier/wavelet geometry appears in Kozyrev's \(p\)-adic spectral analysis. The former establishes general spectral frameworks and asymptotic distribution principles; the latter constructs localized \(p\)-adic wavelet eigenbases for a different operator. Nonasymptotic eigenvalue estimates for general Fourier concentration domains (Marceca--Romero--Speckbacher) give bounds rather than the exact prime-power valuation-shell multiplicities derived here. The subgroup character identity is classical and is not itself claimed as new.

The specific new synthesis being assessed is the **all-parameter exact spectrum and equality-space classification for two centered valuation shells**, with its one-dimensional intermediate spectral transition. Known general bounds or wavelet constructions do not directly assert that complete finite-dimensional statement, though equivalent older presentations remain possible.

## Limitations

The result does not claim a generalization to unions or translations of shells, noncyclic \(p\)-groups, or continuum \(\mathbb Q_p\) operators. It makes no inference from finite numerical tests to an infinite theorem: the algebraic proof covers every allowed parameter. Historical priority is not certified exhaustively; a previously unlocated presentation in finite ultrametric harmonic analysis may overlap.

## References

- S. Kozyrev, *Wavelet analysis as a p-adic spectral analysis*, arXiv:math-ph/0012019 (first publicly submitted 2000-12-09), https://arxiv.org/abs/math-ph/0012019.
- Z. Zhu and M. B. Wakin, *Time-Limited Toeplitz Operators on Abelian Groups: Applications in Information Theory and Subspace Approximation*, arXiv:1711.07956 (2017), https://arxiv.org/abs/1711.07956.
- F. Marceca, J. L. Romero, and M. Speckbacher, *Eigenvalue estimates for Fourier concentration operators on two domains*, arXiv:2301.11685 (2023), https://arxiv.org/abs/2301.11685; *Archive for Rational Mechanics and Analysis* 248, article 35 (2024), DOI:10.1007/s00205-024-01979-9.
