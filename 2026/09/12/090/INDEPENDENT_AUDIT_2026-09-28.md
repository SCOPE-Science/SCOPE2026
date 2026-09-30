# Independent Audit — 2026/09/12/090

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `4c8b430ec755cf887fc9f35e218c9f9c5f8935ea`  
**Disposition:** **PASSED**

## Correctness
**Verdict:** PASS  
The subaction argument is mathematically decisive. With beta=1/2, F=beta-phi+u∘T-u, invariance gives ∫phi dmu=1/2-∫F dmu. The supplied exact-rational verifier reconstructs the degree-48 algebraization R from the degree-12 rational trigonometric u, checks R=(t^2-3)^2 S, uses exact Sturm sequences to certify S>0 (indeed S>=3/200), and separately checks the omitted tangent-chart point x=1/2. Thus F>=0 with zeros exactly at 1/3 and 2/3. Since the period-2 orbit attains average 1/2, beta=1/2; any maximizing invariant measure is supported on that orbit, whose only invariant probability is the orbit measure. I independently checked the proof logic, the elementary orbit average, and the verifier's exact-arithmetic structure; no floating-point step is load-bearing.

## Originality
**Verdict:** PASS  
The closest accessible source, Gao's work on calibrated sub-actions and Sturmian optimization, generalizes Bousch's translated-cosine family for the doubling map. It does not state this explicit two-harmonic potential, its rational degree-12 subaction, or the exact period-2 certificate. More recent periodic-optimization results are generic/typicality statements rather than this exact optimizer computation. The contribution is therefore a concrete certified instance outside the cited one-parameter cosine-translation family, not merely a restatement of the general theory.

## Scientific value
**Verdict:** PASS  
An exact, reproducible maximizing-measure certificate for a nontrivial analytic two-harmonic potential is useful in ergodic optimization: it resolves the posed period-2 versus period-7 dichotomy and supplies a checkable subaction/positivity certificate rather than a periodic-orbit census alone.

## Literature comparison
- https://arxiv.org/abs/2105.10767 — Generalizes Bousch's translated-cosine Sturmian optimization for the doubling map; does not state the audited two-harmonic certificate.
- https://arxiv.org/abs/2501.10949 — Generic/typical periodic optimization context, not the exact potential or exact subaction used here.

## Independent checks
- Checked phi(1/3)+phi(2/3)=1 exactly, so the O2 average is 1/2.
- Inspected the exact-rational verifier: it reconstructs R from u, checks the (t^2-3)^2 factor, applies exact Sturm sequences to S and S-3/200, and separately handles x=1/2.
- Confirmed current record tree SHA equals the assigned source-tree SHA at the checked commit; no GitHub writes were made.

## Limitations
- The audit compared the explicit claim against the cited translated-cosine/generic optimization literature; it does not assert an exhaustive theorem that no unindexed source contains the same numerical potential.
- The exact rational verifier was inspected as evidence; the audit independently reconstructed the proof logic but did not rerun the repository script in a cloned checkout.

## Repository action
This audit is a guarded change-set only. No GitHub write was performed by the audit chat.
