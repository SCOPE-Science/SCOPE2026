# Independent audit — 2026-09-22 campaign

**Source path:** `2026/09/07/024`  
**Audited repository state:** `253a0fe5d0217455660a277f9adb940030e567ad`  
**RESULT.md blob:** `db4f68433f26253f0247fe5a71ea679852b51909`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean verification or expert attestation is claimed.

## Claim audited

A sharp normalized-volume threshold for h*_2 <= 3 h*_1 among reduced reflexive weighted-projective four-simplices: all Q<=377 satisfy the inequality and Q=378 is the first violation.

## Correctness — PASSED

An independent divisor-tuple/age sweep reproduced exactly 136 reduced reflexive rows through Q=377, the two Q=12 equality cases, and the first violation Q=378 at (2,7,54,126,189) with h*=(1,75,226,75,1); the next violation at Q=420 was also reproduced. Independent Ehrhart recounts for witnesses agreed with the age formula. The finite exhaustive claim is therefore reproducible and the scope restriction to weighted-projective simplices is explicit.

## Originality — PASSED

Older reflexive-weight databases and weighted-projective simplex literature contain many of the underlying weight systems, including the relevant sort of reflexive weights, so novelty is not assigned to the existence of the Q=378 weight itself. The audit searched for the specific sharp threshold h*_2 <= 3 h*_1 through normalized volume 377 and did not locate a published theorem/table establishing this threshold or first violation. Relative to the checked sources, the threshold/census statement is a new finite extremal result.

## Scientific value — PASSED

The result gives an exact failure threshold for a concrete coefficient inequality, including equality cases, a first counterexample and a structured family explaining later violations. It provides a reusable finite benchmark for Ehrhart/reflexive-simplex computations and a precise boundary case for conjecture formation, which is sufficient scientific value within its stated finite class.

## Search and independent checks

Independent checks:

- independent exhaustive divisor-tuple/age enumeration through Q=430
- independent Ehrhart recount for equality and violating witnesses
- literature comparison against reflexive weight tables and IDP/unimodality work

Literature/search queries:
- `reflexive weighted projective simplex h2 star 3 h1 threshold`
- `weight (2,7,54,126,189) reflexive simplex`
- `reflexive weight systems dimension 4 h star inequality`

Sources:
- https://arxiv.org/abs/hep-th/0501101
- https://arxiv.org/abs/2103.17156

## Final disposition

**PASSED.** The record remains accepted on all three audited axes.
