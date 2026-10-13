# Scientific review: rare-occupancy revisit allocation

## Correctness — PASS

The finite-history likelihood and Fisher information are stated with all occupancy, detection, independence, and per-visit-cost assumptions. The missing-information identity follows from the variance decomposition for the Bernoulli latent occupancy indicator and was also reconstructed by direct exact-fraction summation. For every \(0<f<p<1\), the Bernoulli log likelihood ratio has a strictly positive finite mean \(d\). Concentration above the threshold yields almost complete information; a positive fractional moment gives a **uniform** exponentially small information bound below the threshold; the complete-data Fisher bound controls all higher allocations. These three regimes imply both claimed limits for every maximizing sequence, not merely for a chosen approximate sequence. At \(f=0\), reduction to any-detection gives exact Fisher information and strict small-\(\psi\) optimality of one visit. The reproducibility script reports 72 exact identity checks, 84 exact boundary checks and four finite illustrative calculations; no finite simulation is used as a proof of the limits.

## Originality — PASS, with stated residual risk

Royle and Link (2006) establish the two-state binomial-mixture occupancy likelihood, not the calibrated-detection large-budget rare-occupancy optimum. MacKenzie and Royle (2005) derive visit-allocation advice for standard occupancy without false positives, with nuisance detection parameters. Clement (2016) provides numerical fixed-parameter optimal survey counts with false positives, including a Royle–Link regime and fixed occupancy levels 0.2, 0.5, and 0.8; its nuisance-parameter estimation changes the Fisher criterion. The inspected primary articles do not imply the joint sharp conclusions \(k_\psi\sim\log(1/\psi)/d\), \(\max J_k\sim d/[\psi\log(1/\psi)]\), and the contrast with uniquely optimal one visit when \(f=0\) under known detection probabilities. Related published mathematical records address different identification, discovery, or probability-law problems. This is not a claim of certified global priority: a specialized binary-mixture optimal-design or sequential-information result may give equivalent coverage, and published search is not exhaustive.

## Value — PASS

Under controlled false-positive misclassification, the best use of visits for an *extremely rare* occupied site has a qualitatively different limit from the false-positive-free case. The precise rate and coefficient quantify the ecological trade-off between collecting enough within-site evidence to distinguish rare genuine occupancy from frequent erroneous detections, and maintaining coverage of many sites. The KL-divergence constant is an interpretable parameter-sensitive survey-design benchmark. The precise invariant is not an arbitrary count or a routine special case of the already published numerical tables. It is restricted to perfectly calibrated detection probabilities, equal marginal costs, fixed-repeat designs, a large-budget Fisher-information objective, and the order of limits specified in the theorem.

## Limits of review

Proof reconstruction and separate direct computational checks used only the displayed finite model; the two asymptotic limits are mathematical, not experimental, conclusions. The literature comparison inspected the original occupancy mixture, classical design guidance, and the full relevant design-methods article. Equivalent specialized information-theoretic optimal-block-design literature remains a concrete residual risk. No independent external review or empirical ecological validation was conducted.

Self-review: passed. Independent audit: not yet performed.
