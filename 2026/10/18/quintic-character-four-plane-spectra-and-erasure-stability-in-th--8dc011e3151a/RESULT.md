# Quintic-character four-plane spectra and erasure stability in the eleven-plane harmonic fusion family

## Finding

The harmonic equi-isoclinic construction of Fickus–Iverson–Jasper–Mixon [1] yields two spectrally distinct classes of eleven two-dimensional complex subspaces in \(\mathbb C^{11}\), obtained from the nontrivial even multiplicative characters of \(\mathbb F_{11}\) of order five. This note gives the **complete four-plane Gram spectra** in both classes, including an exact arithmetic certificate for the worst four-plane restricted-isometry constants and their equality sets.

Fix the primitive element \(2\in\mathbb F_{11}^{\times}\), put \(\omega=e^{2\pi i/5}\), and let \(\chi_k(2^j)=\omega^{kj}\) for \(k\in\{1,2,3,4\}\). The choices \(k=1,4\) have a common four-plane Gram spectral profile, and so do \(k=2,3\), but the profiles and worst four-plane configurations differ between these two classes.

For each four-element set \(A\subset\mathbb F_{11}\), let \(G_A^{(k)}\) be the \(8\times8\) Gram matrix of orthonormal bases of the four associated two-planes. Write
\[
\delta_4^{(k)}=\max_{|A|=4}\|G_A^{(k)}-I_8\|_{\mathrm{op}}.
\]
Define \(t_{\pm}=(-1\pm\sqrt5)/2\). For a set representative \(A\), define a quartic
\[
Q_A^{(t)}(Y)=Y^4-120Y^3+(a+bt)Y^2+(c+dt)Y+(e+ft),
\]
where its six integer coefficients are given exactly by this table:

