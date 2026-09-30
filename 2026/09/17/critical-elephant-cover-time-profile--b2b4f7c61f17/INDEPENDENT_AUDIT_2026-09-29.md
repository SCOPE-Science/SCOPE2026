# Independent Audit — 2026/09/17/critical-elephant-cover-time-profile--b2b4f7c61f17

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `952634226921da598ce3bf1c3d0ad721c78ad175`
- Disposition: **PASSED**

## Correctness

**PASS** — The rare-path argument is coherent and the load-bearing cited estimates were independently checked in the full Qin preprint. Qin's Proposition 3.5 gives the required integrable envelope, Corollary 3.6 converts a.e. tail limits to exact mean asymptotics, Lemma 3.9 gives precisely the conditional Brownian-clock error bound used here, and Question 1 asks for the critical normalized mean constant. In the new Brownian lemma, conditioning on W_H=y, reversing the bridge and exponentially damping it removes both the bridge correction and deterministic drift uniformly for x_H=o(sqrt(H)); the event itself restricts y to a fixed compact interval, so the terminal density contributes 1/sqrt(2*pi*H). In the ERW transfer, ell=(log n)^16 makes the clock, coefficient and mesh errors o(1) outside o(H^-1/2), while 1/(L a_k) matches sqrt(t) exp(-u_k/2) and H~2 log L. This gives the stated 1/(2 sqrt(pi)) profiles. Tonelli then yields the inverse-square Brownian formulas and Qin's envelope justifies dominated convergence for the means.

## Originality

**PASS** — Qin's v1, submitted 2026-09-15, proves only Theta(L^2/sqrt(log L)) at p=3/4 and explicitly poses existence of the exact normalized mean constant as Question 1, observing that an a.e. L^2-time tail limit would suffice. The submitted record supplies exactly that missing tail profile through a new endpoint-mixture/reversed-Brownian-bridge asymptotic and then solves the stated question. Searches through the intervening literature found no matching critical Brownian-profile or exact-mean theorem.

## Scientific value

**PASS** — The result resolves an explicit open question in a current preprint and identifies why the mean is governed by rare L^2-scale paths rather than the usual critical fluctuation limit, whose limiting law has infinite mean. The Brownian path-integral representation also supplies a reusable object for numerical evaluation and possible refinements of critical ERW cover and exit statistics.

## Sources

- Cover times and ranges of elephant random walks (Shuo Qin): https://arxiv.org/abs/2609.17264 — Full text checked: Proposition 3.5, Corollary 3.6, Lemma 3.9 and Question 1 match the inputs and open problem used by the record.
- Estimates on Escape Times for the Elephant Random Walk (Morgan André; Leonel Zuaznábar): https://arxiv.org/abs/2602.18953 — Nearby escape-time results give exact diffusive-regime means and tail bounds, not the p=3/4 exact constant.
- How often does a critical elephant random walk return to origin (Zheng Fang): https://doi.org/10.1214/24-ECP636 — Brownian-embedding background used by Qin; not a source for the critical cover-time profile.

## Limitations

- The Brownian constants are proved finite and positive but no closed form or certified numerical value is supplied.
- Tail convergence is only claimed at continuity points, which is enough for the mean by the verified uniform-integrability envelope.
- The theorem is specific to the classical one-dimensional ERW at p=3/4.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first. Oxford Download was used only where version-specific or full-text source verification remained unavailable through the open-access retrieval path.
