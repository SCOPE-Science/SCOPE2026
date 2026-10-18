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

For full-support pure-state probability laws, a continuous linear combination of purities has zero variance iff it is constant on every pure state. Product probes fix its constant; a Bell pair on sites j,j+h produces the cut indicator B_h(j,s). The translated h=1 matrix has Fourier multiplier z^(j-k+1)(1+z^k); for 2k<n the h=k+1 multiplier is z^(j-k+1)(1+z^(k+1))*sum(r=0..k-1)z^r. If the first vanishes then z^k=-1, z≠1, the second equals 2z^(j-k+1)≠0. The stacked cut incidence rank is therefore n. If n=2k the only Fourier kernel is the k-dimensional half-shift antisymmetry, equivalent to Schmidt equality P_(s+k)=P_s. Bell probes attain each affine dimension. Independent exact rational SymPy matrix ranks for all n=3..14 and admissible k agree; finite tests cannot replace the all-n Fourier proof.

## originality

PASS

Best-of-knowledge distinct mathematical statement relative to the compared accessible primary results, with explicit access and broad-priority risks.

## value

PASS

Exact affine dimension and ensemble-uniform covariance nullspaces are natural structural invariants for cyclic marginal-purity coordinate measurements and planar-uniform state constraints. The theorem rules out all hidden exact linear redundancies outside balanced complements using a constructive finite set of pure probes. It neither claims independence of random variables nor numerical conditioning or sample-size lower eigenvalue bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
