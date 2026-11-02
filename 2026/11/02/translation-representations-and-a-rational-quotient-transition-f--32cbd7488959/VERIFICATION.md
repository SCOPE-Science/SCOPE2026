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

Use Python 3.10 or newer and run `python verify_affine_translation.py` from the directory containing the script. Only the Python standard library is required. This is a self-contained field, graph, and chain-complex computation.

The checker constructs exact field arithmetic for \(\mathbb F_3\), \(\mathbb F_4\) and \(\mathbb F_5\). It constructs spanning trees and integral fundamental-cycle bases of the incidence graphs; checks every basis cycle has zero integral boundary; transports every cycle under all translations; reconstructs each image exactly in the original integral basis; and verifies every character value. It separately computes the augmentation action on line directions, the tensor-product traces, and exact rational fixed dimensions. It also enumerates the \(q=3\) scale-two Rips faces and computes the boundary ranks modulo \(101\).

Expected final output: `AFFINE_TRANSLATION_INTEGRAL_CYCLES_AND_ALL_ACTIONS_OK`. The observed exact ranks of the quotient top homology over \(\mathbb Q\) are \(0\), \(18\), \(160\) for \(q=3,4,5\). The \(q=3\) face vector is \((21,126,282,255,135,84,36,9,1)\), with Betti vector \((1,0,16,16,0,0,0,0,0)\) over \(\mathbb F_{101}\).

This code does not prove the all-order statement by enumeration. The full proof uses a natural integral Mayer--Vietoris sequence, finite-group character theory, and rational transfer. No independent validation or external audit has been performed.
