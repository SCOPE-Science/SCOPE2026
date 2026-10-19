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

# Reproducible finite verification

The provided `witness_certificate.json` gives adjacency information, root-to-every-vertex automorphisms and all required Hamilton path witnesses. Its independent verification needs only Python 3's standard library:

```sh
python3 verify_certificate.py
```

The recorded output is `witness_verification.txt`, terminating with `ALL_VERIFY_OK`. This verifier also enumerates all \(2^{15}\) unused-edge subsets in the Möbius–Kantor obstruction, finds exactly six feasible degree patterns and verifies each disconnects the remaining graph. It computes graph distances to verify the defect signature.

For an independently implemented subset-DP check, use a C++17 compiler:

```sh
g++ -std=c++17 -O3 independent_dp.cpp -o independent_dp
./independent_dp
```

The recorded output is `dp_verification.txt`. It finds zero, one, zero, zero missing endpoint pairs for Heawood, Möbius–Kantor, Pappus and Desargues respectively. Both programs were executed against the actual packaged source and certificate contents and terminated successfully. The generated paths can optionally be regenerated via `python3 generate_certificate.py`, which requires NetworkX; this is not needed for replay. The finite computations are exhaustive only for the displayed graph sizes.
