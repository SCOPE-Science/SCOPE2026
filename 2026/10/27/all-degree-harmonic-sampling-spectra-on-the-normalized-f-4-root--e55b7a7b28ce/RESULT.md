# All-degree harmonic sampling spectra on the normalized \(F_4\) root lines

## Finding

Let \(X\) be one oriented unit vector from each of the 24 antipodal lines in the normalized 48-root system of type \(F_4\), explicitly constructed below. On the sphere \(S^3\), let \(\mathcal H_\ell\) denote the real degree-\(\ell\) spherical harmonics, with the \(L^2\)-inner product for probability-normalized surface measure. Define \(T_\ell f=(f(x)/\sqrt{\ell+1})_{x\in X}\). Then its output Gram operator is

\[
H_\ell=T_\ell T_\ell^*=\bigl[U_\ell(\langle x,y\rangle)\bigr]_{x,y\in X},
\qquad U_\ell(\cos\theta)=\frac{\sin((\ell+1)\theta)}{\sin\theta}.
\]

For every \(\ell=24k+r\), with integers \(k\ge0\) and \(0\le r<24\), the multiset of eigenvalues of \(H_\ell\) is precisely the eigenvalues in the following row \(r\), each **increased by \(24k\)**. Each displayed pair \((v,m)\) means eigenvalue \(v\) with multiplicity \(m\). This is an exhaustive spectral classification for every nonnegative harmonic degree.

| Base degree \(r\) | Complete eigenvalue (multiplicity) pairs |
|---:|:---|
| 0 | \((0,23),(24,1)\) |
| 1 | \((0,20),(12,4)\) |
| 2 | \((0,15),(8,9)\) |
| 3 | \((0,8),(6,16)\) |
| 4 | \((0,11),(8,9),(12,4)\) |
| 5 | \((0,4),(6,16),(12,4)\) |
| 6 | \((0,5),(8,18),(24,1)\) |
| 7 | \((6,16),(12,8)\) |
| 8 | \((0,1),(8,18),(12,4),(24,1)\) |
| 9 | \((0,4),(12,20)\) |
| 10 | \((0,2),(8,9),(12,4),(16,9)\) |
| 11 | \((12,24)\) |
| 12 | \((8,9),(12,4),(16,9),(24,2)\) |
| 13 | \((12,20),(24,4)\) |
| 14 | \((0,1),(12,4),(16,18),(24,1)\) |
| 15 | \((12,8),(18,16)\) |
| 16 | \((0,1),(16,18),(24,5)\) |
| 17 | \((12,4),(18,16),(24,4)\) |
| 18 | \((12,4),(16,9),(24,11)\) |
| 19 | \((18,16),(24,8)\) |
| 20 | \((16,9),(24,15)\) |
| 21 | \((12,4),(24,20)\) |
| 22 | \((0,1),(24,23)\) |
| 23 | \((24,24)\) |

Consequently the exact sampling ranks for degrees \(0\) through \(23\) are

\[
(1,4,9,16,13,20,19,24,23,20,22,24,24,24,23,24,23,24,24,24,24,24,23,24).
\]

Every degree at least \(24\) has rank \(24\). The first full-rank degree is \(7\), but the ranks fall to \(23,20,22\) at consecutive degrees \(8,9,10\), recover to \(24\) at degree \(11\), and have later isolated deficiencies at degrees \(14,16,22\). The 24-line evaluation operator is a **tight surjective sampling operator** (equal positive eigenvalues with rank 24) exactly for degrees \(\ell\equiv11\) or \(23\pmod{24}\). Its first full-rank condition number occurs at degree \(7\) and equals \(\sqrt2\).

## Assumptions and scope

The long unit roots are \( (s e_i+t e_j)/\sqrt2\) for \(1\le i<j\le4\) and \(s,t\in\{-1,1\}\). The short unit roots are \(\pm e_i\) and \(\frac12(s_1,s_2,s_3,s_4)\), with independent signs \(s_i\in\{-1,1\}\). Each family has 24 vectors, for 48 altogether. Form \(X\) by selecting, from each antipodal pair, the vector whose first nonzero coordinate is positive, obtaining 12 long and 12 short representatives. A different orientation changes \(H_\ell\) by a diagonal sign conjugation when \(\ell\) is odd and has no effect when it is even. Eigenvalues and ranks therefore depend only on the 24 lines.

The statement concerns **single, exact homogeneous harmonic degrees**, not low-pass sums, root lattices of other types, or Gaussian quadrature in other dimensions. All eigenvalues refer to the specified probability-surface-measure and \(1/\sqrt{\ell+1}\) evaluation normalization.

## Proof

**Step 1: the spherical harmonic Gram.** The addition theorem on \(S^3\), whose degree-\(\ell\) harmonic dimension is \((\ell+1)^2\), states that for any orthonormal harmonic basis \(\{Y_j\}\),

\[
\sum_jY_j(x)Y_j(y)=(\ell+1)U_\ell(\langle x,y\rangle).
\]

Dividing the evaluation rows by \(\sqrt{\ell+1}\) gives the stated \(H_\ell\), which is real symmetric and positive semidefinite for all \(\ell\).

