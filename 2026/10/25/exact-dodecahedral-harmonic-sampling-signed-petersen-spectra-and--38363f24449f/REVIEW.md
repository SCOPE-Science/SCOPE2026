# Scientific review: dodecahedral exact-degree harmonic sampling

## Correctness — PASS

The claim uses normalized probability surface measure on the sphere and evaluation scaled by \(1/\sqrt{2\ell+1}\). The addition formula gives the Gram kernel \(P_\ell(x\cdot y)\). Exact vertex arithmetic yields the unsigned Petersen identity \(A^2=2I-A+J\) and the signed identities \(B^2=3I+C\), \(B^3=5B\); their eigenstructure gives the three spectral branches in either parity. These steps apply at all degrees, including zero and rank-deficient degrees. The standard-library checker constructs the vertices in \(\mathbb Q(\sqrt5)\), checks these identities entrywise, and makes exhaustive rational checks of the 561 branches through degree \(186\). The Laplace integral for Legendre polynomials bounds all higher-degree eigenvalues from below. The bound is strictly stronger than the asserted rational minimum for degrees at least \(187\). The equality at degree \(13\) is explicitly verified and unique. The minimum-norm bound follows from singular-value calculus. No finite experiment is used as a substitute for the infinite tail inequality.

## Originality — PASS with publication-priority qualification

Dai and Xu (arXiv:1304.2585v1) treat generic harmonic bases and reproducing kernels rather than the twenty-vertex dodecahedral operator. Bannai, Okuda and Tagami (arXiv:1308.5101v1) establish harmonic-index design theory and already remark on vanishing degrees \(8\) and \(14\) for an icosahedral antipodal half; this familiar invariant-theoretic phenomenon is **not** presented as new. Bates, Khalid and Kennedy (arXiv:1502.07099v1) study multi-degree bandlimited reconstruction on deliberately arranged iso-latitude samples, not exact-degree spectra of a Platonic orbit. A related complete icosahedral evaluation classification on twelve vertices does not imply the twenty-vertex signed-Petersen spectrum or its sharp global stability constant: duality does not preserve the two evaluation matrices or their dimensions. Mathematical-record and publication searches for the three-sector eigenvalues, exceptional degrees, and the exact rational constant did not reveal directly dominating coverage. Classical representation-theoretic and association-scheme tables remain a genuine older-equivalence risk; no absolute priority is asserted.

## Mathematical value — PASS

This is a natural canonical 20-point spherical interpolation configuration rather than a parameter-chosen finite slice. Exact spectra expose the nonmonotone rank defects at degrees \(5\), \(8\), and \(14\), establish sharp eventual parity-data surjectivity at degree \(15\), and give the optimal **degree-independent** Moore–Penrose stability factor attained at the unexpectedly delicate degree \(13\). The signed-Petersen decomposition makes the structure transparent and the exact rational certificate reproducible. The theorem does not claim stable recovery from unattainable data, a result for incomplete vertex sets, or a uniform bound on conditioning after changing normalization.

## Residual risks and limitations

An older dodecahedral spherical-association-scheme computation or an icosahedral harmonic-character table may conceal equivalent all-degree eigenvalues, including the rational extremum. The full historical priority question has not been independently adjudicated. The exact arithmetic proof uses a finite executable certificate; the independent mathematical audit channel is separate and unperformed.

Self-review: passed. Independent audit: not yet performed.
