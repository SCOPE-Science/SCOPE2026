# Review

## Correctness

PASS. On a finite target chain, forward confluence can be tested against the largest point of each nonempty successor fiber. A nonempty fiber forces every later source fiber to be nonempty, and applying confluence to its maximum forces weakly increasing maxima. Conversely, the later maximum witnesses confluence for every element of an earlier fiber.

For fixed nonempty-row count \(k\), the source suffix is forced. A row with maximum \(m\) has exactly \(2^{m-1}\) choices, so weakly increasing maxima give the complete homogeneous polynomial \(h_k(1,2,\ldots,2^{n-1})\), equal to the Gaussian coefficient \(\begin{bmatrix}n+k-1\\k\end{bmatrix}_2\). The asymptotic follows from the Gaussian product formula, with the \(k=n\) term dominant and all lower-\(k\) terms exponentially smaller after normalization.

Exhaustive relation-by-relation replay through four worlds agrees with the structural criterion and the closed count.

## Originality

PASS. The 2026 primary source states the forward-confluence condition, studies finite proof search, and proves an \(\mathsf{EXPSPACE}\) upper bound. The original FIK paper proves finite countermodel extraction. Neither checked source gives a chain normal form, an exact chain-frame census, or a Gaussian-binomial expression.

Targeted semantic and literature searches for forward-confluent chain frames, Gaussian-binomial counts, and FIK relation enumeration found no equivalent statement. The closest prior chain-relation result in the existing record has different hypotheses and implications: it requires total nonempty rows with strict growth of both minima and maxima.

## Value

PASS. Finite countermodel generation and proof-search complexity are central in the recent FIK literature. Chains are the canonical first family of finite intuitionistic preorders, so their exact admissible-relation search space is a natural baseline rather than an arbitrary slice. The result reduces a relational confluence condition to a one-dimensional row invariant, gives exact counts at every size, and quantifies asymptotically how restrictive forward confluence is among all modal relations.

## Closest literature and limitations

Gao--Olivetti (2026) is the direct recent source for the FIK frame condition and complexity motivation. Balbiani--Gao--Gencer--Olivetti (2024) is the original FIK source and gives finite countermodels.

The theorem does not extend its closed formula to branching intuitionistic preorders and does not turn the frame count into a decision-problem lower bound.

Same-model review: passed. Independent audit: not yet performed.
