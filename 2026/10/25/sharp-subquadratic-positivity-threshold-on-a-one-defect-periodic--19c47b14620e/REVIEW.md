# Self-review

**Correctness — PASS.** With the displayed finite-element assembly and exact determinant, the 20 off-diagonal and five diagonal identities in `verify.py` prove the complete sign classification for all real mesh ratios and timesteps in scope. Descartes’ rule and endpoint signs give the unique cubic threshold and strict improvement, while the substitution at \(t=h/6+c\) gives the large-stretch expansion. Exact-rational numerical checks are corroboration only.

**Originality — PASS with uncertainty.** Li–Huang (arXiv:1209.5657) establish general sufficient lower timestep bounds; they do not furnish the displayed exact classification in the inspected primary sections. Accessible prior results cover the uniform ring, four-node nonuniform rings, alternating six-node rings, Dirichlet paths and equilateral metric graphs, not the five-node one-defect threshold. The uniform \(h=1\) endpoint is already known and is not independently claimed. General positivity methods in the 2015 Chatzipantelidis–Horváth–Thomée paper are highly relevant; its complete primary text remained inaccessible, so specialized coverage is an explicit residual risk, not claimed absent.

**Mathematical value — PASS.** Exact timestep positivity is an operational numerical maximum-principle invariant. The first simple nonuniform cyclic bypass example exhibits a sharp transition changing the stretching law from the traditional quadratic sufficient bound to a linear sharp bound. That asymptotic separation and the explicit cubic boundary make the result useful beyond a one-off symbolic exercise.

Scientific limitations: five periodic P1 elements, one long cell, equal other cell lengths, unit normalized diffusivity, one backward-Euler step. No general cycle-size theorem, no semigroup statement and no external independent validation. Closest sources: Li–Huang (2012/2013), Thomée–Wahlbin (2008), Chatzipantelidis–Horváth–Thomée (2015); the last was not available as full text.

Self-review: passed. Independent audit: not yet performed.
