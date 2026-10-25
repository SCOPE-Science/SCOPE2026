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

# Verification and limits

Run `python3 verify.py` in the same directory as the result. It uses only the standard library. The checker reconstructs compatible pairs from the original four Hamming distances, enumerates all simplices and checks coverage by coordinate squares and local square/edge blocks; independent mod-two boundary elimination then yields these reduced Betti pairs \((eta_2,eta_3)\): \((0,1),(1,6),(7,24),(31,80),(111,240),(351,672)\) for ambient cube dimensions \(4,5,6,7,8,9\). All checks passed when run against the attached script. The universal assertions are established by the written orbit-cover and homotopy-pushout proof, not by finite enumeration. No external independent audit has been performed.