| Representative \(A\) | Number of affine translates/dilates | \(a\) | \(b\) | \(c\) | \(d\) | \(e\) | \(f\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \(\{0,1,2,3\}\) | 55 | 4530 | -90 | -58600 | 1800 | 133650 | 9225 |
| \(\{0,1,2,4\}\) | 110 | 4350 | -90 | -51760 | 180 | 83250 | 25425 |
| \(\{0,1,2,5\}\) | 110 | 4170 | 270 | -47350 | -7425 | 130050 | 29025 |
| \(\{0,1,3,4\}\) | 55 | 4530 | -270 | -65080 | 8640 | 271350 | -41175 |

The four rows represent **all** \(\binom{11}{4}=330\) unordered four-plane selections, with no repetition. If \(y_1,\ldots,y_4\) denote all four roots of the appropriate quartic with multiplicity, then \(y_j\ge0\), and the **entire Gram spectrum** is
\[
\operatorname{spec}G_A^{(k)}=\left\{1+\frac{\sqrt{y_j}}{10},\ 1-\frac{\sqrt{y_j}}{10}:1\le j\le4\right\},
\]
using \(t=t_-\) for \(k=1,4\) and \(t=t_+\) for \(k=2,3\).

For \(k=1,4\), let \(\rho_-\) be the largest root of \(Q_{\{0,1,2,5\}}^{(t_-)}\). For \(k=2,3\), let \(\rho_+\) be the largest root of \(Q_{\{0,1,3,4\}}^{(t_+)}\). Then the sharp constants are
\[
\boxed{\delta_4^{(1)}=\delta_4^{(4)}=\frac{\sqrt{\rho_-}}{10}=0.8807235348056\ldots,\qquad 77<\rho_-<78,}
\]
\[
\boxed{\delta_4^{(2)}=\delta_4^{(3)}=\frac{\sqrt{\rho_+}}{10}=0.8242260805290\ldots,\qquad 67.9<\rho_+<68.}
\]
Equality occurs for exactly the 110 affine images of \(\{0,1,2,5\}\) in the first character class, but for exactly the 55 affine images of \(\{0,1,3,4\}\) in the second. Every four-plane collection has independent basis vectors because \(\delta_4^{(k)}<1\). The sharp smallest four-plane Gram eigenvalues are approximately \(0.11927646519\) and \(0.17577391947\), respectively. The corresponding worst Gram-matrix spectral condition numbers are approximately \(15.76776719\) and \(10.37825228\), respectively.

## Assumptions and scope

All objects are over \(\mathbb C\). The finite field is exactly \(\mathbb F_{11}\); only the four nontrivial even characters above are considered. These are the **specific harmonic two-plane families** of [1], not arbitrary equi-isoclinic configurations. The character labels depend on the fixed primitive generator \(2\).

An explicit realization makes the normalization unambiguous. For each \(k\), put \(\psi_0=(1,0)^{\mathsf T}\) and
\[
\psi_t=\left(\frac3{\sqrt{20}},\sqrt{\frac{11}{20}}\,\overline{\chi_k(t)}\right)^{\mathsf T}\qquad(t\ne0).
\]
For every \(a\in\mathbb F_{11}\), let \(\Phi_a^{(k)}\) have row \(t\) equal to \(\sqrt{2/11}\,e^{2\pi iat/11}\psi_t^{\mathsf T}\). Its columns are orthonormal. Its range is the corresponding harmonic fusion plane. Fixed unitary changes of the two-column bases do not alter Gram spectra.

## Proof

**1. Gram-block reduction.** Since \(\chi_k(-1)=1\), the multiplicative Gauss sum
\[
\tau_k=\sum_{t\in\mathbb F_{11}^{\times}}\overline{\chi_k(t)}e^{2\pi it/11}
\]
has modulus \(\sqrt{11}\). The orthogonality of additive and multiplicative characters gives \((\Phi_a^{(k)})^*\Phi_a^{(k)}=I_2\). For \(a\ne b\), the cross-Gram diagonal entries are \(1/10\) and \(-1/10\), and the upper-right entry is \(\frac3{10}(\tau_k/\sqrt{11})\chi_k(b-a)\). The *same* diagonal unitary change of basis, \(\operatorname{diag}(1,\overline{\tau_k}/\sqrt{11})\), removes the constant phase from every cross block. Consequently, in this gauge,
\[
(G_A^{(k)})_{aa}=I_2,\quad
(G_A^{(k)})_{ab}=\frac1{10}
\begin{pmatrix}
1&3\chi_k(b-a)\\
3\overline{\chi_k(b-a)}&-1
\end{pmatrix}\quad(a\ne b).
\]
In particular, all pairwise subspace angles are identical in the two character classes: every off-diagonal block has both singular values \(1/\sqrt{10}\). Pairwise coherence therefore cannot distinguish the four-plane erasure behaviors.

**2. Affine orbit reduction.** Put \(B_A^{(k)}=10(G_A^{(k)}-I_8)\). Translation of the four indices preserves their differences. Multiplication of all indices by \(s\in\mathbb F_{11}^{\times}\) multiplies the upper-right character value by \(\chi_k(s)\), removable by a common diagonal unitary on every two-plane basis. Thus \(B_A^{(k)}\) has the same eigenvalues on the entire affine orbit \(sA+b\).

The affine group has order \(110\). Applying its \(110\) transformations to each of the four displayed representatives gives pairwise disjoint orbits of sizes \(55,110,110,55\). Since those sizes sum to \(330\), they exhaust the four-element subsets. The standalone checker verifies all 330 incidences exactly as a finite certificate.

**3. Even characteristic polynomial.** Every off-diagonal block of \(B_A^{(k)}\) is traceless Hermitian. Let \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\) and let \(T\) act on each two-dimensional block by \(v\mapsto J\overline v\). Any traceless Hermitian two-by-two matrix \(H\) satisfies \(J\overline HJ^{-1}=-H\). Therefore the antiunitary \(T\) anticommutes with \(B_A^{(k)}\). The real spectrum of \(B_A^{(k)}\) is consequently invariant under sign reversal. Its characteristic polynomial is a quartic in \(X^2\):
\[
\det(XI_8-B_A^{(k)})=Q_A^{(t)}(X^2).
\]
The four roots of \(Q_A^{(t)}\) are the squares of the nonnegative eigenvalues of \(B_A^{(k)}\), proving the spectral formula.

**4. Exact cyclotomic coefficients.** Use the integral basis \(1,\omega,\omega^2,\omega^3\) of \(\mathbb Z[\omega]\), reducing \(\omega^4=-1-\omega-\omega^2-\omega^3\). The powers \(2^j\pmod{11}\) determine the character table with \(\chi_k(2^j)=\omega^{kj}\). For each representative, take powers of the exact \(8\times8\) matrix \(B_A^{(1)}\) and apply Newton's identities
\[
c_0=1,\qquad c_m=-\frac1m\sum_{j=1}^m c_{m-j}\operatorname{tr}((B_A^{(1)})^j),\quad 1\le m\le8,
\]
where \(\det(XI_8-B_A^{(1)})=\sum_{m=0}^8c_mX^{8-m}\). Every arithmetic operation takes place in the exact integral cyclotomic ring, with integral Newton quotients verified. The four resulting coefficient tuples are precisely those in the table. Replacing \(\omega\) by \(\omega^k\) applies the corresponding Galois automorphism to the coefficient tuples. Their only nonrational generator is \(\omega^2+\omega^3=t_-\), which maps to \(t_+\) for \(k=2,3\) and stays \(t_-\) for \(k=1,4\).

