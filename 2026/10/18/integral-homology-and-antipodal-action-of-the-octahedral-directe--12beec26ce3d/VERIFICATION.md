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

The scripts `verify_complex.py` and `verify_antipodal.py` regenerate the complete directed-linear-forest complex directly from the ordered-arc definition; no stored face table is trusted. They require Python 3 and only the standard library. Run `python verify_complex.py` and then `python verify_antipodal.py` from this folder.

The first script checks 1,816 nonempty faces, all 6,408 directed face-poset covering relations, an acyclic 843-pair discrete-Morse matching, its integral signed critical differential, a primitive rank-one nonzero boundary, and the vanishing adjacent boundary. A separate original-chain mod-two elimination produces boundary ranks \(23,169,444,208\).

The second script checks the signed antipodal permutation on every simplex, the \((+,-)\) chain counts in dimensions zero through four, and projected boundary ranks modulo \(1009\). Their sums match the rational boundary ranks independently implied by the integral Morse reduction, so these projected ranks are exactly the rational eigenspace ranks rather than only modular lower bounds.

The homotopy type, higher cohomology operations, and remaining octahedral symmetry are not verified or claimed. The accompanying `.out` files record actual executions of the two scripts.
