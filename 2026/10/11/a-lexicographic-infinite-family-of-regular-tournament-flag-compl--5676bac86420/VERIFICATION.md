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

The proof is symbolic. The accompanying `verify.py` supplies independent finite checks at the first two odd parameters. It reconstructs the tournament definition from scratch, enumerates all transitive subtournaments, verifies the exact three-join support condition, verifies regularity and unequal common-outneighbor counts, and recomputes boundary ranks over two fields.

For \(n=5\), the verifier obtains face vector \((15,105,315,450,300,75)\) and Betti vector \((1,1,3,3,0,0)\) over both \(\mathbb F_2\) and \(\mathbb F_3\), exactly matching \(S^1\vee\bigvee^3S^2\vee\bigvee^3S^3\).

The universal quantifier is not inferred from these samples. It follows from the proof's exact block-support decomposition and homotopy-pushout calculation. The computational checks are intended to catch normalization, orientation, and small-case mistakes.
