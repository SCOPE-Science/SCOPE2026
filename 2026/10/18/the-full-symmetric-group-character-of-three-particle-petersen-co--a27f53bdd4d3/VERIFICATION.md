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
# Verification record

Execute `python verify_petersen3.py` next to `petersen3.py`; both files use the standard library only. The exact integer boundary is built from local half-edge differences and fifteen edge variables at weight three, not loaded from an external table.

The executable checks every length-two boundary composition in degree two and three; the chain dimensions \((680,2400,2700,960)\); modular ranks \((679,1715,960)\) over \(\mathbb F_3\) and \(\mathbb F_5\); twelve simple five-cycles spanning six-dimensional graph first homology over \(\mathbb Q\); all \(120\) direct signed basis-chain Euler traces against their independent vertex/edge-cycle generating-function computation; and exact seven-class Specht multiplicities using Murnaghan–Nakayama.

The characteristic-zero homology computation additionally relies on the theoretical rank upper bounds explained in `RESULT.md`: the degree-zero augmentation, injectivity of the highest differential, and a surjective total-motion map onto graph first homology. Finite-field elimination alone does not certify characteristic-zero ranks. Successful program output ends in `VERIFY_OK`.

The verification concerns rational homology of three unordered graph configurations only. Integral torsion and independent scientific validation are not established.
