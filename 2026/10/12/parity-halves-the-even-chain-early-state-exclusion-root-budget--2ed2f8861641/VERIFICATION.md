---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Imported primary spectral-fusion Remark 4 establishes root order exactly 2n−1 at t=π. With x=cos(t/2), the Chebyshev expansion has only odd indices 2λ_k and nonzero top coefficient, so P is odd of degree 2λ_n. Removing the x^{2n−1} factor leaves an even Q of degree 2λ_n−2n+1. Distinct positive x∈(0,1) roots consume paired degree with negative x at equal multiplicity. Real-analytic variable change has nonzero derivative for t∈(0,π); hence ESE count ≤degQ/2. Independent exact degree tests at n=2,3,4 confirm boundary λ_n=n−1/2 gives zero budget; proof all parameters analytic.

## originality

PASS

The primary 2026 spectral-fusion paper proves the compulsory multiplicity and gives a weaker even-order ESE bound 2λ_n−n. It mentions Chebyshev P(cos(t/2)) but does not exploit oddness of the reduced polynomial to halve positive-root degree. Our scope is the all-n parity-halved bound, not construction or new spectral fusion.

## value

PASS

The ESE event count is a physically motivated control invariant of perfect state transfer; replacing the published bound by roughly half and excluding early return zeros at the minimal reduced endpoint is a meaningful structural spectral improvement, not a tiny numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
