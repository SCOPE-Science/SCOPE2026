# Review: interleaved-stable two-type branching explosion

## Correctness — PASS

The partition identity \(\phi_1+\phi_2=2\sqrt\pi\sqrt{\cdot}\) gives a *global* quadratic envelope for the zero-argument cumulant sum. The positive-initial solutions are cooperative, so their limit from above solves the cumulant equation and is nonzero for every positive time. Because \(\phi_2\) is bounded and tends to \(L>0\), the second cumulant is asymptotic to \(2Lt\); the first has the proved expansion \(\pi t^2+4\sqrt{2\pi L}\,t^{3/2}+o(t^{3/2})\). Applying the branching Laplace formula gives almost-sure finite explosion and the survival laws. The included checker independently illustrates elementary finite inequalities without replacing the analytic proof.

## Originality — PASS, with limitations

Chaumont–Lamoureux (arXiv:2610.23649v1), Sections 3.1–3.2, explicitly define the mechanism and explain why their three conservativity tests do not resolve it. Li–Li (arXiv:2405.05879v1) provide the general zero-equation uniqueness criterion; Duffie–Filipović–Schachermayer (2003), Section 9, give a related affine-process criterion. Their inspected statements do not classify this specific example or compute the two-scale tails. Targeted searches did not identify exact coverage, but undiscovered equivalent comparison theorems are a residual literature risk.

## Mathematical value — PASS

The result determines the unresolved explosion verdict for a naturally constructed Lévy partition and exhibits a nontrivial initial-type asymmetry: Gaussian-scale versus exponential-scale nonexplosion tails, including a second-order exponent. This distinguishes multitype explosion from the componentwise Grey tests that motivated the example.

## Limits and prior sources

This is a mechanism-specific asymptotic result, not a new general necessary-and-sufficient condition. The 2023 multitype extinction work was inspected only at abstract level. There has been no independent mathematical validation. References and precise definitions are in RESULT.md and the structured review record.

Self-review: passed. Independent audit: not yet performed.
