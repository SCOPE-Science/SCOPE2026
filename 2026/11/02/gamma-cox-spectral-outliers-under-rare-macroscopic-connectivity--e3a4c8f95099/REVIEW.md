# Review of the Gamma–Cox rare-connectivity spectral theorem

## Correctness

**PASS.** The finite graph identity is exact: for a connected threshold graph, the smallest positive Laplacian eigenvalue is the terminal run of universal-vertex creation bits, except that the complete graph has gap equal to its order. The full source spectrum has been independently checked against direct matrix diagonalization on all creation sequences through ten vertices. With the unconditioned two-color Pólya/Beta–Bernoulli law, the macroscopic gap event is precisely a forced terminal block of red bits. Its probability and the Beta posterior therefore follow by direct integration.

The scaling \(n(1-P)\) has a Gamma density limit. Conditional on this latent quantity, the remaining zero bits have probability of order \(1/n\); their finite point process converges by a Laplace-functional calculation. The corresponding eigenvalues differ from reflected vertex positions by at most the tight defect count divided by \(n\). The negative-binomial count, continuous gap density and exact complete-graph atom are mutually consistent consequences. The proof treats all \(a,b>0\) and \(0<\theta<1\), including noninteger urn masses. Numerical and exhaustive finite tests are supporting checks, not substitutes for the limit argument.

## Originality

**PASS under accessible-prior comparison, with historical limits.** The 2026 source gives the exact Laplacian spectrum and urn law, but does not impose an order-\(n\) algebraic-connectivity event or analyze the conditional finite outlier spectrum. Reilly–Scheinerman (2009, Corollaries 5.9–5.10) give the deterministic last-zero identity and fair independent creation-bit gap law in a different random model; these are credited, not presented as new. Diaconis–Holmes–Janson (2008, Theorem 6.4 and Section 9) give fixed-probability empirical graph and Laplacian spectral limits. Their fixed-parameter limits do not retain the finitely many eigenvalues of order \(n\) that remain below the bulk after this shrinking-posterior, rare-event conditioning. The 2026 spectral survey lists general deterministic and random threshold spectra, not the specific conditioned Gamma–Cox limit in the accessible material. Relevant mathematical-record searches also found no directly equivalent or broader covering statement.

The contribution is the joint rare-event posterior and eigenvalue point process, with universal negative-binomial and macroscopic gap laws. Classical Beta–Gamma conjugacy, Poisson approximation, finite threshold spectra and the known fair-bit gap distribution are **not** separately claimed as new. A more general conditioned-exchangeability point-process theorem could yield part of the result with additional specialization; this is a residual priority risk rather than an identified covering result.

## Mathematical value

**PASS.** The source explicitly identifies algebraic connectivity as a natural further spectral property. Conditioning it to be macroscopic is a genuinely rare, polynomial-probability event even though the graph has order \(n\) vertices. The theorem describes *all* remaining macroscopic lower spectral modes, not only the event probability or one moment: the conditioned graph has a finite random number of creation defects whose spatial arrangement is a Gamma-mixed Poisson process, and those defects determine an explicit random spectrum. The atom at the complete graph, the negative-binomial law and the disappearance of the initial red parameter from the conditional limit are specific, interpretable structure. The theorem gives a full, naturally scaled rare-event classification, not an arbitrary finite table or a reparametrization of the known fixed-probability spectral law.

## Scope and residual risks

Fixed positive urn masses relative to reinforcement and a fixed interior conditioning proportion are essential. Endpoints, triangular urn parameters, normalized Laplacian spectra, and fine fluctuations within the bulk are not treated. Priority is based on inspected accessible literature and targeted searches, not an independent historical certification. The full text of the 2026 survey was not exhaustively inspected; accessible sections and cited classical sources were compared. Verification is the stated proof plus a reproducible finite checker; no independent mathematical review has been performed.

Self-review: passed. Independent audit: not yet performed.
