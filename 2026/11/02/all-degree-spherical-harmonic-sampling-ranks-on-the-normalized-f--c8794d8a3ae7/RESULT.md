# All-degree spherical-harmonic sampling ranks on the normalized \(F_4\) root system

## Finding
Let \(X\subset S^3\) be the 48 unit directions of the exceptional root system \(F_4\), namely
\[
X=\left\{\frac{\pm e_i\pm e_j}{\sqrt2}:1\le i<j\le4\right\}
\cup\left\{\pm e_i:1\le i\le4\right\}
\cup\left\{\frac12(\pm e_1\pm e_2\pm e_3\pm e_4)\right\}.
\]
All signs are independent where displayed. For each integer \(\ell\ge0\), evaluate the full complex vector space \(\mathcal H_\ell(S^3)\) of exactly-degree \(\ell\) spherical harmonics at the 48 sites, obtaining \(E_\ell\). Its ranks at degrees \(0\le\ell\le22\) are:

| \(\ell\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\operatorname{rank}E_\ell\) | 1 | 4 | 9 | 16 | 13 | 20 | 19 | 24 | 23 | 20 | 22 | 24 |

| \(\ell\) | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\operatorname{rank}E_\ell\) | 24 | 24 | 23 | 24 | 23 | 24 | 24 | 24 | 24 | 24 | 23 |

For **every** \(\ell\ge23\), the rank is 24. In particular, degree 22 is the last degree at which interpolation fails to be surjective onto the appropriate 24-dimensional antipodal parity subspace. Full parity-compatible interpolation already occurs at degree 7, but it fails again at several later degrees.

## Assumptions and scope
The sphere is the unit three-sphere in \(\mathbb R^4\), and the harmonic spaces are complexifications of real homogeneous harmonic polynomials. The evaluation map has 48 outputs, subject for every \(\ell\) to \(f(-x)=(-1)^\ell f(x)\). Hence its rank is at most 24. The matrix entries and all ranks are over characteristic zero. The 24 short and 24 long roots are each individually normalized to unit length; without this convention the zonal Gram argument would not apply as stated.

## Proof
**1. Addition theorem and antipodal compression.** The addition theorem on \(S^3\) identifies the evaluation Gram matrix, up to a positive scalar, with \(G_\ell(x,y)=U_\ell(x\cdot y)\), where \(U_\ell(\cos\theta)=\sin((\ell+1)\theta)/\sin\theta\) is the degree-\(\ell\) Chebyshev polynomial of the second kind, with \(U_\ell(1)=\ell+1\). Because \(U_\ell(-t)=(-1)^\ell U_\ell(t)\), selecting one representative from each antipodal pair gives a real symmetric \(24\times24\) matrix \(Q_\ell\) with exactly the rank of \(E_\ell\). It is positive semidefinite, and every diagonal entry equals \(\ell+1\).

**2. Exact root inner products.** Partition the 24 representatives into 12 from the normalized long-root cell and 12 from its dual. Distinct representatives from the same part have inner products in \(\{-\tfrac12,0,\tfrac12\}\). Inner products across the parts lie in \(\{-1/\sqrt2,0,1/\sqrt2\}\), and each representative has exactly six nonorthogonal cross-part partners. Directly from the sine formula, \(U_\ell(0)\) is periodic of period four with entries \(1,0,-1,0\); \(U_\ell(1/2)\) has period six with entries \(1,1,0,-1,-1,0\); and \(U_\ell(1/\sqrt2)\) has period eight with entries \(1,\sqrt2,1,0,-1,-\sqrt2,-1,0\). Negative arguments contribute the factor \((-1)^\ell\).

**3. Analytic all-degree cutoff.** When \(\ell\) is even, all 23 off-diagonal entries of each row have modulus at most one, so strict diagonal dominance holds for \(\ell\ge24\). When \(\ell\) is odd, the 11 same-part off-diagonal entries have modulus at most one, and only six cross-part entries may be nonzero, each of modulus at most \(\sqrt2\). The absolute off-diagonal row sum is therefore at most \(11+6\sqrt2<20\). Thus strict diagonal dominance holds for every odd \(\ell\ge19\). A symmetric strictly diagonally dominant matrix with positive diagonal is nonsingular. Consequently only the finite list of small degrees specified in the next step requires exact calculation.

