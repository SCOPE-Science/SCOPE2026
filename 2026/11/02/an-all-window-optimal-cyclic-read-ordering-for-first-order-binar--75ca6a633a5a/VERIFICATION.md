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

# Verification of the coordinate-ordering theorem

The proof establishes the claimed optimum for every integer \(m\ge2\). The finite checks provide independent computational corroboration; they are not used to infer the infinite claim.

Run `python3 verify.py` from the extracted package, using Python 3.8 or newer. The script uses the standard library only. It implements finite-field multiplication from primitive polynomials, evaluates every affine Boolean word directly and separately counts each cyclic window by Boolean OR. It then checks the sharp formula at all widths \(1\le b\le m+1\) for \(m=2,3,4,5,6,7,8\). Higher widths are addressed by the proved monotonicity and absence of \(m+1\) consecutive zeros.

For dimension \(m=3\), the script also enumerates all \(7!=5040\) coordinate permutations with one coordinate anchored, compares maximum minimum distance at all four read widths, and finds exactly \(1680\) rooted orderings attaining the simultaneous optimal profile \((4,6,7,8)\). It checks the complete symbol-pair weight multiplicities for the constructed order at every tested dimension as an additional independent consistency test.

The direct expected profiles for \(m=2,3,4,5,6,7,8\) are respectively \((2,3,4)\); \((4,6,7,8)\); \((8,12,14,15,16)\); \((16,24,28,30,31,32)\); \((32,48,56,60,62,63,64)\); \((64,96,112,120,124,126,127,128)\); and \((128,192,224,240,248,252,254,255,256)\). Successful replay prints `VERIFY_OK`. These bounds, normalization, and branch conditions were also reconstructed from the proof independently of the finite enumeration.

Limits: only dimensions two through eight are computationally enumerated; all larger dimensions are covered by the separate proof. The script does not classify optimal coordinate orders at general dimensions, assess performance under any physical channel model, or establish historical novelty. Independent validation remains unperformed.
