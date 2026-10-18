# Scientific review

## Correctness — PASS

For a length-\(n\) iid word, an unbordered boundary block \(u\) of length \(\ell\le n/2\) is **exactly** its shortest border, independent of the central word. The disjoint boundary events have probabilities \(\prod_i\pi_{u_i}^2\), giving the stated exact conditional renewal recurrence and, by formal series algebra, its bivariate probability generating function. The multivariate unbordered-word recurrence is justified by central-letter insertion: odd lengths create no new short border, and the even-length exceptional insertions are precisely squares \(uu\) with unbordered \(u\). The subtraction weight is therefore \(U_m(\mathbf w^{\odot2})\), rather than a uniform-alphabet substitution.

The infinite two-stream construction provides genuine independent residual tails after each successful shortest match. A mismatch event of positive probability proves the total successful-match mass \(h\) is strictly below one. Taking \(\alpha>1\) with \(B(\alpha)<1\) produces an exponential moment for total peeled length and hence a coupling bound of \((1-h)/(1-B(\alpha))\alpha^{-n}\). The weighted exponential moment with a polynomial factor in successful-step count proves exponential convergence of each fixed positive integer moment; the geometric formulas then yield the mean and variance. Boundary cases (empty center, positive nonempty center, overlapping candidate borders) are addressed explicitly.

`verify.py` independently enumerates words, reconstructs exact rational width laws and the unbordered kernel for binary and ternary alphabets, and tests weighted unbordered recurrences with independent weights. Computation corroborates the proof without being substituted for it. No unproved all-length enumeration or numerical extrapolation is used.

## Originality — PASS, with residual risk

Goto, I, Bannai, and Inenaga (arXiv:1806.00198, Section 3 and Theorem 1) establish the **deterministic greedy factorization**, not a biased random-source distribution. Gabrić and Shallit (arXiv:2302.13147, Theorem 2) establish complete largest-factorization width counts **under uniform sampling**, and Theorem 4 establishes existence of the corresponding uniform limiting mean. These stronger uniform counts subsume every uniform specialization of the weighted law, and this work does not claim uniform counts or their consequences as original. Their statements do not determine the nonuniform word-weight sums, exact multivariate kernel, or exponential coupling bound. Holub and Shallit (arXiv:1509.05240, Sections 2–5) determine period and longest-border statistics for uniformly sampled words, not the iterative shortest-border peeling law.

Targeted comparisons were made against these primary full texts, research-record results, and accessible overlapping claims. No equivalent nonuniform full-width law or stronger coverage was identified. A source not indexed by these searches could still contain it, particularly as a weighted renewal or autocorrelation formulation. Absence of a search hit is not a uniqueness proof. Scientific priority has not been independently assessed.

## Mathematical value — PASS

The source model matters: unequal letter masses change the weight of each unbordered factor and invalidate direct substitution of a noninteger alphabet size into the published uniform recurrence. The finding supplies an exact finite-length bivariate distribution, a nontrivial multivariate unbordered recurrence involving squared letter weights, an infinite limiting law with a quantified exponential rate in total variation, all moment limits, and certified numerical evaluation for **every** strictly biased full-support iid source. These are mathematically natural refinements of the known block-palindrome decomposition invariant, not a selected small input or isolated arithmetic gain. They give a complete distributional answer in a probability model not covered by the closest primary theorem.

## Closest literature, boundaries and risks

The closest antecedents are Goto et al., *Block Palindromes: A New Generalization of Palindromes* (2018), Gabrić–Shallit, *Smallest and Largest Block Palindrome Factorizations* (2023), and Holub–Shallit, *Periods and Borders of Random Words* (2015/2016). The theorem assumes independent letters and positive nonuniform masses, and does not settle the power-series conjecture in the 2023 paper or claim independent certification. Possible unseen biased-source or weighted-unbordered enumerations remain an originality risk.

Self-review: passed. Independent audit: not yet performed.
