# Self-review

## Correctness — PASS

The central conditional reduction is exact: for fixed \(A\), the random restriction \((AB)|_{\operatorname{im}A}\) is uniform on an endomorphism algebra, and nilpotency of this restriction is equivalent to nilpotency of \(AB\). The classical Fine–Herstein count, as proved by Leinster's Theorem 5, then gives the conditional factor \(q^{-\operatorname{rank}A}\). Summing random kernel sizes over all vectors proves the \(k\)-factor identity for all prime powers and dimensions. Nilpotency lifts precisely through the nilpotent Jacobson radical, and uniform projections and Wedderburn factors complete the proof. The extracted checker runs \(21\) exact exhaustive comparisons, including rings with nonzero radical. The checker does not purport to prove universal quantifiers.

## Originality — PASS

Dolžan (2025), Theorem 3.2, gives a full **two-factor, fixed-target** matrix distribution and therefore implies the \(k=2\) matrix probability after summation; that case alone is not offered as original. Leinster's classical theorem covers \(k=1\). Sarma–Subedi (2025) studies \(k\)-fold **zero products**, not nilpotency, while their later 2026-10-06 nilpotent-product paper concentrates on **two factors** and commutative classifications. Comparisons with these inspected works and targeted literature searches did not reveal an arbitrary-\(k\) formula over full matrix algebras, nor its radical-invariant extension to all finite unital rings. The strongest unresolved literature risk is that older random-matrix-product or finite-semigroup probability work may contain the same identity under another name.

## Value — PASS

The theorem gives a universal, exact, closed nilpotent-product probability for every finite unital ring, despite noncommutativity and arbitrary radical structure. Its dependence on the products \(q_i^{n_i}\) identifies a striking invariant blindness: a full matrix ring and a field extension have identical probability sequences for every product length. This answers a natural matrix and ring-probability counting problem at all lengths rather than incrementing a finite table. The number-of-factors dependence supplies exact finite thresholds and asymptotics without numerical estimation.

## Scientific scope and risks

Finite associative unital rings and independent uniform factors only. The literature comparison is meaningful but not exhaustive over historical probabilistic semigroup results; the known two-factor and field cases are properly attributed. The proof does not establish the full matrix-product distribution or any result for nonuniform sampling. Independent checking of every new statement remains desirable.

Self-review: passed. Independent audit: not yet performed.
