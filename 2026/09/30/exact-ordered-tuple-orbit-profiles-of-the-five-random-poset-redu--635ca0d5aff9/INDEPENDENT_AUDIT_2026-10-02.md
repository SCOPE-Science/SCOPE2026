# Independent scientific audit — SCOPE-20260930-635ca0d5aff9

Audited at: 2026-10-02T00:16:07.579488Z

Disposition: **passed**

## Correctness — PASS

Homogeneity identifies \(\operatorname{Aut}(\mathbb P)\)-orbits of injective ordered \(k\)-tuples with labeled \(k\)-element posets, giving \(p_k\). Order duality has exactly one fixed labeled poset, the antichain, so Burnside gives \((p_k+1)/2\) for \(\operatorname{Rev}\). The finite rotation theorem gives, in every rotation class, a unique representative whose sole maximal element is a chosen label; deleting that greatest element bijects rotation classes with labeled posets on \(k-1\) labels, giving \(p_{k-1}\). Modding rotation classes by duality leaves only the antichain class fixed, yielding \((p_{k-1}+1)/2\) for \(\operatorname{Max}\). Equality patterns then give the Stirling transform for all tuples.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify.py
- Pach–Pinsker–Pluhár–Pongrácz–Szabó, arXiv:1111.7109
- Pach–Pinsker–Pongrácz–Szabó, arXiv:1208.3504

### Correctness risks

- The finite verifier checks only low ranks; the general formulas depend on the published finite rotation theorem and its uniqueness statement.

## Originality — PASS

The reduct-classification and rotation papers provide the five groups, rotation equivalence, the three-point characterization, and the unique-maximum representative. Targeted exact-profile searches did not locate the resulting formulas \(p_k,(p_k+1)/2,p_{k-1},(p_{k-1}+1)/2,1\) or the observation that arity three separates all five groups.

### Equivalent formulations

No equivalent orbit-profile theorem was located.

Searches:
- published-corpus query: five reduct groups random partial order exact injective tuple orbit counts \(p_k\) \((p_k+1)/2\) \(p_{k-1}\)
- literature query: random poset reduct oligomorphic orbit profile rotation classes

Evidence:
- The exact corpus hit was the assigned record; nearby results concerned other random structures.
- The primary classification/rotation sources state the structural equivalence relations, not these orbit-count formulas.

### Broader coverage

These results are broader structurally but do not themselves count all finite ordered-tuple orbits for each reduct; the audited bijections and Burnside steps extract new exact profiles.

Searches:
- arXiv:1111.7109
- arXiv:1208.3504

Evidence:
- The first paper classifies the closed supergroups; the second develops rotations and proves the finite local characterization and unique representative with prescribed sole maximum.

### Exact database or table

The formulas are derived for every arity, with small enumerations only as checks.

Searches:
- published-corpus exact query on the five sequences and \(p_{k-1}\) rotation-class count

Evidence:
- No pre-existing orbit-profile table for all five groups was located.

### Claim versus prior implication

Those counting deductions are not stated by the inspected primary theorems and are not merely title/parameter matches.

Searches:
- comparison with the reduct classification and the rotation theorem's unique-maximum and triple-characterization statements

Evidence:
- The Turn formula follows only after using the unique-maximum representative to delete a greatest element; the Max formula further requires identifying the unique dual-fixed rotation class.

### Sources inspected

- **Reducts of the random partial order** — https://arxiv.org/abs/1111.7109. Trigger: Defines and classifies exactly the five closed groups audited. Material read: Primary full-text classification statements and definitions of the five reduct groups. Method: Lawful open primary text. Assessment: COVERING_INGREDIENT. Evidence: It supplies the group classification but not the exact tuple-orbit profiles.
- **A new operation on partially ordered sets** — https://arxiv.org/abs/1208.3504. Trigger: Critical source for finite rotation equivalence. Material read: Primary full-text theorem sections on the three finite rotation classes, local three-point characterization, and the unique rotation-equivalent representative with a prescribed sole maximum. Method: Lawful open primary-text extraction of the relevant theorem sections. Assessment: COVERING_INGREDIENT. Evidence: These theorems justify the rotation counting proof, but the exact five orbit profiles are not stated in the inspected sections.

### Checked sources

- https://arxiv.org/abs/1111.7109
- https://arxiv.org/abs/1208.3504
- https://arxiv.org/abs/1603.00082
- published-result corpus search

### Residual risks

- The relevant rotation theorem sections were inspected directly, but a separately indexed permutation-group paper could have tabulated the same profiles without being found by the targeted searches.

## Value — PASS

Exact orbit profiles are natural invariants of oligomorphic groups. Computing all five reduct profiles and showing that ordered triples already distinguish them gives a compact quantitative complement to the reduct classification.

### Value sources

- arXiv:1111.7109
- arXiv:1208.3504

### Value risks

- The profile uses labeled-poset numbers \(p_k\), so it does not provide closed elementary asymptotics for those numbers.

## Limitations

- The five groups are exactly the published closed reduct groups of the countable random partial order.
- The injective formulas use labeled-poset counts \(p_k\); repetitions are handled by the Stirling transform.
- The finite computational census is corroborative only.
