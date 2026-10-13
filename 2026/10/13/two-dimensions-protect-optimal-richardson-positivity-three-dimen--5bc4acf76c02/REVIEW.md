# Self-review

## Correctness
PASS. For \\(2\\times2\\) SPD Stieltjes matrices, the exact spectral-optimal Richardson matrix \\(T\\) has trace zero and satisfies \\(T^2=q^2I\\), while \\(I+T\\) is entrywise nonnegative. Pairing even and odd powers proves every zero-start iterate is nonnegative for every nonnegative right-hand side. The \\(3\\times3\\) witness is verified exactly: its spectrum is \\(\\{1,9,11\\}\\), the optimal parameter is \\(1/6\\), the iteration spectral radius is \\(5/6\\), and the first coordinate of the third iterate is \\(-1/108\\).

## Originality
PASS with stated residual risk. Published-finding-index searches for optimal Richardson positivity, Stieltjes/M-matrix order preservation, nonnegative iterates, and dimension thresholds returned no implication-equivalent finding. The closest indexed published finding, `2026/9/20/SCOPE-stagewise-safe-two-step-richardson-frontier--31fff666d705`, concerns Euclidean nonexpansion and two-step acceleration, not coordinatewise positivity. Full-text inspection of Vajteršic's 1985 Richardson paper found the classical \\(I-bM\\) iteration and cyclic spectral parameters but no Stieltjes positivity/minimal-dimension statement. Reichel's 1988 work is about polynomial acceleration. Micchelli–Willoughby's 1979 abstract concerns functions preserving the Stieltjes matrix class, a different sign-preservation question. The principal residual risk is older matrix-splitting literature using monotone-iteration terminology.

## Value
PASS. Spectrally optimal Richardson damping is canonical, and Stieltjes systems are the standard symmetric inverse-positive class arising from discrete elliptic problems. The result isolates a sharp dimensional boundary between spectral convergence and coordinatewise order preservation: two dimensions are protected for every right-hand side, while dimension three already permits transient negative solution components. This is a structural distinction, not a parameter renaming or a finite table lookup.

Self-review: passed. Independent audit: not yet performed.
