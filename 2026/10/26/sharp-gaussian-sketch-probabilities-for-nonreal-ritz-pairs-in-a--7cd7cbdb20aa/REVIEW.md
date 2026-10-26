# Research assessment

## Correctness — PASS

The two-step Lanczos basis is exactly \([e_1,e_2]\). Direct multiplication reduces sRR to a symmetric two-by-two projected matrix plus a Gaussian regression perturbation of its final column. Inverse-Wishart Gaussian regression produces the stated normalized planar Student density with \(\nu=\ell-1\), including the minimal \(\ell=2\) boundary. The two-by-two discriminant is negative exactly inside an explicit parabola. Circle intersection gives the angular fraction. The one-sided Laplace calculation uses the correct square-root angular opening at the nearest point \((-b,0)\), with positive derivative of the radial rate, yielding both exponential factor and sharp prefactor. Positive definiteness, nonterminal Lanczos steps, and dimension minimality are verified. The standalone checker confirms exact rational reductions and numerical samples, but no universal theorem is inferred from simulation.

## Originality — PASS, with priority risk

The originating Nakatsukasa–Tropp manuscript explicitly notes that symmetric sRR can return nonreal approximate eigenvalues and gives the last-column Krylov perturbation representation. Those known claims are excluded from the contribution. The claim here is the exact Gaussian finite-sketch probability for the full two-parameter positive-definite Lanczos triple and its sharp square-root-prefactor large-sketch asymptotic. Full-text comparisons to the originating sRR paper, the related sketched GMRES paper, and sketched polynomial Krylov matrix-function work did not identify that exact probability or sharp asymptotic. Known multivariate Student regression and elementary Laplace methods are not claimed as independent novelties. An equivalent probabilistic derivation in less searchable numerical linear algebra or random-matrix literature remains a residual risk. The statement is not claimed publication-priority certain.

## Value — PASS

The first sRR paper identifies nonreal eigenvalues as an intrinsic drawback even for symmetric input, and prescribes real-part postprocessing. Quantifying how frequently the anomaly occurs as Gaussian sketch size grows answers a directly motivated numerical eigenvalue question. The exact exponent and prefactor show explicitly how the ratio of successive Lanczos couplings controls the rare-event probability, while proving three dimensions minimal for the phenomenon. This is more than a generic counterexample or an arbitrary parameter experiment; it is a complete exact risk calculation on the minimal nonterminal Lanczos family, though it provides neither full algorithmic error guarantees nor a general higher-dimensional law.

## Scope and literature

References: Nakatsukasa and Tropp (arXiv:2111.00113v1, Sections 6.7–6.8); Burke, Güttel, and Soodhalter (arXiv:2311.14206v1); Palitta, Schweitzer, and Simoncini (arXiv:2306.06481v1, Section 7). The primary source first appeared on 2021-10-29. The mathematical proof is exact-arithmetic and Gaussian-specific; the asymptotic requires fixed positive coupling parameters as \(\ell\to\infty\). No independent scientific evaluation was performed.

Self-review: passed. Independent audit: not yet performed.
