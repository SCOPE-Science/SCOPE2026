# Same-model scientific review

## Correctness
PASS. The explicit design has residual projector \(vv^\top\) and tested OLS functional \(q^\top\). For iid Gaussian errors, the observed null statistic \(U=q^\top\varepsilon\) is independent of the residual amplitude \(Z=v^\top\varepsilon\). Uniform observation permutations produce exactly three randomized values, with probabilities obtained by counting whether two sampled coordinates of the balanced sign vector have equal or opposite signs. The source's empirical critical value then reduces rejection to a binomial tail conditional on four angular regions of the independent Gaussian pair. Rotational symmetry gives the displayed exact formula. The proof handles the strict rejection inequality and the \(k>m\) no-rejection case.

## Originality
PASS with a stated literature risk. The direct source, arXiv:1908.04218, defines the analyzed full-model residual permutation procedure and proves low-dimensional sufficient validity conditions, but does not state a saturated exact-size construction. The later high-dimensional comparison arXiv:2211.16182 reports numerical over-rejection of the Toulis procedure and develops different projected permutation methods; it does not derive the exact three-point law or finite-\(m\) size. Searches over saturated regression, permuted OLS residuals, exact Gaussian size, and \(p=n-1\) formulations did not locate an equivalent theorem.

## Value
PASS. The result turns a qualitative dimension warning into an exact structural boundary law. It shows that with only one residual degree of freedom the permutation reference distribution can collapse even under iid Gaussian errors, and it quantifies the actual finite number of random permutations used by the source algorithm. The limiting rejection probability \(1/2\) demonstrates a severe and mathematically transparent failure mode.

## Closest literature and limitations
Toulis, arXiv:1908.04218, is the direct predecessor. Wen, Wang, and Wang, arXiv:2211.16182, is the closest later high-dimensional comparison and supplies empirical evidence of residual-randomization size inflation while proposing a distinct projected RPT. The construction here is deliberately saturated and does not establish worst-case behavior for all designs or for restricted-residual, studentized, or Freedman--Lane procedures. Older residual-permutation literature may contain an equivalent boundary calculation under different language.

Same-model review: passed. Independent audit: not yet performed.
