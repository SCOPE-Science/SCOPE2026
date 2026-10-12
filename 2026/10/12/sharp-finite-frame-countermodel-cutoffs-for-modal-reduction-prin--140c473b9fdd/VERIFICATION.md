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

# Computational verification

Compile the adjacent `verify.cpp` with any conforming C++17 compiler, for example:

```sh
g++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
./verify
```

Expected result: `VERIFY_OK frames=66066 serial=50978 graph_parameter_tests=4756752 families=4; m=1..6 k=1..12`.

The program enumerates every labeled binary accessibility relation on sets of one through four worlds (including loops), filters serial relations without losing unrestricted ones, constructs Boolean reachability for path lengths up to 18, and checks the asserted universal frame-validation criteria for \(m\) from 1 to 6 and \(k\) from 1 to 12. It checks all four boundary families: unrestricted and serial, predicted-valid and predicted-invalid. This confirms those finite instances only. The proof in `RESULT.md` uses cycle insertion and explicit witnesses for all positive parameters, without depending on the enumeration. No independent audit was performed.
