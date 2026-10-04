# Same-model review

## Correctness
PASS. Before the first rejection, the published SAFFRON formula contains only the initial-wealth term, and the gamma index is exactly one plus the number of prior noncandidates. This yields a three-outcome renewal at each stage. Summing the self-loop gives the stated rejection and advance hazards, and multiplying stage-survival probabilities gives the exact infinite product. The uncapped envelope follows from elementary product and logarithm inequalities. An exact-rational verifier independently matches exhaustive short-horizon enumeration, dynamic programming, and the stage factorization.

## Originality
PASS with a recorded residual risk. The full SAFFRON algorithm/proof/simulation sections inspected state the threshold recursion, FDR control, and power dependence on \(\lambda\) and \(\gamma\), but not the complete-null first-rejection distribution, attained-FDR product, or gamma concentration/diffusion envelope. Fisher's later SAFFRON paper extends dependence conditions rather than evaluating this global-null law. The closest conceptual source, the exhaustive ADDIS FWER paper, explicitly performs exact global-null calculations to construct an FWER-exhausting ADDIS procedure; it does not state the original-SAFFRON product or its gamma envelope. Targeted repository and web searches for complete-null, first-rejection, product, and no-rejection formulations did not locate an equivalent statement. A residual risk remains that older alpha-investing or renewal-process literature contains the same specialization under different notation.

## Value
PASS. The result converts a qualitative notion of online-testing conservatism into an exact calibration law. It separates the roles of candidate filtering and initial-wealth allocation, shows how the gamma shape alone controls the uncapped complete-null attained FDR, and gives a tight closure envelope. This provides a finite-parameter benchmark for implementations and makes explicit that, under the standard initial-wealth constraint, complete-null SAFFRON cannot exhaust its nominal FDR level.

## Closest literature and limitations
The foundational source is Ramdas et al. (2018), whose constant-\(\lambda\) formula is the exact starting point. Fischer et al. (2024) is closest in using exact global-null online-error probabilities, but for an exhaustive ADDIS FWER construction. Fisher (2024) is closest on later SAFFRON FDR theory, focusing on dependence and stopping. The finding is deliberately limited to independent uniform p-values and the first-rejection event under the complete null.

Same-model review: passed. Independent audit: not yet performed.