**5. Exact ordering of extremal roots.** There is no appeal to rounded roots. For each orbit polynomial and each choice \(t=t_\pm\), the following rational intervals \((L,U)\) satisfy \(Q_A^{(t)}(L)<0\), and **every coefficient** of the shifted polynomial \(Q_A^{(t)}(U+Z)\) is strictly positive. Entries are ordered as the four table rows:
\[
\begin{aligned}
t=t_-:&\quad (51,52),\ (56,57),\ (77,78),\ (27,43),\\
t=t_+:&\quad (62,63),\ (67.2,67.3),\ (65,66),\ (67.9,68).
\end{aligned}
\]
A negative value at \(L\) and monicity establish a real root above \(L\); coefficient positivity excludes every real root at or above \(U\). Hence the greatest real root is strictly between \(L\) and \(U\). The sign tests are **exact**, since each evaluated expression lies in \(\mathbb Q(\sqrt5)\) and its sign is obtained from rational comparisons of squares. In the first character class \(77\) exceeds the three other upper bounds \(52,57,43\). In the second, \(67.9\) exceeds the other upper bounds \(63,67.3,66\). Therefore the two stated winning affine orbits, with multiplicities 110 and 55, are unique. Their upper root bounds are below 100, so every Gram eigenvalue is positive. The sharp constants and eigenvalue/condition-number claims follow.

## Verification

Run `python3 checker.py` with only the Python 3 standard library. It performs a direct harmonic-frame Gram diagnostic across 242 blocks, complete affine enumeration of 330 quartets, exact cyclotomic traces/Newton coefficients for all four orbit representatives, and all eight rational root-separation certificates. The final output ends with `CHECK_PASS 330 quartets, four affine orbits, eight exact quartic profiles and root-separation certificates`; the included `checker_output.txt` records the run. The direct complex Gram diagnostic uses roundoff tolerance, but the crucial finite enumeration, characteristic polynomials, and root inequalities are checked using **integer and rational arithmetic only**. The source construction and elementary Gauss-sum/antiunitary arguments are proved independently of floating-point tests.

## Relationship to prior work

The eleven harmonic complex fusion planes and their Gauss-sum block construction are due to [1]; they are **not** newly constructed here. The conference-matrix paper [2] develops related equi-isoclinic constructions and equivalences but does not supply the explicit two-class four-plane spectra above. The block restricted-isometry viewpoint appears in [3], which primarily constructs totally symmetric families and explicitly leaves its block-isometry analysis for future work. General fusion-frame erasure studies such as [4] do not give the cyclotomic quartics or the switch of the worst four-plane orbit between the two inequivalent quintic-character choices.

A closely related prior result [5] computes all three-plane spectra for real quadratic-character harmonic fusion planes and classifies four-plane Gram spectra in the **real \(q=13\) quadratic-character case**. This is a different field, character, and complex family; its q13 spectra do not imply the present q11 quintic spectra. The new claim here is solely the complete q11 two-class four-plane profile, its exact sharp stability constants, and optimizer classifications.

## Limitations

The result is a complete exact finite calculation at field order eleven, **not** a classification for all prime powers or all fusion frames. The Gram-matrix spectral condition number is not a noise-model-independent reconstruction guarantee. The provenance of the underlying frame construction is [1]. Numerical approximations only illustrate algebraically certified values. The finite certificate is supplied as code and its output. Bibliographic searches and primary-text comparisons do not exclude a differently formulated older conference-matrix or finite-group result.

## References

[1] M. Fickus, J. W. Iverson, J. Jasper, D. G. Mixon, *Harmonic Grassmannian codes*, arXiv:2112.14267v1, 28 December 2021, Theorem 4.2 and equations (39)–(42). https://arxiv.org/abs/2112.14267

[2] M. Fickus, J. W. Iverson, J. Jasper, D. G. Mixon, *Equi-isoclinic subspaces, covers of the complete graph, and complex conference matrices*, arXiv:2212.12617v1, 23 December 2022. https://arxiv.org/abs/2212.12617

[3] M. Fickus, J. W. Iverson, J. Jasper, D. G. Mixon, *Totally symmetric Grassmannian codes*, arXiv:2406.19542v1, 27 June 2024 (also inspected later open version for block-isometry discussion). https://arxiv.org/abs/2406.19542

[4] B. G. Bodmann, J. Cahill, P. G. Casazza, *Fusion frames and the restricted isometry property*, Numer. Funct. Anal. Optim. **33** (2012), 770–790. https://doi.org/10.1080/01630563.2012.682135

[5] *Three-block rigidity and the four-block spectral profile of real Paley harmonic fusion planes*, published-finding corpus published mathematical result, 11 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-block-rigidity-and-the-four-block-spectral-profile-of-real--e1ffd8f9e8e9
