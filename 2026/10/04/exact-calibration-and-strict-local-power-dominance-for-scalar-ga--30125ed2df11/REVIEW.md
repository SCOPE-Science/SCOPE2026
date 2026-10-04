# Same-model review

## Correctness
PASS. The scalar reduction follows directly from the published two-way statistic after accounting for the source denominator \(m^{-1}\sum (X_i-\bar X)^2\), which produces the factor \(\sqrt{m/(m-1)}\) relative to the usual Student statistic. Gaussian mean/variance independence gives the exact null law. The local-power proof uses joint Student convergence, an orthogonal Gaussian rotation, and a monotone folded-normal likelihood ratio; no finite experiment is used as an infinite proof.

## Originality
PASS. The closest direct source, Kim and Ramdas (arXiv:2011.05068; DOI 10.3150/23-BEJ1613), defines the two-way cross-fitted statistic and proves a general fixed-dimensional limiting null distribution, but does not give the scalar finite-sample Student law, exact calibration, or strict cross-fit versus single-split local-power theorem. Guo and Shah (arXiv:2301.02739; DOI 10.1093/jrsssb/qkae091) later develop a different rank-transformed multiple-splitting procedure; their Example 2 explicitly treats the simple cross-fit as nonnormal rather than deriving the present law. Targeted semantic and exact-phrase searches found no equivalent claim. Residual risk remains from older literature under different terminology.

## Value
PASS. The source identifies multiple splitting as a route to reduce single-split inefficiency and explicitly highlights the calibration difficulty. In the canonical scalar Gaussian case, the finding gives an exact finite-sample calibration and proves a strict power gain for every nonzero local signal, providing a sharp solvable benchmark for that open methodological issue.

## Closest literature and limitations
The closest literature is the direct cross-U-statistics paper and the later rank-transformed-subsampling paper. The theorem is deliberately narrow: balanced scalar Gaussian two-way cross-fitting, one-sided \(0<\alpha<1/2\), exact null calibration, and local-asymptotic power. It does not imply finite-sample power dominance, arbitrary multi-split validity, or a high-dimensional result.

Same-model review: passed. Independent audit: not yet performed.
