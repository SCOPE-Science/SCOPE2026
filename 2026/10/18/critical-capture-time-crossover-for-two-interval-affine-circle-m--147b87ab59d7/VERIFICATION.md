---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For fixed 0<c<b<1, 0<lambda<1, 1-b<lambda(1-c), and kappa<(1-lambda)/(b-c), exact exterior recurrence u_(k+1)=(1+kappa*delta)u_k-delta(1-kappa(b-c)+kappa*delta) yields the full n-step survivor thresholds h_n and exactly affine uniform microscopic undershoot on nonterminal cells. Their widths are O(delta), with at most one truncated cell. The limiting H_kappa(t)=alpha(1-exp(-kappa*t))/kappa (or t for kappa=0) has positive derivative through 1-b because 1-kappa(1-c)>0. Inversion proves O(delta) uniform time coupling. Left exterior enters within O(1) steps; U<b gives atom b at 0; density alpha exp(-kappa*t) on (0,T_kappa) integrates to 1-b. CDF difference c on (0,delta) yields W1>=c*delta; upper O(delta). Complete-cell independence yields joint weak product limit. Independent exact rational 33-cell tests corroborated the recurrence, not asymptotics.

## originality

PASS

Primary evidence and published-record searches support best-of-knowledge originality of the precisely isolated mathematical contribution, not unconditional priority. The strongest plausible aliases are first passage, capture, survival, renewal-cell and overshoot laws; no inspected statement gives the exact uniform landing-cell law with parameterized scaling. Existing absorption and rotation conclusions do not mathematically entail the full two-scale entrance/undershoot distribution. General Euler methods can give part of the macroscopic limit only after nontrivial specialization.

## value

PASS

The right exterior becomes a continuum of fixed points at delta=0 but has finite capture for each small positive delta. The exact finite survivor partition, critical positive-time density transition between increasing/uniform/decreasing exponentials, sharp Wasserstein error, and microscopic landing-time asymptotic independence reveal transient dynamics erased by conjugation to the invariant interval; nontrivial and naturally motivated beyond eventual absorption.

The dated certificate retains the supplied scientific assessment, sources and limitations.
