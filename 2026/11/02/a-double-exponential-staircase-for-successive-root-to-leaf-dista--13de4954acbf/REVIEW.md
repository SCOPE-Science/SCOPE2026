# Scientific review

## Correctness — PASS

The binary Kesten spine has precisely one independent ordinary zero-or-two Galton–Watson offspine subtree per depth. The exact leaf-count generating polynomials \(f_0=(1+z)/2\), \(f_h=(z+f_{h-1}^2)/2\) have zero coefficients \(a_h=2^{-(2^{h+1}-1)}\). For at most \(m\) visible leaves, positive-count support sets have size at most \(m\). The unique maximum exponential weight occurs when the first \(m\) offspine subtrees each contribute exactly one leaf. Every competing support loses at least \(2^{r-m}\) in binary-log weight, while the single-support one-leaf probabilities approach \(1/2\) at the required rate. This proves both the exact leading constant and explicit error inequality, not just a double-log order. An exhaustive exact-rational checker verifies small-radius recurrences, bounds and gap arithmetic. Its finite assertions are not the infinite proof. The finite conditioned-tree statement uses only fixed-radius cylinder-event convergence, not an unproved uniform limit.

## Originality — PASS (historical priority provisional)

Maciá–Stufler (arXiv:2606.15339) completely covers the \(m=0\) nearest-leaf tail, including the exact binary double-exponential expression, and its general root local-limit theory. That known result is excluded from the assessed new contribution. The checked §§4.2, 4.5 and 4.6 do not provide distributions of the second or later closest leaves, fixed-multiplicity generating functions, the relative-error staircase or the conditional spine-shape concentration. Maciá (arXiv:2205.10645) likewise treats first-nearest distance. Searches of mathematical research records, prior accessible claims and external literature for closest/second/kth leaf, protection, Kesten binary spine and shallow leaf counts found no claim that implies the fixed-\(m\ge1\) theorem. Searches do not prove unique historical priority; older implicit branching/small-ball formulations remain possible.

## Mathematical value — PASS

One leaf-avoidance probabilities cannot recover the probability of allowing one or more shallow leaves. The theorem gives every fixed leaf-order statistic, a sharp multiplicative estimate, and a rare-event geometric mechanism. The leading exponent changes by a factor two with each new permitted leaf—an interpretable robustness hierarchy for the number of nearby terminal vertices. The conditioning statement explains the mechanism rather than merely tabulating coefficients. The result has meaningful mathematical content despite its explicit binary offspring restriction and does not require an unrelated downstream theorem.

## Sources and risks

The nearest-leaf case and local limit are prior; numerical checks have finite scope. The theorem assumes fixed order as radius grows. Historical priority remains provisional pending independent expert review, particularly among older branching-process leaf-count small-ball results.

Self-review: passed. Independent audit: not yet performed.
