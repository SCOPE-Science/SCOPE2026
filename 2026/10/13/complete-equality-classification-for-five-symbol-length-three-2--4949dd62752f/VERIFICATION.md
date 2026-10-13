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

Run `python3 verify.py` in the directory containing this package. The script uses only the Python standard library.

The verifier reconstructs all \(855\) set partitions of seven labels into at most five blocks. It encodes the \(35\) IPP1 and \(105\) IPP2 conditions from the standard length-three characterization, finds exactly \(210\) coordinate-unordered valid partition triples, directly checks every resulting code with the descendant definition, and quotients the valid triples by all \(7!\) relabelings of the seven codewords. It then recomputes the two representative codes, their Hamming-distance profiles, and their automorphism counts.

A successful replay prints one line beginning `VERIFY_OK`. The reviewed replay reported two equivalence classes, class partition counts \(105\) and \(105\), \(432{,}000\) literal maximum codes, two orbits of size \(216{,}000\), and stabilizer order \(48\) for each class.

The script verifies the equality classification conditioned on seven codewords. The assertion that seven is the maximum is the published Theorem 34 of Tô and Safavi-Naini and is not independently re-derived by the script.
