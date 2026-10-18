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

# Verification of the forcing-polynomial theorem

The standalone `verify.py` enumerates every partial assignment on sixteen finite clique-bouquet instances, with blank and \(q\) labelled-colour states at each vertex. It verifies the properness of the initially coloured vertices, then repeatedly applies the exact local condition that an uncoloured vertex has all but one palette colour represented at its already coloured neighbours. The program tests whether the outcome is a complete proper colouring, counts accepted seeds by domain size, and compares those counts to independently evaluated coefficient formulas. All sixteen tests passed, covering 1,185,610 assignments. The graph families include uniform and nonuniform bouquets and the single-complete-clique boundary.

The proof additionally reconstructs the polynomial by counting unique complete extensions of eligible partial colourings, so correctness is not inferred from a finite sample. The real-root census follows by monotonic intervals and by testing the explicit formal derivative for multiple-root coincidences. No numerical root finder is required for its unrestricted validity. Code uses only the Python standard library; execute `python3 verify.py`. No infinite or external certification is claimed.

Independent audit status: not performed.
