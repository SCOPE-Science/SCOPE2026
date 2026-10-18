# Scientific assessment

## Correctness — PASS

The matrix is exactly decomposed into the constant-vector sector, with eigenvalues \(\lambda_\pm\), and the transverse eigenspaces of its two regular components. The proof explicitly reconstructs the transition amplitudes, performs the Cesàro average with correct degenerate-frequency cross terms, solves every allowed collision equation, and derives the finite-time sinc window from a uniform gap separation. Exact averaging on two equal cliques gives the full finite-window formula without unproved large-size limits. A standalone program replayed 1,330 spectral and finite-window comparisons, including resonances; maximal observed projector-comparison error was below \(2.3\times10^{-14}\). Tests corroborate rather than replace the proof.

## Originality — PASS (self-review)

The 2005 theorem of Lo et al. explicitly excludes lower join-eigenvalue collisions while deriving the known generic average-mixing law for circulant joins. The 2017 work of Coutinho et al. establishes the general spectral-projector identity; the 2023 paper of Kirkland and Monterde supplies general join propagators and state-transfer theory. These known results provide the underlying tools and imply the generic off-resonance component. The assessed contribution is the exact exceptional-coupling classification on arbitrary connected regular components, the positive return-trace jumps with conservation of cross-component mean mass, and the universal finite-time sinc resolution; it is not a claim to invent join diagonalization or average-mixing matrices. A search of semantically matching published mathematical records and published literature found no statement that subsumes this full collision-and-window claim. Unseen equivalent treatments remain possible.

## Value — PASS

The collision is a naturally motivated, excluded case in the prior mean-mixing theorem, not an arbitrary small-graph calculation. Its precise projector jump explains a measurable change in long-time localization, while the finite-window law quantifies how accurately a junction hopping strength must be tuned to observe that effect. Two equal cliques exhibit a jump of \((n-1)/n^2\), and the exact observation window is \(1/(nT)\), giving a physically interpretable graph-size versus waiting-time tradeoff. The result is a complete structure theorem for all connected regular components and a closed all-time benchmark, not just a numerical curiosity.

## Closest literature and limitations

Lo et al., *Mixing of Quantum Walk on Circulant Bunkbeds* (arXiv:quant-ph/0509059v1), Theorem 5, is the closest direct result; its noncollision hypothesis excludes the distinctive phenomenon here. Kirkland–Monterde, *Quantum walks on join graphs* (arXiv:2312.06906v1), treats the same join geometry but not the resonance-resolved Cesàro window. Coutinho–Godsil–Guo–Zhan (arXiv:1709.03591v1) gives the general projector formalism. The result assumes perfectly coherent, finite, uniformly weighted joins, and neither finite simulation nor a negative literature search proves absolute scientific priority.

Self-review: passed. Independent audit: not yet performed.
