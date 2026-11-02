# Scientific review: one-defect theta-graph projection constants

**Claim assessed.** For each integer triple \(p,a,b\ge2\), the absolute real-linear projection constant of the graph Lipschitz space \(\operatorname{Lip}_0(\Theta_{p;a,b})\) has the exact three-case expression in RESULT.md; the large-exceptional-path branch stabilizes at \(H\).

## Correctness — PASS

The proof embeds the gradient space isometrically in edge \(\ell_\infty\), dualizes to minimization of the complementary \(\ell_1\)-projection norm, and symmetrizes over within-path permutations and permutations of the repeated paths. The exact column norms then reduce the unrestricted problem to \(\min_{0\le x\le1/p}\max\{C+hx,1+Bx\}\), whose three cases and boundaries are evaluated directly. Unlike a numerical fit, the argument works for all integers in scope. An exact-rational checker and eight unrestricted projection LP instances give supplementary finite controls; they are not an infinite proof.

## Originality — PASS, qualified

Dilworth, Kutzarova and Ostrovskii (arXiv:2007.07949, especially Section 6) already computed first-level multibranch diamond values, including the case \(a=b=2\). That case is explicitly background rather than a novelty claim. Their 2023 paper (arXiv:2305.12582) provides invariant cycle-space projection methods; Basso (arXiv:2104.14238) treats the general extension/projection relationship. The inspected primary passages do not establish the three-parameter complementary projection norm or saturation threshold. Further methods for minimal hyperplane projections treat \(\min\|P\|\), not automatically the required \(\min\|I-P\|\). An equivalent older result under different terminology cannot be ruled out.

## Mathematical value — PASS

A graph family obtained by unevenly subdividing multibranch diamond networks receives a complete exact operator-space invariant, including a sharp parameter threshold at which lengthening one branch no longer affects the optimum. This is a nontrivial parametric classification of a natural infinite family and identifies a saturation mechanism beyond the previously known calibration case.

## Limitations and verification

The theorem is restricted to positive integer unit-edge path lengths, real scalars, and linear projections. It does not cover arbitrary heterogeneous path lengths, weighted edges, complex scalars, nonlinear projections, or other extension moduli. Computational checks are finite; the analytical proof is indispensable. Published-history coverage is targeted and does not establish exhaustive priority.

Self-review: passed. Independent audit: not yet performed.
