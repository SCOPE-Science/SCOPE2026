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

The standalone `verify.py` uses Python 3 standard library only and directly assembles each finite graph adjacency matrix over the binary field. It computes matrix powers, ranks of the return-minus-identity operators, permutation orders, and explicit configuration orbits.

Execute: `python3 verify.py`. The embedded companion `verification_output.txt` records the exact successful output. Evaluated: 1,200 matrix rank cases across 30 rim lengths and all times through twice the rim length plus five; 21,824 binary configurations for rim lengths three through seven; and 19 direct primitive-orbit comparisons. Every test passed. The computation is finite and does not replace the general algebraic proof.

The proof requires separate treatment of the exceptional primary factor at the polynomial \(x+1\); direct inversion of \(x+x^{-1}\) on that factor would be invalid. The argument uses a Smith reduction and the identity \((A+I)^2=(x+x^{-1})A\), avoiding that division.

No independent audit has been performed.
