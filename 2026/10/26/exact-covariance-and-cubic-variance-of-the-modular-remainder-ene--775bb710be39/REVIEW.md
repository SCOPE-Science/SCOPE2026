# Review of the modular remainder-energy variance theorem

**Correctness — PASS.** The central arithmetic step is conditional independence after separating the common residue modulo \(\gcd(a,b)\), which gives the exact covariance. Summing over modulus pairs and using the Jordan divisor convolution gives the exact variance; summatory \(J_2\) and square-subsequence Borel–Cantelli prove the cubic asymptotic and Haar almost-sure law. The included standard-library checker verified 12 complete periods, 900 pair covariances, 1200 divisor convolutions and 126 comparisons of variance sums. Its checks are finite corroboration rather than the proof of infinite statements.

**Originality — PASS, with qualification.** The complete available text of En-naoui's 2025 introduction gives periodicity and lists statistical distribution as a future direction, without the covariance/moment result. Kaltenböck–Kiuchi–Saad Eddin–Ueda's full accessible gcd-sum paper concerns distinct weighted triangular averages. Statement- and implication-level searches did not reveal the claimed combination. A classical general theorem might still imply part or all of the cubic constant, and independently finding all equivalent formulations is not guaranteed.

**Mathematical value — PASS.** The problem is naturally motivated by the published distributional question; an exact covariance law and quantified concentration explain the collective effect of highly correlated remainders. The almost-sure result further clarifies the correct compatible-residue probabilistic model.

The result does not prove a central limit theorem, a short-interval distribution law, or behavior as \(m\to\infty\) with a fixed ordinary input \(n\). No independent scientific priority review has occurred.

Self-review: passed. Independent audit: not yet performed.
