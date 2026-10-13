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

# Reproducible checks and limits

The finite checker is embedded at `artifacts/verify.cpp`. Reproduce with:

```sh
g++ -O2 -std=c++17 artifacts/verify.cpp -o verify
./verify
```

Observed output:

```text
n=1 relations=2 admissible=2 C1=2 exact_condition=2 schema_valid=2 strict=0
n=2 relations=16 admissible=4 C1=16 exact_condition=16 schema_valid=16 strict=0
n=3 relations=512 admissible=8 C1=512 exact_condition=512 schema_valid=512 strict=0
n=4 relations=65536 admissible=14 C1=38416 exact_condition=42448 schema_valid=42448 strict=4032
VERIFY_OK
```

All labeled exact-permission relations of the tested state spaces are traversed; the verification compares the exact frame condition with the all-pairs positive disjunction schema for **every** join-closed atomic valuation on those spaces. The four-point witness is checked explicitly. The 1–3 point enumeration uses chains; every complete join-semilattice with fewer than four points is a chain. The theorem for arbitrary complete join-semilattices is independently established in the accompanying symbolic proof and is not inferred from these finite runs. This is not a formal proof assistant certificate or independent audit.
