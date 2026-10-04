# Same-model review

## Correctness

PASS. The Euclidean source equations were specialized directly to the scalar constraint-only augmented Lagrangian and then reparameterized by \(s=e^{b_t}\) using the assumed equality \(e^{a_t}=\dot b_t\). The resulting first-order system gives the invariant \(sx-z_\lambda\) by one differentiation. The feasibility variable \(w=sx\) then satisfies an exact forced scalar oscillator. A shifted oscillator energy has integrable forcing and a nonpositive coefficient-drift term, which yields uniform boundedness of \(w\). On the zero-invariant family the same energy has a strictly positive lower bound for every nonzero solution, proving that \(w\) cannot vanish asymptotically and hence that the \(e^{-b_t}\) exponent is sharp.

The bundled numerical replay independently integrates both the full transformed system and the reduced oscillator. It is supporting evidence only; the quantified claim follows from the exact invariant and energy inequalities.

## Originality

PASS. The primary paper was inspected through its coupled mirror equations, friction extension, and feasibility theorem. It gives the generic undamped squared-residual rate and a stronger residual rate under additional conditions, but no scalar conserved quantity or forced-oscillator reduction was found.

The closest accelerated augmented-Lagrangian and primal-dual mirror-flow predecessors were also inspected in full or open-access full text. Their state equations and scaling architectures differ, and neither statement implies the invariant \(e^{b_t}x-z_\lambda\). Targeted published-research searches over aliases and the exact reduction returned no equivalent result.

Residual risk remains that an elementary scalar calculation may occur in older time-rescaled augmented-Lagrangian literature under different notation.

## Value

PASS. The source theorem makes the distinction between squared feasibility and full residual decay mathematically central. On the canonical scalar equality mode, the finding closes that exponent gap without Rayleigh friction and identifies the exact structural reason: a position/lookahead invariant. The same reduction also proves sharpness of the improved exponent, so the result is not merely a better upper bound on an arbitrary example.

Same-model review: passed. Independent audit: not yet performed.
