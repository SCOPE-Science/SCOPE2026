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
`artifacts/verify.py` uses only the Python standard library and starts from the exact coefficient string printed in the source.

It reverses that string according to the source's descending-degree convention, generates the full length-\(36\) negacyclic ideal over \(\mathbb Z_4\), and checks its size, \(2\)-torsion size, minimum Lee distance, and complete Lee weight distribution. The verifier applies the standard Gray map to every codeword and checks that the resulting \(4096\)-word binary set equals its \(12\)-dimensional binary span.

The induced negacyclic Gray-coordinate permutation is checked directly to be a single \(72\)-cycle. In that coordinate order the verifier checks cyclic closure, recomputes the polynomial gcd with \(x^{72}+1\), obtains the stored degree-\(60\) generator, and verifies that its \(12\) cyclic shifts generate exactly the Gray image. Finally it constructs a binary generator matrix, rules out dual dependencies of weights below \(4\), and checks an explicit four-column dependency. No floating-point arithmetic, external algebra system, or solver status is used.
