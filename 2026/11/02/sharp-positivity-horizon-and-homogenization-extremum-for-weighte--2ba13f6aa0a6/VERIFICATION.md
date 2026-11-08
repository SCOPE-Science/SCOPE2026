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

For every star with m>=2 positive spoke conductances, the Schur complement of I+tL has hub inverse diagonal R00=1/(1+sum_i x_i), x_i=tw_i/(1+tw_i), and strictly larger leaf inverse diagonals Rii-R00=sum_{j!=i}x_j/[(1+tw_i)(1+sum x_j)]. Since C(h)=2R-I, off-diagonal entries are nonnegative and positivity is equivalent to sum_i x_i<=1, including equality. Strict monotonicity gives a unique positive t*. Jensen strict concavity at fixed W gives t*>=m/((m-1)W), equality only at uniform weights. On weights (W-(m-1)epsilon,epsilon,...,epsilon), the exact quadratic gives t*~1/sqrt((m-1)W epsilon). Independently verified 9 exact rational resolvent matrices using direct SymPy inversions; inspected original 525-star verifier, which is corroboration, not a universal proof.

## originality

PASS

The generic reversible-Markov resolvent-return criterion and uniqueness are prior work; this complete weighted-star hub ordering, conductance-budget sharp minimizer and singular anisotropy limit were not found stated or implied without additional graph-specific inverse and strict concavity calculations. Qualified best-of-knowledge originality; generic criterion is not new.

## value

PASS

The exact permissible nonnegative Markov step and strict allocation extremum determine a natural positivity invariant for heterogeneous star diffusion. The opposite unbounded boundary behavior is a mathematically meaningful sharp contrast.

The dated certificate retains the supplied scientific assessment, sources and limitations.
