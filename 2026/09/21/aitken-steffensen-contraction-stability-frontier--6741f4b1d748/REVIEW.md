# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** After affine normalization, every admissible orbit is represented by
two scalars \(a=g(1)\) and \(c=g(a)\). Introducing
\(t=(c-a)/(a-1)\) turns the contraction constraints into explicit intervals and
the Aitken point into \((a-t)/(1-t)\). The sign of \(t\) is forced by the sign of
\(a\), so the extremization separates into positive and negative branches. Each
branch reduces to endpoint rational functions with direct derivative bounds.
The positive lower endpoint gives the global maximum
\(2q^2/((1-q)(1+2q))\). Continuous piecewise-affine contractions attain equality.
The nondecreasing subclass is the same calculation with the additional
constraint \(c\ge0\), yielding \(q^2/(1-q^2)\). The second-difference denominator
is bounded away from zero in exact arithmetic on every nonfixed orbit.

Adversarial checks included both signs of the first image, limiting cases
\(q\downarrow0\) and \(q\uparrow1\), the threshold equations, the equality maps,
and direct sampling of the feasible normalized orbit region. The verification
artifact found no violation.

## Originality

**PASS, to the best of our knowledge.** Classical Steffensen literature was
searched through the root-finding, fixed-point, divided-difference, monotone
enclosure, and a-posteriori-error formulations. Modern Anderson-acceleration and
fixed-point-acceleration literature was also checked because scalar restarted
depth-one extrapolation can be described in related language.

The accessible Baptist theorem concerns convexity plus a sign-changing bracket
and proves monotone enclosure, not the bare global contraction class. Pavaloiu
uses semilocal operator hypotheses. Voller's article is explicitly in the
Steffensen-like error-bound tradition. Modern Anderson results use different
algorithms and generally local, coefficient, linear-independence, or linear-system
structure. The 2025 Acta Numerica survey confirms the broad historical setting.

No checked source states the exact factor
\(2q^2/((1-q)(1+2q))\), the universal threshold
\((1+\sqrt{17})/8\), the exact nondecreasing factor \(q^2/(1-q^2)\), or the
same-evaluation comparison showing a minimax loss of at least \(16/9\) versus two
Picard steps.

Residual uncertainty is material but bounded: full theorem-level text was not
available for Schmidt (1966), Johnson--Scholz (1968), Hofmann (1975), and
Schneider (1981). Those papers are the most plausible older sources for an
equivalent inequality in different notation. This is therefore a
"to the best of our knowledge" originality judgment, not a claim of exhaustive
historical exclusion.

## Value

**PASS.** The result supplies an exact black-box robustness law for one of the
oldest acceleration procedures. It identifies the precise contraction strength
at which acceleration ceases to be universally error-nonexpansive, shows that
monotonicity moves that boundary but does not remove the minimax disadvantage,
and gives explicit equality maps. The comparison with two raw Picard evaluations
clarifies a useful distinction between smooth local acceleration and worst-case
global robustness under only Lipschitz information.

## Scientific limitations

The theorem is scalar, real, exact-arithmetic, and based on a global Lipschitz
contraction. It controls fixed-point error over one restarted cycle; it does not
give a vector analogue, a floating-point stability theorem, or a claim that
failure of the universal threshold implies long-run divergence. Smoothness,
convexity, monotonicity beyond the stated subclass, or other structural
assumptions may yield much stronger convergence. Historical equivalence risk
remains in the older sources identified above.
