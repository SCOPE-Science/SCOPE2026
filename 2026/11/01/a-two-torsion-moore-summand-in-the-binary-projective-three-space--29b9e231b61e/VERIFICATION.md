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

# Reproducible mathematical checks

Run both commands from the directory containing the associated files:

```
python3 verify_cap.py
python3 verify_modular.py
```

The first program requires `morse_certificate.json`. It reconstructs the fifteen nonzero vectors of \(\mathbb F_2^4\), all thirty-five projective lines, and all \(3048\) cap simplices, then verifies every certificate pair, partition, gradient edge and directed acyclicity. All \(13770\) incidences are checked. It computes the signed integral Morse boundary row, confirms coefficient multiplicities and greatest common divisor two, and prints `VERIFY_OK` on success. The complete observed output is `verification_output.txt`.

The second program independently reconstructs the cap simplices without reading the Morse certificate. It computes exact simplicial boundary ranks over the finite fields of orders two, three and five. Its observed output is `modular_output.txt`, ending `MODULAR_VERIFY_OK`.

The integral homotopy classification rests on the certified acyclic matching, the exact signed Morse differential, and the fact that attaching maps of four-cells to a three-sphere are classified by degree. Field computations are independent cross-checks and alone would not establish the integral answer. The verification is not an independent mathematical audit, and it does not establish publication priority.
