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
# Reproducibility
Run `python3 verify_cycle6_clique.py` with standard Python 3. The script independently reconstructs all simplices, modular boundary ranks, and signed chain Lefschetz traces for \(m=2,3,4\). On the completed test run it reported

```
m= 2 f= (12, 36, 16) ranks= 11 14 betti= (1, 11, 2) trace_tests= 48
m= 3 f= (18, 81, 54) ranks= 17 38 betti= (1, 26, 16) trace_tests= 108
m= 4 f= (24, 144, 128) ranks= 23 74 betti= (1, 47, 54) trace_tests= 108
C6_CLIQUE_BLOWUP_CHAIN_RANKS_AND_EQUIVARIANT_LEFSCHETZ_OK
```

The modular computations are over \(\mathbb F_{1000003}\); they are finite consistency checks, not a proof of integral torsion claims. The unrestricted integral theorem is proved using a relative exact sequence and the tensor join model. The full rational quotient follows from finite-group averaging, not from numerical extrapolation. Independent external audit: not performed.
