# Review: Exact complete-null FWER law for ADDIS-Spending

## Correctness
**PASS.** Under the stated exact-uniform complete-null assumptions, the ADDIS-Spending state is constant until either a rejection occurs with probability \(a_j=\alpha(\tau-\lambda)\gamma_j\) or a middle-zone p-value advances the state with probability \(q=\tau-\lambda\). The containment condition \(a_j\le\lambda\) makes these exit events disjoint. Conditioning on the first exit gives state-survival probability \((1+\alpha\gamma_j)^{-1}\); multiplying over states and taking the decreasing-event limit yields the exact infinite-product FWER. The product convergence, sharp envelope, and \(\sinh\) specialization follow from elementary inequalities and Euler's product. The checker reproduces the finite recursion and numerical specialization.

Risk: the formula changes if a rejection level exceeds \(\lambda\), so the containment hypothesis is kept explicit throughout.

## Originality
**PASS.** The primary Tian--Ramdas source defines ADDIS-Spending and proves control, but the inspected full text does not state the exact complete-null product law. Fischer's exhaustive-ADDIS paper is the closest comparison: it explicitly says ordinary ADDIS procedures are conservative and constructs a uniform improvement, while also explaining why the history-dependent rejection events prevent a direct ordinary Sidak factorization. Its global-null exactness result concerns the modified exhaustive procedure, not the baseline ADDIS-Spending FWER. Targeted literature and published-finding corpus searches for the product formula, a \(1-\prod(1+\alpha\gamma_j)^{-1}\) representation, and the inverse-square \(\sinh\) form returned no covering result.

Risk: an equivalent identity may exist in supplementary notes not indexed by the searched sources. This residual risk does not overturn the inspected statement-level comparisons.

## Value
**PASS.** The later literature identifies conservatism of ordinary ADDIS as the reason a uniform improvement is possible. The exact formula measures that conservatism, proves that the complete-null FWER is independent of the discard/candidate thresholds in the stated regime, gives the sharp range over all spending schedules, and supplies a closed-form benchmark for a published inverse-square schedule. This is a natural calibration fact for an established online FWER method rather than an arbitrary parameter slice.

Risk: the result is a type-I-error calibration theorem only; it does not establish a power improvement or replace exhaustive ADDIS.

Same-model review: passed. Independent audit: not yet performed.
