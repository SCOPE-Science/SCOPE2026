# Review of sharp unconditional consensus threshold

## Correctness

**PASS.** The original model's exclusion of self-action and inclusion of self-opinion are maintained. The undelayed stochastic matrix has uniformly positive action-to-action and own-opinion-to-action coefficients. Every action receives positive two-step weight from every prior coordinate; this forces all actions strictly inside any nonvanishing limiting envelope. Repeatedly updated extreme opinions cannot remain at an envelope endpoint, hence the persistent extreme opinions are isolated leaders. Their cross-action differences sum to exactly \((1+\phi)D_\infty\), contradicting the confidence threshold. Complete-neighborhood entry and a primitive matrix yield geometric convergence. The exact two-agent equilibrium proves sharpness even at the endpoint. Rational checks reconstruct the key finite-dimensional identities. Scope and limits are given in RESULT.md.

## Originality

**PASS, narrowly scoped.** The full accessible arXiv paper [1] states in Theorem 3 and Remark 4 a finite-stabilization assumption that it cannot prove, and explicitly poses the confidence/decision threshold as future work. Here stabilization follows after proving global consensus above an exact worst-case threshold; the two-agent construction shows that the threshold cannot be lowered uniformly over all finite sizes. The earlier model article [2] gives experiments rather than this theorem. Classical opinion-only HK theorems [3] and general stochastic averaging theory do not directly imply the model-specific exact bound; a broader as-yet-unindexed consensus theorem remains a residual literature risk.

## Value

**PASS.** The primary source identifies parameter thresholds and finite graph stabilization as gaps. The result answers a natural worst-case version with an exact decision-weight law, proves the previously assumed stabilization under a checkable condition, includes equality, and supplies a sharp counterexample. These conditions delineate guaranteed social consensus from feasible persistent polarization without numerical phase diagrams.

## Closest literature and limitations

Source [1] was inspected in its full HTML form including equations, relevant lemmata, main convergence theorem, remarks, and conclusion. Source [2] was compared through accessible abstract/model description and sensitivity discussion. The analytical proof is restricted to full potential contact availability, homogeneous parameters and synchronous deterministic updates. The universal threshold does not classify every initial condition. Related search results do not establish exhaustive novelty; independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
