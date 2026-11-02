---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The q-binomial Newton identity expresses t^rank X as a finite linear combination of indicators of subgroups {X:XU=0}, with coefficients t^(n-j) product_{i<j}(1-q^i t). Character orthogonality yields Fourier eigenvalues lambda_s=sum_{j>=s} [n-s choose j-s]_q q^(m(n-j)) t^(n-j) product_{i<j}(1-q^i t). For 0<=t<q^-(n-1) each eigenvalue is strictly positive, and at q^-k precisely ranks s<=k have positive eigenvalues, giving the exact Gram rank. Outside those points the two top ranks have opposite signs: lambda_n=P(1-q^(n-1)t), lambda_(n-1)=P(1+(q^m-q^(n-1))t). Cases t=0,1, n=2 are included. Independent exact rank-2x2 Fourier characters over F2/F3 and support-boundary examples corroborate the identity; proof is for all fields and m>=n.

## originality

PASS

Best-of-knowledge originality: compared equivalent formulations, stronger-coverage implications, exact tables, and primary literature at their true theorem scopes. No identified inspected source directly states the entire assessed refinement; named inaccessible/implicit-cover risks are retained rather than converted into automatic failure. This does not certify historical priority.

## value

PASS

The complete disconnected PSD region, sharp strict-positive interval, isolated singular supports, and exact finite-field Gram ranks delineate a natural rank-distance kernel usable in coding and harmonic analysis. General Delsarte Fourier machinery does not itself state the parameter frontier; the opposing top-eigenspace sign argument identifies a substantive obstruction to negative type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
