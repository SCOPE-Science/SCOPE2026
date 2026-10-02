# Independent audit — SCOPE-20260919-89fed354a859

Audited: 2026-10-01 UTC.

Disposition: **passed**.

## Final claim

At the critical variance \(\sigma^2=2/(n+1)\), genuine translations of the Euclidean ball are quadratic null directions for the uncentered Gaussian volume product but have a strictly negative explicit quartic coefficient.

## Correctness (C) — PASS

The two factor expansions along \(B+te\) have opposite quadratic coefficients, so the critical quadratic term cancels. Independent symbolic multiplication of the displayed fourth-order coefficients reproduces exactly \(-C_n\). The radial integration-by-parts identity gives \(R=n-qI_2/I_0>n-q=(n-1)/2\); substituting this lower bound makes the bracket in \(C_n\) exceed \(2(n^2+8n-1)>0\) for \(n\ge2\). Thus the first nonzero translation term is indeed strictly negative quartic.

**Sources checked.** assigned RESULT.md at the audited tree; independent symbolic recombination of the two fourth-order expansions; full primary text of arXiv:2609.18472, especially Proposition 5.1

**Risks / limits.** The result is only along the actual translation family; it is not a complete fourth-order normal form.

## Originality (O) — PASS

The primary Artstein-Avidan–Fradelizi–Wyczesany paper computes the translated-ball expansion only through second order and uses it to prove instability for \(\sigma^2>2/(n+1)\); at equality that coefficient vanishes and the paper does not compute the quartic term. Earlier SCOPE records compute the full Hessian but explicitly leave the nonlinear behavior of the translation kernel open. A later 2026-09-20 SCOPE record contains the quartic endpoint plus a bifurcation theorem, but it postdates this 2026-09-19 record.

**Sources checked.** full text arXiv:2609.18472 pages containing Proposition 5.1; published SCOPE 2026-09-17 and 2026-09-18 Hessian records; Resultary search for Gaussian Santaló quartic translation

**Risks / limits.** The motivating preprint is recent, so unindexed parallel work remains a residual risk.

## Value (V) — PASS

At the exact Hessian-degeneracy threshold, the sign of the first nonzero term on the only neutral mode is a natural stability question. The explicit negative quartic coefficient resolves that boundary behavior without claiming a global theorem, and directly informs the open phase-transition interval.

**Sources checked.** primary threshold theorem and the earlier full-Hessian SCOPE results

**Risks / limits.** No conclusion is drawn about arbitrary coupled fourth-order perturbations or global maximization.

## Originality comparison

**Equivalent formulations.** The theorem is a fourth-variation statement restricted to the genuine translated-ball branch at the unique degree-one Hessian kernel.

**Broader coverage.** Earlier work covers the quadratic translation threshold and the complete second-variation spectrum, but not the first nonzero term at equality.

**Exact database or table checks.**

- Resultary: Gaussian Santaló volume product translated ball quartic critical variance 2/(n+1) — The audited record ranked first; the closest stronger SCOPE hit is dated 2026-09-20, after this record. 

- published SCOPE archive: Gaussian volume product Hessian translation kernel — The 2026-09-17 and 2026-09-18 records stop at second order and explicitly leave critical nonlinear behavior open.

**Claim versus prior implication.** A vanishing second derivative does not determine the quartic sign; therefore the primary quadratic instability calculation and prior Hessian theorem do not imply the audited endpoint coefficient.

## Source inspections

- Complete arXiv:2609.18472 full text inspected, including Proposition 5.1 and its translated-ball calculation through second order.

- Earlier SCOPE Hessian records inspected in full.

- Assigned package files inspected from the frozen Git tree.

## Residual risks

- Very recent literature may contain unindexed concurrent fourth-order calculations.

## Scope boundary

The theorem treats only genuine translations at the critical variance. It does not prove a complete fourth-order normal form, a topology-uniform local maximum theorem, or the unresolved higher-dimensional global maximization statement.
