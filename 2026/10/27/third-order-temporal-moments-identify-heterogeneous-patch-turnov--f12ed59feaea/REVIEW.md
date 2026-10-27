# Scientific assessment

## Correctness — PASS

The conditional-expectation identity for a two-state continuous-time Markov chain gives exact exponential autocovariances. The Bernoulli-square identity gives exact third centered joint moments at three equally spaced times. Independence eliminates all mixed-index terms. The covariance Hankel matrix factors through an invertible Vandermonde matrix with strictly positive weights, hence is positive definite; its matrix pencil recovers every distinct decay. A second Vandermonde inverse using squared decays recovers each signed skew coefficient and therefore both positive transition rates. The two-patch example has equal means and entire covariance curves but distinct triple moments, and extra identical independent patches preserve this obstruction. Exact finite-state and rational-algebra checks in `verify.py` corroborate critical identities and an example but are not used to prove the universal theorem.

## Originality — PASS, subject to residual literature risk

The known general exponential-sum inversion is explicitly excluded from the novelty claim. The assessed contribution is the complete moment-order boundary for **aggregate** independent occupancy counts, including finite third-cumulant recovery of hidden colonization/extinction orientation and a sharp nonidentification example at second order. Royle–Kéry (2007) concerns patch-resolved dynamic occupancy modeling. Fukaya–Royle (2013), whose accessible article's introduction, models, simulations and discussion were examined, infers ecological transition matrices from gridpoint state observations, rather than aggregate count autocovariance and third moments. O'Cinneide (1991) studies superposed renewal event streams; only its abstract was accessible. Published mathematical records on two-time-law aliasing and paired reversible-chain covariance were compared: neither statement implies the finite third-order reconstruction here. Other signal-processing or factorial hidden-Markov literature could contain an equivalent unlocated specialization; this is a residual bibliographic risk, not a claim of globally certified novelty.

## Mathematical value — PASS

There is a real observational distinction between patch-resolved field records and aggregate occupancy time series. The theorem shows precisely when perfect aggregate temporal summaries can reconstruct the underlying colonization/extinction mechanism, identifies the moment order needed, and provides an explicit fixed finite collection of lags and inversion method. Its sharp two-patch obstruction prevents an incorrect conclusion from complete second-order agreement. The result is a structurally motivated inverse-identification theorem, not a renamed elementary formula or an arbitrary small numerical slice. The cost is restrictive independence, stationarity, distinct turnover and exact-measurement assumptions; practical statistical stability is not addressed.

## Principal limitations

No claim extends to dependent patches, heterogeneous measurement errors, nonstationary processes, equal turnover rates or finite-sample inference. The cited 1991 renewal-superposition article was not available beyond its abstract. Independent specialist bibliographic review remains necessary.

Self-review: passed. Independent audit: not yet performed.
