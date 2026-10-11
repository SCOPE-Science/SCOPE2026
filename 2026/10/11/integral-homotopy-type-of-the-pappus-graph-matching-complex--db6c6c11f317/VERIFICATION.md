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

# Computational checks

Execute from the directory containing both scripts with Python 3.9 or later:

```
python3 verify_pappus_integral.py
python3 verify_pappus_mod2.py
```

The first script reconstructs the Pappus graph from its LCF rule and enumerates all 35,367 nonempty simplices. It performs a deterministic element-toggle acyclic matching with 17,660 pairs and 47 critical cells, checks every one of the 191,349 directed Hasse incidences by topological sorting, and expands all signed gradient paths needed for the integral cellular differential. Its 43-by-3 matrix is fully specified and checked in the script. The minor in critical-five-cell rows 30, 13 and 27 is \(-I_3\), proving a primitive rank-three image. It prints `VERIFY_OK` only after all checks pass.

The second script enumerates matchings through graph-vertex disjointness using independent recursion and performs exact bit-vector elimination for the \(\mathbb F_2\) simplicial chain complex. It verifies the augmented boundary-rank vector \((1,26,271,1448,4195,6362,4335,984,42)\), reduced degree-five Betti rank 40, and vanishing of all other reduced Betti ranks. It prints `MOD2_VERIFY_OK` after the assertions pass. The mod-two calculation is corroborating evidence only, and cannot independently prove an integral homotopy statement.

The mathematical step beyond the scripts is the dimension-specific fact \(\pi_5(\bigvee^{43}S^5)\cong\mathbb Z^{43}\) and the consequent homotopy cancellation of primitive attaching columns. This establishes the claimed wedge for this graph; no other graph, parameter range, or infinite family is asserted. Independent audit has not been performed.
