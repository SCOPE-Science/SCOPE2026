# Mathematical review

## Correctness — PASS

Exact Feynman--Kac transform and Bromwich inversion are established, with a moving positive saddle for the critical drift. A strictly positive real-part gap on the contour, the explicit second derivative, and Gaussian localization give a uniform sharp probability formula. Comparing fixed prefixes retains the order-one budget shift, and the Cameron--Martin drift factors cancel exactly; Scheffé's lemma upgrades convergence to total variation. The proof depends on genuine analytic contour estimates, not finite sampling. The attached standard-library checker verifies representative identities and the root classification.

## Originality — PASS, qualified

Aurzada--Dutta--Wiegand (arXiv:2610.12354v1) explicitly present the critical \(\mu_T\sim c\sqrt T\) regime as an open question and prove a different (subcritical) regime; the new moving-saddle equation produces a new limiting rate for \(c>0\). Their exact transform is used as a known lemma, not misrepresented as new. Comparisons with accessible mathematical literature did not identify the same conclusion. Aurzada--Lifshits--Schickentanz (arXiv:2312.12982) concerns zero drift. Schmidt (arXiv:2608.19744) is potentially relevant but only its abstract was accessible; this uncertainty remains and no whole-document noncoverage is claimed.

## Mathematical value — PASS

Determines the sharp answer to an explicit parameter-critical question in a recently published probability study and exhibits a transition from drift-independent to drift-dependent conditioned dynamics. The cubic-root confinement law and matching sharp probability asymptotic quantify the critical boundary rather than giving an isolated calculation.

## Residual risk and limits

Related general path-ensemble theory may imply an equivalent result under another formulation; full comparison with one 2026 preprint was inaccessible. The proof covers fixed initial conditions, a hard quadratic constraint, finite drift-squared scaling and fixed time windows, not arbitrarily growing windows or arbitrary confining potentials.

Self-review: passed. Independent audit: not yet performed.
