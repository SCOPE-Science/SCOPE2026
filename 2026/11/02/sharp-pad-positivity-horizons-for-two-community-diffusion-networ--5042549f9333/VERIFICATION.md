---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The Laplacian on complete two-community weighted graphs p,q>=2 (internal a,c>=0, cross b>0) decomposes into four commuting projectors with eigenvalues 0, b(p alpha+q), b(q gamma+p), b(p+q). The [2/2] Pade scalar r(s)=(1-s/2+s^2/12)/(1+s/2+s^2/12)>0, r(0)=1. Spectral reconstruction yields strictly positive cross-block and diagonal entries and two within-block offdiagonal rational functions whose quadratic numerators have one positive root if their leading coefficient is negative, none otherwise. This proves all-h entrywise positivity iff alpha<= (p+2q)/q and gamma<=(q+2p)/p, a single interval [0,H] otherwise, critical O(h^-2) decay and H_A~6/(b q epsilon). Positive definiteness does NOT by itself entail entrywise positivity.

## originality

PASS

The complete necessary-and-sufficient all-timestep positivity phase diagram, independent two-community thresholds, exact finite positivity horizon, and critical divergence are not given by the inspected general sufficient time-step criteria for Metzler/Pade schemes. The method uses standard spectral projectors.

## value

PASS

Separating unconditional symmetric positive definiteness from positivity preservation and solving its precise phase boundary in a natural equitable-partition diffusion graph is a useful numerical-analysis classification. Decoupling and no-reentry give robust design information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
