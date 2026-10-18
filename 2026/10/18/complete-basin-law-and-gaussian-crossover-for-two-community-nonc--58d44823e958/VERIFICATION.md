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

# Reproduction and scope

Run `python verify_nco_biclique.py` from the directory containing this document. The script requires Python's standard library only. It explicitly evaluates the synchronous spin equation with \(\varepsilon=1/2\) (hence self-weight \(3/2\)) for every binary initial configuration of \(K_{m,n}\) with \(2\le m,n\le7\). All 63,504 states matched the analytically described basins. It also checked exact binomial probability identities for each of the 36 ordered graph sizes at \(p=2/5\), their normalization, and the \(p=1/2\) swapping probability.

The field-sign trichotomy for all \(0<\varepsilon<1\), the exhaustive nine-category phase diagram, the formulas for arbitrary real \(p\in[0,1]\), and the Gaussian asymptotics are analytic proofs in RESULT.md. A finite replay is not a proof of their unbounded quantifiers. The available verification does not establish exhaustive originality against inaccessible specialist literature. No independent audit has been performed.
