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

The accompanying Python 3 checker reconstructs the sixteen radius-two graph balls, all simplices, boundary matrices over the binary field, and complete coefficient supports for degree-four cocycle, degree-four cycle, and degree-five primitive. It tests δa=0, ∂z=0, ⟨a,z⟩=1, and δb=a cup_2 a in every six-simplex coefficient using the standard explicit cup-two formula. It also verifies the resulting square is a cocycle. Run with `python verify_q4_cech_sq2.py`; the executed certificate printed `Q4_CECH_SQ2_CERTIFICATE_OK` and binary Betti ranks one and ten in degrees four and six. The original integral homology computation is separately cited; a direct integer Smith-normal-form proof is not claimed. Independent audit has not been performed.
