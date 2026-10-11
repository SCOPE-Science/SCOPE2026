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
# Reproducible verification

Use Python 3.9 or newer. Both included scripts have no third-party dependencies and can be run separately:

`python3 verify_petersen.py`

`python3 verify_petersen_independent.py`

The first program prints the 15 graph edges, face vector \((15,75,145,90,6)\), matching order, 160 paired simplices, one critical vertex, five critical two-cells and five critical three-cells. Its directed Hasse incidence count is 975; a complete topological sort visits all 331 faces. Its signed Morse boundary is the zero five-by-five integer matrix.

The second program independently constructs the graph as \(\operatorname{KG}(5,2)\), enumerates its matching complex by increasing edge combinations, and computes the complete simplicial boundary ranks modulo each of five primes. All primes yield ranks \((14,61,79,6)\) and reduced Betti numbers \((0,0,5,5,0)\).

Neither an execution log nor a finite-field computation is substituted for the signed integral proof. The primary code's complete acyclicity check, integral elimination algorithm, and the null-attachment argument in `RESULT.md` support the integral homotopy claim. Exhaustiveness is finite and exact, but independent external scientific validation and proof-assistant certification were not performed.
