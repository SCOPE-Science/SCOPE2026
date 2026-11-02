# Scientific review of the exact uncentered triangular-prism maximal norm

## Correctness

**PASS.** The exact domain is the unweighted six-vertex triangular prism, counting measure, graph-distance balls, and real \(\ell^2\). A ball containing a fixed vertex is one of six possibilities, which produces exactly 46,656 linear selection matrices. For nonnegative input the maximal operator is the coordinatewise maximum of these positive matrices; their largest singular values give its exact nonlinear norm. This equality is justified by exchanging a finite maximum with a compact unit-sphere maximum and taking absolute values of singular vectors.

The shipped verifier uses exact integer Sylvester tests, not approximate eigenvalue comparisons, to exclude 46,638 of 46,656 matrices below squared norm \(81/50\). It derives and checks the characteristic polynomial for the remaining 18; the largest root of the stated cubic is strictly above that threshold. The displayed positive eigenvector is checked analytically, and an exact rational interval test proves strict activity of every chosen averaging ball. The equality classification follows from simplicity of the Perron eigenvalue for each exceptional matrix. A separate 729-matrix test certifies strict comparison with the centered operator. No extrapolation from a finite sample is used.

## Originality

**PASS, with publication-priority limits.** Full-text inspection of Soria–Tradacete (arXiv:1410.6204) shows finite-graph centered norm results and broad \(0<p\le1\) estimates, not the uncentered six-vertex strong Hilbert problem. González-Riquelme–Madrid (arXiv:2005.03146) explicitly defines uncentered maximal averages but its sharp strong Hilbert norm results apply to complete and star graphs. González-Riquelme–Kovač–Madrid (arXiv:2603.12462) treats centered variation, including a census of graphs up to five vertices, not the present operator or graph. The accessible previous centered triangular-prism result has a different averaging family and does not imply the uncentered cubic or its two equality orbits. Searches of mathematical records and related terminology found no dominating statement. An unindexed calculation or an unpublished equivalent remains possible.

## Value

**PASS.** The triangular prism is the smallest nontrivial Cartesian product of a triangle with an edge and a natural vertex-transitive cubic test graph. A strict centered–uncentered norm gap occurs despite vertex transitivity. Uncentered maximization exhibits two *inequivalent* graph-symmetry orbits, of six and twelve positive extremizer rays, tied at one algebraic cubic norm; this is a substantive structural phenomenon rather than merely another decimal evaluation. The exact finite classification provides a benchmark for prospective estimates on graph products and for understanding changes in extremizer geometry when the ball center is freed.

## Sources, comparisons and risks

Primary full-text sources inspected: arXiv:1410.6204 (definition, general norm estimates, graph examples and theorem scopes), arXiv:2005.03146 (uncentered definition and sharp centered Hilbert result scopes), arXiv:2603.12462 (theorems on graph variation and the five-vertex census). Searches also tested the triangular-prism and Cartesian-product aliases against published mathematical records. No consulted result is known to imply the new theorem. The closest accessible related calculation is the centered triangular-prism operator, which is strictly smaller; that distinction is independently certified inside the new proof.

The result is restricted to one graph and real \(\ell^2\), and broader publication-priority checking cannot be exhaustive. The exact certificate and mathematical argument have not been reviewed independently.

Self-review: passed. Independent audit: not yet performed.
