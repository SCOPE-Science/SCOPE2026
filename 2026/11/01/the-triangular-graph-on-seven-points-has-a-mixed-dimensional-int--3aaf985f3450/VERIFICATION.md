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

Execute `python verify.py` using standard Python 3, no third-party packages. All data are regenerated from the definition of \(T_7\) and the open-neighborhood simplicial condition; there are no input files.

The exact script checks 18,495 augmented simplices and reconstructs 9,121 augmented matching pairs. It topologically sorts the complete reversed-matching Hasse graph with 98,805 incidences on 18,494 ordinary simplices, leaving the critical-cell vector \((1,0,0,246,7)\). The signed integer recursive projection of all seven critical four-simplices is identically zero in 246 coordinates. An independent complete binary Gaussian elimination of all ordinary simplicial boundary matrices gives ranks \((20,190,1000,2534,2646,1764,756,189,21)\) and reduced mod-two ranks 246 and 7.

The integer Morse reduction gives the attaching degrees; the vanishing of those degrees and the Hurewicz isomorphism on a three-sphere wedge imply nullhomotopic four-cell attachments. Finite enumeration is exhaustive for this one graph, and does not establish statements for other sizes. The exact stdout from the packaged script is in `verification_output.txt`.
