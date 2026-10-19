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

# Executable verification of the finite theorem

Use Python 3 with the standard library and a C++17 compiler. From the extracted package directory:

```sh
python3 verification/verify_latin5.py --certificate /tmp/latin5_python.bin > /tmp/latin5_python.json
g++ -O2 -std=c++17 verification/verify_latin5.cpp -o /tmp/latin5_cpp
/tmp/latin5_cpp /tmp/latin5_cpp.bin > /tmp/latin5_cpp.json
cmp /tmp/latin5_python.bin /tmp/latin5_cpp.bin
cmp /tmp/latin5_python.bin certificates/latin5_components.bin
python3 verification/check_structure.py certificates/latin5_components.bin > /tmp/latin5_structure.json
cmp /tmp/latin5_python.json verification/verification_python.json
cmp /tmp/latin5_cpp.json verification/verification_cpp.json
cmp /tmp/latin5_structure.json verification/verification_structure.json
sha256sum certificates/latin5_components.bin
```

The reference SHA-256 is `ce71d8163426d2c0d139614f33225224948d267553e76aa2ff6cda7bc5c556f6` and the byte length is \(4{,}193{,}280\). Binary certificate rows are 26 bytes each: 25 symbols in row-major order and one component tag. The independent generators enumerate two different complete normalizations before generating the same labelled population. They both confirm degree, component and parity counts. The third checker reads the certificate, proves isotopy transitivity for the two reduced-square types, checks all eight component BFS reachabilities and their full distance histograms, and proves vertex transitivity via the row/column/symbol action.

All assertions are *finite*: this is a complete search over all order-five labelled Latin squares, not an extrapolation to other orders. Reproducing the recorded outputs provides a mechanically checkable same-method calculation, not independent external scientific certification. The 2004 primary cycle-switch paper's inaccessible full text is an unresolved literature-completeness limitation.
