# Self-review

## Correctness — PASS

The event \(\{B_a\cap B_b\}\) conditioned on source \(s\) requires exactly the union of three tree paths; this union is the monitor path and the attachment branch. The proof constructs and independently verifies the product-path kernel inverse \(Q\), checks its action on the source-to-path profile separately on and off the monitor path, and uses \(b=K\pi\). The endpoint and interior coefficients are strictly positive because a simple path has at most two incident path edges at each vertex. An exact-rational exhaustive checker independently compared the joint event to the identity over 2,712 tree–pair instances. No finite enumeration is used as an infinite proof.

## Originality — PASS, with risk

The weighted product-distance matrix inverse is known from Bapat–Sivasubramanian (2012), Theorem 2.2, and is expressly excluded from the new contribution; Bapat–Lal–Pati (2006) supplies the homogeneous precursor. The finding instead identifies the probabilistic joint-infection kernel, proves its path-supported inverse image, and eliminates the arbitrary outbreak-source prior. Antulov-Fantulin et al. (2013) infer a source from a partially observed single realization; Sharkey et al. (2013) study pair-time evolution in continuous-time SIR. Searches and inspected primary content did not establish the stated joint-ever-infected/marginal-ever-infected path identity. Equivalent identities in tree reliability or epidemic-observation literature cannot be definitively excluded.

## Value — PASS

Joint infection monitoring is normally a separate pairwise statistic; this result determines all \(\binom{|V|}{2}\) pairwise detection probabilities from only \(|V|\) individual probabilities, even for heterogeneous transmission rates and a completely unknown initial-source distribution. It also gives exact model-consistency checks, a simple neighboring-monitor formula, and an interpretable no-off-path-data principle. This is a concrete structural fact, not a substituted instance of a graph inverse: the latter does not by itself identify the joint-event kernel and localized observable.

## Boundaries and independent assessment

Exact population probabilities and the independent single-source bond model are essential. The result is not a general epidemic SIR closure, multi-source theorem, or finite-sample estimator. The proof is internally checked, not independently validated.

Self-review: passed. Independent audit: not yet performed.
