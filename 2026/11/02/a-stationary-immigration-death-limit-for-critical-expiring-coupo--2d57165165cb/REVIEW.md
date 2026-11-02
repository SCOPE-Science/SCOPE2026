# Self-review

**Correctness — PASS.** A stationary marked-gap construction gives the exact absence-episode immigration intensity \(\lambda=e^{-c}\) and exponential duration; the law of small numbers yields the stationary queue path. Clock concentration and a geometric near-threshold-gap bound transfer it to discrete sliding windows in the \(J_1\) topology. Holding intervals at zero allow first-hitting convergence. An exact resolvent convolution proves the transform and its limiting mean. `verify.py` passed 186 exact finite-word/detailed-balance and numerical consistency checks. It does not replace the functional proof.

**Originality — PASS, qualified.** Long's arXiv:2604.26298v1 Section 8.3 gives the one-time critical Poisson mass and flux, not this process limit. Attrill and Garoni's arXiv:2605.14206v1 Lemma 4.9 already establishes the same \(M/M/\infty\) hitting transform for the *clumsy* model; it is expressly prior mathematics. The new claim is the critical-window process-level convergence for deterministic sliding expiration and consequent transfer. The neighboring reset/clumsy/careless models in arXiv:2605.14511v1 do not directly subsume it. General Poisson-clumping results could offer stronger coverage; historical priority has not been independently determined.

**Mathematical value — PASS.** One-time occupancy and flux do not determine temporal correlations or the first stationary complete-window waiting time. The joint process limit supplies both, including a nonexponential explicit transform, at the natural near-completion scale.

**Limitations.** Two-sided stationary iid uniform draws, fixed \(c\), compact-time functional convergence, no convergence of finite-n mean hitting times, no initially-empty first-completion theorem, no general nonuniform models.

Self-review: passed. Independent audit: not yet performed.
