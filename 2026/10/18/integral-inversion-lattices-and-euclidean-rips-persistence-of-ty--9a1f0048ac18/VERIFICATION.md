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
# Reproduction and checks

Run the adjacent `verify_type_a_rips.py` using an ordinary Python 3 interpreter and the standard library, with no downloaded data or dependencies. It reconstructs the root coordinate vectors, graph orientation conventions, spanning-tree fundamental cycles, and integer involution matrices from definitions in `RESULT.md`.

For \(n=4,\ldots,12\), exact integer multiplication checks \(\tau^2=1\) and the trace of \(\tau\) equal to one. GF(2) elimination checks that the image rank of \(1+\tau\) is \(n(n-3)/2\). The script checks all small-case squared-distance shells and combinatorial clique conditions for \(n=4,\ldots,7\), and exact signed cellular character traces for every permutation when \(n=4,\ldots,7\).

The successful script terminates with `VERIFY_OK_TYPE_A_EUCLIDEAN_RIPS_INTEGRAL_EIGENLATTICE`. The all-integer \(n\) result depends on the structural proofs of the shell classification, nerve and closure equivalences, and mod-two dimension identity, **not** on a finite-range computational extrapolation. Originality may depend on broader graph-covering literature not accessible in full. Independent scientific audit has not been performed.
