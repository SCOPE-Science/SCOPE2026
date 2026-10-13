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
# Verification

Run `python3 verify.py` beside `certificate.json`.

The checker reconstructs the condition \(\mu(F)\le3\) independently in two ways. The first enumerates cuts, piece permutations, and a split between permuted pieces exactly as in the definition. The second checks whether a permutation of two, three, or four pieces forms a square whose midpoint is a piece boundary. These predicates agree on every ternary word of length at most \(8\).

The complete avoiding-language census is then obtained independently by full enumeration of all \(3^n\) words and by incremental extension, where only newly created suffix factors need testing. The engines agree on the complete sets at every length \(1\) through \(8\), including the \(18\) maximizers and the empty length-\(8\) layer.

The symmetry computation independently applies all six alphabet permutations and reversal to the maximum layer and verifies three orbits of size \(6\).

No sampling, timeout inference, or finite-to-infinite extrapolation is used. Independent audit has not been performed.
