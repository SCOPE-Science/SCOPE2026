# Scientific review: dominant-prime stopping-order law

## Correctness — PASS

The theorem applies to every fixed denominator \(M\ge2\), where the exact-order density exists by Carvalho's congruence-class theorem. The published recurrence gives the rational divisor recursion (1) exactly, including its constant term and the exclusion of the divisor one after the first step. The prime-power generating function is taken directly from the published closed formula. The new induction shows that the rational functions for \(M\) and its largest prime-power divisor have **identical full principal parts**, not merely the same highest-order coefficient. The induction's cancellation uses the identity \(\sum_{d\mid m}\varphi(d)=m\) and a denominator that is nonzero at the dominant pole whenever \(m>1\). All other reciprocal-totient pole ratios are strictly smaller than the largest-prime ratio, giving an exponential remainder by partial fractions. Carvalho's density-one theorem justifies identifying the tail density by complementing finitely many exact-order classes.

The extracted standalone program directly recomputes the rational-function pole cancellations, exact recurrence, and independent finite orbit counts. All checks pass. Finite computations support but do not replace the unrestricted divisor-inductive proof.

## Originality — PASS (best-knowledge, subject to independent priority assessment)

The closest 2026 paper, Carvalho (arXiv:2605.21802v1), proves the exact-order recurrence, a closed prime-power formula, and total finite-order density one. It **does not** assert a sharp large-order asymptotic for composite denominators or establish cancellation of the *entire* dominant pole. The full relevant proof and consequences were read. Azevedo–Carvalho–Machiavelo (arXiv:1210.0042v1) proves the same counting recurrence for a **different rational map**, and thus its stated recurrence is an important antecedent. Its examined theorems and tables do not contain the dominant-prime full-principal-part identity or a corresponding exponential remainder. A result deduced by routine substitution of parameters would be covered; here the new proof has an independent nontrivial rational-function pole-cancellation step, making the comparison more than a relabeling of the original formula.

Searches of published mathematical records for the map, order-density asymptotics, dominant prime factor, and full-pole cancellation found no covering claim. One accessible earlier claim about this map studies least two-step entrance numerators for denominators twice an odd prime, not order-density tails. Other historical records were not all accessible. A different unpublished or unindexed analysis of the same rational recurrence could predate this result; the present originality assessment is not an independent certification.

## Mathematical value — PASS

The motivating problem is quantitative: the 2026 paper establishes that finite-order rationals have density one but gives no rate of decay for the remaining order-at-least-\(N\) population at a general composite denominator. The result supplies the **sharp exponential rate, exact polynomial factor, universal leading coefficient**, and the stronger full-principal-part cancellation with an exponentially smaller error. This answers what composite prime factors actually change and proves the unexpected fact that they leave the dominant profile unchanged. The distinction is mathematically substantive: an arbitrary recurrence determines every finite coefficient but does not by itself identify dominant singularities or rule out lower-order pole contamination. The result also offers a reusable singularity principle for other divisor recurrences and rational dynamical maps, without claiming to settle individual termination.

## Remaining scientific limits

The asymptotic is for fixed denominator; no uniform-in-\(M\) error constant or individual finite-order theorem is obtained. The published counting recurrence and prime-power special case are prior art, not novel contributions. Priority relative to unindexed recurrence-asymptotic work needs independent examination.

Self-review: passed. Independent audit: not yet performed.
