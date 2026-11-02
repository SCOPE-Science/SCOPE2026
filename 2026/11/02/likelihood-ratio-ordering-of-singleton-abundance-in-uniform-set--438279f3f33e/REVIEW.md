# Scientific review: singleton abundance and block-count total positivity

## Correctness — PASS

The joint count law is obtained by choosing singleton labels and partitioning the rest into blocks of size at least two. The essential adjacent minor is exactly \(A(N,r)A(N-1,r)-A(N,r+1)A(N-1,r-1)\). The Bóna–Mező recurrence splits it into (i) a Newton inequality term and (ii) a positive cross-product from the likelihood-ratio increase of the nonsingleton block count. The latter follows by matching Bóna–Mező's interlacing roots to Bernoulli success parameters and applying the elementary log-concave Poisson-binomial convolution lemma. Infeasible cells and the \(N\le3\) boundaries are handled separately; the interval support allows passage from adjacent minors to all minors. The finite integer verifier passed 467,463 assertions. The proof's use of the published interlacing theorem and its reliance on standard Newton/log-concavity are explicit.

**Remaining correctness risk:** The published interlacing theorem is assumed as a primary theorem rather than independently re-proved; this is acceptable mathematical dependence, not finite computation treated as proof. The weighted extension requires strictly positive weight for every feasible total block count.

## Originality — PASS (qualified)

Timashev (2003) covers fixed-total-block singleton and fixed-size-block counts as well as asymptotic laws. Bóna–Mező (2007) provides the exact nonsingleton partition recurrence and interlacing of the block-count polynomials. Neither inspected theorem states or dominates the cross-stratum finite-sample TP\(_2\) claim; obtaining it requires the nontrivial adjacent-minor decomposition and Bernoulli likelihood-ratio comparison. Pitman's set-partition framework is broader probabilistic background. The closest searched mathematical record, *Block-size counts switch covariance sign at the Lambert-W scale*, concerns an unconditional covariance versus block size, not finite-sample conditional likelihood-ratio order in the total block count. The checked historical archive includes separate results about local singleton-block correlations and block-count covariances, but no matching TP\(_2\) statement.

**Residual priority risks:** The 2003 Russian original was analyzed through its mathematical statements and available text rather than an independently verified complete English translation. Classical total-positivity and occupancy literature could contain an implicit equivalent not indexed by the exact vocabulary. No universal originality certification is asserted.

## Mathematical value — PASS

Fixed-block-count set partitions are a natural model for clustered sampling and occupancy conditioned on richness. The theorem promotes known marginal and fixed-size count formulae into a uniform all-threshold, all-increasing-transform stochastic dependence law. It also applies simultaneously to arbitrary positive Gibbs tilts based on the number of blocks, an entire family of measures. The exact finite-sample TP\(_2\) property is substantially stronger than an isolated covariance or a routine recomputation of Stirling numbers; the interlacing-to-minor synthesis supplies a reusable structural mechanism. No wider theorem for arbitrary block sizes is claimed.

## Source comparison and limits

Checked primary texts: Bóna–Mező, arXiv:0705.2734 (theorem/recurrence); Timashev, DOI:10.4213/dm201 (joint count/asymptotics); Pitman, *Some Probabilistic Aspects of Set Partitions* (probability representation). Additional published abstracts and semantic database results were checked for conditional total positivity and likelihood-ratio aliases. All numerical checks are finite. No independent audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
