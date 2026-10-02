# Independent audit — 2026-10-01

## Final claim

A determinant-sign proof of stability exchange in the predator-dependent replicator model

## Disposition

**Passed.** Correctness, originality, and value all pass for the final claim as stated in `RESULT.md`; no claim repair is required.

## Correctness

The primary source's exact ABY determinant is \(\beta\delta F^2x(1-x)g\kappa'\). At each nondegenerate AY/BY/AB boundary collision, two spectral directions remain strictly stable and the unique small ABY eigenvalue therefore has the determinant sign. Direct differentiation of the AY and BY invasion eigenvalues, together with the side of the positive ABY branch, gives the opposite sign; at the reproduction-coexistence AB collision the same comparison follows from the sign change of the affine \(g\). In the codominance case, the already-positive prey-plane eigenvalue persists by spectral continuity. These cases exactly match the three numbered assertions of Conjecture 6.2 without asserting a Sotomayor transcritical bifurcation.

## Originality

Full-text inspection confirms that Cruz-Neves state these conclusions as Conjecture 6.2, explain that standard transcritical characterization fails, and list proving Conjecture 6.2 as future work. Exact-title, conjecture-number, author, and semantic searches found no later proof or correction. The determinant formula and boundary stability theorems are prior inputs; the new contribution is the sign comparison that closes the conjecture.

### Equivalent formulations

Searches:
- Resultary semantic search for predator-dependent replicator Conjecture 6.2 stability exchange determinant sign AY BY ABY
- Web searches for the exact title, arXiv:2607.13281 and Conjecture 6.2

Evidence:
- Resultary's closest exact hit was this audited record; no independent proof of the conjecture was found.

Reasoning: The claim is exactly the source's numbered stability conjecture, not a renamed generic transcritical theorem.

### Broader coverage

Searches:
- Cruz and Neves, arXiv:2607.13281 full text
- Sotomayor, Generic bifurcations of dynamical systems (1973)

Evidence:
- Cruz-Neves supply determinant (43), boundary stability results and the conjecture; they explicitly note failure of a standard transcritical condition. Sotomayor supplies generic bifurcation machinery, not the source-specific sign theorem.

Reasoning: Generic local bifurcation theory does not cover the conclusion mechanically because one of the usual transcritical hypotheses fails in the source model.

### Exact database or table

This is an analytic conjecture proof rather than a database/table claim.

Searches:
- Resultary and web searches for Conjecture 6.2, equation (43), and the three boundary collision cases

### Claim versus prior implication

The prior determinant identity does not by itself state the sign of the small eigenvalue relative to each boundary invasion eigenvalue; the audited proof supplies that missing implication.

Evidence:
- The source uses the conjecture conditionally in its examples and explicitly says proving it is future work.

### Source inspections

- **Predator-dependent replicator dynamics or a predator-prey model with two prey types and frequency dependence** — OPEN_PROBLEM_INPUT_NOT_COVERING. Material read: Full text around Jacobian equation (42), determinant equation (43), Conjecture 6.2 and its three numbered assertions, subsequent example discussion, and Conclusion/Future Work. Evidence: The source explicitly calls the stability-exchange statements Conjecture 6.2 and concludes that proving it is future work. Source: https://arxiv.org/abs/2607.13281

### Residual risks

- The search window is short because the primary source is recent; nevertheless, no later proof or correction was located and the primary full text itself establishes the exact originality target.

## Value

Resolving a named recent conjecture about stability exchange in a biologically motivated three-species model is a worthwhile mathematical gap. The proof also isolates a reusable determinant/invasion-eigenvalue mechanism precisely in a setting where the standard transcritical test is unavailable.

## Limitations

The theorem is local near nondegenerate boundary collisions; it does not establish a standard transcritical normal form, cover \(\kappa'=0\) or other simultaneous degeneracies, or classify distant ABY stability.
