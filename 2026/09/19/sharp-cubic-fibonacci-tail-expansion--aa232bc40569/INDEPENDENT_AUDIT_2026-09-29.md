# Independent audit — Sharp residual expansion for cubic reciprocal Fibonacci tails

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/sharp-cubic-fibonacci-tail-expansion--aa232bc40569`  
**Audited tree:** `b18a3b2eaed247cab255142fdd1ee332803723ad`

## Disposition

**PASSED.** Correctness, originality on the explicitly stated boundary, and scientific value pass. The record may remain in the validated set.

## Correctness

**PASS.** Binet's formula and the absolutely convergent expansion (1-u)^{-3}=sum binom(m+2,2)u^m give the stated exact analytic representation S_n=5sqrt(5)x^3 A((-1)^n x^2); since A(0)>0, inversion yields a genuine convergent local expansion. Matching the first two residual terms against the exact Binet expansion of g_n gives the displayed kappa and lambda. I independently evaluated the defining infinite tail at high precision for n=10,15,20,30,40,50: F_n(S_n^{-1}-g_n) converges to 0.316043572066111387330139784596, while (-1)^n F_n^3(S_n^{-1}-g_n-kappa/F_n) converges to -0.00220191196332330159798175564877. After subtracting both terms, the F_n^5-scaled remainder stabilizes near -0.012159709839, consistent with O(F_n^{-5}).

## Originality

**PASS.** The public arXiv abstract of Hwang--Park--Song states convergence of S_n^{-1}-g_n to zero and the eventual window 0<S_n^{-1}-g_n<2/F_n, but not a sharp scaled residual constant or parity-dependent next term. The open-access Li--Yang--Yuan 2025 HTML describes the broader generalized-Fibonacci program of finding g_n with difference tending to zero; targeted searches for the exact radical constants and their decimals found no prior match. Wan--Liang--Liao gives generalized subsequence asymptotics and does not expose this full-tail two-term residual in accessible metadata. No earlier SCOPE record in the September 17--19 inventory contains the same theorem.

## Scientific value

**PASS.** The result replaces a coarse eventual 2/F_n window by the sharp leading coefficient, identifies the next parity oscillation, and provides an analytic mechanism for all higher terms. That resolves both the asymptotic size and the first oscillatory structure of the residual and materially strengthens the prior difference-to-zero statements.

## Independent checks

- Re-derived the Binet/binomial/geometric-series representation and the analytic inversion argument.
- Evaluated the original infinite tail with high precision at six values from n=10 through n=50 and independently reproduced both stated scaled limits.
- Checked the sign/parity convention for the lambda term at both even and odd n.
- After subtracting both displayed terms, verified numerically that the F_n^5-scaled remainder remains bounded and stabilizes.
- Inspected the repository verification output and confirmed it records the same exact constants and convergence diagnostics.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.18179 — Hwang--Park--Song, Continuous approximation to the reciprocal sum of the cubes of Fibonacci numbers; public abstract states the explicit g_n, convergence to zero, and eventual 2/F_n window.
- https://doi.org/10.3934/era.2025020 — Li--Yang--Yuan, The asymptotic behavior of the reciprocal sum of generalized Fibonacci numbers; open-access HTML states the general asymptotic-to-zero framework for powers s=1,2,3,4.
- https://doi.org/10.21136/MB.2026.0161-25 — Wan--Liang--Liao, The asymptotic estimation for two classes of generalized Fibonacci sub-sequences; related generalized-subsequence asymptotics.

- No decisive earlier SCOPE record was identified for the validated novelty boundary.

## Limitations

- The theorem is specific to the full cubic Fibonacci tail and does not itself establish analogous constants for arbitrary powers or general Lucas/Horadam sequences.
- No explicit smallest n for the eventual inequalities is determined.
- Contemporaneous work is recent and may be incompletely indexed; the originality conclusion is to the best of the accessible public record.
