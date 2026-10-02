---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

The Moore--Spiegel oscillator obeys two exact polynomial balance laws that constrain every compact invariant measure, exclude bounded non-equilibrium recurrence for nonpositive T, force positive-parameter recurrence across the nonlinear damping threshold, and imply the sharp period floor 2 pi over square-root T, strict when R is nonzero.

## Correctness — PASS

Direct differentiation independently reproduces both balance identities. Integrating Lie derivatives against compact invariant measures gives the moment laws. For negative T, boundedness and monotonicity yield square-integrability and convergence; at T equal to zero, the second balance plus an exact first integral gives convergence to an equilibrium. For periodic orbits, the first balance, the mean-zero identity for x, and sharp Wirtinger give the period floor; the equality case inserted into the ODE forces R equal to zero.

**Checked sources.** Assigned RESULT.md at tree 02deec3fd5febea177042dc23782ebd8b2af0a39; artifacts/verify_identities.py blob 69615b9cbed8c6197b6e0a74be666da05f8adf42; Balmforth--Craster 1997 full public PDF

**Residual risks.** No global boundedness statement is made.

## Originality — PASS

Prior literature studies periodic, chaotic, averaged, and synchronized Moore--Spiegel dynamics, but no pre-record source located states these exact balances, the nonpositive-T recurrence classification, or the universal sharp period floor. A stronger 2026-09-21 follow-up postdates this record.

### Equivalent formulations

Equivalent invariant-average, coboundary, amplitude-barrier, and periodic-inequality formulations were compared.

### Broader coverage

No inspected broader result implies the full all-measure and all-cycle theorem.

### Exact database or table

Numerical period tables do not imply an all-cycle lower bound.

### Claim versus prior implication

No inspected prior theorem mechanically gives the same conjunction of recurrence and period conclusions.

**Checked sources.** https://doi.org/10.1063/1.166271; Baker--Moore--Spiegel 1971 bibliographic record; published 2026-09-21 follow-up

**Residual risks.** The unread 1971 paper remains the main originality risk.

## Value — PASS

The balances constrain all compact recurrent statistical states, supply a global bounded-recurrence obstruction, and give a sharp parameter-only period lower bound for a classical chaotic oscillator.

**Checked sources.** Balmforth--Craster 1997; historical Moore--Spiegel literature

**Residual risks.** The theorem does not classify positive-parameter attractors or establish cycle existence.

## Limitations

- Invariant-measure statements require compact support.
- The nonpositive-T convergence theorem assumes the forward orbit is bounded.
- The excursion statement assumes R greater than T greater than zero, and the period theorem does not prove cycle existence.
- The full 1971 Baker--Moore--Spiegel paper was unavailable and remains the principal originality risk.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
