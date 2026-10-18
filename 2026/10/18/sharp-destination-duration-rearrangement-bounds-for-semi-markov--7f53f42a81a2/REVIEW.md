# Scientific review: sharp destination–duration rearrangement bounds

## Correctness

**PASS.** The regenerative first-step equations give the fixed mean \(m=(I-P)^{-1}\mu\) and the second moment \(h=(I-P)^{-1}(\nu+2a)\), where \(a_i=\mathbb E[H_im_{J_i}]\). Integrability follows from finite-state absorption and finite second holding moments. The sharp bivariate rearrangement bounds identify the exact extrema of every \(a_i\), while nonnegativity of the Green matrix and independence of rowwise kernel choices give simultaneous attainment. The continuous three-state example is integrated exactly; 1,954 rational checks in `verify.py` passed for discrete feedback models. The numerical tests do not replace the proof.

## Originality

**PASS, qualified.** Voits (arXiv:2610.13505v1, Theorem 15) already gives broad hitting-time moment identities; Le et al. (arXiv:2603.26414v1, Theorem 2 and Appendix A) already give weighted-walk variance formulas; Butler–Bronson already obtain semi-Markov passage transforms; rearrangement of two fixed marginals is classical (Glasserman–Yao). The distinct statement assessed here is the **sharp, simultaneous optimization of absorption-time variance across all initial states while fixing each statewise holding marginal and transition row**. The inspected primary treatments give no stated extremizing joint kernel for that constraint. A general coupling/controlled-renewal result may subsume it, and independent priority review is still required.

## Mathematical value

**PASS.** The exact extremal envelope answers a natural reliability/network-design question left unanswered by mean and moment formulas: how much can hidden correlation between a waiting time and its selected exit channel change absorption-time uncertainty when all observed marginal quantities stay identical? The optimizer is a local quantile rule despite arbitrarily many feedback paths, works for all starts at once, and produces a factor-thirteen variance range in a minimal non-self-loop example. No general tail ordering or higher-cumulant extremality is asserted.

Self-review: passed. Independent audit: not yet performed.
