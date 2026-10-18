# Research review: diagonal risk and Gaussian moment phase for XDiag

## Correctness — PASS

The sign-probe result follows from two explicit rank-one projectors, a samplewise identity between both leave-one-out components, exact fourth-sign pairings, and the probability-simplex bound \(w_i(1-w_i)\le 1/4\). Equality and the one-probe reference case are characterized. The Gaussian phase follows from an independent Haar projector, a nonzero off-diagonal row, a conditional \(1/s\) pole in one probe coordinate, and integrable fractional moments of Gaussian ratios. The two-dimensional constant follows from an explicit bivariate Cauchy representation and a dominated-convergence split into the two larger-ratio sectors. The reproducible script checks the projector algebra, exact-rational finite examples, local poles, and the asymptotic constant empirically; finite tests are not taken as proofs of infinite claims.

## Originality — PASS, conditional on inspected literature

The principal literature source, Epperly–Tropp–Webber, arXiv:2301.07825, Section 2.4, defines XDiag, uses a sign-probe special implementation, and does not state the exact diagonal-input two-probe covariance, sharp relative error \(1/4\), samplewise collapse of two leave-one-out components, or the formal Gaussian-substitution integrability phase. Hallman–Ipsen–Saibaba, arXiv:2202.02887, analyze the standard product-probe diagonal estimator and Gaussian fourth-moment bounds for that different estimator. Targeted searches of published-finding corpus records for XDiag, leave-one-out diagonal covariance, Gaussian quotient poles, aliases, and finite moment thresholds identified related but non-implying results in AdaHessian off-diagonal RMS noise, Adam condition-number poles, and Gaussian cross-HSIC. All 49 accessible preceding ledger claims were compared for equivalent formulations, not merely matching titles. The nearest previous XTrace variance result concerns *trace* estimation, not a coordinatewise XDiag law. Residual risk: a formerly published Gaussian inverse-moment theorem or older coordinatewise exchangeable estimator study might contain a disguised special case; semantic search is not a uniqueness certificate.

## Value — PASS

There is a concrete reliability gap between good average performance and the behavior of the exchangeable diagonal estimator on trivial inputs. Its exact one-probe baseline is zero error, while two probes incur sharply bounded but nonzero mean-square error; both leave-one-out terms nevertheless agree, demonstrating a failure mode for naïve internal disagreement diagnostics. The Gaussian theorem establishes a precise integrability obstruction to transferring the sign-based quotient to another common probe distribution. These statements give actionable distinctions between algorithm, implementation, probe law and diagnostics, rather than a routine normalization change.

## Primary comparison and limitations

Relevant inspected full texts: XTrace/XDiag arXiv:2301.07825, Section 2.4 and code appendix; Monte Carlo diagonal estimation arXiv:2202.02887, Sections 2–5. The published XDiag implementation is sign-specialized, so the Gaussian extension is explicitly formal. The sign calculation is specific to two probes and diagonal PSD inputs. The Gaussian moment phase is specific to scalar matrices. No claims about finite precision, generic matrix inputs, multiple-stage iteration, or original authors' implementation failure are made.

Self-review: passed. Independent audit: not yet performed.
