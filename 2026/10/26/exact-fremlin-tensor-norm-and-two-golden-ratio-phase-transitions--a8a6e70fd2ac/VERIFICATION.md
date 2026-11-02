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

Reconstructed finite-dimensional real positive Fremlin primal majorant/positive-contraction dual. For 0≤t≤1 all-ones rank-one majorant and identity contraction give 3. For 1≤t≤sqrt(phi), u=(1,t^-1,t^-2), v=(1,t,t²) majorize M_t at cost 1+t²+t^-2; explicit tridiagonal positive N saturates this and I-N^T N is a nonnegative ground-state sum of two squared differences with coefficients ab and bc. For t≥sqrt(phi), the dual rows split orthogonally into norm-one blocks while hxy^T majorizes M_t exactly at t^4≥t²+1, yielding 2sqrt(1+t²). Explicit one-sided derivatives match at 1,sqrt(phi), second derivatives differ. Independently computed primal dominance and dual spectral norms for 10 representative parameters including both sides of transitions. No general higher-dimensional assertion.

## originality

PASS

Best-of-knowledge comparison by mathematical implication, using actual Resultary search, relevant primary source material, the assigned final claim, and explicit residual priorities. The contribution is limited to the exact special calculation/structural theorem; general underlying methods are credited.

## value

PASS

Natural three-vertex positive path tensor gives a complete continuous-parameter Fremlin projective norm, optimizer changes and two non-C² phase boundaries. The rank-one primal/dual certificates make a useful sharp test case for positive-tensor gauge optimization, not an arbitrary isolated constant or textbook substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
