# Self-review

## Correctness — PASS

For the stated one-column design and orthogonal residual, the least-squares normal equation reduces exactly to a scalar random quotient. Reused tensor factors split into independent Gaussian-to-chi ratios and yield the stated gamma moments and cutoff at the smaller factor-row dimension. Independent tensor rows give a quotient with independent product-normal design and residual columns; the product-normal logarithmic density singularity, polar integration, and a dominated-convergence argument give the sharp \(t^{-R}(\log t)^R\) tail. The dense reference is a Gaussian-to-chi ratio. The strict mean-square ordering follows from conditional variance and Jensen's inequality. No finite experiment is used as a substitute for asymptotic proof; 1,513 verifier diagnostics confirm sample identities and benchmark constants, not the analytic limit.

## Originality — PASS, with limited priority risk

The main source's two sketch structures and their high-probability embedding theory are acknowledged as prior work, not rebranded. Source-paper text, closely related Gaussian sketching analyses, Gaussian product-moment work, a different tensor-regression sketch, and relevant published numerical-analysis results were compared at claim level. The inspected references neither establish the distinct sharp moment thresholds for these two exact sketch constructions nor the row-independent logarithmic tail coefficient. The classical product-normal density and Student-type ratio results are used as known inputs. Similar results in specialized unindexed work remain possible.

## Value — PASS

This computes the unconditional risk boundary for the two concrete source sketch designs at a fixed sketch row count. Already at four rows, the factor-reusing tensor sketch has infinite mean-square regression error while the independent-row tensor and dense Gaussian alternatives have finite error on a condition-one design; independent rows nevertheless incur a precise logarithmic tail penalty. The ambient problem can be arbitrarily larger than the sketch, making this a meaningful rare-failure distinction for tensor least-squares sketch selection, not a toy conditioning artifact. No claim is made that high-probability guarantees fail or that one method is cheapest to implement.

The benchmark is limited to exact Gaussian sampling, a one-column design, a deterministic orthogonal residual and exact arithmetic. It is not a universal performance ordering for arbitrary inverse problems or an assertion of optimal sketching runtime.

Self-review: passed. Independent audit: not yet performed.
