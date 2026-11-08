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

Once-subdivided K_{n,n} has 2n+n² vertices with old-old distances 2 or 4, incident old-midpoint distance 1 otherwise 3, and midpoint pairs distance 2 if sharing an endpoint else 4. Mean-zero space decomposes into (n-1)² doubly-centered midpoint modes eigenvalue c-2a, two (n-1)-multiplicity paired standard 2×2 blocks M, and two constant-family contrasts, with a=2^p,b=3^p,c=4^p. At p=beta_n=log2(n/(n-1)), Q_-=0 and all other modes are strictly negative for n>=3; at n=2 there are three zero-mass nulls. The mixed-block determinant bound 2a³>n(b-1)² and strict positivity of b-(1+3h/2+h²/2), h=1/(n-1), certify the critical signs for n>=3; above beta_n the A-vs-B old-vertex contrast gives a positive witness. Schoenberg interval and centered rank yield n²+2n-2 at n>=3 and 4 at n=2. Independently constructed graph shortest paths and computed centered spectra for n=2..7 at, below and above beta_n; these finite probes are not the uniform proof.

## originality

PASS

Bounded original statement-to-statement/implication comparisons found no prior result explicitly establishing the full final claim including its nontrivial exact invariant or sharp all-parameter classification. Does not treat unsuccessful search as priority proof; stated source risks remain, especially the diameter-two QEC general method for record 4.

## value

PASS

Subdividing every edge of a balanced biclique changes both metric scale and vertex population drastically; the exact survival of the original exponent despite n² midpoint constraints, together with sharp exceptional n=2 nullity and expanded Hilbert embedding rank, is a motivated structural graph-metric finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
