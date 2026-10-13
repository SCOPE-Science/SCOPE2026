# Scientific review

## Correctness: PASS

The exact conditional factorial-moment identity gives an invertible stationary recurrence with positive denominators, determines every joint presence moment and hence the entire stationary distribution. The covariance and flux follow by direct algebra and stationarity. Stirling's formula and a rigorously controlled improper logarithmic Riemann sum yield the critical rate for every fixed positive parameter. A positive derivative bound proves the strict exponential independence penalty. The independently constructed rational finite-state checker passed 280 exact assertions; numerical and finite checks are not used as universal proof.

## Originality: PASS, with priority risk

Cruciani--Dudeja, arXiv:2602.20705, analyze the model and a mean-field independence approximation; their inspected complete preprint does not supply the exact joint stationary law. Long, arXiv:2605.14511, proves a fixed-loss stationary-entry asymptotic and uses the balance identity credited in this work, but does not provide the critical varying-loss exponent. Attrill--Garoni, arXiv:2605.14206, study a different one-coupon update mechanism. Targeted mathematical-record searches covered stationary moment identities, coupon thinning, stationary entry flux, relevant equivalences and prior stronger claims; the closest entries address resets or static occupancy instead. A general thinning-immigration identity may be an unindexed equivalent and remains a genuine priority risk. Absence from searches is not proof of absolute novelty.

## Value: PASS

The proportional loss scale is a central regime in the motivating published research. The exact all-types stationary synchronization law and its strictly stronger-than-independent exponential rarity exhibit a structural dependence barrier that cannot be read off from stationary marginals. Complete finite-size joint inclusions and negative covariances support its usefulness for investigating synchronized collection and flux. This is not a theorem about hitting times or a Poisson process of entries.

## Verification and limits

`checker.py` independently solves exact finite Markov stationary systems, checks their joint-moment product, the negative covariance and the flux for sizes two through eight at four loss parameters. Universality rests on the written proof. Broader nonuniform arrivals, correlated losses, arbitrary varying loss regimes, and initial-empty first-hitting distributions are not claimed.

Self-review: passed. Independent audit: not yet performed.
