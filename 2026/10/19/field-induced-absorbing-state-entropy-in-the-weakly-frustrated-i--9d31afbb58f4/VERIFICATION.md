---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Flips obey Delta_i H=2 s_i F_i with the displayed nearest- and next-nearest-neighbor field. For h<2K, singleton spins strictly lower the energy on flipping, using K<J/2. At the first down spin of a nonsingleton domain, the left two sites are up, so F_i=h-2K for a down dimer and F_i=h otherwise. Thus all down domains must be dimers. An up boundary in that configuration has field h+2K for an up dimer and h otherwise; up interiors are stable. This gives precisely the stated mixed states below 2K, including the period-four restriction at h=0. At h>=2K neither a singleton down spin nor a nonsingleton down boundary is stable, so only the uniform possibilities remain. The all-minus threshold is strict at 2(J-K); the stipulated neutral flips are decisive at both boundaries. Independently checked 192 rational-field direct-energy comparisons for lengths 5–12, three coupling choices, and both threshold equalities, with trace tests. Marking a down-dimer start reduces the count to weak compositions of N-4k into k gaps and gives the N/k multiplier. The trace counts labeled mixed words uniquely and one all-plus loop, with the all-minus contribution added separately. The characteristic polynomial is lambda^4-lambda^3-z^2, and the primitive Perron root gives the entropy and fugacity derivative. The logarithmic generating function near z=1 also gives concentration at the stated limiting density by Chernoff bounds. The displayed decimal approximations are off by roughly 10^(-13); the defining equations are correct. Higher-precision values are lambda≈1.3802775690976141, log(lambda)≈0.3222846159710301, rho≈0.3016746809203983.

## originality

PASS

The same zero-field Hamiltonian has an earlier weak-blocking classification, but its diagnostic allows Delta_i H=0 and its entropy branch differs. The inspected predecessors do not yield the static-field strict phase diagram or the asymmetric dimer-and-gap count. Familiar local-energy, transfer-matrix and blocked-state enumeration tools are not attributed as new.

## value

PASS

For the specified zero-temperature rule, an arbitrarily small uniform field changes a bounded set of strictly absorbing configurations into an exponentially large set. The sharp endpoints and exact weighted enumeration explain which domain boundaries cause the change and quantify its entropy and magnetization without assuming kinetic or equilibrium selection. These are structural statements about a natural model, not a small-volume census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
