# Same-model review

## Correctness
PASS. The proof reconstructs the exact foldwise likelihood ratio from normalized Gaussian fold means, evaluates its \(q\)-moment by a one-dimensional Gaussian-square integral, and transfers the sharp boundary to the positive fold average. The strict boundary cases are handled: equality makes the Gaussian-square integral diverge. The unequal-split and log-moment corollaries follow from the same normalization and elementary inequalities. `verify.py` independently checks the determinant and threshold algebra.

## Originality
PASS, with residual risk. The closest inspected direct source is Tse and Davison (2022), whose Section 5 studies variance of the cross-fit and \(K\)-fold likelihood-ratio statistics. Wasserman, Ramdas, and Balakrishnan (2023) explicitly note the infinite variance of the Gaussian cross-fit statistic and say its consequences are unclear, while recommending the log statistic as an object of study. The foundational and Gaussian universal-inference papers define and analyze the relevant statistics but do not state the all-real-order moment boundary located here. Targeted searches found no equivalent statement. The publisher-hosted supporting-information file for Tse and Davison was inaccessible, and generic Gaussian quadratic-form theory can abstractly imply the component calculation, so historical-priority risk remains.

## Value
PASS. The result turns an isolated infinite-variance phenomenon into an exact moment phase diagram: \(K\ge p(p-1)+2\) is necessary and sufficient for the integer \(p\)-th moment, two-fold cross-fitting has the golden-ratio critical exponent, balanced splitting uniquely maximizes the two-way exponent, and the logarithm remains polynomially well behaved. These facts directly inform stability diagnostics for universal likelihood-ratio averaging without claiming that larger \(K\) improves power.

## Closest literature and limitations
The scientific comparison is to arXiv:1912.11436, arXiv:2104.14676, DOI:10.1002/sta4.501, and DOI:10.1002/sta4.573. The theorem is restricted to a simple Gaussian mean null with known unit variance and disjoint folds. The inaccessible supporting information is retained as an originality risk rather than treated as negative evidence.

Same-model review: passed. Independent audit: not yet performed.
