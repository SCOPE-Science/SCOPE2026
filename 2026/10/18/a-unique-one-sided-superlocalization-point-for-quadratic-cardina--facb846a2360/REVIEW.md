# Review of a unique one-sided quadratic-spline localization point

## Correctness — PASS
The five-diagonal cardinal spline Gram matrix is computed by exact integration. Its symbol is strictly positive and its reciprocal has exactly two simple poles within the unit circle. The residues reconstruct the inverse Toeplitz coefficients. The finite-support decomposition yields an identity for every remote right cell, not a numerical fit. The slow-mode coefficient is an elementary quadratic with one interior root; at that site the other mode remains nonzero. A separate convex-quadratic calculation determines the exact cell suprema and decay rates. The standalone checker independently passed 297 numerical assertions. No finite calculation is used as a substitute for the proof.

## Originality — PASS within the inspected record
Passenbrunner–Shadrin (2013) show general inverse-Gram and projector-kernel exponential estimates, and Shadrin (2001) establishes the general de Boor spline projector boundedness theorem. The reviewed passages do not identify an interior evaluation point where the leading cardinal quadratic inverse-Gram pole cancels. The new result is the unique exact one-sided cancellation and its sharp two-rate classification, **not** discovery of Gram invertibility or uniform spline localization. published-finding corpus published-record queries covering cardinal quadratic kernels, exact Gram inverse roots and superlocalization found no implied equivalent. Historical priority is not thereby proved.

The especially relevant Demko (1977) and de Boor (2011) texts were located but full-text inspection was not achieved; these are residual literature risks. Equivalent material may use the terminology of dual cardinal B-splines or fundamental spline kernels.

## Value — PASS
Exact pointwise localization rates govern truncation error of spline reproducing kernels and dual basis representations. A unique site with complete cancellation of the dominant residue gives a structurally motivated improvement by nearly an order of magnitude in exponential base on one entire remote half-line; establishing its uniqueness and one-sided nature is more informative than merely recomputing a Gram entry.

## Limitations
Quadratic uniform-cardinal knots only; fixed evaluation points and remote right-hand cell suprema only. No uniform-in-mesh estimate, global optimal projection norm, or independent scholarly audit is claimed.

Self-review: passed. Independent audit: not yet performed.
