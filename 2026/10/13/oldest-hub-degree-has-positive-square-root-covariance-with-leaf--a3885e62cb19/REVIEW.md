# Review

## Correctness

PASS. The proof conditions on the current tree and uses only the defining attachment probabilities. The update variables \(X_n\) and \(Y_n\) satisfy exact conditional expectations \(D_n/(2(n-1))\) and \(L_n/(2(n-1))\). Their product is nonzero precisely when the distinguished initial vertex is still a leaf and is selected, producing the correction \(q_n/(2(n-1))\). The mixed-moment recurrence and the covariance increment follow algebraically.

The closed forms for \(\mathbb E D_n\), \(\mathbb E L_n\), and \(q_n\) solve their one-step recurrences with the correct size-two initial conditions. Positivity follows directly from the exact increment. The square-root asymptotic follows from the gamma-ratio asymptotic and summation of \(n^{-1/2}\).

## Originality

PASS, with a residual risk from older implicit preferential-attachment recurrences. The closest full modern source on leaves, Hartle--Krapivsky, studies typical-vertex degree--leafdegree distributions and aggregate count fluctuations, including aggregate leaf/count covariances. It does not state the degree of a distinguished oldest vertex jointly with the total leaf count. The full Peköz--Röllin--Ross source studies degree counts, order statistics, and old-vertex degree behavior but does not introduce the total leaf count in the inspected text.

The new statement is not implied by either marginal theory: one needs the joint one-step correction in which root selection and leaf selection coincide only while the root remains a leaf.

## Value

PASS. The oldest vertex is a canonical persistent hub in preferential attachment, whereas the total number of leaves is the principal global boundary statistic. Their interaction is mathematically nontrivial because attachment to the hub and attachment to a leaf compete at a single step, yet the resulting covariance is positive and grows like \(\sqrt n\).

The exact increment law explains the mechanism and gives a finite-\(n\) statement rather than only a scaling heuristic. It complements aggregate degree/leaf-count covariance theory by isolating a nonexchangeable old vertex.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK aggregated_states_checked=2055 moment_checks=32 increment_checks=7 positive_covariance_checks=6 asymptotic_ratio_checks=3`.
