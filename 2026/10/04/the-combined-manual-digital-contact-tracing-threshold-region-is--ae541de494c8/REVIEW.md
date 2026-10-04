# Same-model review

## Correctness — PASS
The proof uses the exact combined-model assumptions from Britton and Zhang: a common rate-\(\beta\) potential infection process, independent app marks, independent manual-tracing marks, spontaneous recovery and diagnosis clocks, and instantaneous recursive tracing through infected contacts including those already naturally recovered. Coordinatewise larger \((p,\pi)\) can only add traceable edges. The earliest-discrepant-birth argument shows that the stronger-tracing process cannot realize an infection absent from the weaker-tracing process. The source independently supplies the threshold equivalence between survival and \(R_{\mathrm{DM}}>1\). No finite experiment is used as the infinite proof.

## Originality — PASS
The primary source is the closest possible comparison and explicitly states that its numerically observed monotone \(R_{\mathrm{DM}}=1\) curve lacks a proof, while also documenting non-monotonicity of \(R_{\mathrm{DM}}\) itself. Searches covering monotone-critical-curve aliases, survival/coupling language, manual/digital combinations, and branching-process tracing did not locate a covering theorem. The closest own-ledger contact-tracing result concerns a different pairwise/triplewise mean-field model. The related Zhang–Britton network SEIR paper uses delayed, one-step, forward-only tracing and reports numerical rather than theorem-level combined monotonicity. A residual risk remains that a general tracing-monotonicity principle exists in literature not retrieved here; no inspected source states this source-specific result.

## Value — PASS
This resolves an explicit open structural point in a recent primary-92D30 paper. It separates a useful threshold-order law from the misleading stronger assertion that the component reproduction number itself must decrease. The result implies that the control region is upward closed and that increasing one tracing mechanism can never require increasing the other merely to remain subcritical, even in parameter regimes where noncritical contours of \(R_{\mathrm{DM}}\) bend non-monotonically.

## Closest literature and limitations
The direct predecessor is Britton and Zhang, DOI 10.1017/apr.2025.15. Zhang and Britton, arXiv:2402.13392 / DOI 10.1016/j.mbs.2024.109231, studies a different delayed one-step network model. Ball–Knock–O'Neill and Barlow study other tracing branching processes. The present theorem does not cover delayed tracing, imperfect digital registration, fatigue, structured-contact changes, late-epidemic susceptible depletion, strictness, or value monotonicity of \(R_{\mathrm{DM}}\).

Same-model review: passed. Independent audit: not yet performed.
