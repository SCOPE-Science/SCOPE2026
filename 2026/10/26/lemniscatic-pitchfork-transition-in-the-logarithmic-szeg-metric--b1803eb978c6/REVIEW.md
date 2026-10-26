# Scientific review: annular logarithmic Szegő metric

## Correctness — PASS

For the Euclidean-arclength annular Hardy kernel \(S_q\), orthogonality of Laurent monomials yields the displayed diagonal series. A half-integer rewrite and the precisely normalized classical Jacobi-cosine Fourier expansion give \(Z_h=(2\sqrt mK(m)/\pi)\operatorname{cn}(2iK(m)u/\pi\mid m)\). The Jacobi ODE and first integral yield the exact closed metric formula. Imaginary transformation makes \(C_h(u)^2\) run bijectively through \([1,\infty)\) over half of the annulus, reducing the infinite-dimensional kernel calculation to a globally exhaustive, elementary convex minimization of \(my+(1-m)/y\). The nome identity makes \(m=1/2\) equivalent to \(h=\pi\); the coefficient of the first nonzero critical Taylor term is \(8K(1/2)^6/\pi^6>0\). No numerical experiment is used to establish a global claim. The included finite checker passed 1284 numerical assertions by comparing independent expressions and checking boundary patterns.

## Originality — PASS (with historical-priority risk)

The focal kernel paper (Gafai–Murid–Wahid, arXiv:2202.09114, 2022-02-18) states bilateral/product Szegő formulas and their zeros, not the two-ring metric minimizer bifurcation. The highly relevant Katori–Shirai full article (arXiv:2008.04177) determines one-point zero intensities and different two-point correlation phase transitions, not the logarithmic-metric minimum or critical nome. Krantz–Wójcicki (2021) develop projective Szegő distances but do not analyze annuli. DLMF 22.11.2 gives only a Jacobi Fourier identity. The new optimization is not a restatement of the input kernel, raw Euclidean zero intensity, or an ordinary off-diagonal Szegő zero. A classical elliptic-function or kernel-curvature identity could imply parts of the theorem without matching vocabulary; priority is provisional, not proven by negative searches.

## Mathematical value — PASS

The pointwise norm geometry of an annular Hardy reproducing-kernel space changes qualitatively when the conformal modulus passes a distinguished self-complementary elliptic value. The exact switch between one center circle and two reciprocal rings, sharp transition \(q=e^{-\pi}\), complete optimizer classification, and quartic degeneracy characterize the global geometry of a natural kernel-induced metric and the cylindrical-density profile of its canonical Gaussian zero process. This is a structural threshold for a parameterized family rather than a numerical sample or unmotivated finite cutoff. The exact classical elliptic series is only an input; the motivated global classification is the contribution.

## Sources and limitations

Sources examined: full texts of Gafai–Murid–Wahid (2022), Katori–Shirai (2022), Krantz–Wójcicki (2021), and NIST DLMF §22.11. The ordinary Euclidean-arclength Hardy metric is distinguished from weight-perturbed kernels, Euclidean zero intensity, and global geodesic distance. The remaining risk is an unindexed equivalent classical elliptic formulation. Numerical corroboration is finite and not independent validation.

Self-review: passed. Independent audit: not yet performed.