**4. Exact finite rank certificate.** For the remaining degrees, the attached `CHECKER.py` constructs the 12+12 antipodal representatives from integral coordinate tuples, uses the three exact periodic Chebyshev tables above, and forms \(Q_\ell\). In odd degrees, simultaneous multiplication of the rows and columns corresponding to the dual cell by \(\sqrt2\) turns the matrix into an integer matrix without changing rank; in even degrees it is already integral. The checker computes ranks by Gaussian elimination over exact rational numbers, with no floating-point thresholds. It certifies degrees \(0,1,\dots,18,20,22\) and yields exactly the table in the Finding. Degrees 19 and 21 are already covered by Step 3. Combining Steps 3 and 4 proves the theorem for every nonnegative integer degree.

**5. Group-theoretic interpretation.** The normalized 48-point set is the binary octahedral quaternionic group. Its zonal kernel \(U_\ell(\langle g,h\rangle)\) is the restricted \(\mathrm{SU}(2)\) character of the \((\ell+1)\)-dimensional symmetric-power representation, evaluated at \(g^{-1}h\). For an irreducible group representation \(\sigma\), the corresponding convolution eigenspace has dimension \((\dim\sigma)^2\) and nonzero eigenvalue precisely when \(\sigma\) occurs in the restriction. This explains why the rank defects encode missing representation sectors rather than simply the vanishing of the average of a harmonic.

## Verification
Execute `python3 CHECKER.py` using Python 3 standard libraries only. The program reconstructs all 24 antipodal representatives, validates cross-part inner-product incidences, forms exact integer Gram matrices, and reports 21 certified small-degree ranks. An independent symbolic-rank calculation on the nine nontrivial small-degree cases \(\ell=4,6,8,9,10,14,16,20,22\) agreed. The infinite tail is established by strict diagonal dominance and is **not** inferred from computational sampling.

## Relationship to prior work
The 24-cell's spherical-design structure is studied by Cohn–Conway–Elkies–Kumar (2006) and the coherent-configuration framework by Bannai–Bannai (2009). Hirao–Nozaki–Tasaka (2023) study harmonic-index designs of the 24-root \(D_4\) cell. Crucially, Hirao–Nozaki–Tasaka (2025), Theorem 1.2, determine the harmonic-strength degrees of the 48-point binary octahedral group: \(\{2,4,6,10,14,22\}\) and all positive odd degrees. That asks when the **sum** of all evaluations of any degree-\(\ell\) harmonic is zero. The present rank statement instead determines the **entire image dimension**. In particular, degrees 8 and 16 each lose one nonconstant output dimension although neither belongs to that previously identified even-degree harmonic-strength set. The degrees with larger rank deficits are also quantified. The new classification is not inferred from the harmonic-strength theorem alone.

## Limitations
The theorem addresses the exact 48-point normalized configuration only, not arbitrary perturbations or other root systems. It determines ranks, not singular-value condition numbers or explicit bases for every kernel. The literature comparison is bounded; an equivalent complete rank table hidden in broader finite-group representation literature remains possible. No external independent mathematical validation is claimed.

## References
1. H. Cohn, J. H. Conway, N. D. Elkies, A. Kumar, *The \(D_4\) root system is not universally optimal*, arXiv:math/0607447, first publicly posted 2006-07-19, https://arxiv.org/pdf/math/0607447.
2. E. Bannai, E. Bannai, *Euclidean designs and coherent configurations*, arXiv:0905.2143, first posted 2009-05-13, https://arxiv.org/pdf/0905.2143.
3. M. Hirao, H. Nozaki, K. Tasaka, *Spherical designs and modular forms of the \(D_4\) lattice*, arXiv:2303.09000, first posted 2023-03-16, https://arxiv.org/pdf/2303.09000.
4. M. Hirao, H. Nozaki, K. Tasaka, *Spherical designs for finite quaternionic unit groups and their applications to modular forms*, arXiv:2507.01358, first posted 2025-07-02, https://arxiv.org/pdf/2507.01358.
