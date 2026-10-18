---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For odd n>=3, global tensor terms anticommute and square to I, yielding B^2=mI. Local anticommutation implies each local expectation vector has Euclidean norm <=1; generalized Holder gives exact product threshold 1 (attained by generator eigenstates). Measuring B/sqrt(m) gives probabilities p=(1+b/sqrt(m))/2, q<=(1+1/sqrt(m))/2; relative-entropy data processing and d_bin decreasing in q<p yield the claimed bound. Strict binary Pinsker improvement holds for b>1. At m=3,b=sqrt3 the endpoint is 0.237400786151619 nats versus 0.089316397477041 quadratic.

## originality

PASS

Tian 2026 provides the quadratic quantum-Pinsker correlation bound and odd-party three-Pauli example, not the binary-relative-entropy curve. Wehner and Winter 2008 give local anticommuting-observable geometry but not this multipartite information bound. A semantic Resultary query and targeted literature searches did not locate a prior statement of the combined arbitrary-m witness bound. The data-processing step itself is standard and not claimed as new; the explicit spectral collapse/product threshold and quantified improvement are compared as one theorem.

## value

PASS

The bound gives a concrete stronger lower certificate at fixed odd multipartite Clifford witness value, raising the three-Pauli endpoint certificate by >2.6-fold and covering arbitrary generator count m; it addresses a motivated quantitative weakness of the source parity/Pinsker method rather than a random parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
