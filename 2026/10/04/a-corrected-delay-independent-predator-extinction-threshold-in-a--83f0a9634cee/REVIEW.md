# Same-model review

## Correctness

PASS. The source's asserted adult-predator differential inequality is directly contradicted by its exact equation because the delayed juvenile maturation term is positive and cannot be discarded. The corrected theorem follows from logistic control of the prey, an eventual linear upper bound on juvenile recruitment, and a Lyapunov-Krasovskii functional whose integral term cancels the delayed maturation flux exactly. The strict threshold makes both predator coefficients negative; boundedness plus Barbalat's lemma yields predator extinction, and scalar logistic comparison yields convergence of the prey.

## Originality

PASS. Reproduction-number threshold methods for stage-structured predator-prey systems are established prior art. The closest fully inspected Crowley-Martin predecessor proves extinction/permanence in a different maturation model, so the general idea is not claimed as new. The surviving contribution is the correction of the exact Kong-Shao equations, the source-parameter contradiction, and the explicit delay-independent threshold for that three-variable system. Exact DOI, title, extinction, adult-limit, and parameter-alias searches found no published correction of the source.

## Value

PASS. The flawed calculation concerns extinction of both predator stages, a biologically central qualitative outcome. The source's own stable coexistence example conflicts with its printed adult-predator limiting formula. The replacement theorem supplies a concrete condition that is mathematically valid for arbitrary delays and is less restrictive than the source's stated sufficient condition, so it changes what can rigorously be concluded from the model rather than merely repairing notation.

## Closest literature and limitations

Li, Sun, and Liu, DOI 10.3934/dcdsb.2022177, give the closest threshold result for a stage-structured Crowley-Martin model, but their maturation mechanism uses delayed recruitment with an explicit juvenile survival factor rather than the explicit juvenile compartment and delayed maturation input corrected here. Liu and Beretta, DOI 10.1137/050630003, provide broader stage-structured threshold precedent with a different functional response.

The theorem proves only the strict sufficient regime \(\mathcal R_P<1\). It does not assert sharpness at the boundary or re-audit the source's later bifurcation catalogue.

Same-model review: passed. Independent audit: not yet performed.
