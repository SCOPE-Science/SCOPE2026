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

# Reproduction of the finite enumeration

Extract `delay_verify.py`, `delay_verify.cpp`, and `catalogue.csv` together. Run the Python program with the desired CSV output filename and compile/run the C++17 program with a different CSV output filename. Confirm both complete CSVs match one another and `catalogue.csv` exactly. The expected full distribution, in order \(\infty,1,2,3,4\), is \(6421,86,5546,3116,456\), totaling \(15625\) necklace choices. The finite cases total \(9204\).

The Python verifier also checks the orbit-size distribution under reversal and complementation: delay one has \(7\) size-two and \(18\) size-four orbits; delay two \(17\) and \(1378\); delay three \(10\) and \(774\); delay four \(0\) and \(114\). Those checks are internal to the finite proof and are not a substitute for the graph equivalence argument explained in RESULT.md.

No evidence is offered for larger block lengths, raw-symbol synchronization times or error correction. This verification is finite and reproducible, not an external or independent certification.
