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

# Reproduction and limits
Execute `python3 verify_pappus_pm.py` from the directory containing the two supplied evidence files. Only Python 3 standard-library modules are needed. The verifier reconstructs all twenty-seven graph edges from the LCF sequence, enumerates all forty-two perfect matchings, forms all 15,819 nonempty faces, and checks the 7,905 Morse pairs and every one of the 78,921 covering incidences with an exhaustive topological sort. It then obtains the signed integral cellular differentials \(\partial_3=(0,-1,-1,1,0,0)\) and \(\partial_4=0\) by gradient elimination. Independently it computes all mod-two simplicial boundary ranks and all inclusion-minimal nonextendible matchings. All asserted counts and matrices are checked by executable assertions.

The exact expected text is supplied in `verification_output.txt`; replay returned `VERIFY_OK` and reproduced that file byte-for-byte. In the homotopy argument, the primitive degree-one attaching map cancels the unique critical two-cell; the remaining three-skeleton is \(\bigvee^5S^3\), and the zero four-cell boundary gives a nullhomotopic attachment by the Hurewicz isomorphism. This topological argument is necessary beyond computing Betti numbers.

Limitations: this is a computer-reproducible finite exact certificate for a fixed graph, not a general matching-complex classification. No external or independent audit is performed, and searching does not establish global bibliographic uniqueness.
