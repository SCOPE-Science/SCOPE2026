# Review: Corrected coexistence threshold in the Liu–Zhang delayed Ivlev example

## Correctness
**PASS.** The source equilibrium equations were reconstructed directly. The predator balance gives the printed \(x^*\) formula, and the prey balance gives the printed \(y^*\) formula. Since all factors multiplying \(1-x^*/K\) are positive, coexistence is equivalent to \(x^*<K\), which yields the source's own Proposition 3.1 threshold. Substitution gives \(132.923341652608\ldots\). The separate real-logarithm threshold is \(250.531764704813\ldots\), and direct substitution at \(\tau=250\) produces \(y^*<0\). The checker independently reproduces these arithmetic facts from the printed parameters.

## Originality
**PASS.** Exact DOI/title/parameter/threshold queries in published-finding corpus returned no matching correction. The motivating article was inspected at statement level: its general Proposition 3.1 contains the correct positivity criterion, but Section 4.1 prints the incompatible value \(\tau_c=250\) and then reports \(\tau_3=132.9233\). Searches for a corrigendum or published correction did not locate one. A closely related 2020 Beddington–DeAngelis article was inspected in full; it uses different equations and does not imply this correction. The stage-structured 2020 Ivlev paper is also a different model.

## Value
**PASS.** This is not a rounding discrepancy. The printed value creates an apparent interval of roughly \(117\) delay units in which the article describes a positive-equilibrium branch after the branch has already reached \(y^*=0\). Correcting the endpoint removes that inadmissible interval and aligns the equilibrium-existence statement with the article's own reported transcritical value, which materially changes the interpretation of the main Section 4.1 bifurcation diagram and stability narrative.

## Closest literature and limitations
The closest inspected same-author predecessor is the 2020 Beddington–DeAngelis delay model, which also discusses survival through a gestation delay and eventual predator extinction. Its equations, functional response, and equilibrium threshold differ. The 2020 stage-structured Ivlev paper contains a different state-space model with two delays. No equivalent correction was found in the inspected literature or published-finding corpus records. Search failure is not a proof of absolute novelty, and no independent audit has been performed.

Same-model review: passed. Independent audit: not yet performed.
