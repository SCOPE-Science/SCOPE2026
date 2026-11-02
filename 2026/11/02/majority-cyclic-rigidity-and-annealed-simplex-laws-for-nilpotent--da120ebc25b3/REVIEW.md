# Scientific review

## Correctness — PASS
The exact profile is a direct pair count: \(\operatorname{GL}_n\)-orbits enumerate labeled splittings, and each block supports precisely \(q^{r_i^2-r_i}\) nilpotents. The product-tail estimate supplies the claimed polynomial mean and total-variation approximation to uniform compositions; the continuous simplex limit is weak convergence only. The regular-nilpotent orbit gives probability \(\prod_{i=2}^n(1-q^{-i})>1/2\), and elementary module decomposition identifies exactly the matrices with \(L_k=k\). `verify.py` exhausts four small-field cases with independently computed products and idempotent/projection tests. Extension fields and asymptotic limits are not empirically exhaustive and are handled by proof.

## Originality — PASS relative to inspected evidence
Bogdanić et al. (arXiv:2212.08425v1) classify commuting nilpotent Jordan types inside a two-block centralizer; Khatami (arXiv:2304.08550v1) surveys generic commuting nilpotent types; Fulman–Guralnick (arXiv:1611.05499) enumerate general commuting pairs and nilpotent–nilpotent pairs; Leinster (arXiv:1912.12562) supplies the classical nilpotent count. The exact Gaussian-binomial coefficient factors and GL-orbit method are known machinery, not claimed as new. The assessed statement is the joint all-k invariant-splitting mean, Dirichlet size-biased law, and strict-majority constant-median versus diverging-mean contrast. No direct coverage was located in the inspected literature or searched research records. The residual risk is an earlier equivalent Hall-module/random-matrix law. This is a self-review best-knowledge judgment, not a priority certificate.

## Mathematical value — PASS
Invariant direct-sum splittings are a canonical module invariant and correspond to commuting centralizer idempotents. The theorem gives an exact finite profile in every dimension, determines a continuous scaling limit of macroscopic summand sizes, and shows that the mean can diverge while over half the original sample has its minimum count. These complementary ensemble laws elucidate the centralizer structure of random nilpotents. The value lies in the coherent all-arity ensemble phenomenon, not in pretending the underlying q-multinomial identity is itself new.

## Limits and risk
The sampling distinction is essential. No claim is made for unordered splittings, nonzero-only summands, growing k, or a quenched Dirichlet law. Literature coverage remains incomplete and needs independent specialist audit.

Self-review: passed. Independent audit: not yet performed.
