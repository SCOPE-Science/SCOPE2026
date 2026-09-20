# Review: sharp residual expansion for cubic reciprocal Fibonacci tails

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof starts from the exact Binet identity
\[
F_k^{-3}=5\sqrt5\,\phi^{-3k}\left(1-(-1)^k\phi^{-2k}\right)^{-3}
\]
and the absolutely convergent binomial expansion of \((1-u)^{-3}\). Summing the resulting geometric series over \(k\ge n\) gives the exact analytic representation
\[
S_n=5\sqrt5\,x^3A((-1)^n x^2),\qquad x=\phi^{-n}.
\]
Because \(A(0)>0\), reciprocal power-series expansion is valid in a neighborhood of zero. Expanding through cubic order in the local variable and subtracting the exact Binet expansion of \(g_n\) gives the claimed \(F_n^{-1}\) and \((-1)^nF_n^{-3}\) terms; the next omitted local term is \(O(\phi^{-5n})=O(F_n^{-5})\).

The radical simplifications for \(\kappa\) and \(\lambda\) were checked symbolically. Independent high-precision evaluation of the defining infinite sum agrees with both scaled limits, and the residual after subtracting the two displayed correction terms scales as \(F_n^{-5}\). The verification artifact records these checks.

Adversarial checks included both parities, direct reconstruction of the known \(g_n\) from Binet's formula, and comparison of the \(x^{-1}\) coefficient on both sides. The leading residual constant is positive, consistent with the known lower inequality \(g_n<S_n^{-1}\), while the negative second constant correctly predicts the opposite small deviations from \(\kappa/F_n\) on even and odd indices.

## Originality

**PASS, to the best of our knowledge.** Hwang–Park–Song (arXiv:2609.18179, submitted 16 September 2026) was inspected through its current arXiv text. Its main theorem states convergence of \(S_n^{-1}-g_n\) to zero together with the eventual algebraic window
\[
0<S_n^{-1}-g_n<2/F_n,
\]
but no scaled residual limit, sharp coefficient, parity-dependent next coefficient, or all-order expansion was located.

Li–Yang–Yuan (2025) was inspected at the theorem and proof level. Their Theorem 2.3 gives, under their difference-to-zero convention for the symbol \(\sim\), the generalized cubic approximation that specializes to the same \(g_n\). Their proof contains an \(O(\alpha^{-mn})\)-scale remainder but does not identify its leading coefficient in the Fibonacci specialization.

Wan–Liang–Liao (arXiv:2510.13472; published online 2026) was inspected through its arXiv full text. Its Remark 3.3 explicitly says that the cubic specialization to the special Lucas sequence is exactly Li–Yang–Yuan's Theorem 2.3. Thus it does not supply the residual constant claimed here for the ordinary Fibonacci case.

Searches were also made using the formulations “second-order asymptotic”, “full asymptotic expansion”, “scaled error”, “higher-order reciprocal Fibonacci tail”, the expression \(F_n(S_n^{-1}-g_n)\), and exact forms/decimal values of the two constants. No matching prior statement was located. The 2024 Li–He paper concerns odd and even cubic subsequences and is not the same tail problem.

Residual originality risk remains because not every historical paper on reciprocal Fibonacci sums was inspected in full, and contemporaneous work may be incompletely indexed. The strongest directly relevant primary sources identified above were checked beyond abstract level where accessible.

## Value

**PASS.** The theorem turns a one-sided \(2/F_n\) error window into a sharp asymptotic law with an explicit leading constant approximately \(0.3160435721\), identifies the next parity oscillation, and explains both as the first terms of a systematic convergent local expansion. The known coefficient 2 is therefore more than six times the asymptotic leading coefficient. The analytic representation also supplies a reusable mechanism for computing further terms without returning to the more elaborate floor-function algebra.

## Limitations

The result is specific to the full cubic Fibonacci tail and does not claim a new floor formula or a general theorem for all powers and all second-order recurrences. No explicit least \(n\) for the displayed asymptotic inequalities is claimed. The review is not an independent validation, journal peer review, or formal verification.
