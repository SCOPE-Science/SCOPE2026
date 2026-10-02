---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For uniformly randomized two-coordinate exact Gauss--Seidel with bounded independent i.i.d. delay \(D\), \(S_{k+1}=S_k/2+(r^2/2)\mathbb E[S_{k-D}]\), and the asymptotic factor is the unique \(q\in(1/2,1)\) satisfying \(2q-1=r^2\mathbb E[q^{-D}]\), with the stated ordering, extremal, and asymptotic consequences.

## Correctness — PASS

Conditioning on the coordinate and delay gives the scalar second-moment recurrence exactly. Perron--Frobenius gives the unique factor; convexity of \(q^{-D}\) gives stochastic/convex-order comparisons; the deterministic-delay and near-singular formulas follow by direct expansion. The actual verifier was inspected but is only corroboration.

**Checked sources.** assigned RESULT.md; artifacts/verify_delay_rate.py; Carson--Ma 2026 full paper; Beidas--Papavassilopoulos 1993 abstract; Moga--Dubois 1995 report

**Residual risks.** 

## Originality — PASS

The closest current paper gives general max-delay/communication-pattern energy bounds, not an exact full-delay-law second-moment closure. Older stochastic-delay sources establish convergence conditions or broader rate models; the searched material does not give the audited scalar law or its distribution-order consequences.

### Equivalent formulations

An equivalent result would be an exact second-moment companion-root law; none was located.

### Broader coverage

Their broader scope comes with bounds or different state models and does not imply the full exact benchmark.

### Exact database or table

A database/table lookup is inapplicable to the analytic theorem.

### Claim versus prior implication

No inspected prior statement mechanically yields the final claim.

**Checked sources.** https://arxiv.org/abs/2609.15605; https://doi.org/10.1016/0167-8191(93)90038-M; https://ceng.usc.edu/techreports/1995/Dubois%20CENG%2095-06.pdf; Resultary assigned-record hit

**Residual risks.** A specialized corollary may be hidden in the unread 1993 full text.

## Value — PASS

This is a natural exactly solvable asynchronous-solver benchmark that resolves effects of the full delay distribution, including variability at fixed mean, which max-delay bounds cannot express.

**Checked sources.** Carson--Ma 2026; Beidas--Papavassilopoulos 1993; Moga--Dubois 1995

**Residual risks.** It is a benchmark rather than a high-dimensional solver theorem.

## Limitations

- Two coordinates, uniform coordinate choice, exact overwrites, and bounded iterate-independent i.i.d. delays only.
- The recurrence is for a diagonal-scaled mean-square norm.
- The 1993 source was not read in full.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
