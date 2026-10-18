# Scientific review: voter-diffusion reset onset

## Correctness

PASS. The Green-operator moment recursion supplies analytic Taylor coefficients and finite exponential moments. The uniqueness proof hinges on the exact sign-change structure of \(K'(m)=\operatorname{artanh}(m)[5-4m\operatorname{artanh}(m)]\), not an enumeration. Exact fixed-point integer interval arithmetic with analytically bounded tails verifies the narrow root bracket, positive second restart coefficient, and positive finite local slope. The conclusion is carefully restricted to a local stationary minimizer branch, not a global optimizer or an unproved finite-population transfer.

## Originality

PASS under inspected-source and recovered-record comparisons, with a material general-theory qualification. Argany Herrera et al. (arXiv:2609.39858, sections on all-to-all voter first-passage properties) provide the reset model, report numerical critical magnetization, and expressly leave the scaling derivation open. Pal and Prasad's 2019 *Landau-like expansion* (arXiv:1904.07590, sections on second-order restart transitions and moment coefficients) already gives the generic exponent-one mechanism. The distinctive mathematical statement here is the unique critical location for the specific Wright–Fisher voter diffusion, a certified positive quadratic coefficient, and the resulting explicit local slope. An inaccessible full examination of earlier interval-restart literature remains a historical-priority risk. No broad novelty is attributed to the general restart expansion.

## Mathematical value

PASS. The concrete model-specific transition and its certified slope analytically sharpen a current paper's numerical \(\approx0.630\) threshold and address its stated open scaling problem. The uniqueness proof and certified nondegeneracy distinguish the result from simply invoking a known generic exponent. It provides a quantitative benchmark for voter consensus under rare system-wide resets. It is not a statement about global rate optimization.

## Limitations

The continuum scaling and local nature of the optimum are essential. Historical-priority risk persists for broader first-passage and Wright–Fisher restart literature. Independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
