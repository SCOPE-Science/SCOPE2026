# Same-model review

## Verdict

**PASS (same-model review only).** The contribution is assessed separately as correct, original to the best of our knowledge, and scientifically useful. This is not independent validation or peer review.

Same-model review: passed. Cross-model review: not yet performed.

## Correctness audit

1. **Fixed-conductance theorem preserved.** The source paper's Theorem 1 explicitly assumes a fixed symmetric non-negative conductance matrix. Under that assumption the conductance-work term vanishes and the published proof of \(\dot E=-C\|\dot V\|^2\) is unaffected.
2. **Full chain rule.** The same energy depends explicitly on every adaptive \(G_{ij}(t)\). Differentiation therefore produces \(\tfrac12\sum \dot G_{ij}(V_i-V_j)^2\) in addition to the voltage derivative terms. Symmetry of \(G\) converts the latter exactly to \(-C\|\dot V\|^2+F\cdot\dot V\).
3. **All voltage forcing accounted for.** The source full voltage equation contains GRN feedback \(\Gamma\), external input \(I^{\rm ext}\), and wound signal \(W\). Hence the exact work term is \((\Gamma+I^{\rm ext}+W)\cdot\dot V\). Setting external input and wound signal to zero recovers the commonly analyzed unforced case but does not remove conductance work.
4. **Two-cell obstruction.** For \(V=(-x,x)\) and \(G=a(b^2-x^2)/2\), direct substitution into the symmetric cubic voltage equations gives \(\dot V=0\) exactly. Positive voltage-driven adaptation gives \(\dot G>0\) for \(x\) sufficiently close to \(b\), because the logistic product remains positive while \(G\to0\). The energy derivative is then strictly positive.
5. **Numerical check.** The standalone artifact evaluates the two-cell construction at values matching the source parameterization used for the energy experiment and the public implementation. It verifies voltage residuals at floating-point zero, positive \(\dot G\), and positive \(\dot E\).
6. **Scope of the correction.** The result concerns Eq. (39)'s use as an identity for the adaptive full model and the interpretation of the instantaneous energy with evolving conductances. It does not assert that the paper's plotted trajectories fail to descend and does not rule out another full-system Lyapunov functional.

## Originality audit

### Existing SCOPE records

The current SCOPE archive was searched by the source title/model, morphogenesis and bioelectric terminology, adaptive gap-junction conductance, Lyapunov/energy balance, time-dependent coupling, and equivalent "work term" formulations. No prior SCOPE record covering this correction or counterexample was located.

### External literature checked

- **Cortés-Poza (Journal of Mathematical Biology, 2026), DOI 10.1007/s00285-026-02459-2.** The accessible full text was inspected at the model equations, adaptive-conductance law, fixed-conductance Theorem 1, Eq. (39), the energy figures, and Problem 7. Theorem 1 is explicitly fixed-\(G\), while Eq. (39) is subsequently presented as an identity for the full model without the \(\dot G\) contribution. The paper also reports full adaptive simulations in which the same energy is tracked.
- **Public source implementation accompanying the paper, commit `2b53a08fe096394496b482cecef39b695b500ed7`.** The voltage and conductance right-hand sides were inspected. The energy-rate helper implements only the dissipative voltage term plus GRN work, while the full model evolves \(G\). The energy experiment evaluates the energy using the evolving conductance matrix.
- Exact-title, DOI, author-title, correction/erratum/corrigendum, adaptive-conductance Lyapunov, time-dependent-conductance energy, and synonymous searches were checked. No follow-up correction or source-specific treatment of the missing conductance-work term was located.
- Broader searches of adaptive-network and time-dependent-coupling Lyapunov literature were used to test whether the claimed model-specific correction was already a named consequence of a stronger result. General adaptive-network energy ideas exist, but no located source supplied this correction/counterexample for the Cortés-Poza model. The generic multivariable chain rule itself is not claimed as new.

No inaccessible paper was identified as especially likely to contain this model-specific correction. Because the motivating paper is very recent, undetected discussion or unpublished correspondence remains a residual originality risk. The originality claim is limited to the explicit correction, exact specialized balance, and counterexample for this 2026 model, to the best of our knowledge.

## Value audit

The result changes the mathematical interpretation of the source paper's full-model energy diagnostics without disturbing its valid reduced theorem. It gives the exact quantity that must be monitored for dissipativity, provides a constructive obstruction to any blanket monotonicity claim for the displayed instantaneous energy, and sharpens the source's open Problem 7 by isolating the extra term that an exact adaptive-system Lyapunov theory must control or absorb. The correction is directly reusable in analysis and in future numerical diagnostics of the model.
