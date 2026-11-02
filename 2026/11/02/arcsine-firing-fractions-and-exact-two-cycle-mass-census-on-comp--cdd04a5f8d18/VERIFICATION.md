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

# Reproducibility and limits
The supplied `verify.py` is standalone and uses only Python's standard library. Execute `python verify.py`. The deterministic output is supplied as `verify_output.txt` and starts with `BIPARTITE_TWO_CYCLE_EXACT_OK`.

The checker independently scans all integer configurations inside the invariant confinement box \(0\le x_v\le2\deg(v)-1\) for seven small complete bipartite graphs, including \(K_{3,3}\). It tests \(F^2(x)=x\ne F(x)\) directly, constructs a histogram indexed by conserved mass, and compares this with polynomial (1). Additional integer calculations test all \(1\le a,b\le4\) for polynomial reflection and closed-form counts, and test the complete spectral/phased-state identity for \(1\le n\le14\). The confinement bounds do not omit primitive-two-cycles because every such state has the exact intervals derived in the proof.

The arbitrary-size identities follow from the vertex-interval classification and the polynomial triangularization of the binomial matrix; finite simulation alone does not prove them. The limiting laws use a Gaussian-dominated falling-factorial Riemann sum and a uniform two-binomial local central limit estimate with explicit endpoint domination; they are not inferred from the finite verifier. No independent external audit has been performed.
