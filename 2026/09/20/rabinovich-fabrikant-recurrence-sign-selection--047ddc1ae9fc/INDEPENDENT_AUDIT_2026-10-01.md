# Independent audit — 2026-10-01

## Final claim

For the Rabinovich--Fabrikant flow with \(\alpha>0\), compact ergodic recurrence off \(z=0\) obeys the exact mean laws and sign selection in RESULT.md; the \(\gamma=0\) periodic orbits are exactly the stated circles with exact period, and \(\gamma<0\) makes the physical half-space \(z\ge0\) converge exponentially to the origin.

## Correctness — PASS

Direct differentiation gives \(\dot W=2\gamma(x^2+y^2)-8\alpha z\) and exact sign preservation of \(z\). For a compact ergodic invariant measure off the plane, applying Birkhoff recurrence to \(\log|z|\) yields \(\int xy\,d\mu=-\alpha\) without requiring global integrability of \(\log|z|\); invariance of the bounded smooth observable \(W\) then gives the mean-height identity. The plane law \(\dot q=2\gamma q\) excludes nontrivial compact invariant probabilities there when \(\gamma\ne0\). At \(\gamma=0\), polar reduction gives \(\dot\theta=1-r^2\cos^2\theta\), hence exactly the circles \(0<r<1\) with period \(2\pi/\sqrt{1-r^2}\). For \(\gamma<0,z\ge0\), \(W\ge0\) and \(\dot W\le-\min(2|\gamma|,2\alpha)W\), giving global exponential collapse. Independent symbolic checks reproduced the central identities.

Checked sources:
- M.-F. Danca, M. Fečkan, N. Kuznetsov, G. Chen, Looking More Closely at the Rabinovich--Fabrikant System, IJBC 26 (2016), complete 21-page author full text inspected.
- M. I. Rabinovich and A. L. Fabrikant, Stochastic self-modulation of waves in nonequilibrium media, Sov. Phys. JETP 50 (1979), primary model source.
- Resultary semantic search for Rabinovich--Fabrikant invariant-measure mean laws, recurrence barriers, and periodic-orbit identities.
- Independent symbolic reconstruction of the balance \(\dot W\), the plane radial law, and the \(x+y\) derivative.

Residual risks:
- The invariant-measure theorem is componentwise for compactly supported ergodic measures; it does not classify the negative-\(z\) half-space.

## Originality — PASS

Best-of-knowledge originality passes. The original model and later numerical/bifurcation literature contain the system, equilibria, invariant plane, and many attractors, but the complete 2016 primary article does not state the audited compact-ergodic mean identities, sign-selection theorem, exact \(\gamma=0\) periodic classification, or the global \(\gamma<0,z\ge0\) collapse theorem. Resultary returned the assigned finding as the exact pre-existing record; the closest related stationary-balance result is dated later.

### Equivalent formulations

Searches:
- Resultary semantic search: Rabinovich Fabrikant invariant measure mean xy mean z recurrence sign selection
- Full-text search/inspection of Danca et al. 2016

Evidence:
- The assigned finding is the exact same-topic published result; a related stationary-defect finding is dated 2026-09-21, after this record.
- Danca et al. focus on equilibria, heteroclinic approximations, transient/cycling chaos, and hidden attractors.

Reasoning: Equivalent formulations include stationary coboundary identities, recurrence half-space selection, and exact periodic averages; these were not found in earlier inspected sources.

### Broader coverage

Searches:
- Rabinovich--Fabrikant 1979 model source
- Danca et al. 2016 full text
- Periodic-structure literature cited in RESULT.md

Evidence:
- The earlier literature is broader on numerical/bifurcation dynamics but does not supply a theorem for every compact ergodic recurrent state.
- The 2016 full text explicitly emphasizes predominantly numerical analysis.

Reasoning: No broader inspected theorem mechanically implies the invariant-measure and Lyapunov conclusions.

### Exact database or table

Searches:
- Resultary exact-topic search
- Full 2016 source search for the displayed mean identities and period law

Evidence:
- No earlier exact table or formula for the mean-height law or the full zero-growth period family was located.

Reasoning: This is not a table-driven claim; the relevant exact formulas arise from coboundary identities and polar integration.

### Claim versus prior implication

Searches:
- Historic energy/invariant-plane facts versus final theorem

Evidence:
- The polynomial balance reduces to the known conservative energy only in a special limit, and the plane radial identity is prior art.
- The final recurrence law additionally requires logarithmic recurrence of \(z\), invariant-measure averaging, and a separate Lyapunov estimate.

Reasoning: The final claim is not a routine rephrasing of the historic energy expression or the invariant plane.

### Source inspections

- **Looking More Closely at the Rabinovich--Fabrikant System** — Highly relevant but not covering the audited analytic recurrence theorem. Material read: Complete 21-page author-provided full text. Method: Primary full-text inspection. Evidence: The paper studies equilibria and numerical attractor/heteroclinic phenomena and states that most investigations are numerical; the audited mean identities and half-space theorem are absent from its stated results.

Checked sources:
- M.-F. Danca, M. Fečkan, N. Kuznetsov, G. Chen, Looking More Closely at the Rabinovich--Fabrikant System, IJBC 26 (2016), complete 21-page author full text inspected.
- M. I. Rabinovich and A. L. Fabrikant, Stochastic self-modulation of waves in nonequilibrium media, Sov. Phys. JETP 50 (1979), primary model source.
- Resultary semantic search for Rabinovich--Fabrikant invariant-measure mean laws, recurrence barriers, and periodic-orbit identities.
- Independent symbolic reconstruction of the balance \(\dot W\), the plane radial law, and the \(x+y\) derivative.

Residual risks:
- Unindexed work in the original physical variables may contain related averaged identities; no such implication was located in the inspected literature.

## Scientific value — PASS

The result supplies exact constraints on all compact ergodic recurrent dynamics rather than on a selected numerical attractor. It gives a sign obstruction, exact periodic classification on a natural parameter slice, and a global exclusion region in the physical half-space. These are reusable structural facts for a heavily studied nonlinear system.

Checked sources:
- M.-F. Danca, M. Fečkan, N. Kuznetsov, G. Chen, Looking More Closely at the Rabinovich--Fabrikant System, IJBC 26 (2016), complete 21-page author full text inspected.
- M. I. Rabinovich and A. L. Fabrikant, Stochastic self-modulation of waves in nonequilibrium media, Sov. Phys. JETP 50 (1979), primary model source.
- Resultary semantic search for Rabinovich--Fabrikant invariant-measure mean laws, recurrence barriers, and periodic-orbit identities.
- Independent symbolic reconstruction of the balance \(\dot W\), the plane radial law, and the \(x+y\) derivative.

Residual risks:
- Unindexed work in the original physical variables may contain related averaged identities; no such implication was located in the inspected literature.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
