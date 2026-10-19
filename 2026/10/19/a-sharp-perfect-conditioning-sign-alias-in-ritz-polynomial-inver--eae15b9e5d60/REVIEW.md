# Scientific assessment

## Correctness — PASS

The asserted spectral identity is an exact factorization of \(zq(z)^2-1\). Interpolation at two distinct nodes fixes the line uniquely; its cubic roots prove both the necessary-and-sufficient third-eigenvalue condition and the strict conditioning threshold. The one-step Arnoldi action follows directly from the eigenvector compression, not from an asymptotic approximation. For the full-support pilot, the actual Lanczos roots are reconstructed from four weighted moments; monotonicity and an exact quadratic isolate a unique sign transition. The condition-number expansion follows from differentiated spectral entries. The attached verifier independently checks these critical identities and numerical projections (169 checks).

## Originality — PASS, with qualification

The 2024 polynomial-preconditioning paper already states that loss of the correct polynomial sign can select a different square-root branch; this general warning and both the interpolating-preconditioner and Arnoldi formulas are acknowledged as prior work. The narrow additional result is the algebraic rigidity \(\gamma=(\sqrt\alpha+\sqrt\beta)^2\) of **exactly identity** preconditioned SPD three-point spectra, the sharp threshold \(\kappa_2(A)>4\) in that anchored class, and the complete full-support two-step Lanczos visibility transition. Full HTML portions covering theoretical branch conditions, interpolation, and numerical examples were inspected. Matrix-function branch theory in Higham supplies broader conceptual coverage but not the specific spectral/pilot classification. Search and prior-claim comparisons did not identify a mathematical implication covering all of these additional statements. The remaining possibility that the same small algebraic classification occurs in unindexed literature is a genuine priority risk, not a proof of novelty.

## Value — PASS

Eigenvalue clustering of \(Aq(A)^2\) is commonly used to interpret whether matrix-function polynomial preconditioning will require a small Krylov space, but this test does not enforce the principal branch. The result identifies the strongest possible separation, with \(Aq(A)^2=I\), exact zero projected residual, and maximal relative action error; it determines the unique spectral configuration in the two-node affine setting. The full-support pilot and sharp transition quantify how a partly detected eigenmode can retain or eliminate that failure. These are reusable structural benchmarks for stopping tests and positivity safeguards rather than an arbitrary recomputation of known examples.

## Closest literature and limitations

A. Frommer, G. Ramirez-Hidalgo, M. Schweitzer, and M. Tsolakis, arXiv:2401.06684v1 (2024), Sections 3 and 5, establish the method and warn of sign-branch changes. N. J. Higham, *Functions of Matrices* (2008), develops principal and nonprincipal roots. The result applies only to the specified SPD, exact-arithmetic, affine two-node Ritz-interpolation setting. It does not claim generic failure under random pilots or despite a certified uniform positive polynomial approximation. Full-text priority verification outside the inspected materials and independent scientific audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
