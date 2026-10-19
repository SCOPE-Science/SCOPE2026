# Review of the four-point Walsh minor spectrum

## Correctness: PASS
The proof reduces row index sets to exactly two affine types and evaluates the local restriction matrices using integral geometry of the three-cube. The critical determinant step is explicit: after normalization, a \(4\times4\) sign determinant is \(8\) times a \(3\times3\) binary determinant. The seven binary two-plane triples yield exactly six zero determinants and one determinant of magnitude two; the 28 independent triples yield magnitude one. The restricted-column occupancy formula is inclusion-exclusion. The standalone checker exhausts all \(4900\) minors at order eight and \(3{,}312{,}400\) minors at order sixteen with integer arithmetic; both ranks and determinant counts agree. Cauchy--Binet supplies a separate exact norm check. The infinite-family result follows from the geometric proof, not an extrapolation.

## Originality: PASS, with residual risk
The closest published Walsh-support result classifies zero patterns for four-sparse nonzero-coefficient signals, not the rank and determinant incidence of all four-by-four Fourier submatrices. Existing order-eight determinant-maximality results do not give a dimension-free count of each minor value or rank. The inspected full texts of Herr--Wiegand and Carlet--Pastor-Díaz--Tornero do not supply these counts. Huckle--Kravvaritis's 2016 article is especially relevant in title but its accessible description addresses leading principal submatrices; its full text was unavailable and remains a stated risk. No independence or universal novelty certification is asserted.

## Mathematical value: PASS
The spectrum of the fourth compound of a Walsh Fourier matrix is a natural interpolation and Hadamard-submatrix invariant. The result classifies every possible degeneracy and determinant magnitude for all binary dimensions, distinguishes the two four-point affine types, and gives closed counts for every rank and for every maximally conditioned four-frequency selection. It is not merely a numerical order-eight or order-sixteen table: the structural argument yields formulas for the complete infinite dyadic family. It supplies sharp incidence data invisible in support-cardinality uncertainty diagrams.

## Scope and remaining risk
The classification is for unnormalized Walsh matrices on elementary abelian two-groups, minor size four, and ranks over the reals. There has been no independent audit. An equivalent old classification in specialized Hadamard/design literature remains possible.

Self-review: passed. Independent audit: not yet performed.
