# Review of the sharp two-mode equatorial stability theorem

## Correctness — PASS

The exact observation operator is defined by Haar probability averaging over oriented great circles and exactly one positive Fourier coefficient at each of orders \(2\) and \(3\). Fubini and Jensen extend it to \(L^2(S^2)\), avoiding undefined traces of arbitrary \(L^2\) representatives on any fixed measure-zero great circle. Rotation representation orthogonality gives the diagonal eigenvalues \(\lambda_\ell=(\ell-m)!/(\ell+m)!\,|P_\ell^m(0)|^2\), where \(m=2\) for even \(\ell\ge2\) and \(m=3\) for odd \(\ell\ge3\). Legendre differentiation yields the two closed central-binomial formulas. The strictly decreasing Wallis quantities \(W_k=(2k+1)\binom{2k}{k}^2/16^k\) converge to \(2/\pi\), and explicit rational factors give \((\ell+1)\lambda_\ell>W_k\). High-frequency test harmonics give optimality, while small support-function perturbations preserve strict convexity. Exact-rational zonal integration independently checks the formulas through degree 22; the infinite statement is proved analytically, not by finite sampling.

## Originality — PASS, subject to historical priority

The 2026 motivating primary theorem establishes precisely the **zero-observation kernel** but not any positive sharp stability coefficient or optimal loss. The 2017 arc-transform SVD uses the same Legendre and Wigner ingredients but averages all arcs and incorporates many Fourier orders; the published theorem does not state an inverse bound for exactly orders \(2\) and \(3\), nor the sharp \(2/\pi\) constant for the selected operator. The present eigenvalue identity is closely related to that known machinery, and a reader may derive individual eigenvalues from its components; this is an acknowledged priority risk. The claimed new unit is the sharp two-mode quantitative stability theorem, not the underlying representation identities, qualitative injectivity, or general tomography SVD. Searches for equivalent two-order stability, its Sobolev normalization, and stronger implication did not reveal covering results.

## Mathematical value — PASS

The natural recent qualitative rigidity question asks whether slight violations of projected rotational symmetry force a body close to a sphere. The theorem provides a complete quantitative answer at a natural weak spectral scale, with exact singular multipliers, sharp constant and impossibility of improving the derivative loss; the same sharpness witnesses are real smooth strictly convex bodies. This is not just a finite table, an arbitrary bounded parameter slice, or a restatement of the zero-kernel theorem. A stronger Hausdorff-distance stability theorem would need additional a priori regularity and is not asserted.

## Limitations and nearest literature

Three dimensions, normalized Haar measurements and the specific two positive Fourier orders are required for the exact coefficient. The inequality does not directly control \(L^2\) or Hausdorff distance, and the prior 2017 all-arc SVD may contain equivalent implicit spectral ingredients. The 2004 averaged-projection stability work uses a different operator. No external independent validation or universal historical-priority guarantee is claimed.

Self-review: passed. Independent audit: not yet performed.
