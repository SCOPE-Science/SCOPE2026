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

Exact mathematical checks use `verify.py` from the same directory. The code evaluates recursively defined three-move character types for all \(512\) triples with gap lengths at most \(7\). It checks the closed canonical-form criterion in both directions and reproduces the count \(310\), the sharp representative bound \(19\), and its unique normalized extremal triple. Independently coded direct Ehrenfeucht--Fraïssé game tests cover fourteen prescribed equality/inequality boundary pairs. A successful execution ends in `VERIFY_OK`.

For arbitrary gap lengths the reasoning is mathematical, not empirical: the classical rank-three threshold of \(7\) for monochromatic orders and the coloured-word concatenation lemma reduce every input to the finite checked box. The exhaustive routine is the certificate for the remaining finite lemma. The code and the proof do not address arbitrary binary words or quantifier rank greater than three. No independent audit is claimed.
