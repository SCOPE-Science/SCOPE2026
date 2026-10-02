# Fresh mathematical audit — A half-plane Briot–Bouquet contraction for bounded Mocanu variation

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** After affine normalization of the half-plane, the hypothesis forces \(c=\beta A\) to be real positive and \(a=(\beta B+\gamma)/c\) to satisfy \(\operatorname{Re}a\ge0\). Analyticity of \(P\) makes \(Q+a\) zero-free. For the boundary-winding lemma, a periodic argument exists because the zero-free analytic function has winding number zero; the \(\alpha=0\) case is an exact periodic-primitive identity, while for \(\alpha>0\) the smoothed-sign Stokes formula has nonnegative integrand on its support. This proves the circle \(L^1\) contraction. The Paatero–Pinchuk criterion then transfers membership from \(P\) to \(q\).

Sources checked: RESULT.md at the assigned source tree; Dziok 2013 full open-access article; Dziok–Noor 2017 full PDF problem statement.

Correctness risks: The proof relies on the classical Paatero–Pinchuk characterization as quoted in the source literature; no equality classification is needed..

## Originality

**PASS.** The inspected 2013 source explicitly labels the nonlinear case as open, and the 2017 two-target paper still describes the \(\beta\ne0\) problem as open. The published-record search found no earlier half-plane resolution or equivalent boundary-winding \(L^1\) contraction.

### Equivalent formulations

Searches/sources: Dziok 2013 Problem 1 and Remark 2; Dziok–Noor 2017 Problem 1 / nonlinear remark; Published-record semantic search: Briot Bouquet half-plane bounded Mocanu variation beta nonlinear contraction Dziok problem.

Evidence: Dziok 2013 states that the linear case follows from its theorem but the nonlinear case remains open. Dziok–Noor 2017 restates a broader two-target version and still treats the nonlinear case as unresolved.

The audited theorem supplies an affirmative half-plane branch of exactly that nonlinear implication.

### Broader coverage

Searches/sources: 2015 Dziok multivalent Mocanu paper; 2020 bounded-Mocanu generalization; later bounded-boundary-rotation terminology.

Evidence: The located later works develop related classes and subordination lemmas but no theorem was found that implies the half-plane \(L^1\) contraction. The audited result does not claim arbitrary convex targets or two distinct target functions.

No inspected broader theorem dominates this half-plane branch; the remaining general convex-domain problem is strictly broader and unsolved by this claim.

### Exact database or table

Searches/sources: Resultary exact/semantic search using the nonlinear transform and half-plane target.

Evidence: Only the current record matched the theorem; no earlier exact published-record hit was found.

No numerical database is relevant; theorem-record search is the applicable exact check.

### Claim versus prior implication

Searches/sources: Check whether the known linear \(\beta=0\) theorem implies \(\beta\ne0\); Check whether general one-target Briot–Bouquet lemmas imply the signed-convex-combination \(L^1\) bound.

Evidence: The source itself distinguishes the linear theorem from the nonlinear open problem. The new winding/Stokes inequality is needed to control the nonlinear denominator and is not a renaming of the linear argument.

The half-plane conclusion is not mechanically implied by the prior linear or standard subordination lemmas.

### Source inspections

- **Classes of functions associated with bounded Mocanu variation** — PRIMARY_OPEN_PROBLEM.
  Identifier: https://doi.org/10.1186/1029-242X-2013-349
  Trigger: Original Problem 1.
  Material read: Full open-access HTML, including Problem 1 and Remark 2.
  Method: lawful open-access full text
  Evidence: The article states that the result is known in the linear case and is an open problem in the nonlinear case.
- **Classes of analytic functions related to a combination of two convex functions** — PRIMARY_OPEN_PROBLEM.
  Identifier: https://doi.org/10.7153/jmi-11-35
  Trigger: Later direct restatement of the nonlinear problem.
  Material read: Full PDF inspected, including the problem/remark page.
  Method: lawful open-access full text
  Evidence: The later paper again presents the nonlinear case as open while posing a more general two-target formulation.

Originality risks:
- Equivalent coverage could exist under older bounded-boundary-rotation or Hardy-space terminology not captured by the searched keywords.

## Scientific value

**PASS.** The theorem resolves a broad natural branch of an explicit published nonlinear open problem for every half-plane target and every \(\mu\ge1\), and the boundary-winding contraction lemma is a reusable analytic mechanism rather than a parameter substitution.

Value risks: It does not settle arbitrary convex targets or the two-distinct-target problem..

## Final assessment

The final claim survives unchanged on correctness, originality, and scientific value. No change to the scientific result or slogan is proposed.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