**Step 2: the exact angle set.** By direct dot products of the given root coordinates, two distinct nonantipodal lines have representative inner products in \(\{0,\pm\tfrac12,\pm1/\sqrt2\}\). The corresponding acute/nonacute angles are integer multiples of \(\pi/2,\pi/3,\pi/4\), respectively. For each off-diagonal entry, the trigonometric expression for \(U_\ell\) has period dividing \(4,6,8\), respectively, in \(\ell\). Since their least common multiple is \(24\), all off-diagonal entries of \(H_{\ell+24}\) and \(H_\ell\) coincide. Since \(U_\ell(1)=\ell+1\), the diagonal increases by \(24\). Therefore, for every \(\ell\ge0\),

\[
\boxed{H_{\ell+24}=H_\ell+24 I_{24}.}
\]

This already reduces the infinite-degree statement to the first 24 degrees. Because each \(H_r\) is positive semidefinite, \(H_{r+24k}\) is strictly positive for \(k\ge1\). It also shifts all eigenvalues exactly.

**Step 3: finite exact characteristic-polynomial certificates.** The source file `verify_f4_spectra.py` constructs the 24 signed root representatives using integer coordinate tuples, and builds all 24 base Gram matrices. Their inner products are precisely \(0,1,\pm1/2,\pm1/\sqrt2\) or the diagonal. The required values of \(U_r\) are obtained without trigonometric approximation from the integer cycles

\[
U_r(0): (1,0,-1,0),\quad U_r(1/2):(1,1,0,-1,-1,0),
\]
\[
U_r(1/\sqrt2):(1,\sqrt2,1,0,-1,-\sqrt2,-1,0),
\]

of periods \(4,6,8\), respectively; signs at negative arguments follow from \(U_r(-t)=(-1)^rU_r(t)\). For even \(r\), the Gram is integral. For odd \(r\), the similarity transform

\[
S_r=D^{-1}H_rD,\qquad D=\operatorname{diag}(I_{12},\sqrt2 I_{12})
\]

is integral as well. Each matrix has dimension 24. The checker uses exact integer matrix multiplication to compare \(\operatorname{tr}(S_r^j)\), for every \(1\le j\le24\), with the sum of \(j\)-th powers from the claimed eigenvalue-multiplicity row. Newton's identities imply that these 24 power sums determine the entire characteristic polynomial of each \(24\times24\) matrix. Thus all displayed eigenvalues and multiplicities are certified by finite exhaustive integer identities, not numerical eigenvalue guesses. In particular, the characteristic polynomial at degree \(11\) is \((z-12)^{24}\), and that at degree \(23\) is \((z-24)^{24}\).

**Step 4: consequences.** Reading off the number of nonzero eigenvalues yields the rank sequence and the low-degree losses. A Gram of a surjective sampling map is tight exactly when all its eigenvalues agree. Inspection of the complete base table shows this occurs only at base degrees \(11\) and \(23\); a common scalar shift preserves equality or inequality of eigenvalues. At degree \(7\), the nonzero squared singular values are \(6\) and \(12\), giving the stated condition number.

## Verification

Run `python verify_f4_spectra.py` in an ordinary Python 3 environment. It prints the 24 exact ranks, verifies each base matrix is symmetric before similarity, checks the degree-24 increment entrywise, and verifies all 576 exact integer power-sum identities (24 base degrees times 24 powers). The source requires no third-party packages. These finite integer checks establish the table; the analytic addition theorem and period-shift identity establish the all-degree extension. No finite sample of larger degrees is used to infer the infinite claim.

## Relationship to prior work

Bannai, Okuda, and Tagami (arXiv:1308.5101, initial posting 2013-08-23) formulate spherical harmonic-index designs using Gegenbauer reproducing kernels and give design and cardinality criteria; that work does not report the 24-line \(F_4\) exact-degree evaluation spectrum. Hirao, Nozaki, and Tasaka (arXiv:2303.09000) study the \(D_4\) root lattice, \(F_4\) symmetry and harmonic-index design strength, rather than the pointwise evaluation spectrum on the **union of normalized short and long** \(F_4\) root directions. A known general integer-angle periodicity argument supplies the eventual-surjectivity/period-shift mechanism, and known single-24-cell results supply individual orbit data. Those broader observations do **not** determine the cross-orbit Gram coupling or the 24 new base spectra above. The distinct information here is their complete exact resolution, the nonmonotone rank deficits and the early tight degree \(11\).

## Limitations

The uniqueness claim is limited to the two tight residue classes within this explicitly specified 24-line configuration. The computation certifies full finite-degree characteristic polynomials via exact arithmetic, but no independent audit has been performed. Literature searches and inspected primary texts cannot exclude unidentified equivalent spectral classifications in unindexed or differently named sources. Root directions are normalized before sampling; interpreting the original nonunit \(F_4\) root coordinates directly would define a different problem.

## References

1. E. Bannai, T. Okuda and M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101, initially posted 2013-08-23. Reproducing-kernel and design framework.
2. M. Hirao, H. Nozaki and K. Tasaka, *Spherical designs and modular forms of the D4 lattice*, arXiv:2303.09000, initially posted 2023-03-16. D4 harmonic-index theory, F4 symmetry, and root-system decomposition.
