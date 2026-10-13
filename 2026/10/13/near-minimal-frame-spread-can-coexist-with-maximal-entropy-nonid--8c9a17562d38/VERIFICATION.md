---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The claim is verified analytically from the stated frame normalization and MUB identities.

1. For every normalized rank-one POVM, the Hilbert--Schmidt superoperator trace of \(F_\nu\) is \(d\). The identity direction has eigenvalue \(1\), hence \(\operatorname{Tr}F_{\nu,0}=d-1\). Positivity then gives \(\lambda_{\max}\ge(d-1)/r_\nu\), with equality exactly for a flat nonzero spectrum.

2. For an \(m\)-basis MUB subset, pinching in each basis is the orthogonal projector onto its diagonal operator subspace. Mutual unbiasedness makes the trace-zero parts of these subspaces pairwise orthogonal. Therefore \(F_{\nu_m,0}\) has eigenvalue \(1/m\) with multiplicity \(m(d-1)\) and zero otherwise. This yields \(r_{\nu_m}=m(d-1)\) and \(\kappa_{\nu_m}=(d+1)/m\) exactly.

3. When \(m\le d\), a pure vector from an omitted MUB has probability \(1/(md)\) for every measured outcome, exactly as \(I/d\). The two entropies are \(0\) and \(\log d\). Their common data law gives the lower bound \(\frac14\log^2d\); the constant estimator \((\log d)/2\) attains that bound for every state because entropy lies in \([0,\log d]\).

No finite experiment, numerical optimization, or asymptotic extrapolation is used as proof. The prime-power assumption enters only through existence of a complete \(d+1\)-MUB family. No claim is made for adaptive or collective measurements, or for arbitrary non-informationally-complete POVMs with frame spread near one.
