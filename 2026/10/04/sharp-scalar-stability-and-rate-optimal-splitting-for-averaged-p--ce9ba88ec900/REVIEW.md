# Same-model review

## Correctness

PASS. The proximal map of the quadratic regularizer is explicit, so the aPRG iteration reduces exactly to a real second-order recurrence. The three Jury inequalities simplify to one nontrivial condition, giving the if-and-only-if stability region. The finite boundary has an exact \(-1\) root, and the prescribed source initialization has a nonzero coefficient on that mode; the same initialization cannot cancel the unstable mode above the boundary. The rate formula follows from the two real roots of opposite signs. Differentiating the dominant root proves the unique finite optimum for \(0<\mu<2a\) and strict monotone improvement toward factor \(1/2\) for \(\mu\ge2a\).

The bundled script checks the recurrence identities, exact boundary relations, representative root moduli, and the optimal-step formulas. It is supporting verification only; the quantified proof is algebraic.

## Originality

PASS. The primary 2026 aPRG paper was inspected through its algorithm, special-case remark, convergence theorem, and rate discussion. It proves generic fixed-step convergence for \(\tau<1/L_F\) and an ergodic sublinear rate, but no positive-proximal-quadratic scalar stability or exact rate-optimal phase diagram was found. The paper itself identifies the \(g=0\) specialization with Popov, so that limiting slice is excluded from the originality claim.

The closest database records were inspected in full. One treats unaveraged affine reflected gradient; two treat forward-reflected-backward on split-skew rotations. Their characteristic recurrences differ and do not imply the symmetric proximal-quadratic aPRG formula. Foundational projected-reflected-gradient and forward-reflected-backward sources were also checked at the method and stated-result level.

Residual risk remains that an older scalar calculation under different splitting terminology could contain an equivalent formula.

## Value

PASS. The quadratic split isolates the interaction between forward curvature and proximal curvature in the new averaged method. The exact threshold \(\mu=a\) for removal of every finite step ceiling, together with the closed rate-optimal step for \(0<\mu<2a\), gives actionable parameter-design information that the generic Lipschitz theorem does not expose. It also shows precisely why treating the proximal curvature as irrelevant to the step bound can be highly conservative on a natural commuting model.

Same-model review: passed. Independent audit: not yet performed.
