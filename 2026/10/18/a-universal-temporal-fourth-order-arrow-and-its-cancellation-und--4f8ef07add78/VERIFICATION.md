---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the stationary marked Poisson Brownian jump model dX=√(2D)dW between rate-r jumps X→AX with real iid marks and E|A|⁴<1, all λ_j=r(1−E[A^j]) for j=1..4 are positive. Two-sided stochastic convolution gives finite-fourth-moment stationary law v2=2D/λ2,v4=24D²/(λ2 λ4), unique among finite-fourth-moment stationary laws by fourth-power synchronous contraction. Generator identities Lx=−λ1x, Lx³=6Dx−λ3x³ give H(t)=E[X_t³X0]−E[X_t X0³]=[12D²r/(λ2λ4)]E[(1−A)³(1+A)] ∫_0^t exp(−λ1s−λ3(t−s))ds. Integral >0 at every positive t; unique positive maximum at log(λ3/λ1)/(λ3−λ1), continuous at equality. If |A|≤1 almost surely, F>0 under fourth-moment assumption. For P(A=−2)=p,P(A=0)=1−p, p<1/16, exact F=1−28p, so at p=1/28 contrast vanishes yet one-way off-diagonal jumps x→0 with no reverse jump prove nonreversibility. Covariance v2e^(−λ1|t|) matches reversible Gaussian OU. Independently recomputed exact mark-moment identities and all lag signs for p=1/40,1/28,1/20.

## originality

PASS

Random-amplitude and partial resetting, and one-time moments/propagators, are studied previously; the reviewed final claim is an antisymmetric *two-time fourth-order* observable with an all-positive-lag sign law and a signed-overshoot zero/nonreversible witness, not the stationary distribution or autocovariance itself.

## value

PASS

A natural lag-dependent fourth-order statistic detects temporal irreversibility invisible to the entire covariance, and its precise signed-multiplier threshold gives both a robust positive regime and a sharp measurement blind spot. The explicit closed form and maximizing lag are interpretable dynamical invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
