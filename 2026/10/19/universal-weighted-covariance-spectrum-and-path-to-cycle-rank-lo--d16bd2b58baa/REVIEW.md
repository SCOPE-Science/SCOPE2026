# Scientific review: universal categorical bigram covariance spectrum

## Correctness — PASS

The exact \(L^2(p\otimes p)\) decomposition into a constant, an additive symmetric potential, an additive antisymmetric gradient, and a doubly centered interaction is complete and orthogonal. The open-path quadratic variance identity assigns eigenvalues \(2m-1\), \(1\), and \(m\) in the unnormalized whitened covariance; the cyclic version assigns \(2n\), \(0\), and \(n\). The dimensions sum to \(q^2\), and every assertion includes its required sample-length boundaries. The mean, every raw covariance entry, the potential and interaction eigenvector equations, and the trace were independently checked by exact sequence enumeration over 25 rational models. The asymptotic Pearson statement follows from the bounded one-dependent vector central limit theorem, not an extrapolation of the finite checks.

## Originality — PASS, with material residual risks

The novelty assessment is **only** for the exact all-parameter finite-sample weighted covariance spectrum, the exact \(q-1\)-dimensional additional cyclic nullspace, and the sharp variational extremizers. Earlier general generating-function literature on overlapping words (Park–Spouge 2004) and cyclic word occurrences (Percus–Percus 2005) concerns broader distributions; its accessible abstracts do not state this closed spectral diagonalization. Those full texts remain inaccessible and could encode these formulas implicitly. The serial categorical testing literature (Bilodeau–Lafaye de Micheaux 2009; Elsinger 2020) already covers orthogonal statistical decompositions and asymptotic calibration. Eigenvalues of the empirical *transition matrix* (Pritchard–Scott 2004) and eigenvalues for *subsequence counts* (Even-Zohar–Lakrec–Tessler 2020/2021) are different observables. A relevant public mathematical findings index returned related fixed-composition binary transition results and adjacent-word reconstruction counts, but no explicit matching finite-sample spectrum. Neither searches nor inaccessible texts prove absolute historical uniqueness.

## Mathematical value — PASS

The covariance matrix is the complete second-order uncertainty geometry of a standard transition-frequency table; computing only its entries is not the same as identifying their universal whitened eigenvalues, rank, sharp cost-variance extrema, and exact boundary effect. Closing a path eliminates an entire nontrivial gradient subspace. The condition number \(2m-1\) and the correct weighted Pearson asymptotic law provide direct inferential consequences. The result is motivated by statistical identifiability and calibration rather than an arbitrary finite numerical invariant.

## Verification scope and limitations

Reproduce the 25-case exact rational checks with `python3 verify_bigram.py`. The proof covers all sample sizes in its stated domain. Historical priority is limited by nonaccess to the full original papers on general overlapping-word counting. Only the precise spectral result is assessed as new; general serial-independence testing and joint-count generating functions are acknowledged prior art.

Self-review: passed. Independent audit: not yet performed.
